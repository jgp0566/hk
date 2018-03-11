from django.db import models
import pandas as pd

class Koreans(models.Model):
    textko = models.TextField()
    def get_all_news():
        data = pd.read_csv(r'C:\Users\USER\Desktop\work\HK\scrapping\joongang1.csv', encoding='euc_kr')
        
        for i in range(0,data.textko.size):
            new_text = Koreans(textko = data.textko[i]) 
            new_text.save() 
    
    