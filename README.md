
<div align="center"><img src="assets/readme/homescreen.jpg" alt="A picture of blog_online homepage"></div>


# UX
I've created a website called 'Blog online".
This is a reddit style website where users can sign up and post/blog.
You can create a title, body(description) and upload images.
You can update any images you have personally uploaded (you cannot change other users posts).

Anyone can create an account for free and easily with the register button and immidately start posting;

<div align="center"><img src="assets/readme/registeraccount.jpg" alt="An image of register account menu"></div>

<br />

There are a lot of validation checks. Mainly when creating accounts or changing account settings.
So when you register an account if a different user has the same name or is using that specific email you wont be able to use it also.

<div align="center"><img src="assets/readme/registercheck.jpg" alt="An image showing register check (no duplication emails etc)"></div>


<br />


# Features

__Existing Features__

A fully functioning frontend that includes;
- Whilst logged in;
	- Home page
	- Account (settings)
	- Logout

- Whilst logged out;
	- Home page
	- Login
	- Register

<br />


## __While logged in__

When logged in you can post/blog with a title, description and an image.
You can further update your post (with success messages).
You can change your account settings such as change email/username or password.
Everything is in the top right nav bar;


<div align="center"><img src="assets/readme/loggedin.jpg" alt="An image showing navbar while logged in"></div>


__Create post__

There are two ways to create a post (depending on screen size).
There is only ever 1 way to post at any time.
You can create a post/blog with a title, description and an image;

<div align="center"><img src="assets/readme/createpost.jpg" alt="An image showing create post"></div>

<br />

__Edit post__

You can edit any post YOU have created and no other users;

<div align="center"><img src="assets/readme/updateblog.jpg" alt="An image showing how to update blog"></div>

<br />

__Change password__

You can update your email, and change password in accounts menu;

<div align="center"><img src="assets/readme/account.jpg" alt="An image showing change password"></div>

<br />

__Users posts__

You can view all your uploaded posts as a list on accounts. You can enter the posts and it will lead to 'update' function too.
Currently you can only view your personal uploads this way. But when and if I create it further to add friends I will add a function to enable users to see friends posts in a similar fashion.

<div align="center"><img src="assets/readme/blogposts.jpg" alt="An image showing all users posts"></div>

<br />


## __While logged out__

While logged out my website is mainly made to push people to register and log in.
There is an authentication check before trying to post or changing account settings.
You can register/sign up while logged out or alternatively you can login if you've created an account.
You can still always see other users posts.

<div align="center"><img src="assets/readme/loggedout.jpg" alt="An image showing navbar while logged out"></div>

<br />

__Reset password__

You can reset your password if forgotten. When logged out there is a reset password by login 
(currently sends it into my terminal and not directly through email).

<div align="center"><img src="assets/readme/resetpass.jpg" alt="An image showing reset password"></div>

<br />

## __While logged in or out__


__Search bar__

There is a fully functioning search bar at the top of the page. I've set it's position to fixed so it will follow the user as they scroll.
You can search for any image that's been posted and will recieve a 'nothing found' message if there is no posts that match the search.

<div align="center"><img src="assets/readme/searchbar.jpg" alt="An image showing searchbar"></div>
<br />
<div align="center"><img src="assets/readme/noresults.jpg" alt="An image showing searched no results"></div>

<br />

__Pagination__

At the bottom of the page I've implemented a Pagination system and set it currently to 3 images per page.
When you hit the bottom of the page you can jump one or more pages at a time or completely jump to the last page.
If there was hundreds/thousands of posts I would increase that number, but for now as a test I thought 3 was fine.

<div align="center"><img src="assets/readme/pagi.jpg" alt="An image showing pagination"></div>

<br />

__Validation checks__

The validation checks are when logging in to check credentials are correct.
Also when registering an account to check other users don't have the same name
lastly when registering an account to check the password isn't too weak.

<div align="center"><img src="assets/readme/validlogin.jpg" alt="An image of login in error"></div>

<div align="center"><img src="assets/readme/errorcheck.jpg" alt="An image of error checking"></div>


<br />

Theres also a password check. When you change your password it will ensure you repeat your new password twice (otherwise it will not work).
Password '1' and '2' MUST be the same;

<div align="center"><img src="assets/readme/passwordcheck.jpg" alt="An image showing password 1 and 2 are the same"></div>

<br />

# Features Left to Implement

I have a few ideas I would love to add to this project such as:

	- A like button on posts
	- A comments section on posts 
	- A friends list/add friends

Following closely to friends list (also mentioned above) I would push the ability to be able to see all of your friends posts in a list such as you can your own.

I think these features would add a great touch to the website making it a lot more interactive for users and would bring more to the blog website.

<br />

# Testing

I've tested blog online on multiple browers such as Firefox/Chrome and Microsoft edge. As well as my android phone using "Samsung internet".
To my current knowledge there are no bugs on any device or internet browser - although I'm still yet to test fully on an ipad/tablet.
The website is fully adaptable to all devices and screen sizes.

- Firefox
  - Script works as intended

- Chrome
  - Script works as intended

- Microsoft edge
  - Script works as intended

## Mobile testing

- Firefox (mobile)
  - Script works as intended

- Chrome (mobile)
  - Script works as intended

- Microsoft edge (mobile)
  - Script works as intended


# Validator Testing

All checks are passed and it's running smoothly

<div align="center"><img src="assets/readme/#" alt=""></div>


# Bugs
I've been lucky and not encountered many bugs whilst making this project.
The main bug I've encountered is images not loading correctly while debug is set to True.
I believe it to be happening because my images are being stored onto my ide and not online.
Further tests will need to pursue before potentially running in production mode.


<div align="center"><img src="assets/readme/pictureerror.jpg" alt="An error of pictures/uploads not working correctly"></div>


# Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - <https://github.com/Jordan-Finlay/blog_online>


## Local deployment

- I've downloaded a copy of my wedding checker script onto my computer and am able to access it through local deployment to change and mess around with the overall code and layout/structure for better user experience. I've also installed python that allows me to work on my code as if it was running through code anywhere.


<div align="center"><img src="assets/readme/local.jpg" alt="An error of pictures of local development on my pc"></div>


# Credits

__Content__

- I used google for some images and pixabay for a few others - https://pixabay.com/images/search/logo/
- Other than that, I've not used any third parties for any logos/design/pictures etc

