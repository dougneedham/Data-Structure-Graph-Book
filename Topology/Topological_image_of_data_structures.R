library("rgl")
library(readr)
setwd("~/R/DV_Topography")
cs <- read_csv('DMZone_Demo.csv')
cs$C_DATE <- as.Date(cs$C_DATE,'%m/%d/%Y')
cs$Increment <- as.integer(cs$C_DATE - min(cs$C_DATE))
for(cols in 1:ncol(cs)) {
  for(index in 2:nrow(cs)) { if(cs[index,cols] == 0 & cs[(index-1),cols] !=1) { cs[index,cols] <- cs[(index-1),cols]}}
}
for(index in 2:nrow(cs)) { if(cs[index,3] == 0 & cs[(index-1),3] !=1) { cs[index,3] <- cs[(index-1),3]}}

df <- cs[,c(2:7)]
df <- df[,order(as.integer(names(df)))]

x <- c(1:ncol(df))
y <-cs$Increment
second.element <- function(my.string) { unlist(strsplit(my.string,"X"))[2]}
#df <- df[order(as.integer(sapply(names(df),second.element))),]
#df <- df[order(names(df))]
#df <- data.frame(df[,3],df[,6],df[,5],df[,1],df[,2],df[,4])
dfi <- expand.grid(x,y)
dfi$value <- 0	

for(index in 1:nrow(dfi)) {dfi[index,]$value <- as.integer(df[(dfi[index,]$Var2+1),dfi[index,]$Var1])}

columns <- ncol(df)

#dfi$value2 <- dfi$value-min(dfi$value)/(max(dfi$value)-min(dfi$value))
dfi$value2 <- (dfi$value-min(dfi$value,na.rm=TRUE))/(max(dfi$value,na.rm=TRUE)-min(dfi$value,na.rm=TRUE))
plot_x <- seq(from = 1/ncol(df), to =1, by = 1/ncol(df))
plot_y <- seq(from=1/nrow(df),to=1,by=1/nrow(df))
surface3d(x=plot_x, y=plot_y, z=dfi$value2, col="red", back="lines")
title3d(xlab="Average Document Length", zlab="Numer of records", ylab="Time ")
mtext3d(names(df),edge='x',at=plot_x)
#text3d(y,edge='y++',at=plot_y)
axes3d(tick="TRUE",xlab=x)