rm(list=ls())

data(iris)

df <- as.data.frame(scale(iris[,-5]))
str(df)
table(iris$Species)

similarity1 <- dist(df, method = 'euclidean')
similarity2 <- dist(df, method = 'manhattan')
similarity1
similarity2

library(cluster)
diana <- diana(df, metric = "manhattan")
plot(diana)
k_diana <- cutree(diana, k=4)
plot(k_diana)


library(cluster) # 군집 분석 수행
library(compareGroups) # 기술적 통계표 생성
library(HDclassif) # 데이터를 담고 있는 라이브러리
library(NbClust) # 군집 유효성 체크
library(sparcl) # 계통수 그리기

data(iris)
str(iris)
names(iris) <- c("Sepal.Length","Sepal.Width","Petal.Length","Petal.Width","Species")
names(iris)
str(iris)

numComplete <- NbClust(df, distance = 'euclidean', min.nc = 2, max.nc=6, method='complete', index='all')
# distance : 거리계산법  //  min.nc:최소군집 max.nc:최대군집  //  method: 완전연결법
numComplete$Best.nc  # 3 스크립 차트가 확 꺾이는 구간이 베스트!

dis <- dist(df, method="euclidean")  # 거리 계산 해주고
hc <- hclust(dis,method="complete")  # 그 결과를 가지고 군집화!
plot(hc, hang = -1, labels = FALSE)

str(df)
summary(df)
table(iris$Species)
dis_1 <- dist(df, method='euclidian')

comp3 <- cutree(hc,3)
comp3
ColorDendrogram(hc, y=comp3, main="Complete", branchlength=50)
table(comp3)
table(comp3, iris$Species)


# k-means 군집화
set.seed(1234)
km <- kmeans(df, 3, nstart=25) # nstart: 초기군집화개수
table(km$cluster)
table(km$cluster, iris$Species) 







#####################################################################






library(ggplot2)
data(diamonds)
summary(diamonds)

df <- as.data.frame(scale(diamonds[c(1:1000),-c(2:4,8:10)]))
str(df)

library(cluster)
diana <- diana(df, metric = "manhattan")
plot(diana)
k_diana <- cutree(diana, k=4)
plot(k_diana)

library(cluster) # 군집 분석 수행
library(compareGroups) # 기술적 통계표 생성
library(HDclassif) # 데이터를 담고 있는 라이브러리
library(NbClust) # 군집 유효성 체크
library(sparcl) # 계통수 그리기

numComplete <- NbClust(df, distance = 'euclidean', min.nc = 2, max.nc=6, method='complete', index='all')
# distance : 거리계산법  //  min.nc:최소군집 max.nc:최대군집  //  method: 완전연결법
numComplete$Best.nc  # 3 스크립 차트가 확 꺾이는 구간이 베스트!

dis <- dist(df, method="euclidean")  # 거리 계산 해주고
hc <- hclust(dis,method="complete")  # 그 결과를 가지고 군집화!
plot(hc, hang = -1, labels = FALSE)

str(df)
summary(df)

dis_1 <- dist(df, method='euclidian')

# k-means 군집화
set.seed(1234)
km <- kmeans(df, 3, nstart=25) # nstart: 초기군집화개수
table(km$cluster)