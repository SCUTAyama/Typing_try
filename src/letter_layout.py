#平假名主布局
class Keyboard_Layout:
    BUTTON_LAYOUT_HINAGANA_SEION = [
        'あ','い','う','え','お',
        'か','き','く','け','こ',
        'さ','し','す','せ','そ',
        'た','ち','つ','て','と',
        'な','に','ぬ','ね','の',
        'は','ひ','ふ','へ','ほ',
        'ま','み','む','め','も',
        'や','','ゆ','','よ',
        'ら','り','る','れ','ろ',
        'わ','','','','お',
        'ん','','','','',
    ]
    BUTTON_LAYOUT_KATAKANA_SEION = [
        'ア', 'イ', 'ウ', 'エ', 'オ',
        'カ', 'キ', 'ク', 'ケ', 'コ',
        'サ', 'シ', 'ス', 'セ', 'ソ',
        'タ', 'チ', 'ツ', 'テ', 'ト',
        'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
        'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
        'マ', 'ミ', 'ム', 'メ', 'モ',
        'ヤ', 'ユ', 'ヨ',
        'ラ', 'リ', 'ル', 'レ', 'ロ',
        'ワ', 'オ',
        'ン',
    ]

    #（半）浊音布局
    BUTTON_LAYOUT_HINAGANA_DAKUON = [
        'が','ぎ','ぐ','げ','ご',
        'ざ','じ','ず','ぜ','ぞ',
        'だ','ぢ','づ','で','ど',
        'ば','び','ぶ','べ','ぼ'
    ]
    BUTTON_LAYOUT_HINAGANA_HANDAKUON = [
        'ぱ','ぴ','ぷ','ぺ','ぽ'
    ]
    BUTTON_LAYOUT_KATAKANA_DAKUON = [
        'ガ', 'ギ', 'グ', 'ゲ', 'ゴ',
        'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ',
        'ダ', 'ヂ', 'ヅ', 'デ', 'ド',
        'バ', 'ビ', 'ブ', 'ベ', 'ボ'
    ]
    BUTTON_LAYOUT_KATAKANA_HANDAKUON = [
        'パ', 'ピ', 'プ', 'ペ', 'ポ'
    ]

    #小键
    BUTTON_LAYOUT_HINAGANA_SMALL = [
        'ぁ', 'ぃ', 'ぅ', 'ぇ', 'ぉ',
        'っ',
        'ゃ', 'ゅ', 'ょ',
    ]
    BUTTON_LAYOUT_KATAKANA_SMALL = [
        'ァ', 'ィ', 'ゥ', 'ェ', 'ォ',
        'ッ',
        'ャ', 'ュ', 'ョ',
    ]

    #特殊键
    BUTTON_LAYOUT_SPECIAL = [
        'ー', #延音符
    ]

    @property
    def seion_hinagana(self):
        return self.BUTTON_LAYOUT_HINAGANA_SEION

    @property
    def seion_katakana(self):
        return self.BUTTON_LAYOUT_KATAKANA_SEION

    @property
    def dakuon_hinagana(self):
        return self.BUTTON_LAYOUT_HINAGANA_DAKUON

    @property
    def dakuon_katakana(self):
        return self.BUTTON_LAYOUT_KATAKANA_DAKUON

    @property
    def handakuon_hinagana(self):
        return self.BUTTON_LAYOUT_HINAGANA_HANDAKUON

    @property
    def handakuon_katakana(self):
        return self.BUTTON_LAYOUT_KATAKANA_HANDAKUON

    @property
    def small_hinagana(self):
        return self.BUTTON_LAYOUT_HINAGANA_SMALL

    @property
    def small_katakana(self):
        return self.BUTTON_LAYOUT_KATAKANA_SMALL

    @property
    def special(self):
        return self.BUTTON_LAYOUT_SPECIAL