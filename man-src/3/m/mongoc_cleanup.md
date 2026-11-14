---
title: "mongoc_cleanup(3)"
name: "mongoc_cleanup"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_cleanup/"
---

mongoc_cleanup() - This function is responsible for cleaning up after use of the MongoDB C driver. It will release any lingering allocated memory which can be useful when running under valgrind.
<h2>Synopsis</h2>
 

 <pre>
void
mongoc_cleanup (void);
</pre> 

<h2>Description</h2>
 

 This function is responsible for cleaning up after use of the MongoDB C driver. It will release any lingering allocated memory which can be useful when running under valgrind. 

 

<h2>Colophon</h2>
 This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" HREF="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a>
