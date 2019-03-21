# from django.test import TestCase
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from django.core.urlresolvers import reverse
# import os,socket
# from django.contrib.staticfiles import finders
# #from mainpage.models import Page, Category
# import populate_conspiragram
# import mainpage.test_utils as test_utils
# from mainpage.forms import CommentsForm
# #from mainpage.forms import PictureForm
# from django.template import loader
# from django.conf import settings
# import os.path
# #from rango.models import User
# from mainpage.models import UserProfile,Picture,Comments
# #from rango.forms import UserForm, UserProfileForm
# from selenium.webdriver.common.keys import Keys
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.core.files.storage import default_storage
# from datetime import datetime, timedelta


# '''
# class SessionTests(TestCase):
#     def test_user_number_of_access_and_last_access_to_index(self):
#         #Access index page 100 times
#         for i in range(0, 100):
#             try:
#                 response = self.client.get(reverse('index'))
#             except:
#                 try:
#                     response = self.client.get(reverse('mainpage:index'))
#                 except:
#                     return False
#             session = self.client.session
#             # old_visists = session['visits']

#             # Check it exists visits and last_visit attributes on session
#             self.assertIsNotNone(self.client.session['visits'])
#             self.assertIsNotNone(self.client.session['last_visit'])

#             # Check last visit time is within 0.1 second interval from now
#             # self.assertAlmostEqual(datetime.now(),
#             #     datetime.strptime(session['last_visit'], "%Y-%m-%d %H:%M:%S.%f"), delta=timedelta(seconds=0.1))

#             # Get last visit time subtracted by one day
#             last_visit = datetime.now() - timedelta(days=1)

#             # Set last visit to a day ago and save
#             session['last_visit'] = str(last_visit)
#             session.save()

#             # Check if the visits number in session is being incremented and it's correct
#             self.assertEquals(session['visits'], session['visits'])
#             # before it was i+1 but visits shouldn't change for the same ip visited in one day
        
		
# class LiveServerTests(StaticLiveServerTestCase):
# 	def setUp(self):
# 		from django.contrib.auth.models import User
# 		User.objects.create_superuser(username='admin', password='admin', email='admin@me.com')
# 		chrome_options = webdriver.ChromeOptions()
# 		chrome_options.add_argument('headless')
# 		self.browser = webdriver.Chrome(chrome_options = chrome_options)
# 		self.browser.implicitly_wait(3)

# 	@classmethod
# 	def setUpClass(cls):
# 		cls.host = socket.gethostbyname(socket.gethostname())
# 		super(LiveServerTests, cls).setUpClass()

# 	def tearDown(self):
# 		self.browser.refresh()
# 		self.browser.quit()
	

	

	
# 	def test_links_in_mainpage_when_logged(self):
#         # Access login page
# 		url = self.live_server_url
# 		url = url.replace('localhost', '127.0.0.1')
# 		try:
# 			self.browser.get(url + reverse('auth_login'))
# 		except:
# 			try:
# 				self.browser.get(url + reverse('registration:auth_login'))
# 			except:
# 				return False

# 			# Log in
# 		test_utils.user_login(self)

# 			#Check links that appear for logged person only
# 		self.browser.find_element_by_link_text('Sign Out')
# 		self.browser.find_element_by_link_text('about us')
			
# 			 # Check that links does not appears for logged users
# 		body = self.browser.find_element_by_tag_name('body')
# 		self.assertNotIn('Login', body.text)
# 		self.assertNotIn('Sign Up', body.text)
			
# 		###	
# 	def test_links_in_index_page_when_not_logged(self):
# 			#Access index page
# 		url = self.live_server_url
# 		url = url.replace('localhost', '127.0.0.1')
# 		try:
# 			self.browser.get(url + reverse('index'))
# 		except:
# 			try:
# 				self.browser.get(url + reverse('mainpage:index'))
# 			except:
# 				return False

# 		#Check links that appear for not logged person only
# 		self.browser.find_element_by_link_text('Sign Up')
# 		self.browser.find_element_by_link_text('Login')
# 		self.browser.find_element_by_link_text('about us')

# 		# Check that links does not appears for not logged users
# 		body = self.browser.find_element_by_tag_name('body')
# 		self.assertNotIn('Logout', body.text)
		
		
	
# 	def test_logout_link(self):
# 		# Access login page
# 		url = self.live_server_url
# 		url = url.replace('localhost', '127.0.0.1')
# 		try:
# 			self.browser.get(url + reverse('auth_login'))
# 		except:
# 			try:
# 				self.browser.get(url + reverse('registration:auth_login'))
# 			except:
# 				return False

