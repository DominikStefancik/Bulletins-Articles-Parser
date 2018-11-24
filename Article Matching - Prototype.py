
# coding: utf-8

# In[450]:


import pandas as pd
pd.set_option('display.max_colwidth', 200)
import os
import re
import math


# In[567]:


anker_words_countries = [ "Afghanistan", "Afghanistan", "Afghanestan", "South-Central", "Asia", "Albania", "Albanie", "Shqiperia", "Southern", "Europe", "Algeria", "Algérie", "Jaza'ir", "Northern", "Africa", "American", "Samoa", "Samoa", "Américaines", "American", "Samoa", "Polynesia,", "Oceania", "Andorra", "Andorre", "Andorra", "Southern", "Europe", "Angola", "Angola", "Angola", "Central", "Africa", "Anguilla", "Anguilla", "Anguilla", "Leeward", "Islands,", "Caribbean", "Antarctica", "Antarctique", "Antarctica", "Antarctica", "Antigua", "Barbuda", "Antigua-et-Barbuda", "Antigua", "Barbuda", "Leeward", "Islands,", "Caribbean", "Argentina", "Argentine", "Argentina", "Southern", "South", "America", "Armenia", "Arménie", "Hayastan", "Western", "Asia", "Aruba", "Aruba", "Aruba", "Leeward", "Islands,", "Caribbean", "Australia", "Australie", "Australia", "Australia/Oceania", "Austria", "Autriche", "Österreich", "Western", "Europe", "Azerbaijan", "Azerbaïdjan", "Azarbaycan", "Caucasus,", "Western", "Asia", "Bahamas", "Bahamas", "Bahamas", "Caribbean", "Bahrain", "Bahreïn", "Bahrayn", "Arabian", "Peninsula,", "Middle", "East", "Bangladesh", "Bangladesh", "Bangladesh", "South-Central", "Asia", "Barbados", "Barbade", "Barbados", "Lesser", "Antilles,", "Caribbean", "Belarus", "Bélarus", "Byelarus", "Eastern", "Europe", "Belgium", "Belgique", "Belgique/Belgie", "Western", "Europe", "Belize", "Belize", "Belize", "Central", "America", "Benin", "Bénin", "Benin", "West", "Africa", "Bermuda", "Bermudes", "Bermuda", "North", "America", "Bhutan", "Bhoutan", "Bhutan", "South-Central", "Asia", "Bolivia", "Bolivie", "Bolivia", "Central", "South", "America", "Bosnia", "Herzegovina", "Bosnie-Herzégovine", "Bosna", "Hercegovina", "Southern", "Europe", "Botswana", "Botswana", "Botswana", "Southern", "Africa", "Brazil", "Brésil", "Brasil", "Central", "Eastern", "South", "America", "Brunei", "Darussalam", "Brunéi", "Darussalam", "Negara", "Brunei", "Darussalam", "Southeast", "Asia", "Bulgaria", "Bulgarie", "Bulgaria", "Balkan,", "Eastern", "Europe", "Burkina", "Faso", "Burkina", "Faso", "Burkina", "Faso", "West", "Africa", "Burundi", "Burundi", "Burundi", "Eastern", "Africa,", "African", "Great", "Lakes", "Cambodia", "Cambodge", "Kampuchea", "South-East", "Asia", "Cameroon", "Cameroun", "Cameroon", "Central", "Africa", "Canada", "Canada", "Canada", "North", "North", "America", "Cape", "Verde", "Cap-Vert", "Cabo", "Verde", "West", "Africa", "Cayman", "Islands", "Caïmanes,", "Îles", "Cayman", "Islands", "Greater", "Antilles,", "Caribbean", "Central", "African", "Republic", "Centrafricaine,", "République", "Republique", "Centrafricaine", "Central", "Africa", "Chad", "Tchad", "Tchad", "Central", "Africa", "Chile", "Chili", "Chile", "Western", "South", "America", "China", "Chine", "Zhong", "Guo", "Eastern", "Asia", "Christmas", "Island", "Île", "Christmas", "Christmas", "Island", "Southeast", "Asia", "Cocos", "Keeling", "Islands", "Îles", "Cocos", "Keeling", "Cocos", "Keeling", "Islands", "South-East", "Asia,", "Australia", "Colombia", "Colombie", "Colombia", "North", "West", "South", "America", "Comoros", "Comores", "Comores", "Eastern", "Africa", "Democratic", "Republic", "Congo", "Kinshasa", "Congo,", "République", "Démocratique", "République", "Démocratique", "Congo", "Central", "Africa", "Congo,", "Republic", "Brazzaville", "République", "Congo", "République", "Congo", "Central", "Africa", "Cook", "Islands", "Îles", "Cook", "Cook", "Islands", "Polynesia,", "Oceania", "Costa", "Rica", "Costa", "Rica", "Costa", "Rica", "Central", "America", "Côte", "D'ivoire", "Ivory", "Coast", "Côte", "D'ivoire", "Cote", "d'Ivoire", "West", "Africa", "Croatia", "Croatie", "Hrvatska", "Southern", "Europe", "Cuba", "Cuba", "Cuba", "Greater", "Antilles,", "Caribbean", "Cyprus", "Chypre", "Kibris,", "Kypros", "Mediterranean,", "Western", "Asia", "Czech", "Republic", "République", "Tchèque", "Ceska", "Republika", "Eastern", "Europe", "Denmark", "Danemark", "Danmark", "Northern", "Europe", "Djibouti", "Djibouti", "Djibouti", "Eastern", "Africa", "Dominica", "Dominique", "Dominica", "Lesser", "Antilles,", "Caribbean", "Dominican", "Republic", "Dominicaine,", "République", "Dominicana,", "Republica", "Greater", "Antilles,", "Caribbean", "East", "Timor", "Timor-Leste", "Timor-Leste", "Timor", "Oriental", "Timor", "South-East", "Asia", "Ecuador", "Équateur", "Ecuador", "North", "West", "South", "America", "Egypt", "Égypte", "Misr", "Africa,", "Middle", "East", "Salvador", "Salvador", "Salvador", "Central", "America", "Equatorial", "Guinea", "Guinée", "Équatoriale", "Guinea", "Ecuatorial", "Central", "Africa", "Eritrea", "Érythrée", "Hagere", "Ertra", "Eastern", "Africa", "Estonia", "Estonie", "Eesti", "Vabariik", "Northern", "Europe", "Ethiopia", "Éthiopie", "Ityop'iya", "Eastern", "Africa", "Falkland", "Islands", "Falkland,", "Îles", "Malvinas", "Islas", "Malvinas", "Southern", "South", "America", "Faroe", "Islands", "Îles", "Féroé", "Foroyar", "Northern", "Europe", "Fiji", "Fidji", "Fiji", "Melanesia,", "Oceania", "Finland", "Finlande", "Suomen", "Tasavalta", "Northern", "Europe", "France", "France", "France", "Western", "Europe", "French", "Guiana", "Guyane", "Française", "Guyane", "Northern", "South", "America", "French", "Polynesia", "Polynésie", "Française", "Polynésie", "Française", "Polynesia,", "Oceania", "French", "Southern", "Territories", "Terres", "Australes", "Françaises", "Terres", "Australes", "Antarctiques", "Françaises", "Southern", "South", "America,", "Antarctic", "Gabon", "Gabon", "Gabon", "Central", "Africa", "Gambia", "Gambie", "Gambia", "West", "Africa", "Georgia", "Géorgie", "Sak'art'velo", "Western", "Asia", "Germany", "Allemagne", "Deutschland", "Western", "Europe", "Ghana", "Ghana", "Ghana", "West", "Africa", "Gibraltar", "Gibraltar", "Gibraltar", "Southern", "Europe", "Great", "Britain", "Grande-Bretagne", "Great", "Britain", "Northern", "Europe", "Greece", "Grèce", "Ellas", "Ellada", "Southern", "Europe", "Greenland", "Groenland", "Kalaallit", "Nunaat", "North", "America", "Grenada", "Grenade", "Grenada", "Lesser", "Antilles,", "Caribbean", "Guadeloupe", "Guadeloupe", "Guadeloupe", "Lesser", "Antilles,", "Caribbean", "Guam", "Guam", "Guam", "Micronesia,", "Oceania", "Guatemala", "Guatemala", "Guatemala", "Central", "America", "Guinea", "Guinéee", "Guinee", "West", "Africa", "Guinea-Bissau", "Guinée-Bissau", "Guine-Bissau", "West", "Africa", "Guyana", "Guyana", "Guyana", "North", "Eastern", "South", "America", "Haiti", "Haïti", "Haiti", "Greater", "Antilles,", "Caribbean", "Holy", "See", "Saint-Siège", "État", "Cité", "Vatican", "Status", "Civitatis", "Vaticanæ", "Southern", "Europe", "within", "Italy", "Honduras", "Honduras", "Honduras", "Central", "America", "Hong", "Kong", "Hong-Kong", "Xianggang", "Eastern", "Asia", "Hungary", "Hongrie", "Magyarorszag", "Eastern", "Europe", "Iceland", "Islande", "Lyoveldio", "Island", "Northern", "Europe", "India", "Inde", "Bharat", "South-Central", "Asia", "Indonesia", "Indonésie", "Indonesia", "Maritime", "South-East", "Asia", "Iran", "Islamic", "Republic", "République", "Islamique", "d'", "Iran", "Iran", "South-Central", "Asia", "Iraq", "Iraq", "Iraq", "Middle", "East,", "Western", "Asia", "Ireland", "Irlande", "Éire", "Northern", "Europe", "Israel", "Israël", "Yisra'el", "Middle", "East,", "Western", "Asia", "Italy", "Italie", "Italia", "Southern", "Europe", "Ivory", "Coast", "Côte", "D'ivoire", "Cote", "d'Ivoire", "West", "Africa", "Jamaica", "Jamaïque", "Jamaica", "Greater", "Antilles,", "Caribbean", "Japan", "Japon", "Nippon", "Eastern", "Asia", "Jordan", "Jordanie", "Urdun", "Middle", "East,", "Western", "Asia", "Kazakhstan", "Kazakstan", "Qazaqstan", "Central", "Asia", "Kenya", "Kenya", "Kenya", "Eastern", "Africa", "Kiribati", "Kiribati", "Kiribati,", "Kiribas", "Micronesia,", "Oceania", "Korea,", "Democratic", "People's", "Rep.", "North", "Korea", "Corée,", "République", "Populaire", "Démocratique", "Choson", "Eastern", "Asia", "Korea,", "Republic", "South", "Korea", "Corée,", "République", "Han-guk", "Eastern", "Asia", "Kosovo", "Kosovo", "Albanian:", ":", "Kosova", "Kosovë,", "Serbian:", "Kosovo,", "Косово", "Southern", "Europe", "Kuwait", "Koweït", "Kuwayt", "Middle", "East,", "Western", "Asia", "Kyrgyzstan", "Kirghizistan", "Kyrgyz", "Respublikasy", "Central", "Asia", "Lao,", "People's", "Democratic", "Republic", "Lao,", "République", "Démocratique", "Populaire", "Lao", "South-East", "Asia", "Latvia", "Lettonie", "Latvija", "Northern", "Europe", "Lebanon", "Liban", "Lubnan", "Middle", "East,", "Western", "Asia", "Lesotho", "Lesotho", "Lesotho", "Southern", "Africa", "Liberia", "Libéria", "Liberia", "West", "Africa", "Libya", "Libye", "Libiyah", "Northern", "Africa", "Liechtenstein", "Liechtenstein", "Liechtenstein", "Western", "Europe", "Lithuania", "Lituanie", "Lietuva", "Northern", "Europe", "Luxembourg", "Luxembourg", "Luxembourg,", "Letzebuerg", "Western", "Europe", "Macau", "Macao", "Aomen", "Eastern", "Asia", "Macedonia,", "Rep.", "Macédoine,", "l'ex-République", "Yougoslave", "Makedonija", "Southern", "Europe", "Madagascar", "Madagascar", "Madagascar", "Eastern", "Africa", "Malawi", "Malawi", "Malawi", "Eastern", "Africa", "Malaysia", "Malaisie", "Malaysia", "Southeast", "Asia", "Maldives", "Maldives", "Dhivehi", "Raajje", "South-Central", "Asia", "Mali", "Mali", "Mali", "West", "Africa", "Malta", "Malte", "Malta", "Southern", "Europe", "Marshall", "Islands", "Îles", "Marshall", "Marshall", "Islands", "Micronesia,", "Oceania", "Martinique", "Martinique", "Martinique", "Lesser", "Antilles,", "Caribbean", "Mauritania", "Mauritanie", "Muritaniyah", "West", "Africa", "Mauritius", "Île", "Maurice", "Mauritius", "Eastern", "Africa", "Mayotte", "Mayotte", "Mayotte", "Eastern", "Africa", "Mexico", "Mexique", "Estados", "Unidos", "Mexicanos", "North", "America", "Micronesia,", "Federal", "States", "États", "Fédérés", "Micronésie", "Micronesia", "Micronesia,", "Oceania", "Moldova,", "Republic", "Moldova,", "République", "Moldova", "Eastern", "Europe", "Monaco", "Monaco", "Monaco", "Southern", "Europe", "Mongolia", "Mongolie", "Mongol", "Uls", "Eastern", "Asia", "Montenegro", "Monténégro", "Crna", "Gora", "Southern", "Europe", "Montserrat", "Montserrat", "Montserrat", "Lesser", "Antilles,", "Caribbean", "Morocco", "Maroc", "Maghrib", "Northern", "Africa", "Mozambique", "Mozambique", "Mocambique", "Eastern", "Africa", "Myanmar,", "Burma", "Myanmar,", "Birmanie", "Myanma", "Naingngandaw", "Southeast", "Asia", "Namibia", "Namibie", "Namibia", "Southern", "Africa", "Nauru", "Nauru", "Nauru", "Micronesia,", "Oceania", "Nepal", "Népal", "Nepal", "South-Central", "Asia", "Netherlands", "Pays-Bas", "Nederland/Holland", "Western", "Europe", "Netherlands", "Antilles", "Antilles", "Néerlandaises", "Nederlandse", "Antillen", "Caribbean", "New", "Caledonia", "Nouvelle-Calédonie", "Nouvelle-Calédonie", "Melanesia,", "Oceania", "New", "Zealand", "Nouvelle-Zélande", "Aotearoa", "Oceania;", "Australia", "Nicaragua", "Nicaragua", "Nicaragua", "Central", "America", "Niger", "Niger", "Niger", "West", "Africa", "Nigeria", "Nigéria", "Nigeria", "West", "Africa", "Niue", "Nioué", "Niue", "Polynesia,", "Oceania", "Northern", "Mariana", "Islands", "Îles", "Mariannes", "Nord", "Northern", "Mariana", "Islands", "Micronesia,", "Oceania", "Norway", "Norvège", "Norge", "Northern", "Europe", "Oman", "Oman", "Saltanat", "Uman", "Middle", "East", "Pakistan", "Pakistan", "Pakistan", "South-Central", "Asia", "Palau", "Palaos", "Belau", "Micronesia,", "Oceania", "Palestinian", "territories", "Autorité", "Nationale", "Palestinienne", "Filastin", "Middle", "East,", "Western", "Asia", "Panama", "Panama", "Panama", "Central", "America", "Papua", "New", "Guinea", "Papouasie-Nouvelle-Guinée", "Papua", "Niu", "Gini", "Maritime", "Southeast", "Asia,", "Melanesia,", "Oceania", "Paraguay", "Paraguay", "Paraguay", "Central", "South", "America", "Peru", "Pérou", "Peru", "Western", "South", "America", "Philippines", "Philippines", "Pilipinas", "Southeast", "Asia", "Pitcairn", "Island", "Pitcairn", "Pitcairn", "Island", "Polynesia,", "Oceania", "Poland", "Pologne", "Polska", "Eastern", "Europe", "Portugal", "Portugal", "Portugal", "Southern", "Europe", "Puerto", "Rico", "Porto", "Rico", "Puerto", "Rico", "Greater", "Antilles,", "Caribbean", "Qatar", "Qatar", "Dawlat", "Qatar", "Arabian", "Peninsula,", "Middle", "East", "Reunion", "Island", "Ile", "Réunion", "Ile", "Réunion", "Eastern", "Africa", "Romania", "Roumanie", "Romania", "Eastern", "Europe", "Russian", "Federation", "Russie,", "Fédération", "Rossiya", "Eastern", "Europe", "Northern", "Asia", "Rwanda", "Rwanda", "Rwanda", "Eastern", "Africa,", "African", "Great", "Lakes", "Saint", "Kitts", "Nevis", "Saint-Kitts-et-Nevis", "Lesser", "Antilles,", "Caribbean", "Saint", "Lucia", "Sainte-Lucie", "Saint", "Lucia", "Lesser", "Antilles,", "Caribbean", "Saint", "Vincent", "Grenadines", "Saint-Vincent-et-les", "Grenadines", "Lesser", "Antilles,", "Caribbean", "Samoa", "Samoa", "Samoa", "Polynesia,", "Oceania", "San", "Marino", "Saint-Marin", "San", "Marino", "Southern", "Europe", "within", "Italy", "Sao", "Tome", "Principe", "Sao", "Tomé-et-Principe", "Sao", "Tome", "Principe", "Central", "Africa", "Saudi", "Arabia", "Arabie", "Saoudite", "Arabiyah", "Suudiyah", "Arabian", "Peninsula,", "Middle", "East", "Senegal", "Sénégal", "Senegal", "West", "Africa", "Serbia", "Serbie", "Srbija", "Southern", "Europe", "Seychelles", "Seychelles", "Seychelles", "Eastern", "Africa", "Sierra", "Leone", "Sierra", "Leone", "Sierra", "Leone", "West", "Africa", "Singapore", "Singapour", "Singapore", "Southeast", "Asia", "Slovakia", "Slovak", "Republic", "Slovaquie", "Slovensko", "Eastern", "Europe", "Slovenia", "Slovénie", "Slovenija", "Southern", "Europe", "Solomon", "Islands", "Salomon,", "Îles", "Solomon", "Islands", "Melanesia,", "Oceania", "Somalia", "Somalie", "Somalia", "Eastern", "Africa", "South", "Africa", "Afrique", "Sud", "South", "Africa", "Southern", "Africa", "South", "Sudan", "Soudan", "Sud", "South", "Sudan", "East-Central", "Africa", "Spain", "Espagne", "España", "Southern", "Europe", "Sri", "Lanka", "Sri", "Lanka", "Sri", "Lanka", "South-Central", "Asia", "Sudan", "Soudan", "As-Sudan", "Northern", "Africa", "Suriname", "Suriname", "Suriname", "North-Eastern", "South", "America", "Swaziland", "Swaziland", "Swaziland", "Southern", "Africa", "Sweden", "Suède", "Sverige", "Northern", "Europe", "Switzerland", "Suisse", "Schweiz", "German,", "Suisse", "French,", "Svizzera", "Italian", "Western", "Europe", "Syria,", "Syrian", "Arab", "Republic", "Syrienne,", "République", "Arabe", "Suriyah", "Middle", "East,", "Western", "Asia", "Taiwan", "Republic", "China", "Taïwan,", "Province", "Chine", "T'ai-wan", "Eastern", "Asia", "Tajikistan", "Tadjikistan", "Jumhurii", "Tojikiston", "Central", "Asia", "Tanzania;", "officially", "United", "Republic", "Tanzania", "Tanzanie,", "République-Unie", "Jamhuri", "ya", "Muungano", "wa", "Tanzania", "Eastern", "Africa", "Thailand", "Thaïlande", "Prathet", "Thai", "South-East", "Asia", "Tibet", "Tibet", "Bod", "South-Central", "Asia", "Timor-Leste", "East", "Timor", "Timor-Leste", "Timor", "Oriental", "Timor", "Maritime", "South-East", "Asia", "Togo", "Togo", "Republique", "Togolaise", "West", "Africa", "Tokelau", "Tokelau", "Tokelau", "Oceania/Australia", "Tonga", "Tonga", "Tonga", "Polynesia,", "Oceania", "Trinidad", "Tobago", "Trinité-et-Tobago", "Trinidad,", "Tobago", "Northern", "South", "America,", "Caribbean", "Tunisia", "Tunisie", "Tunis", "Northern", "Africa", "Turkey", "Turquie", "Turkiye", "Southeastern", "Europe,", "Western", "Asia", "Turkmenistan", "Turkménistan", "Turkmenistan", "Central", "Asia", "Turks", "Caicos", "Islands", "Turks", "Caïques,", "Îles", "Turks", "Caicos", "Islands", "Caribbean,", "parts", "Bahamas", "island", "chain.", "Tuvalu", "Tuvalu", "Tuvalu", "Polynesia,", "Oceania", "Uganda", "Ouganda", "Uganda", "Eastern", "Africa", "Ukraine", "Ukraine", "Ukrayina", "Eastern", "Europe", "United", "Arab", "Emirates", "Émirats", "Arabes", "Unis", "Imarat", "Arabiyah", "Muttahidah", "Arabian", "Peninsula,", "Middle", "East", "United", "Kingdom", "Royaume-Uni", "United", "Kingdom", "Northern", "Europe", "United", "States", "États-Unis", "United", "States", "North", "America", "Uruguay", "Uruguay", "Republica", "Oriental", "Uruguay", "Central", "East", "South", "America", "Uzbekistan", "Ouzbékistan", "Uzbekiston", "Respublikasi", "Central", "Asia", "Vanuatu", "Vanuatu", "Vanuatu", "Melanesia,", "Oceania", "Vatican", "City", "State", "Holy", "See", "Saint-Siège", "État", "Cité", "Vatican", "Status", "Civitatis", "Vaticanæ", "Southern", "Europe", "within", "Italy", "Venezuela", "Venezuela", "Venezuela", "Northern", "South", "America", "Vietnam", "Viêt", "Nam", "Viet", "Nam", "South-East", "Asia", "Virgin", "Islands", "British", "Îles", "Vierges", "Britanniques", "Lesser", "Antilles,", "Caribbean", "Virgin", "Islands", "U.S.", "Îles", "Vierges", "États-Unis", "Virgin", "Islands", "Lesser", "Antilles,", "Caribbean", "Wallis", "Futuna", "Islands", "Wallis", "Futuna", "Wallis", "Futuna", "Polynesia,", "Oceania", "Western", "Sahara", "Sahara", "Occidental", "Aṣ-Ṣaḥrā’", "al-Gharbīyah", "Northern", "Africa", "Yemen", "Yémen", "Yaman", "Arabian", "Peninsula,", "Middle", "East", "Zambia", "Zambie", "Zambia", "Eastern", "Africa", "Zimbabwe", "Zimbabwe", "Zimbabwe", "Eastern", "Africa"]


