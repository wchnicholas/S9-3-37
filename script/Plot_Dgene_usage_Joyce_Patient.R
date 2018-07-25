#R code
library(ggplot2)
library(data.table)
library(scales)
library(RColorBrewer)
library(readr)
library(tidyr)
library(reshape)
library(stringr)
library(dplyr)
library(ggrepel)
library(gridExtra)
require(cowplot)

HDusage_by_subject_bar_plot <- function(table_summary){
  textsize <- 7
  p <-  ggplot(table_summary, aes(Subject, HD39_percent*100)) + 
	  geom_bar(stat="identity",position=position_dodge()) +
	  theme(plot.title=element_text(size=textsize,face="bold"),
		axis.title=element_text(size=textsize,face="bold"),
		axis.text=element_text(size=textsize,face="bold"),
		axis.text.x=element_text(angle = 90, hjust = 0.5,size=textsize, vjust=0.5,face="bold"),
		legend.key.size=unit(0.6,'lines'),
		legend.title=element_blank(),
		legend.text=element_text(size=textsize,face="bold"),
		legend.position='right') +
	  scale_y_continuous(breaks=c(0,20,40,60,80,100),labels=c('0','20','40','60','80','100'),expand=c(0,0),limits=c(0,100)) +
	  scale_fill_manual(values=c('gray30','gray70'),drop=FALSE) +
	  ylab(bquote(bold('D3-9 gene segment usage (%)'))) +
	  xlab(bquote(bold('')))
  ggsave('graph/HD39_Joyce_Patient_usage.png',p,height=2.2,width=1.8)
  }

HDusage_within_subject_pie_chart <- function(table_count, subject_id){
  textsize <- 7
  colorscale  <- c(brewer.pal(8,"Set3"))[1:3]
  p <-  ggplot(filter(table_count, Subject==subject_id),aes(Subject, value, fill=variable)) +
	  geom_bar(stat="identity",width=1) +
	  theme(axis.title=element_text(size=textsize,face="bold"),
		axis.text=element_text(size=textsize,face="bold"),
		axis.text.x=element_blank(),
		legend.key.size=unit(0.2,'in'),
		legend.title=element_blank(),
		legend.text=element_text(size=textsize,face="bold"),
		legend.position='right') +
	  labs(y=expression(bold('# of residues')),x=expression()) +
	  scale_fill_manual(values=colorscale,drop=FALSE) +
	  coord_polar("y", start=0)
  ggsave(paste('graph/HD39_usage_Joyce_',str_replace_all(subject_id,' ',''),'.png',sep=''),p,height=2.2,width=4)
  }

table_summary <- read_tsv('result/Dgene_Joyce_Patient_summary.tsv') %>%
                   mutate(HD39_percent=HD39_count/Total_count) %>%
                   mutate(Other_count=HD39_count-ILTG_count-LRYFDWL_count)
HDusage_by_subject_bar_plot(table_summary)

table_count <- table_summary %>%
                 select(Subject, ILTG_count, LRYFDWL_count, Other_count)
setDT(table_count)
table_count <- melt(table_count, id='Subject')
subjects  <- unique(table_count$Subject)
for (subject_id in subjects){HDusage_within_subject_pie_chart(table_count, subject_id)}
