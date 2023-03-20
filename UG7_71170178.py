class Browser:
    def __init__(self):
        self.data = []
        self.cba = []

    def go(self, url):
        self.data.append(url)
        self.cba.clear()

    def back(self):
        if len(self.data) > 1:
            self.cba.append(self.data.pop())
            return self.data[-1]

    def forward(self):
        if self.cba:
            self.data.append(self.cba.pop())
            return self.data[-1]

    def printAll(self):
        print(*self.data)


browser = Browser()
browser.go("https://google.com")
browser.go("https://ukdw.ac.id")
browser.go("https://facebook.com")

print(browser.back()) #output: https://ukdw.ac.id
print(browser.back()) #output: https://google.com
print(browser.forward()) #output: https://ukdw.ac.id

browser.go("https://twitter.com") 
browser.printAll() #output: https://google.com https://ukdw.ac.id https://twitter.com