# Haochong-week2-mini-repo
This is a repo template for course 706_Data_Engineering Week 2 Mini Project. First of all, I search on gooogle to find a csv. Secondly, I define a simple function called "Describe" to return the descriptive statistics of the dataset. After that, I use the Colab to print the data and then use assert in the test.py to test mmy function. Finally, I use Action to run Makefile and got a 100% pass. 

# Purpose
To do an extension base on week 1 by making a python template and generate descriptive statistics on datasets using Pandas. 

## Preparation 
1. open codespaces 
2. open Colab
3. wait for container to be built with requiremnts.txt installed

# Check format and test errors
1.Format code make format
2.Lint code make lint
3.Test code make test
First time I got this.
<img width="651" alt="截屏2023-09-08 下午1 51 53" src="https://github.com/nogibjj/Haochong-Xia-Week-2/assets/89813704/a222f5d3-69d8-4260-a5a5-b7ba46354f2b">
At the beginning, I thought it was because of the round up decimal. Hence, I comment the second assert but got the same test result. Then, I search "Error 5" on google and got this:https://zditect.com/blog/30980196.html , but I don't think I have this problem. After checking with all my document again, I noticed that I accidentally wrote the test_ format as Test_. After fixing this, I got all pass.
<img width="598" alt="截屏2023-09-08 下午1 57 13" src="https://github.com/nogibjj/Haochong-Xia-Week-2/assets/89813704/b46b613c-47f5-4c16-b03e-713fea05d619">

