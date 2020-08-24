rm(list=ls())

data('Adult')
str(Adult)

library(arules)
library(arulesViz)

itemFrequencyPlot(Adult, topN=10, type="absolute") #빈도수 높은 아이템 10

rules <- apriori(Adult, parameter = list(supp=0.05, conf=0.9, maxlen=4))
options(digits = 2) #소수점 두자리까지 보이게
rules <- sort(rules, by="lift", decreasing=TRUE)
inspect(rules[1:5])

tab <- crossTable(Adult)
tab[1:3,1:3]

age.rules <- apriori(data=Adult,
                      parameter = list(support=0.001, confidence=0.9),
                      appearance = list(default = 'lhs', rhs = 'age=Middle-aged')) #이런식으로 rhs나 lhs 고정할 수 있다.
age.rules <- sort(age.rules, by='lift', decreasing=TRUE)
inspect(age.rules[1:5])
