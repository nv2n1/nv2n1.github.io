---

title: "gst-convert(1)"
name: "gst-convert"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-convert/"
description: "gst-convert – Smalltalk syntax converter and beautifier"
---

<h2>NAME</h2>
<p> gst-convert &#8211; Smalltalk syntax converter and beautifier</p>
<h3>Usage:</h3>
<dl>
<dt>
</dt><dd> gst-convert [OPTION]&#8230; [INFILE [OUTFILE]] gst-convert [OPTION]&#8230; <code>-o</code>|&#8211;output OUTFILE INFILES</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> don&#8217;t show any message</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print extra information while processing</dd>
<dt><code>-f</code>, <code>&#8211;format</code>=<i>FORMAT</i></dt>
<dd> convert from given input format (supported formats are gst, gst2, sif, squeak)</dd>
<dt><code>-F</code>, <code>&#8211;output-format</code>=<i>FORMAT</i> convert to given output format (supported</dt>
<dd> formats are gst, gst2, squeak)</dd>
<dt><code>-C</code>, <code>&#8211;class</code>=<i>REGEX</i></dt>
<dd> convert only classes matching REGEX</dd>
<dt><code>-C</code>, <code>&#8211;class=</code>+REGEX</dt>
<dd> in addition, convert classes matching REGEX</dd>
<dt><code>-C</code>, <code>&#8211;class</code>=<i>-REGEX</i></dt>
<dd> do not convert classes matching REGEX</dd>
<dt><code>-c</code>, <code>&#8211;category</code>=<i>REGEX</i></dt>
<dd> convert only classes whose category matches REGEX</dd>
<dt><code>-c</code>, <code>&#8211;category=</code>+REGEX</dt>
<dd> in addition, convert those whose category matches REGEX</dd>
<dt><code>-c</code>, <code>&#8211;category</code>=<i>-REGEX</i></dt>
<dd> do not convert classes whose category matches REGEX</dd>
<dt><code>-r</code>, <code>&#8211;rule=</code>&#8216;CODE-&gt;REPL&#8217;</dt>
<dd> look for CODE and replace it with REPL</dd>
<dt><code>-o</code>, <code>&#8211;output</code> OUTFILE</dt>
<dd> concatenate multiple input files into a single converted output file</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this message and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> print version information and exit</dd></dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gst-convert</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gst-convert</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info gst</code></dd></dl>
<p> should give you access to the complete manual. </p>
