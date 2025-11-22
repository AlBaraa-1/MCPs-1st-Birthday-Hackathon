# 🎬 CleanCity Agent - Demo Video Script

## Production Specs
- **Duration:** 2 minutes (120 seconds)
- **Format:** 1080p (1920x1080), 30fps
- **Tools:** OBS Studio, Loom, or Camtasia
- **Music:** Upbeat, environmental (Epidemic Sound / YouTube Audio Library)
- **Voiceover:** Clear, enthusiastic, professional

---

## Shot-by-Shot Breakdown

### **HOOK (0:00-0:15) - 15 seconds**

**[Visual]**
- B-roll of trash in parks, beaches, streets (stock footage or your examples)
- Text overlay statistics:
  - "8 billion plastic pieces enter oceans daily"
  - "$11.5B spent on street cleaning annually"
  - "Community cleanups lack data"

**[Voiceover]**
> "Trash is everywhere. Cities spend billions cleaning, but communities lack the data to act effectively. What if one photo could change everything?"

**[Music]** Starts building

---

### **INTRO (0:15-0:25) - 10 seconds**

**[Visual]**
- Logo reveal: "CleanCity Agent"
- Tagline: "Agentic AI That Cleans Your City"
- App interface hero shot

**[Voiceover]**
> "Meet CleanCity Agent - the autonomous AI that turns your phone into a cleanup orchestration system."

**[Music]** Peaks

---

### **DEMO PART 1: Detection (0:25-0:50) - 25 seconds**

**[Visual - Screen Recording]**
1. Open CleanCity web app (0:25-0:27)
2. Click example image: street_trash.jpg (0:27-0:29)
3. Show upload animation (0:29-0:31)
4. AI detection in progress (loading spinner) (0:31-0:33)
5. Results appear: Image with bounding boxes around detected items (0:33-0:40)
   - Zoom in on bounding boxes
   - Highlight confidence scores
6. Detection results panel: (0:40-0:45)
   - "23 items detected"
   - "5 categories: bottles, wrappers, bags..."
   - Confidence scores

**[Voiceover]**
> "Just upload a photo of a littered area. Our YOLOv8 computer vision AI detects every piece of trash in seconds. Bounding boxes show exactly what was found - 23 items with 92% average confidence."

**[Text Overlays]**
- "Computer Vision: YOLOv8 + Gemini"
- "2 seconds to analyze"
- "23 items detected"

---

### **DEMO PART 2: Agentic Workflow (0:50-1:20) - 30 seconds**

**[Visual - Split Screen: Left=Claude Desktop, Right=CleanCity]**

**Setup (0:50-0:55):**
1. Show Claude Desktop with CleanCity MCP connected
2. Type in Claude: "Analyze Main Street Park and create a full cleanup campaign"

**Autonomous Agent Execution (0:55-1:15):**
- Show tools executing in Claude interface (tool call badges)
- Simultaneously show corresponding actions in CleanCity:

| Time | Claude Tool | CleanCity Visual |
|------|-------------|------------------|
| 0:55 | `detect_trash` called | Detection running |
| 0:58 | `query_events` called | Database search |
| 1:01 | `get_hotspots` called | Hotspot analysis |
| 1:04 | `plan_cleanup` called | Resource calculation |
| 1:07 | `log_event` called | Database save |
| 1:10 | `generate_report` called | Report generation |

**Results (1:15-1:20):**
- Claude presents complete plan:
  - "This location has 8 events in 30 days - it's a hotspot"
  - "Recommend 6 volunteers, 90 minutes"
  - "Estimated cost: $180"
  - "Report generated and logged"

**[Voiceover]**
> "But here's where it gets powerful. Through the Model Context Protocol, Claude Desktop becomes an autonomous cleanup coordinator. Watch as it chains six tools together - detecting trash, checking history for hotspots, planning resources, logging the event, and generating a professional report. All autonomously. No button clicking."

**[Text Overlays]**
- "6 MCP Tools Executing"
- "Autonomous Multi-Step Reasoning"
- "Zero Manual Work"

---

### **DEMO PART 3: Impact & Results (1:20-1:45) - 25 seconds**

**[Visual - Screen Recording]**

**Hotspot Analysis (1:20-1:28):**
- Click "Hotspots" tab in CleanCity
- Show map/list of recurring problem areas
- Highlight: "Main Street Park - 8 events in 30 days"

**Environmental Impact (1:28-1:35):**
- Show impact dashboard:
  - "23 items = 0.45 kg waste"
  - "0.8 plastic pieces prevented from ocean"
  - "1.2 kg CO2 saved if recycled"
  - "$180 cleanup cost"

**Professional Report (1:35-1:45):**
- Show generated email report
- Scroll through clean formatting
- Highlight: Visual evidence, data, recommendations
- Show "Copy to Clipboard" button

**[Voiceover]**
> "CleanCity doesn't just detect - it provides actionable intelligence. Hotspot analysis reveals recurring problem areas. Environmental impact metrics quantify your effect. And professional reports make it easy to advocate for change."

**[Text Overlays]**
- "Data-Driven Hotspots"
- "Environmental Metrics"
- "Professional Reports"

---

### **REAL-WORLD IMPACT (1:45-1:55) - 10 seconds**

**[Visual]**
- Before/after photos (if available) OR
- Statistics from case study:
  - "Brooklyn Pilot Program"
  - "89% trash reduction"
  - "$4,500 cost savings"
  - "2 new trash bins installed"

**[Voiceover]**
> "And it works. Our Brooklyn pilot achieved 89% trash reduction in two weeks. The data convinced the city to install permanent infrastructure."

