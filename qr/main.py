import segno
url ='https://www.youtube.com/@nyfongITE'
qrcode = segno.make(url)
qrcode.save('yt.png')