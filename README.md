# Canvas‑Pro Workstation 🎨⚡
An advanced, high‑performance multimedia vector design workstation and CAD engineering suite built on a lightweight **HTML5 Canvas Vector Engine** with a **Python Flask** backend.  

This platform bridges the gap between creative vector illustration (Figma/Procreate) and precision industrial schematic blueprints (Altium/AutoCAD), supporting multi‑sheet project tabs, live telemetry, and pixel‑level raster manipulation.

---

## 🚀 Core Workspace Highlights

### 🎨 Creative Illustration & Digital Art Studio
- **Free‑Transform Box Tool (`⛶`)**: Real‑time raycast collision matrix lets you click, drag, shift, and dynamically scale any shape, sticker, or text bounding layer.  
- **Image Layer Stickers**: Import raw image files directly onto the vector canvas layout stack as independent scaling graphic elements.  
- **Velocity Script Calligraphy Brush**: Tracks cursor speed to dynamically scale stroke diameters; moving quickly sweeps thin clean lines, while slowing down pools into heavy ink markers.  
- **Seamless Blending Textures**: Selectable texture profiles (Cloth Fabric, Architectural Brick) that apply complex repeat structures across your freehand lines.  
- **Pixel‑Level Filter Matrix**: Hardware‑accelerated filters (**Invert, Grayscale, Sepia, Pixelate**) that execute directly on image pixel data buffers.  
- **Interactive Live Text Nodes**: Clicking the text tool prompts an on‑canvas boundary field input box to label elements organically.  

### 📐 Precision Engineering CAD Environment
- **Industrial Component Library (`🎛️`)**: Built‑in mathematical vector blueprints for over 16+ categorized logic gates, passive analog devices (resistors, inductors, capacitors), power sources, and multi‑pin embedded microprocessors.  
- **Dynamic RefDes Annotation**: Attribute field to bind active design text descriptions (e.g., `R1 - 10kΩ`, `U1 - 74LS08`) right beneath component boundaries on the fly.  
- **Orthogonal & Isometric 3D Grids**: Toggle layout tracking networks from flat boxes to infinite 30‑degree obliquing grids, perfect for blueprinting hardware casing configurations.  
- **🧲 Intersection Snap‑to‑Grid Matrix**: Forces lines, arrows, shapes, and connection nodes to stick perfectly to the closest junction point, avoiding shaky routing lines.  
- **Live Telemetry Measurement HUD**: Floating dynamic HUD overlay tracks cursor actions to output precise distance layouts (`L: px`) and rotation tracking (`A: °`) in real time.  

### 📑 Project Architecture & Management
- **Multi‑Tab Sheet System**: Dedicated tab bar across the top viewport to create, name, hot‑swap, or delete individual sheets (e.g., separating layout diagrams by sheets) inside a single viewport instance.  
- **Asynchronous Backend Syncing**: Auto‑serializes multi‑page canvas layer arrays into structured JSON configurations directly through the Python Flask server without flattening graphics.  

---

## 🛠️ Project Structure
```text
├── app.py              # Core Python Flask server routing engine
├── saved_canvas.json   # Structural project file save registry (Git ignored)
├── .gitignore          # Keeps junk python cache/local saves out of repository
└── templates/
    └── index.html      # Unified CAD layout & vector computation logic
