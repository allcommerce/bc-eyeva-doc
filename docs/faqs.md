# FAQs

## Disable Sticky Add to Cart Box on Product Details Page

To disable the sticky behavior of the Add to Cart box on the right side of the Product Details Page, add the following script via **Script Manager**:

1. Navigate to **Storefront** > **Script Manager**
2. Click **Create a Script**
3. Configure the script:
    - **Name**: Disable Sticky Add to Cart
    - **Location on page**: Footer
    - **Select pages where script will be added**: Store Pages
    - **Script category**: Essential
4. Paste the following code in the **Script contents** field:

```html
<script>
(function() {
    var style = document.createElement('style');
    style.innerHTML = '.productView ._eyeva-sticky-box { position: relative }';
    document.head.appendChild(style);
})();
</script>
```

5. Click **Save**

This script injects a CSS rule that overrides the sticky positioning, making the Add to Cart box scroll normally with the page content instead of staying fixed on the screen.

---

## Converting Videos to H.265 Format for Safari Compatibility

Install `ffmpeg` on Windows using command line:

```bash
choco install ffmpeg
```

Run the following command to convert the video to H.265 format:

```bash
ffmpeg -i input.mp4 -vcodec libx265 -c:a aac -tag:v hvc1  output.mp4
```
