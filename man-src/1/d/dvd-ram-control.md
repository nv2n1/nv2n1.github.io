---
title: "dvd-ram-control(1)"
name: "dvd-ram-control"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvd-ram-control/"
description: "dev-ram-control – checks features of DVD-RAM discs"
---

<h2 class="name">NAME</h2>
<p> dev-ram-control &#8211; checks features of DVD-RAM discs</p>
<h2>SYNOPSIS</h2>
<p> <code>dvd-ram-control</code> [-arre] [-awre] [-rdonly|-rdwr] <i>/dev/dvd</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>dvd-ram-control</code> command allows the user to check/set features of DVD-RAM discs. One such information is the Persistent Write Protection, controlling if the disc can be in read-only mode or if both reads and writes are enabled. It also allows the user to check and or set if Automatic Write Relocation Enable (AWRE) as well as Automatic Read Relocation Enable (ARRE) are enabled or not for a given media. </p>
<h2>SEE ALSO</h2>
<p> Most up-to-date information on dvd+rw-tools is available at <a rel="nofollow" href="http://fy.chalmers.se/~appro/linux/DVD+RW/.">http://fy.chalmers.se/~appro/linux/DVD+RW/.</a> </p>
<p> The manpage for <code><a href="/docs/linux/man/1-growisofs/">growisofs</a></code>(1), <code>dvd+<a href="/docs/linux/man/1-rw-format/">rw-format</a></code>(1), <code>dvd+<a href="/docs/linux/man/1-rw-booktype/">rw-booktype</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> <code>dvd+rw-mediainfo</code> was written by Andy Polyakov &lt;appro [at] fy.chalmers.se&gt;. This manual page was written by Rog&eacute;rio Brito &lt;rbrito [at] ime.usp.br&gt; for the Debian project, but it may be used by others. </p>
<h2>Index</h2>
