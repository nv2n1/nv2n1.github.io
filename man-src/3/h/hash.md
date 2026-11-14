---
title: "hash(3)"
name: "hash"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hash/"
description: "hash – hash database access method"
---

<h2 class="name">NAME</h2>
<p> hash &#8211; hash database access method </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;db.h&gt;
#include &lt;sys/types.h&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>Note well</i>: This page documents interfaces provided in glibc up until version 2.1. Since version 2.2, glibc no longer provides these interfaces. Probably, you are looking for the APIs provided by the <i>libdb</i> library instead. </p>
<p> The routine <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3) is the library interface to database files. One of the supported file formats is hash files. The general description of the database access methods is in <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3), this manual page describes only the hash-specific information. </p>
<p> The hash data structure is an extensible, dynamic hashing scheme. </p>
<p> The access-method-specific data structure provided to <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3) is defined in the <i>&lt;db.h&gt;</i> include file as follows: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bsize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ffactor;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nelem;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cachesize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(*hash)(const void&nbsp;*, size_t);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lorder; } HASHINFO; </p>
<p> The elements of this structure are as follows:</p>
<dl>
<dt><i>bsize</i></p>
<dd> defines the hash table bucket size, and is, by default, 256 bytes. It may be preferable to increase the page size for disk-resident tables and tables with large data items.</p>
<dt><i>ffactor</i></p>
<dd> indicates a desired density within the hash table. It is an approximation of the number of keys allowed to accumulate in any one bucket, determining when the hash table grows or shrinks. The default value is 8.</p>
<dt><i>nelem</i></p>
<dd> is an estimate of the final size of the hash table. If not set or set too low, hash tables will expand gracefully as keys are entered, although a slight performance degradation may be noticed. The default value is 1.</p>
<dt><i>cachesize</i></p>
<dd> is the suggested maximum size, in bytes, of the memory cache. This value is <i>only advisory</i>, and the access method will allocate more memory rather than fail.</p>
<dt><i>hash</i></p>
<dd> is a user-defined hash function. Since no hash function performs equally well on all possible data, the user may find that the built-in hash function does poorly on a particular data set. A user-specified hash functions must take two arguments (a pointer to a byte string and a length) and return a 32-bit quantity to be used as the hash value.</p>
<dt><i>lorder</i></p>
<dd> is the byte order for integers in the stored database metadata. The number should represent the order as an integer; for example, big endian order would be the number 4,321. If <i>lorder</i> is 0 (no order is specified), the current host order is used. If the file already exists, the specified value is ignored and the value specified when the tree was created is used.</dl>
<p> If the file already exists (and the <code>O_TRUNC</code> flag is not specified), the values specified for <i>bsize</i>, <i>ffactor</i>, <i>lorder</i>, and <i>nelem</i> are ignored and the values specified when the tree was created are used. </p>
<p> If a hash function is specified, <i>hash_open</i> attempts to determine if the hash function specified is the same as the one with which the database was created, and fails if it is not. </p>
<p> Backward-compatible interfaces to the routines described in <code><a href="/docs/linux/man/3-dbm/">dbm</a></code>(3), and <code><a href="/docs/linux/man/3-ndbm/">ndbm</a></code>(3) are provided, however these interfaces are not compatible with previous file formats.</p>
<h2>ERRORS</h2>
<p> The <i>hash</i> access method routines may fail and set <i>errno</i> for any of the errors specified for the library routine <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3).</p>
<h2>BUGS</h2>
<p> Only big and little endian byte order are supported.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-btree/">btree</a></code>(3), <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3), <code><a href="/docs/linux/man/3-mpool/">mpool</a></code>(3), <code><a href="/docs/linux/man/3-recno/">recno</a></code>(3) </p>
<p> <i>Dynamic Hash Tables</i>, Per-Ake Larson, Communications of the ACM, April 1988. </p>
<p> <i>A New Hash Package for UNIX</i>, Margo Seltzer, USENIX Proceedings, Winter 1991.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
