import pytube

ytlink = input('Please enter video link: ')

data = pytube.YouTube(ytlink)
naslov = data.title

Download_type = input('For audio enter a, for video enter v: ')

if Download_type == 'a':
    print('Downloading...')
    audio = data.streams.get_audio_only()
    audio.download('Downloads', '.mp3', naslov )
    print('Download complete')

if Download_type == 'v':
    print('Downloading...')
    video = data.streams.get_highest_resolution()
    video.download('Downloads')
    print('Download complete')

else:
    print('Wrong input data')