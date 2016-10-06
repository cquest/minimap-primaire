convert $1 -gravity Center -crop 400x400+0+0 +repage $1
composite -gravity SouthEast attribution.png $1 $1
optipng -quiet $1
exiftool -delete_original -"PNG:Copyright"="Map data (C) OpenStreetMap.org contributors under ODbL 1.0, Map image (C) OpenStreetMap.fr under CC-by-SA 3.0" $1 2>/dev/null
