# # # # import streamlit as st
# # # # import subprocess
# # # # from pathlib import Path

# # # # st.set_page_config(page_title="Audio Swap with Optional Crop", layout="wide")

# # # # TEMP = Path("temp")
# # # # TEMP.mkdir(exist_ok=True)

# # # # st.title("🎬 Video Audio Swap Tool (FFmpeg)")
# # # # st.caption("Crop only ONE video • Preview videos • Swap audio • Play final result")

# # # # # ==========================
# # # # # Upload Section
# # # # # ==========================
# # # # col1, col2 = st.columns(2)

# # # # with col1:
# # # #     unc_video = st.file_uploader(
# # # #         "Upload UNCENSORED Video (Visual Source)",
# # # #         type=["mp4", "mkv", "mov"],
# # # #         key="unc"
# # # #     )

# # # # with col2:
# # # #     dub_video = st.file_uploader(
# # # #         "Upload CENSORED English Dub Video (Audio Source)",
# # # #         type=["mp4", "mkv", "mov"],
# # # #         key="dub"
# # # #     )

# # # # # ==========================
# # # # # Save files & show preview
# # # # # ==========================
# # # # if unc_video and dub_video:

# # # #     unc_path = TEMP / "unc.mp4"
# # # #     dub_path = TEMP / "dub.mp4"

# # # #     unc_path.write_bytes(unc_video.read())
# # # #     dub_path.write_bytes(dub_video.read())

# # # #     col1, col2 = st.columns(2)

# # # #     with col1:
# # # #         st.subheader("🎥 Uncensored Preview")
# # # #         st.video(str(unc_path))

# # # #     with col2:
# # # #         st.subheader("🎧 Dubbed Preview")
# # # #         st.video(str(dub_path))

# # # #     # ==========================
# # # #     # Duration display
# # # #     # ==========================
# # # #     def get_duration(path):
# # # #         cmd = [
# # # #             "ffprobe", "-v", "error",
# # # #             "-show_entries", "format=duration",
# # # #             "-of", "default=noprint_wrappers=1:nokey=1",
# # # #             str(path)
# # # #         ]
# # # #         result = subprocess.run(cmd, capture_output=True, text=True)
# # # #         return round(float(result.stdout.strip()), 2)

# # # #     unc_dur = get_duration(unc_path)
# # # #     dub_dur = get_duration(dub_path)

# # # #     st.info(f"🕒 Uncensored Duration: **{unc_dur} sec** | Dubbed Duration: **{dub_dur} sec**")

# # # #     # ==========================
# # # #     # Crop Selection
# # # #     # ==========================
# # # #     st.subheader("✂️ Cropping Options")

# # # #     crop_choice = st.radio(
# # # #         "Which video do you want to crop?",
# # # #         ["No Cropping", "Crop Uncensored Video", "Crop Dubbed Video"]
# # # #     )

# # # #     start_time = st.text_input("Start Time (HH:MM:SS)", "00:00:00")
# # # #     end_time = st.text_input("End Time (HH:MM:SS)", "00:01:00")

# # # #     # ==========================
# # # #     # Process
# # # #     # ==========================
# # # #     if st.button("🚀 Swap Audio"):

# # # #         final_video = TEMP / "final.mp4"
# # # #         audio_file = TEMP / "dub_audio.m4a"

# # # #         unc_used = unc_path
# # # #         dub_used = dub_path

# # # #         # ---- Cropping Logic ----
# # # #         if crop_choice == "Crop Uncensored Video":
# # # #             st.info("✂️ Cropping uncensored video...")
# # # #             cropped_unc = TEMP / "unc_cropped.mp4"
# # # #             subprocess.run([
# # # #                 "ffmpeg", "-y",
# # # #                 "-i", str(unc_path),
# # # #                 "-ss", start_time,
# # # #                 "-to", end_time,
# # # #                 "-c", "copy",
# # # #                 str(cropped_unc)
# # # #             ], check=True)
# # # #             unc_used = cropped_unc

# # # #         elif crop_choice == "Crop Dubbed Video":
# # # #             st.info("✂️ Cropping dubbed video...")
# # # #             cropped_dub = TEMP / "dub_cropped.mp4"
# # # #             subprocess.run([
# # # #                 "ffmpeg", "-y",
# # # #                 "-i", str(dub_path),
# # # #                 "-ss", start_time,
# # # #                 "-to", end_time,
# # # #                 "-c", "copy",
# # # #                 str(cropped_dub)
# # # #             ], check=True)
# # # #             dub_used = cropped_dub

# # # #         # ---- Extract Audio ----
# # # #         st.info("🔊 Extracting audio...")
# # # #         subprocess.run([
# # # #             "ffmpeg", "-y",
# # # #             "-i", str(dub_used),
# # # #             "-vn",
# # # #             "-acodec", "aac",
# # # #             str(audio_file)
# # # #         ], check=True)

