---
title: "kbdinfo(1)"
name: "kbdinfo"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kbdinfo/"
description: "kbdinfo – obtain information about the status of a console"
---

<h2 class="name">NAME</h2>
<p> kbdinfo &#8211; obtain information about the status of a console </p>
<h2>SYNOPSIS</h2>
<p> <code>kbdinfo</code> [-C <i>DEVICE</i>] getmode [text|graphics] </p>
<p> <code>kbdinfo</code> [-C <i>DEVICE</i>] gkbmode [raw|xlate|mediumraw|unicode] </p>
<p> <code>kbdinfo</code> [-C <i>DEVICE</i>] gkbmeta [metabit|escprefix] </p>
<p> <code>kbdinfo</code> [-C <i>DEVICE</i>] gkbled [scrolllock|numlock|capslock]</p>
<h2>DESCRIPTION</h2>
<p> <code>kbdinfo</code> is an interface to KDGETMODE, GKBMODE, GKBMETA and GKBLED ioctls. Its primary use case is to query the status of the given <i>CONSOLE</i> (or the currently active one, if no -C option is present) from a shell script. </p>
<p> If the final value argument is not specified, <code>kbdinfo</code> will print the result of the desired ioctl to the standard output. Otherwise, the given value is compared to the actual result, and the utility will exit with a status code of 0 for a match, 1 otherwise. No text is printed for this style of invocation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kbd_mode/">kbd_mode</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> kbdinfo is Copyright &#169; 2011 Alexey Gladkov &lt;gladkov.alexey [at] gmail.com&gt;. </p>
<p> This manual page was written by Michael Schutte &lt;michi [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
