"""
core/thumbnail.py

Thumbnail download and cache manager.
"""

from pathlib import Path
from urllib.request import urlretrieve

from core.logger import logger


class ThumbnailManager:

    def __init__(self, cache_dir="assets/cache/thumbnails"):

        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------

    def get_thumbnail(self, task):
        """
        Returns local thumbnail path.
        Downloads it if not already cached.
        """

        if not getattr(task, "thumbnail_url", None):
            return None

        filename = f"{task.id}.jpg"
        filepath = self.cache_dir / filename

        if filepath.exists():
            return str(filepath)

        try:

            urlretrieve(task.thumbnail_url, filepath)

            logger.info(f"Thumbnail downloaded: {filepath}")

            return str(filepath)

        except Exception as e:

            logger.error(f"Thumbnail download failed: {e}")

            return None

    # --------------------------------------------------

    def clear_cache(self):

        count = 0

        for file in self.cache_dir.glob("*"):

            try:
                file.unlink()
                count += 1

            except Exception:
                pass

        logger.info(f"Thumbnail cache cleared ({count} files)")


thumbnail_manager = ThumbnailManager()
