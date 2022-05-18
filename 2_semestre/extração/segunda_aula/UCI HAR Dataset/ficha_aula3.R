#                                             ------------ Parte I ------------ 

# ------------ Exercício 1 ------------ 


# B
X_train["Subjects"] <- subject_train
X_test["Subjects"] <- subject_test

X_train["Classes"] <- y_train
X_test["Classes"] <- y_test

# C
# juntar os dois datasets
df = rbind(X_train, X_test)
df

# ------------ Exercício 2 ------------ 

# A
colnames(df)[which(names(df) == "Subjects")] <- "Subject"
colnames(df)[which(names(df) == "Classes")] <- "Activity"
colnames(df) = c(as.vector(features[, 1]), "Subject", "Activity")
colnames(df)

# B
for (i in 1:length(activity_labels$V2)){
  df['Activity'][df['Activity'] == i] <- as.vector(activity_labels[i, "V2"])
}

# ------------ Exercício 3 ------------ 

new_df <- data.frame(df$Subject, df$Activity)
new_df

for (i in colnames(df)) {
  if (grepl("mean()", i) || grepl("std()", i)){
    cat(i)
    new_df[i] <- df[i]
  }
}

# ------------ Exercício 4 ------------ 

df_media <- aggregate(df, by = list(df$Subject, df$Activity), FUN = mean)
df_media

# ------------ Exercício 5 ------------ 

any(is.na(df_media))

# ------------ Exercício 6 ------------ 

write.table(df, file = "data_ex2_p1.txt", sep = " ")
write.table(new_df, file = "data_ex3_p1.txt", sep = " ")
write.table(df_media, file = "data_ex4_p1.txt", sep = " ")


#                                             ------------ Parte II ------------ 

# ------------ Exercício 1 ------------ 

# A
sub_1e2 <- df_media[which(df_media$Subject == 1 | df_media$Subject == 2), ]
sub_1e2

# B
body_mean <- c()
gravity_mean <- c()

for (i in unique(df_media$Subject)){
  data <- df_media[which(df_media$Subject == i), ]
  cat("Subject", i, ":", mean(data$`tBodyAcc-mean()-X`), mean(data$`tGravityAcc-mean()-X`), "\n")
  body_mean <- c(body_mean, mean(data$`tBodyAcc-mean()-X`))
  gravity_mean <- c(gravity_mean, mean(data$`tGravityAcc-mean()-X`))
}

# C
rm(mean_data)
mean_data <- data.frame(body_mean, gravity_mean)
mean_data
subjects <- unique(df_media$Subject)

ggplot() + geom_line(aes(x = subjects, y = mean_data$body_mean), color = 1) + geom_line(aes(x = subjects, y = mean_data$gravity_mean), color = 2)

# D -> É a variável "body_mean"

# ------------ Exercício 2 ------------ 

# A
df_laying <- df[which(df$Activity == "LAYING"), ]
df_wupstairs <- df[which(df$Activity == "WALKING_UPSTAIRS"), ]

# B
summary(df_laying$`tBodyAcc-mean()-X`)
summary(df_laying$`tGravityAcc-mean()-X`)
summary(df_wupstairs$`tBodyAcc-mean()-X`)
summary(df_wupstairs$`tGravityAcc-mean()-X`)

# C
boxplot(df_laying$`tBodyAcc-mean()-X`, df_laying$`tGravityAcc-mean()-X`, df_wupstairs$`tBodyAcc-mean()-X`, df_wupstairs$`tGravityAcc-mean()-X`)

# ------------ Exercício 3 ------------ 

# A
ggplot() + geom_line(aes(x = row.names(df_laying), y = df_laying$`tBodyAcc-mean()-X`), color = 1) + geom_line(aes(x = row.names(df_laying), y = df_laying$`tGravityAcc-mean()-X`), color = 2)

as.vector(df_laying$tBodyAcc-mean)

















