install.packages("randomForest")
library(randomForest)
rf <- randomForest(Species ~., data=iris,importance=TRUE)
importance(rf)

varImpPlot(rf,main="varImpPlot of iris")



rf_cpus <- randomForest(perf ~syct + mmin + mmax + cach + chmin + chmax, data=cpus, importance=TRUE)
importance(rf_cpus)
varImpPlot(rf_cpus,main="varImpPlot of cpus")



rf_ky <- randomForest(Kyphosis ~., data=kyphosis,importance=TRUE)
importance(rf_ky)
varImpPlot(rf_ky,main="varImpPlot of kyphosis")





