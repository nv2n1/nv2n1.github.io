---
title: "mongoc_iovec_t(3)"
name: "mongoc_iovec_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_iovec_t/"
description: "mongoc_iovec_t – Synopsis #include <mongoc.h>"
---

<p>mongoc_iovec_t &#8211; Synopsis<br />
&nbsp;<wbr>#include&nbsp;<wbr>&lt;mongoc.h&gt; </p>
<p> #ifdef _WIN32 typedef struct {<br />
u_long&nbsp;<wbr>&nbsp;<wbr>iov_len;<br />
char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>*iov_base; } mongoc_iovec_t; #else typedef struct iovec mongoc_iovec_t; #endif</p>
<h2>Synopsis</h2>
<h2>Synopsis</h2>
<pre>#include &lt;mongoc.h&gt;
#ifdef _WIN32
typedef struct
{
 u_long iov_len;
 char *iov_base;
} mongoc_iovec_t;
#else
typedef struct iovec mongoc_iovec_t;
#endif</pre>
<p>The <code>mongoc_iovec_t</code> structure is a portability abstraction for consumers of the <code>mongoc_stream_t</code> interfaces. It allows for scatter/gather I/O through the socket subsystem. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>When writing portable code, beware of the ordering of <code>iov_len</code> and <code>iov_base</code> as they are different on various platforms. Therefore, you should not use C initializers for initialization.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
