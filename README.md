# Druk: Mental Wellness Chatbot

Druk is a simple and visually appealing mental wellness chatbot designed to provide empathetic and supportive messages to users. Built using HTML, CSS, and JavaScript, the chatbot leverages the Gemini API for generating content.

## Features

- **User-Friendly Interface**: A clean and calming interface with a galaxy-themed background.
- **Interactive Chat**: Users can type messages and receive supportive responses from Druk.
- **Empathetic Responses**: Druk offers guidance and strategies for mental wellness, avoiding medical advice.
- **Dynamic Conversation**: Maintains a conversation history to provide context-aware responses.

## Getting Started

### Prerequisites

- A web browser to run the chatbot.
- An active API key for the Gemini API.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/druk-chatbot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd druk-chatbot
   ```

3. Open `index.html` in your web browser to run the chatbot.

### Configuration

- Replace the placeholder API key in the `apiKey` variable with your Gemini API key.

```javascript
const apiKey = "YOUR_API_KEY_HERE";
```

## File Structure

- **index.html**: The main HTML structure of the chatbot.
- **druk.css**: Contains the CSS for styling the chatbot interface.

## API Integration

This project uses the [Gemini API](https://generativelanguage.googleapis.com/) for generating empathetic and context-aware responses. Ensure you have an API key and proper access to the API before using the chatbot.

## Usage

1. Type a message into the input field.
2. Click the **Send** button or press **Enter**.
3. View the responses from Druk in the chatbox.

## Customization

- **Styling**: Modify `druk.css` to change the appearance of the chatbot.
- **Response Behavior**: Adjust the chatbot's behavior and tone by modifying the `payload` structure in the `sendMessage` function within `index.html`.

## Demo

![Druk Chatbot]("C:\Users\hp\OneDrive\Pictures\Screenshots\Screenshot 2025-01-26 084700.png")

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve Druk.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Galaxy background by [Freepik](https://www.freepik.com).
- Powered by the Gemini API.
```
