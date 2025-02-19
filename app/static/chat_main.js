document.addEventListener('DOMContentLoaded', () => {
  const messageForm = document.getElementById('messageForm');
  const messageInput = document.getElementById('messageInput');
  const messagesList = document.getElementById('messagesList');

  const ws = new WebSocket('ws://localhost:8000/ws');

  ws.onopen = () => {
    console.log('Connected to WebSocket server');
  };

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    addMessageToList(data.number, data.message);
  };

  ws.onerror = (error) => {
    console.error('WebSocket error:', error);
  };

  ws.onclose = () => {
    console.log('Disconnected from WebSocket server');
  };

  const addMessageToList = (number, text) => {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message';
    messageDiv.innerHTML = `
      <span class="message-number">${number}.</span>
      <span class="message-text">${text}</span>
    `;
    messagesList.appendChild(messageDiv);
    messagesList.scrollTop = messagesList.scrollHeight;
  };

  messageForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const messageText = messageInput.value.trim();
    if (!messageText) return;

    ws.send(JSON.stringify({
      message: messageText
    }));
    
    messageInput.value = '';
  });  

  messageInput.focus();
});