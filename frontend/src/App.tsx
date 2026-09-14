import { useState, useEffect, useRef } from 'react'
import './App.css'

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

interface Message {
  id: string
  role: 'customer' | 'bot' | 'agent' | 'system'
  content: string
  created_at: string
}

function App() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [conversationId, setConversationId] = useState<string | null>(null)
  const [sessionId] = useState(() => localStorage.getItem('prh_session') || crypto.randomUUID())
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    localStorage.setItem('prh_session', sessionId)
  }, [sessionId])

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  // Poll for new bot messages every 3 seconds when we have a conversation
  useEffect(() => {
    if (!conversationId) return

    const interval = setInterval(async () => {
      try {
        const res = await fetch(`${API_BASE}/conversations/${conversationId}/messages`)
        if (res.ok) {
          const data: Message[] = await res.json()
          setMessages(data)
        }
      } catch (e) {
        // ignore polling errors
      }
    }, 3000)

    return () => clearInterval(interval)
  }, [conversationId])

  const sendMessage = async () => {
    const text = input.trim()
    if (!text || loading) return

    setLoading(true)
    setInput('')

    // Optimistic UI
    const tempId = crypto.randomUUID()
    setMessages(prev => [
      ...prev,
      {
        id: tempId,
        role: 'customer',
        content: text,
        created_at: new Date().toISOString(),
      },
    ])

    try {
      const res = await fetch(`${API_BASE}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          content: text,
          session_id: sessionId,
          conversation_id: conversationId,
          client_message_id: tempId,
        }),
      })

      if (!res.ok) throw new Error('Failed to send message')

      const data = await res.json()
      setConversationId(data.conversation_id)

      // Replace temp message with real one
      setMessages(prev => {
        const withoutTemp = prev.filter(m => m.id !== tempId)
        return [
          ...withoutTemp,
          {
            id: data.message.id,
            role: data.message.role,
            content: data.message.content,
            created_at: data.message.created_at,
          },
        ]
      })

      // If the backend already returned a bot reply (future), show it
      if (data.bot_reply) {
        setMessages(prev => [
          ...prev,
          {
            id: crypto.randomUUID(),
            role: 'bot',
            content: data.bot_reply,
            created_at: new Date().toISOString(),
          },
        ])
      }
    } catch (err) {
      console.error(err)
      setMessages(prev => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: 'system',
          content: 'Sorry, something went wrong. Please try again.',
          created_at: new Date().toISOString(),
        },
      ])
    } finally {
      setLoading(false)
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  return (
    <div className="app">
      <header className="header">
        <div className="logo">
          <span className="logo-icon">🏠</span>
          <div>
            <h1>PrimeHomes</h1>
            <p className="tagline">Your AI Real Estate Assistant</p>
          </div>
        </div>
      </header>

      <main className="chat-container">
        <div className="messages">
          {messages.length === 0 && (
            <div className="welcome">
              <div className="welcome-card">
                <h2>Welcome to PrimeHomes 👋</h2>
                <p>
                  Tell me what you&apos;re looking for — a 3-bedroom in Lekki, land in Ibadan,
                  or something to rent in Ikeja. I&apos;ll help qualify your requirements and
                  connect you with our team.
                </p>
                <div className="suggestions">
                  <button onClick={() => setInput("I need a 3-bedroom apartment in Lekki, budget around 80 million")}>
                    3-bed in Lekki
                  </button>
                  <button onClick={() => setInput("Looking for land around Ibadan under 20 million")}>
                    Land in Ibadan
                  </button>
                  <button onClick={() => setInput("I want to rent a 2-bedroom in Ikeja")}>
                    Rent in Ikeja
                  </button>
                </div>
              </div>
            </div>
          )}

          {messages.map((msg) => (
            <div key={msg.id} className={`message ${msg.role}`}>
              <div className="bubble">
                {msg.content}
              </div>
            </div>
          ))}

          {loading && (
            <div className="message bot">
              <div className="bubble typing">
                <span></span><span></span><span></span>
              </div>
            </div>
          )}

          <div ref={bottomRef} />
        </div>

        <div className="input-area">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type your message... (e.g. I need a 3-bedroom in Lekki)"
            rows={1}
            disabled={loading}
          />
          <button
            className="send-btn"
            onClick={sendMessage}
            disabled={loading || !input.trim()}
          >
            {loading ? '...' : 'Send'}
          </button>
        </div>
      </main>

      <footer className="footer">
        <p>PrimeHomes Realty • AI-powered lead assistant</p>
      </footer>
    </div>
  )
}

export default App
