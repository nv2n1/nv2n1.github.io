---
title: "zzip_disk_munmap(3)"
name: "zzip_disk_munmap"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_disk_munmap/"
description: "zzip_disk_mmap, zzip_disk_init, zzip_disk_new, zzip_disk_munmap, zzip_disk_open, zzip_disk_buffer, zzip_disk_close – turn a filehandle into a mmapped zip disk archive handle"
---

<p>zzip_disk_mmap, zzip_disk_init, zzip_disk_new, zzip_disk_munmap, zzip_disk_open, zzip_disk_buffer, zzip_disk_close &#8211; turn a filehandle into a mmapped zip disk archive handle</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/mmapped.h&gt;

zzip__new__ ZZIP_DISK *zzip_disk_mmap((int fd));

int zzip_disk_init((ZZIP_DISK * disk, void *buffer, zzip_size_t buflen));

zzip__new__ ZZIP_DISK *zzip_disk_new((void));

int zzip_disk_munmap((ZZIP_DISK * disk));

zzip__new__ ZZIP_DISK *zzip_disk_open((char *filename));

zzip__new__ ZZIP_DISK *zzip_disk_buffer((void *buffer, size_t buflen));

int zzip_disk_close((ZZIP_DISK * disk));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_disk_mmap</code> function uses the given file-descriptor to detect the length of the file and calls the system <code><a href="/docs/linux/man/2-mmap/">mmap</a>(2)</code> to put it in main memory. If it is successful then a newly allocated ZZIP_DISK* is returned with disk-&gt;buffer pointing to the mapview of the zipdisk content. </p>
<p> The <code>zzip_disk_init</code> function does primary initialization of a disk-buffer struct. </p>
<p> The <code>zzip_disk_new</code> function allocates a new disk-buffer with <code><a href="/docs/linux/man/3-malloc/">malloc</a>(3)</code> </p>
<p> The <code>zzip_disk_munmap</code> function is the inverse of <code>zzip_disk_mmap</code> and using the system <a href="/docs/linux/man/2-munmap/">munmap</a>(2) on the buffer area and <code><a href="/docs/linux/man/3-free/">free</a>(3)</code> on the ZZIP_DISK structure. </p>
<p> The <code>zzip_disk_open</code> function opens the given archive by name and turn the filehandle to <code>zzip_disk_mmap</code> for bringing it to main memory. If it can not be <code><a href="/docs/linux/man/2-mmap/">mmap</a>(2)</code>&#8216;ed then we slurp the whole file into a newly <code><a href="/docs/linux/man/2-malloc/">malloc</a>(2)</code>&#8216;ed memory block. Only if that fails too then we return null. Since handling of disk-&gt;buffer is ambigous it should not be snatched away please. </p>
<p> The <code>zzip_disk_buffer</code> function will attach a buffer with a zip image that was acquired from another source than a file. Note that if zzip_disk_mmap fails then zzip_disk_open will fall back and try to read the full file to memory wrapping a ZZIP_DISK around the memory buffer just as the <code>zzip_disk_buffer</code> function will do. Note that the <code>zzip_disk_buffer</code> function will not own the buffer, it will neither be written nor free()d. </p>
<p> The <code>zzip_disk_close</code> function will release all data needed to access a (mmapped) zip archive, including any malloc()ed blocks, sharedmem mappings and it dumps the handle struct as well.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2003,2004,2006 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
