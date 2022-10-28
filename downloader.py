import pytube

class Downloader:

    def __init__(self, url, mtype) -> None:
        self._url = url
        self._mtype = mtype

    def run(self):
        data = pytube.YouTube(self._url)
        naslov = data.title

        if self._mtype == 'a':
            print('Downloading...')
            audio = data.streams.get_audio_only()
            audio.download('Downloads', '.mp3', naslov )
            print('Download complete')

        elif self._mtype == 'v':
            print('Downloading...')
            video = data.streams.get_highest_resolution()
            video.download('Downloads')
            print('Download complete')

        else:
            print('Wrong input data')
