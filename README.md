# 🎬 Video Crop & Audio Swap Tool (Streamlit + FFmpeg)

A **production-ready Streamlit application** to:
- Upload **two videos** from different platforms
- **Crop front / end / both** with millisecond accuracy
- Replace **dubbed audio** into an **uncensored video**
- Preview videos at every stage
- Keep correct duration & avoid audio/video sync issues

Built for **anime / movie / episode dubbing workflows**.

---

## ✨ Features

✅ Upload **Uncensored (video source)**  
✅ Upload **Dubbed (audio source)**  
✅ Play **original videos**  
✅ Show **exact video duration**  
✅ Crop **front / end / both sides**  
✅ Millisecond precision (`HH:MM:SS.mmm`)  
✅ Prevent FFmpeg **keyframe cut issues**  
✅ Keep cropped video after reruns (session-safe)  
✅ Swap audio with **progress bar**  
✅ Prevent last 10s video loss (audio padding)  
✅ Final video **playable & downloadable**

---

## 🧠 Why this tool exists

Videos from different platforms often:
- Start at different times
- End at different frames
- Have different intros / outros
- Cause audio sync mismatch

This tool solves **all of that in one UI**.

---

## 📦 Requirements

### 1️⃣ Python
Python 3.9+


### 2️⃣ FFmpeg (MANDATORY)

Make sure FFmpeg is installed and available in PATH:

ffmpeg -version
ffprobe -version
👉 If this works, you are good to go.

📥 Installation
git clone https://github.com/your-username/video-crop-audio-swap.git
cd video-crop-audio-swap

python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows

pip install -r requirements.txt
▶️ Run the App
streamlit run app.py
Then open:

http://localhost:8501
⏱ Time Format (VERY IMPORTANT)
All crop times must be in:

HH:MM:SS.mmm
✅ Valid examples
00:05:18.000
00:23:40.085
01:02:03.450
❌ Invalid:

00:00:5:180
✂️ How Cropping Works (With Examples)
🔹 Crop FRONT only
Remove first 5 minutes 18 seconds:

Start: 00:05:18.000
End:   (leave empty)
🎯 Result: Video starts from 00:05:18

🔹 Crop END only
Remove last 0.085 seconds:

Start: 00:00:00.000
End:   00:28:02.805
🎯 Result: Exact duration match

🔹 Crop BOTH (front + end)
Keep middle portion only:

Start: 00:05:18.000
End:   00:23:40.085
🎯 Result: Clean, synced middle section

🔄 Audio Swap Logic (Important)
✔ Video = from Uncensored
✔ Audio = from Dubbed

🛡 Why last 10 seconds were disappearing earlier?
Because FFmpeg’s -shortest flag was cutting video when audio ended.

✅ Fix used in this app:
Audio is padded

Video duration is preserved

No missing frames

📊 File Size Explanation
If:

Uncensored = 265 MB

Dubbed = 77 MB

Final output will be:

≈ 265–275 MB
Why?

Video stream dominates size

Audio size is small

Controlled re-encoding prevents size explosion

🚀 Typical Workflow Example
1️⃣ Upload Uncensored + Dubbed videos
2️⃣ Check video lengths
3️⃣ Crop Uncensored END by exact difference
4️⃣ Click Save Cropped Videos
5️⃣ Preview cropped result
6️⃣ Click Swap Dubbed Audio → Uncensored
7️⃣ Download final synced video

🗂 Output Files (Auto-generated)
temp/
├── unc.mp4               # Original uncensored
├── dub.mp4               # Original dubbed
├── unc_cropped.mp4       # Cropped uncensored
├── dub_cropped.mp4       # Cropped dubbed
├── dub_audio.m4a         # Extracted audio
└── final_output.mp4      # Final result
⚠️ Common Mistakes & Fixes
Issue	Reason	Fix
Duplicate widget error	Missing keys	Keys added
Last 10s video missing	-shortest	Audio padding
Wrong crop duration	Keyframe cut	Smart re-encode
Big file size	CRF too low	CRF 23
🧩 Future Enhancements
🎚 Timeline slider crop

🔊 Audio offset adjust

🧠 Auto duration mismatch fix

📦 Batch episode processing

🎧 Fade-in / fade-out audio

🙌 Credits
Streamlit – UI

FFmpeg – Video processing

Built for anime dubbing & editing workflows

⭐ If this helped you
Give the repo a ⭐ and share it with editors & dubbers 🙂

