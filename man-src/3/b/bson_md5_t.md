---
title: "bson_md5_t(3)"
name: "bson_md5_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_md5_t/"
---

<h2>NAME</h2>

 bson_md5_t - BSON MD5 Abstraction

<h2>SYNOPSIS</h2>

 

 <pre><code>
typedef struct
{
    uint32_t count[2]; /* message length in bits, lsw first */
    uint32_t abcd[4];  /* digest buffer */
    uint8_t buf[64];   /* accumulate block */
} bson_md5_t;
</code></pre> 

<h2>DESCRIPTION</h2>

 

 bson_md5_t encapsulates an implementation of the MD5 algorithm. This is used in OID generation for the MD5(hostname) bytes. It is also used by some libraries such as the MongoDB C driver. 

 

<h2>COLOPHON</h2>

 This page is part of libbson. Please report any bugs at <a rel="nofollow" HREF="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> 

<h2>Index</h2>


