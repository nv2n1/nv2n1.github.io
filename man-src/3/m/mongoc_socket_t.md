---
title: "mongoc_socket_t(3)"
name: "mongoc_socket_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_socket_t/"
---

mongoc_socket_t - Portable socket abstraction
<h2>Synopsis</h2><pre>#include &lt;mongoc.h&gt;
typedef struct _mongoc_socket_t mongoc_socket_t</pre><h2>Synopsis</h2>This structure provides a socket abstraction that is friendlier for portability than BSD sockets directly. Inconsistencies between Linux, various BSDs, Solaris, and Windows are handled here. 

 

<h2>Colophon</h2>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" HREF="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a>
