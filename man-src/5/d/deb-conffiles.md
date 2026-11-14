---
title: "deb-conffiles(5)"
name: "deb-conffiles"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-conffiles/"
description: "deb-conffiles – package conffiles"
---

<p>deb-conffiles &#8211; package conffiles</p>
<h2>Synopsis</h2>
<p><code>DEBIAN/conffiles</code></p>
<h2>Description</h2>
<p>A package declares its list of conffiles by including a <i>conffiles</i> file in its control archive (i.e. <i>DEBIAN/conffiles</i> during package creation). </p>
<p> This file contains a list of files, one per line, with an optional leading flag separated by whitespace. The conffiles must be listed as absolute pathnames. Trailing whitespace will be trimmed, but empty or whitespace-only lines are not accepted. </p>
<p> Files without a flag should exist in the binary package, otherwise <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) will ignore them. </p>
<p> There is currently only one flag supported, <code>remove-on-upgrade</code>, to mark that a conffile needs to be removed on the next upgrade (since dpkg 1.20.6). These files must not exist in the binary package, as both <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) and <code><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></code>(1) will not accept building nor processing such binary packages.</p>
<h2>Example</h2>
<pre> /etc/alternatives/README
 /etc/cron.daily/dpkg
 /etc/dpkg/dpkg.cfg
 /etc/logrotate.d/dpkg
 remove-on-upgrade /etc/some-old-file.conf</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></code>(1), <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
