---
title: "mongoc_index_opt_wt_t(3)"
name: "mongoc_index_opt_wt_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_index_opt_wt_t/"
---

mongoc_index_opt_wt_t - #include &lt;mongoc.h&gt; 

 typedef struct { 
mongoc_index_opt_storage_t&nbsp;<wbr>&nbsp;<wbr>base; 
const char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*config_str; 
void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*padding[8]; } mongoc_index_opt_wt_t;
<h2>Synopsis</h2><pre>#include &lt;mongoc.h&gt;
typedef struct
{
 mongoc_index_opt_storage_t base;
 const char *config_str;
 void *padding[8];
} mongoc_index_opt_wt_t;</pre><h2>Description</h2>This structure contains the options that may be used for tuning a WiredTiger specific index. 

<h2>See Also</h2><h2>Colophon</h2>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" HREF="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a>
