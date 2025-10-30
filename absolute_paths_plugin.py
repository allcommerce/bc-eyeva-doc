"""
MkDocs plugin to convert relative URLs to absolute paths (without domain)
"""
import re
from urllib.parse import urljoin, urlparse
from mkdocs.plugins import BasePlugin


class AbsolutePathsPlugin(BasePlugin):
    """
    Plugin to convert all relative URLs to absolute paths (e.g., /usage/get-started/)
    """

    def on_post_page(self, output, page, config, **kwargs):
        """
        Convert relative URLs to absolute paths after page is generated

        Args:
            output: The complete HTML output of the page
            page: The Page object
            config: The MkDocs configuration

        Returns:
            Modified HTML with absolute paths
        """
        site_url = config.get('site_url', '')

        if not site_url:
            return output

        # Ensure site_url ends without slash for consistent joining
        site_url = site_url.rstrip('/')

        # Get the base URL for this page
        page_url = page.url if hasattr(page, 'url') and page.url else ''
        base_url = f"{site_url}/{page_url}"

        # Convert href relative URLs to absolute paths
        def replace_href(match):
            quote = match.group(1)
            url = match.group(2)
            original = match.group(0)

            # Skip if already absolute path, absolute URL, anchor, or special protocols
            if url.startswith(('/', 'http://', 'https://', '//', '#', 'javascript:', 'mailto:', 'data:')):
                return original

            # Skip assets (css, js, images) - keep them relative
            if any(ext in url.lower() for ext in ['.css', '.js', '.png', '.jpg', '.jpeg', '.svg', '.ico', '.woff', '.woff2', '.ttf', '.eot', '.map', '.json', '.gif', '.webp']):
                return original

            # Convert relative URL to absolute path (without domain)
            try:
                # First convert to absolute URL with domain
                absolute_url = urljoin(base_url, url)
                # Then extract just the path
                parsed = urlparse(absolute_url)
                absolute_path = parsed.path

                # Ensure it starts with /
                if not absolute_path.startswith('/'):
                    absolute_path = '/' + absolute_path

                return f'href={quote}{absolute_path}{quote}'
            except Exception:
                # If conversion fails, return original
                return original

        # Replace all href attributes
        output = re.sub(r'href=(["\'])([^"\']+)\1', replace_href, output)

        return output
