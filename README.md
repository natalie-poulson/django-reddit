# Django Reddit Clone Challenge!

We are going to spend the weekend creating a clone of the message board site / forum / garbageheap site [Reddit](www.reddit.com).  Your Django application should have the following:

**Models:**
1. Users (standard Django auth user)
  - email
  - password
  - username
  
1.5 Profile: a user has one profile (User - Profile ) 
  -  profile_pic
  -  user (FK)
  
2. Posts: a post has one User
  - created_at
  - title
  - picture
  - content
  - site_url
  - vote_total
  - user (FK) 
  
3. Comments: a post has many comments
  - created_at
  - content
  - vote_total
  - user(FK)
  - post(FK)
  
3.5. Save: a user has many Saves with Post as a foreign key ( User < Save > Post )
  - user(FK)
  - post(FK)
  - created_at
  
4. Post_Votes: a post has many post_votes through Users ( User < Post_Votes > Post )
  - user(FK)
  - post(FK)
  - value ( choice of -1 or +1)
  
5. Comment_Votes: a comment has many comment_votes through Users ( User < Comment_Votes > Comment )
  - user(FK)
  - comment(FK)
  - value ( choice of -1 or +1)

6. Comments on Comments: a comment has many comments (Comment < Comment )
  - +comment(FK)
  
7. Moderator: A user can be a moderator (User - Moderator)
  - user(FK)


**Views:**

> Sprint 1: MVP
1. All posts (posts)
1. View 1 Post w/ comments (posts/<int:pk>)
1. Registration
1. Login
1. Create Post (posts/new)
1. Create Comment (associated with a post) (posts/<int:pk/comments/new)

> Sprint 2: Gettin Trolly
1. Add Votes for Post (jquery feature)
1. Add Votes for Comment (jquery feature)
1. Save Posts (jquery feature)
1. View Saved Posts (user/<int:pk>/saved)
1. Create Comment on Comments (posts/<int:pk>/comments/<int:cpk>/new)

> Sprint 3: Wrangling the Herd
1. Add moderation
1. subreddits? lol, good luck