# 		# Log in
# 		test_utils.user_login(self)

# 		#Clicks to logout
# 		self.browser.find_element_by_link_text('Sign Out').click()

# 		# Check if it see log in link, thus it is logged out
# 		self.browser.find_element_by_link_text('Sign Up')
		
		
	
# 	#ERROR
# 	def test_navigate_from_index_to_about(self):
# 		# Go to index page
# 		url = self.live_server_url
# 		url = url.replace('localhost', '127.0.0.1')
# 		print(url)
# 		self.browser.get(url + reverse('index'))

# 		# Search for a link to About page
# 		about_link = self.browser.find_element_by_partial_link_text("about us")
# 		about_link.click()

# 		# Check if it goes back to the home page
# 		self.assertIn(url + reverse('about'), self.browser.current_url)

	
	
	
# class ModelTests(TestCase):
# #ERROR
# 	def test_user_profile_model(self):
#         # Create a user
# 		user, user_profile = test_utils.create_user()

# 		# Check there is only the saved user and its profile in the database
# 		all_users = User.objects.all()
# 		self.assertEquals(len(all_users), 1)

# 		all_profiles = UserProfile.objects.all()
# 		self.assertEquals(len(all_profiles), 1)

# 		# Check profile fields were saved correctly
# 		all_profiles[0].user = user
# 		all_profiles[0].website = user_profile.website
		
		
# 		#ERROR
# 	def test_create_a_new_Picture(self):
# 		pic = Picture(title="Python")
# 		pic.save()
# 		# Check category is in database
# 		pictures_in_database = Picture.objects.all()
# 		self.assertEquals(len(pictures_in_database), 1)
# 		only_poll_in_database = pictures_in_database[0]
# 		self.assertEquals(only_poll_in_database, pic)
# 	#ERROR
# 	def test_create_comments_for_pictures(self):
# 		pic = Picture(title="Python")
# 		pic.save()

# 		# create 2 comments for picture python
# 		python_comments = Comments()
# 		python_comments.picture = pic 
# 		python_comments.text="Comment1"
# 		python_comments.save()

# 		python_comments = Comments()
# 		python_comments.picture = pic 
# 		python_comments.text="Comment2"
# 		python_comments.save()
# 		# Check if they both were saved
# 		python_comments = pic.comments_set.all()
# 		self.assertEquals(python_comments.count(), 2)

# 		#Check if they were saved properly
# 		first_comments = python_comments[0]
# 		self.assertEquals(first_comments.text , "Comment1")
	  
# #ERROR
# 	def test_population_script_changes(self):
# 		#Populate database
# 		populate_conspiragram.populate()

		
# 		user = user.objects.get(ID='Shauna239@example.com')
# 		self.assertEquals(user.name, "ShaunaShining")
# 		self.assertEquals(user.rank, "Sighter")
# 		self.assertEquals(user.rankscore, 60)
		
# 		pic = Picture.objects.get(UserID="Shauna239@example")
# 		self.assertEquals(pic.true, 35)
# 		self.assertEquals(pic.false, 20)
# 		self.assertEquals(pic.date, "2018-06-20")
# 		self.assertEquals(pic.location, "Edinburgh")
# 		self.assertEquals(pic.picid, 0)
	 
# 		com = Comment.objects.get(userid='theworst@example',picid=1)
# 		self.assertEquals(com.text,"lol fake" )
# '''	   
	
	
# class ViewTests(TestCase):
# 	'''
# 	def test_base_template_exists(self):
# 		# Check base.html exists inside template folder
# 		path_to_base = settings.TEMPLATE_DIR + '/mainpage/base.html'
# 		print(path_to_base)
# 		self.assertTrue(os.path.isfile(path_to_base))
	
# 	###
# 	def test_titles_displayed(self):
# 		# Create user and log in
# 		test_utils.create_user()
# 		self.client.login(username='testuser', password='test1234')

# 		# Access index and check the title displayed
# 		response = self.client.get(reverse('index'))
# 		self.assertIn('Home'.lower(), response.content.decode('ascii').lower())


# 		# Access about page and check the title displayed
# 		response = self.client.get(reverse('about'))
# 		self.assertIn('About Us'.lower(), response.content.decode('ascii').lower())

# 		# Access mainpage page and check the title displayed
# 		response = self.client.get(reverse('mainpage'))
# 		self.assertIn('Mainpage'.lower(), response.content.decode('ascii').lower())

