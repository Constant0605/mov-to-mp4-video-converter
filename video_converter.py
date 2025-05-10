import os
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import subprocess
import threading

class VideoConverter:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Video Converter")
        self.window.geometry("600x400")
        self.window.resizable(False, False)
        
        # Configure theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Set FFmpeg path
        self.ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"  # Update this path to match your FFmpeg installation
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = ctk.CTkLabel(
            self.window,
            text="MOV to MKV/MP4 Converter",
            font=("Helvetica", 24, "bold")
        )
        title_label.pack(pady=20)
        
        # Input file selection
        self.input_frame = ctk.CTkFrame(self.window)
        self.input_frame.pack(pady=10, padx=20, fill="x")
        
        self.input_label = ctk.CTkLabel(
            self.input_frame,
            text="No file selected",
            font=("Helvetica", 12)
        )
        self.input_label.pack(side="left", padx=10)
        
        self.browse_button = ctk.CTkButton(
            self.input_frame,
            text="Browse",
            command=self.browse_file
        )
        self.browse_button.pack(side="right", padx=10)
        
        # Output format selection
        self.format_frame = ctk.CTkFrame(self.window)
        self.format_frame.pack(pady=10, padx=20, fill="x")
        
        self.format_label = ctk.CTkLabel(
            self.format_frame,
            text="Output Format:",
            font=("Helvetica", 12)
        )
        self.format_label.pack(side="left", padx=10)
        
        self.format_var = tk.StringVar(value="mp4")
        self.mp4_radio = ctk.CTkRadioButton(
            self.format_frame,
            text="MP4",
            variable=self.format_var,
            value="mp4"
        )
        self.mp4_radio.pack(side="left", padx=10)
        
        self.mkv_radio = ctk.CTkRadioButton(
            self.format_frame,
            text="MKV",
            variable=self.format_var,
            value="mkv"
        )
        self.mkv_radio.pack(side="left", padx=10)
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.window)
        self.progress_bar.pack(pady=20, padx=20, fill="x")
        self.progress_bar.set(0)
        
        # Status label
        self.status_label = ctk.CTkLabel(
            self.window,
            text="Ready to convert",
            font=("Helvetica", 12)
        )
        self.status_label.pack(pady=10)
        
        # Convert button
        self.convert_button = ctk.CTkButton(
            self.window,
            text="Convert",
            command=self.start_conversion,
            state="disabled"
        )
        self.convert_button.pack(pady=20)
        
    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("MOV files", "*.mov"), ("All files", "*.*")]
        )
        if file_path:
            self.input_file = file_path
            self.input_label.configure(text=os.path.basename(file_path))
            self.convert_button.configure(state="normal")
            
    def convert_video(self):
        try:
            output_format = self.format_var.get()
            output_file = os.path.splitext(self.input_file)[0] + f".{output_format}"
            
            # Use subprocess to run FFmpeg with full path and specific codecs
            command = [
                self.ffmpeg_path,
                '-i', self.input_file,
                '-c:v', 'libx264',  # Use H.264 codec for video
                '-preset', 'medium',  # Encoding preset (options: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow) (The slower , the better the qualit)
                '-crf', '23',  # Constant Rate Factor (18-28 is good, lower is better quality)
                '-c:a', 'aac',  # Use AAC codec for audio
                '-b:a', '192k',  # Audio bitrate (320k is the best quality)
                output_file
            ]
            
            # Run FFmpeg
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = process.communicate()
            
            if process.returncode == 0:
                self.window.after(0, lambda: self.status_label.configure(text="Conversion completed!"))
                self.window.after(0, lambda: self.progress_bar.set(1))
                self.window.after(0, lambda: messagebox.showinfo("Success", f"Video converted successfully to {output_format.upper()}!\nSaved to: {output_file}"))
            else:
                error_message = stderr.decode('utf-8')
                self.window.after(0, lambda: self.status_label.configure(text=f"Error: {error_message}"))
                self.window.after(0, lambda: messagebox.showerror("Error", f"Conversion failed: {error_message}"))
            
        except Exception as e:
            error_message = str(e)
            self.window.after(0, lambda: self.status_label.configure(text=f"Error: {error_message}"))
            self.window.after(0, lambda: messagebox.showerror("Error", f"Conversion failed: {error_message}"))
        
        finally:
            self.window.after(0, lambda: self.convert_button.configure(state="normal"))
            
    def start_conversion(self):
        self.convert_button.configure(state="disabled")
        self.status_label.configure(text="Converting...")
        self.progress_bar.set(0.5)
        
        # Start conversion in a separate thread
        thread = threading.Thread(target=self.convert_video)
        thread.daemon = True
        thread.start()
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = VideoConverter()
    app.run() 