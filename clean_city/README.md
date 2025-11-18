---
title: CleanCity Agent - AI Trash Detection & Cleanup Planner
emoji: 🌍
colorFrom: green
colorTo: blue
sdk: gradio
sdk_version: "5.9.1"
app_file: app.py
pinned: false
tags:
- mcp-in-action-track-consumer
- mcp
- anthropic
- computer-vision
- environmental
- gradio-hackathon
- ai-agents
- mcp-server
---

# 🌍 CleanCity Agent

**Autonomous Trash Detection & Cleanup Planner**

> 🏆 **MCP's 1st Birthday Hackathon Submission**  
> **Track:** MCP in Action - Consumer Applications  
> **Tags:** `mcp-in-action-track-consumer`

CleanCity Agent is an AI-powered web application that helps communities identify, track, and clean up littered areas. Upload an image of trash, get instant analysis, receive cleanup recommendations, and track environmental improvements over time.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" alt="Python 3.11+">
  <img src="https://img.shields.io/badge/Gradio-6.0-orange.svg" alt="Gradio">
  <img src="https://img.shields.io/badge/MCP-Enabled-green.svg" alt="MCP">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
</p>

---

## ✨ Features

### 🔍 **Smart Trash Detection**
- Computer vision-powered object detection
- Identifies common litter types: bottles, bags, wrappers, cigarette butts, etc.
- Visual bounding boxes with confidence scores

### 📋 **Intelligent Cleanup Planning**
- Automatic severity assessment (Low/Medium/High)
- Resource estimation (volunteers, time, equipment)
- Environmental impact analysis
- Actionable recommendations

### 📊 **Historical Tracking**
- SQLite database for event logging
- Filter by location, date, severity
- Identify recurring "hotspots"
- Track cleanup progress over time

### 📄 **Report Generation**
- Professional reports for city authorities
- Email-ready templates
- Multiple formats (Email, Markdown, Plain text)
- LLM-enhanced descriptions (optional)

### 💬 **AI Chat Assistant**
- Ask questions about your analysis
- Get cleanup strategy advice
- Understand environmental impact
- Community organizing tips

### 🔌 **MCP Integration**
- Expose tools via Model Context Protocol
- Compatible with Claude Desktop and other MCP clients
- Programmatic access to all features

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **pip** (Python package manager)
- **git** (optional, for cloning)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd track2.1
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows (PowerShell):
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - Windows (Command Prompt):
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment (optional)**
   ```bash
   copy .env.example .env
   # Edit .env with your API keys if using LLM features
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser**
   Navigate to: **http://localhost:7860**

---

## 🎯 User Walkthrough

### Step 1: Upload an Image
- Click the image upload area or use webcam
- Select a photo showing trash in streets, parks, or beaches
- Optionally add location and notes

### Step 2: Analyze
- Click **"Start Analysis"**
- AI detects and highlights trash items
- View detection results with confidence scores

### Step 3: Review Plan
- Get severity assessment (Low/Medium/High)
- See volunteer and time estimates
- Review equipment recommendations
- Understand environmental impact

### Step 4: Save & Track
- Events are saved to history (if enabled)
- View past events in the History tab
- Identify hotspots in the Hotspots tab

### Step 5: Take Action
- Copy the generated email report
- Send to city environmental department
- Share with community cleanup groups
- Organize volunteers and execute cleanup

---

## 🏗️ Architecture

### Project Structure

```
track2.1/
├── app.py                          # Main Gradio UI application
├── mcp_server.py                   # MCP server for tool exposure
├── llm_client.py                   # LLM abstraction layer
├── trash_model.py                  # Trash detection model wrapper
├── agents/
│   └── planner_agent.py            # Cleanup workflow orchestrator
├── tools/
│   ├── trash_detection_tool.py     # Detection MCP tool
│   ├── cleanup_planner_tool.py     # Planning logic
│   ├── history_tool.py             # Event logging & querying
│   └── report_generator_tool.py    # Report generation
├── data/
│   └── trash_events.db             # SQLite database (auto-created)
├── Weights/
│   └── best.pt                     # Model weights (for real model)
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment template
└── README.md                       # This file
```

### Technology Stack

- **Frontend**: Gradio 6.x (web UI framework)
- **AI/ML**: Pluggable detection model (currently mock)
- **MCP**: FastMCP for tool exposure
- **LLM**: Multi-provider support (Anthropic, OpenAI, Gemini)
- **Database**: SQLite (local, file-based)
- **Image Processing**: Pillow (PIL)

---

## 🔧 Configuration

### LLM Providers

CleanCity Agent works **offline by default** with mock responses. To enable real LLM capabilities:

1. Copy `.env.example` to `.env`
2. Set `LLM_PROVIDER` to your preferred provider:
   - `anthropic` - Claude (recommended)
   - `openai` - GPT-4
   - `gemini` - Google Gemini
   - `offline` - Mock responses (no API key needed)

3. Add your API key:
   ```env
   LLM_PROVIDER=anthropic
   ANTHROPIC_API_KEY=sk-ant-your-key-here
   ```

### Trash Detection Model

The current implementation uses a **mock detector** for demonstration. To integrate a real model:

1. **Option A: Use existing weights** (Weights/best.pt)
   - If you have a YOLOv8/YOLOv5 model:
     ```python
     from ultralytics import YOLO
     model = YOLO("Weights/best.pt")
     ```
   - Update `trash_model.py` with real inference code

2. **Option B: Hugging Face model**
   ```python
   from transformers import AutoModelForObjectDetection
   model = AutoModelForObjectDetection.from_pretrained("model-name")
   ```

3. **Option C: External API**
   - Connect to Roboflow, Hugging Face Inference API, etc.

See `trash_model.py` for integration points and TODOs.

---

## 🐳 Deployment

### Local Deployment
Already covered in Quick Start section above.

### Hugging Face Spaces

1. Create a new Space at https://huggingface.co/spaces
2. Select "Gradio" as the SDK
3. Upload all project files
4. Add secrets for API keys in Space settings
5. Space will auto-deploy from `app.py`

### Docker (Manual)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 7860
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t cleancity-agent .
docker run -p 7860:7860 cleancity-agent
```

