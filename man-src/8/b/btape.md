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
<dt><code>-?</code></dt>
<dd>Show summary of options and commands.</dd>
<dt><code>-b&nbsp;<wbr></code><i>bootstrap</i></dt>
<dd>Specify a bootstrap file.</dd>
<dt><code>-c&nbsp;<wbr></code><i>config</i></dt>
<dd>Specify configuration file.</dd>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></dt>
<dd>Set debug level to <i>nn</i>.</dd>
<dt><code>-p</code></dt>
<dd>Proceed inspite of I/O errors.</dd>
<dt><code>-s</code></dt>
<dd>No signals (for debugging).</dd>
<dt><code>-v</code></dt>
<dd>Set verbose mode. </dd>
</dl>
<h2>Commands</h2>
<dl>
<dt><code>autochanger</code></dt>
<dd>test autochanger</dd>
<dt><code>bsf</code></dt>
<dd>backspace file</dd>
<dt><code>bsr</code></dt>
<dd>backspace record</dd>
<dt><code>cap</code></dt>
<dd>list device capabilities</dd>
<dt><code>clear</code></dt>
<dd>clear tape errors</dd>
<dt><code>eod</code></dt>
<dd>go to end of Bacula data for append</dd>
<dt><code>eom</code></dt>
<dd>go to the physical end of medium</dd>
<dt><code>fill</code></dt>
<dd>fill tape, write onto second volume</dd>
<dt><code>unfill</code></dt>
<dd>read filled tape</dd>
<dt><code>fsf</code></dt>
<dd>forward space a file</dd>
<dt><code>fsr</code></dt>
<dd>forward space a record</dd>
<dt><code>help</code></dt>
<dd>print this reference</dd>
<dt><code>label</code></dt>
<dd>write a Bacula label to the tape</dd>
<dt><code>load</code></dt>
<dd>load a tape</dd>
<dt><code>quit</code></dt>
<dd>quit btape</dd>
<dt><code>rawfill</code></dt>
<dd>use write() to fill tape</dd>
<dt><code>readlabel</code></dt>
<dd>read and print the Bacula tape label</dd>
<dt><code>rectest</code></dt>
<dd>test record handling functions</dd>
<dt><code>rewind</code></dt>
<dd>rewind the tape</dd>
<dt><code>scan</code></dt>
<dd>read() tape block by block to EOT and report</dd>
<dt><code>scanblocks</code></dt>
<dd>Bacula read block by block to EOT and report</dd>
<dt><code>status</code></dt>
<dd>print tape status</dd>
<dt><code>test</code></dt>
<dd>General test Bacula tape functions</dd>
<dt><code>weof</code></dt>
<dd>write an EOF on the tape</dd>
<dt><code>wr</code></dt>
<dd>write a single Bacula block</dd>
<dt><code>rr</code></dt>
<dd>read a single record</dd>
<dt><code>rb</code></dt>
<dd>read a single bacula block</dd>
<dt><code>qfill</code></dt>
<dd>quick fill command
</dd></dl>
<h2>See Also</h2>
<p><code>bscan</code>(1), <code>bextract</code>(1).</p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;.</p>
