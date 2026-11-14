---
title: "dselect-cfg(5)"
name: "dselect-cfg"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dselect-cfg/"
description: "dselect.cfg – dselect configuration file"
---

<p>dselect.cfg &#8211; dselect configuration file</p>
<h2>Description</h2>
<p>This file contains default options for dselect. Each line contains a single option which is exactly the same as a normal command line option for dselect except for the leading hyphens which are not used here. Quotes surrounding option values are stripped. Comments are allowed by starting a line with a hash sign (&quot;<code>#</code>&quot;).</p>
<h2>Files</h2>
<p><i>/etc/dpkg/dselect.cfg.d/[0-9a-zA-Z_-]*</i><br />
 <i>/etc/dpkg/dselect.cfg</i><br />
 <i>~/.dselect.cfg</i></p>
<h2>Author</h2>
<p>See <i>/usr/share/doc/dpkg/THANKS</i> for the list of people who have contributed to <code>dselect</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dselect/">dselect</a></code>(1). </p>