# # # #         # ---- Swap Audio ----
# # # #         st.info("🎬 Swapping audio...")
# # # #         subprocess.run([
# # # #             "ffmpeg", "-y",
# # # #             "-i", str(unc_used),
# # # #             "-i", str(audio_file),
# # # #             "-map", "0:v:0",
# # # #             "-map", "1:a:0",
# # # #             "-c:v", "copy",
# # # #             "-c:a", "aac",
# # # #             str(final_video)
# # # #         ], check=True)

# # # #         st.success("🎉 Audio Swap Completed!")

# # # #         # ==========================
# # # #         # Final Preview & Download
# # # #         # ==========================
# # # #         st.subheader("✅ Final Output Preview")
# # # #         st.video(str(final_video))

# # # #         with open(final_video, "rb") as f:
# # # #             st.download_button(
# # # #                 "⬇️ Download Final Video",
# # # #                 data=f,
# # # #                 file_name="final_audio_swapped.mp4",
# # # #                 mime="video/mp4"
# # # #             )

# # # # else:
# # # #     st.warning("⬆️ Upload both videos to continue")
# # # import streamlit as st
# # # import subprocess
# # # from pathlib import Path

# # # st.set_page_config("Video Audio Swap", layout="wide")

# # # TEMP = Path("temp")
# # # TEMP.mkdir(exist_ok=True)

# # # st.title("🎬 Video Crop + Audio Swap Tool")
# # # st.caption("Millisecond-accurate cropping • FFmpeg based")

# # # # =====================================
# # # # Upload Videos
# # # # =====================================
# # # c1, c2 = st.columns(2)

# # # with c1:
# # #     unc_video = st.file_uploader(
# # #         "Upload UNCENSORED Video (Visual Source)",
# # #         type=["mp4", "mkv", "mov"],
# # #         key="unc"
# # #     )

# # # with c2:
# # #     dub_video = st.file_uploader(
# # #         "Upload DUBBED Video (Audio Source)",
# # #         type=["mp4", "mkv", "mov"],
# # #         key="dub"
# # #     )

# # # if not (unc_video and dub_video):
# # #     st.stop()

# # # unc_path = TEMP / "unc.mp4"
# # # dub_path = TEMP / "dub.mp4"

# # # unc_path.write_bytes(unc_video.read())
# # # dub_path.write_bytes(dub_video.read())

# # # # =====================================
# # # # Preview Videos
# # # # =====================================
# # # st.subheader("🎥 Preview Uploaded Videos")

# # # p1, p2 = st.columns(2)
# # # with p1:
# # #     st.video(str(unc_path))
# # # with p2:
# # #     st.video(str(dub_path))

# # # # =====================================
# # # # Crop Section
# # # # =====================================
# # # st.subheader("✂️ Crop Options (HH:MM:SS.mmm)")

# # # crop_unc = st.checkbox("Crop Uncensored Video")
# # # crop_dub = st.checkbox("Crop Dubbed Video")

# # # cu1, cu2 = st.columns(2)
# # # with cu1:
# # #     unc_start = st.text_input("Uncensored Start", "00:00:00.000")
# # #     unc_end   = st.text_input("Uncensored End",   "")

# # # with cu2:
# # #     dub_start = st.text_input("Dubbed Start", "00:00:00.000")
# # #     dub_end   = st.text_input("Dubbed End",   "")

# # # cropped_unc = TEMP / "unc_cropped.mp4"
# # # cropped_dub = TEMP / "dub_cropped.mp4"

# # # # =====================================
# # # # Crop Button
# # # # =====================================
# # # if st.button("💾 Save Cropped Videos"):

# # #     if crop_unc and unc_end:
# # #         subprocess.run([
# # #             "ffmpeg", "-y",
# # #             "-i", str(unc_path),
# # #             "-ss", unc_start,
# # #             "-to", unc_end,
# # #             "-c", "copy",
# # #             str(cropped_unc)
# # #         ], check=True)
# # #         st.success("✅ Uncensored video cropped & saved")

# # #     if crop_dub and dub_end:
# # #         subprocess.run([
# # #             "ffmpeg", "-y",
# # #             "-i", str(dub_path),
# # #             "-ss", dub_start,
# # #             "-to", dub_end,
# # #             "-c", "copy",
# # #             str(cropped_dub)
# # #         ], check=True)
# # #         st.success("✅ Dubbed video cropped & saved")

# # # # =====================================
# # # # Preview Cropped Videos
# # # # =====================================
# # # st.subheader("👀 Cropped Preview")

