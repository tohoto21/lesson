

def home():
    f= open('index.html',encoding='utf=8')
    content = f.read()
    f.close()
    print(content)




if __name__ == '__main__':
    home()
