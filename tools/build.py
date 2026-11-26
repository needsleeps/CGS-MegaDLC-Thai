"""Build mod/mod.json from translation/megadlc_th.json.

Usage: python tools/build.py [LOCALE] [LANGUAGE_NAME]

CGS Mega DLC shows its theme names, review lines, events, engine and store features through the
game's translation lookup, using the English text itself as the key. This mod supplies Thai for
those keys, both for the "ไทย (NeedSleep)" language added by the base Thai mod (LOCALE, default
"tt") and for the game's built-in Thai ("th"). Keys longer than 128 characters are rejected by the
game's mod schema, so those lines stay in translation/not_shipped_long_keys.json and are not built.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCALE = sys.argv[1] if len(sys.argv) > 1 else "tt"
NAME = sys.argv[2] if len(sys.argv) > 2 else "ไทย (NeedSleep)"

messages = json.load(open(os.path.join(ROOT, "translation", "megadlc_th.json"), encoding="utf-8"))
too_long = [k for k in messages if len(k) > 128]
if too_long:
    sys.exit("keys longer than 128 characters cannot be shipped: %r" % too_long[:3])
mod = {"translation": {"add": [
    {"name": NAME, "locale": LOCALE, "messages": messages},
    {"name": "ไทย", "locale": "th", "messages": messages},
]}}
out = os.path.join(ROOT, "mod", "mod.json")
with open(out, "w", encoding="utf-8", newline="\n") as f:
    json.dump(mod, f, ensure_ascii=False, indent=2)
    f.write("\n")
print("wrote", out, "| messages:", len(messages), "| locales:", LOCALE, "+ th")
