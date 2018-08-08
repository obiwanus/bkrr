
#    Булки, кефир и рок-н-ролл. Главный файл: вызов меню, запуск мода    #

init 2 python:

    try:
        mods["bkrr"] = bkrr_title[0]
        mod_tags["bkrr"] = ["gameplay:kinetic", "length:days", "protagonist:male", "character:Семён", "character:Мику", "character:Ольга Дмитриевна", "character:Виола", "character:Алиса", "character:Ульяна", "character:Славя", "character:Женя", "character:Лена", "character:Шурик", "character:Электроник", "character:Новый персонаж"]
    except NameError:
        pass

label bkrr:

    window hide

    $ bkrr_new_chapter("Меню")

    scene bg ext_music_club_day:
        subpixel True
        truecenter
        zoom 1.2
        linear 2.5 zoom 1.0
    with dissolve

    play ambience ambience_day_countryside_ambience fadein 3

    play sound_loop sfx_gusty_wind fadein 3

    play music bkrr_music_list["menu"] fadein 15

    $ renpy.pause(2.0, hard=True)

    call screen bkrr_menu
