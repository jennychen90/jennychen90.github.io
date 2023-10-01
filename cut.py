import os
from moviepy.editor import VideoFileClip

input_folder = 'Initial'
output_folder = "resize"

file_list = os.listdir(input_folder)

# 放大倍數
scale_factor = 2.0

for file_name in file_list:
    if file_name.endswith(".mp4"):
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, file_name)
        video = VideoFileClip(input_file)
        video_width, video_height = video.size
        
        # 計算要放大的區域範圍
        start_x = int(video_width / 2 - video_width / (2 * scale_factor)) -75
        start_y = int(video_height / 2 - video_height / (2 * scale_factor))
        end_x = int(video_width / 2 + video_width / (2 * scale_factor)) -75
        end_y = int(video_height / 2 + video_height / (2 * scale_factor))
        
        # 放大到 3840x2160 像素
        resized_video = video.resize(width=3840, height=2160).crop(x1=start_x, y1=start_y, x2=end_x, y2=end_y)
        
        resized_video.write_videofile(output_file, codec="libx264", audio_codec="aac")
