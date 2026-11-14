---
title: "zzip_disk_entry_fopen(3)"
name: "zzip_disk_entry_fopen"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_disk_entry_fopen/"
description: "zzip_disk_fopen, zzip_disk_entry_fopen, zzip_disk_fread, zzip_disk_fclose, zzip_disk_feof – openening a file part wrapped within a (mmapped) zip archive"
---

<p>zzip_disk_fopen, zzip_disk_entry_fopen, zzip_disk_fread, zzip_disk_fclose, zzip_disk_feof &#8211; openening a file part wrapped within a (mmapped) zip archive</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/mmapped.h&gt;

zzip__new__ ZZIP_DISK_FILE *zzip_disk_fopen((ZZIP_DISK * disk, char *filename));

zzip__new__ ZZIP_DISK_FILE *zzip_disk_entry_fopen((ZZIP_DISK * disk, ZZIP_DISK_ENTRY *entry));

zzip_size_t zzip_disk_fread((void *ptr, zzip_size_t sized, zzip_size_t nmemb, ZZIP_DISK_FILE *file));

int zzip_disk_fclose((ZZIP_DISK_FILE * file));

int zzip_disk_feof((ZZIP_DISK_FILE * file));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_disk_fopen</code> function opens a file found by name, so it does a search into the zip central directory with <code>zzip_disk_findfile</code> and whatever is found first is given to <code>zzip_disk_entry_fopen</code> </p>
<p> the ZZIP_DISK_FILE* is rather simple in just encapsulating the arguments given to the <code>zzip_disk_entry_fopen</code> function plus a zlib deflate buffer. Note that the ZZIP_DISK pointer does already contain the full mmapped file area of a zip disk, so open()ing a file part within that area happens to be a lookup of its bounds and encoding. That information is memorized on the ZZIP_DISK_FILE so that subsequent _read() operations will be able to get the next data portion or return an eof condition for that file part wrapped in the zip archive. </p>
<p> The <code>zzip_disk_fread</code> function reads more bytes into the output buffer specified as arguments. The return value is null on eof or error, the stdio-like interface can not distinguish between these so you need to check with <code>zzip_disk_feof</code> for the difference. </p>
<p> The <code>zzip_disk_fclose</code> function releases any zlib decoder info needed for decompression and dumps the ZZIP_DISK_FILE* then. </p>
<p> The <code>zzip_disk_feof</code> function allows to distinguish an error from an eof condition. Actually, if we found an error but we did already reach eof then we just keep on saying that it was an eof, so the app can just continue.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2003,2004,2006 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
