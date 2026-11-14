---
title: "apple_mv(1)"
name: "apple_mv"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apple_mv/"
description: "apple_mv – Do an apple move, moving metadata and the resource fork as well"
---

<h2 class="name">NAME</h2>
<p> apple_mv &#8211; Do an apple move, moving metadata and the resource fork as well </p>
<h2>SYNOPSIS</h2>
<p> <code>/usr/bin/apple_mv</code> <i>SOURCE DEST</i> <code>/usr/bin/apple_mv</code> <i>SOURCE</i>&#8230; <i>DIRECTORY</i></p>
<h2>DESCRIPTION</h2>
<p> <code>apple_mv</code> is a perl script to move SOURCE to DEST or multiple SOURCE(s) to DIRECTORY. It also moves the file specific metadata (including resource forks) to the .AppleDouble directory for DEST or DIRECTORY. If the .AppleDouble directory doesn&#8217;t exist for DEST or DIRECTORY it will create it.</p>
<h2>EXAMPLES</h2>
<p> <code>/usr/bin/apple_mv</code> test.text /target/directory/ </p>
<p> <code>/usr/bin/apple_mv</code> test.text /target/directory/test2.text </p>
<p> <code>/usr/bin/apple_mv</code> test.text testing.text /target/directory/</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to the Netatalk-devel list &lt;netatalk-devel [at] lists.sourceforge.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apple_cp/">apple_cp</a></code>(1), <code><a href="/docs/linux/man/1-apple_rm/">apple_rm</a></code>(1). </p>
<h2>Index</h2>
