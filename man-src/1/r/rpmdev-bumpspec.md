---
title: "rpmdev-bumpspec(1)"
name: "rpmdev-bumpspec"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmdev-bumpspec/"
description: "rpmdev-bumpspec – manual page for rpmdev-bumpspec version 1.0.11"
---

<h2>NAME</h2>
<p> rpmdev-bumpspec &#8211; manual page for rpmdev-bumpspec version 1.0.11</p>
<h2>SYNOPSIS</h2>
<p> <code>rpmdev-bumpspec</code> [<i>OPTION</i>]&#8230; <i>SPECFILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> rpmdev-bumpspec bumps release tags in specfiles.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-c</code> COMMENT, <code>&#8211;comment</code>=<i>COMMENT</i></p>
<dd> changelog comment (default: &quot;- rebuilt&quot;)</p>
<dt><code>-u</code> USERSTRING, <code>&#8211;userstring</code>=<i>USERSTRING</i></p>
<dd> user name+email string (default: output from <a href="/docs/linux/man/1-rpmdev-packager/">rpmdev-packager</a>(1))</p>
<dt><code>-r</code>, <code>&#8211;rightmost</code></p>
<dd> bump trailing .&lt;DIGIT&gt; component if found, append .1 if not; no-op if <code>-s</code> is specified</p>
<dt><code>-s</code> STRING, <code>&#8211;string</code>=<i>STRING</i></p>
<dd> bump trailing .STRING&lt;DIGIT&gt; component if found, append .STRING1 if not; trumps <code>-r</code></p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> more output</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> output version number and exit</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005-2010 Fedora Project This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
