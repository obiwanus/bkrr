﻿
#    Булки, кефир и рок-н-ролл. Функции, параметры, ресурсы    #

init python:

    # Импорт модулей

    import random

    # Название мода

    bkrr_title = (
        u"Булки, кефир и рок-н-ролл",
        u"БКРР",
        u"День кота",
        u"Яой-рут" #TODO
    )

    # Возможные пути к графическим ресурсам для совместимости с обеими версиями

    ES_IMAGES = "images/" if config.version == "1.2" else "images/1080/"
    MOD_IMAGES = "mods/bkrr/images/"

    # Функция, составляющая словарь ссылок на файлы в определённой директории

    def bkrr_form_files_list(path):
        return {i[len(path):i.rfind(".")]:i for i in renpy.list_files() if i.startswith(path)}

    ##    Функции и параметры обработки изображений    ##

    def bkrr_make_rainy_img(imgf):
        return im.MatrixColor(imgf, im.matrix.brightness(-0.1) * im.matrix.saturation(0.4) * im.matrix.contrast(0.95) * bkrr_tint["night"])

    def bkrr_make_sepia_img(imgn):
        return im.Sepia(ImageReference(imgn))

    ## Тонировка изображений

    # в соответствии со временем суток

    bkrr_tint = {
        "sunset":im.matrix.tint(0.94, 0.82, 1.0),
        "night":im.matrix.tint(0.63, 0.78, 0.82)
    }

    # и в конкретный цвет (для простоты – через функцию)

    def bkrr_make_tint_img(imgf, color):
        tc = {
            "red":(1.0, 0.35, 0.35),
            "green_yellow":(0.91, 1.0, 0.59),
            "cyan":(0.0, 1.0, 0.8)
        }
        r, g, b = tc[color]
        return im.MatrixColor(imgf, im.matrix.tint(r, g, b))

    # Функция для быстрого создания зацикленной анимации

    def bkrr_create_anim(img, amount, pause=0.5, transition=None):
        args = list()
        for number in range(1, amount + 1):
            args.append(im.Image(img + str(number) + ".png"))
            args.append(pause)
            args.append(transition)
        return anim.TransitionAnimation(*args)

    # Функции для быстрого собирания "бутербродов"

    def bkrr_fast_composite(*args):
        arg_list = list()
        for arg in args:
            arg_list.append((0, 0))
            arg_list.append(arg)
        return im.Composite((config.screen_width, config.screen_height), *arg_list)

    def bkrr_fast_livecomposite(*args):
        arg_list = list()
        for arg in args:
            arg_list.append((0, 0))
            arg_list.append(arg)
        return LiveComposite((config.screen_width, config.screen_height), *arg_list)

    # Простенькая расфокусировка изображения

    def bkrr_offset_defocusing(imgn, xstep=4, ystep=2, intensity=3):
        args = list()
        for i in range(1, intensity+1):
            offset = {1:(xstep, 0), 2:(0, ystep), 3:(-xstep, 0), 4:(0, -ystep)}
            for j in offset.values():
                args.append((j[0]*i, j[1]*i))
                args.append(Transform(imgn, alpha=random.uniform(0.1, 0.2)))
        return LiveComposite((config.screen_width, config.screen_height), (0, 0), imgn, *args)

    ##    Звуковые функции    ##

    def bkrr_mute(fade=2.5):
        for channel in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music", "test_one", "test_two"):
            renpy.music.stop(channel=channel, fadeout=fade)

    def bkrr_set_volume(channel, value, fade=0.0): # для удобства
        renpy.music.set_volume(volume=value, delay=fade, channel=channel)

    def bkrr_play_random(list, channel="sound"):
        renpy.play(random.choice(list), channel=channel)

    ##    Настройки и ресурсы экранов мода    ##

    bkrr_ui = dict()

    # Перечень дней, доступных по умолчанию

    if not persistent.bkrr_ep4_started:
        persistent.bkrr_ep4_started = True
        persistent.bkrr_check = {4:True, 5:True, 6:True, 7:True, 8:True, 9:True, 10:True, 11:True, 12:True, 13:True, 14:True, 15:True, 16:True, 17:False, 18:False, 19:False, "epilogue":False, "credits4":False}

    # Графические элементы меню

    bkrr_ui["img"] = {img:(MOD_IMAGES + "ui/menu/" + img + ".png") for img in ("achievements", "back", "base", "catday", "credits", "epilogue", "gallery", "main_menu", "plate", "prologue", "shadow", "steam", "tree_shadow", "vbar_full", "vbar_null", "vk")}

    for dn in range(4, 20):
        bkrr_ui["img"]["day"+str(dn)] = (MOD_IMAGES + "ui/menu/day" + str(dn) + ".png", random.randint(-15, 15))

    # Звуковые элементы меню

    bkrr_ui["sound"] = {
        "paper":"mods/bkrr/sound/ui/paper.ogg",
        "plate_stop":"mods/bkrr/sound/ui/plate_stop.ogg",
        "meow":"mods/bkrr/sound/sfx/meow4.ogg"
    }

    # Ссылки на страницы мода

    bkrr_ui["hyperlinks"] = {
        "vk":"http://vk.com/b_k_r_r",
        "steam":"http://steamcommunity.com/sharedfiles/filedetails/?id=451835368"
    }

    # Графические элементы галереи

    for img in ("bg", "button_1", "button_2", "cg", "noise_1", "noise_2", "noise_3", "noise_4", "not_opened_%s_1", "not_opened_%s_2", "not_opened_%s_3", "thumbnail_idle", "thumbnail_hover"):
        bkrr_ui["img"][img] = MOD_IMAGES + "ui/gallery/" + img + ".png"

    # Список ресурсов галереи

    bkrr_gallery_grid = {
        "bg":(
            (["ext_music_club_verandah_day_v1", False], ["ext_music_club_verandah_day_v7", False], ["ext_music_club_verandah_night_v2", False], ["int_music_club_mattresses_day", False], ["int_music_club_mattresses_sunset", False], ["int_music_club_mattresses_night", False]),
            (["int_cinema_people", False], ["int_shed_bkrr_v1", False], ["int_old_building_room_day_rainy_bkrr", MOD_IMAGES + "bg/int_old_building_room_day_rainy.jpg"], ["int_old_building_room_night_bkrr_v1", bkrr_fast_composite(MOD_IMAGES + "bg/int_old_building_room_night_rainy.jpg", MOD_IMAGES + "misc/int_old_building_room_mugs_fire.png", MOD_IMAGES + "misc/int_old_building_room_fire1.png", MOD_IMAGES + "misc/int_old_building_room_steam1.png")], ["int_old_building_room_day_bkrr_v2", False], ["ext_path3_day_bkrr", False]),
            (["semen_room_clean_bkrr", False], ["ext_beach_water_day", MOD_IMAGES + "bg/ext_beach_water_day.jpg"], ["int_infirmary_day", False], ["int_infirmary_sunset", False], ["int_infirmary_night", False], ["int_infirmary_day_guitar", False]),
            (["int_infirmary_sunset_guitar", False], ["int_infirmary_night_guitar", False], ["int_infirmary_night_v2", False], ["int_infirmary_night_guitar_v2", False], ["int_infirmary_night_v3", False], ["int_infirmary_night_guitar_v3", False])
        ),
        "cg":(
            (["d5_cat_in_ventilation", False], ["d5_ghost", False], ["d6_sl_ass", False], ["d6_on_floor", False], ["d6_dv_guitar", False], ["d6_sem_guitar", False]),
            (["d7_mi_embrace", False], ["d7_mi_dance", False], ["d7_mi_walking", False], ["d8_deer", im.Crop(MOD_IMAGES + "cg/d8_deer.jpg", 0, 180, 1920, 1080)], ["d8_chibi", False], ["d8_fstar_main", False]),
            (["d9_walking", bkrr_fast_composite(ES_IMAGES + "bg/ext_houses_day.jpg", MOD_IMAGES + "cg/d9_walking.png")], ["d9_wounded_dv_1", False], ["d9_wounded_dv_2", False], ["d9_squirrel_1", False], ["d9_squirrel_2", False], ["d9_kiss", False]),
            (["d10_ghost", False], ["d11_shirt_1", im.Crop(MOD_IMAGES + "cg/d11_shirt.jpg", 0, 180, 1920, 1080)], ["d11_forest", im.Crop(MOD_IMAGES + "cg/d11_forest.jpg", 0, 0, 1920, 1080)], ["d11_forest_view_with_shadow", False], ["d11_forest_view_with_pi", False], ["d11_mi_sleep_1", MOD_IMAGES + "cg/d11_mi_sleep_1.png"]),
            (["d11_mi_sleep_2", MOD_IMAGES + "cg/d11_mi_sleep_2.png"], ["d11_mi_sleep_3", im.Composite((config.screen_width, config.screen_height), (0, 0), MOD_IMAGES + "cg/d11_mi_sleep_1.png", (1250, 375), im.Crop(MOD_IMAGES + "cg/d11_mi_sleep_2.png", 1250, 375, 100, 100))], ["d11_night_guest", False], ["d12_mi_hair_sl", False], ["d12_mi_hair_sem", False], ["d12_mi_hair_sem_bite", False]),
            (["d12_mi_bath_1", False], ["d12_mi_bath_2", False], ["d12_noon_rest_1", False], ["d12_noon_rest_2", False], ["d12_noon_rest_3", False], ["d12_noon_rest_4", False]),
            (["d12_noon_rest_5", False], ["d12_us_kiss_2", False], ["d12_us_kiss_3", False], ["d12_us_kiss_4", False], ["d12_us_kiss_5", False], ["d12_us_kiss_6", MOD_IMAGES + "cg/d12_us_kiss_6.png"]),
            (["d13_beach", False], ["d14_un_sleep", False], ["d14_us_fall", False], ["d14_un_cry", False], ["d14_dv_spy", False], ["d14_dv_window_1", False]),
            (["d14_dv_window_2", False], ["d14_mi_confession_1", False], ["d14_mi_confession_2", False], ["d14_mi_confession_3", False], ["d14_mi_confession_4", False], ["d14_rocket_1", False]),
            (["d14_rocket_2", MOD_IMAGES + "cg/d14_rocket_2.png"], ["d15_mi_sleep", False], ["d16_cryptography", False], ["d16_gulls", False], ["catday_warp_cat", False])
        )
    }

    for grid in bkrr_gallery_grid.values():
        for page in grid:
            for img in page:
                img.append(str(random.randrange(1, 5, 1)))
                img.append(str(random.randrange(1, 4, 1)))

    ##    Интерфейс и игровой процесс    ##

    # Таймскип

    def bkrr_timeskip(sounded=True, desaturated=False):
        renpy.scene()
        renpy.show("bg black")
        renpy.with_statement(dissolve)
        if sounded:
            renpy.play(bkrr_sfx_list["clock_transition_sound"], channel="sound")
        if desaturated:
            renpy.show("bkrr_timeskip_logo desaturated")
        else:
            renpy.show("bkrr_timeskip_logo")
        renpy.with_statement(bkrr_timeskip_transition(2.0))
        renpy.hide("bkrr_timeskip_logo")
        renpy.with_statement(bkrr_timeskip_transition(2.0))
        if sounded:
            renpy.music.stop(channel="sound", fadeout=2.0)

    def bkrr_timeskip_short():
        renpy.play(bkrr_sfx_list["clock_transition_sound"], channel="sound")
        renpy.scene()
        renpy.show("bg black")
        renpy.with_statement(bkrr_timeskip_transition())
        renpy.music.stop(channel="sound", fadeout=1.0)

    # Создание / объявление персонажей

    bkrr_characters = {
        # основные
        "narrator":[None, None],
        "th":[None, None],
        "me":[u"Семён", "#E1DD7D"],
        # персонажи оригинала
        "mi":[u"Мику", "#00DEFF"],
        "us":[u"Ульяна", "#FF3200"],
        "dv":[u"Алиса", "#FFAA00"],
        "mt":[u"Ольга", "#00EA32"],
        "mz":[u"Женя", "#4A86FF"],
        "sh":[u"Шурик", "#FFF226"],
        "sl":[u"Славя", "#FFD200"],
        "el":[u"Электроник", "#FFFF00"],
        "un":[u"Лена", "#B956FF"],
        "cs":[u"Виола", "#A5A5FF"],
        "pi":[u"Пионер", "#E60000"],
        "uv":[u"Юля", "#4EFF00"],
        # новые персонажи
        "nt":[u"Наталья", "#418AF9"],
        "tol":[u"Толик", "#B3B3B3"],
        "cat":[u"Пират", "#B6DAF1"],
        "ant":[u"Антон", "#F9D277"],
        "kla":[u"Клаус", "#CC4D14"],
        "tr":[u"Трук", "#CCC"],
        "kla_unk":[u"Рыжий пионер", "#CC4D14"],
        "tr_unk":[u"Маленький пионер", "#CCC"],
        "ant_unk":[u"Мужчина", "#F9D277"],
        "vz":[u"Возница", "#FFFFB8"],
        # специальные
        "dy":[u"Голос из динамика", "#B3B3B3"], # для 1.2
        "bus":[u"Автобус", "#68A01D"],
        "t_pl":[u"Магнитофон", "#B3B3B3"]
    }

    renpy.image("bkrr_radio_icon", im.FactorScale(MOD_IMAGES + "ui/dialogue_box/radio_icon.png", 0.051))
    renpy.image("bkrr_speaker_icon", im.FactorScale(MOD_IMAGES + "ui/dialogue_box/speaker_icon.png", 0.051))

    def bkrr_chars_define(kind=adv):
        gl = globals()
        if kind == nvl:
            who_suffix = ":"
            ctc = "ctc_animation_nvl"
        else:
            who_suffix = ""
            ctc = "ctc_animation"
        what_color = "#FFDD7D"
        drop_shadow = (2, 2)
        for i, j in bkrr_characters.items():
            if i == "narrator":
                gl[i] = Character(None, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
            elif i == "th":
                gl[i] = Character(None, kind=kind, what_color=what_color, what_drop_shadow=drop_shadow, what_prefix="~ ", what_suffix=" ~", ctc=ctc, ctc_position="fixed")
            else:
                gl[i] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                gl[i+"_r"] = Character(j[0], kind=kind, who_color=what_color, who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                gl[i+"_v"] = Character(u"Голос", kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                gl[i+"_radio"] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_prefix=" {image=bkrr_radio_icon} ", what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")
                gl[i+"_speaker"] = Character(j[0], kind=kind, who_color=j[1], who_drop_shadow=drop_shadow, who_suffix=who_suffix, what_color=what_color, what_prefix=" {image=bkrr_speaker_icon} ", what_drop_shadow=drop_shadow, ctc=ctc, ctc_position="fixed")

    # Создание / объявление парных персонажей

    def bkrr_double_char_define(first, second, time_of_day):
        colors = {
            "day":"#80A055",
            "sunset":"#CDAF69",
            "night":"#36B198"
        }
        gl = globals()
        what_color = "#FFDD7D"
        drop_shadow = (2, 2)
        character = "{color=%s}%s{/color} {color=%s}|{/color} {color=%s}%s{/color}" % (bkrr_characters[first][1], bkrr_characters[first][0], colors[time_of_day], bkrr_characters[second][1], bkrr_characters[second][0])
        gl[first + "_" + second + "_" + time_of_day[0]] = Character(character, kind=adv, what_color=what_color, what_drop_shadow=drop_shadow, ctc="ctc_animation", ctc_position="fixed")

    for i in (("me", "tol", "day"), ("sl", "mz", "sunset"), ("dv", "us", "day"), ("dv", "us", "sunset"), ("cs", "mi", "sunset"), ("me", "cs", "day"), ("me", "mi", "day")):
        bkrr_double_char_define(i[0], i[1], i[2])

    # Переключение режима и смена имён

    def bkrr_set_mode(mode=adv):
        nvl_clear()
        bkrr_chars_define(kind=mode)

    def bkrr_set_name(name, value):
        bkrr_characters[name][0] = value
        bkrr_chars_define()

    # Настройка интерфейса и тонировки спрайтов

    def bkrr_set_time(time_of_day="day", sprite_time=None):
        persistent.timeofday = time_of_day
        if sprite_time == None:
            if time_of_day == "prologue":
                sprite_time = "night"
            else:
                sprite_time = time_of_day
        persistent.sprite_time = sprite_time

    # Функция, возвращающая текущее время суток

    def bkrr_get_usertime():
        from time import strftime, localtime
        time = strftime("%H:%M:%S", localtime())
        hour, min, sec = time.split(":")
        hour = int(hour)
        if 9 < hour < 19:
            return "day"
        elif 5 < hour > 18:
            return "sunset"
        elif 20 > hour >= 0:
            return "night"

    # Функция, назначающая имя сохранения

    def bkrr_set_savename(ch):
        global save_name
        if config.version == "1.2":
            title = bkrr_title[0] + "\n"
        else:
            title = bkrr_title[1] + ". " # в 1.1 используется аббревиатура
        if ch in range(4, 20):
            save_name = title + u"День №" + str(ch)
        else:
            save_name = title + ch

    # Бэкдроп, назначение имени сохранения, сброс параметров, звуков и т. д.

    def bkrr_new_chapter(ch):
        # renpy.block_rollback()
        bkrr_set_mode()
        bkrr_mute(1.0)
        for channel in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music", "test_one", "test_two"):
            bkrr_set_volume(channel, 1.0, 0.0)
        bkrr_set_savename(ch)
        renpy.scene()
        renpy.show("black")
        renpy.with_statement(Dissolve(2.0))
        bkrr_set_time()
        if ch in range(4, 20):
            renpy.pause(1.0, hard=True)
            renpy.movie_cutscene(bkrr_video_list["backdrop"][ch], delay=14.0)
        elif ch == u"Эпилог":
            renpy.pause(1.0, hard=True)
            renpy.movie_cutscene(bkrr_video_list["backdrop"]["epilogue"], delay=21.0)

    ## Предметы и ачивменты

    # Регистрация ачивментов и предметов

    bkrr_ach_list = (
        ("start", u"Запустить 1-ое демо."),
        ("pedobear", u"На охоту с Ульянкой!"),
        ("bass", u"Вступить в муз. кружок."),
        # ("hatiko", u"Дождаться 2-го эпизода."), # не актуально
        ("squirrel", u"Сорванный поцелуй."),
        ("catday", u"Превратиться в кота."),
        # ("far", u"Проснуться с Мику."), # не актуально
        ("bath", u"С лёгким паром!"),
        ("cold", u"Живо в изолятор!"),
        ("bass2", u"Наш басист – молодец!"),
        ("exactly_what_you_think", u"Да. Именно."),
    )

    if not persistent.bkrr_ach:
        persistent.bkrr_ach = dict()

    for ach in bkrr_ach_list:
        renpy.image("bkrr_ach_" + ach[0], im.Scale(MOD_IMAGES + "ui/achievements/" + ach[0] + ".png", 450, 125))
        if ach[0] not in persistent.bkrr_ach:
            persistent.bkrr_ach[ach[0]] = False

    renpy.image("bkrr_ach_blank", im.Scale(MOD_IMAGES + "ui/achievements/blank.png", 450, 125))

    bkrr_item_list = ("knife", "paint", "tape", "key", "food", "powder", "accumulator", "comb", "pills", "apple", "note", "shark_tooth", "matchbox")

    for item in bkrr_item_list:
        renpy.image("bkrr_item_" + item, im.Scale(MOD_IMAGES + "ui/items/" + item + ".png", 450, 360))

    # Вывод ачивментов и предметов

    def bkrr_get_achievement(ach):
        if not persistent.bkrr_ach[ach]:
            persistent.bkrr_ach[ach] = True
            renpy.play(sfx_achievement, channel="sound")
            renpy.show("bkrr_ach_" + ach, [bkrr_get_achievement_atl])
            renpy.pause(7.5)
            renpy.hide("bkrr_ach_" + ach)

    def bkrr_get_all_achievements():
        for ach in bkrr_ach_list:
            bkrr_get_achievement(ach[0])

    def bkrr_get_item(item, sounded=True):
        if sounded:
            renpy.play(bkrr_sfx_list["get_item"], channel="sound")
        renpy.show("bkrr_item_%s" % item, [bkrr_get_item_atl])
        renpy.pause(5.0)
        renpy.hide("bkrr_item_%s" % item)

    # Прочие операции с ачивментами

    def bkrr_check_achievements():
        j = 0
        for i in persistent.bkrr_ach.values():
            if i:
                j += 1
        return j

    def bkrr_reset_achievements():
        for ach in bkrr_ach_list:
            persistent.bkrr_ach[ach[0]] = False

init 2:

    ##    Логотип    ##

    # Обычный логотип

    image bkrr_logo = im.Image(MOD_IMAGES + "ui/logo.png", xalign=0.5, yalign=0.5)

    # Логотип для таймскипа и его ATL

    $ bkrr_timeskip_logo_normal = im.FactorScale(MOD_IMAGES + "ui/logo.png", 0.5)
    $ bkrr_timeskip_logo_desaturated = im.MatrixColor(bkrr_timeskip_logo_normal, im.matrix.saturation(0.5))
    $ bkrr_timeskip_logo_flash = im.MatrixColor(bkrr_timeskip_logo_normal, im.matrix.brightness(0.25))

    image bkrr_timeskip_logo:
        contains:
            bkrr_timeskip_logo_normal
            bkrr_timeskip_logo_atl
        contains:
            bkrr_timeskip_logo_flash
            parallel:
                bkrr_timeskip_logo_atl
            parallel:
                bkrr_timeskip_logo_flash_atl

    image bkrr_timeskip_logo desaturated:
        contains:
            bkrr_timeskip_logo_desaturated
            bkrr_timeskip_logo_atl
        contains:
            bkrr_timeskip_logo_flash
            parallel:
                bkrr_timeskip_logo_atl
            parallel:
                bkrr_timeskip_logo_flash_atl

    transform bkrr_timeskip_logo_atl:
        truecenter
        subpixel True
        block:
            ease 0.25 zoom 1.025
            ease 0.25 zoom 1.0
            repeat

    transform bkrr_timeskip_logo_flash_atl:
        alpha 0.0
        block:
            ease 0.25 alpha 0.5
            ease 0.25 alpha 0.0
            repeat

    ##    Фоны    ##

    # Заливка и прочее

    image null = Null(0, 0)
    image bg null = Null(config.screen_width, config.screen_height)

    image black = Solid("#000")
    image white = Solid("#FFF")
    image red = Solid("#F00")

    # Новые фоны

    image bg ext_music_club_verandah_day_v1 = MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg" # версия без плакатов, используется в прологе и 4-6 днях
    image bg ext_music_club_verandah_day_v2 = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png") # версия с плакатами, используется в 7 дне
    image bg ext_music_club_verandah_day_v3 = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png", MOD_IMAGES + "misc/ext_music_club_verandah_text1.png") # версия с плакатами и первой надписью, используется в 8 дне
    image bg ext_music_club_verandah_day_v4 = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png", MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", MOD_IMAGES + "misc/ext_music_club_verandah_text2.png") # версия с плакатами, первой и второй надписями, используется в 9 дне
    image bg ext_music_club_verandah_day_v5 = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png", MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", MOD_IMAGES + "misc/ext_music_club_verandah_text2.png", MOD_IMAGES + "misc/ext_music_club_verandah_text3.png") # версия с плакатами, 1-3 надписями, используется в 10 и 11 дне (см. пасмурную версию)
    image bg ext_music_club_verandah_day_v6 = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png", MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", MOD_IMAGES + "misc/ext_music_club_verandah_text2.png", MOD_IMAGES + "misc/ext_music_club_verandah_text3.png", MOD_IMAGES + "misc/ext_music_club_verandah_text4.png") # версия с плакатами, 1-4 надписями, используется в 12 дне
    image bg ext_music_club_verandah_day_v7 = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png", MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", MOD_IMAGES + "misc/ext_music_club_verandah_text2.png", MOD_IMAGES + "misc/ext_music_club_verandah_text3.png", MOD_IMAGES + "misc/ext_music_club_verandah_text4.png", MOD_IMAGES + "misc/ext_music_club_verandah_text5.png") # версия с плакатами, 1-5 надписями, используется в 13 дне
    image bg ext_music_club_verandah_day_v8 = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png", MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", MOD_IMAGES + "misc/ext_music_club_verandah_text2.png", MOD_IMAGES + "misc/ext_music_club_verandah_text3.png", MOD_IMAGES + "misc/ext_music_club_verandah_text4.png", MOD_IMAGES + "misc/ext_music_club_verandah_text5.png", MOD_IMAGES + "misc/ext_music_club_verandah_text6.png") # версия с плакатами, 1-6 надписями, используется в 14 дне
    image bg ext_music_club_verandah_day_v9 = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png", MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", MOD_IMAGES + "misc/ext_music_club_verandah_text2.png", MOD_IMAGES + "misc/ext_music_club_verandah_text3.png", MOD_IMAGES + "misc/ext_music_club_verandah_text4.png", MOD_IMAGES + "misc/ext_music_club_verandah_text5.png", MOD_IMAGES + "misc/ext_music_club_verandah_text6.png", MOD_IMAGES + "misc/ext_music_club_verandah_text7.png") # версия с плакатами, 1-7 надписями, используется в 15 дне
    image bg ext_music_club_verandah_day_v9_ajar = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png", MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", MOD_IMAGES + "misc/ext_music_club_verandah_text2.png", MOD_IMAGES + "misc/ext_music_club_verandah_text3.png", MOD_IMAGES + "misc/ext_music_club_verandah_text4.png", MOD_IMAGES + "misc/ext_music_club_verandah_text5.png", MOD_IMAGES + "misc/ext_music_club_verandah_text6.png", MOD_IMAGES + "misc/ext_music_club_verandah_text7.png", MOD_IMAGES + "misc/ext_music_club_verandah_day_ajar.png")
    image ext_music_club_verandah_day_v9_blocker = MOD_IMAGES + "misc/ext_music_club_verandah_day_blocker.png"
    image ext_music_club_verandah_day_v9_double = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png", MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", MOD_IMAGES + "misc/ext_music_club_verandah_text2.png", MOD_IMAGES + "misc/ext_music_club_verandah_text3.png", MOD_IMAGES + "misc/ext_music_club_verandah_text4.png", MOD_IMAGES + "misc/ext_music_club_verandah_text5.png", MOD_IMAGES + "misc/ext_music_club_verandah_text6.png", MOD_IMAGES + "misc/ext_music_club_verandah_text7.png") # версия с плакатами, 1-7 надписями, используется в 15 дне

    image bg ext_music_club_verandah_night_v1 = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_night.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_night_posters.png", im.Alpha(MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", 0.3), im.Alpha(MOD_IMAGES + "misc/ext_music_club_verandah_text2.png", 0.3)) # версия с плакатами, первой и второй надписями, используется в 9 дне, ночной вариант веранды v4
    image bg ext_music_club_verandah_night_v2 = bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_night.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_night_posters.png", im.Alpha(MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", 0.3), im.Alpha(MOD_IMAGES + "misc/ext_music_club_verandah_text2.png", 0.3), im.Alpha(MOD_IMAGES + "misc/ext_music_club_verandah_text3.png", 0.3), im.Alpha(MOD_IMAGES + "misc/ext_music_club_verandah_text4.png", 0.3)) # версия с плакатами, 1-4 надписями, используется в 12 дне, ночной вариант веранды v6

    image bg int_music_club_mattresses_day = bkrr_fast_composite(MOD_IMAGES + "bg/int_music_club_mattresses_day.jpg", MOD_IMAGES + "misc/int_music_club_clock_day.png")
    image bg int_music_club_mattresses_sunset = bkrr_fast_composite(MOD_IMAGES + "bg/int_music_club_mattresses_sunset.jpg", MOD_IMAGES + "misc/int_music_club_clock_sunset.png")
    image bg int_music_club_mattresses_night =bkrr_fast_composite(MOD_IMAGES + "bg/int_music_club_mattresses_night.jpg", MOD_IMAGES + "misc/int_music_club_clock_night.png")
    image bg int_music_club_mattresses_dark_night = im.MatrixColor(bkrr_fast_composite(MOD_IMAGES + "bg/int_music_club_mattresses_night.jpg", MOD_IMAGES + "misc/int_music_club_clock_night.png"), im.matrix.brightness(-0.15) * im.matrix.saturation(0.6))

    image bg int_cinema_empty = MOD_IMAGES + "bg/int_cinema_empty.png"
    image bg int_cinema_people = MOD_IMAGES + "bg/int_cinema_people.png"
    image bg int_cinema_movie = MOD_IMAGES + "bg/int_cinema_movie.png"

    image bg int_shed_bkrr_v1 = bkrr_fast_composite(MOD_IMAGES + "bg/int_shed.jpg", MOD_IMAGES + "misc/int_shed_plank1.png")
    image bg int_shed_bkrr_v2 = bkrr_fast_composite(MOD_IMAGES + "bg/int_shed.jpg", MOD_IMAGES + "misc/int_shed_plank2.png")

    image bg int_old_building_room_day_rainy_bkrr = bkrr_fast_livecomposite(MOD_IMAGES + "bg/int_old_building_room_day_rainy.jpg", bkrr_create_anim(MOD_IMAGES + "misc/int_old_building_room_rain", 3, 0.15, Dissolve(0.15, alpha=True)))

    image bg int_old_building_room_night_bkrr_v1 = bkrr_fast_livecomposite(MOD_IMAGES + "bg/int_old_building_room_night_rainy.jpg", MOD_IMAGES + "misc/int_old_building_room_mugs_fire.png", bkrr_glow_atl(MOD_IMAGES + "misc/int_old_building_room_flash1.png"), bkrr_glow_atl(MOD_IMAGES + "misc/int_old_building_room_flash2.png"), bkrr_glow_atl(MOD_IMAGES + "misc/int_old_building_room_flash3.png"), bkrr_create_anim(MOD_IMAGES + "misc/int_old_building_room_fire", 3, 0.5, Dissolve(0.5, alpha=True)), bkrr_create_anim(MOD_IMAGES + "misc/int_old_building_room_steam", 3, 0.3, Dissolve(0.3, alpha=True)))
    image bg int_old_building_room_night_bkrr_v2 = bkrr_fast_livecomposite(MOD_IMAGES + "bg/int_old_building_room_night_rainy.jpg", bkrr_glow_atl(MOD_IMAGES + "misc/int_old_building_room_flash1.png"), bkrr_glow_atl(MOD_IMAGES + "misc/int_old_building_room_flash2.png"), bkrr_glow_atl(MOD_IMAGES + "misc/int_old_building_room_flash3.png"), bkrr_create_anim(MOD_IMAGES + "misc/int_old_building_room_fire", 3, 0.5, Dissolve(0.5, alpha=True)))

    image bg int_old_building_room_day_bkrr_v1 = MOD_IMAGES + "bg/int_old_building_room_day.png"
    image bg int_old_building_room_day_bkrr_v2 = bkrr_fast_composite(MOD_IMAGES + "bg/int_old_building_room_day.png", MOD_IMAGES + "misc/int_old_building_room_mugs.png")

    image bg int_infirmary_day = MOD_IMAGES + "bg/int_infirmary_day.png"
    image bg int_infirmary_sunset = im.MatrixColor(MOD_IMAGES + "bg/int_infirmary_day.png", bkrr_tint["sunset"] * im.matrix.contrast(1.3))
    image bg int_infirmary_night = MOD_IMAGES + "bg/int_infirmary_night.png"

    image bg int_infirmary_day_guitar = MOD_IMAGES + "bg/int_infirmary_day_guitar.png"
    image bg int_infirmary_sunset_guitar = im.MatrixColor(MOD_IMAGES + "bg/int_infirmary_day_guitar.png", bkrr_tint["sunset"] * im.matrix.contrast(1.3))
    image bg int_infirmary_night_guitar = MOD_IMAGES + "bg/int_infirmary_night_guitar.png"

    image bg int_infirmary_night_v2 = MOD_IMAGES + "bg/int_infirmary_night_v2.png"
    image bg int_infirmary_night_guitar_v2 = MOD_IMAGES + "bg/int_infirmary_night_guitar_v2.png"
    image bg int_infirmary_night_v3 = MOD_IMAGES + "bg/int_infirmary_night_v3.png"
    image bg int_infirmary_night_guitar_v3 = MOD_IMAGES + "bg/int_infirmary_night_guitar_v3.png"

    image bg ext_path3_day_bkrr = MOD_IMAGES + "bg/ext_path3_day.jpg"

    image bg ext_pier_day = MOD_IMAGES + "bg/ext_pier_day.jpg"
    image bg ext_pier_sunset = im.MatrixColor(MOD_IMAGES + "bg/ext_pier_day.jpg", bkrr_tint["sunset"])

    # "Новые" фоны из модпака, из инета, дополненные, отредактированные и переобъявленные оригинальные и пр.

    image bg int_dining_hall_people_sunset_bkrr = MOD_IMAGES + "bg/int_dining_hall_people_sunset.jpg"
    image bg ext_houses_night_bkrr = MOD_IMAGES + "bg/ext_houses_night.jpg"
    image bg ext_aidpost_sunset_bkrr = MOD_IMAGES + "bg/ext_aidpost_sunset.jpg"
    image bg ext_boathouse_sunset_bkrr = MOD_IMAGES + "bg/ext_boathouse_sunset.jpg"
    image bg ext_library_sunset_bkrr = MOD_IMAGES + "bg/ext_library_sunset.jpg"
    image bg ext_storage_day_bkrr = MOD_IMAGES + "bg/ext_storage_day.png"
    image bg ext_storage_sunset_bkrr = MOD_IMAGES + "bg/ext_storage_sunset.jpg"
    image bg ext_storage_night_bkrr = MOD_IMAGES + "bg/ext_storage_night.jpg"
    image bg ext_stage_big_day_bkrr = MOD_IMAGES + "bg/ext_stage_big_day.jpg"
    image bg ext_playground_sunset_bkrr = MOD_IMAGES + "bg/ext_playground_sunset.jpg"
    image bg ext_old_building_day_bkrr = im.Scale(MOD_IMAGES + "bg/ext_old_building_day.jpg", config.screen_width, config.screen_height)

    image bg int_music_club_day = bkrr_fast_composite(ES_IMAGES + "bg/int_musclub_day.jpg", MOD_IMAGES + "misc/int_music_club_clock_day.png") # переобъявлен для удобства

    image bg ext_music_club_day = ES_IMAGES + "bg/ext_musclub_day.jpg" # переобъявлен для удобства
    image bg ext_music_club_sunset_bkrr = MOD_IMAGES + "bg/ext_music_club_sunset.png"
    image bg ext_music_club_night_bkrr = im.Scale(MOD_IMAGES + "bg/ext_music_club_night.png", config.screen_width, config.screen_height)

    image bg ext_square_night_party_glow:
        contains:
            "bg ext_square_night_party"
        contains:
            (MOD_IMAGES + "misc/ext_square_night_party_glow_blue.png")
            alpha 0.5
            block:
                ease 1.25 alpha 0.25
                ease 1.25 alpha 0.5
                repeat
        contains:
            (MOD_IMAGES + "misc/ext_square_night_party_glow_magenta.png")
            alpha 0.5
            pause 0.5
            block:
                ease 1.25 alpha 0.25
                ease 1.25 alpha 0.5
                repeat

    image bg ext_house_of_sl_day_zhenya:
        contains:
            "bg ext_house_of_sl_day"
        contains:
            im.Scale(MOD_IMAGES + "misc/d17_zhenya_window.png", config.screen_width, config.screen_height)

    image bg ext_house_of_un_night_bkrr = MOD_IMAGES + "bg/ext_house_of_un_night.jpg"

    image bg ext_forest_day_rainy_bkrr = MOD_IMAGES + "bg/ext_forest_day_rainy.jpg"
    image bg ext_forest2_day_rainy_bkrr = MOD_IMAGES + "bg/ext_forest2_day_rainy.jpg"

    image bg ext_old_building_day_rainy = MOD_IMAGES + "bg/ext_old_building_day_rainy.jpg"
    image bg ext_old_building_day_rainy_with_mi = MOD_IMAGES + "bg/ext_old_building_day_rainy_with_mi.jpg"

    image bg ext_bathhouse_day_bkrr = MOD_IMAGES + "bg/ext_bathhouse_day.png"
    image bg ext_bathhouse_sunset_bkrr = im.MatrixColor(MOD_IMAGES + "bg/ext_bathhouse_day.png", bkrr_tint["sunset"] * im.matrix.contrast(1.25))
    image bg int_bathhouse_bkrr = MOD_IMAGES + "bg/int_bathhouse.jpg"

    image bg ext_beach_water_day:
        contains:
            (MOD_IMAGES + "bg/ext_beach_water_day.jpg")
        contains:
            (MOD_IMAGES + "misc/ext_beach_water_day_add.png")
            bkrr_water_atl

    image bg int_aidpost_sunset_bkrr = im.MatrixColor(ES_IMAGES + "bg/int_aidpost_day.jpg", bkrr_tint["sunset"] * im.matrix.contrast(1.25))
    image bg int_aidpost_night_lamplight_bkrr = MOD_IMAGES + "bg/int_aidpost_night_lamplight.png"

    image bg semen_room_clean_bkrr = MOD_IMAGES + "bg/semen_room_clean.jpg"

    image bg ext_infirmary_sunset:
        im.MatrixColor(im.Flip(ES_IMAGES + "bg/ext_path2_day.jpg", horizontal = True), bkrr_tint["sunset"] * im.matrix.contrast(1.25))
        align(0.82, 0.7)
        zoom 1.17

    image bg ext_no_bus_horse = bkrr_fast_composite(ES_IMAGES + "bg/ext_no_bus.jpg", MOD_IMAGES + "misc/ext_no_bus_horse.png")

    image bg ext_meadow_day = MOD_IMAGES + "bg/ext_meadow_day.jpg"

    image bg ext_camp_car = im.Scale(MOD_IMAGES + "bg/ext_camp_car.png", config.screen_width, config.screen_height)

    # Дождливые, пасмурные фоны

    image bg ext_music_club_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/ext_musclub_day.jpg")
    image bg ext_music_club_verandah_day_rainy_bkrr = bkrr_make_rainy_img(bkrr_fast_composite(MOD_IMAGES + "bg/ext_music_club_verandah_day.jpg", MOD_IMAGES + "misc/ext_music_club_verandah_day_posters.png", MOD_IMAGES + "misc/ext_music_club_verandah_text1.png", MOD_IMAGES + "misc/ext_music_club_verandah_text2.png", MOD_IMAGES + "misc/ext_music_club_verandah_text3.png")) # пасмурная версия с плакатами, 1-3 надписями, используется в 11 дне

    image bg ext_storage_day_rainy_bkrr = bkrr_make_rainy_img(MOD_IMAGES + "bg/ext_storage_day.png")
    image bg ext_square_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/ext_square_day.jpg")
    image bg ext_house_of_un_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/ext_house_of_un_day.jpg")
    image bg ext_dining_hall_near_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/ext_dining_hall_near_day.jpg")
    image bg ext_beach_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/ext_beach_day.jpg")
    image bg ext_boathouse_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/ext_boathouse_day.jpg")
    image bg ext_path_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/ext_path_day.jpg")
    image bg ext_path2_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/ext_path2_day.jpg")
    image bg ext_house_of_mt_night_without_light_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/ext_house_of_mt_night_without_light.jpg")

    image bg int_house_of_un_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/int_house_of_un_day.jpg")
    image bg int_dining_hall_people_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/int_dining_hall_people_day.jpg")
    image bg int_dining_hall_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/int_dining_hall_day.jpg")
    image bg int_clubs_male_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/int_clubs_male_day.jpg")
    image bg int_house_of_mt_day_rainy_bkrr = bkrr_make_rainy_img(ES_IMAGES + "bg/int_house_of_mt_day.jpg")
    image bg int_old_building_day_rainy_bkrr = MOD_IMAGES + "bg/int_old_building_day_rainy.jpg"

    ##    CG    ##

    # Позаимствованные CG

    image cg d5_potato_1 = MOD_IMAGES + "cg/d5_potato_1.jpg"
    image cg d5_potato_2 = MOD_IMAGES + "cg/d5_potato_2.jpg"
    image cg d7_mirror = MOD_IMAGES + "cg/d7_mirror.jpg"

    # Ориджинал и почти ориджинал CG

    image cg d5_cat_in_ventilation = im.Scale(MOD_IMAGES + "cg/d5_cat_in_ventilation.png", config.screen_width, config.screen_height)
    image cg d5_ghost = im.Scale(MOD_IMAGES + "cg/d5_ghost.png", config.screen_width, config.screen_height)
    image cg d6_sl_ass = MOD_IMAGES + "cg/d6_sl_ass.png"
    image cg d6_on_floor = MOD_IMAGES + "cg/d6_on_floor.png"
    image cg d6_sem_guitar = MOD_IMAGES + "cg/d6_sem_guitar.png"
    image cg d6_dv_guitar = MOD_IMAGES + "cg/d6_dv_guitar.png"
    image cg d7_mi_embrace = MOD_IMAGES + "cg/d7_mi_embrace.png"
    image cg d7_mi_dance = MOD_IMAGES + "cg/d7_mi_dance.png"
    image cg d7_mi_walking = MOD_IMAGES + "cg/d7_mi_walking.png"
    image cg d8_deer:
        (MOD_IMAGES + "cg/d8_deer.jpg")
        yanchor 0.0
        ypos -120
    image cg d8_chibi = MOD_IMAGES + "cg/d8_chibi.png"
    image cg d8_fstar:
        (MOD_IMAGES + "cg/d8_fstar.jpg")
        subpixel True
        topleft
        ease 5.0 xalign 1.0
    image cg d8_fstar_lone = bkrr_fast_composite(im.Crop(MOD_IMAGES + "cg/d8_fstar.jpg", 635, 0, 1920, 1080), MOD_IMAGES + "misc/d8_fstar_sem.png")
    image cg d8_fstar_mt = bkrr_fast_composite(im.Crop(MOD_IMAGES + "cg/d8_fstar.jpg", 635, 0, 1920, 1080), MOD_IMAGES + "misc/d8_fstar_sem.png", MOD_IMAGES + "misc/d8_fstar_mt.png")
    image cg d8_fstar_main = bkrr_fast_composite(im.Crop(MOD_IMAGES + "cg/d8_fstar.jpg", 635, 0, 1920, 1080), MOD_IMAGES + "misc/d8_fstar_star.png", MOD_IMAGES + "misc/d8_fstar_sem.png", MOD_IMAGES + "misc/d8_fstar_mt.png")
    image cg d9_walking:
        contains:
            "bg ext_houses_day"
            subpixel True
            truecenter
            zoom 1.5
            rotate -17
        contains:
            (MOD_IMAGES + "cg/d9_walking.png")
            subpixel True
            xalign 0.57
            yalign 1.0
            zoom 0.93
    image cg d9_wounded_dv = MOD_IMAGES + "cg/d9_wounded_dv.png"
    image cg d9_squirrel_1 = im.MatrixColor(MOD_IMAGES + "cg/d9_squirrel_1.png", bkrr_tint["sunset"])
    image cg d9_squirrel_2 = im.MatrixColor(MOD_IMAGES + "cg/d9_squirrel_2.png", bkrr_tint["sunset"])
    image cg d9_kiss = MOD_IMAGES + "cg/d9_kiss.png"
    image cg d10_ghost = MOD_IMAGES + "cg/d10_ghost.jpg"
    image cg d10_ghost_view = MOD_IMAGES + "cg/d10_ghost_view.jpg"
    image cg d11_shirt_1 = bkrr_make_rainy_img(MOD_IMAGES + "cg/d11_shirt.jpg")
    image cg d11_shirt_2:
        contains:
            bkrr_make_rainy_img(MOD_IMAGES + "cg/d11_shirt.jpg")
            yalign 1.0
        contains:
            bkrr_make_rainy_img(MOD_IMAGES + "misc/d11_shirt_shirt.png")
    image cg d11_forest = bkrr_make_rainy_img(MOD_IMAGES + "cg/d11_forest.jpg")
    image cg d11_forest_view = bkrr_make_rainy_img(MOD_IMAGES + "cg/d11_forest_view.jpg")
    image cg d11_forest_view_with_shadow = bkrr_make_rainy_img(bkrr_fast_composite(im.Crop(MOD_IMAGES + "cg/d11_forest_view.jpg", 1769, 0, 1920, 1080), im.Alpha(MOD_IMAGES + "misc/d11_forest_view_shadow.png", 0.8)))
    image cg d11_forest_view_with_pi = bkrr_make_rainy_img(bkrr_fast_composite(im.Crop(MOD_IMAGES + "cg/d11_forest_view.jpg", 1769, 0, 1920, 1080), MOD_IMAGES + "misc/d11_forest_view_pi.png"))
    image cg d11_mi_sleep_1 = bkrr_fast_livecomposite(MOD_IMAGES + "cg/d11_mi_sleep_1.png", bkrr_glow_atl(MOD_IMAGES + "misc/d11_mi_sleep_flash.png"))
    image cg d11_mi_sleep_2 = bkrr_fast_livecomposite(MOD_IMAGES + "cg/d11_mi_sleep_2.png", bkrr_glow_atl(MOD_IMAGES + "misc/d11_mi_sleep_flash.png"))
    image cg d11_mi_sleep_3 = LiveComposite((config.screen_width, config.screen_height), (0, 0), MOD_IMAGES + "cg/d11_mi_sleep_1.png", (1250, 375), im.Crop(MOD_IMAGES + "cg/d11_mi_sleep_2.png", 1250, 375, 100, 100), (0, 0), bkrr_glow_atl(MOD_IMAGES + "misc/d11_mi_sleep_flash.png"))
    image cg d11_night_guest = MOD_IMAGES + "cg/d11_night_guest.jpg"
    image cg d12_mi_hair_sl = MOD_IMAGES + "cg/d12_mi_hair_sl.png"
    image cg d12_mi_hair_sem = MOD_IMAGES + "cg/d12_mi_hair_sem.png"
    image cg d12_mi_hair_sem_bite = MOD_IMAGES + "cg/d12_mi_hair_sem_bite.png"
    image cg d12_mi_bath_1 = bkrr_fast_composite(MOD_IMAGES + "cg/d12_mi_bath_1.png", MOD_IMAGES + "misc/d12_mi_bath_steam.png")
    image cg d12_mi_bath_2 = bkrr_fast_composite(MOD_IMAGES + "cg/d12_mi_bath_2.png", MOD_IMAGES + "misc/d12_mi_bath_steam.png")
    image cg d12_noon_rest_1 = MOD_IMAGES + "cg/d12_noon_rest_1.jpg"
    image cg d12_noon_rest_2 = MOD_IMAGES + "cg/d12_noon_rest_2.jpg"
    image cg d12_noon_rest_3 = MOD_IMAGES + "cg/d12_noon_rest_3.jpg"
    image cg d12_noon_rest_4 = MOD_IMAGES + "cg/d12_noon_rest_4.jpg"
    image cg d12_noon_rest_5 = MOD_IMAGES + "cg/d12_noon_rest_5.jpg"
    image cg d12_us_kiss_1:
        contains:
            (MOD_IMAGES + "misc/d12_us_kiss_bg.png")
        contains:
            (MOD_IMAGES + "cg/d12_us_kiss_1.png")
            center
            zoom 1.0
            ease 1.5 zoom 1.3
            linear 0.5 alpha 0.0
    image cg d12_us_kiss_2 = MOD_IMAGES + "cg/d12_us_kiss_2.png"
    image cg d12_us_kiss_3 = MOD_IMAGES + "cg/d12_us_kiss_3.png"
    image cg d12_us_kiss_4 = MOD_IMAGES + "cg/d12_us_kiss_4.png"
    image cg d12_us_kiss_5 = MOD_IMAGES + "cg/d12_us_kiss_5.png"
    image cg d12_us_kiss_6:
        contains:
            (MOD_IMAGES + "cg/d12_us_kiss_6.png")
        contains:
            (MOD_IMAGES + "misc/d12_us_kiss_blush.png")
            alpha 0.0
            ease 3.5 alpha 1.0
    image cg d12_fireflies:
        contains:
            (MOD_IMAGES + "cg/d8_fstar.jpg")
            align(0.5, 1.0)
            zoom 1.15
    image cg d13_beach = MOD_IMAGES + "cg/d13_beach.png"
    image cg d14_un_sleep = MOD_IMAGES + "cg/d14_un_sleep.png"
    image cg d14_us_fall = MOD_IMAGES + "cg/d14_us_fall.jpg"
    image cg d14_un_cry = MOD_IMAGES + "cg/d14_un_cry.png"
    image cg d14_dv_spy = MOD_IMAGES + "cg/d14_dv_spy.png"
    image cg d14_dv_window_1 = MOD_IMAGES + "cg/d14_dv_window_1.jpg"
    image cg d14_dv_window_2 = MOD_IMAGES + "cg/d14_dv_window_2.jpg"
    image cg d14_mi_confession_1 = MOD_IMAGES + "cg/d14_mi_confession_1.png"
    image cg d14_mi_confession_2 = MOD_IMAGES + "cg/d14_mi_confession_2.png"
    image cg d14_mi_confession_3 = MOD_IMAGES + "cg/d14_mi_confession_3.png"
    image cg d14_mi_confession_4 = MOD_IMAGES + "cg/d14_mi_confession_4.png"
    image cg d14_rocket_1 = MOD_IMAGES + "cg/d14_rocket_1.png"
    image cg d14_rocket_2:
        contains:
            (MOD_IMAGES + "cg/d14_rocket_1.png")
        contains:
            (MOD_IMAGES + "cg/d14_rocket_2.png")
            ease 15.0 alpha 0.0
    image cg d15_mi_sleep = im.Scale(MOD_IMAGES + "cg/d15_mi_sleep.jpg", config.screen_width, config.screen_height)
    image cg d16_boat_shed = MOD_IMAGES + "cg/d16_boat_shed.jpg"
    image cg d16_cryptography = MOD_IMAGES + "cg/d16_cryptography.png"
    image cg d16_gulls = MOD_IMAGES + "cg/d16_gulls.jpg"
    image cg d17_alisa_klaus = MOD_IMAGES + "cg/d17_alisa_klaus.jpg"
    image cg d17_klaus_guitar = im.Scale(MOD_IMAGES + "cg/d17_klaus_guitar.jpg", config.screen_width, config.screen_height)
    image cg d17_tmp_sex:
        contains:
            im.Scale(MOD_IMAGES + "cg/d15_mi_sleep.jpg", config.screen_width, config.screen_height)
        contains:
            Solid("#000")
            alpha 0.90
    image cg d18_bed_1 = im.Scale(MOD_IMAGES + "cg/d18_bed.png", config.screen_width, config.screen_height)
    image cg d18_bed_2:
        contains:
            im.Scale(MOD_IMAGES + "cg/d18_bed.png", config.screen_width, config.screen_height)
        contains:
            im.Scale(MOD_IMAGES + "cg/d18_bed_mi_open.png", config.screen_width, config.screen_height)
    image cg d18_klaus_play = MOD_IMAGES + "cg/d18_klaus_play.png"

    # Комбинированные сюжетные вставки, анимированные и статичные (тоже идут под тегом cg)

    image cg d6_guitar_hit:
        contains:
            "bg ext_clubs_day"
        contains:
            (MOD_IMAGES + "bg/ext_clubs_day_blur.jpg")
            alpha 0.0
            linear 3.5 alpha 1.0
        contains:
            (MOD_IMAGES + "misc/d6_dv_hit.png")
            pos(0.75, 0.5)
            anchor(0.5, 0.5)
            linear 3.4 pos(0.5, 0.5)
            linear 0.1 zoom 1.33
        contains:
            im.Scale(MOD_IMAGES + "misc/d6_dv_hit_text.png", 585, 155)
            pos(0.5, 0.9)
            anchor(0.5, 0.5)
            alpha 0.0
            pause 1.2
            ease 2.0 pos(0.5, 0.75) alpha 1.25 zoom 2
            ease 0.3 zoom 2.0
        contains:
            "white"
            alpha 0.0
            pause 3.45
            linear 0.05 alpha 1.0

    image cg d8_theft:
        contains:
            "bg int_dining_hall_people_day"
        contains:
            (MOD_IMAGES + "misc/d8_theft_sh.png")
            topleft
            alpha 0.0
            pause 2.0
            parallel:
                linear 0.25 alpha 1.0
                pause 4.0
                linear 0.5 alpha 0.0
            parallel:
                ease 2.5 xpos 0.12
        contains:
            (MOD_IMAGES + "misc/d8_theft_us.png")
            topleft
            alpha 0.0
            parallel:
                linear 0.25 alpha 1.0
                pause 2.0
                linear 0.25 alpha 0.0
            parallel:
                ease 2.0 xpos 1.0

    image cg d12_mi_bath_scene:
        contains:
            "bg int_bathhouse_bkrr"
        contains:
            "mi normal body_loo close"
            center
        contains:
            im.Composite((1050, 1080), (0, 0), MOD_IMAGES + "sprites/close/mi/mi_3_shorts.png") # н-да
            center
            subpixel True
            ease 3.0 xpos 0.506 ypos 0.017

    image cg d12_fight:
        contains:
            bkrr_make_tint_img(MOD_IMAGES + "bg/int_music_club_mattresses_sunset.jpg", "red")
            bkrr_shiver_atl
        contains:
            bkrr_make_tint_img(MOD_IMAGES + "misc/int_music_club_clock_sunset.png", "red")
            bkrr_shiver_atl
        contains:
            "dv rage pioneer2"
            fright
            ypos -0.5
            zoom 2.5
            alpha 0.22
        contains:
            "us evsmile pioneer"
            fleft
            ypos -0.8
            zoom 2.5
            alpha 0.22
        contains:
            "us evsmile pioneer"
            fleft
            ease 5.0 xpos 0.25
        contains:
            "dv rage pioneer2"
            fright
            ease 5.0 xpos 0.75
        contains:
            (MOD_IMAGES + "misc/d12_fight_breach.png")

    image cg d14_mi_surprise:
        truecenter
        contains:
            "bg int_infirmary_night_guitar_v3"
        contains:
            "mi smile yukata close"
            center

    # Прочие эффекты

    image d17_knife_slice = MOD_IMAGES + "misc/d17_knife_slice.png"
    image d17_knife_slice2 = MOD_IMAGES + "misc/d17_knife_slice2.png"

    ##    Звуки    ##

    $ bkrr_sfx_list = bkrr_form_files_list("mods/bkrr/sound/sfx/")
    $ bkrr_ambience_list = bkrr_form_files_list("mods/bkrr/sound/ambience/")
    $ bkrr_music_list = bkrr_form_files_list("mods/bkrr/sound/music/")

    ##    Видео    ##

    $ bkrr_video_list = {
        "intro":"mods/bkrr/video/intro.webm",
        "credits":"mods/bkrr/video/credits.webm"
    }

    $ bkrr_video_list["backdrop"] = {dn:("mods/bkrr/video/backdrop_day" + str(dn) + ".webm") for dn in range(4, 20)}
    $ bkrr_video_list["backdrop"]["epilogue"] = "mods/bkrr/video/backdrop_epilogue.webm"

