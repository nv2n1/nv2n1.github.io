---
title: "blueproximity(1)"
name: "blueproximity"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blueproximity/"
description: "blueproximity – locks/unlocks your desktop tracking a bluetooth device"
---

<h2>NAME</h2>
<p> blueproximity &#8211; locks/unlocks your desktop tracking a bluetooth device</p>
<h2>SYNOPSIS</h2>
<p> <code>blueproximity</code></p>
<h2>DESCRIPTION</h2>
<p> <code>blueproximity</code> helps you adding a little more security to your desktop. It does so by detecting one of your bluetooth devices, most likely your mobile phone, and keeping track of its distance. If you move away from your computer and the distance is above a certain level (no measurementin meters is possible) for a given time, it automatically locks your desktop (or starts any other shell command you want). Once away, if you return nearer than a given level for a set time your computer unlocks magically without any interaction (or starts any other shell command you want). </p>
<p> Have a look at the package documentation in your distribution&#8217;s doc directory, likely /usr/share/doc/blueproximity, to read the complete html manual or visit the website <a rel="nofollow" href="http://blueproximity.sourceforge.net">http://blueproximity.sourceforge.net</a> .</p>
<h2>OPTIONS</h2>
<p> <code>blueproximity</code> doesn&#8217;t support any command-line parameter.</p>
<h2>FILES</h2>
<p> <i>~/.blueproximityrc</i> <code>The</code>config<code>file</code>containing<code>the</code>user&#8217;s<code>settings.</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> blueproximity was written by Lars Friedrichs &lt;larsfriedrichs [at] gmx.de&gt;. </p>
<p> This manual page was written by Francesco Namuri &lt;francesco [at] namuri.it&gt; and Lars Friedrichs for the Debian project and Ubuntu (but may be used by others). </p>
<h2>Index</h2>
