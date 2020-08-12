rm(list=ls())

data(Boston)

##파일입출력
df <- read.csv("Boston.csv", header = TRUE, stringsAsFactors = FALSE)
df <- df[,-1] 
write.csv(df, file="df.csv", row.names = TRUE)

#기술통계량
library(Hmisc)
describe(df)
summary(medv~crim+zn, data=df)

#데이터분할
t.idx <- sample(1:506, 100)
df.tr <- df[t.idx,]
df.te <- df[-t.idx,]

#분산이 0에 가까운 변수 제거
library(caret)
nearZeroVar(df,saveMetrics = TRUE)

#변수 중요도 평가
library(randomForest)
rf <- randomForest(medv~., data=df)
varImp(rf)


##모델링
lm1 <- lm(medv ~ crim + indus + nox + rm + age + dis + tax + ptratio + black + lstat, data = df.tr)
lm2 <- step(lm1,direction = "both")

pred <- predict(lm1, newdata = df.te)
pred <- predict(lm1, newdata = df.te, interval = "confidence")

pred <- predict(lm1, newdata = df.te, interval = "prediction")

pred
coef(lm1)
fitted(lm1)

prob <- predict(lm1, newdata=df.te)


library(forecast)
accuracy(lm1)

summary(lm1)








#newcol가지고 돌리기
library(ROCR)

df$newcol[df$medv<=40] <- 1
df$newcol[df$medv>40] <- 0
df$newcol

t.idx <- sample(1:506, 100)
df.tr <- df[t.idx,]
df.te <- df[-t.idx,]

lm2 <- glm(newcol~.,data=df.tr,family="binomial")

predicted <- predict(lm2,newdata=df.te,type="response")
pr <- prediction(predicted, df.te$newcol)
prf <- performance(pr,measure="tpr",x.measure="fpr") 
plot(prf)

auc <- performance(pr, measure="auc")
auc <- auc@y.values[[1]]
auc











