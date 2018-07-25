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

HDusage_HIV_bnAb_pie_chart <- function(table_count){
  textsize <- 7
  colorscale  <- c('grey30', 'grey70')
  p <-  ggplot(table_count,aes(Subject, value, fill=variable)) +
          geom_bar(stat="identity",width=1) +
          theme(axis.title=element_text(size=textsize,face="bold"),
                axis.text=element_text(size=textsize,face="bold"),
                axis.text.x=element_blank(),
                legend.key.size=unit(0.2,'in'),
                legend.title=element_blank(),
                legend.text=element_text(size=textsize,face="bold"),
                legend.position='right') +
          labs(y=expression(bold(' of residues')),x=expression()) +
          scale_fill_manual(values=colorscale,drop=FALSE) +
          coord_polar("y", start=0)
  ggsave(paste('graph/HD39_HIV_usage.png',sep=''),p,height=2.2,width=4)
  }

table_count <- read_tsv('result/Dgene_HIV_bnAb_summary.tsv') %>%
                   mutate(HD39_percent=HD39_count/Total_count) %>%
                   mutate(Other_count=HD39_count-ILTG_count-LRYFDWL_count) %>%
                   mutate(non_HD39_count=Total_count-HD39_count) %>%
                   select(Subject, HD39_count, non_HD39_count)
setDT(table_count)
table_count <- melt(table_count, id='Subject')
HDusage_HIV_bnAb_pie_chart(table_count)
