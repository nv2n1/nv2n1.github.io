---
title: "pmempool-rm(1)"
name: "pmempool-rm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmempool-rm/"
description: "pmempool-rm – Remove (unlink) poolset files"
---

<h2>NAME</h2>
<p> pmempool-rm &#8211; Remove (unlink) poolset files</p>
<h2>SYNOPSIS</h2>
<p> <code>pmempool rm</code> [&lt;options&gt;] &lt;file&gt;..</p>
<h2>DESCRIPTION</h2>
<p> The <code>pmempool</code> invoked with <code>rm</code> command removes (unlinks) all files specified in command line arguments. If the specified file is a poolset file all parts will be removed. All files are removed using the <code>unlink (3)</code> call. Without specifying the <code>-i|&#8211;interactive</code> option, the <code>rm</code> command prompts only before removing <i>write-protected</i> files. If specified file does not exist the <code>rm</code> command terminates with error code. The <code>-f|&#8211;force</code> command ignores non-existing files and never prompts before removing a file. See <code>EXAMPLES</code> section for example usage of the <code>rm</code> command.</p>
<h3>Available options:</h3>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Print help message.</dl>
<p> <code>-v, &#8211;verbose</code></p>
<dl>
<dt>
<dd> Be verbose and print all removing files.</dl>
<p> <code>-s, &#8211;only-pools</code></p>
<dl>
<dt>
<dd> Remove only pool files and do not remove poolset files.</dl>
<p> <code>-f, &#8211;force</code></p>
<dl>
<dt>
<dd> Remove all specified files, ignore not existing files, never prompt.</dl>
<p> <code>-i, &#8211;interactive</code></p>
<dl>
<dt>
<dd> Prompt before removing every single file.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>pmempool rm pool.obj pool.blk</p>
<dd> # Remove specified pool files</p>
<dt>pmempool rm -s pool.set</p>
<dd> # Remove all pool files from the pool.set, do not remove pool.set itself.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmempool/">pmempool</a>(1) <a href="/docs/linux/man/1-pmempool-create/">pmempool-create</a>(1)</code></p>
<h2>PMEMPOOL</h2>
<p> Part of the <code><a href="/docs/linux/man/1-pmempool/">pmempool</a>(1)</code> suite. </p>
<h2>Index</h2>
