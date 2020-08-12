rm(list=ls())
data(cpus, package="MASS"); str(cpus)
summary(cpus)

(dt <- rpart(perf ~ syct + mmin + mmax + cach + chmin + chmax,data=cpus))
#rpart.plot(dt,type=4,extra=101)

windows(height=8,width=8)
par(mar=c(1,1,1,1),xpd=TRUE)
plot(dt, uniform=F)
text(dt, use.n=T, cex=0.8)

rpart.plot(dt,type=4,extra=101)

cpus.tree.1 <- rpart(perf ~ syct + mmin + mmax + cach + chmin + chmax,
                     data=cpus, control=rpart.control(cp=0.02))
# control=rpart.control(cp=0.02) : 불순도의 상대적 감소가 5%(=0.02) 미만이면 노드 분리를 종결한다. 디폴트=1%

subsample <- sample(1:209,replace=T)
cpus.train <- cpus[subsample,]
cpus.test <- cpus[-subsample,]

cpus.tree.1 <- rpart(perf ~ syct + mmin + mmax + cach + chmin + chmax,
                     data=cpus.train, control=rpart.control(cp=0.02))

pred.err <- cpus.test$perf - predict(cpus.tree.1,newdata=cpus.test)
pred.err
mean(pred.err*pred.err)

