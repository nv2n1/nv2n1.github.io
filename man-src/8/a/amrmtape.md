---
title: "amrmtape(8)"
name: "amrmtape"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amrmtape/"
description: "amrmtape – remove a tape from the Amanda database"
---

<p>amrmtape &#8211; remove a tape from the Amanda database</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amrmtape</code> [&#8211;changer&nbsp;<wbr><i>changer-name</i>] [&#8211;cleanup] [&#8211;dryrun] [-n] [&#8211;erase] [&#8211;keep-label] [&#8211;quiet] [-q] [&#8211;verbose] [-v] <i>config</i> <i>label</i></dl>
<h2>Description</h2>
<p><code>Amrmtape</code></p>
<dd>invalidates the contents of an existing backup tape in the configuration database. This is meant as a recovery mechanism when a good backup is damaged either by faulty hardware or user error, e.g. the tape is eaten by the drive or is overwritten. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p><code>&#8211;changer </code><i>changer-name</i></p>
<dl>
<dd>Specify which changer to use when erasing <i>label</i></dl>
<p> <code>&#8211;cleanup</code></p>
<dl>
<dd>Remove logs and indexes associated with <i>label</i>. Otherwise, they&#8217;ll remain until the next run of amdump.</dl>
<p> <code>&#8211;dryrun</code>, <code>-n</code></p>
<dl>
<dd>Generate new <code><a href="/docs/linux/man/5-tapelist/">tapelist</a></code>(5) and database files with <i>label</i> removed, but leave them in /tmp and do not update the original copies.</dl>
<p> <code>&#8211;erase</code></p>
<dl>
<dd>Attempt to erase the data contained on the volume with the given label. This requires that Amanda be able to find that volume using the tape changer. Erasure is not supported by all Amanda devices, and the erasure is not &quot;secure&quot; in the sense that the data can most likely be recovered by someone with the right tools.</dl>
<p> <code>&#8211;keep-label</code></p>
<dl>
<dd>Do not remove <i>label</i> from the tapelist.</dl>
<p> <code>&#8211;verbose</code>, <code>-v</code></p>
<dl>
<dd>List backups of hosts and disks that are being discarded. Enabled by default.</dl>
<p> <code>&#8211;quiet</code>, <code>-q</code></p>
<dl>
<dd>Opposite of <code>-v</code>.</dl>
<h2>Example</h2>
<p>Remove tape labeled <i>DAILY034</i> from the <i>DailySet1</i> configuration. </p>
<pre># amrmtape DailySet1 DAILY034</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amadmin/">amadmin</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Adrian T. Filipi-Martin</code> &lt;atf3r [at] cs.virginia.edu&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
