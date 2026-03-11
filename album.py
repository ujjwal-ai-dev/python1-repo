def album(artist_name,album_title,track_num=''):
    new_album = {'artist_name':artist_name,'album_title':album_title}
    if track_num:
        new_album['track_num'] = track_num
    return new_album

while True:
    print('Enter the artist name and the name of the album, enter "q" to quit: ')
    a_name = input('enter the name of the artist: ')
    if a_name.lower() == 'q':
        break

    allbum_n = input('enter the name of the album: ')
    if allbum_n == 'q':
        break

    new_album = album(a_name,allbum_n)
    print(new_album,'\n')
    

    