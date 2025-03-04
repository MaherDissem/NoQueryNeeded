import React, { useState, useEffect, useRef } from "react";
import "./static/ChatBot.css";

const ChatBot = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const chatWindowRef = useRef(null);
  const inputRef = useRef(null);

  // Scroll to the latest message
  useEffect(() => {
    if (chatWindowRef.current) {
      chatWindowRef.current.scrollTop = chatWindowRef.current.scrollHeight;
    }
  }, [messages]);

  // Function to send user message to the backend API
  const sendMessageToBot = async (message) => {
    setIsLoading(true);

    try {
        const response = await fetch("http://127.0.0.1:8000/query_db", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                message: message,
                history: messages.filter(msg => msg.text).map(msg => msg.text), // Exclude images from history
            }),
        });

        if (!response.ok) {
            throw new Error("Failed to fetch bot response");
        }

        const data = await response.json();
        
        const botMessages = [];
        if (JSON.parse(data.data).length > 0) {
            botMessages.push({ text: data.sql_response, sender: "bot" });
            botMessages.push({ text: `Query Result: ${JSON.parse(data.data)}`, sender: "bot" });
            botMessages.push({ image: `data:image/png;base64,${data.image}`, sender: "bot" });
        }
        else if (data.intent === "database") {
            botMessages.push({ text: "No data found", sender: "bot" });
        }
        else {
            botMessages.push({ text: data.sql_response, sender: "bot" });
        }

        setMessages((prevMessages) => [...prevMessages, ...botMessages]);
    } catch (error) {
        console.error("Error:", error);
        setMessages((prevMessages) => [
            ...prevMessages,
            { text: "Sorry, something went wrong. Please try again.", sender: "bot" },
        ]);
    } finally {
        setIsLoading(false);
    }
};

  const handleSendMessage = () => {
    if (inputValue.trim() === "") return;

    const newMessage = { text: inputValue, sender: "user" };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    sendMessageToBot(inputValue);
    setInputValue("");

    if (inputRef.current) {
      inputRef.current.focus();
    }
  };

  return (
    <div className="chat-bot">
      <div className="chat-window" ref={chatWindowRef}>
          {messages.map((message, index) => (
              <div key={index} className={`message ${message.sender}`}>
                  {message.text && 
                  <p>
                    {message.sender === "bot" && (
                      <span style={{
                        alignItems: "center",
                        justifyContent: "center",
                        width: "40px",
                        height: "40px",
                        borderRadius: "50%",
                        backgroundColor: "#000", // Black background
                        color: "#fff", // White text color
                        marginRight: "10px",
                        fontSize: "1.5rem",
                      }}>🤖</span>
                    )}
                    {message.text}
                  </p>}
                  {message.image && <img src={message.image} alt="Bot response" 
                    style={{ 
                      maxWidth: "100%", 
                      height: "auto", 
                      borderRadius: "8px",
                      display: "block",
                      margin: "auto"
                  }} 
                />}
              </div>
          ))}
          {isLoading && <div className="message bot"><em>Bot is typing...</em></div>}
      </div>
      <div className="input-area">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
          placeholder="Type a message..."
          disabled={isLoading}
          ref={inputRef}
        />
        <button onClick={handleSendMessage} disabled={isLoading}>
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatBot;