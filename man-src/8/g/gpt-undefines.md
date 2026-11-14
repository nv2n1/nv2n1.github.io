---
title: "gpt-undefines(8)"
name: "gpt-undefines"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-undefines/"
description: "gpt-undefines – Generate a list of preprocessor macros that are not defined."
---

<p><code>gpt-undefines</code> &#8211; Generate a list of preprocessor macros that are not defined.</p>
<h2>Synopsis</h2>
<p>gpt-undefines [-srcdir=PATH -config -disable-undefs -verbose -help] headers containing defines</p>
<h2>Description</h2>
<p><code>gpt-undefines</code> Generates a list of preprocessor macros that are not defined internally in the source code. Macros that are defined in the header files listed during <code>gpt-undefines</code>&#8216;s invocation will also be excluded.</p>
<h2>Options</h2>
<dl>
<dt>-srcdir=PATH</p>
<dd>Use <font SIZE="-1">PATH</font> as the directory containing the source code. Source code in the entire directory tree will be scanned. Default <font SIZE="-1">PATH</font> is the directory <code>gpt-undefines</code> was invoked in.</p>
<dt>-config</p>
<dd>Prints the list out in a format that can be pasted into an installable header file.</p>
<dt>-disable-undefs</p>
<dd>Do not count commented out undefines as a define. This technique is used by autoconf to indicate a negative test result. Example: </p>
<pre> /* #undef HAVE_TCP_FASTACK */</pre>
</dl>
<h2>Managing Autoconf defines.</h2>
<p>By default the defines tested for by the configure script are stored in a file called <code>config.h</code>. This file should never be installed. to add autoconf defines to config.h simply add the define in the following format to the file acconfig.h: </p>
<pre> #undef AUTOCONF_DEFINE</pre>
<p>acconfig.h is tranformed into a config.h.in by the script <code>autoheader</code>. Then the configure script transform it into config.h. </p>
<p> A problem occurs when the autoconf defines are used in installed header files. In this case the defines should be put in an installable header file using the following format: </p>
<pre> #ifndef AUTOCONF_DEFINE
 #undef AUTOCONF_DEFINE
 #endif</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-autoconf/">autoconf</a></i>(1) <i><a href="/docs/linux/man/1-autoheader/">autoheader</a></i>(1)</p>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
