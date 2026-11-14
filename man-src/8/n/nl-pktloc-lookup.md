---
title: "nl-pktloc-lookup(8)"
name: "nl-pktloc-lookup"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nl-pktloc-lookup/"
description: "nl-pktloc-lookup – Lookup packet location definitions"
---

<p>nl-pktloc-lookup &#8211; Lookup packet location definitions</p>
<h2>Synopsis</h2>
<p><code>nl-pktloc-lookup</code> <i>name</i><br />
 <code>nl-pktloc-lookup &#8211;list</code> </p>
<h2>Description</h2>
<p>nl-pktloc-lookup searches the packet location database for a matching entry. It is used to resolve packet location aliases to their definition, i.e. alignment, layer, offset, and mask. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Print help text to console and exit.</p>
<dt><code>-v</code> or <code>&#8211;version</code></p>
<dd>Print versioning information to console and exit.</p>
<dt><code>-l</code> or <code>&#8211;list</code></p>
<dd>List all packet location definitions.</p>
<dt><code>&#8211;u32=VALUE</code></p>
<dd>Prints the packet location definition in a special format that is understood by iproute2&#8217;s u32 selector parser. It will output a u32 selector which will compare the provided value with the value specified by the packet location. </p>
<p> Please note that due to the limitation of u32, it is not possible to use packet locations based on the link layer. nl-pktloc-lookup will print an error message in this case. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>selector=$(nl-pktloc-lookup &#8211;u32 22 tcp.sport)<br />
&nbsp;<wbr>&nbsp;<wbr>tc filter add&nbsp;<wbr>[&#8230;]&nbsp;<wbr>u32 match&nbsp;<wbr>$(selector)&nbsp;<wbr>flowid 1:2 </p>
</dl>
<h2>Files</h2>
<p>/etc/libnl/pktloc</p>
<h2>Author</h2>
<p>Thomas Graf is the original author and current maintainer of libnl and libnl tools. Many people have contributed to it since.</p>
