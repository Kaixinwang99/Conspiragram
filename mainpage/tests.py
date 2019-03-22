from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from django.core.urlresolvers import reverse
import os,socket
from django.contrib.staticfiles import finders
#from mainpage.models import Page, Category
import populate_conspiragram
import mainpage.test_utils as test_utils
#from mainpage.forms import CommentsSubmissionForm
#from mainpage.forms import PictureForm
from django.template import loader
from django.conf import settings
import os.path
#from rango.models import User
from mainpage.models import User,Picture,Comment
#from rango.forms import UserForm, UserProfileForm
from selenium.webdriver.common.keys import Keys
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage
from datetime import datetime, timedelta


'''
class SessionTests(TestCase):
    def test_user_number_of_access_and_last_access_to_index(self):
        #Access index page 100 times
        for i in range(0, 100):
            try:
                response = self.client.get(reverse('index'))
            except:
                try:
                    response = self.client.get(reverse('mainpage:index'))
                except:
                    return False
            session = self.client.session
            # old_visists = session['visits']

            # Check it exists visits and last_visit attributes on session
            self.assertIsNotNone(self.client.session['visits'])
            self.assertIsNotNone(self.client.session['last_visit'])

            # Check last visit time is within 0.1 second interval from now
            # self.assertAlmostEqual(datetime.now(),
            #     datetime.strptime(session['last_visit'], "%Y-%m-%d %H:%M:%S.%f"), delta=timedelta(seconds=0.1))

            # Get last visit time subtracted by one day
            last_visit = datetime.now() - timedelta(days=1)

            # Set last visit to a day ago and save
            session['last_visit'] = str(last_visit)
            session.save()

            # Check if the visits number in session is being incremented and it's correct
            self.assertEquals(session['visits'], session['visits'])
            # before it was i+1 but visits shouldn't change for the same ip visited in one day
        
'''	


class ModelTests(TestCase):

	def test_user_slug(self):
		user = User(email='123@46.com', first_name = 'test' , last_name = 'user')
		user.save()
		self.assertEqual(user.slug, 'test-user')

	def test_foreignkey_match(self):
		user = User(email='123@46.com', first_name = 'test' , last_name = 'user')
		user.save()
		pic = Picture (author=user,description='text')
		pic.save()
		self.assertEqual(pic.author , user)
	
	
class ViewTests(TestCase):
	
	def test_base_template_exists(self):
		# Check base.html exists inside template folder
		path_to_base = settings.TEMPLATE_DIR + '/mainpage/base.html'
		print(path_to_base)
		self.assertTrue(os.path.isfile(path_to_base))
	
	def test_url_reference_in_index_page_when_not_logged(self):
		#Access index page with user not logged
		response = self.client.get(reverse('index'))

		self.assertIn(reverse('registration_register'), response.content.decode('ascii'))
		self.assertIn(reverse('auth_login'), response.content.decode('ascii'))
		self.assertIn(reverse('auth_password_reset'), response.content.decode('ascii'))
		
	
		
	def test_index_using_template(self):
		response = self.client.get(reverse('index'))

		# Check the template used to render index page
		self.assertTemplateUsed(response, 'mainpage/index.html')

	def test_about_using_template(self):
		self.client.get(reverse('index'))
		response = self.client.get(reverse('about'))

		# Check the template used to render about page
		self.assertTemplateUsed(response, 'mainpage/about.html')

	def test_index_picture_displayed(self):
		response = self.client.get(reverse('index'))

		# Check if is there an image in index page
		self.assertIn('img src="/static/images/index_bg.jpg'.lower(), response.content.decode('ascii').lower())
		
	def test_serving_static_files(self):
		
		result = finders.find('images/default_avatar.jpg')
		result = finders.find('images/hugo.jpg')
		result = finders.find('images/kaixin.pong')
		result = finders.find('images/mark.pong')
		result = finders.find('images/miao.pong')
		result = finders.find('images/index_bg.jpg')
		self.assertIsNotNone(result)
		
		
	def test_titles_displayed(self):
		# Create user and log in
		test_utils.create_user()
		self.client.login(username='testuser', password='test1234')

		# Access index and check the title displayed
		response = self.client.get(reverse('index'))
		self.assertIn('Home'.lower(), response.content.decode('ascii').lower())
	
	def test_url_reference_in_mainpage_page(self):
		#Create user and log in
		test_utils.create_user()
		self.client.login(email='testuser@testuser.com', password='test1234')

		# Access mainpage
		response = self.client.get(reverse('mainpage'))
		self.assertIn(reverse('about'), response.content.decode('ascii'))
		self.assertIn(reverse('profile_edit'), response.content.decode('ascii'))

	
	
	
	