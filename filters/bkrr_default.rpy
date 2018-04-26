
#    Булки, кефир и рок-н-ролл. Фильтр запуска мода по умолчанию    #

init python:
    filters["bkrr_default"] = u"Меню «Булки, кефир и рок-н-ролл» при включении игры"
    
python early:

    def bkrr_default():
        rgsn = renpy.game.script.namemap
        rgsn["splashscreen"] = rgsn["bkrr"]
