---
title: "nspr-config(1)"
name: "nspr-config"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nspr-config/"
description: "nspr-config – Return meta information about nspr libraries"
---

<h2 class="name">NAME</h2>
<p> nspr-config &#8211; Return meta information about nspr libraries </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>nspr-config</code> [<code>&#8211;prefix</code>] [<code>&#8211;exec-prefix</code>] [<code>&#8211;includedir</code>] [<code>&#8211;libs</code>] [<code>&#8211;cflags</code>] [<code>&#8211;libdir</code>] [<code>&#8211;version</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>nspr-config</code></p>
<dd>is a shell script which can be used to obtain gcc options for building client pacakges of nspr.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;prefix</code></p>
<dl>
<dt>
<dd> Returns the top level system directory under which the nspr libraries are installed.</dl>
<p> <code>&#8211;exec-prefix</code></p>
<dl>
<dt>
<dd> Returns the top level system directory under which any nspr binaries would be installed.</dl>
<p> <code>&#8211;includedir</code> <i>count</i></p>
<dl>
<dt>
<dd> Returns the path to the directory were the nspr headers are installed.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Returns the upstream version of nspr in the form major_version-minor_version-patch_version.</dl>
<p> <code>&#8211;libs</code></p>
<dl>
<dt>
<dd> Returns the compiler linking flags.</dl>
<p> <code>&#8211;cflags</code></p>
<dl>
<dt>
<dd> Returns the compiler include flags.</dl>
<p> <code>&#8211;libdir</code></p>
<dl>
<dt>
<dd> Returns the path to the directory were the nspr libraries are installed.</dl>
<h2>EXAMPLES</h2>
<p> The following example will query for both include path and linkage flags: </p>
<dl>
<dt>
<dd>
<pre>
        /usr/bin/nspr-config --cflags --libs
      
</pre>
</dl>
<h2>FILES</h2>
<p> /usr/bin/nspr-config</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pkg-config/">pkg-config</a>(1)</p>
<h2>AUTHORS</h2>
<p> The NSPR liraries were written and maintained by developers with Netscape, Red Hat, Sun, Oracle, Mozilla, and Google. </p>
<p> Authors: Elio Maldonado &lt;emaldona [at] redhat.com&gt;.</p>
<h2>LICENSE</h2>
<p> Licensed under the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a rel="nofollow" href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> </p>
<h2>Index</h2>
