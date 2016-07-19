# Udacity Data Visualization Project

## titanicViz

#### Summary

The sinking of the RMS Titanic is one of the most infamous shipwrecks in history. This dataset is based on this event. It contains 892 passengers and 10 features, 1 id column and 1 labels of survival or not for each passenger. I'll build a data visualization based on passengers' group.

#### Design

Since I've explored this dataset in the final project of [P2](https://github.com/kaiwang0112006/titanic_exploring)， I decide to show readers which group of passengers have the best chance of survival. Passengers are divided into different groups based on their class, gender and age. These three features I've discussed a lot in [P2](https://github.com/kaiwang0112006/titanic_exploring).

What I want is to let reads to explore the data. By choosing the different combination of features, they'll be able to find the survival rate of the group of people they care about. And they'll find out which group has the best chance of survival by their own. 

There're some conclusions that I want to draw audience's attention to. First, wemen have a better chance of survival then men if only we only focus on the changes of gender. There's a clear decrease of unsurvived people. And if taken the class into count, women from the first class had the best chances to survive. A sadly fact is that men in the third class have the lowest chances to survive.

Gladly Xiaoli found the some information that I want to show from her feedback and I also made a few adjustment.

According to Alvin's feedback, I added notes on the right top corner to tell audience the exact survival rate of each group.

According to Xiaoli's idea, I added adjustment to the yticks when y values has a small range.

According to Hui's advice, I add more choices in the pclass choose box.

#### Feedback

1. From Alvin Wong: "I think you can add precise number to show the exact survival rate of each group. The Animation is also rough. You should add smooth change."

2. From Xiaoli Hou: "This visualiztion shows the survival rate of different class, gender and age group. And I want to know what is “pclass” in the up-right side. I found that the Passenger calss 1 and class 2 have an higher survival rate than Passenger calss 3. The main information I learn is that it is better to buy a first class tickets in terms of high survival rate. For the problem, I should say the y ticks will have half a person(.5) when the max person count is less then 5. It's not realistic and should be removed."

3. From Hui Xu: "I really like the work. But you should tell people what data you're using. Besides, I'd also like to see the survival rate of people in both class one and class two."

#### How to see the visualization

To see the final page, one can either find it on github page at [here](https://kaiwang0112006.github.io/titanicViz/page_final/index_final.html) or [set up a local web server](http://chimera.labs.oreilly.com/books/1230000000345/ch04.html#_setting_up_a_web_server).

    $ ls
    README.md	js		page2		page_final
    data		page1		page3		pythonsrc
    
    $ python -m SimpleHTTPServer 8888
    
Then the page can be found at [http://localhost:8888/page_final/index_final.html](http://localhost:8888/page_final/index_final.html)

#### File of this project

* `pythonsrc/cleanData.py` : Script for removing missing data and output clean data for data visualization.

* `data/titanic_data.csv` : Original data.

* `data/data.csv` : clean data that used final page.

* `page_final/` : final page.

* `js/` : javascript files used by each page. viz_final.js is used by the final page.



