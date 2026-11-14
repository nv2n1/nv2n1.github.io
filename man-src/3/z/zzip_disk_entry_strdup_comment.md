---
title: "zzip_disk_entry_strdup_comment(3)"
name: "zzip_disk_entry_strdup_comment"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_disk_entry_strdup_comment/"
description: "zzip_disk_entry_to_data, zzip_disk_entry_to_file_header, zzip_disk_entry_strdup_name, zzip_disk_entry_strdup_comment – helper functions for (mmapped) zip access api"
---

<p>zzip_disk_entry_to_data, zzip_disk_entry_to_file_header, zzip_disk_entry_strdup_name, zzip_disk_entry_strdup_comment &#8211; helper functions for (mmapped) zip access api</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/mmapped.h&gt;

zzip_byte_t *zzip_disk_entry_to_data((ZZIP_DISK * disk, struct zzip_disk_entry *entry));

struct zzip_file_header *zzip_disk_entry_to_file_header((ZZIP_DISK * disk, struct zzip_disk_entry *entry));

zzip__new__ char *zzip_disk_entry_strdup_name((ZZIP_DISK * disk, struct zzip_disk_entry *entry));

zzip__new__ char *zzip_disk_entry_strdup_comment((ZZIP_DISK * disk, struct zzip_disk_entry *entry));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_disk_entry_to_data</code> function augments the other zzip_disk_entry_* helpers: here we move a disk_entry pointer (as returned by _find* functions) into a pointer to the data block right after the file_header. Only disk-&gt;buffer would be needed to perform the seek but we check the mmapped range end as well. </p>
<p> The <code>zzip_disk_entry_to_file_header</code> function does half the job of <code>zzip_disk_entry_to_data</code> where it can augment with <code>zzip_file_header_to_data</code> helper from format/fetch.h </p>
<p> The <code>zzip_disk_entry_strdup_name</code> function is a big helper despite its little name: in a zip file the encoded filenames are usually NOT zero-terminated but for common usage with libc we need it that way. Secondly, the filename SHOULD be present in the zip central directory but if not then we fallback to the filename given in the file_header of each compressed data portion. </p>
<p> The <code>zzip_disk_entry_strdup_comment</code> function is similar creating a reference to a zero terminated string but it can only exist in the zip central directory entry.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2003,2004,2006 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
