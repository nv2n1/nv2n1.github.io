---
title: "lirc-lsremotes(1)"
name: "lirc-lsremotes"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lirc-lsremotes/"
description: "lirc-lsremotes – parse lirc configuration files."
---

<h2>NAME</h2>
<p> lirc-lsremotes &#8211; parse lirc configuration files.</p>
<h2>SYNOPSIS</h2>
<p> <code>lirc-lsremotes [options] &lt;directory&gt;</code><br />
 <code>lirc-lsremotes [options] &lt;file&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> lirc-lsremotes can parse lirc remote configuration files (i. e., lircd.conf) and display a condensed index line, the complete data and/or diagnostics. </p>
<p> When given a directory (first form) it expects this to contain a number of vendor directories, each of which containing one or more configuration files. </p>
<p> In the second form lirc-lsremotes displays remote configurations for a given config file. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;dump</code></p>
<dd> Dump the complete configuration data for listed configurations.</p>
<dt><code>-s, &#8211;silent</code></p>
<dd> Only print diagnostics.</p>
<dt><code>-v &#8211;version</code></p>
<dd> Print version info</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print help message.</dl>
<h2>EXAMPLES</h2>
<p> Print a status line and possible diagnostics for a file: </p>
<pre><code>

$ lirc - lsremotes remotes / hitachi / RM - 466E.lircd.conf

    lirc -
    lsremotes : Warning RM - 466E : you should specify a valid gap value

                                        hitachi;
RM - 466E.lircd.conf;
no_lircmd;
no_photo;
RM - 466E;
timing;
no_raw
</code></pre>
</dl>
<p> List a status line for all remotes under remotes, saving diagnostics into a file:</p>
<dl>
<dt>
<dd> $ lirc-lsremotes remotes &gt; remotes.list 2&gt;warnings.txt </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://sourceforge.net/projects/lirc-remotes">http://sourceforge.net/projects/lirc-remotes</a> </p>
<h2>Index</h2>
