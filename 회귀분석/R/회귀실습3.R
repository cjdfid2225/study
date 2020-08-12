rm(list=ls())

library(MASS)
data("biopsy")
table(biopsy$class)

library(Hmisc)
bp <- biopsy
bp$class <- as.character(bp$class)
bp$class[bp$class=="benign"] <- "0"
bp$class[bp$class=="malignant"] <- "1"
bp$class <- as.factor(bp$class)
str(bp)

sum(is.na(bp))
bp[!complete.cases(bp),]
library(DMwR)
bp <- centralImputation(bp)
bp

library(sampling)
(x <- strata(c("class"),size=c(200,200,200),method="srswor",data=bp))
train <- getdata(bp,x)
train <- train[,-c(12:14)]
train

library(car)
logit <- glm(class ~ V1+V2+V3+V4+V5+V6+V7+V8+V9, data=bp,family="binomial")
logit2 <- step(logit,direction = "both")

predicted <- predict(logit,newdata=train,type="response")
pr <- prediction(predicted, train$class)
prf <- performance(pr,measure="tpr",x.measure="fpr") 
plot(prf)

auc <- performance(pr, measure="auc")
auc <- auc@y.values[[1]]
auc







# 파생변수 만들기
install.packages("smbinning")
library(smbinning)
bp$class <- as.numeric(bp$class) - 1
result = smbinning(bp,x="V1",y="class")
result$ivtable
result$iv
pop = smbinning.gen(bp,result,"v1_2") #smbinning.gen:파생변수를 만들어주는 함수
table(pop$v1_2)
summary(pop$v1_2)
str(pop$v1_2)
#v1_2를 쓰려면 v1은 지워야한다 >> v1과 v1_2의 상관계수가 너무 높게 나와서
