---
title: "ammt(8)"
name: "ammt"
section: "8"
letter: "a"
url: "/docs/linux/man/8-ammt/"
description: "ammt – Amanda version of mt"
---

<p>ammt &#8211; Amanda version of mt</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ammt</code> [-d] [-f | -t | <i>device</i>] <i>command</i> [<i>count</i>]</dl>
<h2>Description</h2>
<p><code>Ammt</code></p>
<dd>provides just enough of the standard UNIX <code>mt</code> command for the needs of <i>Amanda</i>. This is handy when doing a full restore and the standard <code>mt</code> program has not yet been found. </p>
<p> <code>Ammt</code> also provides access to the <i>Amanda</i> output drivers that support various tape simulations. </p>
<p> See the <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8) man page for more details about <i>Amanda</i>. See the <code>OUTPUT DRIVERS</code> section of <i><a href="/docs/linux/man/8-amanda/">amanda</a>(8)</i> for more information on the <i>Amanda</i> output drivers.</p>
<h2>Options</h2>
<p><code>-d</code></p>
<dl>
<dd>Turn on debugging output.</dl>
<p> <code>-f</code><i> device</i></p>
<dl>
<dd>Access tape device <i>device</i>. If not specified, the <code>TAPE</code> environment variable is used.</dl>
<p> <code>-t</code><i> device</i></p>
<dl>
<dd>Same as <code>-f</code>.</dl>
<p> <code>command</code><i> count</i></p>
<dl>
<dd>Which command to issue, and an optional count of operations.</dl>
<h2>Commands</h2>
<p>Each command may be abbreviated to whatever length makes it unique. </p>
<p> <code>eof|weof</code><i> count</i></p>
<dl>
<dd>Write <i>count</i> (default: 1) end of file marks (tapemarks).</dl>
<p> <code>fsf</code><i> count</i></p>
<dl>
<dd>Skip forward <i>count</i> (default: 1) files.</dl>
<p> <code>bsf</code><i> count</i></p>
<dl>
<dd>Skip backward <i>count</i> (default: 1) files.</dl>
<p> <code>asf</code><i> count</i></p>
<dl>
<dd>Position to file number <i>count</i> (default: 0) where zero is beginning of tape. This is the same as a <code>rewind</code> followed by a <code>fsf</code> <i>count</i>.</dl>
<p> <code>rewind</code></p>
<dl>
<dd>Rewind to beginning of tape.</dl>
<p> <code>offline|rewoffl</code></p>
<dl>
<dd>Rewind to beginning of tape and unload the tape from the drive.</dl>
<p> <code>status</code></p>
<dl>
<dd>Report status information about the drive. Which data reported, and what it means, depends on the underlying operating system, and may include: </p>
<p> ONLINE</p>
<dl>
<dd>Indicates the drive is online and ready.</dl>
<p> OFFLINE</p>
<dl>
<dd>Indicates the drive is offline or not ready.</dl>
<p> BOT</p>
<dl>
<dd>Indicates the drive is at beginning of tape.</dl>
<p> EOT</p>
<dl>
<dd>Indicates the drive is at end of tape.</dl>
<p> PROTECTED</p>
<dl>
<dd>Indicates the tape is write protected.</dl>
<p> ds</p>
<dl>
<dd>Device status.</dl>
<p> er</p>
<dl>
<dd>Error register.</dl>
<p> fileno</p>
<dl>
<dd>Current tape file number.</dl>
<p> blkno</p>
<dl>
<dd>Current tape block number file.</dl>
</dl>
<p> Note </p>
<p> Many systems only report good data when a tape is in the drive and ready.</p>
<h2>Author</h2>
<p>Marc Mengel &lt;mengel [at] fnal.gov&gt;, John R. Jackson &lt;jrj [at] purdue.edu&gt;: Original text </p>
<p> Stefan G. Weichinger, &lt;sgw [at] amanda.org&gt;, maintainer of the <i>Amanda</i>-documentation: XML-conversion</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), : <a rel="nofollow" href="http://wiki.zmanda.com">http://wiki.zmanda.com</a> </p>
