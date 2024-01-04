from models.art import *

class Display:
    def __init__(self, border_head="+", border_body="-", title="", content="", options={}, width=0, alt_border_head="|", alt_border_body = "=", art=""):
        self.title = title
        self.border_head = border_head
        self.border_body = border_body
        self.alt_border_head = alt_border_head
        self.alt_border_body = alt_border_body
        self.content = content
        self.options = options 
        self.width = width
        self.art = art

        self.border_segment = (f"{self.border_head}{self.border_body * self.width}{self.border_head}")
        self.border =  (f"{self.border_segment}{self.border_segment}")
        self.alt_border_segment = (f"{self.alt_border_head}{self.alt_border_body * self.width}{self.alt_border_head}")
        self.alt_border = (f"{self.alt_border_segment}{self.alt_border_segment}")

    @property
    def title (self):
        return self._title
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise Exception("title must be a string")
        else:
            self._title = title
    
    @property
    def border_head (self):
        return self._border_head
    @border_head.setter
    def border_head(self, border_head):
        if not isinstance(border_head, str):
            raise Exception("border_head must be a string")
        else:
            self._border_head = border_head
    
    @property
    def alt_border_head (self):
        return self._alt_border_head
    @alt_border_head.setter
    def alt_border_head(self, alt_border_head):
        if not isinstance(alt_border_head, str):
            raise Exception("alt_border_head must be a string")
        else:
            self._alt_border_head = alt_border_head
    
    @property
    def alt_border_body (self):
        return self._alt_border_body
    @alt_border_body.setter
    def alt_border_body(self, alt_border_body):
        if not isinstance(alt_border_body, str):
            raise Exception("alt_border_body must be a string")
        else:
            self._alt_border_body = alt_border_body
    
    @property
    def border_body (self):
        return self._border_body
    @border_body.setter
    def border_body(self, border_body):
        if not isinstance(border_body, str):
            raise Exception("border_body must be a string")
        else:
            self._border_body = border_body
    
    @property
    def content (self):
        return self._content
    @content.setter
    def content(self, content):
        if not isinstance(content, str):
            raise Exception("content must be a string")
        else:
            self._content = content
    
    @property
    def options (self):
        return self._options
    @options.setter
    def options(self, options):
        # if not isinstance(options, list):
        #     raise Exception("options must be a list")
        # else:
            self._options = options
    
    @property
    def width (self):
        return self._width
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise Exception("width must be an integer")
        if width < len(self.title):
            self._width = len(self.title)
        else:
            self._width = width
    
    def print_screen(self):
        print(self.alt_border)
        white_spaced_title = f"*{' ' * int((len(self.border) - len(self.title)) / 2 )}{self.title}{' ' * int((len(self.border) - len(self.title)) / 2 - 1)}*"
        print(white_spaced_title)
        print(self.art)
        print(f"{self.alt_border}\n")

        word_list = self.content.split(' ')
        content = []
        content_line = (" ".join(content))
        for word in word_list:
            if len(content_line) >= self.width * 2 - 5:
                print(f"| {content_line} ")
                content = []
                content.append(word)
                content_line = (" ".join(content))
            else:
                content.append(word)
                content_line = (" ".join(content))
        print(f"| {content_line}\n")
        print(self.border)
        for selection in self.options:
            print(f"{selection}")
            
    def __repr__(self):
        return f"<Display: {self.title}>"
    


