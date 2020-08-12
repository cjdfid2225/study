rm(list=ls())

install.packages("MASS")
install.packages("rpart")
install.packages("rpart.plot")
install.packages("ROCR")

library(MASS)
library(rpart)
library(rpart.plot)
library(ROCR)

data(iris)
t.idx <- sample(1:150,100)
iris.tr <- iris[t.idx,]
iris.te <- iris[-t.idx,]

dt <- rpart(Species~.,data=iris.tr,method="class")
dt
#dt_m <- predict(dt, newdata=iris.te, type="class")
rpart.plot(dt,type=4,extra=101)
summary(iris.tr)

