---
title: "wrjpgcom(1)"
name: "wrjpgcom"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wrjpgcom/"
description: "wrjpgcom – insert text comments into a JPEG file"
---

<h2 class="name">NAME</h2>
<p> wrjpgcom &#8211; insert text comments into a JPEG file </p>
<h2>SYNOPSIS</h2>
<p> <code>wrjpgcom</code> [ <code>-replace</code> ] [ <code>-comment</code><i> text</i> ] [ <code>-cfile</code><i> name</i> ] [ <i>filename</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>wrjpgcom</code> reads the named JPEG/JFIF file, or the standard input if no file is named, and generates a new JPEG/JFIF file on standard output. A comment block is added to the file. </p>
<p> The JPEG standard allows &quot;comment&quot; (COM) blocks to occur within a JPEG file. Although the standard doesn&#8217;t actually define what COM blocks are for, they are widely used to hold user-supplied text strings. This lets you add annotations, titles, index terms, etc to your JPEG files, and later retrieve them as text. COM blocks do not interfere with the image stored in the JPEG file. The maximum size of a COM block is 64K, but you can have as many of them as you like in one JPEG file. </p>
<p> <code>wrjpgcom</code> adds a COM block, containing text you provide, to a JPEG file. Ordinarily, the COM block is added after any existing COM blocks; but you can delete the old COM blocks if you wish.</p>
<h2>OPTIONS</h2>
<p> Switch names may be abbreviated, and are not case sensitive.</p>
<dl>
<dt><code>-replace</code></p>
<dd> Delete any existing COM blocks from the file.</p>
<dt><code>-comment</code><i> text</i></p>
<dd> Supply text for new COM block on command line.</p>
<dt><code>-cfile</code><i> name</i></p>
<dd> Read text for new COM block from named file.</dl>
<p> If you have only one line of comment text to add, you can provide it on the command line with <code>-comment</code>. The comment text must be surrounded with quotes so that it is treated as a single argument. Longer comments can be read from a text file. </p>
<p> If you give neither <code>-comment</code> nor <code>-cfile,</code> then <code>wrjpgcom</code> will read the comment text from standard input. (In this case an input image file name MUST be supplied, so that the source JPEG file comes from somewhere else.) You can enter multiple lines, up to 64KB worth. Type an end-of-file indicator (usually control-D) to terminate the comment text entry. </p>
<p> <code>wrjpgcom</code> will not add a COM block if the provided comment string is empty. Therefore <code>-replace -comment &quot;&quot;</code> can be used to delete all COM blocks from a file.</p>
<h2>EXAMPLES</h2>
<p> Add a short comment to in.jpg, producing out.jpg:</p>
<dl>
<dt>
<dd> <code>wrjpgcom -c</code> <i>&quot;View of my back yard&quot; in.jpg </i><code>&gt;</code> <i>out.jpg</i></dl>
<p> Attach a long comment previously stored in comment.txt:</p>
<dl>
<dt>
<dd> <code>wrjpgcom</code> <i>in.jpg</i> <code>&lt;</code> <i>comment.txt</i> <code>&gt;</code> <i>out.jpg</i></dl>
<p> or equivalently</p>
<dl>
<dt>
<dd> <code>wrjpgcom</code> <code>-cfile</code> <i>comment.txt</i> <code>&lt;</code> <i>in.jpg</i> <code>&gt;</code> <i>out.jpg</i></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cjpeg/">cjpeg</a></code>(1), <code><a href="/docs/linux/man/1-djpeg/">djpeg</a></code>(1), <code><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></code>(1), <code><a href="/docs/linux/man/1-rdjpgcom/">rdjpgcom</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Independent JPEG Group </p>
<h2>Index</h2>
