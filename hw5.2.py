import urllib.request

import os
import re
import urllib.error
def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf-8')
   


        regPostTitle = re.compile('<title>.*? </title>', flags= re.DOTALL)
        titles = regPostTitle.findall(text)
        regTag = re.compile('<.*?>', re.DOTALL)
        regSpace = re.compile('\s{2,}', re.DOTALL)
        for t in titles:
            clean_t = regSpace.sub("", t)
            clean_t = regTag.sub("", clean_t)


        regAuthor = re.compile('<span class="createdby">.*?</span>', flags= re.DOTALL)
        author = regAuthor.findall(text)
        regTag1 = re.compile('<.*?>', re.DOTALL)
        regSpace1 = re.compile('\s{2,}', re.DOTALL)
        regDescr1 = re.compile('Автор: ', re.DOTALL)
        for a in author:
            clean_a = regSpace1.sub("", a)
            clean_a = regTag1.sub("", clean_a)
            clean_a = clean_a.replace("Автор: ", "")
##            clean_a = regDescr1.sub("", clean_a)
     
        regDate = re.compile('<span class="modified">.*?</span>', flags= re.DOTALL)
        date = regDate.findall(text)
        regTag1 = re.compile('<.*?>', re.DOTALL)
        regSpace1 = re.compile('\s{2,}', re.DOTALL)
##        regDescr1 = re.compile('Обновлено ', re.DOTALL)
        for d in date:
            clean_d = regSpace1.sub("", d)
            clean_d = regTag1.sub("", clean_d)
            clean_d = clean_d.replace("Обновлено ", "")
##            clean_d = regDescr1.sub("", clean_d)
    
 
        regText = re.compile("""<p style="text-align: justify;">.*?</p>""", flags= re.DOTALL)
        plaintxt = regText.findall(text)
        newtxt = []
        regTag = re.compile('<.*?>', re.DOTALL)
        regSpace = re.compile('\s{2,}', re.DOTALL)
        for p in plaintxt:
            clean_p = regSpace.sub("", p)
            clean_p = regTag.sub("", clean_p)
            newtxt.append(clean_p)
        for l in newtxt:
            l = l.replace("&nbsp;", " ")
        with open('newspaper/article.txt', 'a', encoding="utf-8") as f:
            f.write('@au', clean_a)
            f.write('\n')
            f.write('@ti', clean_t)
            f.write('\n')
            f.write('@da', clean_d)
            f.write('\n')
            f.write(l)

            
            
##        print('@au', clean_a)
##
##        print('@ti', clean_t)
##
##        print('@da', clean_d)


    
    
    

        data = 'path\t%s\t\t%s\t%s\tпублицистика\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t нейтральный\tn-возраст\tn-уровень\tгородская\t%s\tРославльская правда\t%s\tгазета\tРоссия\tРославль\tru' % (clean_a, clean_t, clean_d, pageUrl, clean_d[6:])
        fieldnames = ['path', 'author', 'sex', 'birthday', 'header', 'created', 'sphere', 'genre_fi', 'type', 'topic', 'chronotop', 'style', 'audience_age', 'audience_level', 'audience_size', 'source', 'publication', 'publisher', 'publ_year', 'medium', 'country', 'region', 'language']

            
        with open('newspaper/metadata14.csv', 'a',encoding="utf-8") as f:
            f.write('\t'.join(fieldnames) + '\n')
            f.write(data + '\n')
##        with open('article.txt', 'w', encoding="utf-8") as f:

##            f.write('@url', pageUrl)
##            f.write('\n')
##            f.write(clean_p)

    except:
        print('Error at', pageUrl)
        return



 

commonUrl = 'http://ropravda.ru/index.php/'
cat = ['roslavl-i-roslavlchane','delovaya-zhizn', 'mestnoe-samoupravlenie', 'selo-rodnoe', 'obrazovanie', 'kultura', 'sport', 'kraevedenie', 'roslavl-pravoslavnyj', 'tvorchestvo-nashikh-zemlyakov', 'proisshestviya', 'sotsialnaya-sfera', 'raznoe']
for c in cat:
    for i in range(1000, 1600):
        pageUrl = commonUrl + c + '/'+ str(i) 
        download_page(pageUrl)



