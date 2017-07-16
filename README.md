# blogz
http://education.launchcode.org/web-fundamentals/assignments/blogz
- Flask based app implements blog.  
- Builds upon build-a-blog assignment.  Refactor to expand our codebase to make this a multi-user blog site.  Add authentication, users will have own blog pages, vistors can view blogs by authors, or view all blog posts on the site.  We will still maintain the ability to view individual blog entry.
# Overview of Improvements
- Add following templates: signup.html, login.html, index.html
- Add a singleUser.html template that will be used to display only the blogs associated with a single given author. It will be used when we dynamically generate a page using a GET request with a user query parameter on the /blog route (similar to how we dynamically generated individual blog entry pages in the last assignment).
- Add the following route handler functions: signup, login, and index.
- Add logout function that handles a POST request to /logout and redirects the user to /blog after deleting the username from the session.
- Add a User class to make all this new functionality possible, which is what we'll tackle next after a brief explanation of use cases.
# Functionality Check (midway check)
After adding user class, adding login and signup pages, adding logout function and navigation, and adding a login requirement, the following functionality should be included in app:
- User is logged in and adds a new blog post, then is redirected to a page featuring the individual blog entry they just created (as in Build-a-Blog).
- User visits the /blog page and sees a list of all blog entries by all users.
- User clicks on the title of a blog entry on the /blog page and lands on the individual blog entry page.
- User clicks "Logout" and is redirected to the /blog page and is unable to access the /newpost page (is redirected to /login page instead)
# Final Steps
- Make a Home Page
- Create Dynamic User Pages
# Bonus Missions
- Add Pagination
- Add Hashing