# Read in

# In[407]:


articles_en = [open(f"C:/Users/mgoedicke/Desktop/Python/Notebooks/Untitled Folder/1971_9_en/{file}","r",encoding = "utf8").read()
                  for file in os.listdir("C:/Users/mgoedicke/Desktop/Python/Notebooks/Untitled Folder/1971_9_en/")
                  if file.endswith(".txt")
            ]

articles_fr = [open(f"C:/Users/mgoedicke/Desktop/Python/Notebooks/Untitled Folder/1971_9_fr/{file}","r",encoding = "utf8").read()
                  for file in os.listdir("C:/Users/mgoedicke/Desktop/Python/Notebooks/Untitled Folder/1971_9_fr/")
                  if file.endswith(".txt")
            ]


all_issues_en = [open(f"C:/Users/mgoedicke/Desktop/Python/Notebooks/Whole_Korpus/{file}",mode="r",encoding = "utf8").read()
                for file in os.listdir("C:/Users/mgoedicke/Desktop/Python/Notebooks/Whole_Korpus")
                if file.endswith("en.xml")
            ]
all_issues_en = " ".join(all_issues_en)

all_issues_fr = [open(f"C:/Users/mgoedicke/Desktop/Python/Notebooks/Whole_Korpus/{file}",mode="r",encoding = "utf8").read()
                for file in os.listdir("C:/Users/mgoedicke/Desktop/Python/Notebooks/Whole_Korpus")
                if file.endswith("fr.xml")
            ]
