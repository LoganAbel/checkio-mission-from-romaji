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
            "input": "hiragana",
            "answer": "ひらがな",
            "explanation": ""
        },
        {
            "input": "arigatou",
            "answer": "ありがとう",
            "explanation": ""
        },
        {
            "input": "ningyou",
            "answer": "にんぎょう",
            "explanation": "gyo -> gi ~yo"
        },
        {
            "input": "kakkoii",
            "answer": "かっこいい",
            "explanation": "kko -> x2 ko"
        },
        {
            "input": "ninja",
            "answer": "にんじゃ",
            "explanation": "ja -> ji ~ya"
        },
    ],
    "Extra": [
        {
            "input": "emoji",
            "answer": "えもじ",
            "explanation": ""
        },
        {
            "input": "uun",
            "answer": "ううん",
            "explanation": ""
        },
        {
            "input": "attakai",
            "answer": "あったかい",
            "explanation": "tta -> x2 ta"
        },
        {
            "input": "matte",
            "answer": "まって",
            "explanation": "tte -> x2 te"
        },
        {
            "input": "matteiru",
            "answer": "まっている",
            "explanation": "tte -> x2 te"
        },
        {
            "input": "happyou",
            "answer": "はっぴょう",
            "explanation": "ppyo -> x2 pi ~yo"
        },
        {
            "input": "kocchi",
            "answer": "こっち",
            "explanation": "ppyo -> x2 pi ~yo"
        },
        {
            "input": "poketto",
            "answer": "ぽけっと",
            "explanation": "tto -> x2 to"
        },
        {
            "input": "yoissho",
            "answer": "よいっしょ",
            "explanation": "ssho -> x2 shi ~yo"
        },
        {
            "input": "beddo",
            "answer": "べっど",
            "explanation": "ddo -> x2 do"
        },
        {
            "input": "shuppatsu",
            "answer": "しゅっぱつ",
            "explanation": "shu -> shi ~yu, ppa -> x2 pa"
        },
        {
            "input": "nanminn",
            "answer": "なんみん",
            "explanation": "nmi -> nn mi"
        },
    ]
}
