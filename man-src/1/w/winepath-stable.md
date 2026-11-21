---

title: "winepath-stable(1)"
name: "winepath-stable"
section: "1"
letter: "w"
url: "/docs/linux/man/1-winepath-stable/"
description: "winepath – Tool to convert Unix paths to/from Win32 paths"
---

<p> <code>winepath</code> <i>option </i>{<i>path</i>}</p>
<p> <code>winepath</code> is a tool to convert a Unix path to/from a Win32 (short/long) path compatible with its Microsoft Windows counterpart. </p>
<p> If more than one option is given then the input paths are output in all formats specified, in the order long, short, Unix, Windows. If no option is given the default output is Unix format.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u</code>,<code>&nbsp;&#8211;unix</dt>
<dd> converts a Windows path to a Unix path.</dd>
<dt>-w</code>,<code>&nbsp;&#8211;windows</dt>
<dd> converts a Unix path to a long Windows path.</dd>
<dt>-l</code>,<code>&nbsp;&#8211;long</dt>
<dd> converts the short Windows path of an existing file or directory to the long format.</dd>
<dt>-s</code>,<code>&nbsp;&#8211;short</dt>
<dd> converts the long Windows path of an existing file or directory to the short format.</dd>
<dt>-0</dt>
<dd> separate output with \0 character, instead of a newline.  </dd>
<dt>-h</code>,<code>&nbsp;--help</dt>
<dd>  shows winepath help message and exit.  </dd></dl>
 </code> <h2>BUGS</h2>
 Bugs can be reported on the <code>Wine bug tracker</code>  <h2>AVAILABILITY</h2>
 <code>winepath</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code>  <h2>SEE ALSO</h2>
 <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1), <br />
 <code>Wine documentation and support</code> 
