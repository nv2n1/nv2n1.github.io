---
title: "metalink_t(3)"
name: "metalink_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-metalink_t/"
description: "metalink_t – Metalink top level structure."
---

<h2>NAME</h2>
<p> metalink_t &#8211; Metalink top level structure.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/metalink/metalink_types.h">metalink/metalink_types.h</a>&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>metalink_t</code> is a top level structure that contains metadata for Metalink file and list of <code><a href="/docs/linux/man/3-metalink_file_t/">metalink_file_t</a></code>(3) structure. Typically <code>metalink_t</code> is created by parser function such as <code><a href="/docs/linux/man/3-metalink_parse_file/">metalink_parse_file</a></code>(3). </p>
<h2>STRUCTURE MEMBERS</h2>
<p> metalink_file_t **files;<br />
 char *identity;<br />
 char *tags; </p>
<h3>files</h3>
<p> Null terminated array of pointer of <code><a href="/docs/linux/man/3-metalink_file_t/">metalink_file_t</a></code>(3) structure. This corresponds to files tag in Metalink XML file. Each <code><a href="/docs/linux/man/3-metalink_file_t/">metalink_file_t</a></code>(3) structure corresponds to file element in Metalink XML file. </p>
<h3>identity</h3>
<p> Null terminated string which corresponds to identity element in Metalink XML file. </p>
<h3>tags</h3>
<p> Null terminated string which corresponds to tags element in Metalink XML file. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-metalink_delete_t/">metalink_delete_t</a></code>(3), <code><a href="/docs/linux/man/3-metalink_file_t/">metalink_file_t</a></code>(3), <code><a href="/docs/linux/man/3-metalink_parse_file/">metalink_parse_file</a></code>(3) </p>
<h2>Index</h2>