all_issues_fr = " ".join(all_issues_fr)


words_to_delete = ["<div>","</div>","\n","\t"]
for word_to_delete in words_to_delete:
    articles_en = [article.replace(word_to_delete,"") for article in articles_en]
    articles_fr = [article.replace(word_to_delete,"") for article in articles_fr]
for word_to_delete in words_to_delete:
    all_issues_en = all_issues_en.replace(word_to_delete,"")
    all_issues_fr = all_issues_fr.replace(word_to_delete,"")


# Helper methods for word importances

# In[438]:


from nltk.stem import SnowballStemmer

def get_clean_text(text, language):
    to_delete = ['"',",",".","?","!","“","”","'","(",")",":","‘","%","-","+","/","—"]
    for item in to_delete:
        text = text.replace(item,"")
    
    to_replace_with_whitespace = ["´","’"]
    for item in to_replace_with_whitespace:
        text = text.replace(item," ")
        
    stemmer = SnowballStemmer(language)
    text = " ".join([stemmer.stem(word) for word in text.split()])
    return text

def get_tfidf_score(word,document,reference_documents):
    tf = document.count(word) / len(document.split(" "))
    idf = math.log ( len(reference_documents) 
                    / (1 + len([reference_document for reference_document in reference_documents if word in reference_document]))
                   )    
    return tf * idf

