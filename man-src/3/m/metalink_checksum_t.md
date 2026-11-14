---
title: "metalink_checksum_t(3)"
name: "metalink_checksum_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-metalink_checksum_t/"
description: "metalink_checksum_t – The structure that holds a hash value of an entire resource."
---

<h2>NAME</h2>
<p> metalink_checksum_t &#8211; The structure that holds a hash value of an entire resource. </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/metalink/metalink_types.h">metalink/metalink_types.h</a>&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>metalink_checksum_t</code> is a structure that holds a hash value of an entire resource. It contains a hash value of a resource and its message digest algorithm name. </p>
<h2>STRUCTURE MEMBERS</h2>
<p> char *type;<br />
 char *hash; </p>
<h3>type</h3>
<p> Null terminated string of a message digest algorithm name used to calculate hash value for a resource. </p>
<h3>hash</h3>
<p> Null terminated string of a hash value in ASCII hexadecimal notation. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-metalink_parse_file/">metalink_parse_file</a></code>(3) </p>
<h2>Index</h2>
