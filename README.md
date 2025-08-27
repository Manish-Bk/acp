# Agent Communication Protocol (ACP)

A demonstration project showcasing agent-to-agent communication using the ACP SDK. This project implements two distinct AI agents - a comedian and a poet - that communicate with each other through HTTP-based messaging.

## 🎭 Project Overview

This project consists of:
- **Comedian Agent**: A comedy-focused AI agent that makes jokes and puns
- **Poem Writer Agent**: A poetry-focused AI agent that creates poems about friendship
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
├── acp_client.py              # Client that orchestrates agent communication
├── comedian_server.py         # Comedy agent server (runs on port 8001)
├── poem_writer_server.py      # Poetry agent server (runs on port 8002)
├── requirements.txt           # Python dependencies
├── .env                      # Environment variables (create from .example.env)
├── .example.env              # Example environment variables file
└── README.md                 # This file
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
   
   **Note**: If you're using Windows, you might want to create a virtual environment first:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Copy the example environment file and add your API key:
   ```bash
   copy .example.env .env
   ```
   
   Then edit the `.env` file and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_BASE_URL=your_openai_base_url_here
   ```

## ⚡ Quick Start

1. **Install dependencies** (if not already done):
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your OpenAI API key** in the `.env` file

3. **Start both servers** (in separate terminals):
   ```bash
   # Terminal 1
   python comedian_server.py
   
   # Terminal 2  
   python poem_writer_server.py
   ```

4. **Run the client**:
   ```bash
   python acp_client.py
   ```

## 🚀 Usage

### Starting the Servers

You'll need to run the agent servers in separate terminals:

1. **Start the Comedian Agent Server**:
   ```bash
   python comedian_server.py
   ```
   This starts the comedy agent on `http://localhost:8001`

2. **Start the Poem Writer Agent Server** (in a new terminal):
   ```bash
   python poem_writer_server.py
   ```
   This starts the poetry agent on `http://localhost:8002`

### Running the Client

Once both servers are running, execute the client:

```bash
python acp_client.py
```

## 🎭 How It Works

1. **Client Initialization**: The client creates connections to both agent servers
2. **Comedian Interaction**: Sends "Hello, how are you?" to the comedian agent
3. **Comedian Response**: The comedian agent responds with a joke or humorous comment
4. **Poem Writer Interaction**: Forwards the comedian's response to the poem writer agent
5. **Poem Writer Response**: The poem writer agent creates a poem based on the comedian's message
6. **Output Display**: Both responses are displayed with color coding

### Sample Interaction Flow

```
Client → Comedian Agent: "Hello, how are you?"
Comedian Agent → Client: [Jokes/Puns response]
Client → Poem Writer Agent: [Comedian's response]
Poem Writer Agent → Client: [Friendship poem response]
```

## 🎨 Output Colors

- **Blue**: Comedian agent responses (comedy)
- **Yellow**: Poem writer agent responses (poetry)
- **White**: Reset to default color

## 🔧 Configuration

### Customizing Agent Behavior

You can modify the agent prompts in their respective server files:

- **Comedian Agent**: Edit the prompt in `comedian_server.py` (line 25)
- **Poem Writer Agent**: Edit the prompt in `poem_writer_server.py` (line 25)

### Changing Ports

Default ports can be modified:
- Comedian server: Port 8001 (change in `comedian_server.py`)
- Poem writer server: Port 8002 (change in `poem_writer_server.py`)

Remember to update the client URLs accordingly.

## 📋 Dependencies

- **acp-sdk**: Core ACP communication framework
- **langgraph**: Agent workflow management
- **langchain-openai**: OpenAI model integration
- **crewai**: Additional AI agent capabilities
- **colorama**: Terminal color output (auto-installed with acp-sdk)
- **python-dotenv**: Environment variable management (auto-installed with other packages)

### Checking Server Status

Verify servers are running by checking:
- Comedian server: `http://localhost:8001`
- Poem writer server: `http://localhost:8002`
