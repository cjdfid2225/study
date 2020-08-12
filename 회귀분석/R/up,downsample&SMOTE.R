install.packages("mlbench")
library(mlbench)
data(BreastCancer)
table(BreastCancer$Class)

install.packages("caret")
library(caret)
x <- upSample(subset(BreastCancer,select=-Class),BreastCancer$Class)
table(BreastCancer$Class)
table(x$Class)
#Å« ÂÊ¿¡ ¸ÂÃçÁüÀ» º¼ ¼ö ÀÖ´Ù.

x_d <- downSample(subset(BreastCancer,select=-Class),BreastCancer$Class)
table(BreastCancer$Class)
table(x_d$Class)
#ÀÛÀº ÂÊ¿¡ ¸ÂÃçÁü


install.packages("DMwR")
library(DMwR)
data(iris)
data <- iris[,c(1,2,5)]
data$Species <- factor(ifelse(data$Species == "setosa","rare","common"))
table(data$Species)

newData <- SMOTE(Species~.,data,perc.over=600,perc.under=100)
table(newData$Species)
