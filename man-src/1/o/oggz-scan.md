---
title: "oggz-scan(1)"
name: "oggz-scan"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggz-scan/"
description: "oggz-scan — Scan an Ogg file and output characteristic landmarks"
---

<h2>NAME</h2>
<p> oggz-scan &#8212; Scan an Ogg file and output characteristic landmarks<br />
&nbsp;<wbr></p>
<h2>SYNOPSIS</h2>
<p> <code>oggz-scan</code> [-k | &#8211;keyframe ] [-o <code>filename</code> | &#8211;output <code>filename</code> ] [-f <code>format</code> | &#8211;format <code>format</code> ] filename </p>
<p> <code>oggz-scan</code> [-h | &#8211;help ] [-v | &#8211;version ]</p>
<h2>Description</h2>
<p> <code>oggz-scan</code> scans the content of an Ogg file and outputs timestamps of characteristic features.</p>
<h2>Options</h2>
<p> <code>oggz-scan</code> accepts the following options:<br />
&nbsp;<wbr></p>
<h3>Output options</h3>
<dl>
<dt>-o <code>filename</code>, &#8211;output <code>filename</code></p>
<dd> Write output to the specified <code>filename</code> instead of printing it to standard output.</p>
<dt>-f <code>format</code>, &#8211;format <code>format</code></p>
<dd> Write output in the specified <code>format</code>. Supported formats are plain, cmml, html. (Default: plain)</dl>
<h3>Feature options</h3>
<dl>
<dt>-k, &#8211;keyframe</p>
<dd> Display timestamps of unforced Theora keyframes.</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt>-h, &#8211;help</p>
<dd> Display usage information and exit.</p>
<dt>-v, &#8211;version</p>
<dd> Output version information and exit.</dl>
<h2>AUTHOR</h2>
<p> Silvia Pfeiffer October 7, 2005;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 CSIRO Australia<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oggz-dump/">oggz-dump</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-info/">oggz-info</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-rip/">oggz-rip</a></code><code>(1)</code>, <code><a href="/docs/linux/man/1-oggz-validate/">oggz-validate</a></code><code>(1)</code> </p>
<h2>Index</h2>
