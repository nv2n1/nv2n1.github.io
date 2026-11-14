---
title: "nl-classid-lookup(8)"
name: "nl-classid-lookup"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nl-classid-lookup/"
description: "nl-classid-lookup – Lookup classid definitions"
---

<p>nl-classid-lookup &#8211; Lookup classid definitions</p>
<h2>Synopsis</h2>
<p><code>nl-classid-lookup</code> [<code>-hv</code>] [<code>-r</code>] [<code>&#8211;raw</code>] <i>name</i> </p>
<h2>Description</h2>
<p>nl-classid-lookup searches the classid database for a matching entry. It is used to resolve qdisc/class names to classid values and vice versa. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Print help text to console and exit.</p>
<dt><code>-v</code> or <code>&#8211;version</code></p>
<dd>Print versioning information to console and exit.</p>
<dt><code>-r</code> or <code>&#8211;reverse</code></p>
<dd>Do a reverse lookup. Lookup a classid and print its name.</p>
<dt><code>&#8211;raw</code></p>
<dd>Print the raw classid in hexadecimal format, do not pretty print it. </p>
</dl>
<h2>Usage</h2>
<p>Resolve the qdisc/class name &quot;interactive&quot;: </p>
<dl>
<dd># nl-classid-lookup interactive</dl>
<p> Lookup the name of classid 1:2: </p>
<dl>
<dd># nl-classid-lookup -r 1:2</dl>
<h2>Files</h2>
<p>/etc/libnl/classid</p>
<h2>Author</h2>
<p>Thomas Graf is the original author and current maintainer of libnl and libnl tools. Many people have contributed to it since.</p>
