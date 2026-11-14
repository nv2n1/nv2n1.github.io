---
title: "metalink_chunk_checksum_t(3)"
name: "metalink_chunk_checksum_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-metalink_chunk_checksum_t/"
description: "metalink_chunk_checksum_t – The structure that holds piece hashes for a resource."
---

<h2>NAME</h2>
<p> metalink_chunk_checksum_t &#8211; The structure that holds piece hashes for a resource. </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/metalink/metalink_types.h">metalink/metalink_types.h</a>&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>metalink_chunk_checksum_t</code> is a structure that holds piece hashes for a resource. It contains length of piece and a message digest algorithm name and each hash value which is stored in <code><a href="/docs/linux/man/3-metalink_piece_hash_t/">metalink_piece_hash_t</a></code>(3). </p>
<h2>STRUCTURE MEMBERS</h2>
<p> char *type;<br />
 int length;<br />
 metalink_piece_hash_t **piece_hashes; </p>
<h3>type</h3>
<p> Null terminated string of a message digest algorithm name used to calculate hash value for a resource. </p>
<h3>length</h3>
<p> Length of a piece in bytes. </p>
<h3>piece_hashes</h3>
<p> Null terminated array of pointer of <code><a href="/docs/linux/man/3-metalink_piece_hash_t/">metalink_piece_hash_t</a></code>(3) structure. They are ordered so that a pointer to <code><a href="/docs/linux/man/3-metalink_piece_hash_t/">metalink_piece_hash_t</a></code>(3) of <i>i</i>th piece can be accessed by piece_hashes[<i>i</i>]. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-metalink_parse_file/">metalink_parse_file</a></code>(3), <code><a href="/docs/linux/man/3-metalink_piece_hash_t/">metalink_piece_hash_t</a></code>(3) </p>
<h2>Index</h2>