# # # pc1, pc2 = st.columns(2)

# # # with pc1:
# # #     if cropped_unc.exists():
# # #         st.video(str(cropped_unc))
# # #     else:
# # #         st.info("No uncensored crop yet")

# # # with pc2:
# # #     if cropped_dub.exists():
# # #         st.video(str(cropped_dub))
# # #     else:
# # #         st.info("No dubbed crop yet")

# # # # =====================================
# # # # Audio Swap
# # # # =====================================
# # # st.subheader("🔄 Swap Audio")

# # # if st.button("🚀 Swap Dubbed Audio → Uncensored"):

# # #     final_video = TEMP / "final_output.mp4"
# # #     audio_file = TEMP / "dub_audio.m4a"

# # #     unc_used = cropped_unc if cropped_unc.exists() else unc_path
# # #     dub_used = cropped_dub if cropped_dub.exists() else dub_path

# # #     # Extract audio from dubbed
# # #     subprocess.run([
# # #         "ffmpeg", "-y",
# # #         "-i", str(dub_used),
# # #         "-vn",
# # #         "-acodec", "aac",
# # #         str(audio_file)
# # #     ], check=True)

# # #     # Replace audio
# # #     subprocess.run([
# # #         "ffmpeg", "-y",
# # #         "-i", str(unc_used),
# # #         "-i", str(audio_file),
# # #         "-map", "0:v:0",
# # #         "-map", "1:a:0",
# # #         "-c:v", "copy",
# # #         "-c:a", "aac",
# # #         "-shortest",
# # #         str(final_video)
# # #     ], check=True)

# # #     st.success("🎉 Audio swapped successfully!")

# # #     st.video(str(final_video))

# # #     with open(final_video, "rb") as f:
# # #         st.download_button(
# # #             "⬇️ Download Final Video",
# # #             f,
# # #             file_name="audio_swapped.mp4",
# # #             mime="video/mp4"
# # #         )
# # import streamlit as st
# # import subprocess
# # from pathlib import Path
# # import re

# # # =========================
# # # Config
# # # =========================
# # st.set_page_config(page_title="Video Crop & Audio Swap", layout="wide")

# # TEMP = Path("temp")
# # TEMP.mkdir(exist_ok=True)

# # # =========================
# # # Helper Functions
# # # =========================

# # def get_duration_seconds(video_path):
# #     cmd = [
# #         "ffprobe", "-v", "error",
# #         "-show_entries", "format=duration",
# #         "-of", "default=noprint_wrappers=1:nokey=1",
# #         str(video_path)
# #     ]
# #     result = subprocess.run(cmd, capture_output=True, text=True)
# #     return round(float(result.stdout.strip()), 3)


# # def sec_to_hms(sec):
# #     h = int(sec // 3600)
# #     m = int((sec % 3600) // 60)
# #     s = sec % 60
# #     return f"{h:02}:{m:02}:{s:06.3f}"


# # def is_valid_time(t):
# #     return re.match(r"^\d{2}:\d{2}:\d{2}(\.\d{1,3})?$", t)

# # # =========================
# # # UI START
# # # =========================

# # st.title("🎬 Video Crop & Audio Swap Tool")
# # st.caption("Millisecond-accurate cropping • Audio replace using FFmpeg")

# # # =========================
# # # Upload Section
# # # =========================

# # c1, c2 = st.columns(2)

# # with c1:
# #     unc_video = st.file_uploader(
# #         "Upload UNCENSORED Video (Visual Source)",
# #         type=["mp4", "mkv", "mov"]
# #     )

# # with c2:
# #     dub_video = st.file_uploader(
# #         "Upload DUBBED Video (Audio Source)",
# #         type=["mp4", "mkv", "mov"]
# #     )

# # if not (unc_video and dub_video):
# #     st.warning("⬆️ Upload both videos to continue")
# #     st.stop()

# # unc_path = TEMP / "unc.mp4"
# # dub_path = TEMP / "dub.mp4"

# # unc_path.write_bytes(unc_video.read())
# # dub_path.write_bytes(dub_video.read())

# # # =========================
# # # Preview Videos
# # # =========================

# # st.subheader("🎥 Original Video Preview")

# # p1, p2 = st.columns(2)
# # with p1:
# #     st.video(str(unc_path))
# # with p2:
# #     st.video(str(dub_path))

# # # =========================
# # # Original Duration
# # # =========================

# # st.subheader("🕒 Original Video Length")

# # unc_len = get_duration_seconds(unc_path)
# # dub_len = get_duration_seconds(dub_path)

# # diff_sec = abs(unc_len - dub_len)
# # longer = "Uncensored" if unc_len > dub_len else "Dubbed"

# # d1, d2, d3 = st.columns(3)

