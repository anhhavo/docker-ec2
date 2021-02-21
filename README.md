# Assignment-2-465820

#  CSE427S- Cloud Computing and Big Data Applications

***Lab 2***

For this lab, we will learn about Docker Containers and Images.
We will dockerize the previous application :)

This is my app's IP address: 3.140.146.214

The app is running on port 5000, here is the link: [here](http://3.140.146.214:5000)

This is my DockerHub's repo [here](https://hub.docker.com/repository/docker/anhhavo/anhhavo-repo)

#### The image and tag is: anhhavo/anhhavo-repo:latest4 ###

#  Step 1: Setup Structure #
Make sure that your lab structure is setup properly like this:

Our image configuration will be recored in "conf" folder
Our app will be saved in "src" fodler. 

The structure will look like this:

![](https://github.com/CSE-427/assignment-2-anhhavo-465820/blob/master/images/path.png)


# Step 2: Setup Configuration #

We want to record our dependencies for our image. 
In order to do that, in my working directory (it can be done in lab1), I run "pip3 list" to list all the necessary version.

![](https://github.com/CSE-427/assignment-2-anhhavo-465820/blob/master/images/dependencies.png)

Now create a dependencies file "requirements.txt" in "conf" directory, and include necessary information for our layers. I figured that I do not need specific version of "fsspec" or "s3fs".

![](https://github.com/CSE-427/assignment-2-anhhavo-465820/blob/master/images/requirement.png)

# Step 3: Create Docker Image

Create a docker file "Dockerfile".

The first two lines are for our parent image and dependencies.

Our Docker parent image should be Alpine Linux (3.7). 

Copy the dependencies for our layers.

![](https://github.com/CSE-427/assignment-2-anhhavo-465820/blob/master/images/first.png)

# Step 4: Create Layers

Include all the needed layers for our image.

Firstly, I included the first two layers: python3 packages and pandas so that a foundation is formed. 
(Bring your snacks, this takes some time to build). Build then push the image to my DockerHub. 

In order to push the image, This link [here](https://stackoverflow.com/questions/48038969/an-image-does-not-exist-locally-with-the-tag-while-pushing-image-to-local-regis) is useful. 

![](https://github.com/CSE-427/assignment-2-anhhavo-465820/blob/master/images/layers.png)

From here, we can keep adding layer, build and save/push our process.

![](https://github.com/CSE-427/assignment-2-anhhavo-465820/blob/master/images/final.png)

When the final image is done, we can test our image locally by running: 
"docker run -p 5000:5000 lab2"

Or use this command if you need access to S3-Bucket.

![](https://github.com/CSE-427/assignment-2-anhhavo-465820/blob/master/images/command.png)


# Step 6: Pull image onto my EC2 Instance #

Create a new directory /lab2 in /var/www/html/
And give the directory the permission. Now pull my image onto ec2.

![](https://github.com/CSE-427/assignment-2-anhhavo-465820/blob/master/images/ec2.png)


Next, run "aws s3 ls" inside the container, using the instance profile of ec2-user.

![](https://github.com/CSE-427/assignment-2-anhhavo-465820/blob/master/images/lsdebug.png)

Now we can use "Screen command" to and launch our app :)
