"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["hiragana"],
            "answer": "ひらがな",
            "explanation": "hiragana -> ひらがな"
        },
        {
            "input": ["arigatou"],
            "answer": "ありがとう",
            "explanation": "arigatou -> ありがとう"
        },
        {
            "input": ["ningyou"],
            "answer": "にんぎょう",
            "explanation": "ningyou -> にんぎょう"
        },
        {
            "input": ["kakkoii"],
            "answer": "かっこいい",
            "explanation": "kakkoii -> かっこいい"
        },
        {
            "input": ["ninja"],
            "answer": "にんじゃ",
            "explanation": "ninja -> にんじゃ"
        },
    ],
    "Extra": [
        {
            "input": ["emoji"],
            "answer": "えもじ",
            "explanation": "emoji -> えもじ"
        },
        {
            "input": ["uunn"],
            "answer": "ううん",
            "explanation": "uunn -> ううん"
        },
        {
            "input": ["attakai"],
            "answer": "あったかい",
            "explanation": "attakai -> あったかい"
        },
        {
            "input": ["matte"],
            "answer": "まって",
            "explanation": "matte -> まって"
        },
        {
            "input": ["matteiru"],
            "answer": "まっている",
            "explanation": "matteiru -> まっている"
        },
        {
            "input": ["happyou"],
            "answer": "はっぴょう",
            "explanation": "happyou -> はっぴょう"
        },
        {
            "input": ["kocchi"],
            "answer": "こっち",
            "explanation": "kocchi -> こっち"
        },
        {
            "input": ["poketto"],
            "answer": "ぽけっと",
            "explanation": "poketto -> ぽけっと"
        },
        {
            "input": ["yoissho"],
            "answer": "よいっしょ",
            "explanation": "yoissho -> よいっしょ"
        },
        {
            "input": ["beddo"],
            "answer": "べっど",
            "explanation": "beddo -> べっど"
        },
        {
            "input": ["shuppatsu"],
            "answer": "しゅっぱつ",
            "explanation": "shuppatsu -> しゅっぱつ"
        },
        {
            "input": ["nanminn"],
            "answer": "なんみん",
            "explanation": "nanminn -> なんみん"
        },
        {
            "input": ["nyann"],
            "answer": "にゃん",
            "explanation": "nyann -> にゃん"
        },
        {
            "input": ["amerika"],
            "answer": "あめりか",
            "explanation": "amerika -> あめりか"
        },
        {
            "input": ["sayonara"],
            "answer": "さよなら",
            "explanation": "sayonara -> さよなら"
        },
        {
            "input": ["sumimasenn"],
            "answer": "すみません",
            "explanation": "sumimasenn -> すみません"
        },
        {
            "input": ["attouteki"],
            "answer": "あっとうてき",
            "explanation": "attouteki -> あっとうてき"
        },
        {
            "input": ["chuugoku"],
            "answer": "ちゅうごく",
            "explanation": "chuugoku -> ちゅうごく"
        },

        # punctuation
        {
            "input": ["~nakya"],
            "answer": "~なきゃ",
            "explanation": "~nakya -> ~なきゃ"
        },
        {
            "input": ["damatte!"],
            "answer": "だまって!",
            "explanation": "damatte! -> だまって!"
        },
        {
            "input": ["nani?"],
            "answer": "なに?",
            "explanation": "nani? -> なに?"
        },
        {
            "input": ["tokorode..."],
            "answer": "ところで...",
            "explanation": "tokorode... -> ところで..."
        },
        {
            "input": ["maru."],
            "answer": "まる.",
            "explanation": "maru. -> まる."
        },
        {
            "input": ["2kaime"],
            "answer": "2かいめ",
            "explanation": "2kaime -> 2かいめ"
        },

        # cities / districts
        {
            "input": ["toukyou"],
            "answer": "とうきょう",
            "explanation": "toukyou -> とうきょう"
        },
        {
            "input": ["yokohama"],
            "answer": "よこはま",
            "explanation": "yokohama -> よこはま"
        },
        {
            "input": ["oosaka"],
            "answer": "おおさか",
            "explanation": "oosaka -> おおさか"
        },
        {
            "input": ["nagoya"],
            "answer": "なごや",
            "explanation": "nagoya -> なごや"
        },
        {
            "input": ["sapporo"],
            "answer": "さっぽろ",
            "explanation": "sapporo -> さっぽろ"
        },
        {
            "input": ["fukuoka"],
            "answer": "ふくおか",
            "explanation": "fukuoka -> ふくおか"
        },
        {
            "input": ["kawasaki"],
            "answer": "かわさき",
            "explanation": "kawasaki -> かわさき"
        },
        {
            "input": ["koube"],
            "answer": "こうべ",
            "explanation": "koube -> こうべ"
        },
        {
            "input": ["kyouto"],
            "answer": "きょうと",
            "explanation": "kyouto -> きょうと"
        },
        {
            "input": ["saitama"],
            "answer": "さいたま",
            "explanation": "saitama -> さいたま"
        },
        {
            "input": ["hiroshima"],
            "answer": "ひろしま",
            "explanation": "hiroshima -> ひろしま"
        },
        {
            "input": ["ginza"],
            "answer": "ぎんざ",
            "explanation": "ginza -> ぎんざ"
        },
        {
            "input": ["shibuya"],
            "answer": "しぶや",
            "explanation": "shibuya -> しぶや"
        },
        {
            "input": ["asakusa"],
            "answer": "あさくさ",
            "explanation": "asakusa -> あさくさ"
        },
        {
            "input": ["shinjuku"],
            "answer": "しんじゅく",
            "explanation": "shinjuku -> しんじゅく"
        },
        {
            "input": ["harajuku"],
            "answer": "はらじゅく",
            "explanation": "harajuku -> はらじゅく"
        },
        {
            "input": ["akihabara"],
            "answer": "あきはばら",
            "explanation": "akihabara -> あきはばら"
        },
        {
            "input": ["hanbun"],
            "answer": "はんぶn",
            "explanation": "hanbun -> はんぶn"
        },
        {
            "input": ["gyuunyuu"],
            "answer": "ぎゅうんゆう",
            "explanation": "gyuunyuu -> ぎゅうんゆう"
        },
        {
            "input": ["fukuzatsu"],
            "answer": "ふくざつ",
            "explanation": "fukuzatsu -> ふくざつ"
        },
    ]
}
