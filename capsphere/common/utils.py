# from dataclasses import fields
#
#
# def to_snake_case(text: str) -> str:
#     if text.isupper():
#         return text
#     else:
#         return ''.join(['_' + c.lower() if c.isupper() else c for c in text]).lstrip('_')
#
#
# def dataclass_to_dict(obj):
#     return {to_snake_case(f.name): getattr(obj, f.name) for f in fields(obj)}
