from cmp.pycompiler import Symbol, Epsilon, Sentence, Production, Grammar, Item
from cmp.grammartools import Action
from cmp.automata import State

import zlib, base64

Html = base64.b64decode(b'PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KPCFET0NUWVBFIGh0bWwgUFVCTElDICItLy9XM0MvL0RURCBYSFRNTCAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvVFIveGh0bWwxMS9EVEQveGh0bWwxMS5kdGQiPgo8aHRtbCB4bWw6bGFuZz0iZW4iIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj4KICA8aGVhZD4KICAgIDx0aXRsZT5SRVNVTFRBRE9TPC90aXRsZT4KICAgIDxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+CiAgICAgIGJvZHkKICAgICAgewogICAgICAgIGJhY2tncm91bmQ6IHJnYmEoMjU2LCAyNTYsIDI1NiwgMC4wKTsKICAgICAgICAvKiBiYWNrZ3JvdW5kLWltYWdlOiB1cmwoIi4vaW1hZ2VzL2ZlbHQucG5nIik7ICovCiAgICAgICAgLyogZGlzcGxheTogaW5saW5lLWJsb2NrOyAqLwogICAgICB9CiAgICAgIGRpdi5sZXZlbDFEaXYKICAgICAgewogICAgICAgIGJvcmRlci1yYWRpdXM6IDVweDsKICAgICAgICBib3JkZXI6IHRoaW4gc29saWQgI0FEQURDOTsKICAgICAgICBwYWRkaW5nOiA4cHQ7CiAgICAgICAgbWFyZ2luOiA4cHQ7CiAgICAgIH0KICAgICAgZGl2LmxldmVsMkRpdgogICAgICB7CiAgICAgICAgYm9yZGVyLXJhZGl1czogNXB4OwogICAgICAgIGJvcmRlcjogdGhpbiBzb2xpZCAjQURBREM5OwogICAgICAgIHBhZGRpbmc6IDhwdDsKICAgICAgICBtYXJnaW46IDhwdDsKICAgICAgfQogICAgICBkaXYuY29udGFpbmVyRGl2CiAgICAgIHsKICAgICAgICBvdmVyZmxvdy14OiBhdXRvOwogICAgICB9CiAgICAgIGRpdi5ob3Jpem9udGFsCiAgICAgIHsKICAgICAgICBkaXNwbGF5OiBmbGV4OwogICAgICB9CiAgICAgIGgxCiAgICAgIHsKICAgICAgICBib3JkZXItcmFkaXVzOiA1cHg7CiAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogdGVhbDsKICAgICAgICBjb2xvcjogI0ZGRkZGRjsKICAgICAgICBwYWRkaW5nOiA0cHQ7CiAgICAgICAgbWFyZ2luOiAwcHQ7CiAgICAgIH0KICAgICAgaDIKICAgICAgewogICAgICAgIGJvcmRlci1yYWRpdXM6IDVweDsKICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiB0b21hdG87CiAgICAgICAgY29sb3I6ICNGRkZGRkY7CiAgICAgICAgcGFkZGluZzogNHB0OwogICAgICAgIG1hcmdpbjogMHB0OwogICAgICB9CiAgICAgIGgzLmVycm9yCiAgICAgIHsKICAgICAgICBjb2xvcjogcmVkCiAgICAgIH0KICAgICAgaDMuZ29vZAogICAgICB7CiAgICAgICAgY29sb3I6IGdyZWVuCiAgICAgIH0KICAgICAgcC5pdGVtQ29sbGVjdGlvbgogICAgICB7CiAgICAgICAgd2hpdGUtc3BhY2U6IG5vd3JhcDsKICAgICAgICBtYXJnaW46IDA7CiAgICAgICAgcGFkZGluZzogMDsKICAgICAgfQogICAgICB0YWJsZQogICAgICB7CiAgICAgICAgYm9yZGVyLWNvbGxhcHNlOiBjb2xsYXBzZTsKICAgICAgICBwYWRkaW5nOiA0cHQ7CiAgICAgICAgbWFyZ2luOiA0cHQ7CiAgICAgIH0KICAgICAgdGQKICAgICAgewogICAgICAgIG1hcmdpbjogMHB4OwogICAgICAgIGJvcmRlcjogdGhpbiBzb2xpZCAjMDAwMDAwOwogICAgICAgIHRleHQtYWxpZ246IGNlbnRlcjsKICAgICAgICBwYWRkaW5nOiA0cHQ7CiAgICAgIH0KICAgICAgdGQuZXJyb3JDZWxsCiAgICAgIHsKICAgICAgICBtYXJnaW46IDBweDsKICAgICAgICBib3JkZXI6IHRoaW4gc29saWQgIzAwMDAwMDsKICAgICAgICB0ZXh0LWFsaWduOiBjZW50ZXI7CiAgICAgICAgcGFkZGluZzogNHB0OwogICAgICAgIGJhY2tncm91bmQtY29sb3I6IHJnYigxNTAsIDEwMCwgMTAwKTsKICAgICAgfQogICAgICB0aAogICAgICB7CiAgICAgICAgbWFyZ2luOiAwcHg7CiAgICAgICAgYm9yZGVyOiB0aGluIHNvbGlkICMwMDAwMDA7CiAgICAgICAgZm9udC13ZWlnaHQ6IGJvbGQ7CiAgICAgICAgdGV4dC1hbGlnbjogY2VudGVyOwogICAgICAgIHBhZGRpbmc6IDRwdDsKICAgICAgICBiYWNrZ3JvdW5kLWNvbG9yOiAjREREREREOwogICAgICB9CiAgICAgIHVsCiAgICAgIHsKICAgICAgICBsaXN0LXN0eWxlLXR5cGU6IG5vbmU7CiAgICAgICAgcGFkZGluZzogNnB0OwogICAgICAgIG1hcmdpbjogMHB0OwogICAgICB9CiAgICAgIGgzCiAgICAgIHsKICAgICAgICBwYWRkaW5nOiA0cHQ7CiAgICAgICAgbWFyZ2luOiAwcHQ7CiAgICAgIH0KICAgICAgLmdyYW1tYXJTeW1ib2wKICAgICAgewogICAgICAgIGZvbnQtZmFtaWx5OiAiQ291cmllciBOZXciICwgQ291cmllciwgbW9ub3NwYWNlOwogICAgICAgIGNvbG9yOiAjMDAwMDY2OwogICAgICAgIGZvbnQtd2VpZ2h0OiBib2xkOwogICAgICB9CiAgICAgIC5ncmFtbWFyU3ltYm9sU3BlY2lhbCwgLmdyYW1tYXJFcHNpbG9uCiAgICAgIHsKICAgICAgICBmb250LWZhbWlseTogIkNvdXJpZXIgTmV3IiAsIENvdXJpZXIsIG1vbm9zcGFjZTsKICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICBmb250LXN0eWxlOiBpdGFsaWM7CiAgICAgICAgY29sb3I6ICMwMDAwNjY7CiAgICAgIH0KICAgICAgLmdyYW1tYXJEb3QKICAgICAgewogICAgICAgIGZvbnQtZmFtaWx5OiAiQ291cmllciBOZXciICwgQ291cmllciwgbW9ub3NwYWNlOwogICAgICAgIGNvbG9yOiAjMDAwMDAwOwogICAgICB9CiAgICAgIC5ncmFtbWFyQXJyb3cKICAgICAgewogICAgICAgIGZvbnQtZmFtaWx5OiAiVGltZXMgTmV3IFJvbWFuIiAsIFRpbWVzLCBzZXJpZjsKICAgICAgICBjb2xvcjogIzAwMDAwMDsKICAgICAgICBmb250LXdlaWdodDogYm9sZDsKICAgICAgICBmb250LXNpemU6IGxhcmdlcjsKICAgICAgfQogICAgICAuZ3JhbW1hck9yLCAuZ3JhbW1hckNvbW1hCiAgICAgIHsKICAgICAgICBmb250LWZhbWlseTogIlRpbWVzIE5ldyBSb21hbiIgLCBUaW1lcywgc2VyaWY7CiAgICAgICAgY29sb3I6ICMwMDAwMDA7CiAgICAgICAgZm9udC13ZWlnaHQ6IGJvbGQ7CiAgICAgICAgZm9udC1zaXplOiBsYXJnZXI7CiAgICAgIH0KICAgICAgLmhlYWRlckZvb3RlckRpdgogICAgICB7CiAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogI0M4QzhDODsKICAgICAgICBwYWRkaW5nOiAycHQ7CiAgICAgIH0KICAgICAgaDQKICAgICAgewogICAgICAgIHBhZGRpbmc6IDRwdDsKICAgICAgICBtYXJnaW46IDBwdDsKICAgICAgfQogICAgICB0ZC5zZXBhcmF0b3JUYWJsZUNlbGwKICAgICAgewogICAgICAgIHBhZGRpbmc6IDFweDsKICAgICAgICBtYXJnaW46IDFweDsKICAgICAgICBib3JkZXI6IHRoaW4gc29saWQgIzAwMDAwMDsKICAgICAgfQogICAgICB0aC5zZXBhcmF0b3JUYWJsZUNlbGwKICAgICAgewogICAgICAgIHBhZGRpbmc6IDFweDsKICAgICAgICBtYXJnaW46IDFweDsKICAgICAgICBib3JkZXI6IHRoaW4gc29saWQgIzAwMDAwMDsKICAgICAgfQogICAgPC9zdHlsZT4KICA8L2hlYWQ+CiAgPGJvZHk+CiAgICA8ZGl2IGNsYXNzPSJsZXZlbDFEaXYiPgogICAgICA8aDE+R3JhbSZhYWN1dGU7dGljYTwvaDE+CiAgICAgIDxkaXY+CiAgICAgICAgJXMKICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxldmVsMkRpdiI+CiAgICAgICAgPGgyPkdyYW0mYWFjdXRlO3RpY2Egc2luIHJlY3Vyc2l2aWRhZCBpenF1aWVyZGEsIHByZWZpam9zIGNvbXVuZXMgeSBwcm9kdWNpb25lcyBpbm5lY2VzYXJpYXM8L2gyPgogICAgICAgIDxkaXY+CiAgICAgICAgICAlcwogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAgIDwvZGl2PgogICAgPGRpdiBjbGFzcz0ibGV2ZWwxRGl2Ij4KICAgICAgPGgxPkNvbmp1bnRvcyBGSVJTVCB5IEZPTExPVzwvaDE+CiAgICAgIDxkaXYgY2xhc3M9ImxldmVsMkRpdiI+CiAgICAgICAgPGgyPkZJUlNUPC9oMj4KICAgICAgICA8ZGl2PgogICAgICAgICAgJXMKICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxldmVsMkRpdiI+CiAgICAgICAgPGgyPkZPTExPVzwvaDI+CiAgICAgICAgPGRpdj4KICAgICAgICAgICVzCiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+CiAgICA8ZGl2IGNsYXNzPSJsZXZlbDFEaXYiPgogICAgICA8aDE+QW4mYWFjdXRlO2xpc2lzIExMKDEpPC9oMT4KICAgICAgPGRpdiBjbGFzcz0ibGV2ZWwyRGl2Ij4KICAgICAgICA8aDI+VGFibGEgTEwoMSk8L2gyPgogICAgICAgIDxkaXYgY2xhc3M9ImNvbnRhaW5lckRpdiI+CiAgICAgICAgICAlcwogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ibGV2ZWwyRGl2Ij4KICAgICAgICA8aDI+UmVzdWx0YWRvPC9oMj4KICAgICAgICAlcwogICAgICA8L2Rpdj4KICAgIDwvZGl2PgogICAgPGRpdiBjbGFzcz0ibGV2ZWwxRGl2Ij4KICAgICAgPGgxPkdyYW0mYWFjdXRlO3RpY2EgYXVtZW50YWRhPC9oMT4KICAgICAgPGRpdj4KICAgICAgICAlcwogICAgICA8L2Rpdj4KICAgIDwvZGl2PgogICAgPGRpdiBjbGFzcz0ibGV2ZWwxRGl2Ij4KICAgICAgPGgxPkFuJmFhY3V0ZTtsaXNpcyBTTFIoMSk8L2gxPgogICAgICA8ZGl2IGNsYXNzPSJsZXZlbDJEaXYiPgogICAgICAgIDxoMj5Db2xlY2NpJm9hY3V0ZTtuIGRlIGl0ZW1zIExSKDApPC9oMj4KICAgICAgICA8ZGl2IGNsYXNzPSJjb250YWluZXJEaXYiPgogICAgICAgICAgPGRpdiBjbGFzcz0iaG9yaXpvbnRhbCI+CiAgICAgICAgICAgICVzCiAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxldmVsMkRpdiI+CiAgICAgICAgPGgyPkF1dCZvYWN1dGU7bWF0YSBMUigwKTwvaDI+CiAgICAgICAgPGRpdiBjbGFzcz0iY29udGFpbmVyRGl2Ij4KICAgICAgICAgICVzCiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJsZXZlbDJEaXYiPgogICAgICAgIDxoMj5UYWJsYXMgQUNUSU9OLUdPVE88L2gyPgogICAgICAgIDxkaXYgY2xhc3M9ImNvbnRhaW5lckRpdiI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJob3Jpem9udGFsIj4KICAgICAgICAgICAgJXMKICAgICAgICAgICAgJXMKICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ibGV2ZWwyRGl2Ij4KICAgICAgICA8aDI+UmVzdWx0YWRvPC9oMj4KICAgICAgICAlcwogICAgICA8L2Rpdj4KICAgIDwvZGl2PgogICAgPGRpdiBjbGFzcz0ibGV2ZWwxRGl2Ij4KICAgICAgPGgxPkFuJmFhY3V0ZTtsaXNpcyBMUigxKTwvaDE+CiAgICAgIDxkaXYgY2xhc3M9ImxldmVsMkRpdiI+CiAgICAgICAgPGgyPkNvbGVjY2kmb2FjdXRlO24gZGUgaXRlbXMgTFIoMSk8L2gyPgogICAgICAgIDxkaXYgY2xhc3M9ImNvbnRhaW5lckRpdiI+CiAgICAgICAgICA8ZGl2IGNsYXNzPSJob3Jpem9udGFsIj4KICAgICAgICAgICAgJXMKICAgICAgICAgIDwvZGl2PgogICAgICAgIDwvZGl2PgogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ibGV2ZWwyRGl2Ij4KICAgICAgICA8aDI+QXV0Jm9hY3V0ZTttYXRhIExSKDEpPC9oMj4KICAgICAgICA8ZGl2IGNsYXNzPSJjb250YWluZXJEaXYiPgogICAgICAgICAgJXMKICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxldmVsMkRpdiI+CiAgICAgICAgPGgyPlRhYmxhIEFDVElPTi1HT1RPPC9oMj4KICAgICAgICA8ZGl2IGNsYXNzPSJjb250YWluZXJEaXYiPgogICAgICAgICAgPGRpdiBjbGFzcz0iaG9yaXpvbnRhbCI+CiAgICAgICAgICAgICVzCiAgICAgICAgICAgICVzCiAgICAgICAgICA8L2Rpdj4KICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxldmVsMkRpdiI+CiAgICAgICAgPGgyPlJlc3VsdGFkbzwvaDI+CiAgICAgICAgJXMKICAgICAgPC9kaXY+CiAgICA8L2Rpdj4KICAgIDxkaXYgY2xhc3M9ImxldmVsMURpdiI+CiAgICAgIDxoMT5BbiZhYWN1dGU7bGlzaXMgTEFMUigxKTwvaDE+CiAgICAgIDxkaXYgY2xhc3M9ImxldmVsMkRpdiI+CiAgICAgICAgPGgyPkNvbGVjY2kmb2FjdXRlO24gZGUgaXRlbXMgTEFMUigxKTwvaDI+CiAgICAgICAgPGRpdiBjbGFzcz0iY29udGFpbmVyRGl2Ij4KICAgICAgICAgIDxkaXYgY2xhc3M9Imhvcml6b250YWwiPgogICAgICAgICAgICAlcwogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJsZXZlbDJEaXYiPgogICAgICAgIDxoMj5BdXQmb2FjdXRlO21hdGEgTEFMUigxKTwvaDI+CiAgICAgICAgPGRpdiBjbGFzcz0iY29udGFpbmVyRGl2Ij4KICAgICAgICAgICVzCiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJsZXZlbDJEaXYiPgogICAgICAgIDxoMj5UYWJsYSBBQ1RJT04tR09UTzwvaDI+CiAgICAgICAgPGRpdiBjbGFzcz0iY29udGFpbmVyRGl2Ij4KICAgICAgICAgIDxkaXYgY2xhc3M9Imhvcml6b250YWwiPgogICAgICAgICAgICAlcwogICAgICAgICAgICAlcwogICAgICAgICAgPC9kaXY+CiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgICA8ZGl2IGNsYXNzPSJsZXZlbDJEaXYiPgogICAgICAgIDxoMj5SZXN1bHRhZG88L2gyPgogICAgICAgICVzCiAgICAgIDwvZGl2PgogICAgPC9kaXY+CiAgICA8ZGl2IGNsYXNzPSJsZXZlbDFEaXYiPgogICAgICA8aDE+RGVyaXZhY2lvbmVzIGRlIGxhcyBjYWRlbmFzPC9oMT4KICAgICAgPGRpdiBjbGFzcz0iY29udGFpbmVyRGl2Ij4KICAgICAgICA8ZGl2IGNsYXNzPSJob3Jpem9udGFsIj4KICAgICAgICAgICVzCiAgICAgICAgPC9kaXY+CiAgICAgIDwvZGl2PgogICAgPC9kaXY+CiAgICA8ZGl2IGNsYXNzPSJsZXZlbDFEaXYiPgogICAgICA8aDE+QW4mYWFjdXRlO2xpc2lzIGRlIFJlZ3VsYXJpZGFkPC9oMT4KICAgICAgPGRpdiBjbGFzcz0ibGV2ZWwyRGl2Ij4KICAgICAgICA8aDI+UmVzdWx0YWRvPC9oMj4KICAgICAgICAlcwogICAgICA8L2Rpdj4KICAgICAgPGRpdiBjbGFzcz0ibGV2ZWwyRGl2Ij4KICAgICAgICA8aDI+QXV0Jm9hY3V0ZTttYXRhPC9oMj4KICAgICAgICA8ZGl2IGNsYXNzPSJjb250YWluZXJEaXYiPgogICAgICAgICAgJXMKICAgICAgICA8L2Rpdj4KICAgICAgPC9kaXY+CiAgICAgIDxkaXYgY2xhc3M9ImxldmVsMkRpdiI+CiAgICAgICAgPGgyPkV4cHJlc2kmb2FjdXRlO24gUmVndWxhcjwvaDI+CiAgICAgICAgICAlcwogICAgICA8L2Rpdj4KICAgIDwvZGl2PgogIDwvYm9keT4KPC9odG1sPg==').decode()

