# probability_distribution_app
Metaculus coding challenge (back end)

Author: Luke Sabor

Challenge statement:

Metaculus coding challenge
The task is to create a probability distribution drawing web app. The app should allow users to create 
forecasts by drawing (as on paper) probability distributions. Forecasts can be saved to a database, and 
loaded for later edits and viewing. 

Create a home page listing all of the stored forecasts and add a link to a new forecast creation page.
Create a forecast drawing area on the new forecasting page and make it possible to draw probabilistic 
distributions. If the user hits the delete key, the last stroke should be removed (or last action reversed)
When the user is satisfied with their creation, they should be able to save their masterpiece to the 
database. There will need to be a field where the user can enter a title and a save button.
The user should be able to edit their forecasts, and save their changes to the database.
Add a minimal amount of CSS to your pages so that they don't look quite so bare. This doesn't need to 
be anything fancy, but it ought to be responsive and look clean. Since the design is so simple, it is 
preferred that you write the CSS (or SCSS) yourself and not rely on external frameworks (Bootstrap, etc.). 
If styling is your strength we encourage you to make it look spectacular. 
Use Django on the backend. You're free to use any frontend tools/frameworks that you like (or none at all!), 
but try to keep the code simple and well-organized.
We don’t expect you to do everything perfectly. Focus on what you consider to be the most important. 
For example you might try to figure out the math behind the distributions, or focus on solving the drawing experience. 
Let us know how you would improve the app if you had more time.

If you applied for a Front-End position. It’s not required to develop the backend, but we expect you to deliver 
a higher quality front-end experience. It’s recommended that you use d3, React and TypeScript.

For Back-End candidates we expect you to do at least a minimal version of front-end and you can focus on backend 
structure, data models, API endpoints, security, etc. It’s okay to replace the drawing area with numerical input.

For Full-Stack candidates you can find your ideal balance.

When you're done, send us a ZIP file with your working application. We should be able to run everything via 
`python manage.py runserver` or `npm run dev`. Our hope is that you'll be able to finish this within 4 hours. 
If it takes you longer, don't worry, just send us what you have so far and tell us what you would have planned to do next. 
Take a moment to think about how the app could be improved.

