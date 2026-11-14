---
title: "zzip_entry_ffile(3)"
name: "zzip_entry_ffile"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_entry_ffile/"
description: "zzip_entry_fopen, zzip_entry_ffile, zzip_entry_fread, zzip_entry_fclose, zzip_entry_feof – open a file within a zip disk for reading"
---

<p>zzip_entry_fopen, zzip_entry_ffile, zzip_entry_fread, zzip_entry_fclose, zzip_entry_feof &#8211; open a file within a zip disk for reading</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/fseeko.h&gt;

zzip__new__ ZZIP_ENTRY_FILE *zzip_entry_fopen((ZZIP_ENTRY * entry, int takeover));

zzip__new__ ZZIP_ENTRY_FILE *zzip_entry_ffile((FILE * disk, char *filename));

zzip_size_t zzip_entry_fread((void *ptr, zzip_size_t sized, zzip_size_t nmemb, ZZIP_ENTRY_FILE *file));

int zzip_entry_fclose((ZZIP_ENTRY_FILE * file));

int zzip_entry_feof((ZZIP_ENTRY_FILE * file));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_entry_fopen</code> function does take an &quot;entry&quot; argument and copies it (or just takes it over as owner) to a new ZZIP_ENTRY_FILE handle structure. That structure contains also a zlib buffer for decoding. The <code>zzip_entry_fopen</code> function does seek to the file_header of the given &quot;entry&quot; and validates it for the data buffer following it. We do also prefetch some data from the data buffer thereby trying to match the disk pagesize for faster access later. The <code>zzip_entry_fread</code> will then read in chunks of pagesizes which is the size of the internal readahead buffer. If an error occurs then null is returned. </p>
<p> The <code>zzip_entry_ffile</code> function opens a file found by name, so it does a search into the zip central directory with <code>zzip_entry_findfile</code> and whatever is found first is given to <code>zzip_entry_fopen</code> </p>
<p> The <code>zzip_entry_fread</code> function reads more bytes into the output buffer specified as arguments. The return value is null on eof or error, the stdio-like interface can not distinguish between these so you need to check with <code>zzip_entry_feof</code> for the difference. </p>
<p> The <code>zzip_entry_fclose</code> function releases any zlib decoder info needed for decompression and dumps the ZZIP_ENTRY_FILE struct then. </p>
<p> The <code>zzip_entry_feof</code> function allows to distinguish an error from an eof condition. Actually, if we found an error but we did already reach eof then we just keep on saying that it was an eof, so the app can just continue.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2003,2004 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
