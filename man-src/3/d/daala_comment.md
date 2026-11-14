---
title: "daala_comment(3)"
name: "daala_comment"
section: "3"
letter: "d"
url: "/docs/linux/man/3-daala_comment/"
description: "daala_comment –"
---

<h2 class="name">NAME</h2>
<p> daala_comment &#8211; </p>
<p> The comment information.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;codec.h&gt;</p>
<h3>Data Fields</h3>
<p> char ** <code>user_comments</code><br />
 <i>The array of comment string vectors. </i><br />
 int * <code>comment_lengths</code><br />
 <i>An array of the corresponding lengths of each vector, in bytes. </i><br />
 int <code>comments</code><br />
 <i>The total number of comment strings. </i><br />
 char * <code>vendor</code><br />
 <i>The null-terminated vendor string. </i></p>
<h2>Detailed Description</h2>
<p> The comment information. </p>
<p> This structure holds in the in-stream metadata corresponding to the &#8216;comment&#8217; header packet. The comment header is meant to be used much like someone jotting a quick note on the label of a disc. It should be a short, to the point text note that can be more than a couple words, but not more than a short paragraph. </p>
<p> The metadata is stored as a series of (tag, value) pairs, in length-encoded string vectors. The first occurrence of the &#8216;=&#8217; character delimits the tag and value. A particular tag may occur more than once, and order is significant. The character set encoding for the strings is always UTF-8, but the tag names are limited to ASCII, and treated as case-insensitive. See the Daala specification for details. </p>
<p> In filling in this structure, <code>daala_decode_header_in()</code> will null-terminate the user_comment strings for safety. However, the bitstream format itself treats them as 8-bit clean vectors, possibly containing null characters, and so the length array should be treated as their authoritative length.</p>
<h2>Field Documentation</h2>
<h3>char** daala_comment::user_comments</h3>
<p> The array of comment string vectors.</p>
<h3>int* daala_comment::comment_lengths</h3>
<p> An array of the corresponding lengths of each vector, in bytes.</p>
<h3>int daala_comment::comments</h3>
<p> The total number of comment strings.</p>
<h3>char* daala_comment::vendor</h3>
<p> The null-terminated vendor string. This identifies the software used to encode the stream. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for daala from the source code. </p>
<h2>Index</h2>
