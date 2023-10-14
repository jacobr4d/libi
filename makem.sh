TMPP="/tmp/libi"
mkdir -p "${TMPP}"

TEXTP="${1}"
OUTD="${2}"
FLACP="${TMPP}/tmp.flac"
MP3P="${OUTD}/"$(basename "${TEXTP}").mp3
echo $TEXTP
echo $OUTD
echo $FLACP
echo $MP3P

touch "${FLACP}"
say -f "${TEXTP}" -o "${FLACP}"
ffmpeg -i "${FLACP}" "${MP3P}"
open "${MP3P}"