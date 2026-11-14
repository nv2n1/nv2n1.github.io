---
title: "jbig2dec(1)"
name: "jbig2dec"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jbig2dec/"
description: "jbig2dec – File format converter specialized in JBIG2 decoding"
---

<h2 class="name">NAME</h2>
<p> jbig2dec &#8211; File format converter specialized in JBIG2 decoding</p>
<h2>SYNOPSIS</h2>
<p> <code>jbig2dec</code> [<i>options</i>] <i>file.jbig2</i><br />
 <code>jbig2dec</code> [<i>options</i>] <i>global-stream page-stream</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>jbig2dec</code> command converts JBIG2 files to png or pbm files. </p>
<p> When passed a single <i>file</i> argument it is interpreted as a JBIG2 file stream, with either sequential or random-access organization. </p>
<p> When passed two stream arguments, they are interpreted as the global and page-specific portions of an embedded organzation, as used in PDF. If a particular page references no global segment stream, /dev/null can be passed for the <i>global-stream</i> argument to request the embedded parser. </p>
<h2>OPTIONS</h2>
<p> The options are as follows:</p>
<dl>
<dt><code>-o</code><i> file</i></p>
<dd> Store the decoded output in <i>file</i>. Defaults to the input with a different extension. Set to <i>&#8211;</i> for standard output.</p>
<dt><code>-t</code><i> type</i></p>
<dd> Force a particular output file format. Supported are <i>png</i> and <i>pbm</i>.</p>
<dt><code>-d</code> or <code>&#8211;dump</code></p>
<dd> Print the structure of the JBIG2 file rather than explicitly decoding it.</p>
<dt><code>&#8211;hash</code></p>
<dd> Print a hash of the decoded document.</p>
<dt><code>-q</code> or <code>&#8211;quiet</code></p>
<dd> Suppress warnings and other diagnostic output.</p>
<dt><code>-v</code> or <code>&#8211;verbose</code></p>
<dd> Report additional information about the decoding process. Pass just <code>-v</code> for information about the file as it&#8217;s being decoded. This is the same as <code>&#8211;verbose=2</code>. Pass <code>&#8211;verbose=3</code> or higher for debugging information.</p>
<dt><code>&#8211;version</code></p>
<dd> Show program version information.</p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd> Show usage summary. </p>
</dl>
<h2>AUTHOR</h2>
<p> jbig2-dev &lt;jbig2-dev [at] ghostscript.com&gt; This manpage was initially written by Sebastian Rasmussen &lt;sebras [at] hotmail.com&gt; for jbig2dec and the Debian Project. </p>
<h2>Index</h2>
