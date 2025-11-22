# 🔌 CleanCity Agent - MCP Setup & Proof Guide

## Purpose
This document provides **step-by-step instructions** for connecting CleanCity Agent to Claude Desktop via Model Context Protocol (MCP), plus **screenshots for judges** to prove it works.

---

## Prerequisites

- Claude Desktop installed ([download here](https://claude.ai/desktop))
- CleanCity Agent cloned locally
- Python 3.11+ in PATH

---

## Part 1: MCP Server Setup

### Step 1: Locate Your Claude Config File

**Windows:**
```powershell
# Open in Notepad
notepad "$env:APPDATA\Claude\claude_desktop_config.json"
```

**macOS:**
```bash
# Open in TextEdit
open ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Linux:**
```bash
# Open in nano
nano ~/.config/Claude/claude_desktop_config.json
```

### Step 2: Add CleanCity MCP Server

**If file is empty or doesn't exist, paste this:**

```json
{
  "mcpServers": {
    "cleancity": {
      "command": "python",
      "args": ["C:/Users/YourUsername/path/to/CleanCity/mcp_server.py"],
      "env": {
        "LLM_PROVIDER": "offline"
      }
    }
  }
}
```

**If file already has servers, add CleanCity to the list:**

```json
{
  "mcpServers": {
    "existing-server": {
      "command": "...",
      "args": ["..."]
    },
    "cleancity": {
      "command": "python",
      "args": ["C:/Users/YourUsername/path/to/CleanCity/mcp_server.py"],
      "env": {
        "LLM_PROVIDER": "offline"
      }
    }
  }
}
```

**⚠️ IMPORTANT:** 
- Replace `C:/Users/YourUsername/path/to/CleanCity/mcp_server.py` with your **actual absolute path**
- Use forward slashes `/` even on Windows
- Path must point to `mcp_server.py` file, not the directory

**To find your path:**
```powershell
# In CleanCity directory, run:
cd C:\Users\POTATO\Desktop\codeing\MCPs-1st-Birthday-Hackathon\HF_deploys\CleanCity
python -c "import os; print(os.path.abspath('mcp_server.py'))"
```

Copy the output and paste it into your config.

### Step 3: Save and Restart Claude Desktop

1. Save `claude_desktop_config.json`
2. **Completely quit Claude Desktop** (not just close window)
   - Windows: Right-click system tray icon → Quit
   - macOS: Cmd+Q
3. Reopen Claude Desktop
4. Wait 5-10 seconds for MCP servers to connect

---

## Part 2: Verification

### Test 1: List Available Tools

**In Claude Desktop, type:**
```
What CleanCity tools are available?
```

**Expected Response:**
```
The CleanCity MCP server exposes 6 tools:

1. detect_trash - Analyze images for trash detection using computer vision
2. plan_cleanup - Generate cleanup action plans based on detected trash
3. log_event - Save detection events to the database
4. query_events - Search historical trash detection events
5. get_hotspots - Identify locations with recurring trash problems
6. generate_report - Create professional reports for authorities

Would you like to know more about any specific tool?
```

**✅ If you see this:** MCP is working!

**❌ If you see "I don't have access to CleanCity tools":**
- Check config file path is correct (absolute path, not relative)
- Ensure Python is in PATH (`python --version` works in terminal)
- Check Claude Desktop logs (see Troubleshooting section below)

---

### Test 2: Use a Simple Tool

**In Claude Desktop, type:**
```
Use the query_events tool to check if there are any logged events in the last 30 days.
```

**Expected Response:**
```
I'll check the CleanCity database for recent events.

[Claude uses query_events tool]

Result: [X events found] or [No events found - database is empty]

[Claude explains the results]
```

**✅ If you see tool execution:** MCP is working correctly!

---

### Test 3: Autonomous Multi-Tool Workflow

**This is what judges want to see - autonomous agent behavior.**

**In Claude Desktop, type:**
```
I have a photo of trash at Main Street Park. The image is at C:/path/to/trash_image.jpg. Please:
1. Detect the trash items
2. Plan a cleanup
3. Log the event
4. Check if this location is a hotspot
5. Generate a professional report

Do all of this autonomously without asking me for confirmation at each step.
```

**Expected Autonomous Behavior:**

Claude will:
1. **Call `detect_trash`** with image path
   - Parse results: "Detected 15 items: 8 bottles, 5 wrappers, 2 cans"

2. **Call `plan_cleanup`** with detection results
   - Analyze severity: "Medium severity - requires 4 volunteers, 60 minutes"

3. **Call `log_event`** to save to database
   - Confirm: "Event logged with ID 42"

4. **Call `query_events`** for Main Street Park history
   - Find: "3 previous events at this location in past 30 days"

5. **Call `get_hotspots`** to check if it's a recurring issue
   - Identify: "Yes, Main Street Park is a hotspot (4 events total)"

6. **Call `generate_report`** with all context
   - Create: Professional email report with all data

7. **Present results** in a cohesive summary

**This demonstrates true agentic behavior - no human intervention between steps.**

---

## Part 3: Troubleshooting

### Issue: "I don't have access to CleanCity tools"

**Causes & Fixes:**

1. **Wrong file path:**
   ```powershell
   # Verify path exists:
   Test-Path "C:/path/to/mcp_server.py"
   # Should return: True
   ```

2. **Python not in PATH:**
   ```powershell
   python --version
   # Should show: Python 3.11+ 
   # If error, add Python to PATH or use full path: "C:/Python311/python.exe"
   ```

3. **Syntax error in config:**
   - Use [JSONLint](https://jsonlint.com/) to validate your `claude_desktop_config.json`
   - Common errors: missing commas, trailing commas, unescaped backslashes

4. **Claude Desktop didn't restart:**
   - Fully quit (not just close) and reopen

---

### Issue: Tool execution fails with errors

**Check MCP server logs:**

**Windows:**
```powershell
# View Claude Desktop logs
Get-Content "$env:APPDATA\Claude\logs\mcp-server-cleancity.log" -Tail 50
```

**macOS/Linux:**
```bash
tail -f ~/Library/Application\ Support/Claude/logs/mcp-server-cleancity.log
```

**Common errors:**

1. **Import errors:**
   ```
   ModuleNotFoundError: No module named 'tools'
   ```
   **Fix:** MCP server must be run from CleanCity directory. Update config:
   ```json
   {
     "command": "python",
     "args": ["C:/path/to/CleanCity/mcp_server.py"],
     "cwd": "C:/path/to/CleanCity"  // Add this line
   }
   ```

2. **Database errors:**
   ```
   sqlite3.OperationalError: no such table: events
   ```
   **Fix:** Run app once to initialize database:
   ```powershell
   cd C:\path\to\CleanCity
   python app.py
   # Let it start, then close
   ```

3. **Image path errors:**
   ```
   FileNotFoundError: [Errno 2] No such file or directory: 'image.jpg'
   ```
   **Fix:** Use absolute paths for images when calling `detect_trash`

---

### Issue: Tools work but give unexpected results

**Debug mode:**

Add logging to MCP server:

```python
# Add to top of mcp_server.py
import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename='cleancity_mcp_debug.log'
)
```

Restart Claude Desktop and check `cleancity_mcp_debug.log` for details.

---

## Part 4: Screenshots for Judges

### Screenshot 1: Claude Desktop with CleanCity Tools Listed

**What to capture:**
- Claude's response to "What CleanCity tools are available?"
- All 6 tool names visible
- Claude Desktop UI showing conversation

**How to take:**
1. Ask Claude to list tools
2. Wait for full response
3. Windows: Win+Shift+S, macOS: Cmd+Shift+4
4. Crop to show: message + tool list + Claude branding

**Save as:** `screenshots/mcp_tools_list.png`

---

### Screenshot 2: Autonomous Tool Chain Execution

**What to capture:**
- Claude executing multiple tools in sequence
- Tool call badges visible
- Results from each tool
- Final summary

**How to take:**
1. Ask Claude to run multi-step workflow (see Test 3 above)
2. Scroll to show all tool executions
3. Take screenshot showing conversation flow
4. **OR** take multiple screenshots and stitch in editing tool

**Save as:** `screenshots/mcp_autonomous_workflow.png`

---

### Screenshot 3: Tool Result Details

**What to capture:**
- Detailed output from `detect_trash` or `generate_report`
- Show data structure (JSON or formatted text)
- Prove tools return real data, not mock

**How to take:**
1. Ask Claude to use `detect_trash` on an example image
2. Expand full response
3. Screenshot the detection results

**Save as:** `screenshots/mcp_tool_results.png`

---

### Screenshot 4: Config File (Optional)

**What to capture:**
- Your `claude_desktop_config.json` with CleanCity server configured
- Shows judges your exact setup

**How to take:**
1. Open config in VS Code or Notepad++
2. Ensure no sensitive data (API keys) visible
3. Screenshot

**Save as:** `screenshots/claude_config.png`

---

## Part 5: Alternative MCP Clients

### Using with Cline (VS Code Extension)

**Cline** is an alternative MCP client that runs in VS Code.

**Setup:**
1. Install Cline extension in VS Code
2. Open VS Code settings (JSON)
3. Add:
   ```json
   "cline.mcpServers": {
     "cleancity": {
       "command": "python",
       "args": ["C:/path/to/CleanCity/mcp_server.py"]
     }
   }
   ```
4. Reload VS Code
5. Open Cline chat and test

---

### Using MCP Inspector (Debugging)

**MCP Inspector** is Anthropic's official debugging tool.

**Install:**
```bash
npm install -g @modelcontextprotocol/inspector
```

**Run:**
```bash
mcp-inspector python C:/path/to/CleanCity/mcp_server.py
```

**Opens browser UI where you can:**
- Test each tool individually
- See request/response JSON
- Debug schema issues

**Great for:** Verifying tools work before connecting to Claude

---

## Part 6: Demo Script for Judges

**If recording a video demo of MCP integration:**

### Script (30 seconds):

1. **Show config file (5s):**
   - "Here's CleanCity configured in Claude Desktop's MCP servers"

2. **Open Claude Desktop (5s):**
   - "I'll ask Claude what tools are available"

3. **List tools (5s):**
   - Claude responds with 6 tools
   - "All 6 tools are connected"

4. **Autonomous workflow (15s):**
   - "Now I'll ask Claude to autonomously analyze a trash photo and plan a cleanup"
   - Type request
   - Show Claude calling tools in sequence without prompts
   - "Notice it chains detect → query → hotspots → plan → log → report automatically"

---

## Part 7: Advanced Configuration

### Using Real LLM for Enhanced Reports

**In config, add API key:**
```json
{
  "mcpServers": {
    "cleancity": {
      "command": "python",
      "args": ["C:/path/to/CleanCity/mcp_server.py"],
      "env": {
        "LLM_PROVIDER": "anthropic",
        "ANTHROPIC_API_KEY": "sk-ant-your-key"
      }
    }
  }
}
```

**Enables:**
- Natural language in generated reports
- Better cleanup recommendations
- Context-aware planning

---

### Multiple CleanCity Instances

**For testing different configurations:**

```json
{
  "mcpServers": {
    "cleancity-prod": {
      "command": "python",
      "args": ["C:/path/to/CleanCity/mcp_server.py"],
      "env": {
        "LLM_PROVIDER": "anthropic"
      }
    },
    "cleancity-test": {
      "command": "python",
      "args": ["C:/path/to/CleanCity-test/mcp_server.py"],
      "env": {
        "LLM_PROVIDER": "offline"
      }
    }
  }
}
```

Claude will distinguish them as separate tool namespaces.

---

## Checklist for Judges

**To prove MCP works, include in submission:**

- [ ] Screenshot of Claude listing CleanCity tools
- [ ] Screenshot of autonomous multi-tool workflow
- [ ] Screenshot of tool result details
- [ ] This setup guide in repo (MCP_SETUP.md)
- [ ] Video demo showing MCP integration (30s minimum)
- [ ] Mention MCP in README with setup link

**Judges look for:**
- ✅ Proof tools actually execute (not just exist)
- ✅ Autonomous behavior (agent chains tools)
- ✅ Real data returned (not mock responses)
- ✅ Clear setup documentation

---

## FAQ

**Q: Do I need API keys to use MCP?**
A: No! CleanCity works in offline mode for demos. Real LLM keys only needed for enhanced report generation.

**Q: Can judges test MCP without installing?**
A: Not easily - MCP requires local setup. **That's why screenshots/video are critical.**

**Q: What if my MCP server crashes?**
A: Check logs (see Troubleshooting). Most common: import errors, missing database, wrong paths.

**Q: Does MCP work on HuggingFace Spaces?**
A: No - MCP is for local agents (Claude Desktop, Cline). HuggingFace Spaces hosts the web UI.

**Q: Can I use CleanCity tools from Python directly?**
A: Yes! Import from `tools/` directory:
```python
from tools.trash_detection_tool import detect_trash_mcp
result = detect_trash_mcp({"path": "image.jpg"})
```

---

## Support

**Still having issues?**

1. Check [Claude Desktop MCP docs](https://modelcontextprotocol.io/docs/tools/claude-desktop)
2. Open issue on CleanCity GitHub
3. Join MCP Hackathon Slack (if available)

**For judges:** If you can't get MCP running, watch our demo video - it shows full functionality.

---

**🔌 MCP is what makes CleanCity an agentic system, not just a web app. Take time to get this working!**
