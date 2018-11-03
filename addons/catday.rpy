
#    Булки, кефир и рок-н-ролл. Бонус «Котодень»    #

label bkrr_addon_catday:

    $ bkrr_new_chapter("Котодень")

    scene bg int_aidpost_day with dissolve

    $ bkrr_set_time()

    play ambience ambience_medstation_inside_day fadein 3

    $ renpy.pause(1.0, hard=True)

    show cs normal close at center with dissolve

    window show

    cs "Значит, жар, головные боли, суставы крутит, головокружение. Правильно?"
    me "Да…"
    cs "У тебя жар, пионер. Будем лечиться или как? {w}Думаю, один небольшой укольчик решит твою проблему."
    me "А без укола не получится? Я бы выбрал «или как». Таблетку там, пилюлю… Порошок какой-нибудь?"

    show cs smile close at center with dspr

    "Виола зловеще хихикнула и кивнула."
    cs "Таблетку? Можно и таблетку. Сейчас, посиди, я за шуруповёртом схожу."
    me "Я помню эту шутку. Не нужно шуруповёрта."

    show cs normal close at center with dspr

    cs "Как скажешь. Подожди три минутки, я только шприц простерилизую."

    window hide

    hide cs with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Виола выключила электроплитку и достала из железной коробки стерилизатора многоразовый шприц, сноровисто его собрала. {w}Затем она хищно высосала иглой содержимое двух ампул и одного флакончика, постучала по стеклу шприца и выпустила тонкую струйку лекарства в потолок, выгоняя воздух."

    show cs normal close at center with dissolve

    cs "Снимай шорты."
    me "Только, пожалуйста, полегче."

    show cs smile close at center with dspr

    cs "Не бойся, пионер! Иголка новенькая, только весной купили. Ты даже не заметишь. Обещаю."

    window hide

    hide cs with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я со вздохом спустил шорты и трусы, оголяя место для укола. Меня звонко шлёпнули пониже спины."
    me "А это ещё зачем?"

    show cs smile close:
        center
        zoom 1.1
    with dissolve

    cs "Чтоб кровь прилила. Быстрее прильёт – быстрее лекарство впитается."
    me "Понял…"

    window hide

    hide cs with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я тихо замычал, когда внушительная многоразовая игла вонзилась в мой зад, но боль тут же ушла."

    scene cg d5_cs with dissolve

    cs "Тихо, теперь посиди. Ватку прижимай. {w}Сейчас у тебя может закружиться голова, но это нормально."
    "Она наклонилась к моему лицу. Её разноцветные глаза оказались точно напротив моих. {w}Сейчас они смотрели тепло, понимающе, но всё равно насмешливо."
    "На какую-то долю секунды мне показалось, что она хочет меня поцеловать, но медсестра всего лишь коснулась ладонью моего лба."
    "Я невзначай опустил глаза и буквально утонул в заманчивых глубинах выреза её халата. {w}Кожа Виолы была гладкой, очень светлой, без единого изъяна; от неё исходил едва уловимый пряный аромат духов и приятное тепло."

    window hide

    scene bg int_aidpost_day
    show cs smile close:
        center
        zoom 1.1
    with dissolve

    window show

    "Виола перехватила мой взгляд, понимающе улыбнулась и выпрямилась."
    cs "И куда же это мы с таким интересом смотрим? А, пионер?"
    me "У меня жар, я не соображаю, что делаю."
    cs "Раз проявляешь интерес, значит, не так ты и болен. Симулируешь?"
    me "Нет, точно нет."

    show cs normal close:
        center
        zoom 1.1
    with dspr

    cs "Если за завтрашний день не пройдёт, то поедешь в больницу. Ну-ка, вставай… {w}Только осторожно!"

    window hide

    hide cs with dissolve

    window show

    "Она подала мне руку, и я, пошатывась, принялся вставать."

    window hide

    stop ambience fadeout 5

    $ renpy.pause(0.5, hard=True)

    play music music_list["doomed_to_be_defeated"]

    play sound sfx_hell_alarm_clock

    scene bg int_aidpost_day:
        truecenter
        parallel:
            ease 0.75 zoom 1.8
            ease 0.75 zoom 1.7
            ease 0.5 zoom 1.9
            ease 0.75 zoom 1.8
            ease 0.25 zoom 2.4
        parallel:
            ease 2.0 pos(0.5, 0.25)
            ease 2.0 pos(0.5, 0.35)
            ease 1.0 pos(0.5, 0.17)
        parallel:
            ease 5.0 rotate -23.0
    with None
    show black:
        alpha 0.0
        pause 2.75
        ease 0.25 alpha 1.0
    with None

    $ renpy.pause(3.0, hard=True)

    stop sound fadeout 5

    play sound2 bkrr_sfx_list["sem_falls_on_floor"]

    window show

    "Задача была выполнена почти успешно, но тут окружающие меня вещи все, как одна, понеслись куда-то вверх, а белоснежные плитки пола больно стукнули по голове. {w}Опять…"
    th "Почему моей голове достаётся столько ударов?"
    th "Нужно было бы надеть каску… Или мотошлем… Или…"

    window hide

    $ renpy.pause(2.5, hard=True)

    stop music fadeout 3

    scene cg catday_uvao_bus:
        yalign 1.0
        linear 10.0 yalign 0.0
    with fade3

    $ bkrr_set_time("night")

    $ bkrr_set_name("uv", "Девушка")

    play ambience ambience_camp_entrance_night fadein 3

    play music music_list["sparkles"] fadein 5

    window show

    "Когда я открыл глаза, то понял, что смотрю снизу вверх на симпатичные ножки. Там, где они сходились, дразняще белели трусики."
    "Я ожидал, что на Виоле будет что-нибудь более… игривое. {w}Кружева, пояс для чулок, а здесь…"
    th "Стоп-стоп. А Виола ли это? У неё ведь хвоста не было."
    th "Точно, не было. Я бы заметил."
    "Кошачий хвост, виднеющийся из-под потрёпанного платьица, тут же вытеснил мысли о фасоне белья медсестры. Этот хвостик я уже видел. Там, в лесу…"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Я вспомнил про Мику и отвёл взгляд."
    th "Всё, Семён. Прекращаем заглядывать под платья посторонним девушкам."
    th "Мику. Думай про Мику."
    "Тем временем сверху участливо поинтересовались:"
    uv "Как ты себя чувствуешь?"
    me "Необычно…"
    "Я покачал головой. Ощущения были странные. Когда я потерял сознание, уже вечерело, но сейчас все краски вокруг были яркие и сочные."
    "Вдобавок, запахи ощущались остро и резко. {w}Запах пыли, резины, металла и почему-то бензина."
    "Я лежал на потёртом резиновом коврике, покрывавшем пол пассажирского салона автобуса."
    th "Тот самый автобус. Вот и конец моей истории… А Мику? Мы ведь только…"
    th "Нет! Только не сейчас!"
    "Я попытался закричать «Нет», но с удивлением понял, что из моей глотки доносится нечто совсем-совсем иное."

    stop music fadeout 5

    play sound bkrr_sfx_list["meow1"]

    me "Мяу…"

    stop ambience fadeout 5

    play music bkrr_music_list["i_am_a_cat"] fadein 5

    "Я подскочил, но ноги девушки так и остались на уровне моих глаз, только теперь я не утыкался носом в её пальцы, а видел их чуть сверху."

    window hide

    scene bg int_bus_night:
        align(0.5, 0.25)
        zoom 1.4
    show uv surprise2 at center
    with dissolve

    window show

    uv "Ты только не волнуйся!"
    me "Что… Что происходит?"

    show uv guilty at center with dspr

    uv "Понимаешь, твоему телу сейчас плохо, я и решила, что тебе лучше побыть вне его."

    play sound bkrr_sfx_list["meow2"]

    me "ЧЕГО???"

    show uv sad at center with dspr

    "Я услышал истошный кошачий вопль, какой доносился из-под окон каждый март, но сейчас он складывался в осмысленное слово."
    uv "Я… Я направила тебя."
    me "Куда ещё направила?"

    show uv normal at center with dspr

    "Девушка виновато прижала уши."
    uv "Понимаешь, я такого раньше не делала, ну почти не делала. {w}Ты должен был временно побыть в сознании другого Семёна в другом лагере. Для тебя это было бы как сон."
    me "И-и-и?.."

    show uv smile at center with dspr

    uv "Но у меня не очень получилось. И ты побудешь в… {w}Вот в нём."

    window hide

    hide uv with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Мне было страшно смотреть вниз. Но всё же я медленно опустил глаза."
    "Прямо передо мной, там, где полагалось быть рукам, лежали аккуратные пушистые лапы в белых «носочках». Кошачьи лапы."
    me "Я… {w}Я в коте? Я в теле кота?"

    show uv sad at center with dissolve

    uv "Да. Прости, я хотела как лучше."
    me "Я в теле кота? Я – кот?"

    show uv guilty at center with dspr

    uv "Да."
    me "Это… мне ловить птиц, ходить в туалет в ямку, лазить по деревьям, и всё такое? Всю оставшуюся жизнь?"

    show uv smile at center with dspr

    uv "Не волнуйся так. Это всего лишь до завтра. Мне нужно отдохнуть, и я верну тебя в твоё тело."
    me "А… А моё тело? Как… Что с ним? В нём кот?"

    show uv laugh at center with dspr

    "Девушка звонко рассмеялась и покачала головой."
    uv "Ну что ты такое придумал. Оно без сознания, спит крепким здоровым сном. И проспит до завтрашнего вечера."
    me "Тогда где же кот?"

    show uv smile at center with dspr

    uv "Кошки – они не такие, как мы. Они живут во многих мирах сразу, и то, что в этом кошачьем теле денёк поживёшь ты, он даже не заметит."
    me "А ты…"
    "Я показал {s}рукой{/s} лапой на её ушки и хвост."
    me "Ты тоже?"

    window hide

    show uv surprise at center with dspr

    $ renpy.pause(1.0, hard=True)

    show uv normal at center with dspr

    window show

    "Собеседница очень серьёзно посмотрела на меня, потом снова покачала головой."
    uv "Я не кошка. И не человек. Я – это я. Понимаешь?"
    me "Не очень."

    show uv smile at center with dspr

    uv "Вот и не думай об этом. Лучше попробуй встать."
    "Я попытался подняться на ноги, но тут же завалился набок."
    me "Что такое? Я будто пьяный."
    uv "У тебя теперь четыре лапы, а не две ноги. Нужно привыкнуть."
    me "Я не хочу привыкать! Я хочу обратно свои ноги!"
    "Внезапно я понял, что моя спина легко и органично изогнулась дугой, мышцы в районе копчика напряглись, а… а там, внизу спины, где ничего не должно было быть, было очень странное ощущение. {w}Словно ещё один палец… только очень гибкий и подвижный. Сейчас он непроизвольно подёргивался."

    window hide

    show uv smile close at center with dissolve

    $ renpy.pause(0.3, hard=True)

    show uv smile close:
        center
        sit_down1
    with None

    window show

    "Она наклонилась и взяла меня на руки."
    uv "Придётся потерпеть."

    window hide

    stop music fadeout 5

    play ambience ambience_camp_entrance_night fadein 3

    scene bg ext_camp_entrance_night with dissolve

    $ bkrr_get_achievement("catday")

    $ renpy.pause(1.0, hard=True)

    window show

    "Девушка легко спрыгнула по ступенькам, и мы оказались у главных ворот. {w}Я осторожно посмотрел через её плечо."

    scene bg ext_bus_night with dissolve

    "Конечно, это был он. {w}Красно-белый «Икарус», тот самый, что привёз меня сюда."

    scene bg ext_camp_entrance_night
    show uv smile close at center
    with dissolve

    uv "Твоему сознанию нужно обжиться в новом теле. Лучше всего, если ты сейчас поспишь."
    me "Откуда ты знаешь? Ты же не делала этого раньше?"

    show uv guilty close at center with dspr

    uv "Я так думаю. Пойдём, отнесу тебя в твоё логово."
    me "Логово?"

    show uv laugh close at center with dspr

    uv "До-мик. {w}Да, домик. Вы их так называете."

    window hide

    stop ambience fadeout 2

    scene bg ext_houses_night_bkrr with fade2

    play ambience ambience_camp_center_night fadein 3

    window show

    "Она бережно несла меня на руках, а я смотрел по сторонам, слишком шокированный, чтобы удивляться."
    "Вокруг явно была ночь, но при этом я отчётливо видел всё вокруг, словно в сумерках. {w}Путешествие во времени и смена тела на молодое немного подготовили меня к тому, что произошло, но всё равно, ощущать себя в кошачьем теле было очень странно."
    "Чтобы отвлечься, я попытался завести беседу:"
    me "Как тебя зовут?"

    show uv smile close at center with dissolve

    uv "Ты всё равно не выговоришь. Вообще, ты называешь меня Юлей."
    me "Как я могу называть тебя Юлей, если я тебя впервые вижу?"

    $ bkrr_set_name("uv", "Юля")

    uv "А вот и не впервые!"
    "Она дружески почесала меня за ухом. Волна удовольствия прокатилась от уха к затылку и мягко растеклась по спине. Я вдруг ощутил, что моё горло на выдохе стало странно вибрировать и издавать урчание."
    "Юля улыбнулась мне."
    uv "Вот! Мурлыкать уже научился. Это главное для кошки."
    me "Я что, ещё и кошка, а не кот?"

    show uv laugh close at center with dspr

    "Она бесцеремонно перехватила меня под мышки, и я ничего не мог с этим поделать, только болтать {s}ногами{/s} {s}лапами{/s} задними конечностями в воздухе."
    uv "Нет-нет. {w}Кот. Стопроцентный, настоящий кот."
    "Она поднесла меня поближе к лицу, мне вдруг стало неловко, и я попытался поджать лапы, чтобы прикрыть то, что она рассматривала."
    "Неожиданно, хвост сам собой изогнулся и прижался к животу, прикрыв нужное место."
    "Юля захихикала."
    uv "Ты быстро учишься."

    window hide

    scene bg ext_house_of_mt_night_without_light
    show uv smile close at center
    with fade3

    window show

    uv "Вот, мы пришли."

    stop ambience fadeout 0.5

    play sound sfx_door_squeak_light

    scene bg int_house_of_mt_night2 with dissolve

    play ambience ambience_int_cabin_night fadein 3

    "Она осторожно открыла дверь. {w}Ольга уже лежала в своей кровати, а на моей громоздилась куча одежды. Вот, значит, как. Мне бумажку на пол нельзя кинуть, а сама развела такой беспорядок!"

    show uv smile close at center with dissolve

    uv "Куда тебя положить? На свою кровать или...?"
    "Она улыбнулась и показала подбородком в сторону Ольги. {w}Вожатая томно потянулась во сне и что-то пробормотала."
    me "Эй-эй, подожди. Как это «куда»? Если она проснётся, то…"

    show uv laugh close at center with dspr

    uv "То улыбнётся и примется тебя тискать. Ты ей очень нравишься. То есть не ты, а Пират."
    me "Так я… {w}я в теле Пирата?"

    show uv guilty close at center with dspr

    uv "Да. Времени было мало: или в кота, или там ещё летучая мышь была возле окна."
    me "Спасибо, что не в мышь. Они противные."

    show uv smile close at center with dspr

    uv "А по-моему, очень симпатичные."

    window hide

    hide uv with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Она сдвинула горку Ольгиной одежды и устроила меня на подушке."

    show uv smile at center with dspr

    uv "Теперь спи. Завтра вечером приходи ко мне в лес, я верну всё, как было."
    me "Точно вернёшь?"

    show uv laugh at center with dspr

    uv "Не знаю!"

    hide uv with dissolve

    "Она беззвучной тенью исчезла за дверью, оставив меня один на один с фактом, что я теперь кот. Во всяком случае, до завтра."
    "Нестерпимо зачесался затылок. Я машинально потянулся к нему и…"

    show red:
        alpha 0.3
        ease 0.25 alpha 0.0
    with hpunch

    th "Ой! Больно!"
    "…немедленно оцарапался когтем."
    th "Нужно осторожнее, а то вдруг соринка в глаз попадёт, и я его сам себе вырву. Глупо получится."
    "От нечего делать я повернул к себе покрытую шерстью {s}руку{/s} лапку и попытался выпустить когти."
    "Четыре острия тут же показались из-за подушечек, затем втянулись обратно."

    window hide

    show blink

    $ renpy.pause(2.0, hard=True)

    window show

    "Я развлекался таким нехитрым способом, пока не заснул."

    window hide

    stop ambience fadeout 2.5

    $ renpy.pause(2.5, hard=True)

    scene bg int_house_of_mt_day
    show unblink
    with None

    $ bkrr_set_time()

    play ambience ambience_int_cabin_day fadein 3

    play music music_list["my_daily_life"] fadein 5

    $ renpy.pause(1.5, hard=True)

    window show

    "Проснулся я от того, что на меня упало что-то розовое, лёгкое и очень приятно пахнущее. Не такой хищно-пряный аромат, как у Виолы, но лёгкий и очень женственный."
    "Я не сразу понял, что происходит, но потом воспоминания о вчерашнем вечере безжалостно разбили моё замечательное утреннее настроение."
    th "Это же духи Ольги…"
    th "Стоп-стоп. Если это её ночная рубашка, то на ней сейчас… {b}ничего{/b} нет?"
    "Я осторожно выглянул из-под душистого розового покрывала и потерял дар речи. {w}Кошачьей речи."

    window hide

    scene cg d2_mt_undressed with dissolve

    window show

    "На Ольге Дмитриевне действительно почти ничего не было."
    "Изящная загорелая спина без полос от загара, тонкая талия, стройные бёдра, обтянутые тонкими чёрными чулками… {w}Я подался вперёд, чтобы рассмотреть её получше, но из-под моих лап посыпались карандаши, ручки и ещё какая-то канцелярская дребедень. "

    scene cg d2_mt_undressed_2 with dspr

    extend "Они застучали по полу, а Ольга сердито оглянулась через плечо."
    "Увидев меня, она улыбнулась и продолжила одеваться."
    mt "Какого… {w}А, это ты, котейка."
    mt "Пришёл Семёна проведать? Так его нет, он приболел."

    window hide

    scene bg int_house_of_mt_day with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Нужно было что-то сказать, поэтому я вполне правдоподобно мяукнул, положил морду на лапы и отвернулся в сторону."
    "Застегнув рубашку и повязав галстук, Ольга подошла к зеркалу и повернулась перед ним."

    show mt smile pioneer at center with dissolve

    mt "А я думала, кто-то подглядывает. {w}Ведь поглядеть-то есть на что, правда?"

    hide mt with dissolve

    "Она убрала с меня свою ночную рубашку, потом погладила между ушей... {w}Всё-таки бытие котом имеет свои преимущества. Когда я застал её в таком виде, то она на меня наорала. А тут, скажите, пожалуйста."
    mt "Раз твой хозяин про тебя забыл, давай мама тебе что-нибудь найдёт."
    mt "Что тут у нас… Печенье, яблоки… О! Вот!"

    show mt smile pioneer at center with dissolve

    "Она достала из тумбочки тарелку с бутербродом, отрезала от кружка колбасы хорошую часть и бросила на пол."
    mt "На, ешь! Вкусная, почти свежая."

    hide mt with dissolve

    "Я потрогал лапой розовый ломтик, лежащий на полу."
    "Пахло вкусно, рот наполнился слюной, но есть с пола… {w}Нет, я не настолько голоден."

    show mt sad pioneer close at center with dissolve

    mt "Ну, чего ты? Кушай!"

    show mt sad pioneer at center with dspr

    "Я отодвинулся и отвернулся от угощения."
    mt "Значит, не будешь? {w}Ладно-ладно."
    mt "Придёшь ты ещё у меня подкормиться. Только продукт испортила. Лучше бы Семёна угостила."

    window hide

    hide mt with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Вожатая принюхалась, потом покачала головой."

    show mt sad pioneer at center with dissolve

    mt "Надо же, испортилась. Лучше выброшу."
    mt "А то Семён слопает и после простуды сразу с отравлением в лазарет ляжет. {w}Виола подумает, что я нарочно."

    window hide

    hide mt with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Она вздохнула, завернула бутерброд в газету и бросила в мусорное ведро."

    show mt normal pioneer at center with dissolve

    mt "Всё, больше ничего нет! Иди мышку поймай или птичку."

    show mt angry pioneer at center with dspr

    mt "Иди, иди!"
    th "Кажется, она обиделась. А что делать? С пола есть?"

    window hide

    stop ambience fadeout 0.5

    scene bg ext_house_of_mt_day with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show

    "Я легко спрыгнул с порога, мимолётно удивившись, как легко управляю кошачьим телом."
    "Где-то на краю сознания билась мысль, что это неправильно и что мне положено выть и думать, как вернуть себе человеческое обличье. {w}Но это было… забавно."

    window hide

    stop music fadeout 5

    scene bg ext_houses_day with dissolve

    window show

    "Мне было всё равно, куда направиться, так что я машинально переступал пушистыми кошачьими лапами и почти не обращал внимания на то, куда иду."

    window hide

    scene bg ext_music_club_day_bkrr with dissolve

    window show

    "Когда я прекратил прислушиваться к ощущениям от изменившегося тела и огляделся, то понял, что пришёл в музклуб."

    window hide

    scene bg ext_music_club_verandah_day_v5 with dissolve

    window show

    "Несмотря на ранний час, из-за дверей доносилось приглушённое бормотание."
    "Дверь оказалась приоткрыта, так что я осторожно подцепил её когтями и потянул."

    window hide

    stop ambience fadeout 0.5

    play sound sfx_door_squeak_light

    scene bg int_music_club_mattresses_day with dissolve

    play ambience ambience_music_club_day fadein 3

    window show

    dv_v "М-м-м… ладонь… тронь… огонь… {w}БЛИН!!!"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Алиса сидела на своём любимом месте у окна и что-то писала в тетради. Периодически она мотала головой, энергично зачёркивала написанное, тихо шипя себе под нос ругательства."

    show dv smile bkrr_sport at center with dissolve

    dv "Ага! Пришёл, блохастик?"
    dv "Иди сюда, дай я твоё жирное пузо почешу! Скоро Ульяну по весу перегонишь."

    window hide

    show dv normal bkrr_sport at center with dspr

    $ renpy.pause(1.0, hard=True)

    show dv guilty bkrr_sport at center with dspr

    window show

    "Я опасливо держался на расстоянии от нашей гитаристки. Мало ли что? Вдруг она Пирата привыкла за хвост таскать?"
    dv "Ну, ты чего, как неродной? Иди сюда, говорю! Кис-кис-кис!"

    hide dv with dissolve

    "Может, рыжая хулиганка и любила ставить фингалы смазливым кибернетикам, но кот, в тело которого я угодил, явно числился её любимчиком. Алиса небрежно стянула обувь, протянула ногу в белоснежном носке и принялась поглаживать мне живот."
    "Снова это странное ощущение, словно горло сжалось и принялось мелко вибрировать. Воздух выходил из моих лёгких с мягким урчанием, и это было очень приятно."

    show dv laugh bkrr_sport close at center with dissolve

    dv "Ага! Нравится?"
    th "Очень!"

    hide dv with dissolve

    "Она отняла ногу, и я едва подавил искушение обхватить её лапами и не отпускать."
    "Алиса снова принялась чёркать что-то в тетради. Я осторожно попытался заглянуть в неё, но пионерка захлопнула её перед самым моим носом."

    show dv normal bkrr_sport close at center with dissolve

    dv "Что-то есть охота… {w}Что тут у нас пожевать осталось?"

    hide dv with dissolve

    "Она со вздохом достала из тумбочки пакет кефира, подозрительно понюхала."
    dv "Со вчерашнего утра лежит! Не пропал, как ты думаешь, котяра? Если прокис, то его пить уже нельзя."
    "Она помолчала, затем хитро улыбнулась."

    show dv smile bkrr_sport close at center with dissolve

    dv "Придумала! Давай на тебе проверим! Вдруг он уже испортился."

    show dv normal bkrr_sport close at center with dspr

    dv "Пиратик… Хочешь кефира? Вкусный-вкусный!"

    hide dv with dissolve

    "Алиса поставила на пол блюдце и плеснула в него кефира из пакета."
    "Пахло не очень хорошо. {w}Со вчерашнего дня я ничего не ел, но лакать подозрительную водянистую жижу тоже не хотелось."
    "С другой стороны, случай был слишком удобным, чтобы его упускать."
    "Я осторожно лизнул кефир. Он оказался основательно прокисшим и отвратительным на вкус."
    th "Интересно, как выразить, что он мне нравится?"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Я притворился, что лакаю, а потом принялся тереться об ноги Алисы и старательно мурлыкать, затем пару раз мяукнул, словно прося добавки."
    "Алиса показала мне язык и налила кефир в свою любимую чашку."

    show dv laugh bkrr_sport at center with dissolve

    dv "Ещё чего! Всё, иди гуляй. Это я сама допью!"

    hide dv with dissolve

    th "Ой, что сейчас будет…"

    play music music_list["that_s_our_madhouse"]

    "Она залпом опрокинула в себя кефир, а затем скривилась."

    show dv angry bkrr_sport at center with dissolve

    dv "Ой, какая гадость…"

    show dv rage bkrr_sport at center with dspr

    dv "Ты что, нарочно, гадина шерстяная? А ну, брысь отсюда!"

    window hide

    hide dv with dissolve

    stop ambience fadeout 1.5

    $ renpy.pause(1.0, hard=True)

    scene bg ext_music_club_verandah_day_v5:
        align(0.5, 0.4)
        zoom 1.25
    show dv angry bkrr_sport close at center
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show

    "Её голос звучал раздражённо, и я был готов уворачиваться от летящего тапка, но Алиса всего лишь взяла меня под мышки и выставила за дверь."
    dv "Иди отсюда!"

    hide dv with dissolve

    th "Ладно, розыгрыш – это здорово, но надо бы раздобыть что-нибудь поесть. {w}Или учиться ловить мышей."
    th "Как, оказывается, Пирата все любят и знают…"

    window hide

    stop music fadeout 5

    scene bg ext_music_club_day_bkrr with dissolve

    window show

    "Я затрусил по аллее, ведущей к воротам и клубу кибернетиков."

    window hide

    stop ambience fadeout 3

    scene bg ext_clubs_day:
        align(0.5, 0.4)
        ease 4.0 zoom 1.25
    with fade3

    play ambience ambience_camp_center_day fadein 3

    window show

    th "Кибернетики! Наверняка у них найдётся лежащий без присмотра бутерброд."

    window hide

    stop ambience fadeout 0.5

    scene bg int_clubs_male_day with dissolve

    play ambience ambience_medium_crowd_indoors_1 fadein 3

    window show

    "Бутербродов в мастерской не оказалось. {w}Зато было много шума и гама."
    "Небольшая комната была заполнена пионерами из младших отрядов, которые галдели, норовили покрутить ручки на приборах или подёргать модели планеров. Двое самых ушлых уже добрались до робота и старались отвинтить ему руку, видимо, на память о лагере."
    "Электроник с Шуриком пытались держать мелких под контролем, но стоило им угомонить одного, как за их спинами начинали хулиганить двое других."

    show el sad pioneer at left
    show sh serious pioneer at right
    with dissolve

    el "Шурик, что делать будем?"
    sh "Не знаю! Давай, по физике им чего-нибудь покажи. Нам бы только до завтрака продержаться!"

    show el smile pioneer at left with dspr

    "Электроник напряжённо улыбнулся и почесал в затылке."
    el "Знаю! Давай им опыты с электричеством покажем!"

    show sh normal_smile pioneer at right with dspr

    sh "Точно."

    window hide

    hide el with dissolve

    show sh smile pioneer at center with ease

    window show

    "Шурик натянул ненатуральную улыбку и повернулся к аудитории."
    sh "Смотрите! Вы знаете, откуда берётся электричество?"

    stop ambience fadeout 3

    play music music_list["you_won_t_let_me_down"] fadein 5

    "Мелкие переглянулись и принялись строить версии."

    window hide

    $ bkrr_thoughts_show("Из розетки?", "Из батарейки!", "Из электростанции!")

    show sh normal pioneer at center with dspr

    window show

    sh "Правильно. А знаете, как быстро получить электрический заряд прямо сейчас?"
    sh "Смотрите!"

    show sh serious pioneer at center with dspr

    "Он достал странный прибор, похожий на стеклянный барабан с железкой внутри."
    sh "Это называется электроскоп! Видите две пластинки?"

    show sh normal pioneer at center with dspr

    sh "Сейчас я поднесу к прибору вот эту палочку, и ничего не произойдёт. Но если мы зарядим их статическим электричеством."
    "Шурик блеснул очками в сторону Электроника."

    show sh normal_smile pioneer at center with dspr

    sh "Сыроежка, давай шерстяную тряпку!"

    show el upset pioneer at left with easeinleft

    el "Саш… а она… Мокрая. В масле она."

    show sh surprise pioneer at center with dspr

    sh "Как мокрая?"

    show el normal pioneer at left with dspr

    el "Мы же масло разлили, ты сам её ухватил и стал вытирать."

    show sh normal pioneer at center with dspr

    sh "Вот незадача. И как мне теперь наэлектризовать эбонитовый стержень?"

    window hide

    hide el
    hide sh
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    th "Ты, чем электризовать эбонитовые стержни, лучше бы свой нефритовый держал под контролем! Совратитель медицинских работников, хе-хе…"
    "Вместо смеха у меня вырвалось нечто среднее между чиханием и фырканием. Шурик молниеносно сориентировался и показал на меня."

    show sh normal pioneer at right with dissolve

    sh "Давай вот его!"
    "Электроник осторожно посмотрел на твёрдый гладкий эбонитовый стержень в руках Шурика, затем на мелкого рыжего пионера, сидевшего рядом с дверями. {w}Рыжий тоже вздрогнул и напрягся."
    sh "Давай его сюда!"

    show el surprise pioneer at left with dissolve

    el "Саш… а ты чего с ним делать собрался?"
    sh "Я про кота!"

    show el smile pioneer at left with dspr

    el "А, про кота… "

    show el smile pioneer close at left with dspr

    extend "Пират, иди-ка сюда!"

    hide el with dissolve

    "Он нагнулся, взял меня в руки и усадил на стол. Шурик приложил палочку к моему боку."

    show sh normal_smile pioneer close at center with dissolve

    sh "Теперь смотрите: шерсть кота накапливает статическое электричество, и если мы сейчас…"
    "Из-за спины раздался противный скрип. Я скосил глаза и увидел, как Шурик крошит кусок пенопласта на маленькие шарики."

    show sh normal pioneer close at center with dspr

    sh "… посыплем на кота кусочками пенопласта, то накопленный заряд их притянет!"

    window hide

    hide sh with dissolve

    $ renpy.pause(1.0, hard=True)

    stop music fadeout 7.5

    window show

    "Мелкие белые шарики липли к моей… в смысле, к шерсти нашего кота, а малышня довольно смеялась, некоторые даже захлопали."
    "Шурик, явно довольный вниманием, продолжал, осторожно водя палочкой мне по боку:"

    show sh normal pioneer at center with dissolve

    sh "А ещё мы можем натереть об его шёрстку эбонитовую палочку, создав статический заряд, и потом поднести её к электроскопу…"

    window hide

    play sound sfx_scary_sting

    play music music_list["awakening_power"]

    scene cg catday_warp_cat:
        truecenter
        zoom 1.25
        ease 0.5 zoom 1.0
    with bkrr_fade(0.5)

    window show

    sh "Ай!"

    play sound bkrr_sfx_list["kitchen_mayhem"]

    "То ли заряд получился слишком большой, то ли у котов такой низкий болевой порог, но накопившийся заряд пронзил всё моё тело, сильно кольнув под хвост."
    "Я вырвался и помчался по столу."
    "На пол полетели баночки с шурупами, какие-то железки, робот опрокинулся на спину, призывно раскинув железные бёдра."
    "Я выскочил за дверь, сопровождаемый звонким детским смехом и воплями Шурика."
    sh "ЗАРАЗА МОХНАТАЯ!!! УБЬЮ!!! ДОГОНЮ И УБЬЮ!!! СТО-О-ОЙ!!!"

    window hide

    stop music fadeout 5

    scene bg ext_square_day with dissolve

    play ambience ambience_camp_center_day fadein 5

    window show

    "Бежалось в кошачьем теле легко и быстро. {w}Несколько секунд, и разъярённый Шурик остался далеко позади."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Я присел и попытался вычесать из шерсти пенопласт. Шарики были мелкие, а дотягивался я не везде, так что вскоре решил плюнуть на эту затею и походить как есть."

    play sound sfx_dinner_horn_processed

    "Репродуктор на столбе зашипел, а потом разразился записью сигнала на завтрак."

    window hide

    stop sound fadeout 3

    scene bg ext_dining_hall_away_day with dissolve

    $ renpy.pause(1.0, hard=True)

    scene bg ext_dining_hall_near_day with dissolve

    window show

    "По устоявшейся привычке я направился туда же, куда и все: к столовой. Сейчас чего-нибудь перехватим, и…"

    show nt smile cook at center with dissolve

    nt "И куда же мы так вышагиваем, а? Пока пионеры едят, коты ждут на улице! Забыл?"
    th "Я и не знал..."

    play sound bkrr_sfx_list["meow5"]

    me "Тётя Наташа, выручайте, есть хочу!"
    nt "Котик голодный?"

    play sound bkrr_sfx_list["meow4"]

    me "Да-а-а! А что у вас есть?"

    show nt normal cook at center with dspr

    nt "Ну, ты посиди, пока завтрак закончится. Тут Саша карасиков наловил, на уху. Я тебе сейчас дам покушать!"

    window hide

    $ bkrr_timeskip_short()

    scene bg ext_dining_hall_near_day with bkrr_timeskip_transition()

    window show

    "Время тянулось так долго. Я сидел на крыльце, слушая, как пионеры звенят ложками о тарелки, и втягивал идущие из окон ароматы."
    th "Уха… Здорово! Я рыбу не очень люблю, но наваристый янтарно-жёлтый, с кусочками зелени и медальками жира, плавающими на поверхности, рыбный суп, это совсем другое."
    th "Тётя Наташа, если с Мику у нас ничего не выйдет, то я точно на вас женюсь!"
    "Наконец, из кухни донеслось долгожданное:"
    nt "Пират! Кис-кис-кис! Смотри, какая вкуснятина!"

    window hide

    stop ambience fadeout 0.5

    scene bg int_dining_hall_day with dissolve

    play music music_list["smooth_machine"] fadein 5

    play ambience ambience_dining_hall_empty fadein 3

    window show

    "Предвкушая полную миску горячей ухи, я со всех ног помчался на этот зов."

    show nt normal cook at center with dissolve

    nt "Вот! Кушай, только осторожно, косточки не глотай."
    th "Да вы издеваетесь!"
    "Миска действительно была полной, но не ухи, а рыбьих голов. {w}Они укоризненно смотрели на меня мутными глазками, а одна даже слабо подёргивала жабрами. Меня замутило."
    me "Не-не-не… В другой раз!"

    show nt sad cook close at center with dspr

    nt "Котя, что такое? Свеженькие! Бери, кушай!"

    hide nt with dissolve

    th "Неужели в такой большой столовой никто не оставил несъеденную котлетку? Да быть не может!"
    "Увы, пионеры в лагере отличались отличным аппетитом, и тарелки на столах даже мыть было необязательно."
    "Тут я ощутил густой манящий мясной аромат, он шёл со стола вожатых."
    "Там в гордом одиночестве стояла полная тарелка пюре, а на краю, выгодно оттенённая зелёным горошком, исходила аппетитным паром горячая, восхитительно румяная котлета."
    me "Да-а-а... {w}О, да! {w}ДА!!!"
    "Я сам не понял, как, но мои ноги сами собой согнулись в коленях, словно отвечая моему желанию быть как можно незаметнее, и мягко понесли меня по направлению к столу. {w}Тем временем от окошка раздачи доносились знакомые голоса."

    show nt sad cook at left
    show mt normal pioneer at right
    with dissolve

    nt "Оля, ты так и не поела?"

    show mt sad pioneer at right with dspr

    mt "Нет. Забегалась с утра. У меня там бутерброд лежал, думала им позавтракать, но он испортился. Даже кот есть не стал."
    nt "Ой, знаешь, он и у меня рыбку тоже не стал. Может, приболел?"

    show nt normal cook at left

    nt "Давай вот у Виолы спросим! Виола, а ты в кошачьих болезнях не разбираешься?"

    window hide

    hide nt
    hide mt
    with dissolve

    show cs normal at center with dissolve

    window show

    "Медсестра нараспев произнесла:"
    cs "Санитарное состояние посуды удовлетворительное? {w}Удовлетворительное."

    show cs smile at center with dspr

    cs "Еда приготовлена качественно. {w}Даже, я бы сказала, потрясающе."

    show cs normal at center with dissolve

    cs "Дата, подпись."
    "Потом, после небольшой паузы, она ответила:"
    cs "Нет, Натали. Кошки – это не моё. Это к ветеринару! Мне и больного пионера хватит."

    window hide

    show cs normal at left with ease

    show mt smile pioneer at right with easeinright

    window show

    mt "Как там Семён, кстати? Скоро вернётся в отряд?"
    cs "В отряд? Хм… Ну, конечно же, в отряд. Вроде температура сошла."

    show cs shy at left with dspr

    cs "Что, уже соскучилась без молодого-интересного в соседней кровати? Понимаю, понимаю…"

    show mt surprise pioneer at right with dspr

    mt "Нет!"

    show cs smile at left with dspr

    cs "Спит твой Семён. Я его попыталась разбудить, но он только что-то проворчал, даже глаз не открыл. Потерпи ещё немного. Думаю, завтра выпишу."

    show mt sad pioneer at right with dspr

    mt "Да не мой он! Просто я переживаю за пионера из отряда…"

    show mt angry pioneer at right with dspr

    mt "И нечего так улыбаться!"

    window hide

    hide mt
    hide cs
    with dissolve

    show nt smile cook at center with dissolve

    window show

    nt "Да брось ты. Она же тебя дразнит."

    window hide

    hide nt with dissolve

    show cs smile at center with dissolve

    window show

    cs "Дразню, конечно. Но ты глянь, как она покраснела. Вы что-то недоговариваете, Ольга Дмитриевна?"

    hide cs with dissolve

    "По столовой разнёсся смех Натальи, чуть позже к ней присоединились и Ольга с Виолой."

    show mt smile pioneer at center with dissolve

    mt "Ну вас! Давайте лучше есть."

    show cs normal at right with easeinright

    cs "Я у себя позавтракала, так что пойду."

    window hide

    hide cs with easeoutright

    show mt smile pioneer at right with ease

    show nt smile cook at left with easeinleft

    window show

    nt "Оля, я тебе вон там порцию оставила. {w}Пить что будешь? Чай, кофе, что покрепче?"

    show mt grin pioneer at right with dspr

    mt "А что, у тебя есть и покрепче?"
    nt "Палыч из города домашнего вина привёз. Слабенькое, но вкусное-вкусное. Будешь?"

    show mt sad pioneer at right with dspr

    mt "Вот сейчас возьму и выйду к пионерам с факелом изо рта."

    show nt sad cook at left with easeinleft

    nt "Ой, да брось ты! От пятидесяти грамм ничего не будет."

    show cs shy at center with dissolve

    cs "А вы что, без меня пить собрались?"
    nt "Ой, ну что ты такое говоришь?"

    show mt smile pioneer at right with dspr

    mt "Только если пятьдесят грамм, для аппетита. Перед сном, наверное, ешё чуть-чуть приму, очень плохо спала."

    show cs smile at center with dspr

    cs "Странно. Почему плохо? Соседа-то нет? Нет причины, чтобы не высыпаться."

    show nt laugh cook at left
    show mt angry pioneer at right
    with dspr

    mt "ВИЛКА!!!"

    show nt smile cook at left
    show cs shy at center
    show mt sad pioneer at right
    with dspr

    mt "Мне в жару плохо спится! Жарко, понимаешь?"

    show cs normal at center with dspr

    cs "Надо же, как она реагирует. Я шучу, не волнуйся. Ну, за педагогических работников!"
    "Она помолчала, затем весело добавила:"

    show cs smile at center with dspr

    cs "И любовь к детям!"
    "Я мысленно улыбнулся."

    hide nt
    hide cs
    hide mt
    with dissolve

    stop music fadeout 5

    th "Интересно, она про нас с Ольгой или про себя с Шуриком?"

    window hide

    scene cg d1_food_normal:
        align(0.5, 0.95)
        ease 5.0 zoom 1.2
    with dissolve

    $ renpy.pause(2.5, hard=True)

    window show

    "Тарелка осталась без присмотра."
    "Я вскочил на стул, потом на стол, схватил обжигающую котлету в пасть и помчался к выходу."

    play music music_list["revenga"]

    scene bg int_dining_hall_day with dissolve

    cs "Оля! Кот твою котлету украл!"
    nt "Стой, ворюга!!!"
    mt "Пират, зараза такая!!!"

    window hide

    scene bg ext_dining_hall_near_day with dissolve

    $ renpy.pause(1.0, hard=True)

    scene bg ext_dining_hall_away_day with dissolve

    $ renpy.pause(1.0, hard=True)

    scene bg ext_path2_day with dissolve

    $ renpy.pause(1.0, hard=True)

    stop music fadeout 5

    play ambience ambience_forest_day fadein 5

    window show

    "Метко пущенный половник врезался в дверь у самой моей головы. Я прибавил ходу и умчался в заросли."
    th "Вот, значит, что чувствовала Ульяна, когда я за ней гнался."

    window hide

    scene bg ext_polyana_day with fade3

    window show

    "Кот там или не кот, а есть с земли всё равно было противно, так что я отыскал большой лист лопуха и устроил на нём добычу."

    uv_v "Приятного аппетита!"

    play sound sfx_bush_leaves

    "Кусты зашуршали, и из них показалась знакомая девочка."

    show uv smile far at center with dissolve

    me "Юля?"

    show uv surprise at center with dspr

    uv "А кого ты ждал?"
    me "Вожатую, медсестру, повариху, а может быть, Алису. {w}Или Шурика. Мы с ними немножко… не в ладах."

    show uv laugh at center with dspr

    uv "Интересный набор."
    me "У меня было очень насыщенное утро. Ой, как есть охота!"

    hide uv with dissolve

    "Я попытался откусить кусок от котлеты, но она ещё не остыла, я только обжёг рот и зафыркал."
    me "Не поможешь?"

    show uv smile close at center with dissolve

    uv "Конечно."
    "Она разломила добычу на части, затем взяла один ломтик и принялась с аппетитом его жевать."
    me "Эй! Не объедай безответное животное!"

    show uv laugh close at center with dspr

    uv "Ничего не знаю."
    "Она почесала меня за ухом."
    uv "Не ты один котлеты тёти Наташи любишь!"
    me "Ты их пробовала?"

    show uv smile close at center with dspr

    uv "Конечно! Там окно не запирается."

    window hide

    hide uv with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я не совсем понял связь, так что принялся жевать котлету, отложив разгадки ребусов на потом."
    me "Ты ещё не отдохну…"
    "Я не договорил, так как снова остался один. Юля грациозно подпрыгнула вверх, зацепилась за ветку и быстро исчезла в зелени."
    me "Значит, по деревьям скакать у неё силы есть. А вернуть меня обратно – нет. Вот ведь зараза ушастая!"

    play sound sfx_bush_leaves

    show uv laugh:
        center
        yanchor 0.4
        ypos 0.0
        rotate 185
    with easeintop

    uv "Сам такой!"

    window hide

    hide uv with easeouttop

    $ renpy.pause(0.5, hard=True)

    play sound sfx_punch_medium

    scene bg ext_polyana_day:
        truecenter
        parallel:
            linear 0.15 rotate -1
            linear 0.15 rotate 0.5
            linear 0.15 rotate -0.5
            linear 0.15 rotate 0
        parallel:
            ease 0.25 zoom 1.05
            ease 0.5 zoom 1.0
    show red:
        alpha 0.0
        ease 0.1 alpha 0.3
        ease 0.1 alpha 0.0
    with vpunch

    $ renpy.pause(1.0, hard=True)

    window show

    "Сверху прилетела сосновая шишка, больно стукнув меня по макушке, а потом я услышал удаляющийся девичий смех."
    me "Очень смешно!"

    window hide

    stop ambience fadeout 3

    scene bg ext_path2_day with fade3

    play ambience ambience_forest_day fadein 3

    $ renpy.pause(1.0, hard=True)

    window show

    "То ли голова у кота маленькая, то ли желудок большой, но пока я был голоден, желание поесть забивало все остальные мысли. Зато теперь мне страшно захотелось увидеть Мику."
    th "Ну и что, что она меня не узнает?"

    window hide

    stop ambience fadeout 0.5

    scene bg ext_houses_day with dissolve

    play ambience ambience_camp_center_day fadein 3

    $ renpy.pause(1.0, hard=True)

    window show

    "Я осторожно выглянул из кустов. По аллее прошёл Шурик с длинной тонкой палкой, высматривая что-то и шурша своей хворостиной в кустах и под домиками."
    th "Интересно, он решил стать лозоходцем и ищет место для колодца, или хочет сломать эту палку об мою пушистую спинку? Очень не хочется проверять."
    "Подождав, пока мстительный кибернетик уйдёт подальше, я на полусогнутых побежал к домику Мику."
    "По пути воображение рисовало заманчивую картинку, как она поцелует меня в кошачий нос и я тут же превращаюсь в прекрасного прин… Кхм. Пионера Семёна."

    window hide

    scene bg ext_house_of_un_day with dissolve

    window show

    "За дверью негромко переговаривались."
    "Голос Лены я узнал, а вот второй звучал смущённо и приглушённо. Это точно была не Мику."
    sl_v "Стыдоба-то какая. Как я вообще дала себя уговорить?"
    un "Я так рада, что ты согласилась. Знаешь, это ведь не совсем обычная просьба."
    un "Я боялась, что ты не захочешь. Мне… было непросто тебя просить о таком. Но если ты передумала…"
    sl_v "Нет-нет. Я тоже этого хочу. Просто я никогда раньше такого не делала."
    un "А я пробовала. Один раз. С подругой из кружка. Но тогда я ещё ничего не умела, у меня плохо получилось."
    sl_v "А сейчас, значит, получится лучше?"
    un "А сейчас получится. Ты не пожалеешь, честное слово!"
    sl_v "Только запри двери, пожалуйста."
    un "Да, если придёт вожатая, то заругает. Ей не понять."
    sl_v "Это точно. Не понять. Мне уже раздеваться, да?"
    un "Да. Теперь встань вот так, и…"

    window hide

    stop ambience fadeout 0.5

    play sound sfx_door_squeak_light

    scene bg int_house_of_un_day
    show sl scared swim at left
    show un surprise pioneer far at right
    with dissolve

    play ambience ambience_int_cabin_day fadein 3

    play music music_list["forest_maiden"] fadein 10

    window show

    sl_v "Ой! Двери!"
    "Я не удержался, и потянул двери когтями, протиснулся в домик и тут же сел на месте от неожиданности."
    "Прямо посреди домика в живописной позе стояла почти голая Славя, а Лена сидела на кровати с альбомом и карандашом в руках."

    show un smile pioneer at right with dissolve

    un "Не волнуйся, это всего лишь котик. А двери я сейчас запру."

    show sl shy swim at left with dspr

    "Славя смущённо улыбнулась."
    sl "Я немного стесняюсь."

    show un shy pioneer at right with dspr

    un "Кого? {w}Меня?"

    show sl smile swim at left with dspr

    sl "Нет, мы же девочки. Вот его!"

    show un smile pioneer at right with dspr

    un "Да, Пират, он ведь мужчина. Да, котик?"

    play sound bkrr_sfx_list["meow5"]

    "Я мяукнул, потёрся о тумбочки и вообще старательно притворялся обычным котом."
    un "Славя, ты… Античные богини купальников не носили, даже таких красивых. Сними его, пожалуйста."

    show sl surprise swim at left with dspr

    sl "И плавки?"

    show un smile pioneer at right with dspr

    un "Плавки оставляй, я только до пояса буду рисовать."

    window hide

    show sl tender swim at left with dspr

    $ renpy.pause(1.0, hard=True)

    show sl normal swim at left with dspr

    window show

    "Славяна покосилась на меня, затем потянула вниз бретельку белого купальника."
    "Я остро осознал, что во все глаза таращусь на приоткрывающуюся славину грудь."

    show sl sad swim at left with dspr

    "Славя уже расстёгивала верх купальника, но снова посмотрела на меня и покачала головой."
    sl "Лен, прости, я не могу, когда он так смотрит. У меня такое чувство, что он всё понимает."

    show un shy pioneer at right with dspr

    un "Брось, это всего лишь кот."
    sl "Нет. Давай его прогоним, ладно?"

    show un normal pioneer at right with dspr

    un "Ладно. Вынесешь его? А то он мне рубашку обшерстит."

    show sl sad swim close at left with dissolve

    sl "Сейчас."

    window hide

    hide un
    hide sl
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Славя подхватила меня на руки, прижав к своей высокой, умопомрачительно упругой и красивой груди, и понесла к дверям. От удовольствия я даже не подумал сопротивляться, только мурлыкал."
    "Перед тем, как поставить меня на землю, Славяна тихо прошептала мне на ухо:"
    sl "В другой раз посмотришь!"

    window hide

    stop ambience fadeout 0.5

    stop music fadeout 7.5

    scene bg ext_house_of_un_day with dissolve

    play ambience ambience_camp_center_day fadein 3

    play sound sfx_close_door_1

    $ renpy.pause(1.0, hard=True)

    window show

    "Затем меня ласково, но твёрдо вытолкнули за двери. Ещё секунда – и щелчок шпингалета ознаменовал окончание короткого, но яркого пионерского стриптиза."

    window hide

    scene bg ext_houses_day with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    th "Может, оно и к лучшему? Я бы точно не хотел, чтобы Мику разглядывала голых парней."

    window hide

    scene bg ext_square_day with dissolve

    $ renpy.pause(1.0, hard=True)

    play music music_list["doomed_to_be_defeated"]

    scene bg ext_square_day:
        truecenter
        ease 0.5 zoom 1.25
        ease 0.25 zoom 1.2
    show sh rage pioneer close:
        center
        ease 0.5 zoom 1.25
        ease 0.25 zoom 1.2
    show red:
        alpha 0.0
        ease 0.1 alpha 0.3
        ease 0.1 alpha 0.0
    with vpunch

    play sound bkrr_sfx_list["hiss1"]

    window show

    "Ещё секунда – и меня ухватили за шиворот. Я зашипел, извернулся и увидел злобно горящие глаза Шурика."
    sh "Ага! Попался, вредитель! Кто мне полмастерской разнёс? Кто робота сломал? Кому…"

    play sound bkrr_sfx_list["hiss2"]

    "Я приготовился дорого продать свою жизнь, но из-за спины Шурика донеслось раздражённое:"

    show sh upset pioneer close at center
    show dv rage pioneer far at right behind sh
    with dissolve

    dv "Кому я сейчас нос набок сворочу, а, четырёхглазый? Ты чего наше клубное животное обижаешь?"

    window hide

    hide sh
    hide dv
    with dissolve

    $ renpy.pause(1.0, hard=True)

    scene bg ext_square_day:
        truecenter
        zoom 1.2
        ease 1.0 zoom 1.0
    with None

    stop music fadeout 5

    window show

    "Алиса отобрала меня у Шурика и опустила на землю."

    scene cg catday_dv_argue with dissolve

    sh "Алиса, ваше клубное животное мне кучу приборов переколотило. Что я завхозу в конце смены скажу?"
    dv "Да мне какая разница?"
    sh "Ну, нельзя же… вот так…"
    dv "Я не поняла?"
    sh "Ладно. Забирай."

    window hide

    scene bg ext_square_day with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я потёрся о ногу своей спасительницы и благодарно замурлыкал."
    "Алиса насмешливо посмотрела на меня, затем крикнула в спину Шурика:"

    show dv smile pioneer close at center with dissolve

    dv "Эй, Сашка, ты не дуйся, я сама его сейчас в речку кину! Пусть поплавает, раз вести себя не умеет!"

    window hide

    hide dv with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я ещё переваривал слова Алисы, когда она резко наклонилась и ухватила меня в охапку."
    th "Интересно, почему все девочки держат котов именно {b}так{/b}?"
    "Конечно, грудь Алисы заметно уступала славиной по размерам, но никак не по форме и упругости."
    th "Будь что будет. Хоть река."
    "Я обмяк на её руках и подобострастно замурлыкал."

    show dv grin pioneer close at center with dissolve

    dv "И не подлизывайся! Ты сегодня в залёте!"
    th "А зачем ты доверяешь коту в выборе продуктов?"
    "Когда она повернулась спиной к пляжу и зашагала в сторону домиков, я окончательно успокоился."

    show dv smile pioneer close at center with dspr

    dv "Наглая пушистая морда! Я тебя кормлю, пою и воспитываю, а ты!.."
    dv "Да не трясись ты так, не буду я тебя в воду кидать. Мне репутацию надо поддерживать. Понял?"

    play sound bkrr_sfx_list["meow6"]

    "Я согласно мяукнул и попытался кивнуть."

    show dv guilty pioneer close at center with dspr

    dv "Дожила. С котами разговариваю. Если Ульянка увидит… {w}Пошли ко мне, у нас поспишь. А то вожатая тебя в клубе искала, злая-презлая, теперь вот Шурик ищет. Что ж ты им всем сделал, очень интересно."
    "Я ткнулся ей в подбородок и замурлыкал."

    show dv normal pioneer close at center with dspr

    dv "Я тоже злюсь, так что не подлизывайся."

    window hide

    stop ambience fadeout 3

    scene bg int_house_of_dv_day with fade3

    play ambience ambience_int_cabin_day fadein 3

    window show

    dv "Уля, я тут кошака…"

    show dv surprise pioneer close at center with dissolve

    dv "А где эта мелкая? "

    show dv angry pioneer close at center with dspr

    dv "Опять двери не заперла!"

    window hide

    hide dv with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Она устроила меня на своей кровати, сама села рядом и принялась почёсывать и поглаживать, приговаривая что-то про лапки и царапки."

    show dv smile pioneer close at center with dissolve

    dv "Всё. Спи здесь и не хулигань. Понял?"
    "Я утвердительно мяукнул."
    dv "То-то же. А я на пляж! Может, взять тебя с собой и всё-таки окунуть пару раз?"

    play sound bkrr_sfx_list["meow5"]

    me "НЕТ!"

    show dv grin pioneer close at center with dspr

    dv "Ну, как знаешь. Ладно… буду переодеваться. Не подглядывай!"

    window hide

    $ renpy.pause(1.0, hard=True)

    show dv laugh pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    hide dv with dissolve

    window show

    "Она засмеялась, явно довольная своей шуткой."
    th "Интересно, что бы рыжая сказала, знай, кто сейчас скрывается за личиной клубного кота?"

    window hide

    show blink

    $ renpy.pause(2.5, hard=True)

    hide blink
    show unblink
    with None

    $ renpy.pause(1.5, hard=True)

    window show

    "Я прикрыл глаза и слушал дразнящее шуршание одежды, пока Алиса переодевалась для похода на пляж. {w}Наконец, не выдержав, я приоткрыл один глаз, но увидел только закрывающуюся дверь."

    window hide

    $ renpy.pause(0.5, hard=True)

    play sound sfx_close_door_1

    $ renpy.pause(1.0, hard=True)

    window show

    "Побродив по кровати, я устроился в тёплом пятне солнечного света и задремал."

    window hide

    stop ambience fadeout 3

    scene black with fade3

    $ renpy.pause(3.0, hard=True)

    scene bg int_house_of_dv_day
    show unblink
    with None

    play ambience ambience_int_cabin_day fadein 3

    play music music_list["i_want_to_play"] fadein 5

    $ renpy.pause(2.5, hard=True)

    window show

    "Меня разбудила странная возня."

    show us laugh2 pioneer at center behind unblink with dissolve

    us "Этой нет? Вот и хорошо. А то опять начнётся…"

    window hide

    hide us with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Ульяна забралась в Алискин шкафчик и принялась там рыться. Через пару минут она с победным восклицанием достала белый лифчик и быстро его надела. Естественно, он печально повис, так как заполнить его у мелкой пока было нечем."
    us "Угу. Значит, подложим сюда… {w}и сюда… {w}и вот сюда…"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Я с интересом наблюдал за её манипуляциями. Ульяна повернулась ко мне, продемонстрировав лифчик с набитыми тряпками чашечками, и поинтересовалась:"

    show us normal bra at center with dissolve

    us "Пират, мне нужно твоё мужское мнение!"

    play sound bkrr_sfx_list["meow3"]

    me "Мяу?"

    show us sad bra at center with dspr

    us "Если я вот так сделаю, будет нормально?"
    dv "Ни разу не нормально!"
    us "Ой…"

    window hide

    show us shy bra at right with ease

    show dv normal pioneer2 at left with easeinleft

    window show

    dv "Я тебе говорила не заниматься ерундой?"

    show us upset bra at right with dspr

    us "Говорила."
    dv "Я тебе говорила, чтобы ты моё бельё оставила в покое?"
    us "Говорила."

    show dv rage pioneer2 at left with dspr

    dv "Так чего ты дурью маешься?"

    show us sad bra at right with dspr

    us "Тебе не понять. У тебя они есть."

    show dv grin pioneer2 at left with dspr

    dv "И у тебя будут. {w}Со временем."

    show us dontlike bra at right with dspr

    us "С каким ещё временем? Одни танцы остались! Понимаешь, {b}одни{/b}!"

    show dv normal pioneer2 at left with dspr

    dv "Уля, вот ты представь: потанцуете вы с ним. {w}Представила?"

    show us normal bra at right with dspr

    us "Угу…"
    dv "Потом пойдёте прогуляться. Он тебя зажмёт где-нибудь у сосны."

    show us dontlike bra at right with dspr

    us "Он не такой!"

    show dv smile pioneer2 at left with dspr

    dv "Все они не такие. Вот. {w}Зажмёт, значит… Полезет трогать."

    show us calml bra at right with dspr

    us "НЕТ!!!"

    show dv angry pioneer2 at left with dspr

    "Алиса жёстко покачала головой."
    dv "Да!"

    show us sad bra at right with dspr

    us "Нет!"

    window hide

    show dv grin pioneer2 at left with dspr

    $ renpy.pause(0.5, hard=True)

    show dv smile pioneer2 at center with ease

    show us fear bra at right with dspr

    window show

    "Алиса быстро протянула руку и выхватила одну из тряпок, которые формировали кривоватую фальшивую грудь Ульяны."

    stop music fadeout 7.5

    show us shy bra at right with dspr

    dv "А твоя сиська — р-раз! — и превратится в кучу носков… НОСКОВ???"

    show dv shocked pioneer2 at center with dspr

    dv "Улька, ты набила мой лучший лифон носками?"

    show us upset bra at right with dspr

    us "Но они же чистые…"

    show dv angry pioneer2 at center with dspr

    dv "НЕ ВРИ МНЕ!!! Ты стиралась неделю назад в последний раз! Откуда у тебя чистые носки?"

    show us sad bra at right with dspr

    us "Ладно, ладно. Почти чистые. Не парься так."

    show dv smile pioneer2 at center with dspr

    "Алиса вздохнула и улыбнулась. От её улыбки температура в комнате сразу понизилась градусов на десять."
    dv "А я не парюсь."

    show dv grin pioneer2 at center with dspr

    dv "Это ты паришься, где достать нормальный стиральный порошок. И прямо после репетиции ты мне его постираешь. А если ещё раз полезешь в мои вещи, получишь по морде! По…"

    show us shy bra at right with dspr

    us "По наглой рыжей морде. Я помню."
    dv "Вот и умничка. Мы друг друга поняли?"
    us "Угу."

    show dv smile pioneer2 at left with ease

    "Алиса улыбнулась, на этот раз тепло, словно старшая сестра."
    dv "Не зацикливайся ты так. Всё вырастет. {w}Обязательно."

    show dv laugh pioneer2 at fleft with ease

    "Она показала подруге язык и мстительно добавила:"
    dv "Сантиметра на полтора."

    hide dv with easeoutleft

    "Ульяна проводила её взглядом, не сулившим ничего хорошего."

    show us smile bra at center with ease

    us "Вот змея."
    us "Ну, ничего! Мы ещё посмотрим, как ты через пару дней шутить будешь."

    window hide

    hide us with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Она грустно опустошила лифчик, бросила его на кровать и надела рубашку."

    show us smile pioneer close at center with dissolve

    us "Такие дела, Пиратик. Нервы, нервы. И в доме ничего сладкого."

    window hide

    $ renpy.pause(1.0, hard=True)

    show us normal pioneer close at center with dissolve

    window show

    "Ульяна задумчиво посмотрела на меня."
    us "Слушай, а ведь за твоё спасение повара тогда отсыпали столько конфет! {w}Ты ведь поможешь, правда?"

    show us smile pioneer close at center with dspr

    us "Не бойся, просто постой спокойно! Сейчас сбегаем к кухне, как раз к обеду начнёшь мяукать, и…"

    show us smile pioneer at center with dspr

    "Я подался назад. {w}Оказаться в вентиляции, как тогда, мне совершенно не хотелось."

    show us sad pioneer at center with dspr

    us "Ну, не убегай! А я тебе сосиску завтра отдам. Полчаса страха и всё!"

    play sound sfx_open_door_1

    "Дверь снова открылась."

    window hide

    show us normal pioneer at right with ease

    show dv normal pioneer2 at left with dissolve

    window show

    dv "Улька, хватит животное мучить. Идём репетировать!"

    show us upset pioneer at right with dspr

    us "Не хочу!"

    show dv normal pioneer2 at left with dspr

    dv "Мику печенье принесла."

    show dv smile pioneer2 at left
    show us surp1 pioneer at right
    with dspr

    dv "Но, раз не хочешь, тогда отдохни, мы без ленивых барабанщиц поиграем. Всё равно Сенька у медсестры завис, ритма не будет, так что чаи погоняем."
    us "Что ж ты сразу не сказала, что у вас ритм-секции не хватает? Уже бегу."

    show dv grin pioneer2 at left with dspr

    dv "Нет-нет. Отдыхай. Ты же не хочешь?"

    show us dontlike pioneer at right with dspr

    us "Алиса, не борзей! Хочу!"

    show dv smile pioneer2 at left with dspr

    dv "Вот и хорошо. Пошли, Мику заждалась!"

    window hide

    show us smile pioneer at right with dspr

    $ renpy.pause(1.0, hard=True)

    hide dv
    hide us
    with dissolve

    window show

    "Мику... {w}При мысли о ней моё кошачье сердце учащённо забилось. Я понял, как же соскучился по моему разговорчивому сокровищу."

    window hide

    stop ambience fadeout 0.5

    play sound sfx_close_door_1

    scene bg ext_house_of_dv_day with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show

    "Я проскочил между ногами Алисы и отправился в клуб."

    show dv surprise pioneer2:
        fright
        zoom 1.2
    show us surp1 pioneer:
        cright
        zoom 1.2
    with dissolve

    dv "Чего это с ним? Чуть с ног не сбил, как про Мику услышал."
    us "Может, кошка где-то гуляет? {w}Кто их знает."

    show us grin pioneer:
        cright
        zoom 1.2
    with dspr

    us "А конфет всё равно хочется."

    window hide

    stop ambience fadeout 3

    scene bg ext_music_club_day_bkrr at bkrr_moving_forward_far(5.0, 1.5) with fade3

    play ambience ambience_camp_center_day fadein 3

    $ renpy.pause(1.0, hard=True)

    scene bg ext_music_club_verandah_day_v5 with dissolve

    $ renpy.pause(1.0, hard=True)

    play music music_list["orchid"] fadein 5

    window show

    mi_v "И-и-и!!! ПОМОГИТЕ!!!"
    th "Мику в беде?"
    "Забыв обо всём, даже о том, что я сейчас в кошачьем теле, я бросился в клуб."
    th "Что? Что там могло случиться?"

    window hide

    stop ambience fadeout 0.5

    scene bg int_music_club_mattresses_day with dissolve

    window show

    "Я вбежал в комнату и осмотрелся."
    "Стаи страшилищ в поле зрения не оказалось. {w}Мику с ногами забралась на стул и испуганно смотрела куда-то в сторону ударной установки."

    show dv surprise pioneer2 at fleft
    show us surp2 pioneer at left
    with easeinleft

    us "Микуська, чего голосим, как на пожар?"
    dv "Что такое? Что случилось?"

    window hide

    stop music fadeout 2

    $ renpy.pause(1.0, hard=True)

    show mi shocked pioneer at fright with easeinright

    mi "МЫШЬ! Там мышь! Или крыса! Огромная и страшная!"

    window hide

    $ renpy.pause(1.0, hard=True)

    play music music_list["pile"]

    show dv shocked pioneer2 at fleft
    show us fear pioneer at left
    show mi shocked pioneer at fright
    with dissolve

    $ renpy.pause(1.0, hard=True)

    hide dv
    hide us
    with easeoutleft

    hide mi with easeoutright

    window show

    "Я ожидал, что девчонки её засмеют, но вместо этого они синхронно взвизгнули и тоже забрались на стулья."
    th "Это ещё что? Они мышей так боятся?"

    show us fear pioneer close at right with easeinright

    us "Алиска, сделай что-нибудь!"

    show dv shocked pioneer2 close at left with easeinleft

    dv "Сама делай!"

    show mi shocked pioneer close at center with easeinbottom

    mi "Девочки, ну придумайте что-нибудь, а то она кого-нибудь покусает, а это очень опасно."
    mi "Они ведь бешенство переносят. И ещё что-то такое. Я читала, только не помню, я ведь в журнале статью про музыку искала, а не про грызунов."

    show dv guilty pioneer2 close at left with dspr

    dv "Тихо! Девчата, не визжите, дайте подумать."

    show mi sad pioneer close at center
    show us sad pioneer close at right
    with dspr

    dv "Мику, она точно там? За улькиными барабанами?"
    mi "Да, точно. Во-о-он там."
    dv "Блин, Сенька не вовремя заболел. Он точно мышей не боится."

    stop music fadeout 5

    play ambience ambience_music_club_day fadein 3

    show us normal pioneer close at right with dspr

    us "Слушай… А у нас ведь кот есть. Даром, что ли, он наши харчи лопает? Пусть отрабатывает! Пират, поймай мыша!"

    show dv normal pioneer2 close at left with dspr

    dv "Ага. Ещё «апорт» скажи. Он же тупой. Ест да спит."

    play sound bkrr_sfx_list["meow6"]

    "Я обиженно мяукнул, демонстративно припал на полусогнутые лапы и двинулся к ударной установке. Три пары испуганных глаз провожали каждое моё движение."
    us "Пират, миленький, поймай её, ладно? Пожалуйста-пожалуйста!"

    show dv smile pioneer2 close at left with dspr

    dv "Тихо, не зови его, а то пойдёт к тебе об ноги тереться и эту мышь до утра не поймает."

    show mi dontlike pioneer close at center with dspr

    mi "Я не могу здесь до утра сидеть, мне ещё Семёна надо в изоляторе навестить!"

    show dv normal pioneer2 close at left with dspr

    dv "Кому что."

    show dv surprise pioneer2 close at left with dspr

    dv "Смотри, смотри, учуял!"

    window hide

    hide dv
    hide us
    hide mi
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я действительно слышал резкий запах какой-то зверушки. Прямо под педалью самого большого барабана сидел и испуганно смотрел на меня очаровательный маленький мышонок."
    th "Повезло тебе, серая шкурка, что я не кот, а то быть бы тебе поздним завтраком. Что же мне с тобой делать-то?"
    "Я втянул когти и лёгким шлепком вытолкнул мышонка из-под барабана. Тот жалобно пискнул и попытался вернуться назад. Наверное, совсем маленький и ничего не соображает от страха."
    th "Нет-нет-нет. Не пойдёт. Тебе не сюда."
    "Серией быстрых мягких шлепков я почти оттеснил несмышлёныша к дверям, не давая вернуться в угол. Ещё метр, и он окажется на улице. Если хоть немного мозгов есть, то уйдёт подальше, а если нет, то Пират завтра с аппетитом им закусит."
    "Девочки поняли мои действия по-своему."

    show dv angry pioneer2 at center with dissolve

    dv "Пират, не играйся с ним, ему же больно! Садюга усатая!"

    show us surp1 pioneer at right with dissolve

    us "Ой, какой хорошенький! Мику, это же не крыса!"

    show mi sad_smile pioneer at left with dissolve

    mi "И правда, но он показался очень большим."

    show us smile pioneer at right with dspr

    us "У страха глаза велики. Давайте его банкой накроем и выпустим?"

    show dv laugh pioneer2 at center with dspr

    dv "Действуй."

    show us shy pioneer at right with dspr

    us "Не-не-не. Я мышей боюсь! Даже маленьких!"

    window hide

    hide dv
    hide us
    hide mi
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я осторожно прижал мышонка лапой, чтобы не гоняться за ним по клубу, пока девчонки что-то придумают. {w}Тот дёрнулся и затих, только мелко и испуганно дышал."

    stop ambience fadeout 5

    play music music_list["revenga"]

    show dv shocked pioneer2 at center with dissolve

    dv "Ой-ой-ой, девочки, он его сейчас раздавит."
    dv "Пират, н-н-на!!!"

    window hide

    play sound sfx_bus_window_hit

    scene black
    show red:
        alpha 0.5
        ease 2.5 alpha 0.0
    show bkrr_bang:
        truecenter
        alpha 1.1
        zoom 1.1
        linear 2.5 alpha 0.0 zoom 0.9
    with flash

    stop music fadeout 5

    window show

    "Она сорвала с ноги босоножку и отточенным, метким движением кинула её в меня. {w}Импровизированный снаряд врезался мне точно между глаз. Кажется, из них полетели искры."
    "Мышонок вырвался и убежал в двери, а у меня потемнело в глазах и подкосились лапы."
    "Из темноты доносились голоса:"
    mi "Алиса, ну что ты наделала? Ему же больно!"
    dv "Ну простите, дура я! Я за мышонка испугалась. Он такой маленький, такой беззащитный, а эта рожа с ним игралась."
    us "Семён тебя убьёт. Он этого кота обожает. А ты его вырубила."
    us "Всё, придётся тебе неделю перед ним в купальнике ходить и выполнять все его приказы, а то ведь не простит."
    mi "Уля, сейчас стукну! У него вообще-то девушка есть!"
    dv "Точно!"

    window hide

    $ renpy.pause(1.0, hard=True)

    play music music_list["sparkles"] fadein 5

    window show

    "Я почувствовал, как меня подняли на руки. {w}Мягкие, нежные, очень знакомые пальцы принялись ощупывать мой лоб, а затем всё поплыло и исчезло."

    window hide

    $ renpy.pause(5.0, hard=True)

    stop music fadeout 3

    scene bg int_aidpost_day
    show unblink
    with None

    play ambience ambience_medstation_inside_day fadein 3

    $ renpy.pause(1.5, hard=True)

    show cs normal far at center behind unblink with dissolve

    window show

    cs "Что за делегация?"

    play music music_list["so_good_to_be_careless"] fadein 5

    show us smile pioneer at right behind unblink with dissolve

    us "Мы Семёна проведать!"
    cs "Ну, давайте, только быстро."

    window hide

    hide cs with dissolve

    show us smile pioneer at left with ease
    show dv smile pioneer2 at right
    show mi sad_smile pioneer at center
    with easeinright

    window show

    dv "Вот где наша басота косит от репетиций!"

    show dv grin pioneer2 at right with dspr

    dv "Девчат, вы гляньте на его ленивую наглую рожу! Сень, ты хочешь, чтобы я поверила, что ты больной?"
    me "Очень больной! Просто я рад всех вас видеть."

    show us grin pioneer at left with dspr

    us "Ага! Ладно, у нас с Алисой срочное дело, вы с Мику посидите, пообщайтесь. Мы пошли!"

    show dv surprise pioneer2 at right with dspr

    dv "Какое дело?"

    show us normal pioneer at left with dspr

    us "{b}Срочное!{/b} Пошли, пошли. По пути расскажу."
    dv "Но мы же только…"

    window hide

    hide us
    hide dv
    with easeoutright

    show mi normal pioneer at center with ease

    show mi normal pioneer:
        center
        sit_down
    show chair_c behind mi:
        center
        chair_move_sd
    with dspr

    window show

    "Мику присела рядом на стуле и взяла меня за руку."
    mi "Как ты?"
    me "Теперь – намного лучше. А вы как там без меня?"

    show mi smile pioneer at bkrr_sit_center with dspr

    mi "Лично я очень скучаю. А как остальные, я не знаю."
    me "А остальные меня не так интересуют. Чем вы занимались весь день? Репетировали? Что новенького вообще?"

    show mi sad_smile pioneer at bkrr_sit_center with dspr

    stop music fadeout 10

    mi "Ой, Сенечка, ты только не ругайся, мы тут…"

    window hide

    show mi upset pioneer at bkrr_sit_center with dspr

    $ renpy.pause(1.0, hard=True)

    show mi sad_smile pioneer at bkrr_sit_center with dspr

    window show

    mi "Пират у нас приболел. Ушибся сильно. Но ты не волнуйся, он будет в порядке."
    me "Жалко котейку. Что случилось-то?"

    show mi serious pioneer at bkrr_sit_center with dspr

    mi "Несчастный случай."
    "Всё-таки она совершенно не умеет врать. Её щёки порозовели, а глаза старательно смотрели в сторону."
    me "Да, да. Пришло бедное животное, кушать попросило, а вы в него тапками. {w}Как он? Жить-то будет?"

    show mi surprise pioneer at bkrr_sit_center with dspr

    "Мику подняла на меня удивлённый взгляд."
    mi "Нормально, только испугался немножко."

    show mi upset pioneer at bkrr_sit_center with dspr

    mi "Сеня, а мы про тапки ничего не рассказали. Девочки знают, что ты Пирата любишь, и боялись, что ты ругаться начнёшь."
    mi "А ну-ка, расскажи, откуда ты знаешь?"
    me "А он мне рассказал! Пришёл и на ухо нажаловался."

    show mi normal pioneer at bkrr_sit_center with dspr

    mi "Ну! Не сочиняй."
    mi "Я Алису и Ульяну заставила его нянчить до полного выздоровления. Признавайся, ты убегал и подглядывал за нами?"
    me "Нет. Честное слово, я здесь был."

    show mi upset pioneer at bkrr_sit_center with dspr

    mi "Тогда откуда?"

    stop ambience fadeout 5

    play music music_list["lightness"] fadein 7.5

    me "Милая, ты не поверишь. Мне такой сон приснился!"

    show mi serious pioneer at bkrr_sit_center with dspr

    mi "Сон? Какой сон?"
    me "Садись поудобнее, и я тебе сейчас всё расскажу…"

    window hide

    $ renpy.pause(1.0, hard=True)

    show mi smile pioneer at bkrr_sit_center with dspr

    scene black with Dissolve(5.0)

    stop music fadeout 5

    $ renpy.pause(5.0)

    $ renpy.movie_cutscene(bkrr_video_list["catday_ending"], delay = 25.0)

    scene black with None

    jump bkrr
