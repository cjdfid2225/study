rm(list=ls())

install.packages("arules")
install.packages("arulesViz")
library(arules)
library(arulesViz)

data(Groceries)
head(Groceries)
str(Groceries)
itemFrequencyPlot(Groceries, topN=10, type="absolute") #빈도수 높은 아이템 10

#연관성 분석을 돌려야하는데 만일 클래스가 transaction이 아닐 때는,
#transaction.df <- as(df, "transactions") 라고 해주고 연관성 분석 하면 된다.

rules <- apriori(Groceries, parameter = list(supp=0.001, conf=0.9, maxlen=4))
#apriori: 연관성 분석 함수  //  supp=0.001:1000번의 거래 중 하나  //  conf:A가 일어날 때 B가 일어날 확률
#maxlen=4:최대 연관 아이템 4개 이하
inspect(rules[1:5])

options(digits = 2) #소수점 두자리까지 보이게
rules <- sort(rules, by="lift", decreasing=TRUE)
inspect(rules[1:5])
#lift > 1이면 연관성 있다고 판단한다.

tab <- crossTable(Groceries)
tab[1:3,1:3]
tab['bottled beer','bottled beer']

beer.rules <- apriori(data=Groceries,
                      parameter = list(support=0.0015, confidence=0.3),
                      appearance = list(default = 'lhs', rhs = 'bottled beer')) #이런식으로 rhs나 lhs 고정할 수 있다.
beer.rules <- sort(beer.rules, by='lift', decreasing=TRUE)
inspect(beer.rules)
tab['bottled beer','red/blush wine']





######################################################################






data(Epub)
str(Epub)
inspect(Epub[1:5])

itemFrequencyPlot(Epub, topN=10, type="absolute")
rules <- apriori(Epub, parameter = list(supp=0.001, conf=0.6, maxlen=3))
options(digits = 2)
rules <- sort(rules, by="lift", deccreasing=TRUE)
inspect(rules)

tab <- crossTable(Epub)
tab[1:3,1:3]
tab['doc_11d','doc_11d']

doc_11d.rules <- apriori(data=Epub,
                         parameter = list(support=0.001, confidence=0.001),
                         appearance = list(default = 'lhs', rhs = 'doc_11d'))
doc_11d.rules <- sort(doc_11d.rules, by='lift', decreasing=TRUE)
inspect(doc_11d.rules)