# # with d1:
# #     st.metric("Uncensored", sec_to_hms(unc_len))

# # with d2:
# #     st.metric("Dubbed", sec_to_hms(dub_len))

# # with d3:
# #     st.metric(
# #         "Difference",
# #         sec_to_hms(diff_sec),
# #         help=f"Longer video: {longer}"
# #     )

# # # =========================
# # # Crop Section
# # # =========================

# # st.subheader("✂️ Crop Options")

# # with st.expander("ℹ️ How cropping works (Read this)"):
# #     st.markdown("""
# # ### 🎬 Cropping Explained

# # **Crop FRONT**
# # - Removes everything BEFORE Start time

# # **Crop END**
# # - Removes everything AFTER End time

# # **Crop BOTH**
# # - Keeps content BETWEEN Start & End

# # **Time Format**
# # HH:MM:SS.mmm

# # **FFmpeg Used**

# # ffmpeg -ss START -i input.mp4 -to END -c copy output.mp4

# # """)

# # crop_unc = st.checkbox("Crop Uncensored Video")
# # crop_dub = st.checkbox("Crop Dubbed Video")

# # cu1, cu2 = st.columns(2)

# # with cu1:
# #     st.markdown("#### 🎥 Uncensored Crop")
# #     unc_start = st.text_input("Start", "00:00:00.000", key="unc_s")
# #     unc_end = st.text_input("End", "", key="unc_e")

# # with cu2:
# #     st.markdown("#### 🎧 Dubbed Crop")
# #     dub_start = st.text_input("Start", "00:00:00.000", key="dub_s")
# #     dub_end = st.text_input("End", "", key="dub_e")

# # cropped_unc = TEMP / "unc_cropped.mp4"
# # cropped_dub = TEMP / "dub_cropped.mp4"

# # # =========================
# # # Crop Execution
# # # =========================

# # if st.button("💾 Save Cropped Videos"):

# #     if crop_unc:
# #         if unc_start and not is_valid_time(unc_start):
# #             st.error("❌ Invalid Uncensored START format")
# #             st.stop()
# #         if unc_end and not is_valid_time(unc_end):
# #             st.error("❌ Invalid Uncensored END format")
# #             st.stop()

# #         cmd = ["ffmpeg", "-y"]
# #         if unc_start:
# #             cmd += ["-ss", unc_start]
# #         cmd += ["-i", str(unc_path)]
# #         if unc_end:
# #             cmd += ["-to", unc_end]
# #         cmd += ["-c", "copy", str(cropped_unc)]

# #         subprocess.run(cmd, check=True)
# #         st.success("✅ Uncensored video cropped")

# #     if crop_dub:
# #         if dub_start and not is_valid_time(dub_start):
# #             st.error("❌ Invalid Dubbed START format")
# #             st.stop()
# #         if dub_end and not is_valid_time(dub_end):
# #             st.error("❌ Invalid Dubbed END format")
# #             st.stop()

# #         cmd = ["ffmpeg", "-y"]
# #         if dub_start:
# #             cmd += ["-ss", dub_start]
# #         cmd += ["-i", str(dub_path)]
# #         if dub_end:
# #             cmd += ["-to", dub_end]
# #         cmd += ["-c", "copy", str(cropped_dub)]

# #         subprocess.run(cmd, check=True)
# #         st.success("✅ Dubbed video cropped")

# # # =========================
# # # After Crop Duration
# # # =========================

# # st.subheader("📊 Video Length After Cropping")

# # a1, a2 = st.columns(2)

# # with a1:
# #     if cropped_unc.exists():
# #         new_len = get_duration_seconds(cropped_unc)
# #         st.metric(
# #             "Uncensored (Cropped)",
# #             sec_to_hms(new_len),
# #             delta=f"-{round(unc_len - new_len, 3)} sec"
# #         )
# #         st.video(str(cropped_unc))
# #     else:
# #         st.info("Uncensored not cropped")

# # with a2:
# #     if cropped_dub.exists():
# #         new_len = get_duration_seconds(cropped_dub)
# #         st.metric(
# #             "Dubbed (Cropped)",
# #             sec_to_hms(new_len),
# #             delta=f"-{round(dub_len - new_len, 3)} sec"
# #         )
# #         st.video(str(cropped_dub))
# #     else:
# #         st.info("Dubbed not cropped")

# # # =========================
# # # Audio Swap
# # # =========================

# # st.subheader("🔄 Swap Audio")

# # if st.button("🚀 Swap Dubbed Audio → Uncensored"):

# #     final_video = TEMP / "final_output.mp4"
# #     audio_file = TEMP / "dub_audio.m4a"

# #     unc_used = cropped_unc if cropped_unc.exists() else unc_path
# #     dub_used = cropped_dub if cropped_dub.exists() else dub_path

