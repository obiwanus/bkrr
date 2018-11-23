
#    Булки, кефир и рок-н-ролл. Тестовый файл    #

init 999 python:

    config.developer = True
    config.debug = True

init 2:

    $ mods["bkrr_test"] = bkrr_title[0] + " (тест)"

    python:

        char = None

        chars = {
            "mi":(
                ("angry", "cry", "cry_smile", "dontlike", "grin", "happy", "laugh", "normal", "rage", "sad", "sad_smile", "scared", "serious", "shocked", "shy", "smile", "surprise", "upset"),
                ("body", "body_loo", "pioneer_loo", "swim_loo", "bkrr_dress", "yukata", "underwear", "bkrr_sport", "apron", "dirt apron", "jacket", "shorts", "wet pioneer")
            ),
            "mt":(
                ("angry", "grin", "laugh", "normal", "rage", "sad", "smile", "surprise"),
                ("bkrr_sport", "nightdress")
            ),
            "dv":(
                ("angry", "cry", "grin", "guilty", "laugh", "normal", "rage", "sad", "scared", "shocked", "shy", "smile", "surprise"),
                ("swim", )
            ),
            "us":(
                ("angry", "calml", "cry", "cry2", "dontlike", "fear", "grin", "laugh", "laugh2", "normal", "normal_dontlike", "sad", "shy", "shy2", "smile", "surp1", "surp2", "surp3", "upset"),
                ("bra", "bkrr_dress")
            ),
            "nt":(
                ("laugh", "normal", "sad", "smile"),
                ("cook", )
            ),
            "tol":(
                ("normal", "pain", "sad", "shy", "smile"),
                ("pioneer", )
            ),
            "tr":(
                ("normal", "smile1", "surp", "upset2", "smile2", "smile3", "upset1"),
                ("pioneer", "cas")
            ),
            "ant":(
                ("normal", "serious", "smile", "surprise"),
                ("shirt", )
            ),
            "kla":(
                ("laugh", "normal", "smile", "shy", "surprise"),
                ("pioneer", "sport")
            ),
            "el":(
                ("angry", "fingal", "grin", "laugh", "normal", "sad", "scared", "serious", "shocked", "smile", "surprise", "upset"),
                ("shirt", )
            ),
            "sh":(
                ("cry", "laugh", "normal", "normal_smile", "rage", "serious", "scared", "surprise", "upset", "smile"),
                ("bathrobe", "shirt")
            ),
            "un":(
                ("angry", "angry2", "cry", "cry_smile", "evil_smile", "grin", "laugh", "normal", "rage", "sad", "scared", "serious", "shocked", "shy", "shy_smile", "smile", "smile2", "smile3", "surprise"),
                ("bkrr_dress", )
            ),
            "cs":(
                ("normal", "shy", "smile"),
                ("body", "dress", "civil", "civil2", "panties", "swim", "robe")
            ),
            "mz":(
                ("angry", "bukal", "laugh", "normal", "rage", "shy", "smile"),
                ("bkrr_sport", "mask bkrr_sport", "bkrr_dress", "glasses bkrr_sport", "glasses bkrr_dress")
            )
        }

        distances = ("close", "normal", "far")

        def test_spr(name, dt = "day"):
            bg = "bg ext_square_%s" % dt
            renpy.scene()
            renpy.show(bg)
            bkrr_set_time(dt)
            for emotion in chars[name][0]:
                for clothes in chars[name][1]:
                    for distance in distances:
                        if distance == "normal":
                            sprite = "%s %s %s" % (name, emotion, clothes)
                        else:
                            sprite = "%s %s %s %s" % (name, emotion, clothes, distance)
                        renpy.show(sprite)
                        renpy.with_statement(dissolve)
                        renpy.say(th, sprite)

label bkrr_test:
    window hide
    $ bkrr_new_chapter("Тест")
    scene black with dissolve
    $ bkrr_set_time()
    scene bg ext_square_day with dissolve

    window show
    "Тест."
    window hide
    $ renpy.pause()
    menu:
        with dissolve
        "Протестировать предметы":
            jump bkrr_test_item
        "Протестировать достижения":
            jump bkrr_test_ach
        "Сбросить все достижения":
            jump bkrr_reset_ach
        "Протестировать спрайты":
            jump bkrr_test_spr
        "Протестировать песни":
            jump bkrr_test_song
        "\n"
        "Или выйти:"
        "в меню БКРР":
            jump bkrr
        "в главное меню игры":
            return

label bkrr_test_song:
    show bkrr_lyrics_screen with bkrr_blindstotop_transition
    show bkrr_song "d4_mi":
        xalign 0.5
        ypos 1.0
        linear 25.0 ypos -1.0
    $ renpy.pause(25.0)
    hide bkrr_lyrics_screen
    hide bkrr_song
    with bkrr_blindstobottom_transition
    show bkrr_lyrics_screen with bkrr_blindstotop_transition
    show bkrr_song "d6_dv":
        xalign 0.5
        ypos 1.0
        linear 35.0 ypos -2.0
    $ renpy.pause(35.0)
    hide bkrr_lyrics_screen
    hide bkrr_song
    with bkrr_blindstobottom_transition
    show bkrr_lyrics_screen with bkrr_blindstotop_transition
    show bkrr_song "d9_sem":
        xalign 0.5
        ypos 1.0
        linear 25.0 ypos -1.0
    $ renpy.pause(25.0)
    hide bkrr_lyrics_screen
    hide bkrr_song
    with bkrr_blindstobottom_transition
    jump bkrr_test

label bkrr_test_item:
    python:
        for item in bkrr_item_list:
            bkrr_get_item(item)
    jump bkrr_test

label bkrr_test_ach:
    python:
        bkrr_get_all_achievements()
    jump bkrr_test

label bkrr_reset_ach:
    python:
        bkrr_reset_achievements()
    jump bkrr_test

label bkrr_test_spr:
    menu:
        with dissolve
        "Протестировать спрайты:"
        "Мику":
            $ char = "mi"
        "Ольги":
            $ char = "mt"
        "Алисы":
            $ char = "dv"
        "Ульяны":
            $ char = "us"
        "Натальи":
            $ char = "nt"
        "Толика":
            $ char = "tol"
        "Трука":
            $ char = "tr"
        "Антона":
            $ char = "ant"
        "Клауса":
            $ char = "kla"
        "Электроника":
            $ char = "el"
        "Шурика":
            $ char = "sh"
        "Лены":
            $ char = "un"
        "Виолы":
            $ char = "cs"
        "Жени":
            $ char = "mz"
    python:
        for dt in ("day", "sunset", "night"):
            test_spr(char, dt)
    jump bkrr_test
