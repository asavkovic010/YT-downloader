from downloader import Downloader


if __name__ == '__main__':
    url = input('Please enter video link: ')
    mtype = input('For audio enter a, for video enter v: ')
    d = Downloader(url, mtype)
    d.run()
