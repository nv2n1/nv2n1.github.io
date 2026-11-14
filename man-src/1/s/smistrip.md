---
title: "smistrip(1)"
name: "smistrip"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smistrip/"
description: "smistrip – extract MIB or PIB modules from text files, like RFCs or I-Ds"
---

<h2>NAME</h2>
<p> smistrip &#8211; extract MIB or PIB modules from text files, like RFCs or I-Ds</p>
<h2>SYNOPSIS</h2>
<p> <code>smistrip</code> [ <code>-Vhn</code> ] [ <code>-d </code><i>dir</i> ] [ <code>-m </code><i>module</i> ] [ <i>file(s)</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>smistrip</code> program is used to extract MIB and PIB module files from ASCII documents like RFCs or Internet Drafts. Modules are identified by a starting ASN.1 DEFINITIONS clause and the matching END clause. The output is written to files named by the modules&#8217; names.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></p>
<dd> Show the smistrip version and exit.</p>
<dt><code>-h</code></p>
<dd> Show a help text and exit.</p>
<dt><code>-n</code></p>
<dd> Print only what would be extracted, but do not write any output file.</p>
<dt><code>-d </code><i>dir</i></p>
<dd> Write module file(s) to directory <i>dir</i> instead of the current working directory.</p>
<dt><code>-m </code><i>module</i></p>
<dd> Extract only the module <i>module</i> instead of all modules found in the input file(s).</p>
<dt><i>file(s)</i></p>
<dd> The input text file(s) from which modules will be extracted. If no file is given, input is read from stdin.</dl>
<p> Note that <code>smistrip</code> tries to be smart about locating module start and end, detecting page breaks and blank lines near page breaks. It also tries to cut off blank prefixing columns from all lines of a modules. However, there might by documents that cannot be parsed correctly by <code>smistrip</code> and probably produce incorrect output. You might consider to use <code>smilint</code> on every extracted module file to check its syntactical correctness.</p>
<h2>EXAMPLE</h2>
<p> This example extracts only the module IPV6-MIB from the file rfc2465 and writes it to the directory /usr/local/tmp. </p>
<pre>
  $ smistrip -d /usr/local/tmp -m IPV6-MIB rfc2465
</pre>
<h2>SEE ALSO</h2>
<p> The <code><a href="/docs/linux/man/3-libsmi/">libsmi</a></code>(3) project is documented at <code><a rel="nofollow" href="http://www.ibr.cs.tu-bs.de/projects/libsmi/">http://www.ibr.cs.tu-bs.de/projects/libsmi/</a></code>. </p>
<p> <code><a href="/docs/linux/man/1-smilint/">smilint</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> (C) 1999-2004 F. Strauss, TU Braunschweig, Germany &lt;strauss [at] ibr.cs.tu-bs.de&gt;<br />
 (C) 2002 M. Bunkus, TU Braunschweig, Germany &lt;bunkus [at] ibr.cs.tu-bs.de&gt;<br />
 and contributions by many other people. </p>
<h2>Index</h2>
