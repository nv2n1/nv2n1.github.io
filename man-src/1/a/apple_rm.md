---
title: "apple_rm(1)"
name: "apple_rm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apple_rm/"
description: "apple_rm – Do an apple remove, remove metadata and resource fork as well"
---

<h2 class="name">NAME</h2>
<p> apple_rm &#8211; Do an apple remove, remove metadata and resource fork as well </p>
<h2>SYNOPSIS</h2>
<p> <code>/usr/bin/apple_rm</code> <i>FILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>apple_rm</code> is a perl script that removes FILE(s) as well as the .AppleDouble metadata file(s) that corresponds to FILE(s). These AppleDouble header files eventually also contain the resource fork if the files had one. <code>apple_rm</code> does not delete directories.</p>
<h2>EXAMPLES</h2>
<p> <code>/usr/bin/apple_rm</code> test.text </p>
<p> <code>/usr/bin/apple_rm</code> test.text testing.text</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the Netatalk-devel list &lt;netatalk-devel [at] lists.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apple_cp/">apple_cp</a></code>(1), <code><a href="/docs/linux/man/1-apple_mv/">apple_mv</a></code>(1). </p>
<h2>Index</h2>
