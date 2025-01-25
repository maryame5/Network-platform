Network Platform

A social network web application built using Python, JavaScript, HTML, and CSS. The platform allows users to make posts, follow other users, and "like" posts. Below is a detailed breakdown of the features implemented.

Features

1. New Post

Users who are signed in can write a new text-based post by:

Filling in text into a text area.

Clicking a button to submit the post.

The "New Post" box is displayed at the top of the "All Posts" page for convenience. Alternatively, this feature can be accessed on a separate page.

2. All Posts

The "All Posts" link in the navigation bar directs users to a page displaying all posts from all users, ordered by the most recent posts first.

Each post includes:

The username of the poster.

The post content.

The date and time of posting.

The number of likes the post has received (initially set to 0).

3. Profile Page

Clicking on a username navigates to that user’s profile page, which displays:

The number of followers the user has.

The number of people the user follows.

All posts made by the user, in reverse chronological order.

For other users’ profiles, a "Follow" or "Unfollow" button is available for toggling the follow status. Users cannot follow themselves.

4. Following

The "Following" link in the navigation bar takes users to a page displaying posts from users they follow.

This page behaves like the "All Posts" page but shows a filtered list of posts.

Accessible only to signed-in users.

5. Pagination

All pages displaying posts include pagination to enhance usability:

A maximum of 10 posts per page.

A "Next" button appears if more than 10 posts exist.

A "Previous" button appears when not on the first page.

6. Edit Post

Users can edit their own posts by:

Clicking an "Edit" button/link on their post.

A textarea replaces the post content for editing.

A "Save" button updates the post asynchronously using JavaScript.

Users cannot edit posts created by others.

7. Like and Unlike

Users can toggle the "like" status of any post by clicking a button/link.

The like count updates asynchronously using JavaScript without reloading the page.

Technologies Used

Backend: Python (Django framework)

Frontend: HTML, CSS, JavaScript

Database: SQLite (default Django database, easily replaceable with PostgreSQL or others)

API Communication: Fetch API for asynchronous actions (like editing posts and updating likes)
