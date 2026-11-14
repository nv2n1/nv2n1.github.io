---
title: "pitchplay(1)"
name: "pitchplay"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pitchplay/"
description: "pitchplay – wrapper script to play audio tracks with cdda2wav with different pitches through a soundcard (cdda2wav must have soundcard support enabled)."
---

<h2 class="name">NAME</h2>
<p> pitchplay &#8211; wrapper script to play audio tracks with cdda2wav with different pitches through a soundcard (cdda2wav must have soundcard support enabled).</p>
<h2>SYNOPSIS</h2>
<p> <code>pitchplay</code> &lt;track a&gt; &lt;pitch a&gt; &lt;track b&gt; &lt;pitch b&gt;&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>pitchplay</code> allows playback of audio tracks with cdda2wav with pitches specified in percentage with 100% being the original pitch, 50% being one octave lower, 200% one octave higher. </p>
<h2>EXAMPLES</h2>
<p> <code>pitchplay</code> 1 90 3 140 5 50<br />
 will play track 1 with a pitch of 90%, track 3 with a pitch of 140%, and track 5 with a pitch of 50%. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cdda2wav/">cdda2wav</a>(1) </p>
<h2>AUTHOR</h2>
<p> <code>cdda2was</code> was written by Joerg Schilling &lt;js [at] cs.tu-berlin.de&gt; and others. </p>
<p> This manpage describes the program implementation of <code>pitchplay</code> as shipped by the cdrkit distribution. See <code><a rel="nofollow" href="http://alioth.debian.org/projects/debburn/">http://alioth.debian.org/projects/debburn/</a></code> for details. It is a spinoff from the original program distributed by the cdrtools project. However, the cdrtools developers are not involved in the development of this spinoff and therefore shall not be made responsible for any problem caused by it. Do not try to get support for this program by contacting the original authors. </p>
<p> If you have support questions, send them to </p>
<p> <code>debburn-devel [at] lists.alioth.debian.org</code> </p>
<p> If you have definitely found a bug, send a mail to this list or to </p>
<p> <code>submit [at] bugs.debian.org</code> </p>
<p> writing at least a short description into the Subject and &quot;Package: cdrkit&quot; into the first line of the mail body. </p>
<p> This manual page was written by Oleksandr Moskalenko &lt;malex [at] tagancha.org&gt;, for the Debian GNU/Linux system. It may be used by other distributions without contacting the author. Any mistakes or omissions in the manual page are my fault; inquiries about or corrections to this manual page should be directed to me (and not to the primary author). </p>
<h2>Index</h2>
