rm(list=ls())

d <- subset(iris, Species=="virginica"|Species=="versicolor")
str(d)

d$Species <- factor(d$Species)
str(d)

m <- glm(Species~.,data=d,family="binomial")
summary(m)


f <- fitted(m)
as.numeric(d$Species)
ifelse(f>.5,1,0) == as.numeric(d$Species) -1

is_correct <- (ifelse(f>.5,1,0)==as.numeric(d$Species)-1)
sum(is_correct)/NROW(is_correct)

predict(m,newdata=d[c(1,10,55),],type="response")



library(ROCR)

fittedt.idx <- sample(1:100,70)
d.tr <- d[t.idx,]
d.te <- d[-t.idx,]

m_2 <- glm(Species~.,data=d.tr,family="binomial")

predicted <- predict(m_2,newdata=d.te,type="response")
pr <- prediction(predicted, d.te$Species)
prf <- performance(pr,measure="tpr",x.measure="fpr") #tpr:1일때1일확률 / fpr:0일때0일확률
plot(prf)

auc <- performance(pr, measure="auc")
auc <- auc@y.values[[1]]
auc




#car.csv를 이용한 로지스틱회귀 연습(실습)
rm(list=ls())

car <- read.csv(file="C:/Users/Playdata/Desktop/월요일교수님/car.csv",header=TRUE)
summary(car)
str(car)
car$clm <- factor(car$clm)
str(car)

m_car <- glm(clm ~., data=car, family="binomial")
summary(m_car)

fit.idx <- sample(1:67856,47500)
car.tr <- car[fit.idx,]
car.te <- car[-fit.idx,]

#rf <- randomForest(clm ~., data=car,importance=TRUE)
#importance(rf)
#m_car2 <- glm(clm ~ numclaims+claimcst0+veh_value_2+veh_value+exposure, data=car.tr, family="binomial")

m_car2 <- glm(clm ~ ., data=car.tr, family="binomial")
#summary(m_car2)

car_predicted <- predict(m_car2,newdata=car.te,type="response")
car_pr <- prediction(car_predicted, car.te$clm)
car_prf <- performance(car_pr,measure="tpr",x.measure="fpr")
plot(car_prf)

car_auc <- performance(car_pr, measure="auc")
car_auc <- car_auc@y.values[[1]]
car_auc



# 연습2
rm(list=ls())

data(Sonar)
str(Sonar)
summary(Sonar)

fittedt.idx <- sample(1:208,140)
Sonar.tr <- Sonar[fittedt.idx,]
Sonar.te <- Sonar[-fittedt.idx,]

m <- glm(Class ~ ., data=Sonar.tr, family="binomial")

predicted <- predict(m,newdata=Sonar.te,type="response")
pr <- prediction(predicted, Sonar.te$Class)
prf <- performance(pr,measure="tpr",x.measure="fpr")
plot(prf)

auc <- performance(pr, measure="auc")
auc <- auc@y.values[[1]]
auc