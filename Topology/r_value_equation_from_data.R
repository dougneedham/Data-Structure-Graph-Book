


r_values <- c(1.357,2.26,3.762,1.184,1.177,1.437)
y <- sort(r_values)
x <- c(1:6)

fit2 <- lm(y~poly(x,2,raw=TRUE))
fit3 <- lm(y~poly(x,3,raw=TRUE))
fit4 <- lm(y~poly(x,4,raw=TRUE))
fite <- lm(log(cs$`9876`)~log(cs$Increment+1))
xx <- c(1:6)
lines(xx,predict(fit,data.frame(x=xx)),col="red")
lines(xx,predict(fit2,data.frame(x=xx)),col="blue")
lines(xx,predict(fit3,data.frame(x=xx)),col="green")
summary(fit)$r.squared
summary(fit2)$r.squared
summary(fit3)$r.squared

paste("y = ",round(coef(fit3)[4],5),"x^3 + ",round(coef(fit3)[3],5),"x^2 + ",round(coef(fit3)[2],5),"x +",round(coef(fit3)[1],5)      ,sep="")
