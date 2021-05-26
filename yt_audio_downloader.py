from pytube import YouTube
import moviepy.editor as mp
import os
import shutil

def limpieza(): #Elimina la carpeta temp.
    shutil.rmtree(c_temp)

def descargar():
    print('Descargando...')
    ytf = yt.streams.get_by_itag(140) #Selecciona el archivo correspondiente al audio del video en 128kbps.
    os.mkdir(c_temp, 0o777) #Crea una carpeta temporal (temp) para alojar la descarga.
    ytf.download(c_temp) #Comienza la descarga del archivo y lo guarda en la carpeta temp.

#Renombra el archivo descargado para no tener problemnas a la hora de convertirlo a mp3.
def renombrar_temporal():
    nombre_win = os.listdir(c_temp)
    nombre_win_str = "".join(nombre_win)
    titulo_final = nombre_win_str[:-4]
    titulo_temporal = c_temp + '\\' + 'temporal' + '.mp4'
    tit_original = c_temp + '\\' + nombre_win_str
    os.rename(tit_original, titulo_temporal)
    return titulo_final

def conversor(titulo_final):
    while True:
        existe_mp3 = os.path.exists('MP3')

        if existe_mp3 == True:
            mp4_audio = mp.AudioFileClip(c_temp + '\\' + 'temporal.mp4')
            mp4_audio.write_audiofile( c_mp3 + '\\' + 'temporal.mp3', verbose=False)
            os.rename(c_mp3 + '\\' + 'temporal.mp3', c_mp3 + '\\' + titulo_final + '.mp3')
            break
        else:
            os.mkdir(c_mp3, 0o777)

c_actual = os.getcwd()
c_temp = c_actual + r'\temp'
c_mp3 = c_actual + r'\MP3'

print('\n>>>-----------------------<<<')
url = str(input('Ingrese la URL del video: '))
yt = YouTube(url)
titulo = yt.title

print('\n<<<----------------------->>>')
print('Titulo:  ' + titulo)
print('<<<----------------------->>>\n')

lstst=yt.streams.filter(file_extension='mp4')
eleccion = str.lower(input('Comenzar la descarga? S/N  '))

if eleccion == 's':
    existe = os.path.exists("temp")
    if existe == True:
        limpieza()
        descargar()
        titulo = renombrar_temporal()
        conversor(titulo)
        limpieza()
    else:
        descargar()
        titulo = renombrar_temporal()
        conversor(titulo)
        limpieza()
else:
    pass

print('\n>>> Fin del programa <<<\n')

'''
-----------------------------------
YouTube video stream format codes  
Comprehensive list of YouTube format code itags

itag Code	Container	Content	Resolution	Bitrate	Range	VR / 3D
5	        flv	    audio/video	240p	-	-	-
6	        flv	    audio/video	270p	-	-	-
17      	3gp 	audio/video	144p	-	-	-
18      	mp4 	audio/video	360p	-	-	-
22      	mp4	    audio/video	720p	-	-	-
34      	flv	    audio/video	360p	-	-	-
35      	flv	    audio/video	480p	-	-	-
36      	3gp	    audio/video	180p	-	-	-
37      	mp4	    audio/video	1080p	-	-	-
38      	mp4	    audio/video	3072p	-	-	-
43      	webm	audio/video	360p	-	-	-
44      	webm	audio/video	480p	-	-	-
45      	webm	audio/video	720p	-	-	-
46      	webm	audio/video	1080p	-	-	-
82      	mp4	    audio/video	360p	-	-	3D
83      	mp4	    audio/video	480p	-	-	3D
84      	mp4	    audio/video	720p	-	-	3D
85      	mp4	    audio/video	1080p	-	-	3D
92      	hls	    audio/video	240p	-	-	3D
93      	hls	    audio/video	360p	-	-	3D
94      	hls	    audio/video	480p	-	-	3D
95      	hls	    audio/video	720p	-	-	3D
96      	hls	    audio/video	1080p	-	-	-
100	        webm	audio/video	360p	-	-	3D
101	        webm	audio/video	480p	-	-	3D
102	        webm	audio/video	720p	-	-	3D
132	        hls	    audio/video	240p	-	-	
133	        mp4	    video	    240p	-	-	
134	        mp4	    video	    360p	-	-	
135	        mp4	    video   	480p	-	-	
136	        mp4	    video   	720p	-	-	
137	        mp4	    video	    1080p	-	-	
138	        mp4	    video	    2160p60	-	-	
139	        m4a	    audio       	-	48k	-	
140	        m4a	    audio       	-	128k	-	
141	        m4a	    audio       	-	256k	-	
151	        hls 	audio/video	72p	-	-	
160	        mp4	    video	    144p	-	-	
167	        webm	video	    360p	-	-	
168	        webm	video	    480p	-	-	
169	        webm	video	    1080p	-	-	
171	        webm	audio       	-	128k	-	
218	        webm	video	    480p	-	-	
219	        webm	video	    144p	-	-	
242	        webm	video	    240p	-	-	
243	        webm	video	    360p	-	-	
244	        webm	video   	480p	-	-	
245	        webm	video   	480p	-	-	
246	        webm	video   	480p	-	-	
247	        webm	video	    720p	-	-	
248	        webm	video	    1080p	-	-	
249	        webm	audio       	-	50k	-	
250	        webm	audio       	-	70k	-	
251	        webm	audio       	-	160k -
264	        mp4	    video	    1440p	-	-	
266	        mp4	    video	    2160p60	-	-	
271	        webm	video	    1440p	-	-	
272	        webm	video	    4320p	-	-	
278	        webm	video	    144p	-	-	
298	        mp4	    video   	720p60	-	-	
299	        mp4	    video   	1080p60	-	-	
302	        webm	video   	720p60	-	-	
303	        webm	video	    1080p60	-	-	
308	        webm	video	    1440p60	-	-	
313	        webm	video	    2160p	-	-	
315	        webm	video	    2160p60	-	-	
330	        webm	video	    144p60	-	hdr	
331	        webm	video	    240p60	-	hdr	
332	        webm	video	    360p60	-	hdr	
333	        webm	video	    480p60	-	hdr	
334	        webm	video	    720p60	-	hdr	
335	        webm	video   	1080p60	-	hdr	
336	        webm	video   	1440p60	-	hdr	
337	        webm	video	    2160p60	-	hdr	

'''