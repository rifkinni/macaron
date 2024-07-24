# Running the app
1) Follow these instructions for [cloning a git repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
2) Open the `terminal` application on your mac. Copy and paste the following commands: 
```
cd macaron/
pip install flask
flask run --debug
```

3) In your web browser, go to `http://localhost:5000`. Fill out the form and click "calculate". The numbers provided are all fake for now - it will be your job to calculate them and complete the result page! 

# Exploring the code
The most relevant file to look at is `app.py`, which contains all of the logic. Open a text editor and experiment with what gets printed on the results page. (I love [sublime](https://www.sublimetext.com/) as a free text editor but there are lots of options!) 

Inside the `/templates` folder, the `form.html` file declares the inputs for the egg white form. You can style the form by adding a new `.css` file or by using inline styling in the html file. 