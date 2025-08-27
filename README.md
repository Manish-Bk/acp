# Agent Communication Protocol (ACP)

A demonstration project showcasing agent-to-agent communication using the ACP SDK. This project implements two distinct AI agents - a comedian cat and a poet dog - that communicate with each other through HTTP-based messaging.

## 🐱 Project Overview

This project consists of:
- **Cat Agent**: A comedy-focused AI agent that makes jokes and puns
- **Dog Agent**: A poetry-focused AI agent that creates poems about friendship
- **Client**: Orchestrates communication between the two agents

## 🚀 Features

- **Multi-Agent Communication**: Seamless communication between different AI agents
- **Personality-Driven Responses**: Each agent has distinct personality traits
- **Asynchronous Processing**: Built with async/await for efficient communication
- **Colorful Output**: Color-coded console output for better readability
- **OpenAI Integration**: Powered by GPT-4o model for intelligent responses

## 📁 Project Structure

```
acp/
├── acp_client.py      # Client that orchestrates agent communication
├── cat_server.py      # Comedy agent server (runs on port 8001)
├── dog_server.py      # Poetry agent server (runs on port 8002)
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## 🛠️ Prerequisites

- Python 3.8+
- OpenAI API key
- ACP SDK installed

## 📦 Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd acp
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_BASE_URL=your_openai_base_url_here

## 🚀 Usage

### Starting the Servers

You'll need to run the agent servers in separate terminals:

1. **Start the Cat Agent Server**:
   ```bash
   python cat_server.py
   ```
   This starts the comedy agent on `http://localhost:8001`

2. **Start the Dog Agent Server** (in a new terminal):
   ```bash
   python dog_server.py
   ```
   This starts the poetry agent on `http://localhost:8002`

### Running the Client

Once both servers are running, execute the client:

```bash
python acp_client.py
```

## 🎭 How It Works

1. **Client Initialization**: The client creates connections to both agent servers
2. **Cat Interaction**: Sends "Hello, how are you?" to the cat agent
3. **Cat Response**: The cat agent responds with a joke or humorous comment
4. **Dog Interaction**: Forwards the cat's response to the dog agent
5. **Dog Response**: The dog agent creates a poem based on the cat's message
6. **Output Display**: Both responses are displayed with color coding

### Sample Interaction Flow

```
Client → Cat Agent: "Hello, how are you?"
Cat Agent → Client: [Jokes/Puns response]
Client → Dog Agent: [Cat's response]
Dog Agent → Client: [Friendship poem response]
```

## 🎨 Output Colors

- **Blue**: Cat agent responses (comedy)
- **Yellow**: Dog agent responses (poetry)
- **White**: Reset to default color

## 🔧 Configuration

### Customizing Agent Behavior

You can modify the agent prompts in their respective server files:

- **Cat Agent**: Edit the prompt in `cat_server.py` (line 25)
- **Dog Agent**: Edit the prompt in `dog_server.py` (line 25)

### Changing Ports

Default ports can be modified:
- Cat server: Port 8001 (change in `cat_server.py`)
- Dog server: Port 8002 (change in `dog_server.py`)

Remember to update the client URLs accordingly.

## 📋 Dependencies

- **acp-sdk**: Core ACP communication framework
- **langgraph**: Agent workflow management
- **langchain-openai**: OpenAI model integration
- **colorama**: Terminal color output
- **python-dotenv**: Environment variable management

## 🐛 Troubleshooting

### Common Issues

1. **Connection Refused**: Ensure both agent servers are running before starting the client
2. **API Key Error**: Verify your OpenAI API key is correctly set in the `.env` file
3. **Port Conflicts**: Check if ports 8001 and 8002 are available
4. **Module Import Errors**: Ensure all dependencies are installed via `pip install -r requirements.txt`

### Checking Server Status

Verify servers are running by checking:
- Cat server: `http://localhost:8001`
- Dog server: `http://localhost:8002`

## 🤝 Contributing

Feel free to contribute by:
- Adding new agent personalities
- Implementing additional tools for agents
- Enhancing the communication protocol
- Improving error handling

## 📝 License

[Add your license information here]

## 🙋‍♂️ Support

For questions or issues, please [create an issue](link-to-issues) or contact the development team.

---

**Note**: This project is a demonstration of the ACP SDK capabilities and can be extended to support more complex multi-agent scenarios.

