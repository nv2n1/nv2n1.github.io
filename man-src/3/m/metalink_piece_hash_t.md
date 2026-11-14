---
title: "metalink_piece_hash_t(3)"
name: "metalink_piece_hash_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-metalink_piece_hash_t/"
description: "metalink_piece_hash_t – The structure that holds hash value of a piece."
---

<h2>NAME</h2>
<p> metalink_piece_hash_t &#8211; The structure that holds hash value of a piece. </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/metalink/metalink_types.h">metalink/metalink_types.h</a>&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>metalink_piece_hash_t</code> is a structure that holds a hash value of a piece. </p>
<h2>STRUCTURE MEMBERS</h2>
<p> int piece;<br />
 char *hash; </p>
<h3>type</h3>
<p> Index of a piece starting 0. </p>
<h3>hash</h3>
<p> Null terminated string of a hash value in ASCII hexadecimal notation. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-metalink_parse_file/">metalink_parse_file</a></code>(3), </p>
<h2>Index</h2>