class HtmlFormatter:
    @staticmethod
    def symbol_to_html(s):
        return f'<span class="grammarSymbol">{s}</span>'

    @staticmethod
    def epsilon_to_html(e):
        return f'<span class="grammarEpsilon">{e}</span>'

    @staticmethod
    def sentence_to_html(s):
        return HtmlFormatter.collection_to_html(s, ' ')

    arrow_to_html = '<span class="grammarArrow"> → </span>'

    @staticmethod
    def production_to_html(p):
        return '%s%s%s' % (HtmlFormatter.symbol_to_html(p.Left), HtmlFormatter.arrow_to_html,
                            HtmlFormatter.custom_to_html(p.Right))

    or_to_html = '<span class="grammarOr"> | </span>'

    @staticmethod
    def nt_productions_to_html(nt):
        return '%s%s%s' % (HtmlFormatter.symbol_to_html(nt), HtmlFormatter.arrow_to_html,
                            HtmlFormatter.collection_to_html([p.Right for p in nt.productions], HtmlFormatter.or_to_html))

    @staticmethod
    def action_to_html(a):
        action, tag = a
        return '%s%s' % ('<span style="color: gray">S</span>' if action == Action.SHIFT else '<span style="color: green">OK</span>' if action == Action.OK else '',
                        HtmlFormatter.custom_to_html(tag))

    dot_to_html = '<span class="grammarDot"> • </span>'

    @staticmethod
    def item_to_html(i):
        return '%s%s%s%s%s, { %s }' % (HtmlFormatter.symbol_to_html(i.production.Left), HtmlFormatter.arrow_to_html,
                                        HtmlFormatter.collection_to_html(i.production.Right[:i.pos], ' '), 
                                        HtmlFormatter.dot_to_html,
                                        HtmlFormatter.collection_to_html(i.production.Right[i.pos:], ' '), 
                                        HtmlFormatter.collection_to_html(i.lookaheads))

    @staticmethod
    def custom_to_html(c):
        if isinstance(c, Symbol):
            return HtmlFormatter.symbol_to_html(c)
        if isinstance(c, Epsilon):
            return HtmlFormatter.epsilon_to_html(c)
        if isinstance(c, Sentence):
            return HtmlFormatter.sentence_to_html(c)
        if isinstance(c, Production):
            return HtmlFormatter.production_to_html(c)
        if isinstance(c, Item):
            return HtmlFormatter.item_to_html(c)
        if isinstance(c, State):
            return HtmlFormatter.custom_to_html(c.state)
        if isinstance(c, Action):
            return HtmlFormatter.action_to_html(c)
        return f'<span style="color: red"><strong>{c}</strong></span>'

    @staticmethod
    def format_collection(c):
        return [HtmlFormatter.custom_to_html(item) for item in c]

    @staticmethod
    def collection_to_html(c, sep=', ', formatter=None):
        return sep.join([formatter(item) for item in c] if formatter else HtmlFormatter.format_collection(c))

    eol = '\n'

    @staticmethod
    def grammar_to_html(G):
        return f'''<dl>
                <dt><strong>Terminales:</strong></dt> 
                <dd><p>{HtmlFormatter.collection_to_html(G.terminals)}</p></dd>
                <dt><strong>No Terminales:</strong></dt> 
                <dd><p>{HtmlFormatter.collection_to_html(G.nonTerminals)}</p></dd>
                <dt><strong>Producciones:</strong></dt>
                <dd><p>{HtmlFormatter.collection_to_html(G.nonTerminals, '</p><p>', HtmlFormatter.nt_productions_to_html)}</p></dd>
                </dl>'''

    @staticmethod
    def firsts_to_html(G, firsts):
        sf = lambda s: '<p>FIRST(%s) = { %s }</p>' % (HtmlFormatter.symbol_to_html(s), HtmlFormatter.collection_to_html(firsts[s].items()))
        pf = lambda p: '<p>FIRST(%s) = { %s }</p>' % (HtmlFormatter.production_to_html(p), HtmlFormatter.collection_to_html(firsts[p.Right].items()))

        return f'''<dl>
                <dt><strong>No Terminales:</strong></dt> 
                <dd>{HtmlFormatter.collection_to_html(G.nonTerminals, HtmlFormatter.eol, sf)}</dd>
                <dt><strong>Producciones:</strong></dt>
                <dd>{HtmlFormatter.collection_to_html(G.Productions, HtmlFormatter.eol, pf)}</dd>
                </dl>'''

    @staticmethod
    def follows_to_html(G, follows):
        sf = lambda s: '<p>FOLLOW(%s) = { %s }</p>' % (HtmlFormatter.symbol_to_html(s), HtmlFormatter.collection_to_html(follows[s]))

        return f'''<dl>
                <dt><strong>No Terminales:</strong></dt>
                <dd>{HtmlFormatter.collection_to_html(G.nonTerminals, HtmlFormatter.eol, sf)}</dd>
                </dl>'''

    @staticmethod
    def cell_class(row, symbol): 
        return f'''<td {'class="errorCell"' if symbol in row and len(row[symbol]) > 1 else ''} title="{symbol}">'''

    @staticmethod
    def ll1_table_to_html(G, table, label=''):
        return f'''<table>
                    <tr><th>{label}</th><th>{HtmlFormatter.collection_to_html(G.terminals, '</th><th>')}</th>
                    {''.join(f'<tr><th>{HtmlFormatter.symbol_to_html(nt)}</th>'
                            + ''.join(f'{HtmlFormatter.cell_class(row, t)}<p>' + 
                            (HtmlFormatter.collection_to_html(row[t], '</p><p>') if t in row else '-----') + '</p></td>'
                                for t in G.terminals) + '</tr>'
                        for nt, row in table.items())}
                    </table>'''

    @staticmethod
    def items_collection_to_html(automaton):
        ni = lambda i: f'<p class="itemCollection">{HtmlFormatter.custom_to_html(i)}</p>'
        nr = lambda n: f'''<table>
                        <tr><th>I<sub>{n.idx}</sub>:</th></tr>
                        <tr><td>{HtmlFormatter.collection_to_html(n.state, HtmlFormatter.eol, ni)}</td></tr>
                        </table>'''

        return HtmlFormatter.collection_to_html(automaton, HtmlFormatter.eol, nr)

    @staticmethod
    def action_goto_table_to_html(table, columns, label=''):
        cs = lambda c: f'<th>{HtmlFormatter.symbol_to_html(c)}</th>'
        cl = lambda c: f'<p>{HtmlFormatter.custom_to_html(c)}</p>'    
        return f'''<table>
                    <tr><th>{label}</th>{HtmlFormatter.collection_to_html(columns, HtmlFormatter.eol, cs)}</tr>
                    {''.join('<tr>' + f'<th>I<sub>{idx}</sub></th>' + ''.join(HtmlFormatter.cell_class(row, symbol) +
                            (HtmlFormatter.collection_to_html(row[symbol], '', cl) if symbol in row else '-----')  + '</td>'
                                for symbol in columns) + '</tr>' 
                        for idx, row in table.items())}
                    </table>'''

    @staticmethod
    def derivations_to_html(words, derivations):
        dr = lambda d: HtmlFormatter.error_message_to_html('Error al parsear') if d is None else d 
        wd = lambda c: f'<table><tr><th>{HtmlFormatter.collection_to_html(c[0])}</th></tr><tr><td>{dr(c[1])}</td></tr></table>'

        return HtmlFormatter.collection_to_html(zip(words, derivations), HtmlFormatter.eol, wd)

    @staticmethod
    def error_message_to_html(msg):
        return f'<h3 class="error">• {msg}</h3>'

    @staticmethod
    def message_to_html(msg):
        return f'<h3>• {msg}</h3>'

    @staticmethod
    def good_message_to_html(msg):
        return f'<h3 class="good">• {msg}</h3>'
