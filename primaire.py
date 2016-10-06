import csv
import subprocess

# liste des images (id, latitude, longitude)
bureaux = csv.DictReader(open('primaire.csv'))
for bureau in bureaux:
    print(bureau)
    # calcul image plus grande avec nik2img
    cmd = """/usr/local/bin/nik2img.py /home/cquest/osmfr-lowzoom.xml png/%s.png -f png -c %s %s -z 15 -d 1024 1024 2>1""" % (bureau['Id'],bureau['longitude'],bureau['latitude'])
    subprocess.call(cmd,shell=True)
    # crop, attribution, optipng et exiftool en //
    subprocess.Popen("sh post.sh png/%s.png" % (bureau['Id'],),shell=True)
