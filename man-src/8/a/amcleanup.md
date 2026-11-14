---
title: "amcleanup(8)"
name: "amcleanup"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amcleanup/"
description: "amcleanup – run the Amanda cleanup process after a failure"
---

<p>amcleanup &#8211; run the Amanda cleanup process after a failure</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amcleanup</code> [<code>-k</code>] [<code>-p</code>] [<code>-r</code>] [<code>-v</code>] <i>config</i></dl>
<h2>Description</h2>
<p><code>Amcleanup</code></p>
<dd>generates the <i>Amanda Mail Report</i> and updates the Amanda databases after a system failure on a tape server host. This cleanup process is normally done automatically as part of the <code>amdump</code> program, but if <code>amdump</code> cannot complete for some reason (usually because of a tape server host crash), <code>amcleanup</code> must be run some time later (usually during system boot). </p>
<p> The <code>amcleanupdisk</code> program is run with the same [<code>-r</code>] and [<code>-v</code>] options. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about Amanda.</p>
<h2>Options</h2>
<p><code>-k</code></p>
<dl>
<dd>Kill all process listed in the log file are their child. if there is no log file, then kill all amdump and amflush process and their child.</dl>
<p> <code>-p</code></p>
<dl>
<dd>Do the cleanup only if all process listed in the log file are already terminated.</dl>
<p> <code>-r</code></p>
<dl>
<dd>Remove bad file in holding disk. This options is passed to amcleanupdisk.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Generate verbose output. This options is passed to amcleanupdisk.</dl>
<h2>Examples</h2>
<p>This example runs the Amanda cleanup process by hand after a failure. </p>
<pre>% amcleanup daily</pre>
<p>Putting the following line in a system boot script (e.g. /etc/rc.local) runs the Amanda cleanup process as part of the reboot, eliminating the need to run it by hand. </p>
<pre>/usr/local/sbin/amcleanup daily</pre>
<p>If nothing needs to be done, <code>amcleanup</code> exits normally with the message: </p>
<pre>amcleanup: no unprocessed logfile to clean up.</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt;</p>
