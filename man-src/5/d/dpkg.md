---
title: "dpkg(5)"
name: "dpkg"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dpkg/"
description: "dpkg.cfg – dpkg configuration file"
---

<p>dpkg.cfg &#8211; dpkg configuration file</p>
<h2>Description</h2>
<p>This file contains default options for dpkg. Each line contains a single option which is exactly the same as a normal command line option for dpkg except for the leading hyphens which are not used here. Quotes surrounding option values are stripped. Comments are allowed by starting a line with a hash sign (&quot;<code>#</code>&quot;).</p>
<h2>Files</h2>
<p><i>/etc/dpkg/dpkg.cfg.d/[0-9a-zA-Z_-]*</i><br />
 <i>/etc/dpkg/dpkg.cfg</i><br />
 <i>~/.dpkg.cfg</i></p>
<h2>Author</h2>
<p>See <i>/usr/share/doc/dpkg/THANKS</i> for the list of people who have contributed to <code>dpkg</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
