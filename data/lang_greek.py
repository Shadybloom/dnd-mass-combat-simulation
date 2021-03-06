#!/usr/bin/env python
# -*- coding':' utf-8 -*-

# https://thoughtcatalog.com/holly-riordan/2018/05/ancient-greek-names/
dict_words = {
    'warrior':'achilles',
    'protector':'aegeus',
    'praising':'aeneas',
    'shame':'aeschylus',
    'good hearted':'agafya',
    'resolute':'agammemnon',
    'love and affection':'agape',
    'good hearted':'agata',
    'good hearted':'agatha',
    'good hearted':'agda',
    'sacred, chaste':'aggie',
    'sacred, chaste':'agnes',
    'sacred, chaste':'agneta',
    'sacred, chaste':'agnete',
    'sacred, chaste':'agnetha',
    'sacred, chaste':'agnieszka',
    'good hearted':'agot',
    'good hearted':'agota',
    'good hearted':'agueda',
    'torch of light':'aileen',
    'manly':'aindrea',
    'powerful eagle':'ajax',
    'defender of the people':'alastair',
    'defender of man':'ale',
    'defending men':'alec',
    'ceaseless':'alecta',
    'ceaseless':'alecto',
    'defender of man':'aleixo',
    'protector of humanity':'alejandra',
    'defender of man':'alejandro',
    'defender of man':'aleksander',
    'defender of man':'aleksanteri',
    'torch of light':'alena',
    'defender of man':'ales',
    'protector of humanity':'alessa',
    'protector of humanity':'alessandra',
    'protector of humanity':'alessandro',
    'truthful':'aleta',
    'truthful':'alethea',
    'protector of humanity':'alex',
    'protector of humanity':'alexa',
    'defender of man':'alexander',
    'protector of humanity':'alexandra',
    'helper':'alexis',
    'helper':'alexius',
    'lord':'anaxagoras',
    'to shout':'bakchos',
    'bringer of victory':'berenike',
    'life':'bion',
    'the east':'cadmus',
    'to raise up':'caiaphas',
    'most beautiful':'calisto',
    'gift of beauty':'callidora',
    'beauty born':'calligenia',
    'most beautiful':'callisto',
    'a swallow bird':'celandine',
    'happiness':'chara',
    'shining happiness':'charalampos',
    'grace, kindness':'chariton',
    'fierce brightness':'charon',
    'green':'chloris',
    'golden flower':'chrysanthe',
    'golden':'chryseis',
    'sky blue':'cyanea',
    'hearkening':'cymone',
    'calf':'damali',
    'calf':'damalis',
    'calf':'damaris',
    'glory of the people':'damokles',
    'to tame':'damon',
    'parched':'danae',
    'wealthy':'dareia',
    'fear, terror':'deimos',
    'of earth':'demeter',
    'earth mother':'demetra',
    'pledge, vow':'desma',
    'mistress':'despoina',
    'mistress':'despoine',
    'g0d flower':'diantha',
    'god flower':'dianthe',
    'the goddess':'diona',
    'the goddess':'dione',
    'gazelle':'dorcia',
    'gift':'dorus',
    'dragon':'drakon',
    'sound':'echo',
    'well spoken':'efimia',
    'joy, mirth':'efrosyni',
    'flourishing':'efthalia',
    'the ready comer':'eileithyia',
    'peace':'eirene',
    'the lord is my god':'elias',
    'the liberator':'eleftheria',
    'bright, shining':'elektra',
    'torch':'elene',
    'torch':'eleni',
    'god is my oath':'elisavet',
    'wanderer':'elissa',
    'hope':'elpida',
    'hope':'elpis',
    'horror':'enyo',
    'dawn':'eos',
    'lovely':'erato',
    'work power':'erika',
    'strife':'eris',
    'good and holy':'euadne',
    'to seem well':'eudokia',
    'good gift':'eudora',
    'good glory':'eudoxia',
    'well born':'eugenia',
    'melody':'eumelia',
    'good victory':'eunike',
    'well spoken':'eupheme',
    'joy, mirth':'euphrosyne',
    'good action':'eupraxia',
    'wide, violent force':'eurybia',
    'wide justice':'eurydike',
    'giver of pleasure':'euterpe',
    'well blooming':'euthalia',
    'versatile':'eutropia',
    'well born':'evgenia',
    'light':'fotios',
    'light':'fotis',
    'self-controlled':'frona',
    'earth':'gaia',
    'noble':'gennadios',
    'old age':'gerasimos',
    'watchful':'gregorios',
    'sweet':'glykeria',
    'murderer':'gorgophone',
    'bloody':'haemon',
    'unseen':'haides',
    'kingfisher':'halkyone',
    'harmony':'harmonia',
    'young':'hebe',
    'far off':'hecuba',
    'far off':'hekate',
    'ascend':'heli',
    'sun':'helios',
    'of the earth':'hermes',
    'of the earth':'hermia',
    'of the earth':'hermione',
    'hero':'hero',
    'hero given':'herodotos',
    'fireside':'hestia',
    'to send song':'hesiod',
    'joyful, happy':'hilarion',
    'horse power':'hippokrates',
    'horse freer':'hippolyte',
    'hostage':'homer',
    'the distant one':'horus',
    'healthy':'hyginos',
    'supreme':'hypatios',
    'supreme':'hypatia',
    'violent flower':'iantha',
    'violent flower':'ianthe',
    'god is gracious':'ioanna',
    'to heal':'iason',
    'red':'iduma',
    'god is salvation':'iesos',
    'follower':'ikaros',
    'god is gracious':'ioannes',
    'violet':'iola',
    'violet':'iole',
    'strong born':'iphigenia',
    'rainbow':'iris',
    'equal power':'isokrates',
    'dove':'jonas',
    'he who is praised':'judas',
    'he who is praised':'jude',
    'the east':'kadmos',
    'beauty':'kallias',
    'beautiful voice':'kalliope',
    'most beautiful':'kallisto',
    'cover, conceal':'kalypso',
    'fruit':'karpos',
    'beaver':'kastor',
    'head':'kephalos',
    'gardener':'kepheus',
    'demon of the pit':'kerberos',
    'anointed':'khristos',
    'glory':'kleio',
    'glory':'kleitos',
    'glory of the father':'kleopatra',
    'spinner':'klotho',
    'praiseworthy might':'klymene',
    'famous':'klytie',
    'maiden':'kore',
    'maiden':'korinna',
    'beauty, order':'kosmos',
    'horn':'kronos',
    'of the lord':'kyriake',
    'apportioner':'lachesis',
    'my god has helped':'lazarus',
    'lion man':'leandros',
    'woman':'leda',
    'liberator':'lefteris',
    'the hidden one':'leto',
    'shrill voice':'ligeia',
    'wolf work':'lykourgos',
    'freedom fighter':'lysimachos',
    'the tall one':'macedon',
    'mother':'maeja',
    'mother':'maia',
    'blessed':'makarios',
    'causing to forget':'manasses',
    'pearl':'margarites',
    'gift of god':'mathias',
    'cunning':'medeia',
    'guardian':'medousa',
    'to grudge':'megaira',
    'dark':'melaina',
    'dark flower':'melantha',
    'honey':'melina',
    'honey bee':'melita',
    'choir':'melpomene',
    'spirit':'mentor',
    'method':'methodios',
    'red earth':'miltiades',
    'defender':'minta',
    'memory':'mneme',
    'shape':'morpheus',
    'myrrh':'myron',
    'numbness, sleep':'narkissa',
    'resurrection':'natasa',
    'retribution':'nemesis',
    'cloudy':'nephele',
    'lady of the house':'nephthys',
    'water':'nereus',
    'homecoming':'nestor',
    'victory':'nike',
    'bearer of victory':'nikephoros',
    'relating to the law':'nomiki',
    'night':'nyx',
    'sore feet':'oedipus',
    'wine':'oinone',
    'ocean':'okeanos',
    'to hate':'olysseus',
    'beneficial':'onesimos',
    'help':'ophelos',
    'mountain born':'origen',
    'darkness of night':'orpheus',
    'to hate':'oulixes',
    'heavenly':'ourania',
    'the heavens':'ouranos',
    'healer':'paeon',
    'wager':'paris',
    'to wield a weapon':'pallas',
    'friend of all':'pamphilos',
    'all gift':'pandora',
    'all holy':'panos',
    'panther':'pantheras',
    'preparation':'paraskeve',
    'virgin':'parthenia',
    'virgin voice':'parthenope',
    'small':'pavlos',
    'the sea':'pelagios',
    'weaver of cunning':'penelope',
    'person slayer':'persephone',
    'persian woman':'persis',
    'bright':'phaidra',
    'bright':'phaidros',
    'to love':'phile',
    'affectionate':'philemon',
    'sweet singer':'philomena',
    'light':'photine',
    'foliage':'phyllidos',
    'foliage':'phyllis',
    'broad, flat':'platon',
    'sweet':'polydeuces',
    'hospitable':'polyxene',
    'distribution lord':'poseidon',
    'animated spirit, soul':'psyche',
    'aggressive':'ptolema',
    'flame like':'pyrros',
    'menstruation':'rhea',
    'rose':'rhoda',
    'dawn':'roxane',
    'saphire':'sappho',
    'princess':'sara',
    'moon':'selene',
    'of the earth':'semele',
    'dazzle':'sethos',
    'knowledge':'smeme',
    'wisdom':'sofia',
    'wisdom':'solon',
    'clever':'sophos',
    'self-controlled':'sophronia',
    'safe army':'sostrate',
    'salvation':'sotiria',
    'lily':'sousanna',
    'spirit':'spyridoula',
    'spirit':'spyro',
    'stop':'stamatia',
    'pillar':'stelios',
    'army':'straton',
    'common fate':'syntyche',
    'all holy':'takis',
    'serpent lady':'tanis',
    'gift of god':'tedora',
    'support':'telamon',
    'liberator':'teris',
    'enjoying the dance':'terpsichore',
    'bandage':'thais',
    'flourishing':'thalia',
    'blossom':'thales',
    'death':'than',
    'immortal':'thanos',
    'glory of god':'thecla',
    'glory of god':'thekla',
    'law':'themis',
    'servant':'therapon',
    'hunter':'theron',
    'he who balances':'thoth',
    'honor':'timaios',
    'honor':'timo',
    'avenging murder':'tisiphone',
    'white clay, white earth':'titos',
    'god is good':'tobias',
    'delicate, soft':'tryphaina',
    'delicate, soft':'tryphosa',
    'hitting the mark':'tychon',
    'god is my light':'urias',
    'good tidings':'usiris',
    'king':'vasilis',
    'king, queen':'vasiliki',
    'yellow':'xanthe',
    'yellow':'xanthia',
    'yellow':'xanthippe',
    'yellow horse':'xanthippos',
    'stranger':'xene',
    'strange voice':'xenophon',
    'ruler over heroes':'xerxes',
    'god is gracious':'yanni',
    'farmer':'yorgos',
    'god has remembered':'zacharias',
    'god has given':'zebedee',
    'life':'zoe',
    'belt':'zona',
    'west wind':'zephyr',
    'glowing':'zopyros',
    'survivor':'zosime',
    'full of life ':'zotikos',
    }
