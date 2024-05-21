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
            "explanation": "(hi) (ra) (ga) (na)"
        },
        {
            "input": "arigatou",
            "answer": "ありがとう",
            "explanation": "(a) (ri) (ga) (to) (u)"
        },
        {
            "input": "ningyou",
            "answer": "にんぎょう",
            "explanation": "(ni) (n) [(gi) (small yo)] (u)"
        },
        {
            "input": "kakkoii",
            "answer": "かっこいい",
            "explanation": "(ka) [(small tsu) (ko)] (i) (i)"
        }
    ],
    "Extra": [
        {
            "input": "emoji",
            "answer": "えもじ",
            "explanation": "(e) (mo) (ji)"
        },
        {
            "input": "uun",
            "answer": "ううん",
            "explanation": "(u) (u) (n)"
        },
        {
            "input": "attakai",
            "answer": "あったかい",
            "explanation": "(a) [(small tsu) (ta)] (ka) (i)"
        },
    ]
}
