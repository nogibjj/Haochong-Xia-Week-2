# Haochong-week2-mini-repo [![CI](https://github.com/nogibjj/Haochong-Xia-Week-2/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Haochong-Xia-Week-2/actions/workflows/ci.yml)
This is a repo template for course 706_Data_Engineering Week 2 Mini Project. First of all, I search on gooogle to find a csv. Secondly, I define functions called "Describe" and "get_median" to return the descriptive statistics of the dataset. After that, I use the Colab to print the data and plot histagrams and then use assert in the test.py to test my function. Finally, I use Action to run Makefile and got a 100% pass. 

# Purpose
To do an extension base on week 1 by making a python template and generate descriptive statistics and visualization on datasets using Pandas. 

## Preparation 
1. open codespaces 
2. open Colab
3. wait for container to be built with requiremnts.txt installed

## Check format and test errors
1. Format code `make format`
   <img width="974" alt="截屏2023-09-10 下午3 43 18" src="https://github.com/nogibjj/Haochong-Xia-Week-2/assets/89813704/fd210688-7317-4f5e-bd81-fba58e7c2899">

2. Lint code `make lint`
3. Test code `make test`
First time I got this.
<img width="651" alt="截屏2023-09-08 下午1 51 53" src="https://github.com/nogibjj/Haochong-Xia-Week-2/assets/89813704/a222f5d3-69d8-4260-a5a5-b7ba46354f2b">

At the beginning, I thought it was because of the round up decimal. Hence, I comment the second assert but got the same test result. Then, I search "Error 5" on google and got this:https://zditect.com/blog/30980196.html , but I don't think I have this problem. After checking with all my document again, I noticed that I accidentally wrote the test_ format as Test_. After fixing this, I got all pass.
<img width="598" alt="截屏2023-09-08 下午1 57 13" src="https://github.com/nogibjj/Haochong-Xia-Week-2/assets/89813704/b46b613c-47f5-4c16-b03e-713fea05d619">
<img width="662" alt="截屏2023-09-10 下午3 49 46" src="https://github.com/nogibjj/Haochong-Xia-Week-2/assets/89813704/b588e18d-4414-487e-b85c-6a90ca4c8d67">

## Visualization
Two histagrams of two data in the dataframe can be visualized by `PlotShapeLeng` and `PlotShapeArea` and here are them:
<img width="858" alt="截屏2023-09-10 下午3 37 14" src="https://github.com/nogibjj/Haochong-Xia-Week-2/assets/89813704/1956d33a-071a-4feb-9880-5d2da6a6a6ed">
<img width="858" alt="截屏2023-09-10 下午3 37 38" src="https://github.com/nogibjj/Haochong-Xia-Week-2/assets/89813704/ca8fe507-0eb7-4296-9cbe-3246d9fc81df">

## Summary statistics
Summary reports can be generated by ydata-profiling by using `test_generate_summary_report()` in test_main.py. Here are them:
Describe:
<img width="283" alt="截屏2023-09-10 下午3 41 12" src="https://github.com/nogibjj/Haochong-Xia-Week-2/assets/89813704/80795732-336a-4c0b-8a54-f0ff7b9577fe">
Median:
<img width="240" alt="截屏2023-09-10 下午3 42 02" src="https://github.com/nogibjj/Haochong-Xia-Week-2/assets/89813704/ed98e4d1-d6da-42a8-9e2b-bed63f98bf61">







