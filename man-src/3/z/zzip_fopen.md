---
title: "zzip_fopen(3)"
name: "zzip_fopen"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zzip_fopen/"
description: "zzip_fopen, zzip_freopen –"
---

<p>zzip_fopen, zzip_freopen &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;zzip/lib.h&gt;





ZZIP_FILE * zzip_fopen((zzip_char_t * filename, zzip_char_t * mode));


ZZIP_FILE * zzip_freopen((zzip_char_t * filename, zzip_char_t * mode, ZZIP_FILE * stream));</code></pre>
<h2>Description</h2>
<dd>The <code>zzip_fopen</code> function will <code><a href="/docs/linux/man/3-fopen/">fopen</a>(3)</code> a real/zipped file. </p>
<p> It has some magic functionality builtin &#8211; it will first try to open the given <i>filename</i> as a normal file. If it does not exist, the given path to the filename (if any) is split into its directory-part and the file-part. A &quot;.zip&quot; extension is then added to the directory-part to create the name of a zip-archive. That zip-archive (if it exists) is being searched for the file-part, and if found a zzip-handle is returned. </p>
<p> Note that if the file is found in the normal fs-directory the returned structure is mostly empty and the <code>zzip_read</code> call will use the libc <code><a href="/docs/linux/man/2-read/">read</a>(2)</code> to obtain data. Otherwise a <code>zzip_file_open</code> is performed and any error mapped to <code><a href="/docs/linux/man/3-errno/">errno</a>(3)</code>. </p>
<p> unlike the posix-wrapper <code>zzip_open</code> the mode-argument is a string which allows for more freedom to support the extra zzip modes called ZZIP_CASEINSENSITIVE and ZZIP_IGNOREPATH. Currently, this <code>zzip_fopen</code> call will convert the following characters in the mode-string into their corrsponding mode-bits: </p>
<dl>
<dd>&bull; &quot;r&quot; : O_RDONLY : read-only</dl>
<dl>
<dd>&bull; &quot;b&quot; : O_BINARY : binary (win32 specific)</dl>
<dl>
<dd>&bull; &quot;f&quot; : O_NOCTTY : no char device (unix)</dl>
<dl>
<dd>&bull; &quot;i&quot; : ZZIP_CASELESS : inside zip file</dl>
<dl>
<dd>&bull; &quot;*&quot; : ZZIP_NOPATHS : inside zip file only</dl>
<p> all other modes will be ignored for zip-contained entries but they are transferred for compatibility and portability, including these extra sugar bits: </p>
<dl>
<dd>&bull; &quot;x&quot; : O_EXCL : fail if file did exist</dl>
<dl>
<dd>&bull; &quot;s&quot; : O_SYNC : synchronized access</dl>
<dl>
<dd>&bull; &quot;n&quot; : O_NONBLOCK : nonblocking access</dl>
<dl>
<dd>&bull; &quot;z#&quot; : compression level : for zlib</dl>
<dl>
<dd>&bull; &quot;g#&quot; : group access : unix access bits</dl>
<dl>
<dd>&bull; &quot;u#&quot; : owner access : unix access bits</dl>
<dl>
<dd>&bull; &quot;o#&quot; : world access : unix access bits</dl>
<p> &#8230; the access bits are in traditional unix bit format with 7 = read/write/execute, 6 = read/write, 4 = read-only. </p>
<p> The default access mode is 0664, and the compression level is ignored since the lib can not yet write zip files, otherwise it would be the initialisation value for the zlib deflateInit where 0 = no-compression, 1 = best-speed, 9 = best-compression. </p>
<p> The <code>zzip_fopen</code> function returns a new zzip-handle (use <code>zzip_close</code> to return it). On error the <code>zzip_fopen</code> function will return null setting <code><a href="/docs/linux/man/3-errno/">errno</a>(3)</code>. </p>
<p> The <code>zzip_freopen</code> function receives an additional argument pointing to a ZZIP_FILE* being already in use. If this extra argument is null then the <code>zzip_freopen</code> function is identical with calling <code>zzip_fopen</code> </p>
<p> Per default, the old file stream is closed and only the internal structures associated with it are kept. These internal structures may be reused for the return value, and this is a lot quicker when the filename matches a zipped file that is incidently in the very same zip arch as the old filename wrapped in the stream struct. </p>
<p> That&#8217;s simply because the zip arch&#8217;s central directory does not need to be read again. As an extension for the <code>zzip_freopen</code> function, if the mode-string contains a &quot;q&quot; then the old stream is not closed but left untouched, instead it is only given as a hint that a new file handle may share/copy the zip arch structures of the old file handle if that is possible, i.e when they are in the same zip arch. </p>
<p> The <code>zzip_freopen</code> function returns a new zzip-handle (use <code>zzip_close</code> to return it). On error the <code>zzip_freopen</code> function will return null setting <code><a href="/docs/linux/man/3-errno/">errno</a>(3)</code>.</p>
<h2>Author</h2>
<dl>
<dd>&bull; Guido Draheim &lt;guidod [at] gmx.de&gt; Tomi Ollila &lt;Tomi.Ollila [at] iki.fi&gt;</dl>
<h2>Copyright</h2>
<p>Copyright (c) 1999,2000,2001,2002,2003 Guido Draheim All rights reserved, use under the restrictions of the Lesser GNU General Public License or alternatively the restrictions of the Mozilla Public License 1.1</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/2-fopen/">fopen</a>(2) </p>