def get_word_importances(text, reference_texts, cutoff = 10):
    #set of tfidf-scores per word 
    text_word_importances=set([(word,get_tfidf_score(word ,text ,reference_texts)) 
                               for word in text.split(" ") 
                               if word != ""
                              ]
                             )

    #sort
    text_word_importances = sorted(text_word_importances, key = lambda x: x[1], reverse = True) 
    
    #only the words, not the scores, of the top 10 words per article
    text_word_importances =  [item[0] for item in text_word_importances[:10]]
    
    return text_word_importances                              


# Compute word importances (commented take longer)

# In[439]:


articles_en2 = [get_clean_text(article, "english") for article in articles_en ]
articles_fr2 = [get_clean_text(article, "french") for article in articles_fr ]

word_importances_reference_articles_en = [get_word_importances(article, articles_en2) for article in articles_en2]
word_importances_reference_articles_fr = [get_word_importances(article, articles_fr2) for article in articles_fr2]

#issues_en2 = [get_clean_text(issue, "english") for issue in all_issues_en ]
#issues_fr2 = [get_clean_text(issue, "french") for issue in all_issues_fr ]

#word_importances_reference_issues_en = [get_word_importances(article, issues_en2) for article in articles_en2]
#word_importances_reference_issues_fr = [get_word_importances(article, issues_fr2) for article in articles_en2]