# 		# Access profile_edit page and check the title displayed
# 		response = self.client.get(reverse('Profile_edit'))
# 		self.assertIn('Profile Edit'.lower(), response.content.decode('ascii').lower())
		
		
		
# 	'''
# 	'''
# 	#EEROR
# 	def test_url_reference_in_mainpage_page_when_logged(self):
# 		# Create user and log in
# 		test_utils.create_user()
# 		self.client.login(username='testuser', password='test1234')

# 		# Access index page
# 		response = self.client.get(reverse('mainpage'))

# 		# Check links that appear for logged person only
# 		self.assertIn(reverse('user_profile'), response.content.decode('ascii'))
# 		self.assertIn(reverse('profile_edit'), response.content.decode('ascii'))
# 		self.assertIn(reverse('auth_logout'), response.content.decode('ascii'))
		
# 	#EEROR
# 	def test_url_reference_in_index_page_when_not_logged(self):
# 		#Access index page with user not logged
# 		response = self.client.get(reverse('index'))

# 		# Check links that appear for logged person only
# 		self.assertIn(reverse('registration_register'), response.content.decode('ascii'))
# 		self.assertIn(reverse('auth_login'), response.content.decode('ascii'))
# 		self.assertIn(reverse('auth_password_reset'), response.content.decode('ascii'))
		
		
# 	#EEROR
# 	def test_link_to_about_in_base_template(self):
# 		# Access about
# 		response = self.client.get(reverse('about'))

# 		# Check for url referencing about
# 		self.assertIn(reverse('about'), response.content.decode('ascii'))
		
	
# 	#EEROR
# 	def test_registration_form_is_displayed_correctly(self):
# 		#Access registration page
# 		try:
# 			response = self.client.get(reverse('registration_register'))
# 		except:
# 			try:
# 				response = self.client.get(reverse('registration:registration_register'))
# 			except:
# 				return False

# 		# Check form in response context is instance of UserForm
# 		self.assertTrue(isinstance(response.context['user_form'], UserForm))

# 		# Check form in response context is instance of UserProfileForm
# 		self.assertTrue(isinstance(response.context['profile_form'], UserProfileForm))

# 		user_form = UserForm()
# 		profile_form = UserProfileForm()

# 		# Check form is displayed correctly
# 		self.assertEquals(response.context['user_form'].as_p(), user_form.as_p())
# 		self.assertEquals(response.context['profile_form'].as_p(), profile_form.as_p())

# 		# Check submit button
# 		self.assertIn('type="submit"', response.content.decode('ascii'))
# 		self.assertIn('name="submit"', response.content.decode('ascii'))
# 		self.assertIn('value="Register"', response.content.decode('ascii'))

# 	'''
# 	'''
# 	def test_index_using_template(self):
# 		response = self.client.get(reverse('index'))

# 		# Check the template used to render index page
# 		self.assertTemplateUsed(response, 'mainpage/index.html')

# 	def test_about_using_template(self):
# 		self.client.get(reverse('index'))
# 		response = self.client.get(reverse('about'))

# 		# Check the template used to render about page
# 		self.assertTemplateUsed(response, 'mainpage/about.html')

# 	def test_avatar_picture_displayed(self):
# 		response = self.client.get(reverse('index'))

# 		# Check if is there an image in index page
# 		self.assertIn('img src="/static/images/default_avatar.jpg'.lower(), response.content.decode('ascii').lower())
# '''
# 	# New media test
# 	#ERROR
# 	def test_ufo_picture_displayed(self):
# 		response = self.client.get(reverse('mainpage'))

# 		# Check if is there an image in main page
# 		self.assertIn('img src="/media/ufo1.jpg'.lower(), response.content.decode('ascii').lower())
# 	#ERROR
# 	def test_about_contain_image(self):
# 		self.client.get(reverse('index'))
# 		response = self.client.get(reverse('about'))

# 		# Check if is there an image in index page
# 		self.assertIn('img src="/static/images/index.jpg', response.content.decode('utf8'))
# 	#ERROR
# 	def test_serving_static_files(self):
		
# 		result = finders.find('images/default_avatar.jpg')
# 		result = finders.find('images/hugo.jpg')
# 		result = finders.find('images/kaixin.jpg')
# 		result = finders.find('images/mark.jpg')
# 		result = finders.find('images/miao.jpg')
# 		result = finders.find('images/index.jpg')
# 		self.assertIsNotNone(result)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
# 	