# #     # Extract audio
# #     subprocess.run([
# #         "ffmpeg", "-y",
# #         "-i", str(dub_used),
# #         "-vn",
# #         "-acodec", "aac",
# #         str(audio_file)
# #     ], check=True)

# #     # Replace audio
# #     subprocess.run([
# #         "ffmpeg", "-y",
# #         "-i", str(unc_used),
# #         "-i", str(audio_file),
# #         "-map", "0:v:0",
# #         "-map", "1:a:0",
# #         "-c:v", "copy",
# #         "-c:a", "aac",
# #         "-shortest",
# #         str(final_video)
# #     ], check=True)

# #     st.success("🎉 Audio swapped successfully!")
# #     st.video(str(final_video))

# #     with open(final_video, "rb") as f:
# #         st.download_button(
# #             "⬇️ Download Final Video",
# #             data=f,
# #             file_name="audio_swapped.mp4",
# #             mime="video/mp4"
# #         )
# import streamlit as st
# import subprocess
# from pathlib import Path
# import re

# # =========================
# # Config
# # =========================
# st.set_page_config(page_title="Video Crop & Audio Swap", layout="wide")

# TEMP = Path("temp")
# TEMP.mkdir(exist_ok=True)

# # =========================
# # Helper Functions
# # =========================

# def get_duration_seconds(video_path):
#     cmd = [
#         "ffprobe", "-v", "error",
#         "-show_entries", "format=duration",
#         "-of", "default=noprint_wrappers=1:nokey=1",
#         str(video_path)
#     ]
#     result = subprocess.run(cmd, capture_output=True, text=True)
#     return round(float(result.stdout.strip()), 3)

# def sec_to_hms(sec):
#     h = int(sec // 3600)
#     m = int((sec % 3600) // 60)
#     s = sec % 60
#     return f"{h:02}:{m:02}:{s:06.3f}"

# def is_valid_time(t):
#     return re.match(r"^\d{2}:\d{2}:\d{2}(\.\d{1,3})?$", t)

# # 🔑 SMART CROP (KEY FIX)
# def smart_crop(input_video, start, end, output_video):
#     """
#     Re-encode to avoid keyframe trimming issues.
#     Guarantees millisecond accuracy.
#     """
#     cmd = ["ffmpeg", "-y"]

#     if start:
#         cmd += ["-ss", start]

#     cmd += ["-i", str(input_video)]

#     if end:
#         cmd += ["-to", end]

#     cmd += [
#         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
#         "-c:a", "aac",
#         str(output_video)
#     ]

#     subprocess.run(cmd, check=True)

# # =========================
# # UI START
# # =========================

# st.title("🎬 Video Crop & Audio Swap Tool")
# st.caption("Millisecond-accurate cropping • Safe audio replacement (FFmpeg)")

# # =========================
# # Upload Section
# # =========================
# c1, c2 = st.columns(2)

# with c1:
#     unc_video = st.file_uploader(
#         "Upload UNCENSORED Video (Visual Source)",
#         type=["mp4", "mkv", "mov"]
#     )

# with c2:
#     dub_video = st.file_uploader(
#         "Upload DUBBED Video (Audio Source)",
#         type=["mp4", "mkv", "mov"]
#     )

# if not (unc_video and dub_video):
#     st.warning("⬆️ Upload both videos to continue")
#     st.stop()

# unc_path = TEMP / "unc.mp4"
# dub_path = TEMP / "dub.mp4"
# unc_path.write_bytes(unc_video.read())
# dub_path.write_bytes(dub_video.read())

# # =========================
# # Preview Videos
# # =========================
# st.subheader("🎥 Original Video Preview")
# p1, p2 = st.columns(2)
# with p1:
#     st.video(str(unc_path))
# with p2:
#     st.video(str(dub_path))

# # =========================
# # Original Duration
# # =========================
# st.subheader("🕒 Original Video Length")

# unc_len = get_duration_seconds(unc_path)
# dub_len = get_duration_seconds(dub_path)
# diff = abs(unc_len - dub_len)

# d1, d2, d3 = st.columns(3)
# with d1:
#     st.metric("Uncensored", sec_to_hms(unc_len))
# with d2:
#     st.metric("Dubbed", sec_to_hms(dub_len))
# with d3:
#     st.metric("Difference", sec_to_hms(diff))

# # =========================
# # Crop Section
# # =========================
# st.subheader("✂️ Crop Options")

# with st.expander("ℹ️ How cropping works"):
#     st.markdown("""
# ### Cropping Modes

# **Front Trim**
# - Set Start time

# **End Trim**
# - Set End time

# **Front + End**
# - Set both