---

## 🛠️ MCP Server Usage

The MCP server exposes all tools for programmatic access:

### Running the MCP Server

```bash
python mcp_server.py
```

### Available Tools

1. **detect_trash** - Detect trash in images
2. **plan_cleanup** - Generate cleanup plans
3. **log_event** - Save events to database
4. **query_events** - Search historical events
5. **get_hotspots** - Identify recurring problem areas
6. **generate_report** - Create formatted reports
7. **mark_cleaned** - Update event status

### Claude Desktop Integration

Add to your Claude Desktop configuration (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "cleancity": {
      "command": "python",
      "args": ["C:\\path\\to\\track2.1\\mcp_server.py"]
    }
  }
}
```

---

## 📊 Database Schema

SQLite database (`data/trash_events.db`) with the following schema:

```sql
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    location TEXT,
    latitude REAL,
    longitude REAL,
    severity TEXT NOT NULL,
    trash_count INTEGER NOT NULL,
    categories TEXT NOT NULL,  -- JSON array
    detections_json TEXT NOT NULL,  -- JSON array
    notes TEXT,
    image_path TEXT,
    cleaned BOOLEAN DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- **Real trash detection model** integration
- **GPS/mapping** features for hotspot visualization
- **Multi-user support** with authentication
- **Mobile app** wrapper (React Native, Flutter)
- **Gamification** (points, badges for cleanups)
- **Social sharing** features
- **Volunteer coordination** tools

Please open an issue or PR on the repository.

---

## ⚠️ Limitations

- **Mock detection**: Currently uses random detections for demonstration
- **Local storage**: Data stored locally, not synchronized
- **No authentication**: Single-user design
- **Detection accuracy**: Depends on image quality and model training
- **LLM costs**: Using real LLM APIs incurs API charges

This is a **prototype** designed for community groups and individual activists. Production deployment requires additional hardening.

---

## 📜 License

MIT License - see LICENSE file for details.

---

## 🙏 Acknowledgments

- Built with [Gradio](https://gradio.app/)
- Powered by [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- LLM support via Anthropic, OpenAI, and Google
- Inspired by community environmental activists worldwide

---

## 📧 Support

For questions, issues, or feature requests:
- Open an issue on GitHub
- Check the FAQ in the app's "How It Works" tab
- Review the inline code documentation

---

**Let's make our cities cleaner, together! 🌍♻️**
