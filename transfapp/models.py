from django.db import models
import pandas as pd

class Koreans(models.Model):
    textko = models.TextField()
    textidx = models.IntegerField(default=0)
    
    def get_all_news():
        data = pd.read_csv(r'C:\Users\USER\Desktop\work\HK\scrapping\joongang1.csv', encoding='utf')
        
        for i in range(0,data.textko.size):
            new_text = Koreans(textidx = i, textko = data.textko[i]) 
            new_text.save() 
    
    