# Create DataFrame

# In[578]:


column_values_en = list(zip(articles_en
                            ,word_importances_reference_articles_en
                           # ,word_importances_reference_issues_en
                        )
                    )
column_values_fr = list(zip(articles_fr
                            ,word_importances_reference_articles_fr
                           # ,word_importances_reference_issues_fr
                        )
                    )

df_en = pd.DataFrame(column_values_en, columns = ["text","word_importances_compare_issue"])#,"word_importances_compare_all_issues"])
df_fr = pd.DataFrame(column_values_fr, columns = ["text","word_importances_compare_issue"])#,"word_importances_compare_all_issues"])


# Helper methods syntactic feature generation

# In[580]:


def get_occurring_interesting_numbers(text):
    pattern = "\d+[\%\€\$£¥]?"
    return list(set(re.findall(pattern,text)))

def get_occuring_elements(text,reference):
    return list(set([element for element in reference if element in text]))
    
def get_jaccard_distance(list_1,list_2):
    
    set_1 = set(list_1)
    set_2 = set(list_2)
    
    length_union = len(set_1.union(set_2))
    if length_union == 0:
        return 0
    else:
        return round(len(set_1.intersection(set_2)) / length_union,4)

def get_z_score(series):
    mean = series.mean()
    #std = series.std()
    return series.map(lambda cnt: (cnt-series.mean()) / series.std())
