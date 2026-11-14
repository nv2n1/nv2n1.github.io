---
title: "zzip_fstat(3)"
name: "zzip_fstat"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_fstat/"
description: "zzip_dir_stat, zzip_file_stat, zzip_fstat – …"
---

<p>zzip_dir_stat, zzip_file_stat, zzip_fstat &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

int zzip_dir_stat((ZZIP_DIR * dir, zzip_char_t *name, ZZIP_STAT *zs, int flags));

int zzip_file_stat((ZZIP_FILE * file, ZZIP_STAT *zs));

int zzip_fstat((ZZIP_FILE * file, ZZIP_STAT *zs));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_file_stat</code> function will obtain information about a opened file _within_ a zip-archive. The file is supposed to be open (otherwise -1 is returned). The st_size stat-member contains the uncompressed size. The optional d_name is never set here. </p>
<p> The <code>zzip_fstat</code> function will obtain information about a opened file which may be either real/zipped. The file is supposed to be open (otherwise -1 is returned). The st_size stat-member contains the uncompressed size. The optional d_name is never set here. For a real file, we do set the d_csize := st_size and d_compr := 0 for meaningful defaults.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt; Tomi Ollila &lt;Tomi.Ollila [at] iki.fi&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
