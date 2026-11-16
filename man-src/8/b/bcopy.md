---
title: "bcopy(8)"
name: "bcopy"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bcopy/"
description: "bcopy – Bacula’s ‘Copy from tape’"
---

<p>&nbsp;<wbr>bcopy &#8211; Bacula&#8217;s&nbsp;<wbr>&#8216;Copy from tape&#8217;</p>
<h2>Synopsis</h2>
<p><code>bcopy </code> [<i>options</i>] <i>input-archive </i> <i>output-archive</i></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>bcopy</code> command. </p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-?</code></dt>
<dd>Show version and usage of program.</dd>
<dt><code>-b&nbsp;<wbr></code><i>bootstrap</i></dt>
<dd>Specify a bootstrap file.</dd>
<dt><code>-c&nbsp;<wbr></code><i>config</i></dt>
<dd>Specify configuration file.</dd>
<dt><code>-d&nbsp;<wbr></code><i>nn</i></dt>
<dd>Set debug level to <i>nn</i>.</dd>
<dt><code>-dt</code></dt>
<dd>Print timestamp in debug output.</dd>
<dt><code>-i&nbsp;<wbr></code><i>input</i></dt>
<dd>Specify input Volume names (separated by &#8216;|&#8217;)</dd>
<dt><code>-o&nbsp;<wbr></code><i>output</i></dt>
<dd>Specify output Volume names (separated by &#8216;|&#8217;)</dd>
<dt><code>-p</code></dt>
<dd>Proceed in spite of I/O errors.</dd>
<dt><code>-w&nbsp;<wbr></code><i>directory</i></dt>
<dd>Specify working directory (default <i>/tmp</i>).</dd>
<dt><code>-v</code></dt>
<dd>Set verbose mode.</dd></dl>
<h2>See Also</h2>
<p><code>bls</code>(1), <code>bextract</code>(1).</p>
<h2>Author</h2>
<p>This manual page was written by Jose Luis Tallon &lt;jltallon [at] adv-solutions.net&gt;.</p>
