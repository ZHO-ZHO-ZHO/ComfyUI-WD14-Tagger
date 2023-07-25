from .pysssss import init

if init(check_imports=["onnxruntime"]):
    NODE_CLASS_MAPPINGS = {
        "WD14Tagger|pysssss": WD14Tagger,
    }
    NODE_DISPLAY_NAME_MAPPINGS = {
        "WD14Tagger|pysssss": "WD14 Tagger 🐍",
    }
