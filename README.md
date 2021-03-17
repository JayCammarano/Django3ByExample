Following along with Antonio Melé - Django 3 By Example: Build powerful and reliable Python web applications from scratch (3 ed)

# Projects include: 
  - Blog site
     - Add posts from an admin dashboard
     - Share posts via email
     - Add comments from the blog page, hide/show from admin page
     - Tag posts and view similar posts based on number of tags in common
     - Blog posts support markdown formatting
     - Includes sitemap and rss feeds
     - Search functionality using trigram similarity in the words of the title
  - Social image bookmarking site
     - Authentication: login, logout, sign up, password reset + change
     - Authenticate with username or email
     - Edit user's profile to include date of birth and profile pic
  - Online shop
  - E-learning platform

# Major Modifications:
 - Creating one site with multiple apps instead of 4 separate sites

# Dependancies:
Most dependancies are contained in the Pipfile, except:
For image handling with Pillow:
 - Zlib
 - libjpeg