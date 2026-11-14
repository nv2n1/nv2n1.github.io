---
title: "mgnokiidev(8)"
name: "mgnokiidev"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mgnokiidev/"
description: "mgnokiidev – links /dev/gnokii to a virtual modem"
---

<p>mgnokiidev &#8211; links /dev/gnokii to a virtual modem</p>
<h2>Synopsis</h2>
<p><code>mgnokiidev </code><i>/dev/pts/?</i> </p>
<h2>Description</h2>
<p><code>mgnokiidev</code> is a tool from the gnokii tool suite used to create the link /dev/gnokii that points to a pseudo-tty (/dev/pts/?). It is called after <code>gnokiid</code> has created a virtual modem that is attached to the pty. It&#8217;s operation is transparent under normal usage as gnokiid takes care of calling it when required. Since <code>mgnokiidev</code> must modifiy files in /dev, it must be either run as root or SUID root. The latter is the preferred method. Normally the <code>mgnokiidev</code> binary is chmod 4750 and owned by root.gnokii. gnokii is a Linux/Unix tool suite and (eventually) modem/fax driver for Nokia mobile phones, released under the GPL. gnokii supports most phones from the 3810/8110 and 5110/6110 series, details including bugs specific to each series appear in the files Docs/README-3810 and Docs/README-6110 respectively. </p>
<h2>Diagnostics</h2>
<p>Various error messages are printed to STDERR.</p>
<h2>Bugs</h2>
<p>None reported. </p>
<h2>Author</h2>
<p>Hugh Blemings &lt;hugh [at] blemings.org&gt; and Pavel Janik ml. &lt;Pavel.Janik [at] suse.cz&gt; are the authors of the gnokii tool suite. </p>
<p> This manual page was written by Erik Rossen &lt;rossen [at] freesurf.ch&gt;. </p>
<p> See also Docs/CREDITS from the gnokii sources.</p>
<h2>Copying</h2>
<p>This program is distributed under the GNU Public License.</p>
<h2>See Also</h2>
<p>gnokiid, gnokii </p>
