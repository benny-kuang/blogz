# blogz
http://education.launchcode.org/web-fundamentals/assignments/blogz
- Flask based app implements blog.  
- Builds upon build-a-blog assignment.  Refactor to expand our codebase to make this a multi-user blog site.  Add authentication, users will have own blog pages, vistors can view blogs by authors, or view all blog posts on the site.  We will still maintain the ability to view individual blog entry.
 # Changes to Build A Blog
- Make a Home Page ("/" or "/blog")
    - Display all blog users
- Registered User Integration
    - Add following templates: signup.html, login.html, index.html
    - Add the following route handler functions: signup, login, and index.
    - ~~Add a User class~~
    - Add a logout function
        - Handles a POST request to /logout and redirects user to /blog after deleting user from session
- Create Dynamic User Pages
    - Add a singleUser.html template that will be used to display only the blogs associated with a single given author. It will be used when we dynamically generate a page using a GET request with a user query parameter on the /blog route (similar to how we dynamically generated individual blog entry pages in the last assignment).


# Bonus Missions
- Add Pagination
- Add Hashing 
# User Scenarios
## Scenario A: Not Logged In
- **Given** Anonymous Visitor (not logged in)
- **When** Arrive at the site (route "/")
- **Then** See list of blog users
    - **If** Visitor clicks All Posts
         - **Then** See list of previous posts by registered users
    - **If** Visitor clicks New Post
        - **Then** Visitor is redirected to Log In page
    - **If** Visitor clicks Log In
        - **And** Arrive at Login Page
 
## Scenario B: Logged In
- **Given** Registerd User (logged in)
- **When** Arrive at the site (route "/")
- **Then** See list of previous blog entries by registered users