init 1:

    ##    ATL, transform-ы и различные эффекты    ##

    # Размещение спрайтов на экране (стоя)
    # Переназначение позиций для ES 1.2

    if config.version == "1.2":
        transform fleft:
            xalign 0.16
            xanchor 0.5
            yalign 0.0

        transform left:
            xalign 0.28
            xanchor 0.5
            yalign 0.0

        transform cleft:
            xalign 0.355
            xanchor 0.5
            yalign 0.0

        transform center:
            xalign 0.5
            yalign 0.0

        transform cright:
            xalign 0.645
            xanchor 0.5
            yalign 0.0

        transform right:
            xalign 0.72
            xanchor 0.5
            yalign 0.0

        transform fright:
            xalign 0.84
            xanchor 0.5
            yalign 0.0

    # Размещение спрайтов на экране (сидя)

    transform bkrr_sit_left:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0
        ypos 0.22

    transform bkrr_sit_center:
        xalign 0.5
        yanchor 0.0
        ypos 0.22

    transform bkrr_sit_right:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0
        ypos 0.22

    # Для персонажей невысокого роста и для дистанции close

    transform bkrr_sit_left1:
        xalign 0.28
        xanchor 0.5
        yanchor 0.0
        ypos 0.15

    transform bkrr_sit_center1:
        xalign 0.5
        yanchor 0.0
        ypos 0.15

    transform bkrr_sit_right1:
        xalign 0.72
        xanchor 0.5
        yanchor 0.0
        ypos 0.15

    ## Текст

    # Стиль текста для песен и сами тексты

    $ style.bkrr_song_style = Style(style.default)
    $ style.bkrr_song_style.color = "#FFF"
    $ style.bkrr_song_style.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.bkrr_song_style.drop_shadow_color = "#000"
    $ style.bkrr_song_style.text_align = 0.5
    $ renpy.image("bkrr_song", ParameterizedText(style="bkrr_song_style", size=48))

    # Стиль текста для оформления мыслей главного героя, соответствующая функция и ATL

    $ style.bkrr_thought = Style(style.default)
    $ style.bkrr_thought.drop_shadow = (2, 2)
    $ style.bkrr_thought.drop_shadow_color = "#000"
    $ style.bkrr_thought.text_align = 0.5
    $ renpy.image("bkrr_thought", ParameterizedText(style="bkrr_thought", size=40))

    # Стиль текста для для TODO

    $ style.bkrr_todo_style = Style(style.default)
    $ style.bkrr_todo_style.color = "#F00"
    $ style.bkrr_todo_style.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.bkrr_todo_style.drop_shadow_color = "#800"
    $ style.bkrr_todo_style.text_align = 0.5
    $ style.bkrr_todo_style.align = (0.5, 0.5)
    $ renpy.image("bkrr_todo", ParameterizedText(style="bkrr_todo_style", size=48))

    python:

        def bkrr_thoughts_show(*args):
            colors = {
                "day":"#E2C778",
                "sunset":"#DCD168",
                "night":"#3CCFA2",
                "prologue":"#98D8DA"
            }
            pt = 0.1
            t = 4.0
            sy = ey = 1.0 / len(args)
            for i, text in enumerate(args):
                if not i % 2:
                    sx = -0.1
                    ex = random.uniform(0.3, 0.4)
                    rot = -27.5
                else:
                    sx = 1.1
                    ex = random.uniform(0.7, 0.6)
                    rot = 27.5
                sy += 0.1
                ey += 0.1
                renpy.show("thought_text", [bkrr_thoughts_atl(t, pt, sx, sy, ex, ey, rot)], tag="thought_text" + str(i), what=Text(text, style=style.bkrr_thought, color=colors[persistent.timeofday], size=40))
                pt += 0.22
            renpy.pause()
            for i in range(len(args)):
                renpy.hide("thought_text" + str(i))
                renpy.with_statement(Dissolve(0.15))

    transform bkrr_thoughts_atl(t, pt, sx, sy, ex, ey, rot):
        pos(sx, sy)
        anchor(0.5, 0.5)
        rotate rot
        alpha 0.0
        pause pt
        ease t pos(ex, ey) rotate renpy.random.randint(-4, 4) alpha 1.0

    # Стиль текста для "служебных" сообщений

    $ style.bkrr_service = Style(style.default)
    $ style.bkrr_service.font = "mods/bkrr/fonts/Balloon_XBd.ttf"
    $ style.bkrr_service.color = "#FFF"
    $ style.bkrr_service.drop_shadow = (2, 2)
    $ style.bkrr_service.drop_shadow_color = "#222"
    $ style.bkrr_service.text_align = 0.5
    $ style.bkrr_service.yalign = 0.5
    $ style.bkrr_service.kerning = 17.0
    $ renpy.image("bkrr_service", ParameterizedText(style="bkrr_service", size=64))

    $ bkrr_title_message = bkrr_title[0].replace(u" и ", u"\nи\n")
    $ bkrr_ending_message = u"Продолжение следует…"

    $ style.bkrr_service2 = Style(style.bkrr_service)
    $ style.bkrr_service2.font = "mods/bkrr/fonts/capitalist.ttf"
    $ style.bkrr_service2.color = "#FCF3EC"
    $ style.bkrr_service2.drop_shadow = [(1, 1), (1, 1), (1, 1), (1, 1)]
    $ style.bkrr_service2.drop_shadow_color = "#47240A"
    $ renpy.image("bkrr_service2", ParameterizedText(style="bkrr_service2", size=64))

    ## Специальные изображения

    image bkrr_lyrics_screen:
        Frame(ES_IMAGES + "gui/choice/" + persistent.timeofday + "/choice_box.png", 50, 50)
        truecenter
        size(1240, 1240)

    image bkrr_flying_notes = bkrr_create_anim(MOD_IMAGES + "misc/d5_flying_notes_", 3, 1.5, Dissolve(0.25, alpha=True))

    image bkrr_bang = MOD_IMAGES + "misc/bang.png"

    ## Эффекты

    # Анимации "встань" и "сядь" для спрайтов

    transform sit_down:
        parallel:
            ease 1.0 ypos 0.22
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    transform sit_down1:
        parallel:
            ease 1.0 ypos 0.15
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    transform get_up:
        parallel:
            ease 1.0 ypos 0.0
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    # Анимация стула, когда персонаж встаёт или садится

    transform chair_move_sd:
        yanchor 0.0
        ypos 0.1
        zoom 0.95
        ease 0.75 ypos 0.0 zoom 1.0

    transform chair_move_gu:
        yanchor 0.0
        ease 0.75 ypos 0.1 zoom 0.95

    # Анимация движения вперёд

    transform bkrr_moving_forward_near(t, z=1.5):
        subpixel True
        truecenter
        linear t zoom z ypos 0.25

    transform bkrr_moving_forward_far(t, z=1.5):
        subpixel True
        truecenter
        linear t zoom z ypos 0.40

    # Анимация бега

    transform bkrr_running_atl:
        truecenter
        zoom 1.25
        parallel:
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.25 rotate -0.75
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.35 rotate -0.75
            repeat
        parallel:
            ease 0.25 xpos 0.495
            ease 0.20 xpos 0.505
            repeat
        parallel:
            ease 0.25 ypos 0.495
            ease 0.30 ypos 0.505
            repeat

    # Анимация воды

    transform bkrr_water_atl:
        truecenter
        subpixel True
        alpha 0.8
        ease 0.5 zoom 1.2
        parallel:
            choice:
                ease 1.5 zoom 1.19
                ease 1.5 zoom 1.21
            choice 2:
                ease 2.0 zoom 1.195
                ease 2.0 zoom 1.205
            repeat
        parallel:
            choice:
                ease 15.0 xpos 0.51
            choice:
                ease 15.0 xpos 0.49
            choice:
                ease 20.0 xpos 0.51
            choice:
                ease 20.0 xpos 0.49
            repeat
        parallel:
            choice:
                ease 1.5 rotate 0.0
            choice:
                ease 1.5 rotate 0.5
                ease 1.5 rotate -0.5
            choice:
                ease 2.5 rotate 0.5
                ease 2.5 rotate -0.5
            choice:
                ease 2.5 rotate 0.75
                ease 2.5 rotate -0.75
            repeat

    # Эффект встряски

    transform bkrr_shake_atl:
        truecenter
        zoom 1.2
        parallel:
            linear 0.15 rotate -1
            linear 0.15 rotate 0.5
            linear 0.15 rotate -0.5
            linear 0.15 rotate 0
        parallel:
            ease 0.25 zoom 1.0

    transform bkrr_shiver_atl:
        truecenter
        ease 0.25 zoom 1.1
        parallel:
            ease 0.25 zoom 1.11 rotate 0.75
            ease 0.25 zoom 1.1 rotate -0.75
            repeat
        parallel:
            ease 0.10 xpos 0.495
            ease 0.10 xpos 0.505
            repeat
        parallel:
            ease 0.15 ypos 0.495
            ease 0.15 ypos 0.505
            repeat

    transform bkrr_shiver_lite:
        truecenter
        ease 0.25 zoom 1.005
        parallel:
            ease 0.35 zoom 1.006 rotate 0.01
            ease 0.35 zoom 1.005 rotate -0.01
            repeat
        parallel:
            ease 0.15 xpos 0.499
            ease 0.15 xpos 0.501
            repeat
        parallel:
            ease 0.25 ypos 0.499
            ease 0.25 ypos 0.501
            repeat

    # Отсвет от пламени (да, быдлокод)

    transform bkrr_glow_atl(imgf):
        im.MatrixColor(imgf, im.matrix.brightness(0.17))
        choice 2:
            ease 0.4 alpha 0.5
        choice 2:
            ease 0.3 alpha 0.75
        choice 2:
            ease 0.3 alpha 0.6
        choice:
            ease 0.25 alpha 0.9
        choice:
            ease 0.2 alpha 1.0
        repeat

    # Эффект двоения в глазах

    transform bkrr_appdouble_atl(imgn, z=1.1, zt=1.0, t=1.0):
        contains:
            ImageReference(imgn)
            truecenter
            linear zt zoom z
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t xpos 0.48 alpha 0.3 zoom (z + 0.05)
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t xpos 0.51 alpha 0.2 zoom (z + 0.05)

    # Горящая спичка

    image bkrr_match_glow = bkrr_glow_atl(MOD_IMAGES + "effects/match_glow.png")

    # Эффект ледяной воды

    image coldwater_shock = MOD_IMAGES + "misc/d5_coldwater_shock.png"

    # Эффект для моментов пробуждения

    transform bkrr_awakening_atl(imgn):
        contains:
            ImageReference(imgn)
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.5))
            truecenter
            alpha 0.9
            zoom 1.05
            ease 5.0 alpha 0.0 zoom 1.0
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.5))
            truecenter
            alpha 0.9
            zoom 1.075
            ease 5.0 alpha 0.0 zoom 1.0

    transform bkrr_awakening_dark(imgn):
        contains:
            ImageReference(imgn)
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.1))
            truecenter
            alpha 0.9
            zoom 1.05
            ease 5.0 alpha 0.0 zoom 1.0
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.1))
            truecenter
            alpha 0.9
            zoom 1.075
            ease 5.0 alpha 0.0 zoom 1.0

    # Анимации получения ачивментов и предметов

    transform bkrr_get_achievement_atl:
        pos(0.85, 0.85)
        anchor(0.5, 0.5)
        zoom 0.0
        ease 1.5 zoom 1.05
        ease 0.25 zoom 0.95
        ease 0.25 zoom 1.0
        pause 4.0
        ease 0.5 pos(0.8, 0.85)
        ease 0.5 pos(1.0, 0.85) alpha 0.0

    transform bkrr_get_item_atl:
        pos(-0.1, 0.75)
        anchor(0.0, 0.5)
        alpha 0.0
        ease 1.0 pos(0.0, 0.75) alpha 1.0
        pause 3.0
        ease 1.0 pos(-0.1, 0.75) alpha 0.0

    # Специальные эффекты и анимации (для конкретных ивентов и т. п.)

    transform d4_mttalk_cgs_atl(rot):
        truecenter
        zoom 1.25
        rotate rot
        ease 0.75 zoom 1.0 rotate 0.0

    transform d5_stars_atl:
        subpixel True
        truecenter
        ease 5.0 zoom 1.25 rotate 7.5

    transform d6_sl_ass_atl:
        subpixel True
        truecenter
        zoom 1.25
        linear 10.0 zoom 1.0

    transform d6_on_floor_atl:
        subpixel True
        truecenter
        zoom 1.25
        rotate -7.5
        ease 7.5 zoom 1.0 rotate 0.0

    transform d6_dv_guitar_atl:
        subpixel True
        pos(0.38, 0.65)
        anchor(0.5, 0.5)
        zoom 2.0
        linear 15.0 pos(0.5, 0.5) zoom 1.0

    transform d7_mi_embrace_atl:
        subpixel True
        truecenter
        zoom 1.5
        ease 17.0 zoom 1.0

    transform d7_mi_dance_atl:
        subpixel True
        pos(0.42, 0.7)
        anchor(0.5, 0.5)
        zoom 1.5
        ease 16.0 zoom 1.0 pos(0.5, 0.5)

    image bkrr_d9_cinema:
        xalign 0.517
        yalign 0.436
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame1.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame2.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame3.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame4.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame5.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame6.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame7.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame8.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame9.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame10.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame11.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame12.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame13.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame14.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame15.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        im.Scale(MOD_IMAGES + "misc/d9_cinema/frame16.jpg", 366, 222) with Dissolve(3.5)
        pause 3.5
        repeat

    transform d9_kiss_atl:
        subpixel True
        truecenter
        zoom 1.25
        rotate 7.5
        ease 5.0 zoom 1.0 rotate 0.0

    transform d10_ghost_view_atl:
        subpixel True
        ypos -2320
        ease 15.0 ypos -410

    ## Осадки: партиклы, ATL и т. д.

    # Небольшая шпаргалка на будущее:
    # SnowBlossom(img, count=int, border=int, xspeed=tuple, yspeed=tuple, start=int, fast=bool, horizontal=bool)

    image bkrr_raindrop_particle_large = MOD_IMAGES + "effects/particles/raindrop_large.png"
    image bkrr_raindrop_particle_normal = MOD_IMAGES + "effects/particles/raindrop_normal.png"
    image bkrr_raindrop_particle_small = MOD_IMAGES + "effects/particles/raindrop_small.png"

    image bkrr_eff_light_rain:
        truecenter
        xzoom 1.3 yzoom 2.2
        contains:
            SnowBlossom("bkrr_raindrop_particle_normal", 10, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("bkrr_raindrop_particle_small", 25, 50, (25, 50), (1400, 1500))

    image bkrr_eff_light_rain_l:
        "bkrr_eff_light_rain"
        rotate 16.0

    image bkrr_eff_light_rain_l:
        "bkrr_eff_light_rain"
        rotate -16.0

    image bkrr_eff_rain:
        truecenter
        xzoom 1.3
        yzoom 2.11
        contains:
            SnowBlossom("bkrr_raindrop_particle_large", 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom("bkrr_raindrop_particle_normal", 25, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("bkrr_raindrop_particle_small", 150, 50, (25, 50), (1400, 1500))

    image bkrr_eff_rain_l:
        "bkrr_eff_rain"
        truecenter
        rotate 16.0

    image bkrr_eff_rain_r:
        "bkrr_eff_rain"
        truecenter
        rotate -16.0

    image bkrr_eff_hard_rain:
        contains:
            "bkrr_eff_rain"
        contains:
            "bkrr_eff_rain"

    image bkrr_eff_hard_rain_l:
        contains:
            "bkrr_eff_rain_l"
            truecenter
        contains:
            "bkrr_eff_rain_l"
            truecenter

    image bkrr_eff_hard_rain_r:
        contains:
            "bkrr_eff_rain_r"
            truecenter
        contains:
            "bkrr_eff_rain_r"
            truecenter

    image bkrr_eff_snow:
        contains:
            SnowBlossom(im.Alpha(im.FactorScale(ES_IMAGES + "anim/snow.png", 0.75), 0.75), 50, 50, (15, 30), (25, 125))
        contains:
            SnowBlossom(im.Alpha(im.FactorScale(ES_IMAGES + "anim/snow.png", 0.5), 0.50), 75, 50, (15, 30), (25, 100))
        contains:
            SnowBlossom(im.Alpha(im.FactorScale(ES_IMAGES + "anim/snow.png", 0.25), 0.25), 100, 50, (15, 30), (25, 75))
        contains:
            SnowBlossom(im.Alpha(im.FactorScale(ES_IMAGES + "anim/snow.png", 0.25), 0.15), 200, 50, (15, 30), (25, 50))
        contains:
            SnowBlossom(im.Alpha(im.FactorScale(ES_IMAGES + "anim/snow.png", 0.2), 0.1), 200, 50, (15, 30), (25, 50))

    image bkrr_eff_skylight:
        contains:
            SnowBlossom(MOD_IMAGES + "effects/particles/skylight1.png", 5, 50, (15, 30), (-50, -300))
        contains:
            SnowBlossom(MOD_IMAGES + "effects/particles/skylight2.png", 10, 50, (15, 30), (-50, -300))
        contains:
            SnowBlossom(MOD_IMAGES + "effects/particles/skylight3.png", 15, 50, (15, 30), (-50, -300))
        contains:
            SnowBlossom(MOD_IMAGES + "effects/particles/skylight4.png", 20, 50, (15, 30), (-50, -300))

    image bkrr_eff_fireflies:
        contains:
            SnowBlossom(bkrr_make_tint_img(im.FactorScale(MOD_IMAGES + "effects/particles/firefly.png", 0.9), "green_yellow"), 5, 40, (-50, 50), (-40, -200))
        contains:
            SnowBlossom(bkrr_make_tint_img(im.FactorScale(MOD_IMAGES + "effects/particles/firefly.png", 0.8), "green_yellow"), 10, 40, (-50, 50), (-40, -200))
        contains:
            SnowBlossom(bkrr_make_tint_img(im.FactorScale(MOD_IMAGES + "effects/particles/firefly.png", 0.7), "green_yellow"), 15, 40, (-50, 50), (-40, -200))
        contains:
            SnowBlossom(bkrr_make_tint_img(im.FactorScale(MOD_IMAGES + "effects/particles/firefly.png", 0.6), "green_yellow"), 20, 40, (-50, 50), (-40, -200))

    image bkrr_eff_yoba = SnowBlossom(MOD_IMAGES + "effects/particles/yoba.png", 25, 50, (15, 30), (-50, -300))

    ## Переходы

    python:

        bkrr_circlein_transition = ImageDissolve(MOD_IMAGES + "transitions/circle.png", 0.5, ramplen=5, reverse = True, alpha=True)
        bkrr_circleout_transition = ImageDissolve(MOD_IMAGES + "transitions/circle.png", 0.5, ramplen=5, reverse = False, alpha=True)

        bkrr_blindstoleft_transition = ImageDissolve(MOD_IMAGES + "transitions/blinds_h.png", 1.0, ramplen=25, reverse = False, alpha=True)
        bkrr_blindstoright_transition = ImageDissolve(MOD_IMAGES + "transitions/blinds_h.png", 1.0, ramplen=25, reverse = True, alpha=True)
        bkrr_blindstotop_transition = ImageDissolve(MOD_IMAGES + "transitions/blinds_v.png", 1.0, ramplen=25, reverse = False, alpha=True)
        bkrr_blindstobottom_transition = ImageDissolve(MOD_IMAGES + "transitions/blinds_v.png", 1.0, ramplen=25, reverse = True, alpha=True)

        def bkrr_timeskip_transition(t=1.0):
            return ImageDissolve(MOD_IMAGES + "transitions/timeskip.png", t, ramplen=0, reverse=False, alpha=True)

        def bkrr_fade(time=1.0, color="white"):
            ft = time * 0.5
            fc = {
                "black":"#000",
                "white":"#FFF",
                "red":"#F00"
            }
            return Fade(ft, 0.0, ft, color = fc[color])

        def bkrr_hurt_transition(t=0.5):
            return bkrr_fade(time=t, color="red")

init 2:

    python:

        ##    Спрайты    ##

        # Эмоции спрайтов старых персонажей и их отношение к позе

        emotion_to_pose = {
            'dv': {
                'cry': 1, 'scared': 1, 'shocked': 1, 'surprise': 1, 'grin': 2, 'guilty': 3, 'shy': 3, 'sad': 3, 'laugh': 4, 'normal': 4, 'smile': 4, 'angry': 5, 'rage': 5,
            },
            'mz': {
                'bukal': 1, 'normal': 1, 'laugh': 1, 'angry': 2, 'rage': 2, 'shy': 3, 'smile': 3,
            },
            'mt': {
                'normal': 1, 'sad': 1, 'smile': 1, 'surprise': 1, 'angry': 2, 'rage': 2, 'grin': 3, 'laugh': 3,
            },
            'sh': {
                'laugh': 1, 'scared': 1, 'smile': 1, 'upset': 1, 'cry': 2, 'normal_smile': 2, 'rage': 2, 'normal': 3, 'serious': 3, 'surprise': 3,
            },
            'un': {
                'angry': 1, 'evil_smile': 1, 'normal': 1, 'shy': 1, 'shy_smile': 1, 'smile': 1, 'smile2': 1, 'cry': 2, 'cry_smile': 2, 'sad': 2, 'scared': 2, 'shocked': 2, 'surprise': 2, 'angry2': 3, 'grin': 3, 'laugh': 3, 'rage': 3, 'serious': 3, 'smile3': 3,
            },
            'us': {
                'grin': 1, 'laugh': 1, 'laugh2': 1, 'normal': 1, 'normal_dontlike': 1, 'sad': 1, 'smile': 1, 'angry': 2, 'calml': 2, 'dontlike': 2, 'fear': 2, 'upset': 2, 'cry': 3, 'cry2': 3, 'shy': 3, 'shy2': 3, 'surp1': 3, 'surp2': 3, 'surp3': 3,
            },
            'cs': {
                'normal': 1, 'shy': 1, 'smile': 1, 'sad': 1,
            },
            'mi': {
                'cry': 1, 'dontlike': 1, 'laugh': 1, 'shocked': 1, 'scared': 1, 'shy': 1, 'surprise': 1, 'cry_smile': 2, 'grin': 2, 'happy': 2, 'sad': 2, 'sad_smile': 2, 'smile': 2, 'angry': 3, 'normal': 3, 'rage': 3, 'serious': 3, 'upset': 3,
            },
            "ant": {
                'normal': 1, 'serious': 1, 'smile': 1, 'surprise': 1,
            },
            "kla": {
                'laugh': 1, 'normal': 1, 'smile': 1, 'shy': 2, 'surprise': 2,
            },
            "nt": {
                'laugh': 1, 'normal': 1, 'sad': 1, 'smile': 1,
            },
            "tol": {
                'normal': 1, 'pain': 1, 'sad': 1, 'shy': 1, 'smile': 1,
            },
            "tr": {
                'normal': 1, 'smile1': 1, 'surp' : 1, 'upset2': 1, 'smile2': 2, 'smile3': 2, 'upset1': 2,
            },
        }

        distance_to_position = {
            "far": (675, 1080),
            "normal": (900, 1080),
            "close": (1125, 1080)
        }

        def _sprite_for_all_times(full_sprite_name, composite_image):
            """
            Объявляем спрайт для всех времен суток
            """
            renpy.image(
                full_sprite_name,
                ConditionSwitch(
                    "persistent.sprite_time == 'sunset'", im.MatrixColor(composite_image, bkrr_tint["sunset"]),
                    "persistent.sprite_time == 'night'", im.MatrixColor(composite_image, bkrr_tint["night"]),
                    True, composite_image,
                )
            )

        def _sepia_sprite(full_sprite_name, composite_image):
            """
            Спрайт, окрашенный в сепию
            """
            renpy.image(full_sprite_name, im.Sepia(composite_image))

        # Генератор новых спрайтов для персонажей из оригинального БЛ

        def make_sprites_for(character, sprite_name, layers, emotions=None, distances=None, exclude=None, sprite_define_func=None):
            """
            Позволяет объявить почти любой спрайт, состоящий из нескольких слоев,
            каждый слой может идти либо из мода, либо из оригинала.
            Картинки должны класться в папки строго как в оригинале, чтобы это работало.
            """

            if emotions is None:
                emotions = emotion_to_pose[character].keys()
            if distances is None:
                distances = distance_to_position.keys()
            if sprite_define_func is None:
                sprite_define_func = _sprite_for_all_times

            for emotion in emotions:
                if exclude and emotion in exclude:
                    continue

                pose = emotion_to_pose[character][emotion]

                for distance in distances:
                    # Получаем название спрайта, например dv angry bkrr_sport far
                    full_sprite_name = '%s %s %s' % (character, emotion, sprite_name)
                    if distance != 'normal':
                        full_sprite_name += ' ' + distance

                    # Комбинируем изображение
                    image_parts = [distance_to_position[distance]]
                    for layer in layers:
                        source, file_name = layer.split(':')
                        base_path = MOD_IMAGES if source == 'mod' else ES_IMAGES
                        image_path = base_path + "sprites/%s/%s/%s_%s_%s.png" % (
                            distance, character, character, pose, file_name if file_name != '<emotion>' else emotion,
                        )
                        image_parts += [(0, 0), image_path]
                    composite_image = im.Composite(*image_parts)

                    # Объявляем спрайт
                    sprite_define_func(full_sprite_name, composite_image)


        def make_sprites_with_custom_emotions(custom_emotions, *args):
            """
            Удобно, когда нужно объявить новую эмоцию
            """
            args = list(args)
            assert args[-1][-1] == 'es:<emotion>'
            make_sprites_for(*args, exclude=custom_emotions)
            args[-1][-1] = 'mod:<emotion>'
            make_sprites_for(*args, emotions=custom_emotions)


        # Объявляем спрайты

        make_sprites_for('dv', 'bkrr_sport', ['es:body', 'mod:sport', 'es:<emotion>'])
        make_sprites_for('dv', 'swim', ['es:body', 'mod:swim', 'es:<emotion>'], emotions=('angry', 'guilty', 'rage', 'sad', 'shy'))

        make_sprites_for('mz', 'bkrr_sport', ['es:body', 'mod:sport', 'es:<emotion>'])
        make_sprites_for('mz', 'mask bkrr_sport', ['es:body', 'mod:sport', 'es:<emotion>', 'mod:mask'])
        make_sprites_for('mz', 'zombie', ['mod:zomb'], emotions=['normal'], distances=['far'])
        make_sprites_for('mz', 'glasses bkrr_sport', ['es:body', 'mod:sport', 'es:<emotion>', 'es:glasses'])
        make_sprites_for('mz', 'glasses bkrr_dress', ['es:body', 'mod:dress', 'es:<emotion>', 'es:glasses'])

        make_sprites_for('mt', 'bkrr_sport', ['es:body', 'mod:sport', 'es:<emotion>'])
        make_sprites_for('mt', 'nightdress', ['es:body', 'mod:nightdress', 'es:<emotion>'])
        make_sprites_for('mt', 'torn', ['es:body', 'mod:torn', 'es:<emotion>'], distances=['normal'])

        make_sprites_for('sh', 'bathrobe', ['mod:bathrobe', 'es:<emotion>'])
        make_sprites_for('sh', 'shirt', ['mod:shirt', 'es:<emotion>'])

        make_sprites_with_custom_emotions(['shy_smile'], 'un', 'bkrr_dress', ['es:body', 'mod:dress', 'es:<emotion>'])
        make_sprites_for('un', 'bra', ['es:body', 'mod:bra', 'es:<emotion>'], emotions=['cry', 'cry_smile', 'sad', 'scared', 'shocked', 'surprise'])
        make_sprites_for('un', 'jacket', ['es:body', 'mod:jacket', 'es:<emotion>'])
        make_sprites_for('un', 'pioneer', ['es:body', 'es:pioneer', 'mod:<emotion>'], emotions=['shy_smile'])
        make_sprites_for('un', 'sport', ['es:body', 'es:sport', 'mod:<emotion>'], emotions=['shy_smile'])

        make_sprites_for('us', 'bra', ['es:body', 'mod:bra', 'es:<emotion>'])
        make_sprites_for('us', 'bkrr_dress', ['es:body', 'mod:dress', 'es:<emotion>'])
        make_sprites_for('us', 'swim', ['es:body', 'es:swim', 'mod:<emotion>'], emotions=['normal_dontlike'])
        make_sprites_for('us', 'pioneer', ['es:body', 'es:pioneer', 'mod:<emotion>'], emotions=['normal_dontlike'])
        make_sprites_for('us', 'sport', ['es:body', 'es:sport', 'mod:<emotion>'], emotions=['normal_dontlike'])

        make_sprites_with_custom_emotions(['sad'], 'cs', 'body', ['mod:body', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad'], 'cs', 'panties', ['mod:body', 'mod:panties', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad'], 'cs', 'robe', ['es:body', 'mod:noshirt', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad'], 'cs', 'civil', ['mod:body', 'mod:civil', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad'], 'cs', 'civil2', ['mod:body', 'mod:civil2', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad'], 'cs', 'dress', ['mod:body', 'mod:dress', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad'], 'cs', 'swim', ['mod:body', 'es:<emotion>', 'mod:swim'])

        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'bkrr_dress', ['es:body', 'mod:dress', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'wet pioneer', ['mod:wet_pioneer', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'swim_loo', ['mod:body_loo', 'es:swim', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'swim', ['es:body', 'mod:underwear', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'jacket', ['es:body', 'mod:underwear', 'mod:jacket', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'yukata', ['mod:yukata', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'pioneer_loo', ['mod:body_loo', 'es:pioneer', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'underwear', ['es:body', 'mod:underwear', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'bkrr_sport', ['es:body', 'mod:sport', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'apron', ['es:body', 'mod:apron', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'dirt apron', ['es:body', 'mod:apron', 'mod:apron_dirt', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'shorts', ['mod:body_loo', 'mod:shorts', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'shorts_hair', ['mod:body_loo', 'mod:shorts', 'mod:hair', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'body_loo', ['mod:body_loo', 'es:<emotion>'])
        make_sprites_with_custom_emotions(['sad_smile'], 'mi', 'body', ['es:body', 'es:<emotion>'])

        make_sprites_for('mi', 'sheet', ['mod:body_loo', 'mod:sheet', 'es:<emotion>'], distances=['close'])
        make_sprites_for('mi', 'pioneer', ['es:body', 'es:pioneer', 'mod:<emotion>'], emotions=['sad_smile'])

        # Новые персонажи
        make_sprites_for('ant', 'shirt', ['mod:body', 'mod:shirt', 'mod:<emotion>'])
        make_sprites_for('kla', 'sport', ['mod:body', 'mod:sport', 'mod:<emotion>'])
        make_sprites_for('kla', 'pioneer', ['mod:body', 'mod:pioneer', 'mod:<emotion>'])
        make_sprites_for('nt', 'cook', ['mod:cook', 'mod:<emotion>'])
        make_sprites_for('tol', 'pioneer', ['mod:pioneer', 'mod:<emotion>'])
        make_sprites_for('tr', 'pioneer', ['mod:pioneer', 'mod:<emotion>'])
        make_sprites_for('tr', 'cas', ['mod:cas', 'mod:<emotion>'])

        # Спрайты, окрашенные в сепию
        make_sprites_for('mi', 'pioneer sepia', ['es:body', 'es:pioneer', 'es:<emotion>'], exclude=['sad_smile'], sprite_define_func=_sepia_sprite)
        make_sprites_for('mi', 'pioneer sepia', ['es:body', 'es:pioneer', 'mod:<emotion>'], emotions=['sad_smile'], sprite_define_func=_sepia_sprite)
        make_sprites_for('dv', 'pioneer2 sepia', ['es:body', 'es:pioneer2', 'es:<emotion>'], sprite_define_func=_sepia_sprite)
        make_sprites_for('us', 'dress sepia', ['es:body', 'es:dress', 'es:<emotion>'], sprite_define_func=_sepia_sprite)


    ## Спрайты, которые не подходят для создания автоматически

    # Мику в юкате (силуэт)

    image mi yukata dark = im.MatrixColor(MOD_IMAGES + "sprites/normal/mi/mi_3_yukata.png", im.matrix.brightness(-0.99))
    image mi yukata dark close = im.MatrixColor(MOD_IMAGES + "sprites/close/mi/mi_3_yukata.png", im.matrix.brightness(-0.99))
    image mi yukata dark far = im.MatrixColor(MOD_IMAGES + "sprites/far/mi/mi_3_yukata.png", im.matrix.brightness(-0.99))

    # Пионер, переобъявление для 1.1

    image bkrr_pi normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(ES_IMAGES + "sprites/normal/pi/pi_1_pioneer.png", bkrr_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(ES_IMAGES + "sprites/normal/pi/pi_1_pioneer.png", bkrr_tint["night"]),
        True, ES_IMAGES + "sprites/normal/pi/pi_1_pioneer.png")

    image bkrr_pi smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(ES_IMAGES + "sprites/normal/pi/pi_1_pioneer_smile.png", bkrr_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(ES_IMAGES + "sprites/normal/pi/pi_1_pioneer_smile.png", bkrr_tint["night"]),
        True, ES_IMAGES + "sprites/normal/pi/pi_1_pioneer_smile.png")

    image bkrr_pi normal dark = im.MatrixColor(ES_IMAGES + "sprites/normal/pi/pi_1_pioneer.png", bkrr_tint["night"] * im.matrix.brightness(-0.45))

    # Эл-ведроид

    image el vedro = MOD_IMAGES + "sprites/normal/el/vedro_normal.png"
    image el vedro close = MOD_IMAGES + "sprites/close/el/vedro_close.png"
    image el vedro far = MOD_IMAGES + "sprites/far/el/vedro_far.png"

    # Электроник в футболке

    image el angry shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_angry.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_angry.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_angry.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_angry.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_angry.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_angry.png"))

    image el fingal shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_fingal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_fingal.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_fingal.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_fingal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_fingal.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_fingal.png"))

    image el grin shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_grin.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_grin.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_grin.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_grin.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_grin.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_grin.png"))

    image el laugh shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_laugh.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_laugh.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_laugh.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_laugh.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_laugh.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_laugh.png"))

    image el normal shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_normal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_normal.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_normal.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_normal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_normal.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_normal.png"))

    image el sad shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_sad.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_sad.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_sad.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_sad.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_sad.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_sad.png"))

    image el scared shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_scared.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_scared.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_scared.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_scared.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_scared.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_scared.png"))

    image el serious shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_serious.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_serious.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_serious.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_serious.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_serious.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_3_serious.png"))

    image el shocked shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_shocked.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_shocked.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_shocked.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_shocked.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_shocked.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_shocked.png"))

    image el smile shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_smile.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_smile.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_smile.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_smile.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_smile.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_1_smile.png"))

    image el surprise shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_surprise.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_surprise.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_surprise.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_surprise.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_surprise.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_surprise.png"))

    image el upset shirt:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_upset.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_upset.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_upset.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_upset.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_upset.png"), bkrr_tint["night"]),
                True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/normal/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/normal/el/el_2_upset.png"))

    image el angry shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_angry.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_angry.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_angry.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_angry.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_angry.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_angry.png"))

    image el fingal shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_fingal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_fingal.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_fingal.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_fingal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_fingal.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_fingal.png"))

    image el grin shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_grin.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_grin.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_grin.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_grin.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_grin.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_grin.png"))

    image el laugh shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_laugh.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_laugh.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_laugh.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_laugh.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_laugh.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_laugh.png"))

    image el normal shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_normal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_normal.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_normal.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_normal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_normal.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_normal.png"))

    image el sad shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_sad.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_sad.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_sad.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_sad.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_sad.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_sad.png"))

    image el scared shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_scared.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_scared.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_scared.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_scared.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_scared.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_scared.png"))

    image el serious shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_serious.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_serious.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_serious.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_serious.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_serious.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_3_serious.png"))

    image el shocked shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_shocked.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_shocked.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_shocked.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_shocked.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_shocked.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_shocked.png"))

    image el smile shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_smile.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_smile.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_smile.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_smile.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_smile.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_1_smile.png"))

    image el surprise shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_surprise.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_surprise.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_surprise.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_surprise.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_surprise.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_surprise.png"))

    image el upset shirt close:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_upset.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_upset.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_upset.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_upset.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_upset.png"), bkrr_tint["night"]),
                True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/close/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/close/el/el_2_upset.png"))

    image el angry shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_angry.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_angry.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_angry.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_angry.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_angry.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_angry.png"))

    image el fingal shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_fingal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_fingal.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_fingal.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_fingal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_fingal.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_fingal.png"))

    image el grin shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_grin.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_grin.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_grin.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_grin.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_grin.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_grin.png"))

    image el laugh shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_laugh.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_laugh.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_laugh.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_laugh.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_laugh.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_laugh.png"))

    image el normal shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_normal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_normal.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_normal.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_normal.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_normal.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_normal.png"))

    image el sad shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_sad.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_sad.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_sad.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_sad.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_sad.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_sad.png"))

    image el scared shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_scared.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_scared.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_scared.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_scared.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_scared.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_scared.png"))

    image el serious shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_serious.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_serious.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_serious.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_serious.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_serious.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_3_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_3_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_3_serious.png"))

    image el shocked shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_shocked.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_shocked.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_shocked.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_shocked.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_shocked.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_shocked.png"))

    image el smile shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_smile.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_smile.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_smile.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_smile.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_smile.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_1_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_1_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_1_smile.png"))

    image el surprise shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_surprise.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_surprise.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_surprise.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_surprise.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_surprise.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_surprise.png"))

    image el upset shirt far:
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_upset.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_upset.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_alive.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_upset.png"))
        choice:
            ConditionSwitch(
                "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_upset.png"), bkrr_tint["sunset"]),
                "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_upset.png"), bkrr_tint["night"]),
                True, im.Composite((630, 1080), (0, 0), ES_IMAGES + "sprites/far/el/el_2_body.png", (0, 0), MOD_IMAGES + "sprites/far/el/el_2_shirt_dead.png", (0, 0), ES_IMAGES + "sprites/far/el/el_2_upset.png"))


    ## Спрайты для единичного использования

    # Алиса с закрытыми глазами

    image dv closed_eyes pioneer2 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/dv/dv_3_body.png", (0, 0), ES_IMAGES + "sprites/close/dv/dv_3_pioneer2.png", (0, 0), MOD_IMAGES + "sprites/close/dv/dv_3_closed_eyes.png"), bkrr_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/dv/dv_3_body.png", (0, 0), ES_IMAGES + "sprites/close/dv/dv_3_pioneer2.png", (0, 0), MOD_IMAGES + "sprites/close/dv/dv_3_closed_eyes.png"), bkrr_tint["night"]),
        True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/dv/dv_3_body.png", (0, 0), ES_IMAGES + "sprites/close/dv/dv_3_pioneer2.png", (0, 0), MOD_IMAGES + "sprites/close/dv/dv_3_closed_eyes.png"))

    # Злая улыбка Слави

    image sl evsmile swim = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/sl/sl_2_body.png", (0, 0), ES_IMAGES + "sprites/normal/sl/sl_2_swim.png", (0, 0), MOD_IMAGES + "sprites/normal/sl/sl_2_evsmile.png"), bkrr_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/sl/sl_2_body.png", (0, 0), ES_IMAGES + "sprites/normal/sl/sl_2_swim.png", (0, 0), MOD_IMAGES + "sprites/normal/sl/sl_2_evsmile.png"), bkrr_tint["night"]),
        True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/sl/sl_2_body.png", (0, 0), ES_IMAGES + "sprites/normal/sl/sl_2_swim.png", (0, 0), MOD_IMAGES + "sprites/normal/sl/sl_2_evsmile.png"))

    # Злая улыбка Ульянки

    image us evsmile pioneer = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/us/us_1_body.png", (0, 0), ES_IMAGES + "sprites/normal/us/us_1_pioneer.png", (0, 0), MOD_IMAGES + "sprites/normal/us/us_1_evsmile.png"), bkrr_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/us/us_1_body.png", (0, 0), ES_IMAGES + "sprites/normal/us/us_1_pioneer.png", (0, 0), MOD_IMAGES + "sprites/normal/us/us_1_evsmile.png"), bkrr_tint["night"]),
        True, im.Composite((900, 1080), (0, 0), ES_IMAGES + "sprites/normal/us/us_1_body.png", (0, 0), ES_IMAGES + "sprites/normal/us/us_1_pioneer.png", (0, 0), MOD_IMAGES + "sprites/normal/us/us_1_evsmile.png"))

    # Славя купается в озере

    image sl d9_swim:
        im.MatrixColor(MOD_IMAGES + "misc/d9_sl_swim.png", bkrr_tint["sunset"])
        pos(0.85, 0.6)
        anchor(0.5, 0.5)
        zoom 0.59

    # Безразличный взгляд Мику

    image mi apathy pioneer close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/mi/mi_3_body.png", (0, 0), ES_IMAGES + "sprites/close/mi/mi_3_pioneer.png", (0, 0), MOD_IMAGES + "sprites/close/mi/mi_3_apathy.png"), bkrr_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/mi/mi_3_body.png", (0, 0), ES_IMAGES + "sprites/close/mi/mi_3_pioneer.png", (0, 0), MOD_IMAGES + "sprites/close/mi/mi_3_apathy.png"), bkrr_tint["night"]),
        True, im.Composite((1050, 1080), (0, 0), ES_IMAGES + "sprites/close/mi/mi_3_body.png", (0, 0), ES_IMAGES + "sprites/close/mi/mi_3_pioneer.png", (0, 0), MOD_IMAGES + "sprites/close/mi/mi_3_apathy.png"))

    ## Разное

    # Кошак Пират

    image cat full = MOD_IMAGES + "misc/cat/cat.png"
    image cat musclub_1 = MOD_IMAGES + "misc/cat/cat_musclub_1.png"
    image cat musclub_2 = MOD_IMAGES + "misc/cat/cat_musclub_2.png"
    image cat washstand = MOD_IMAGES + "misc/cat/cat_washstand.png"

    # Стулья для столовой

    image chair = ConditionSwitch("persistent.sprite_time == 'sunset'", im.MatrixColor(MOD_IMAGES + "misc/chair.png", bkrr_tint["sunset"]), "persistent.sprite_time == 'night'", im.MatrixColor(MOD_IMAGES + "misc/chair.png", bkrr_tint["night"]), True, MOD_IMAGES + "misc/chair.png")

    image chair_l:
        "chair"
        left
        yalign 0.0

    image chair_c:
        "chair"
        center
        yalign 0.0

    image chair_r:
        "chair"
        right
        yalign 0.0

    ##    Бонусные эпизоды. Параметры и ресурсы    ##

    ## Котодень

    # CG

    image cg catday_uvao_bus = im.Scale(MOD_IMAGES + "cg/catday_uvao_bus.jpg", config.screen_width, 2918)
    image cg catday_dv_argue = im.MatrixColor(ES_IMAGES + "cg/d5_dv_argue.jpg", im.matrix.brightness(0.15) * im.matrix.contrast(1.2))
    image cg catday_warp_cat = MOD_IMAGES + "cg/catday_warp_cat.jpg"

    # Звуки

    $ bkrr_meow_list = [bkrr_sfx_list[i] for i in bkrr_sfx_list.keys() if i.startswith("meow")]

    # Музыка

    $ bkrr_music_list["i_am_a_cat"] = "mods/bkrr/sound/music/i_am_a_cat.ogg"

    # Видео

    $ bkrr_video_list["catday_ending"] = "mods/bkrr/video/catday_ending.webm"
