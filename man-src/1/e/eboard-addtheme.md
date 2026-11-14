---
title: "eboard-addtheme(1)"
name: "eboard-addtheme"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eboard-addtheme/"
description: "eboard-addtheme – a program to easily install new eboard board and sound themes."
---

<h2>NAME</h2>
<p> eboard-addtheme &#8211; a program to easily install new eboard board and sound themes.</p>
<h2>SYNOPSIS</h2>
<p> <code>eboard-addtheme</code> <i>P graphics-file description</i> </p>
<p> <code>eboard-addtheme</code> <i>S sound-file</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page briefly documents the <code>eboard-addtheme</code> command. This manual page was contributed by the developers of the Debian GNU/Linux distribution. </p>
<p> eboard-addtheme installs the given theme for eboard. If it has sufficient permissions, it will install the theme in the system themes directory; otherwise, it will install it in <i>~/.eboard</i>. </p>
<p> eboard-addtheme&#8217;s behavior depends on its first argument. If this argument is <i>P</i>, a graphics file in the proper format should be provided as the second argument, and the third argument should be a description of the theme. The graphics file will be installed as a new piece/board set. If, on the other hand, this argument is <i>S</i>, a sound file should be provided as the second argument; it will be installed as a new sound theme. </p>
<p> eboard must be restarted after a new theme has been added to notice the addition. Graphics become available in the <code>Settings | Bitmapped Piece Sets</code> submenus, sound files become available in the Sound Event configuration dialog boxes. </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Daniel Burrows &lt;dburrows [at] debian.org&gt; (for the Debian GNU/Linux system) and by Felipe Bergo &lt;bergo [at] seul.org&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/6-eboard/">eboard</a></code>(6), <code><a href="/docs/linux/man/1-eboard-config/">eboard-config</a></code>(1) </p>
<h2>Index</h2>
