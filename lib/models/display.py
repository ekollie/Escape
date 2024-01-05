from models.art import *

class Display:
    def __init__(self, border_head="+", border_body="-", title="", content="", options={}, width=0, alt_border_head="|", alt_border_body="=", art=""):
        self.title = title
        self.border_head = border_head
        self.border_body = border_body
        self.alt_border_head = alt_border_head
        self.alt_border_body = alt_border_body
        self.content = content
        self.options = options 
        self.width = width
        self.art = art

        # Precompute border and alternative border segments for efficiency
        self.border_segment = f"{self.border_head}{self.border_body * self.width}{self.border_head}"
        self.border = f"{self.border_segment}{self.border_segment}"
        self.alt_border_segment = f"{self.alt_border_head}{self.alt_border_body * self.width}{self.alt_border_head}"
        self.alt_border = f"{self.alt_border_segment}{self.alt_border_segment}"

    # Property getters and setters for data validation

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise Exception("title must be a string")
        else:
            self._title = title
    
    # Similar property getters and setters for other attributes...

    def print_screen(self):
        # Print the display screen with proper formatting
        print(self.alt_border)
        white_spaced_title = f"*{' ' * int((len(self.border) - len(self.title)) / 2)}{self.title}{' ' * int((len(self.border) - len(self.title)) / 2 - 1)}*"
        print(white_spaced_title)
        print(self.art)
        print(f"{self.alt_border}\n")

        # Break content into lines to fit within the specified width
        word_list = self.content.split(' ')
        content = []
        content_line = " ".join(content)
        for word in word_list:
            if len(content_line) >= self.width * 2 - 5:
                print(f"| {content_line} ")
                content = []
                content.append(word)
                content_line = " ".join(content)
            else:
                content.append(word)
                content_line = " ".join(content)
        print(f"| {content_line}\n")
        print(self.border)
        
        # Print options
        for selection in self.options:
            print(f"{selection}")
            
    def __repr__(self):
        return f"<Display: {self.title}>"
