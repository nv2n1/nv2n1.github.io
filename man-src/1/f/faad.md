---
title: "faad(1)"
name: "faad"
section: "1"
letter: "f"
url: "/docs/linux/man/1-faad/"
description: "faad — Process an Advanced Audio Codec stream"
---

<h2>NAME</h2>
<p> faad &#8212; Process an Advanced Audio Codec stream </p>
<h2>SYNOPSIS</h2>
<p> <code>faad </code> [options] [-w | -o &lt;output_filename&gt; | -a &lt;output_filename&gt;] input_filename </p>
<h2>DESCRIPTION</h2>
<p> This utility provides a command line interface to libfaad2. This program reads in MPEG-4 AAC files, processes, and outputs them in either Microsoft WAV, MPEG-4 AAC ADTS, or standard PCM formats. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code><i> &lt;filename&gt;</i><code>, &#8211;adtsout</code><i> &lt;filename&gt;</i></p>
<dd> Sets the processing to output to the specified file in MPEG-4 AAC ADTS format</p>
<dt><code>-b</code><i> &lt;number&gt;</i><code>, &#8211;bits</code><i> &lt;number&gt;</i></p>
<dd> Set the output (individual) sample format. The number takes one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 1: 16-bit PCM data (default).<br />
 2: 24-bit PCM data.<br />
 3: 32-bit PCM data.<br />
 4: 32-bit floatingpe&quot; &quot; &lt;number&gt;&quot; Sets the MPEGpe for the processing to use. The number takes one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 1: Main object type.<br />
 2: Low Complexity (LC) object type (default).<br />
 4: Long Term Prediction (LTP) object type.<br />
 23: Low Delay (LD) object type.</dl>
</dl>
<dl>
<dt><code>-o</code><i> &lt;filename&gt;</i><code>, &#8211;outfile</code><i> &lt;number&gt;</i></p>
<dd> Sets the filename for processing output.</p>
<dt><code>-q , &#8211;quiet</code></p>
<dd> Quiet &#8211; Suppresses status messages during processing.</p>
<dt><code>-t , &#8211;oldformat</code></p>
<dd> Sets the processing to use the old MPEG-4 AAC ADTS format when outputting in said format.</p>
<dt><code>-w , &#8211;stdio</code></p>
<dd> Sets the processing output to be sent to the standard out. </p>
</dl>
</dl>
</dl>
</dl>
<h2>AUTHOR</h2>
<p> Matthew W. S. Bell &lt;matthew (at) bells23.org.uk&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-faac/">faac</a></code>(1) </p>
<h2>Index</h2>
