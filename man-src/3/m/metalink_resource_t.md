---
title: "metalink_resource_t(3)"
name: "metalink_resource_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-metalink_resource_t/"
description: "metalink_resource_t – The structure that holds an URL of a resource and its metadata."
---

<h2>NAME</h2>
<p> metalink_resource_t &#8211; The structure that holds an URL of a resource and its metadata. </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/metalink/metalink_types.h">metalink/metalink_types.h</a>&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>metalink_resource_t</code> is a structure that holds an URL of a resource and its metadata. </p>
<h2>STRUCTURE MEMBERS</h2>
<p> char *url;<br />
 char *type;<br />
 char *location;<br />
 int preference;<br />
 int maxconnections; </p>
<h3>url</h3>
<p> Null terminated string of URL. </p>
<h3>type</h3>
<p> Null terminated string of protocol of URL, like &quot;http&quot;, &quot;ftp&quot;. </p>
<h3>location</h3>
<p> Null terminated string of country code, like &quot;JP&quot;, where the server in URL resides. </p>
<h3>preference</h3>
<p> Preference of this resource. The higher value has bigger preference. </p>
<h3>maxconnections</h3>
<p> Max connections that a client can establish to this resource simultaneously. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-metalink_parse_file/">metalink_parse_file</a></code>(3) </p>
<h2>Index</h2>
