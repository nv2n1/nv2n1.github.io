---
title: "dump-acct(8)"
name: "dump-acct"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dump-acct/"
description: "dump-acct – print an acct/pacct file in human-readable format"
---

<p>dump-acct &#8211; print an acct/pacct file in human-readable format</p>
<h2>Synopsis</h2>
<p><code>dump-acct</code> [<code>-r</code>|<code>&#8211;reverse</code>] [<code>-R</code>|<code>&#8211;raw</code>] [<code>-n</code>|<code>&#8211;num</code>&nbsp;<wbr><i>recs</i>] [<code>&#8211;byte-swap</code>] [<code>&#8211;format</code>] [<code>&#8211;ahz</code>&nbsp;<wbr><i>freq</i>] [<code>-h</code>|<code>&#8211;help</code>] [<i>files</i>] </p>
<h2>Description</h2>
<p>The dump-acct command transforms the output <code>file</code> from the accton format to the human-readable format: one record per line. Each record consists of severald fields which are separated by character &quot;|&quot; (the meaning of concreate field depends on the version of kernel package &#8211; with which the accton file was created). </p>
<h2>Options</h2>
<p>The following options are supported:</p>
<dl>
<dt><code>-r, &#8211;reverse</code></p>
<dd>Print the output in reverse order.</p>
<dt><code>-R, &#8211;raw</code></p>
<dd>The records will be printed without any parsing.</p>
<dt><code>-n, &#8211;num NUMRECS</code></p>
<dd>Display only the first NUMRECS number of records.</p>
<dt><code>&#8211;byteswap</code></p>
<dd>Swap the bytes (relative to your system&#8217;s native byte order) in &#8211;raw output.</p>
<dt><code>&#8211;format</code></p>
<dd>Set output format with &#8211;raw option.</p>
<dt><code>&#8211;ahz FREQ</code></p>
<dd>Set the AHZ (platform dependent frequency in Hertz) to FREQ.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Print a help message and the default location of the process accounting file and exit. </p>
</dl>
<h2>See Also</h2>
<p>accton (8), lastcomm (1) </p>
