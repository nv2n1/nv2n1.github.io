---
title: "dh_update_autotools_config(1)"
name: "dh_update_autotools_config"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_update_autotools_config/"
description: "dh_update_autotools_config – Update autotools config files"
---

<h2 class="name">NAME</h2>
<p> dh_update_autotools_config &#8211; Update autotools config files </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_update_autotools_config</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_update_autotools_config</code> replaces all occurrences of <code>config.sub</code> and <code>config.guess</code> in the source tree by the up-to-date versions found in the autotools-dev package. The original files are backed up and restored by <code>dh_clean</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Niels Thykier &lt;niels [at] thykier.net&gt; </p>
<h2>Index</h2>
