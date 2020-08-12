rm(list=ls())
data(kyphosis)
str(kyphosis)
summary(kyphosis)

table(kyphosis$Kyphosis)
(m <- rpart(Kyphosis ~.,data=kyphosis))
rpart.plot(m,type=1,extra=101)

tree.1 <- rpart(Kyphosis ~ Age + Number + Start, data = kyphosis)
tree.2 <- rpart(Kyphosis ~ Age + Number + Start, data = kyphosis,
                parms = list(split = "information"))
#parms=list(split="information") : 분리기준을 정보지수로 한다

tree.2
par(mar=c(1,1,1,1),xpd=TRUE);plot(tree.2)
text(tree.2, use.n=TRUE)

# modeling 할 때 정확도 높이는 방법 : 파생변수설정(연속변수>구간화/범주변수>그룹핑) & 샘플링(층화랜덤추출) & 분리기준
