
#    Булки, кефир и рок-н-ролл. Файл экранов    #

init 2:

    # Для неактивных кнопок используется add, а не imagebutton без action, потому как 1.1 не позволяет использовать конструкции "if ... else" внутри imagebutton.
    # Также для 1.1 пришлось убрать звуки кнопок, ибо она перезапускает весь ATL при наличии hovered, и это печально.

    ##    Экран меню    ##

    screen bkrr_menu():

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        # Локальные функции и переменные

        python:

            def menu_img_status(imgf, condition="hover"):
                if condition == "hover":
                    return im.MatrixColor(imgf, im.matrix.contrast(1.7))
                if condition == "insensitive":
                    return im.Alpha(imgf, 0.38)

            menu_hovered_action_common = Play("test_one", bkrr_ui["sound"]["paper"])
            menu_hovered_action_catday = Play("test_two", bkrr_ui["sound"]["meow"])
            menu_hovered_action_plate = Play("sound", bkrr_ui["sound"]["plate_stop"], fadein=1.8)


        # Основные элементы

        frame:
            background bkrr_ui["img"]["base"]
            area(0.0, 0.0, 1.0, 1.0)
            at bkrr_menu_frame_atl

            # plate

            imagebutton:
                action NullAction()
                idle bkrr_ui["img"]["plate"]
                hover bkrr_ui["img"]["plate"]
                hovered menu_hovered_action_plate
                at bkrr_menu_plate_atl

            # prologue, epilogue, credits, main_menu

            imagebutton:
                action [Hide("bkrr_menu", transition=dissolve), Jump("bkrr_prologue")]
                idle bkrr_ui["img"]["prologue"]
                hover menu_img_status(bkrr_ui["img"]["prologue"])
                hovered menu_hovered_action_common
                at bkrr_menu_pos_atl(0.65, 0.16, 0.49, -2.0)

            if persistent.bkrr_check["epilogue"]:
                imagebutton:
                    action [Hide("bkrr_menu", transition=dissolve), Jump("bkrr_epilogue")]
                    idle bkrr_ui["img"]["epilogue"]
                    hover menu_img_status(bkrr_ui["img"]["epilogue"])
                    hovered menu_hovered_action_common
                    at bkrr_menu_pos_atl(0.65, 0.16, 0.57, 3.0)
            else:
                add menu_img_status(bkrr_ui["img"]["epilogue"], "insensitive"):
                    at bkrr_menu_pos_atl(0.65, 0.16, 0.57, 3.0)

            if persistent.bkrr_check["credits4"]:
                imagebutton:
                    action [Hide("bkrr_menu", transition=dissolve), Jump("bkrr_credits")]
                    idle bkrr_ui["img"]["credits"]
                    hover menu_img_status(bkrr_ui["img"]["credits"])
                    hovered menu_hovered_action_common
                    at bkrr_menu_pos_atl(0.65, 0.16, 0.66, -2.2)
            else:
                add menu_img_status(bkrr_ui["img"]["credits"], "insensitive"):
                    at bkrr_menu_pos_atl(0.65, 0.16, 0.66, -2.2)

            imagebutton:
                action [Hide("bkrr_menu", transition=dissolve), MainMenu(confirm=False)]
                idle bkrr_ui["img"]["main_menu"]
                hover menu_img_status(bkrr_ui["img"]["main_menu"])
                hovered menu_hovered_action_common
                at bkrr_menu_pos_atl(0.65, 0.16, 0.75, 2.8)

            # steam, vk

            imagebutton:
                action [NullAction(), OpenURL(bkrr_ui["hyperlinks"]["steam"])]
                idle bkrr_ui["img"]["steam"]
                hover bkrr_ui["img"]["steam"]
                at bkrr_menu_pos_atl(1.0, 0.11, 0.87, 12.0)

            imagebutton:
                action [NullAction(), OpenURL(bkrr_ui["hyperlinks"]["vk"])]
                idle bkrr_ui["img"]["vk"]
                hover bkrr_ui["img"]["vk"]
                at bkrr_menu_pos_atl(1.0, 0.2, 0.88, -17.3)

            # days

            grid 4 4:
                spacing -147
                at bkrr_menu_pos_atl(0.88, 0.51, 0.51, 0.0)

                for dn in range(4, 20):
                    if persistent.bkrr_check[dn]:
                        imagebutton:
                            action [Hide("bkrr_menu", transition=dissolve), Jump("bkrr_day" + str(dn) + "_start")]
                            idle bkrr_ui["img"]["day"+str(dn)][0]
                            hover menu_img_status(bkrr_ui["img"]["day"+str(dn)][0])
                            hovered menu_hovered_action_common
                            at bkrr_menu_pos_atl(0.69, 0.5, 0.5, bkrr_ui["img"]["day"+str(dn)][1])
                    else:
                        add menu_img_status(bkrr_ui["img"]["day"+str(dn)][0], "insensitive"):
                            at bkrr_menu_pos_atl(0.69, 0.5, 0.5, bkrr_ui["img"]["day"+str(dn)][1])

            # addons

            imagebutton:
                action [Hide("bkrr_menu", transition=dissolve), Jump("bkrr_addon_catday")]
                idle bkrr_ui["img"]["catday"]
                hover LiveComposite((366, 463), (0, 0), bkrr_ui["img"]["catday"], (103, 380), Text(bkrr_title[2].lower(), style=style.bkrr_service2, drop_shadow=None, kerning=7.4, color="#6F5C43", size=32))
                hovered menu_hovered_action_catday
                at bkrr_menu_pos_atl(0.79, 0.852, 0.283, 18.1)

            # gallery

            imagebutton:
                action ShowMenu("bkrr_gallery_menu")
                idle bkrr_ui["img"]["gallery"]
                hover menu_img_status(bkrr_ui["img"]["gallery"])
                hovered menu_hovered_action_common
                at bkrr_menu_pos_atl(0.68, 0.858, 0.66, -5.2)

            # achievements

            imagebutton:
                action ShowMenu("bkrr_achievements")
                idle bkrr_ui["img"]["achievements"]
                hover menu_img_status(bkrr_ui["img"]["achievements"])
                hovered menu_hovered_action_common
                at bkrr_menu_pos_atl(0.667, 0.86, 0.75, -6.7)

            # sprites preferences

            imagebutton:
                action ShowMenu("bkrr_sprites_pref")
                idle bkrr_ui["img"]["sprites_pref"]
                hover menu_img_status(bkrr_ui["img"]["sprites_pref"])
                hovered menu_hovered_action_common
                at bkrr_menu_pos_atl(0.69, 0.86, 0.86, -3.7)

            # shadows

            add bkrr_ui["img"]["tree_shadow"]:
                at bkrr_menu_tree_shadow_atl

            add bkrr_ui["img"]["shadow"]:
                at bkrr_menu_shadow_atl

    ## Экран меню: ATL

    # Общее

    transform bkrr_menu_pos_atl(z, x, y, rot):
        zoom z
        pos(x, y)
        anchor(0.5, 0.5)
        rotate rot
        bkrr_menu_hover_atl(z, rot)

    transform bkrr_menu_hover_atl(z, rot):
        on hover:
            ease 0.1 zoom (z - 0.15) rotate 0.0
            ease 0.1 zoom (z - 0.02)
        on idle:
            ease 0.1 zoom z rotate rot

    # Для конкретных элементов

    transform bkrr_menu_frame_atl:
        subpixel True
        truecenter
        zoom 1.2
        on show:
            alpha 0.0
            ease 1.0 zoom 1.0 alpha 1.0

    transform bkrr_menu_plate_atl:
        subpixel True
        pos(0.152, 0.24)
        anchor(0.5, 0.5)
        zoom 0.65
        on idle:
            ease 0.2 zoom 0.65
            block:
                linear 8.2 rotate 360.0
                rotate 0.0
                repeat
        on hover:
            ease 0.2 zoom 0.72 rotate 0.0

    transform bkrr_menu_shadow_atl:
        topleft
        alpha 0.82

    transform bkrr_menu_tree_shadow_atl:
        subpixel True
        pos(0.28, -0.11)
        anchor(0.0, 0.0)
        alpha 0.34 rotate -1.0 zoom 1.0
        parallel:
            choice 3:
                ease 2.5 rotate 0.5
                ease 2.5 rotate -0.5
                repeat
            choice 2:
                ease 2.25 rotate 1.0
            choice:
                ease 1.25 rotate 1.5
            repeat
        parallel:
            choice 2:
                ease 1.25 zoom 1.025
                ease 1.25 zoom 1.02
            choice:
                ease 1.5 zoom 1.03
                ease 1.5 zoom 1.02
            choice:
                ease 1.5 zoom 1.035
                ease 1.5 zoom 1.02
            repeat

    ##    Экран достижений    ##

    screen bkrr_achievements():

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        $ columns = 2
        $ rows = len(bkrr_ach_list)+1

        # Основные элементы

        frame:
            background bkrr_ui["img"]["base"]
            area (0.0, 0.0, 1.0, 1.0)

            # back

            imagebutton:
                action Return()
                idle bkrr_ui["img"]["back"]
                hover bkrr_ui["img"]["back"]
                at bkrr_menu_pos_atl(0.82, 0.86, 0.85, -6.7)

            # plate

            add bkrr_ui["img"]["plate"]:
                at bkrr_menu_pos_atl(1.22, 0.935, 0.132, 27.0)

            # shadows

            add bkrr_ui["img"]["tree_shadow"]:
                at bkrr_menu_tree_shadow_atl

            add bkrr_ui["img"]["shadow"]:
                at bkrr_menu_shadow_atl

            # achievements

            frame:
                background "#0005"
                area(128, 38, 1160, 985)

                vbox:
                    align(0.5, 0.0)

                    null height 50

                    text u"Достижения {size=-4}{k=0.0}(%s / %s){/k}{/size}" % (bkrr_check_achievements(), len(bkrr_ach_list)):
                        align(0.5, 0.0)
                        style "bkrr_service2"
                        size 42
                        kerning 2.2

                    null height 25

                    viewport:
                        id "menu_ach_viewport"
                        draggable True
                        mousewheel True
                        scrollbars None

                        grid columns rows:
                            spacing 15

                            for ach in bkrr_ach_list:
                                if persistent.bkrr_ach[ach[0]]:
                                    imagebutton:
                                        action NullAction()
                                        idle ("bkrr_ach_" + ach[0])
                                        hover im.MatrixColor(ImageReference("bkrr_ach_" + ach[0]), im.matrix.contrast(1.3))
                                        align(0.75, 0.5)
                                    text ach[1]:
                                        style "bkrr_service2"
                                        size 36
                                        kerning 1.25
                                        align(1.0, 0.5)
                                else:
                                    add im.Alpha(ImageReference("bkrr_ach_blank"), 0.42):
                                        align(0.75, 0.5)
                                    text u"Достижение не открыто.":
                                        style "bkrr_service2"
                                        size 36
                                        kerning 1.25
                                        align(1.0, 0.5)

                            null

                            null

                vbar:
                    value YScrollValue("menu_ach_viewport")
                    bottom_bar Frame(bkrr_ui["img"]["vbar_full"], 0, 0)
                    top_bar Frame(bkrr_ui["img"]["vbar_null"], 0, 0)
                    thumb "null"
                    at Transform(alpha=0.74, align=(0.02, 0.5), xzoom=1.5, yzoom=0.92)

    ##    Экран меню галереи   ##

    screen bkrr_gallery_menu():

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        # Основные элементы

        frame:
            background bkrr_ui["img"]["base"]
            area (0.0, 0.0, 1.0, 1.0)

            # back

            imagebutton:
                action Return()
                idle bkrr_ui["img"]["back"]
                hover bkrr_ui["img"]["back"]
                at bkrr_menu_pos_atl(0.82, 0.86, 0.85, -6.7)

            # plate

            add bkrr_ui["img"]["plate"]:
                at bkrr_menu_pos_atl(1.22, 0.935, 0.132, 27.0)

            # shadows

            add bkrr_ui["img"]["tree_shadow"]:
                at bkrr_menu_tree_shadow_atl

            add bkrr_ui["img"]["shadow"]:
                at bkrr_menu_shadow_atl

            hbox:
                align(0.5, 0.5)
                spacing 40

                for mode in ("bg", "cg"):
                    imagebutton:
                        action Show("bkrr_gallery", transition=dissolve)
                        idle (bkrr_ui["img"][mode])
                        hover im.MatrixColor(bkrr_ui["img"][mode], im.matrix.contrast(1.1))
                        hovered [SetVariable("bkrr_gallery_mode", mode), SetVariable("bkrr_gallery_page", 0)] # пришлось вставить костыль, т. к. множество действий в action по какой-то причине отключает ATL
                        at bkrr_gallery_mode_atl

    ## Экран меню галереи: ATL

    # Общее

    transform bkrr_gallery_mode_atl:
        subpixel True
        truecenter
        on hover:
            ease 0.25 zoom 1.25
        on idle:
            ease 0.1 zoom 1.0

    ##    Экран галереи    ##

    $ bkrr_gallery_mode = None

    $ bkrr_gallery_page = 0

    screen bkrr_gallery():

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        python:

            def gallery_make_thumb(imgf):
                return im.Scale(imgf, 384, 216)

            columns = 2
            rows = 3
            cells = rows * columns

        # Основные элементы

        frame:
            background bkrr_ui["img"]["base"]
            area(0.0, 0.0, 1.0, 1.0)

            # back

            imagebutton:
                action ShowMenu("bkrr_gallery_menu")
                idle bkrr_ui["img"]["back"]
                hover bkrr_ui["img"]["back"]
                at bkrr_menu_pos_atl(0.82, 0.86, 0.85, -6.7)

            # plate

            add bkrr_ui["img"]["plate"]:
                at bkrr_menu_pos_atl(1.22, 0.935, 0.132, 27.0)

            # shadows

            add bkrr_ui["img"]["tree_shadow"]:
                at bkrr_menu_tree_shadow_atl

            add bkrr_ui["img"]["shadow"]:
                at bkrr_menu_shadow_atl

            # gallery

            frame:
                background "#0005"
                area(128, 38, 1080, 985)

                vbox:
                    align(0.5, 0.0)

                    null height 50

                    text u"Галерея":
                        align(0.5, 0.0)
                        style "bkrr_service2"
                        size 42
                        kerning 2.2

                    null height 25

                    hbox:

                        null width 84

                        grid columns rows:
                            spacing 37

                            for img in bkrr_gallery_grid[bkrr_gallery_mode][bkrr_gallery_page]:
                                if (bkrr_gallery_mode, img[0]) in persistent._seen_images.keys():
                                    $ th = gallery_make_thumb(ImageReference((bkrr_gallery_mode, img[0]))) if not img[1] else gallery_make_thumb(img[1])
                                    imagebutton:
                                        action Show("bkrr_gallery_item", transition=bkrr_fade(0.5, color="black"), item=(bkrr_gallery_mode, img[0]))
                                        idle im.Composite((400, 232), (8, 8), im.Sepia(th), (0, 0), im.Alpha(bkrr_ui["img"]["thumbnail_idle"], 0.4), (8, 8), im.Alpha(bkrr_ui["img"]["noise_"+img[2]], 0.3))
                                        hover im.Composite((400, 232), (8, 8), th, (0, 0), bkrr_ui["img"]["thumbnail_hover"])
                                        at bkrr_gallery_item_atl
                                else:
                                    imagebutton:
                                        action NullAction()
                                        auto bkrr_ui["img"]["not_opened_%s_"+img[3]]
                                        at bkrr_gallery_item_atl

                            for i in range(cells - len(bkrr_gallery_grid[bkrr_gallery_mode][bkrr_gallery_page])):
                                null

                        null width 27

                        # pages

                        viewport:
                            id "menu_gallery_viewport"
                            draggable True
                            mousewheel True
                            scrollbars None

                            vbox:
                                yalign 0.5
                                spacing -22

                                for page in range(len(bkrr_gallery_grid[bkrr_gallery_mode])):
                                    if bkrr_gallery_page != page:
                                        imagebutton:
                                            action SetVariable("bkrr_gallery_page", page)
                                            idle im.Alpha(im.FactorScale(bkrr_ui["img"]["button_1"], 0.75), 0.7)
                                            hover im.FactorScale(bkrr_ui["img"]["button_1"], 0.75)
                                            align(0.5, 0.5)
                                    else:
                                        add im.FactorScale(bkrr_ui["img"]["button_2"], 0.6):
                                            align(0.5, 0.5)

    ## Экран галереи: ATL

    # Общее

    transform bkrr_gallery_item_atl:
        subpixel True
        truecenter
        on hover:
            ease 0.25 zoom 0.95
        on idle:
            ease 0.1 zoom 1.0

    ##    Экран просмотра элементов галереи    ##

    screen bkrr_gallery_item(item):

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        imagebutton:
            action Show("bkrr_gallery", transition=Fade(0.25, 0.0, 0.25, color="#000"))
            idle ImageReference(item)
            hover ImageReference(item)

    ##    Экран выбора спрайтов для новых персонажей    ##

    screen bkrr_sprites_pref():

        tag menu
        modal True

        key "game_menu":
            action NullAction()

        key "screenshot":
            action NullAction()

        # functions

        python:

            sprites_pref_action = Play("test_one", bkrr_ui["sound"]["paper"])

            def togglePersistentDictKey(persistentDict, key):
                persistentDict[key] = not persistentDict[key]

            TogglePDK = renpy.curry(togglePersistentDictKey)

        # Основные элементы

        frame:
            background bkrr_ui["img"]["base"]
            area(0.0, 0.0, 1.0, 1.0)

            # photos

            add im.Sepia(bkrr_ui["img"]["bg"]):
                at bkrr_menu_pos_atl(2.3, 0.86, 0.85, -9.7)

            add im.Sepia(bkrr_ui["img"]["cg"]):
                at bkrr_menu_pos_atl(2.6, 0.178, 0.82, 13.4)

            # back

            imagebutton:
                action Return()
                idle bkrr_ui["img"]["back"]
                hover bkrr_ui["img"]["back"]
                at bkrr_menu_pos_atl(0.82, 0.86, 0.85, -6.7)

            # plate

            add bkrr_ui["img"]["plate"]:
                at bkrr_menu_pos_atl(1.22, 0.935, 0.132, 27.0)

            # shadows

            # необходимость перезагрузки экрана после каждого переключения спрайтов лишает нас возможности использовать анимацию в данном экране
            #add bkrr_ui["img"]["tree_shadow"]:
                #at bkrr_menu_tree_shadow_atl

            add bkrr_ui["img"]["shadow"]:
                at bkrr_menu_shadow_atl

            # triggers

            frame:
                background "#0005"
                area(128, 38, 1160, 985)

                vbox:

                    null height 50

                    text u"Выбор спрайтов":
                        align(0.5, 0.0)
                        style "bkrr_service2"
                        size 42
                        kerning 2.2

                    null height 25

                    viewport:
                        id "menu_spr_viewport"
                        draggable True
                        mousewheel True
                        scrollbars None
                        at Transform(align=(0.5, 0.0))

                        vbox:
                            for character in (("nt", "Натальи"), ("tol", "Толика")):
                                $ char_img = [im.FactorScale(bkrr_ui["img"][character[0]+"_"+img], 0.5) for img in ("on", "off", "new_on", "new_off")]
                                vbox:
                                    align(0.5, 0.0)
                                    xfill True
                                    text u"Спрайты %s" % (character[1]):
                                        align(0.5, 0.0)
                                        style "bkrr_service2"
                                        size 36
                                        kerning 1.25
                                    null height 10
                                    hbox:
                                        align(0.5, 0.0)
                                        spacing 75
                                        imagebutton:
                                            align(0.5, 1.0)
                                            if persistent.bkrr_old_sprites[character[0]]:
                                                idle char_img[1]
                                                action [sprites_pref_action, TogglePDK(persistent.bkrr_old_sprites, character[0]), ShowMenu("bkrr_sprites_pref")]
                                            else:
                                                idle char_img[0]
                                                action NullAction()
                                            hover char_img[0]
                                        imagebutton:
                                            align(0.5, 1.0)
                                            if persistent.bkrr_old_sprites[character[0]]:
                                                idle char_img[2]
                                                action NullAction()
                                            else:
                                                idle char_img[3]
                                                action [sprites_pref_action, TogglePDK(persistent.bkrr_old_sprites, character[0]), ShowMenu("bkrr_sprites_pref")]
                                            hover char_img[2]
                                    null height 75

                            null height 15

                            textbutton u"Применить":
                                align(0.5, 0.0)
                                background None
                                text_style "bkrr_service2"
                                text_size 36
                                text_hover_color "#00FF3E"
                                text_kerning 1.25
                                action (Function(stop_music), Function(renpy.utter_restart))

                            text u"(игра будет перезапущена)":
                                align(0.5, 0.0)
                                style "bkrr_service2"
                                size 36
                                kerning 1.25

                vbar:
                    value YScrollValue("menu_spr_viewport")
                    bottom_bar Frame(bkrr_ui["img"]["vbar_full"], 0, 0)
                    top_bar Frame(bkrr_ui["img"]["vbar_null"], 0, 0)
                    thumb "null"
                    at Transform(alpha=0.74, align=(0.02, 0.5), xzoom=1.5, yzoom=0.92)

    screen bkrr_disable_keys():
        key "mouseup_1" action NullAction()
        key "K_RETURN" action NullAction()
        key "K_SPACE" action NullAction()
        key "K_KP_ENTER" action NullAction()
        key "joy_dismiss" action NullAction()
