---
title: "mkbindic(1)"
name: "mkbindic"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkbindic/"
description: "mkbindic – Convert a text-form dictionary into a binary-form dictionary"
---

<h2>NAME</h2>
<p> mkbindic &#8211; Convert a text-form dictionary into a binary-form dictionary </p>
<h2>SYNOPSYS</h2>
<p> <code>mkbindic [-m | -s] [-name </code><i>dicname</i>] [-c <i>version</i>] <i>textfile</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>mkbindic</code> creates a binary-form dictionary (with extension .cbd or <i>dicname</i>) from a text-form dictionary <i>textfile</i>. With -c mkbindic creates old format dictionary. Current supported <i>version</i>s are 3.0 and 3.7. </p>
<h2>EXAMPLE</h2>
<pre>
<code>% mkbindic user.ctd</code>
A binary-form dictionary user.cbd and a frequency dictionary
user.cld are created from a text-form dictionary user.ctd.
</pre>
<h2>ENVIRONMENT</h2>
<dl>
<dt>TMPDIR</p>
<dd> mkbindic uses the value of this variable for the working directory when it makes temporary files. The value defaults to /tmp if not specified. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dicar/">dicar</a>(1), <a href="/docs/linux/man/1-dpbindic/">dpbindic</a>(1) </p>
<h2>Index</h2>
