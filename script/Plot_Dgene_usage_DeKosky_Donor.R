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
  setDT(table_summary)
  table_summary <- table_summary %>% 
                     select(Subject,ILTG_percent,LRYFDWL_percent) %>%
                     rename(`31.b.09-like`=ILTG_percent) %>%
                     rename(`S9-3-37-like`=LRYFDWL_percent) %>%
                     melt(id='Subject')
  textsize <- 7
  colorscale  <- c(brewer.pal(3,"Accent"))
  p <-  ggplot(table_summary, aes(variable, log10(value),group=Subject, color=Subject)) + 
	  geom_point() +
	  geom_line() +
	  theme(plot.title=element_text(size=textsize,face="bold"),
		axis.title=element_text(size=textsize,face="bold"),
		axis.text=element_text(size=textsize,face="bold"),
		axis.text.x=element_text(angle = 90, hjust = 1,size=textsize, vjust=0.5,face="bold"),
		legend.key.size=unit(0.6,'lines'),
		legend.title=element_blank(),
		legend.text=element_text(size=textsize,face="bold"),
		legend.position='right') +
	  scale_y_continuous(breaks=c(-4,-3,-2),labels=c('0.01','0.1','1'),limits=c(-4.2,-1.5)) +
	  scale_color_manual(values=colorscale,drop=FALSE) +
	  ylab(bquote(bold('Frequency (%)'))) +
	  xlab(bquote(bold('')))
  ggsave('graph/HD39_Donor_usage.png',p,height=2.2,width=2.5,dpi=600)
  }

classify_HD39 <- function(ILTG, LRYFDWL){
  if (LRYFDWL=='yes'){return ('S9-3-39-like')}
  else if (ILTG=='yes'){return ('31.b.09-like')}
  else if (LRYFDWL=='no' && ILTG=='no'){return ('Other')}
  else {print ("Something is wrong!!")}
  }

plot_CDRH3_length <- function(HD39_info){
  textsize <- 7
  donor_levels <- rev(c('Donor 1', 'Donor 2', 'Donor 3'))
  HD39_info <- HD39_info %>%
                 mutate(donorID=factor(donorID, levels=donor_levels))
  colorscale  <- rev(c(brewer.pal(3,"Accent")))
  p <-  ggplot(filter(HD39_info,HD39_class=='S9-3-39-like'), aes(x=donorID, y=CDRH3_len, fill=donorID, size=count)) +
          geom_point(position = position_jitter(width = 0.3), color='black', pch=21) +
          theme(plot.title=element_text(size=textsize,face="bold"),
                axis.title=element_text(size=textsize,face="bold"),
                axis.text=element_text(size=textsize,face="bold"),
                axis.text.x=element_text(angle = 0, hjust = 0.5,size=textsize, vjust=0.5,face="bold"),
                legend.key.size=unit(0.6,'lines'),
                legend.title=element_blank(),
                legend.text=element_text(size=textsize,face="bold"),
                legend.position='none') +
          scale_fill_manual(values=colorscale,drop=FALSE) +
          scale_size(range = c(0,1.2)) +
	  scale_y_continuous(breaks=c(5,10,15,20,25),labels=c('5','10','15','20','25'),limits=c(10,25)) +
          ylab(bquote(bold('Length of CDR H3 (aa)'))) +
          xlab(bquote(bold(''))) +
          ggtitle('S9-3-37-like CDR H3') +
          coord_flip()
  ggsave('graph/HD39_Donor_CDRH3_len.png',p,height=2,width=2.5,dpi=600)
  }

table_summary <- read_tsv('result/Dgene_Donor_summary.tsv') %>%
                   mutate(ILTG_percent=ILTG_count/Total_count) %>%
                   mutate(LRYFDWL_percent=LRYFDWL_count/Total_count)
HD39_info <- read_tsv('result/HD39_Donor_summary.tsv') %>%
               mutate(HD39_class=mapply(classify_HD39, ILTG, LRYFDWL))
HDusage_by_subject_bar_plot(table_summary)
plot_CDRH3_length(HD39_info)