# **Why re-encode?**
# - Stream copy cuts only at keyframes
# - Re-encoding keeps exact milliseconds

# **Time format**
# HH:MM:SS.mmm""")

# crop_unc = st.checkbox("Crop Uncensored Video", key="crop_unc")
# crop_dub = st.checkbox("Crop Dubbed Video", key="crop_dub")

# cu1, cu2 = st.columns(2)

# with cu1:
#     st.markdown("#### 🎥 Uncensored Crop")
#     unc_start = st.text_input(
#         "Start",
#         "00:00:00.000",
#         key="unc_start"
#     )
#     unc_end = st.text_input(
#         "End",
#         "",
#         key="unc_end"
#     )

# with cu2:
#     st.markdown("#### 🎧 Dubbed Crop")
#     dub_start = st.text_input(
#         "Start",
#         "00:00:00.000",
#         key="dub_start"
#     )
#     dub_end = st.text_input(
#         "End",
#         "",
#         key="dub_end"
#     )



# cropped_unc = TEMP / "unc_cropped.mp4"
# cropped_dub = TEMP / "dub_cropped.mp4"

# # =========================
# # Crop Execution
# # =========================
# if st.button("💾 Save Cropped Videos", key="save_crop"):

#     if crop_unc:
#         if not is_valid_time(unc_start):
#             st.error("❌ Invalid Uncensored START format")
#             st.stop()

#         if unc_end.strip() != "" and not is_valid_time(unc_end):
#             st.error("❌ Invalid Uncensored END format")
#             st.stop()

#     if crop_dub:
#         if not is_valid_time(dub_start):
#             st.error("❌ Invalid Dubbed START format")
#             st.stop()

#         if dub_end.strip() != "" and not is_valid_time(dub_end):
#             st.error("❌ Invalid Dubbed END format")
#             st.stop()

#         smart_crop(dub_path, dub_start, dub_end, cropped_dub)
#         st.success("✅ Dubbed video cropped accurately")

# # =========================
# # After Crop Duration
# # =========================
# # st.subheader("📊 Video Length After Cropping")

# # a1, a2 = st.columns(2)

# # with a1:
# #     if cropped_unc.exists():
# #         new_len = get_duration_seconds(cropped_unc)
# #         st.metric("Uncensored (Cropped)", sec_to_hms(new_len),
# #                   delta=f"-{round(unc_len - new_len, 3)} sec")
# #         st.video(str(cropped_unc))
# #     else:
# #         st.info("Uncensored not cropped")

# # with a2:
# #     if cropped_dub.exists():
# #         new_len = get_duration_seconds(cropped_dub)
# #         st.metric("Dubbed (Cropped)", sec_to_hms(new_len),
# #                   delta=f"-{round(dub_len - new_len, 3)} sec")
# #         st.video(str(cropped_dub))
# #     else:
# #         st.info("Dubbed not cropped")

# # # =========================
# # # Audio Swap with Progress
# # # =========================
# # st.subheader("🔄 Swap Audio")

# # if st.button("🚀 Swap Dubbed Audio → Uncensored", key="swap_audio"):

# #     progress = st.progress(0)
# #     status = st.empty()

# #     final_video = TEMP / "final_output.mp4"
# #     audio_file = TEMP / "dub_audio.m4a"

# #     unc_used = cropped_unc if cropped_unc.exists() else unc_path
# #     dub_used = cropped_dub if cropped_dub.exists() else dub_path

# #     status.info("🔊 Extracting audio from dubbed video…")
# #     progress.progress(30)

# #     subprocess.run([
# #         "ffmpeg", "-y",
# #         "-i", str(dub_used),
# #         "-vn",
# #         "-c:a", "aac",
# #         str(audio_file)
# #     ], check=True)

# #     status.info("🎬 Swapping audio into uncensored video…")
# #     progress.progress(70)

# #     subprocess.run([
# #         "ffmpeg", "-y",
# #         "-i", str(unc_used),
# #         "-i", str(audio_file),
# #         "-map", "0:v:0",
# #         "-map", "1:a:0",
# #         "-c:v", "copy",
# #         "-c:a", "aac",
# #         "-shortest",
# #         str(final_video)
# #     ], check=True)

# #     progress.progress(100)
# #     status.success("✅ Audio swap completed!")

# #     st.video(str(final_video))
# #     with open(final_video, "rb") as f:
# #         st.download_button(
# #             "⬇️ Download Final Video",
# #             data=f,
# #             file_name="audio_swapped.mp4",
# #             mime="video/mp4"
# #         )
# st.subheader("📊 Video Length After Cropping")

# a1, a2 = st.columns(2)

