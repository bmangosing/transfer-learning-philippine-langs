import pandas as pd
import re

filepath = ["tagalog_literary_text.txt", 
            "tagalog_religious_text.txt", 
            "ilokano_literary_text.txt", 
            "ilokano_religious_text.txt", 
            "cebuano_literary_text.txt", 
            "cebuano_religious_text.txt",
            "bikol_literary_text.txt", 
            "bikol_religious_text.txt",
            "hiligaynon_literary_text.txt", 
            "hiligaynon_religious_text.txt",
            "kapampangan_literary_text.txt", 
            "kapampangan_religious_text.txt",
            "pangasinense_literary_text.txt", 
            "pangasinense_religious_text.txt", 
            "waray_literary_text.txt", 
            "waray_religious_text.txt"]

for i in filepath:
    with open(i, 'r') as file:
        filedata = file.read()

    # Replace the the html tags
    filedata = filedata.replace('<b>', '')
    filedata = filedata.replace('</b>', '')
    filedata = filedata.replace('<i>', '')
    filedata = filedata.replace('</i>', '')
    filedata = filedata.replace('<pd>', '')
    filedata = filedata.replace('</pd>', '')
    filedata = filedata.replace('<lbl>', '')
    filedata = filedata.replace('</lbl>', '')

    # Write the file out again
    with open(i, 'w') as file:
          file.write(filedata)

#Read in all the different texts and languages from the corpus

tag_lit = pd.read_csv('tagalog_literary_text.txt', sep='delimiter', header=None, engine='python')
tag_reg = pd.read_csv('tagalog_religious_text.txt', sep='delimiter', header=None, engine='python')

ilo_lit = pd.read_csv('ilokano_literary_text.txt', sep='delimiter', header=None, engine='python')
ilo_reg = pd.read_csv('ilokano_religious_text.txt', sep='delimiter', header=None, engine='python')

ceb_lit = pd.read_csv('cebuano_literary_text.txt', sep='delimiter', header=None, engine='python')
ceb_reg = pd.read_csv('cebuano_religious_text.txt', sep='delimiter', header=None, engine='python')

bik_lit = pd.read_csv('bikol_literary_text.txt', sep='delimiter', header=None, engine='python')
bik_reg = pd.read_csv('bikol_religious_text.txt', sep='delimiter', header=None, engine='python')

hil_lit = pd.read_csv('hiligaynon_literary_text.txt', sep='delimiter', header=None, engine='python')
hil_reg = pd.read_csv('hiligaynon_religious_text.txt', sep='delimiter', header=None, engine='python')

kap_lit = pd.read_csv('kapampangan_literary_text.txt', sep='delimiter', header=None, engine='python')
kap_reg = pd.read_csv('kapampangan_religious_text.txt', sep='delimiter', header=None, engine='python')

pan_lit = pd.read_csv('pangasinense_literary_text.txt', sep='delimiter', header=None, engine='python')
pan_reg = pd.read_csv('pangasinense_religious_text.txt', sep='delimiter', header=None, engine='python')

war_lit = pd.read_csv('waray_literary_text.txt', sep='delimiter', header=None, engine='python')
war_reg = pd.read_csv('waray_religious_text.txt', sep='delimiter', header=None, engine='python')


#Setting the columns for the datasets
#I didn't use all of the data just because it's a lot

text_list = [tag_lit, tag_reg, ilo_lit, ilo_reg, ceb_lit, ceb_reg, bik_lit, bik_reg, hil_lit, hil_reg, war_lit, war_reg] #,kap_lit, kap_reg, pan_lit, pan_reg

for i in text_list:
    i.columns = ['text']

tag_lit['language'] = 'tagalog literature'
tag_reg['language'] = 'tagalog religious'

ilo_lit['language'] = 'ilokano literature'
ilo_reg['language'] = 'ilokano religious'

ceb_lit['language'] = 'cebuano literature'
ceb_reg['language'] = 'cebuano religious'

bik_lit['language'] = 'bikol literature'
bik_reg['language'] = 'bikol religious'

hil_lit['language'] = 'hiligaynon literature'
hil_reg['language'] = 'hiligaynon religious'

kap_lit['language'] = 'kapampangan literature'
kap_reg['language'] = 'kapampangan religious'

pan_lit['language'] = 'pangasinense literature'
pan_reg['language'] = 'pangasinense religious'

war_lit['language'] = 'waray literature'
war_reg['language'] = 'waray religious'

filipino_data = pd.concat(text_list)

print(len(filipino_data))

filipino_data = filipino_data.sample(frac=1).reset_index(drop=True)

filipino_data = filipino_data.dropna()

print(len(filipino_data))
labels = list(set(filipino_data['language']))
print(labels)