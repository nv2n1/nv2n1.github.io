---
title: "mongoc_index_opt_geo_t(3)"
name: "mongoc_index_opt_geo_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_index_opt_geo_t/"
---

mongoc_index_opt_geo_t - #include &lt;mongoc.h&gt; 

 typedef struct { 
uint8_t twod_sphere_version; 
uint8_t twod_bits_precision; 
double&nbsp;<wbr>&nbsp;<wbr>twod_location_min; 
double&nbsp;<wbr>&nbsp;<wbr>twod_location_max; 
double&nbsp;<wbr>&nbsp;<wbr>haystack_bucket_size; 
uint8_t&nbsp;<wbr>*padding[32]; } mongoc_index_opt_geo_t;
<h2>Synopsis</h2><pre>#include &lt;mongoc.h&gt;
typedef struct
{
 uint8_t twod_sphere_version;
 uint8_t twod_bits_precision;
 double twod_location_min;
 double twod_location_max;
 double haystack_bucket_size;
 uint8_t *padding[32];
} mongoc_index_opt_geo_t;</pre><h2>Description</h2>This structure contains the options that may be used for tuning a GEO index. 

<h2>See Also</h2><h2>Colophon</h2>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" HREF="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a>