# with a1:
#     if st.session_state.use_cropped_unc and cropped_unc.exists():
#         new_len = get_duration_seconds(cropped_unc)
#         st.metric(
#             "Uncensored (Cropped)",
#             sec_to_hms(new_len),
#             delta=f"-{round(unc_len - new_len, 3)} sec"
#         )
#         st.video(str(cropped_unc))
#     else:
#         st.info("Uncensored not cropped")

# with a2:
#     if st.session_state.use_cropped_dub and cropped_dub.exists():
#         new_len = get_duration_seconds(cropped_dub)
#         st.metric(
#             "Dubbed (Cropped)",
#             sec_to_hms(new_len),
#             delta=f"-{round(dub_len - new_len, 3)} sec"
#         )
#         st.video(str(cropped_dub))
#     else:
#         st.info("Dubbed not cropped")

# # =========================
# # Audio Swap with Progress
# # =========================

# st.subheader("🔄 Swap Audio")

# if st.button("🚀 Swap Dubbed Audio → Uncensored", key="swap_audio"):

#     progress = st.progress(0)
#     status = st.empty()

#     final_video = TEMP / "final_output.mp4"
#     audio_file = TEMP / "dub_audio.m4a"

#     unc_used = cropped_unc if st.session_state.use_cropped_unc else unc_path
#     dub_used = cropped_dub if st.session_state.use_cropped_dub else dub_path

#     status.info("🔊 Extracting audio from dubbed video…")
#     progress.progress(30)

#     subprocess.run([
#         "ffmpeg", "-y",
#         "-i", str(dub_used),
#         "-vn",
#         "-c:a", "aac",
#         str(audio_file)
#     ], check=True)

#     status.info("🎬 Swapping audio into uncensored video…")
#     progress.progress(70)

#     subprocess.run([
#         "ffmpeg", "-y",
#         "-i", str(unc_used),
#         "-i", str(audio_file),
#         "-map", "0:v:0",
#         "-map", "1:a:0",
#         "-c:v", "copy",
#         "-c:a", "aac",
#         "-shortest",
#         str(final_video)
#     ], check=True)

#     progress.progress(100)
#     status.success("✅ Audio swap completed!")

#     st.video(str(final_video))

#     with open(final_video, "rb") as f:
#         st.download_button(
#             "⬇️ Download Final Video",
#             data=f,
#             file_name="audio_swapped.mp4",
#             mime="video/mp4"
#         )
import streamlit as st
import subprocess
from pathlib import Path
import re

# =========================
# Page Config
# =========================
st.set_page_config(page_title="Video Crop & Audio Swap", layout="wide")

TEMP = Path("temp")
TEMP.mkdir(exist_ok=True)

# =========================
# Session State Init
# =========================
if "use_cropped_unc" not in st.session_state:
    st.session_state.use_cropped_unc = False

if "use_cropped_dub" not in st.session_state:
    st.session_state.use_cropped_dub = False

