from re import match

class Handler:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)
    def start(self, name):
        self.callback('start_', name)
    def end(self, name):
        self.callback('end_', name)
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                result = match.group(0) # The entire match
            return result
        return substitution

class HTMLRenderer(Handler):
    def start_document(self):
        print('<!DOCTYPE html>')
        print('<html><head><title>...</title>')
        print('<link rel="stylesheet" type="text/css" href="E:/pythonProgram/20171008_txt2html/test_css.css" />')
        print('''<style>
        body {
            background-color: linen;
        }

        h1 {
            color: maroon;
            margin-left: 40px;
        }
        </style>''')
        print('</head><body>')
    def end_document(self):
        print('</body></html>')
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2>')
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
    def start_title(self):
        print('<h1>')
    def end_title(self):
        print('</h1>')
    def sub_emphasis(self, match): #强调的内容
        return '<em>%s</em>' %match.group(1)
    def sub_url(self, match): #强调的内容
        return '<a href="%s">%s</a>' %(match.group(1), match.group(1))
    def sub_img(self, match):
        return '<img src="%s"  alt="%s" />' %(match.group(1), match.group(1))
    def sub_video(self, match):
        return '<video src="%s" controls="controls" width=600> 您的浏览器不支持 video 标签。 </video>' %match.group(1)
    def feed(self, data):
        print(data)

