---
title: "file2brl(1)"
name: "file2brl"
section: "1"
letter: "f"
url: "/docs/linux/man/1-file2brl/"
description: "file2brl – Translate an xml or a text file into an embosser-ready braille file"
---

<h2 class="name">NAME</h2>
<p> file2brl &#8211; Translate an xml or a text file into an embosser-ready braille file </p>
<h2>SYNOPSIS</h2>
<p> <code>file2brl</code> [<i>,OPTION/</i>] [<i>,inputFile/</i>] [<i>,outputFile/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Translate an xml, html or a text file into an embosser-ready braille file. This includes translation into grade two, if desired, mathematical codes, etc. It also includes formatting according to a built-in style sheet which can be modified by the user. </p>
<p> If inputFile is not specified or &#8216;-&#8216; input is taken from stdin. If outputFile is not specified the output is sent to stdout.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> display version information and exit</p>
<dt><code>-f</code>, <code>&#8211;config-file</code></p>
<dd> name a configuration file that specifies how to do the translation</p>
<dt><code>-b</code>, <code>&#8211;backward</code></p>
<dd> backward translation</p>
<dt><code>-r</code>, <code>&#8211;reformat</code></p>
<dd> reformat a braille file</p>
<dt><code>-T</code>, <code>&#8211;text</code></p>
<dd> Treat as text even if xml</p>
<dt><code>-t</code>, <code>&#8211;html</code></p>
<dd> html document, not xhtml</p>
<dt><code>-p</code>, <code>&#8211;poorly-formatted</code></p>
<dd> translate a poorly formatted file</p>
<dt><code>-P</code>, <code>&#8211;paragraph-line</code></p>
<dd> treat each block of text ending in a newline as a paragraph. If there are two newline characters a blank line will be inserted before the next paragraph</p>
<dt><code>-C</code>, <code>&#8211;config-setting</code></p>
<dd> specify particular configuration settings They override any settings that are specified in a config file</p>
<dt><code>-w</code> <code>&#8211;writeable-path</code></p>
<dd> path for temp files and log file</p>
<dt><code>-l</code>, <code>&#8211;log-file</code></p>
<dd> write errors to file2brl.log instead of stderr</dl>
<h2>AUTHOR</h2>
<p> Written by John J. Boyer.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;liblouis-liblouisxml [at] freelists.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 ViewPlus Technologies, Inc. and JJB Software, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>file2brl</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>file2brl</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info liblouisutdml</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