# =========================
# Helper Functions
# =========================
def get_duration_seconds(video_path):
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(video_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return round(float(result.stdout.strip()), 3)

def sec_to_hms(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = sec % 60
    return f"{h:02}:{m:02}:{s:06.3f}"

def is_valid_time(t):
    return re.match(r"^\d{2}:\d{2}:\d{2}(\.\d{1,3})?$", t)

# 🔑 Smart crop (re-encode for accuracy)
def smart_crop(input_video, start, end, output_video):
    cmd = ["ffmpeg", "-y"]

    if start:
        cmd += ["-ss", start]

    cmd += ["-i", str(input_video)]

    if end:
        cmd += ["-to", end]

    cmd += [
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
        "-c:a", "aac",
        str(output_video)
    ]

    subprocess.run(cmd, check=True)

# =========================
# UI START
# =========================
st.title("🎬 Video Crop & Audio Swap Tool")
st.caption("Accurate trimming + safe audio swapping using FFmpeg")

# =========================
# Upload Videos
# =========================
c1, c2 = st.columns(2)

with c1:
    unc_video = st.file_uploader(
        "Upload UNCENSORED Video (Visual Source)",
        type=["mp4", "mkv", "mov"],
        key="upload_unc"
    )

with c2:
    dub_video = st.file_uploader(
        "Upload DUBBED Video (Audio Source)",
        type=["mp4", "mkv", "mov"],
        key="upload_dub"
    )

if not (unc_video and dub_video):
    st.warning("⬆️ Upload both videos to continue")
    st.stop()

unc_path = TEMP / "unc.mp4"
dub_path = TEMP / "dub.mp4"

unc_path.write_bytes(unc_video.read())
dub_path.write_bytes(dub_video.read())

# =========================
# Preview Original Videos
# =========================
st.subheader("🎥 Original Videos")

p1, p2 = st.columns(2)
with p1:
    st.video(str(unc_path))
with p2:
    st.video(str(dub_path))

# =========================
# Durations
# =========================
unc_len = get_duration_seconds(unc_path)
dub_len = get_duration_seconds(dub_path)
diff = abs(unc_len - dub_len)

st.subheader("🕒 Video Lengths")

d1, d2, d3 = st.columns(3)
with d1:
    st.metric("Uncensored", sec_to_hms(unc_len))
with d2:
    st.metric("Dubbed", sec_to_hms(dub_len))
with d3:
    st.metric("Difference", sec_to_hms(diff))

# =========================
# Crop Section
# =========================
st.subheader("✂️ Cropping")

with st.expander("ℹ️ How cropping works"):
    st.markdown("""
- **Front trim** → use Start  
- **End trim** → use End  
- **Both** → Start + End  

Uses re-encoding to avoid keyframe jumps  
Time format: `HH:MM:SS.mmm`
""")

crop_unc = st.checkbox("Crop Uncensored Video", key="crop_unc")
crop_dub = st.checkbox("Crop Dubbed Video", key="crop_dub")

cu1, cu2 = st.columns(2)

with cu1:
    st.markdown("#### 🎥 Uncensored")
    unc_start = st.text_input("Start", "00:00:00.000", key="unc_start")
    unc_end   = st.text_input("End", "", key="unc_end")

with cu2:
    st.markdown("#### 🎧 Dubbed")
    dub_start = st.text_input("Start", "00:00:00.000", key="dub_start")
    dub_end   = st.text_input("End", "", key="dub_end")

cropped_unc = TEMP / "unc_cropped.mp4"
cropped_dub = TEMP / "dub_cropped.mp4"

# =========================
# Crop Execution
# =========================
if st.button("💾 Save Cropped Videos", key="save_crop"):

    if crop_unc:
        if not is_valid_time(unc_start):
            st.error("❌ Invalid Uncensored START format")
            st.stop()
        if unc_end.strip() and not is_valid_time(unc_end):
            st.error("❌ Invalid Uncensored END format")
            st.stop()

        smart_crop(unc_path, unc_start, unc_end, cropped_unc)
        st.session_state.use_cropped_unc = True
        st.success("✅ Uncensored video cropped")

    if crop_dub:
        if not is_valid_time(dub_start):
            st.error("❌ Invalid Dubbed START format")
            st.stop()
        if dub_end.strip() and not is_valid_time(dub_end):
            st.error("❌ Invalid Dubbed END format")
            st.stop()

        smart_crop(dub_path, dub_start, dub_end, cropped_dub)
        st.session_state.use_cropped_dub = True
        st.success("✅ Dubbed video cropped")

# =========================
# After Crop Preview
# =========================
st.subheader("📊 After Cropping")

a1, a2 = st.columns(2)

with a1:
    if st.session_state.use_cropped_unc and cropped_unc.exists():
        new_len = get_duration_seconds(cropped_unc)
        st.metric(
            "Uncensored (Cropped)",
            sec_to_hms(new_len),
            delta=f"-{round(unc_len - new_len, 3)} sec"
        )
        st.video(str(cropped_unc))
    else:
        st.info("Uncensored not cropped")

with a2:
    if st.session_state.use_cropped_dub and cropped_dub.exists():
        new_len = get_duration_seconds(cropped_dub)
        st.metric(
            "Dubbed (Cropped)",
            sec_to_hms(new_len),
            delta=f"-{round(dub_len - new_len, 3)} sec"
        )
        st.video(str(cropped_dub))
    else:
        st.info("Dubbed not cropped")

# =========================
# Audio Swap
# =========================
st.subheader("🔄 Audio Swap")

if st.button("🚀 Swap Dubbed Audio → Uncensored", key="swap_audio"):

    progress = st.progress(0)
    status = st.empty()

    final_video = TEMP / "final_output.mp4"
    audio_file = TEMP / "dub_audio.m4a"

    unc_used = cropped_unc if st.session_state.use_cropped_unc else unc_path
    dub_used = cropped_dub if st.session_state.use_cropped_dub else dub_path

    status.info("🔊 Extracting dubbed audio…")
    progress.progress(30)

    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(dub_used),
        "-vn",
        "-c:a", "aac",
        str(audio_file)
    ], check=True)

    status.info("🎬 Replacing audio in uncensored video…")
    progress.progress(70)

    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(unc_used),
        "-i", str(audio_file),
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        str(final_video)
    ], check=True)

    progress.progress(100)
    status.success("✅ Audio swap complete!")

    st.video(str(final_video))

    with open(final_video, "rb") as f:
        st.download_button(
            "⬇️ Download Final Video",
            data=f,
            file_name="audio_swapped.mp4",
            mime="video/mp4"
        )
