class DownloadManager:
    def __init__(self):
        self.downloads = []

    def add_download(self, title, status="Waiting"):
        self.downloads.append(
            {
                "title": title,
                "progress": 0,
                "status": status,
                "speed": "0 MB/s",
                "eta": "--:--",
            }
        )

    def update_progress(self, index, progress, speed, eta, status):
        if 0 <= index < len(self.downloads):
            self.downloads[index]["progress"] = progress
            self.downloads[index]["speed"] = speed
            self.downloads[index]["eta"] = eta
            self.downloads[index]["status"] = status

    def get_downloads(self):
        return self.downloads
