import time
import scrapy
import MySQLdb
import urllib
from selenium import webdriver
from scrapy.http import TextResponse
from selenium.webdriver.common.keys import Keys
from PIL import Image
import json
import os

class tel():
	def start_requests(self):
		driver = webdriver.Firefox()
		driver.get("https://web.telegram.org/")
		time.sleep(2)
		while True:
	            db = MySQLdb.connect(host="", port=, user="", passwd="", db="")
        	    cursor = db.cursor()
	            sql ="select no_hp from table1 where table2 = 0"
        	    cursor.execute(sql)
	            nohp = cursor.fetchall()
	            #cursor.close()
	            #db.close()
         	    try:
            		for loop in range(len(nohp)):
            			keyword = nohp[loop]
                    		keyword = str(keyword).replace('(', '').replace(')', '').replace('\'', '').replace(',', '')
                             	bar = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/a/div/span[2]")
				bar.click()
				time.sleep(2)
				kontak = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/ul/li[2]/a")
				kontak.click()
				time.sleep(2)
				new = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[3]/div/button")
				new.click()
				time.sleep(2)
				add = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div[1]/form/div[1]/input")
				add.send_keys(keyword)
				time.sleep(5)
				save = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div[2]/button[2]")
				save.click()
				time.sleep(2)
				myid = "select id from table1 where no_hp =%s"% keyword
				cursor.execute(myid)
				id_sql = cursor.fetchone()
				try:
					#for apabebas in range(0,10):
					time.sleep(1)
				#	try:
					gagal = driver.find_element_by_xpath('//*[@class="modal-dialog"]/div[1]/div[1]/div[2]/button')
					gagal.click()
					close = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[1]/div[1]/div/a[1]')
					close.click()
					sql = "update table1 set table2 = -1 where no_hp = '" + str(keyword) + "'"
                	       		cursor.execute(sql)
        		        	db.commit()
			                print "update fail"
					
					json_post = json.dumps({"id" : str(id_sql[0]) ,"type" : "telegram","data" : [{"no_hp" : keyword, "name" : "user notfound", "url_image" : "/home/.../.../empty_image.png"}]})
                    			
					p = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/div/div[2]/a")
					p.click()
					time.sleep(3)
					
					more = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[3]/div/div[3]/div[2]/a')
					more.click()
					time.sleep(2)
					delete = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[3]/div/div[3]/div[2]/a')
					delete.click()
					time.sleep(2)
					response = TextResponse(driver.current_url, body=driver.page_source, encoding='utf-8')
					nama = response.xpath('/html/body/div[5]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/text()').extract_first()
					try :
						gambar = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div[2]/div[1]/a/img")
						gambar.click()
						time.sleep(1)
						direktori3 = '/data/.../image/' + str(keyword) 
						try :
							os.mkdir(direktori3)
						except :
							pass
						direktori = direktori3 + '/' + str(keyword) + '.jpg'
						direktori2 = direktori.replace("data", "home").replace("crawler2","crawler")
						driver.get_screenshot_as_file(direktori)							
									
						img = Image.open(direktori)
						img2 = img.crop((340,26, 631, 317))
						img2.save(direktori)
					except :
						direktori2 = '/home/.../../.../empty_image.png'
					
					print nama
					nama = ''.join(nama).encode('utf-8')
					json_post = json.dumps({"id" : str(id_sql[0]) ,"type" : "telegram","data" : [{"no_hp" : keyword,"name" : str(nama),"url_image" : direktori2}]})
					print json_post
					
			print "Done"
	            except:
        		 pass
		    cursor.close()
		    db.close()
		    time.sleep(3)

if __name__ == '__main__':
    telegram().start_requests()
