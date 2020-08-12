rm(list=ls())

library(caret)
data("GermanCredit")
str(GermanCredit)
table(GermanCredit$Class)

#신용평가가 BAD일 것 같은 애들을 찾아서 모델링하기 (타겟변수: class)

library(Hmisc)
gc <- GermanCredit
str(gc)
describe(gc)
gc$Class <- as.character(gc$Class)
gc$Class[gc$Class=="Bad"] <- "0"
gc$Class[gc$Class=="Good"] <- "1"
gc$Class <- as.factor(gc$Class)
str(gc)

sum(is.na(gc))

library(sampling)
(x <- strata(c("Class"),size=c(300,300),method="srswor",data=gc))
train <- getdata(gc,x)
train <- train[,-c(63:65)]
train
library(car)
lm1 <- lm(Class~.,data=gc)


logit <- glm(Class ~., data = train, family="binomial")
logit2 <- step(logit,direction = "both")

predicted <- predict(logit,newdata=train,type="response")
pr <- prediction(predicted, train$Class)
prf <- performance(pr,measure="tpr",x.measure="fpr") 
plot(prf)

auc <- performance(pr, measure="auc")
auc <- auc@y.values[[1]]
auc
