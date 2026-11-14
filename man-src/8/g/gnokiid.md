---
title: "gnokiid(8)"
name: "gnokiid"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gnokiid/"
description: "gnokiid – create a virtual modem for old Nokia mobile phones"
---

<p>gnokiid &#8211; create a virtual modem for old Nokia mobile phones</p>
<h2>Synopsis</h2>
<p><code>gnokiid</code> <code>gnokiid</code> [<code>&#8211;help</code>|<code>&#8211;version</code>|<code>&#8211;debug</code>] </p>
<h2>Description</h2>
<p><code>gnokiid</code> is a tool from the gnokii tool suite used to create a virtual modem device with a Nokia portable telephone. The virtual modem device is usually accessed via a symbolic link called /dev/gnokii (created automatically by <code><a href="/docs/linux/man/8-mgnokiidev/">mgnokiidev</a></code>(8)). Please note that you don&#8217;t need a virtual modem when you have real modem accepting AT Hayes commands (most of the modern phones). gnokiid was written for the phones that supported data transfer but didn&#8217;t expose AT layer (namely Nokia 6110, 6130, 6150, 5110, 5130). After <code>gnokiid</code> has created the virtual modem, it can be accessed like any other Hayes-compatible modem by such programs as the terminal program <code><a href="/docs/linux/man/1-minicom/">minicom</a></code>(1) or the PPP daemon <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) to make standard data connections to remote computers. The full range of portable telephone functions (SMS messaging, phone book, operator logos, etc.) are accessed using the command-line program <code><a href="/docs/linux/man/1-gnokii/">gnokii</a></code>(1) or the graphical interface program <code><a href="//www.systutorials.com/docs/linux/man/1x-xgnokii/">xgnokii</a></code>(1x). gnokii is a Linux/Unix tool suite and (eventually) modem/fax driver for Nokia mobile phones, released under the GPL. gnokii supports most phones from the 3810/8110 and 5110/6110 series, details including bugs specific to each series appear in the files Docs/README-3810 and Docs/README-6110 respectively. </p>
<h2>Options</h2>
<p>If called without any options, <code>gnokiid</code> will set up a virtual modem device using the settings in <a href="/docs/linux/man/1-gnokii/">gnokii</a>(1) config file (if it exists). Otherwise,</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>print out a short usage message</p>
<dt><code>&#8211;version</code></p>
<dd>print out version, copyright, phone, and serial device info</p>
<dt><code>&#8211;debug</code></p>
<dd>uses STDIN/STDOUT for a virtual modem</dl>
<h2>Diagnostics</h2>
<p>Various error messages are printed to STDERR.</p>
<h2>Bugs</h2>
<p>Hmmm&#8230; </p>
<h2>Author</h2>
<p>Hugh Blemings &lt;hugh at blemings dot org&gt; and Pavel Janik ml. &lt;Pavel.Janik at suse dot cz&gt; are the authors of the gnokii tool suite. </p>
<p> This manual page was written by Erik Rossen &lt;rossen at freesurf dot ch&gt;. </p>
<p> See also Docs/CREDITS from the gnokii sources.</p>
<h2>Copying</h2>
<p>This program is distributed under the GNU Public License Version 2, or (at your option) any later version..</p>
<h2>See Also</h2>
<p>gnokii, xgnokii, mgnokiidev </p>