def add_metadata_features(df):
    df["cnt_characters"] = df.text.map(lambda text: len(text))
    df["cnt_words"] = df.text.map(lambda text: len(re.split("\s",text)))
    df["cnt_sentences"] = df.text.map(lambda text: len(re.split("[\?\.\!]",text)))
    df["cnt_questions"] = df.text.map(lambda text: len(re.split("[\?]",text))-1)
    df["cnt_exclamations"] = df.text.map(lambda text: len(re.split("[!?]",text))-1)


    df["cnt_characters_z_score"] = get_z_score(df.cnt_characters) 
    df["cnt_words_z_score"] = get_z_score(df.cnt_words)
    df["cnt_sentences_z_score"] = get_z_score(df.cnt_sentences)
    df["cnt_questions_z_score"] = get_z_score(df.cnt_questions)
    df["cnt_exclamations_z_score"] = get_z_score(df.cnt_exclamations)
    
    df["interesting_numbers"] = df.text.map(lambda text: get_occurring_interesting_numbers(text))
    df["ankerwords"] = df.text.map(lambda text: get_occuring_elements(text,anker_words_countries))
    df["constant"] = 1


# In[581]:


add_metadata_features(df_en)
add_metadata_features(df_fr)


# In[582]:


df_en[:3]


# In[570]:


df_fr[:3]


# In[560]:


# constant for cross join
df = df_en.merge(df_fr, on = ["constant"], suffixes = ("_EN","_FR"))
df[:3]


# Compute distance
# 
# First draft, lot of space for improvement

# In[572]:


df["distance"] =(
    abs(df.cnt_characters_z_score_EN - df.cnt_characters_z_score_FR)
    + abs(df.cnt_words_z_score_EN - df.cnt_words_z_score_FR)
    + abs(df.cnt_sentences_z_score_EN - df.cnt_sentences_z_score_FR)
    + abs(df.cnt_questions_z_score_EN - df.cnt_questions_z_score_FR)
    + abs(df.cnt_exclamations_z_score_EN - df.cnt_exclamations_z_score_FR)
) * (1 - df.apply(lambda row: get_jaccard_distance(row.interesting_numbers_EN, row.interesting_numbers_FR), axis = 1))


# View results

# In[575]:


pd.set_option('display.max_colwidth', 1000)
df[["text_EN","text_FR","distance"]].sort_values(by="distance")

