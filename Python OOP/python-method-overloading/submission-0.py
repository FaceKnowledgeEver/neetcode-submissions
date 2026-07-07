class TextProcessor:
    def format_text (self, *args: str) -> str:
        res = ""
        if len(args) == 1:
            res = args[0]
            return res.upper()
        else:
            for arg in args:
                res += arg
            return res
# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