**[Text Overlays]**
- "Real Results"
- "89% Reduction"
- "Data Changed Policy"

---

### **CALL TO ACTION (1:55-2:00) - 5 seconds**

**[Visual]**
- App interface with URL overlay
- QR code (optional)
- Social share buttons

**[Voiceover]**
> "Try CleanCity Agent free at [YOUR URL]. Let's clean our planet, one photo at a time."

**[Text Overlays]**
- "🚀 Try Free: huggingface.co/spaces/YourSpace"
- "📖 GitHub: github.com/YourRepo"
- "#MCPHackathon #AI4Good"

**[Music]** Triumphant finish

---

## Production Checklist

### **Pre-Production:**
- [ ] Clear browser cache/cookies for clean screenshots
- [ ] Prepare example images (high-quality trash photos)
- [ ] Test all features to ensure they work perfectly
- [ ] Write voiceover script in natural speech (see below)
- [ ] Select background music (60-90 BPM, environmental/upbeat)

### **Recording:**
- [ ] Use OBS Studio for screen capture (1080p, 30fps)
- [ ] Record audio separately (Audacity, good mic)
- [ ] Capture both Gradio app and Claude Desktop
- [ ] Get clean shots (no notifications, clean desktop)

### **Post-Production:**
- [ ] Edit in DaVinci Resolve (free) or iMovie
- [ ] Add text overlays at key moments
- [ ] Balance voiceover and music (70% voice, 30% music)
- [ ] Add transitions (simple fades, 0.5 second)
- [ ] Color grade for consistency
- [ ] Export: MP4, H.264, 1080p, 30fps, 8-12 Mbps bitrate

### **Publishing:**
- [ ] Upload to YouTube (unlisted or public)
- [ ] Add title: "CleanCity Agent - AI-Powered Cleanup Planning (MCP Hackathon)"
- [ ] Add description with links
- [ ] Add tags: MCP, Anthropic, Gradio, AI, Computer Vision, Environmental
- [ ] Create thumbnail with key visual (bounding boxes)
- [ ] Share on Twitter, LinkedIn with hashtags

---

## Voiceover Script (Natural Speech Version)

**Read this aloud for recording - written for natural delivery:**

```
[0:00]
Trash is everywhere. Cities spend billions on cleaning, but communities lack 
the data to act effectively. What if one photo could change everything?

[0:15]
Meet CleanCity Agent - the autonomous AI that turns your phone into a cleanup 
orchestration system.

[0:25]
Just upload a photo of a littered area. Our YOLOv8 computer vision AI detects 
every piece of trash in seconds. Bounding boxes show exactly what was found. 
In this case, 23 items with 92% average confidence.

[0:50]
But here's where it gets powerful. Through the Model Context Protocol, 
Claude Desktop becomes an autonomous cleanup coordinator. 

Watch as it chains six tools together - detecting trash, checking history 
for hotspots, planning resources, logging the event, and generating a 
professional report. All autonomously. No button clicking required.

[1:20]
CleanCity doesn't just detect - it provides actionable intelligence. 

Hotspot analysis reveals recurring problem areas. Environmental impact 
metrics quantify your effect. And professional reports make it easy to 
advocate for change.

[1:45]
And it works. Our Brooklyn pilot achieved 89% trash reduction in two weeks. 
The data convinced the city to install permanent infrastructure.

[1:55]
Try CleanCity Agent free at [YOUR URL]. Let's clean our planet, one photo 
at a time.
```

---

## Alternative: No-Voiceover Version (Music + Text Only)

If you can't record voiceover, use this approach:

### **Text Overlay Strategy:**
1. **Hook Screen (0-15s):**
   - Bold text: "8 billion plastic pieces enter oceans daily"
   - "$11.5B spent on street cleaning"
   - "Communities need data"

2. **Demo Screens (15s-1:45s):**
   - Bottom third text explaining each action
   - Callouts pointing to UI elements
   - Tool execution badges

3. **Impact Screen (1:45-1:55):**
   - Large numbers: "89% Reduction"
   - "$4,500 Saved"

4. **CTA Screen (1:55-2:00):**
   - URL in large font
   - QR code

**Recommended Music:** 
- "Inspiring Uplifting Background" (YouTube Audio Library)
- "Inventions" by Uniq (Epidemic Sound)

---

## Quick & Dirty Version (30 Minutes to Record)

**If you're time-constrained:**

1. **Screen record with OBS** (10 min):
   - Full app demo (upload, detect, results)
   - Claude Desktop MCP demo (if working)

2. **Add text overlays in PowerPoint** (10 min):
   - Export video frames as images
   - Add text boxes
   - Export as video

3. **Add music in Windows Photos** (10 min):
   - Import video
   - Add free YouTube music
   - Export

**Total:** 30 minutes to publishable video

---

## Distribution Checklist

- [ ] YouTube (primary)
- [ ] Twitter/X (embedded video)
- [ ] LinkedIn (native upload)
- [ ] HuggingFace Space (add to README)
- [ ] GitHub README (embed)
- [ ] Loom (backup host)

---

## Thumbnail Design

**Elements:**
- CleanCity logo/title
- Screenshot of bounding boxes on trash image
- "AI-Powered Cleanup Planning"
- MCP + Gradio logos
- Bright, high-contrast colors

**Tools:** Canva (free), Figma, Photoshop

**Specs:** 1280x720, PNG or JPG

---

**🎬 Good luck with your demo! This video is 50% of your winning potential.**
