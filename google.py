
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

'''
셀레니움을 활용한 웹 크롤링
'''

# 크롬 드라이버를 불러와서 driver 변수로 저장
driver = webdriver.Chrome('/Users/youngseonkim/Documents/crawling_practice/chromedriver')

# 크롬을 실행해서 이동하고자하는 URL 주소로 실행
driver.get("https://www.youtube.com")

# HTML 태그중 name == search_query 인 태그를 가져옴 
elem = driver.find_element_by_name("search_query")

# 해당 태그에 input 값을 임의로 지정
elem.send_keys("I can't stop me 커버")

# Enter 치는 것과 같은 역할 수행
elem.send_keys(Keys.RETURN)

# 3초동안 코드 진행을 멈춤, 브라우저가 로딩될 때 까지 기다리기 위해 사용
time.sleep(3)

# Scroll Down 하는 코드
SCROLL_PAUSE_TIME = 1.0

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    


# css class 중 입력된 값에 해당하는 태그를 찾아 첫번째 element를 클릭한다
# driver.find_elements_by_css_selector(".style-scope.yt-img-shadow")[0].click()

# css class 중 입력된 값에 해당하는 태그를 찾아 src attribute의 src를 가져옴
# driver.find_element_by_css_selector(".style-scope.yt-img-shadow").get_attribute("src")

# urllib.request.urlretrieve(img_url, "test.jpg")
# img = driver.find_element_by_tag_name("img")
images = driver.find_elements_by_css_selector("img.style-scope.yt-img-shadow")

count = 1
thumbnail_num = 1
for image in images:
    try:
        img_url = image.get_attribute("src")
        print(img_url)
        urllib.request.urlretrieve(img_url, str(thumbnail_num) + '.jpg')
        thumbnail_num += 1
    except:
        pass
driver.close()

