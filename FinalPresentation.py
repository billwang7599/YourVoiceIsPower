#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

init()
    #tempo
setTempo(110)

    #SOUNDBANK variables 
speech1 = DKBEAR_FREE_TALK_DOING_THIS
speech2 = DKBEAR_FREE_TALK_NEED_TO
speech3 = DKBEAR_FREE_TALK_MUST_DO
piano1 = DKBEAR_FREE_THEME_PIANO
synth2 = DKBEAR_FREE_THEME_SYNTH_2
snare1 = MILKNSIZZ_CRASH_PAD_SNARE
kick1 = DKBEAR_FREE_PERC_KICK
verse1a = DKBEAR_FREE_VOX_VERSE_1A
verse1b = DKBEAR_FREE_VOX_VERSE_1B

    #intro
fitMedia(speech1, 1, 1, 2.8)
fitMedia(synth2, 2, 2.5, 22.5)
fitMedia(piano1, 3, 6.5, 22.5)

    #verse
fitMedia(verse1a, 6, 10 , 18)
fitMedia(verse1b, 6, 18, 22.25)
#setEffect(2, VOLUME, GAIN, -10.0, 3, 3.5) 

    #verse fade
insertMediaSection(verse1b, 10, 22, 5, 5.25)

    #outro
fitMedia(speech2,7,23,25)
fitMedia(speech3,7,25,27)


    # Fills
fillA = "--------------0-0-------------0-0-------------0-0-------------0-0-----0000----0000-----+00-----000-----00-0----00-0-----+00-----000-----0-00----0-0------+00-----000-----0-0-----0-0------+00-----000-----0-0------+00-----000-----0-0"
fillB = "0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------0-------"
fillC = "--000-00-00-0-00"

    #beat
makeBeatSlice(snare1, 4, 6.5, fillA, [1.7, 2.0])
makeBeatSlice(kick1, 5, 6.5, fillB, [1.5, 2.0])

    #effects
def fadeOut(track, start, end):
    setEffect(track, VOLUME, GAIN, 1, start, -60, end)

# Echo to repeat message
setEffect(10, DELAY, DELAY_FEEDBACK, -120, 20, -1, 24)
setEffect(7, VOLUME, GAIN, -60, 23, 5, 23.75)

    #fade outs
#fade out to emphasize lyrics -- helps spreads the message
fadeOut(4, 16, 25)
fadeOut(5, 16, 25)
fadeOut(2, 16, 21.5)
fadeOut(3, 16, 21.5)
#fadeOut(7, 25, 26)

finish()
