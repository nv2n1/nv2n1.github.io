---
title: "zzip_open(3)"
name: "zzip_open"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_open/"
description: "zzip_open, zzip_open_ext_io, zzip_open_shared_io – …"
---

<p>zzip_open, zzip_open_ext_io, zzip_open_shared_io &#8211; &#8230;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;

ZZIP_FILE *zzip_open((zzip_char_t * filename, int o_flags));

ZZIP_FILE *zzip_open_ext_io((zzip_char_t * filename, int o_flags, int o_modes, zzip_strings_t *ext, zzip_plugin_io_t io));

ZZIP_FILE *zzip_open_shared_io((ZZIP_FILE * stream, zzip_char_t *filename, int o_flags, int o_modes, zzip_strings_t *ext, zzip_plugin_io_t io));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_open_ext_io</code> function uses explicit ext and io instead of the internal defaults, setting them to zero is equivalent to <code>zzip_open</code> </p>
<p> note that the two flag types have been split into an o_flags (for fcntl-like openflags) and o_modes where the latter shall carry the zzip_flags and possibly accessmodes for unix filesystems. Since this version of zziplib can not write zipfiles, it is not yet used for anything else than zzip-specific modeflags. </p>
<p> The <code>zzip_open_ext_io</code> function returns a new zzip-handle (use <code>zzip_close</code> to return it). On error the <code>zzip_open_ext_io</code> function will return null setting <code><a href="/docs/linux/man/3-errno/">errno</a>(3)</code>. </p>
<p> If any ext_io handlers were used then the referenced structure should be static as the allocated ZZIP_FILE does not copy them. </p>
<p> The <code>zzip_open_shared_io</code> function takes an extra stream argument &#8211; if a handle has been then ext/io can be left null and the new stream handle will pick up the ext/io. This should be used only in specific environment however since <code>zzip_file_real</code> does not store any ext-sequence. </p>
<p> The benefit for the <code>zzip_open_shared_io</code> function comes in when the old file handle was openened from a file within a zip archive. When the new file is in the same zip archive then the internal zzip_dir structures will be shared. It is even quicker, as no check needs to be done anymore trying to guess the zip archive place in the filesystem, here we just check whether the zip archive&#8217;s filepath is a prefix part of the filename to be opened. </p>
<p> Note that the <code>zzip_open_shared_io</code> function is also used by <code>zzip_freopen</code> that will unshare the old handle, thereby possibly closing the handle. </p>
<p> The <code>zzip_open_shared_io</code> function returns a new zzip-handle (use <code>zzip_close</code> to return it). On error the <code>zzip_open_shared_io</code> function will return null setting <code><a href="/docs/linux/man/3-errno/">errno</a>(3)</code>.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt; Tomi Ollila &lt;Tomi.Ollila [at] iki.fi&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
