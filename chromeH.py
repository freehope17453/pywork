# 对于动态加载的网页，例如知乎，需要使用Selenium+ChromeDriver(或PhantomJS)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 写一个关于刀的故事
url = 'https://www.zhihu.com/question/45694301'

# 让界面滚动的函数 --
def scroll(driver):
    driver.execute_script("""
           (function () {
               var y = document.body.scrollTop;
               var step = 100;
               window.scroll(0, y);


               function f() {
                   if (y < document.body.scrollHeight) {
                       y += step;
                       window.scroll(0, y);
                       setTimeout(f, 50);
                   }
                   else {
                       window.scroll(0, y);
                       document.title += "scroll-done";
                   }
               }
               setTimeout(f, 1000);
           })();
           """)

driver = webdriver.Chrome()
driver.get(url)
scroll(driver)
# 等到滑到最下面
time.sleep(150)
html = driver.page_source

soup = BeautifulSoup(html,'lxml')
storys = soup.find_all('div',class_="List-item")
for story in storys :
    nameLabel = story.find('meta',itemprop="name")
    name = nameLabel["content"]
    with open('关于刀的故事-'+str(name)+'.txt','w') as f:
        storyText = story.find('span', class_="RichText ztext CopyrightRichText-richText")
        storyPages = storyText.find_all('p')
        # 打印看标签内容到底是什么
        # print(storyPages)
        try:
                for storyPage in storyPages:
                    f.write(str(storyPage.string)+'\n')
                print('By '+str(name)+' has been finished')
        except Exception:
            print('Something is wrong on writing to txt')

print('That is all')
