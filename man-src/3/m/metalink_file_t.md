---
title: "metalink_file_t(3)"
name: "metalink_file_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-metalink_file_t/"
description: "metalink_file_t – The structure that holds information of a single file."
---

<h2>NAME</h2>
<p> metalink_file_t &#8211; The structure that holds information of a single file. </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/metalink/metalink_types.h">metalink/metalink_types.h</a>&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>metalink_file_t</code> is a structure that holds information of a single file. It contains array of URLs(<code><a href="/docs/linux/man/3-metalink_resource_t/">metalink_resource_t</a></code>(3)), checksums and metadata for a file. </p>
<h2>STRUCTURE MEMBERS</h2>
<p> char *name;<br />
 long long int size;<br />
 char *version;<br />
 char *language;<br />
 char *os;<br />
 metalink_resource_t **resources;<br />
 int maxconnections;<br />
 metalink_checksum_t **checksums;<br />
 metalink_chunk_checksum_t *chunk_checksum; </p>
<h3>name</h3>
<p> Null terminated file name of the resource which corresponds to name element in Metalink XML file. </p>
<h3>size</h3>
<p> Length of the resource in bytes. </p>
<h3>version</h3>
<p> Null terminated version string which corresponds to version element in Metalink XML file. </p>
<h3>language</h3>
<p> Null terminated language string which corresponds to language element in Metalink XML file. </p>
<h3>os</h3>
<p> Null terminated os string which corresponds to os element in Metalink XML file. </p>
<h3>resources</h3>
<p> Null terminated array of pointer of <code><a href="/docs/linux/man/3-metalink_resource_t/">metalink_resource_t</a></code>(3) structure. This corresponds to resources element in Metalink XML file. Each <code><a href="/docs/linux/man/3-metalink_resource_t/">metalink_resource_t</a></code>(3) structure corresponds to url element in Metalink XML file. </p>
<h3>maxconnections</h3>
<p> This is a value of maxconnections attribute of file element. This value is usually used for upper limit of concurrent connections for the resource. </p>
<h3>checksums</h3>
<p> Null terminated array of pointer of <code><a href="/docs/linux/man/3-metalink_checksum_t/">metalink_checksum_t</a></code>(3) structure. This field is an array because in Metalink specification, verification element can contain multiple hash elements. Each <code><a href="/docs/linux/man/3-metalink_checksum_t/">metalink_checksum_t</a></code>(3) structure corresponds to hash element in Metalink XML file. </p>
<h3>chunk_checksum</h3>
<p> The chunk checksum(aka piece hash) for the resource. This corresponds to pieces element under verification element in Metalink XML file. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-metalink_checksum_t/">metalink_checksum_t</a></code>(3), <code><a href="/docs/linux/man/3-metalink_chunk_checksum_t/">metalink_chunk_checksum_t</a></code>(3), <code><a href="/docs/linux/man/3-metalink_resource_t/">metalink_resource_t</a></code>(3), <code><a href="/docs/linux/man/3-metalink_parse_file/">metalink_parse_file</a></code>(3) </p>
<h2>Index</h2>
