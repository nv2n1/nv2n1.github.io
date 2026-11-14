---
title: "convert-ly(1)"
name: "convert-ly"
section: "1"
letter: "c"
url: "/docs/linux/man/1-convert-ly/"
description: "convert-ly – manual page for convert-ly 2.12.2"
---

<h2>NAME</h2>
<p> convert-ly &#8211; manual page for convert-ly 2.12.2</p>
<h2>SYNOPSIS</h2>
<p> <code>convert-ly</code> [<i>OPTION</i>]&#8230; <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> Update LilyPond input to newer version. By default, update from the version taken from the ersion command, to the current LilyPond version.Examples:</p>
<dl>
<dt>
<dd> <tt>$ convert-ly -e old.ly</tt><br />
 <tt>$ convert-ly --from=2.3.28 --to=2.5.21 foobar.ly &gt; foobar-new.ly</tt></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help and exit</p>
<dt><code>-f</code>, <code>&#8211;from</code>=<i>VERSION</i></p>
<dd> start from VERSION [default: ersion found in file]</p>
<dt><code>-e</code>, <code>&#8211;edit</code></p>
<dd> edit in place</p>
<dt><code>-n</code>, <code>&#8211;no-version</code></p>
<dd> do not add ersion command if missing</p>
<dt><code>-c</code>, <code>&#8211;current-version</code></p>
<dd> force updating ersion number to 2.12.2</p>
<dt><code>-s</code>, <code>&#8211;show-rules</code></p>
<dd> show rules [default: <code>-f</code> 0, <code>-t</code> 2.12.2]</p>
<dt><code>-t</code>, <code>&#8211;to</code>=<i>VERSION</i></p>
<dd> convert to VERSION [default: 2.12.2]</p>
<dt><code>-w</code>, <code>&#8211;warranty</code></p>
<dd> show warranty and copyright</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs via <a rel="nofollow" href="http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs">http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs</a></p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>convert-ly</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>convert-ly</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info convert-ly</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
