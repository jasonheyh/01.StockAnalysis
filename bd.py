from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.co.jp/s/ref=nb_sb_noss?__mk_ja_JP=カタカナ&url=search-alias%3Daps&field-keywords=+再生クリアホルダー角丸+++枚+")

temp1=driver.find_element_by_id("leftNavContainer").text
for tmpText in temp1:

    print(tmpText)

driver.get(
        "https://www.amazon.co.jp/s/ref=nb_sb_noss?__mk_ja_JP=カタカナ&url=search-alias%3Daps&field-keywords=+再生クリアホルダー角丸+++枚+")

temp1 = driver.find_element_by_id("leftNavContainer").text
for tmpText in temp1:
    print(tmpText)

driver.close()


# tableI = driver.find_element_by_tag_name("a").text
# print(tableI)
# #获取网页源码
# data = driver.page_source
# print(data)
# #获取元素的html源码
# tableData = driver.find_elements_by_tag_name('tableData').get_attribute('innerHTML')
# #获取元素的id值
# tableI = driver.find_elements_by_tag_name('tableData').get_attribute('id')
# #获取元素的文本内容
# tableI = driver.find_elements_by_tag_name('tableData').text
# driver.quit()