---
title: "btree(3)"
name: "btree"
section: "3"
letter: "b"
url: "/docs/linux/man/3-btree/"
description: "btree – btree database access method"
---

<h2 class="name">NAME</h2>
<p> btree &#8211; btree database access method </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;db.h&gt;
#include &lt;sys/types.h&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>Note well</i>: This page documents interfaces provided in glibc up until version 2.1. Since version 2.2, glibc no longer provides these interfaces. Probably, you are looking for the APIs provided by the <i>libdb</i> library instead. </p>
<p> The routine <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3) is the library interface to database files. One of the supported file formats is btree files. The general description of the database access methods is in <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3), this manual page describes only the btree-specific information. </p>
<p> The btree data structure is a sorted, balanced tree structure storing associated key/data pairs. </p>
<p> The btree access-method-specific data structure provided to <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3) is defined in the <i>&lt;db.h&gt;</i> include file as follows: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;cachesize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;maxkeypage;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;minkeypage;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;psize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(*compare)(const DBT&nbsp;*key1, const DBT&nbsp;*key2);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(*prefix)(const DBT&nbsp;*key1, const DBT&nbsp;*key2);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lorder; } BTREEINFO; </p>
<p> The elements of this structure are as follows:</p>
<dl>
<dt><i>flags</i></p>
<dd> The flag value is specified by ORing any of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>R_DUP</code></p>
<dd> Permit duplicate keys in the tree, that is, permit insertion if the key to be inserted already exists in the tree. The default behavior, as described in <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3), is to overwrite a matching key when inserting a new key or to fail if the <code>R_NOOVERWRITE</code> flag is specified. The <code>R_DUP</code> flag is overridden by the <code>R_NOOVERWRITE</code> flag, and if the <code>R_NOOVERWRITE</code> flag is specified, attempts to insert duplicate keys into the tree will fail.</p>
<dt>
<dd> If the database contains duplicate keys, the order of retrieval of key/data pairs is undefined if the <i>get</i> routine is used, however, <i>seq</i> routine calls with the <code>R_CURSOR</code> flag set will always return the logical &quot;first&quot; of any group of duplicate keys.</dl>
</dl>
<dt><i>cachesize</i></p>
<dd> A suggested maximum size (in bytes) of the memory cache. This value is <i>only</i> advisory, and the access method will allocate more memory rather than fail. Since every search examines the root page of the tree, caching the most recently used pages substantially improves access time. In addition, physical writes are delayed as long as possible, so a moderate cache can reduce the number of I/O operations significantly. Obviously, using a cache increases (but only increases) the likelihood of corruption or lost data if the system crashes while a tree is being modified. If <i>cachesize</i> is 0 (no size is specified), a default cache is used.</p>
<dt><i>maxkeypage</i></p>
<dd> The maximum number of keys which will be stored on any single page. Not currently implemented.</p>
<dt><i>minkeypage</i></p>
<dd> The minimum number of keys which will be stored on any single page. This value is used to determine which keys will be stored on overflow pages, that is, if a key or data item is longer than the pagesize divided by the minkeypage value, it will be stored on overflow pages instead of in the page itself. If <i>minkeypage</i> is 0 (no minimum number of keys is specified), a value of 2 is used.</p>
<dt><i>psize</i></p>
<dd> Page size is the size (in bytes) of the pages used for nodes in the tree. The minimum page size is 512 bytes and the maximum page size is 64 KiB. If <i>psize</i> is 0 (no page size is specified), a page size is chosen based on the underlying filesystem I/O block size.</p>
<dt><i>compare</i></p>
<dd> Compare is the key comparison function. It must return an integer less than, equal to, or greater than zero if the first key argument is considered to be respectively less than, equal to, or greater than the second key argument. The same comparison function must be used on a given tree every time it is opened. If <i>compare</i> is NULL (no comparison function is specified), the keys are compared lexically, with shorter keys considered less than longer keys.</p>
<dt><i>prefix</i></p>
<dd> Prefix is the prefix comparison function. If specified, this routine must return the number of bytes of the second key argument which are necessary to determine that it is greater than the first key argument. If the keys are equal, the key length should be returned. Note, the usefulness of this routine is very data-dependent, but, in some data sets can produce significantly reduced tree sizes and search times. If <i>prefix</i> is NULL (no prefix function is specified), <i>and</i> no comparison function is specified, a default lexical comparison routine is used. If <i>prefix</i> is NULL and a comparison routine is specified, no prefix comparison is done.</p>
<dt><i>lorder</i></p>
<dd> The byte order for integers in the stored database metadata. The number should represent the order as an integer; for example, big endian order would be the number 4,321. If <i>lorder</i> is 0 (no order is specified), the current host order is used.</dl>
<p> If the file already exists (and the <code>O_TRUNC</code> flag is not specified), the values specified for the arguments <i>flags</i>, <i>lorder</i>, and <i>psize</i> are ignored in favor of the values used when the tree was created. </p>
<p> Forward sequential scans of a tree are from the least key to the greatest. </p>
<p> Space freed up by deleting key/data pairs from the tree is never reclaimed, although it is normally made available for reuse. This means that the btree storage structure is grow-only. The only solutions are to avoid excessive deletions, or to create a fresh tree periodically from a scan of an existing one. </p>
<p> Searches, insertions, and deletions in a btree will all complete in O lg base N where base is the average fill factor. Often, inserting ordered data into btrees results in a low fill factor. This implementation has been modified to make ordered insertion the best case, resulting in a much better than normal page fill factor.</p>
<h2>ERRORS</h2>
<p> The <i>btree</i> access method routines may fail and set <i>errno</i> for any of the errors specified for the library routine <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3).</p>
<h2>BUGS</h2>
<p> Only big and little endian byte order is supported.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3), <code><a href="/docs/linux/man/3-hash/">hash</a></code>(3), <code><a href="/docs/linux/man/3-mpool/">mpool</a></code>(3), <code><a href="/docs/linux/man/3-recno/">recno</a></code>(3) </p>
<p> <i>The Ubiquitous B-tree</i>, Douglas Comer, ACM Comput. Surv. 11, 2 (June 1979), 121-138. </p>
<p> <i>Prefix B-trees</i>, Bayer and Unterauer, ACM Transactions on Database Systems, Vol. 2, 1 (March 1977), 11-26. </p>
<p> <i>The Art of Computer Programming Vol. 3: Sorting and Searching</i>, D.E. Knuth, 1968, pp 471-480.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
