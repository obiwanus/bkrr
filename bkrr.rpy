
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

    if persistent.bkrr_rekord_hit:
        jump bkrr_start_normal

    play music bkrr_music_list["menu"] fadein 15
    $ renpy.pause(1.5, hard=True)

    play sound bkrr_ui["sound"]["plate_stop"]
    play music music_list["gentle_predator"] fadein 3

    show dv normal pioneer2 close with dissolve

    "Так. Кто это у нас тут."

    menu:
        "Рекорд":
            jump alisa_rekord
        "Кот":
            jump alisa_kot

    label alisa_rekord:
        "Рекорд Надоев.{w} Опять весь мод скачал кнопкой Download?"

        show dv angry pioneer2 close with dspr

        "Я тебе говорила больше так не делать? {w}Говорила."
        "Говорила поставить сурстри и качать нормально? {w}Говорила."
        "Говорила, что врежу? {w}Говорила."

        show dv rage pioneer2 close with dspr

        "Ну и не обижайся.{w=1}{nw}"

        window hide

        scene cg rekord_guitar_hit with bkrr_fade(1.0)

        $ renpy.pause(3.50, hard=True)

        play sound bkrr_sfx_list["guitar_hit"]

        scene black
        show bkrr_bang:
            truecenter
            alpha 1.1
            zoom 1.1
            linear 2.5 alpha 0.0 zoom 0.9
        with None

        stop music fadeout 1.0

        $ renpy.run(OpenURL("https://bitbucket.org/obiwanus/bkrr/issues/40/sourcetree-pull"))

        $ persistent.bkrr_rekord_hit = True

        jump bkrr_start_normal


    label alisa_kot:

        show dv sad pioneer2 close with dspr

        "Ладно. Проходи. У меня к Рекорду вопросы."

        window hide
        $ renpy.pause(2.0)
        window show

        show dv angry pioneer2 close with dspr

        "Проходи уже, кому сказала!{w=1}{nw}"

        window hide

        jump bkrr_start_normal



    label bkrr_start_normal:
        play music bkrr_music_list["menu"] fadein 10
        call screen bkrr_menu
