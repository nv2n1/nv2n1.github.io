---
title: "zzip_entry_fread_file_header(3)"
name: "zzip_entry_fread_file_header"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_entry_fread_file_header/"
description: "zzip_entry_data_offset, zzip_entry_fread_file_header, zzip_entry_strdup_name – helper functions for (fseeko) zip access api"
---

<p>zzip_entry_data_offset, zzip_entry_fread_file_header, zzip_entry_strdup_name &#8211; helper functions for (fseeko) zip access api</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/fseeko.h&gt;

zzip_off_t zzip_entry_data_offset((ZZIP_ENTRY * entry));

static zzip_off_t zzip_entry_fread_file_header((ZZIP_ENTRY * entry, struct zzip_file_header *file_header));

zzip__new__ char *zzip_entry_strdup_name((ZZIP_ENTRY * entry));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_entry_data_offset</code> functions returns the seekval offset of the data portion of the file referenced by the given zzip_entry. It requires an intermediate check of the file_header structure (i.e. it reads it from disk). After this call, the contained diskfile readposition is already set to the data_offset returned here. On error -1 is returned. </p>
<p> The <code>zzip_entry_fread_file_header</code> functions read the correspoding struct zzip_file_header from the zip disk of the given &quot;entry&quot;. The returned off_t points to the end of the file_header where the current fseek pointer has stopped. This is used to immediatly parse out any filename/extras block following the file_header. The return value is null on error. </p>
<p> The <code>zzip_entry_strdup_name</code> function is a big helper despite its little name: in a zip file the encoded filenames are usually NOT zero-terminated but for common usage with libc we need it that way. Secondly, the filename SHOULD be present in the zip central directory but if not then we fallback to the filename given in the file_header of each compressed data portion.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2003,2004 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
