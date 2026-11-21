---

title: "rnano(1)"
name: "rnano"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rnano/"
description: "rnano – a restricted nano"
---

<p> <code>rnano</code> [<i>options</i>] [[+<i>line</i>[,<i>column</i>]]&nbsp;<i>file</i>]&#8230; </p>
<p> <code>rnano</code> runs the <code>nano</code> editor in restricted mode. This allows editing only the specified file or files, and doesn&#8217;t allow the user access to the filesystem nor to a command shell. </p>
<p> In restricted mode, <code>nano</code> will:</p>
<dl>
<dt>&bull;</dt>
<dd> not allow suspending;</dd>
<dt>&bull;</dt>
<dd> not allow saving the current buffer under a different name;</dd>
<dt>&bull;</dt>
<dd> not allow inserting another file or opening a new buffer;</dd>
<dt>&bull;</dt>
<dd> not allow appending or prepending to any file;</dd>
<dt>&bull;</dt>
<dd> not make backup files nor do spell checking. </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show the available command-line options and exit.</dd></dl>
<p> For all existing options, see the <code><a href="/docs/linux/man/1-nano/">nano</a></code>(1) man page. </p>
<h2>BUGS</h2>
<p> Please report bugs via <i><a rel="nofollow" href="https://savannah.gnu.org/bugs/?group=nano">https://savannah.gnu.org/bugs/?group=nano</a></i>. </p>
<h2>HOMEPAGE</h2>
<p> <i><a rel="nofollow" href="https://nano-editor.org/">https://nano-editor.org/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nano/">nano</a></code>(1) </p>
