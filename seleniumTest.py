from selenium import webdriver
from time import sleep   #由于程序执行快，服务器还没来得及响应，就会报错没找到，这时find前设置睡眠时间/等待时间------------->多久好呢?==>selenuim提供的机制（implicitly_wait（最大等待时间））

driver = webdriver.Chrome(r'D:\SoftwarePackage\SoftwarePackage\chromedriver.exe')  # Chrome遥控器

driver.implicitly_wait(10)

driver.get('https://www.icourse163.org/course/BIT-268001')   # 自动打开网页

searchElement = driver.find_element_by_class_name('course-title')

# 由于id属性唯一，最为该高效
# searchElement = driver.find_element_by_id('review-tag-button')  #生成操纵搜索框的元素控制器  WebElement对象
print(searchElement.text)
print(searchElement.get_attribute('class'))                 # 获取element的class属性
print(searchElement.get_attribute('outerHTML'))             # 获取外部标签<span class="course-title f-ib f-vam">Python语言程序设计</span>
print(searchElement.get_attribute('innerHTML'))              # 获取内部标签


# find_elements_by_class_name 方法返回的是找到的符合条件的 所有 元素 (这里有3个元素)， 放在一个 列表 中返回。
# 而如果我们使用 find_element_by_class_name (注意少了一个s) 方法， 就只会返回 第一个 元素
# text属性就是该 WebElement对象对应的元素在网页中的文本内容

# 不仅 WebDriver对象有 选择元素 的方法， WebElement对象 也有选择元素的方法。
# WebElement对象 也可以调用 find_elements_by_xxx， find_element_by_xxx 之类的方法
# WebDriver 对象 选择元素的范围是 整个 web页面， 而WebElement 对象 选择元素的范围是 该元素的内部

# 对于input输入框的元素，要获取里面的输入文本，用text属性是不行的，这时可以使用 element.get_attribute('value')


# searchElement.send_keys('Chrome')  # 输入前可以利用clear清除已有的输入框中的内容
# searchElement.click()

# CSS选择器
# elements = driver.find_elements_by_css_selector('div') <=> elements = driver.find_elements_by_tag_name('div')
# element = wd.find_element_by_css_selector('#searchtext') <=> element = driver.find_element_by_id('searchtext')
# elements = wd.find_elements_by_css_selector('.animal') <=> elements = wd.find_elements_by_class_name('animal')
# CSS选择器中的直接子元素（>）来选择，非直接子元素（ ）来选择
# CSS选择器中的属性选择器用[属性值]来选择
#     element = wd.find_element_by_css_selector('[href="http://www.miitbeian.gov.cn"]')
#     div[class='SKnet']
#     [href]表示选择所有具有属性名为href的元素
# CSS选择器选择属性属性是否含有某些字符串
#   a[href*="miitbeian"] 含有
#   a[href^="http"]     前缀
#   a[href$="gov.cn"]   后缀
# 多属性   div[class=misc][ctype=gun]

# F12验证是是否选中  点击element  CTRL+F 查询是否定位到那一块区域

# CSS选择器高级----->非常强大
# 联合选择
# div.footer1 > span.copyright  ->   .footer1 > .copyright   ->  .footer1  .copyright     .....  再写选择表达式的时候先再浏览器上验证一下是否有误
#组选择
# .plant , .animal  逗号表示和的关系
# 注意类似  #t1 > span,p 和 #t1 > span , #t1 > p的区别是  前者找到t1下的span和所有p，而后者是t1下的span和p ------>所以尽量写细一点

# CSS按顺序选择子元素
# 父元素第几个节点 span:nth-child(2)           与:nth-child(2)不同，它是所有第二节点
# 父元素倒数第几个节点  p:nth-last-child(1)
# 父元素的第几个某类型的子节点  span:nth-of-type(1)
# 父元素的倒数第几个某类型的子节点 p:nth-last-of-type(2)
# 奇数节点和偶数节点 p:nth-child(even) p:nth-child(odd)
# 相邻兄弟节点选择  h3 + span
# 后续所有兄弟节点选择 h3 ~ span


# frame切换/窗口切换
# 遇到iframe， wd.switch_to.frame(frame_reference)  参数列表里可以是id，class，name等等，也可以是webelement对象  wd.switch_to.frame(wd.find_element_by_tag_name("iframe")) ，返回到原始窗口  wd.switch_to.default_content()
# 新的window，再原始标签中，点击链接并不能爬取到想要的目标链接的元素，所以先要 wd.switch_to.window(handle) handle中是一个个页面ID组成的列表
# example：
# for handle in wd.window_handles:
#     # 先切换到该窗口
#     wd.switch_to.window(handle)
#     # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
#     if 'Bing' in wd.title:
#         # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
#         break
# 切换回原来的窗口
# mainWindow = wd.current_window_handle
# wd.switch_to.window(mainWindow)




