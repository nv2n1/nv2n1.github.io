---
title: "btape(8)"
name: "btape"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btape/"
description: "btape – Bacula’s Tape interface test program"
---

<p>&nbsp;<wbr>btape &#8211; Bacula&#8217;s Tape interface test program</p>
<h2>Synopsis</h2>
<p><code>btape</code> [<i>options</i>] <i>device-name</i></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>btape</code> command. </p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-?</code></p>
<dd>Show summary of options and commands.</p>
<dt><code>-b&nbsp;<wbr></code><i>bootstrap</i></p>
<dd>Specify a bootstrap file.</p>
<dt><code>-c&nbsp;<wbr></code><i>config</i></p>
<dd>Specify configuration file.</p>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></p>
<dd>Set debug level to <i>nn</i>.</p>
<dt><code>-p</code></p>
<dd>Proceed inspite of I/O errors.</p>
<dt><code>-s</code></p>
<dd>No signals (for debugging).</p>
<dt><code>-v</code></p>
<dd>Set verbose mode. </p>
</dl>
<h2>Commands</h2>
<dl>
<dt><code>autochanger</code></p>
<dd>test autochanger</p>
<dt><code>bsf</code></p>
<dd>backspace file</p>
<dt><code>bsr</code></p>
<dd>backspace record</p>
<dt><code>cap</code></p>
<dd>list device capabilities</p>
<dt><code>clear</code></p>
<dd>clear tape errors</p>
<dt><code>eod</code></p>
<dd>go to end of Bacula data for append</p>
<dt><code>eom</code></p>
<dd>go to the physical end of medium</p>
<dt><code>fill</code></p>
<dd>fill tape, write onto second volume</p>
<dt><code>unfill</code></p>
<dd>read filled tape</p>
<dt><code>fsf</code></p>
<dd>forward space a file</p>
<dt><code>fsr</code></p>
<dd>forward space a record</p>
<dt><code>help</code></p>
<dd>print this reference</p>
<dt><code>label</code></p>
<dd>write a Bacula label to the tape</p>
<dt><code>load</code></p>
<dd>load a tape</p>
<dt><code>quit</code></p>
<dd>quit btape</p>
<dt><code>rawfill</code></p>
<dd>use write() to fill tape</p>
<dt><code>readlabel</code></p>
<dd>read and print the Bacula tape label</p>
<dt><code>rectest</code></p>
<dd>test record handling functions</p>
<dt><code>rewind</code></p>
<dd>rewind the tape</p>
<dt><code>scan</code></p>
<dd>read() tape block by block to EOT and report</p>
<dt><code>scanblocks</code></p>
<dd>Bacula read block by block to EOT and report</p>
<dt><code>status</code></p>
<dd>print tape status</p>
<dt><code>test</code></p>
<dd>General test Bacula tape functions</p>
<dt><code>weof</code></p>
<dd>write an EOF on the tape</p>
<dt><code>wr</code></p>
<dd>write a single Bacula block</p>
<dt><code>rr</code></p>
<dd>read a single record</p>
<dt><code>rb</code></p>
<dd>read a single bacula block</p>
<dt><code>qfill</code></p>
<dd>quick fill command
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bscan/">bscan</a></code>(1), <code><a href="/docs/linux/man/1-bextract/">bextract</a></code>(1).</p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;.</p>
