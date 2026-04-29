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

---

## Fix Add to Cart Button Not Working in Cart Drawer Suggested Products

If the **Add to Cart** button inside the cart drawer's "You May Also Like" or "Recently Viewed" sections does nothing when clicked, it means the product card link rendered with an empty `href` and the existing handler cannot extract the `product_id`.

This is fixed in theme version **1.3.4+**. For stores running an older version, apply the following runtime workaround via **Script Manager** without rebuilding the theme:

1. Navigate to **Storefront** > **Script Manager**
2. Click **Create a Script**
3. Configure the script:
    - **Name**: Fix Cart Drawer Add to Cart
    - **Location on page**: Footer
    - **Select pages where script will be added**: Store Pages
    - **Script category**: Essential
4. Paste the following code in the **Script contents** field:

```html
<script>
(function () {
    function getProductId(el) {
        // 1. Try existing href first
        try {
            var url = new URL(el.href, location.origin);
            var pid = url.searchParams.get('product_id');
            if (pid) return pid;
        } catch (e) { /* href empty or invalid */ }

        // 2. data-product-id on element itself or closest ancestor
        var withPid = el.closest('[data-product-id]');
        if (withPid && withPid.getAttribute('data-product-id')) {
            return withPid.getAttribute('data-product-id');
        }

        // 3. data-entity-id on the closest card wrapper
        var withEid = el.closest('[data-entity-id]');
        if (withEid && withEid.getAttribute('data-entity-id')) {
            return withEid.getAttribute('data-entity-id');
        }

        return null;
    }

    // Run in capture phase so we mutate the link BEFORE the theme's
    // bubble-phase click handler reads its href.
    document.addEventListener('click', function (event) {
        var el = event.target && event.target.closest
            ? event.target.closest('[data-papathemes-cart-item-add]')
            : null;
        if (!el) return;

        var href = el.getAttribute('href') || '';
        if (/[?&]product_id=\d+/.test(href)) return; // already valid

        var pid = getProductId(el);
        if (!pid) return;

        el.setAttribute(
            'href',
            '/cart.php?action=add&product_id=' + encodeURIComponent(pid)
        );
    }, true);
})();
</script>
```

5. Click **Save**

### How it works

- Listens for clicks in the **capture phase** so it runs before the theme's existing bubble-phase handler bound to `[data-papathemes-cart-item-add]`.
- When the clicked link's `href` is missing or has no `product_id` parameter, the script resolves the product ID from `data-product-id` (on the button or an ancestor) or `data-entity-id` (on the card wrapper rendered by the suggested-products and recently-viewed-products components).
- It then writes a valid `/cart.php?action=add&product_id=...` URL back onto the link so the existing AJAX add-to-cart logic picks it up unchanged.

The script is a no-op on links that already contain a working `product_id`, so it is safe to leave installed even after upgrading to a fixed theme version.
