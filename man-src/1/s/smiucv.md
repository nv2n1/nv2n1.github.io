---
title: "smiucv(1)"
name: "smiucv"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smiucv/"
description: "smiucv – helper utility that provides an IUCV interface to the z/VM System Management API (SMAPI)."
---

<h2>NAME</h2>
<p> smiucv &#8211; helper utility that provides an IUCV interface to the z/VM System Management API (SMAPI).</p>
<h2>SYNOPSYS</h2>
<p> <code>smiucv</code> [user] [name] &lt;request&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>smiucv</code> is a utility which reads requests from stdin, sends them to the SMAPI server via IUCV and writes the response to stdout. It is intended to be used with the smaclient shell command.</p>
<h2>OPTIONAL PARAMETERS</h2>
<dl>
<dt><code>user</code></p>
<dd> Defaults to VSMREQIU</p>
<dt><code>name</code></p>
<dd> Defaults to DMSRSRQU.</dl>
<h2>AUTHOR</h2>
<p> smiucv written by Leland Lucius. Manpage written by Rafael Fonseca.</p>
<h2>LICENSE</h2>
<p> Released under the Artistic License 2.0. Full license text can be found at <a rel="nofollow" href="http://opensource.org/licenses/artistic-license-2.0">http://opensource.org/licenses/artistic-license-2.0</a> </p>
<h2>Index</h2>
