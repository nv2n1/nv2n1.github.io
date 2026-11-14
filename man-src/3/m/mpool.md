---
title: "mpool(3)"
name: "mpool"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mpool/"
description: "mpool – shared memory buffer pool"
---

<p>mpool &#8211; shared memory buffer pool </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;db.h&gt;</code>
<code>#include &lt;mpool.h&gt;</code>
<code>MPOOL *mpool_open(DBT *</code><i>key</i><code>, int </code><i>fd</i><code>, pgno_t </code><i>pagesize</i><code>, pgno_t </code><i>maxcache</i><code>);</code>
<code>void mpool_filter(MPOOL *</code><i>mp</i><code>, void (*pgin)(void *, pgno_t, void *),</code>
<code> void (*</code><i>pgout</i><code>)(void *, pgno_t, void *),</code>
<code> void *</code><i>pgcookie</i><code>);</code>
<code>void *mpool_new(MPOOL *</code><i>mp</i><code>, pgno_t *</code><i>pgnoaddr</i><code>);</code>
<code>void *mpool_get(MPOOL *</code><i>mp</i><code>, pgno_t </code><i>pgno</i><code>, unsigned int </code><i>flags</i><code>);</code>
<code>int mpool_put(MPOOL *</code><i>mp</i><code>, void *</code><i>pgaddr</i><code>, unsigned int </code><i>flags</i><code>);</code>
<code>int mpool_sync(MPOOL *</code><i>mp</i><code>);</code>
<code>int mpool_close(MPOOL *</code><i>mp</i><code>);</code></pre>
<h2>Description</h2>
<p><i>Note well</i>: This page documents interfaces provided in glibc up until version 2.1. Since version 2.2, glibc no longer provides these interfaces. Probably, you are looking for the APIs provided by the <i>libdb</i> library instead. </p>
<p> <i>Mpool</i> is the library interface intended to provide page oriented buffer management of files. The buffers may be shared between processes. </p>
<p> The function <code>mpool_open</code>() initializes a memory pool. The <i>key</i> argument is the byte string used to negotiate between multiple processes wishing to share buffers. If the file buffers are mapped in shared memory, all processes using the same key will share the buffers. If <i>key</i> is NULL, the buffers are mapped into private memory. The <i>fd</i> argument is a file descriptor for the underlying file, which must be seekable. If <i>key</i> is non-NULL and matches a file already being mapped, the <i>fd</i> argument is ignored. </p>
<p> The <i>pagesize</i> argument is the size, in bytes, of the pages into which the file is broken up. The <i>maxcache</i> argument is the maximum number of pages from the underlying file to cache at any one time. This value is not relative to the number of processes which share a file&#8217;s buffers, but will be the largest value specified by any of the processes sharing the file. </p>
<p> The <code>mpool_filter</code>() function is intended to make transparent input and output processing of the pages possible. If the <i>pgin</i> function is specified, it is called each time a buffer is read into the memory pool from the backing file. If the <i>pgout</i> function is specified, it is called each time a buffer is written into the backing file. Both functions are called with the <i>pgcookie</i> pointer, the page number and a pointer to the page to being read or written. </p>
<p> The function <code>mpool_new</code>() takes an <i>MPOOL</i> pointer and an address as arguments. If a new page can be allocated, a pointer to the page is returned and the page number is stored into the <i>pgnoaddr</i> address. Otherwise, NULL is returned and <i>errno</i> is set. </p>
<p> The function <code>mpool_get</code>() takes an <i>MPOOL</i> pointer and a page number as arguments. If the page exists, a pointer to the page is returned. Otherwise, NULL is returned and <i>errno</i> is set. The <i>flags</i> argument is not currently used. </p>
<p> The function <code>mpool_put</code>() unpins the page referenced by <i>pgaddr</i>. <i>pgaddr</i> must be an address previously returned by <code>mpool_get</code>() or <code>mpool_new</code>(). The flag value is specified by ORing any of the following values:</p>
<dl COMPACT>
<dt><code>MPOOL_DIRTY</code></p>
<dd>The page has been modified and needs to be written to the backing file.</dl>
<p> <code>mpool_put</code>() returns 0 on success and -1 if an error occurs. </p>
<p> The function <code>mpool_sync</code>() writes all modified pages associated with the <i>MPOOL</i> pointer to the backing file. <code>mpool_sync</code>() returns 0 on success and -1 if an error occurs. </p>
<p> The <code>mpool_close</code>() function free&#8217;s up any allocated memory associated with the memory pool cookie. Modified pages are <code>not</code> written to the backing file. <code>mpool_close</code>() returns 0 on success and -1 if an error occurs.</p>
<h2>Errors</h2>
<p>The <code>mpool_open</code>() function may fail and set <i>errno</i> for any of the errors specified for the library routine <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). </p>
<p> The <code>mpool_get</code>() function may fail and set <i>errno</i> for the following:</p>
<dl COMPACT>
<dt><code>EINVAL</code></p>
<dd>The requested record doesn&#8217;t exist.</dl>
<p> The <code>mpool_new</code>() and <code>mpool_get</code>() functions may fail and set <i>errno</i> for any of the errors specified for the library routines <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), and <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). </p>
<p> The <code>mpool_sync</code>() function may fail and set <i>errno</i> for any of the errors specified for the library routine <code><a href="/docs/linux/man/2-write/">write</a></code>(2). </p>
<p> The <code>mpool_close</code>() function may fail and set <i>errno</i> for any of the errors specified for the library routine <code><a href="/docs/linux/man/3-free/">free</a></code>(3).</p>
<h2>Conforming To</h2>
<p>Not in POSIX.1. Present on the BSDs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-btree/">btree</a></code>(3), <code><a href="/docs/linux/man/3-dbopen/">dbopen</a></code>(3), <code><a href="/docs/linux/man/3-hash/">hash</a></code>(3), <code><a href="/docs/linux/man/3-recno/">recno</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
