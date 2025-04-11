# FAQs

## Converting Videos to H.265 Format for Safari Compatibility

Install `ffmpeg` on Windows using command line:

```bash
choco install ffmpeg
```

Run the following command to convert the video to H.265 format:

```bash
ffmpeg -i input.mp4 -vcodec libx265 -c:a aac -tag:v hvc1  output.mp4
```
