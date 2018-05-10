# PDSB Final Project
## Final Reflections
Alexander M. Procton

__Now that you have seen many full research projects saved online as GitHub repositories do you plan to use GitHub for your future projects as a way to store code and data in the cloud and to share your progress with others?__

Yes, I have really enjoyed learning to use Git and Github and will definitely be using GitHub repos to store and share code for future projects. I realize I have a lot to learn with Git, but the convenience of being able to demonstrate a project anywhere at anytime using GitHub and Jupyter nbviewer is awesome.

__Did you project accomplish the goals that you set out for yourself in your proposal? If not, why? What was the hardest problem in your project that were able to overcome? What, if any, was a problem that you were unable to overcome in your project within the given time?__

I accomplished the main goal that I set out for myself: creating a Python package for converting sequential behavior data into social networks for reproducible science, but I was not able to implement a few features I had planned, including the ability to merge behaviors to create a composite column. I decided that this was a convenient utility but not essential to my project.

I also was not able to implement just-in-time compiling using numba, although I coded three functions, `partner_split()`, `subjtime()`, and `matrix()` that only used numpy arrays. I did not anticipate how finicky numba would be about the `dtype` of numpy arrays, so I decided to leave the `jit()` decorators off the code for now. Writing functions for numba that only used numpy arrays and no dictionaries or dataframes was definitely the most difficult part of my code.

__Do you feel that you've learned the skills necessary perform data analysis in Python, and to write your own program or pipeline for data analysis? What skills do you think you need to work on further, and where would you look to find more information about learning these skills?__

Yes, I have definitely learned the skills necessary to perform many analyses, as well as the ability to work in Jupyter notebooks, which makes trying out new packages and saving methods that work easier. I am now researching which tools for network science in Python are the best, because each tool does some things well but not others. For example, igraph has much better, more intuitive graphics than networkx.

PS - Deren, I used a ton of these skills for my project for the Data Incubator, and made it to the finalist round! Thanks for all the advice. The repo is [here](https://github.com/aprocton/climber-net) if you're interested in seeing how it's turned out so far. I'll be working more on it this weekend and hopefully making it more interactive/hosted on Bokeh, too.