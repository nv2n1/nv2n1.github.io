---

title: "fc-list(1)"
name: "fc-list"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fc-list/"
description: "fc-list – list available fonts"
---

<p> <code>fc-list</code> [ <code>-vVh</code> ] [ <code>&#8211;verbose</code> ] [ <code> [ -f </code><i>format</i><code> ] [ &#8211;format </code><i>format</i><code> ] </code> ] [ <code> [ -q ] [ &#8211;quiet ] </code> ] [ <code>&#8211;version</code> ] [ <code>&#8211;help</code> ] </p>
<p>&nbsp;[&nbsp;<i>pattern</i><code>&nbsp;<wbr>&nbsp;[&nbsp;</code><i>element</i><i>&#8230;</i><code>&nbsp;]&nbsp;<wbr>&nbsp;</code>&nbsp;]&nbsp;</p>
<p> <code>fc-list</code> lists fonts and styles available on the system for applications using fontconfig. If any elements are specified, only those are printed. Otherwise family and style are printed, unless verbose output is requested.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-v</code></dt>
<dd> Print verbose output of the whole font pattern for each match, or <i>element</i>s if any is provided.</dd>
<dt><code>-f</code></dt>
<dd> Format output according to the format specifier <i>format</i>.</dd>
<dt><code>-q</code></dt>
<dd> Suppress all normal output. returns 1 as the error code if no fonts matched.</dd>
<dt><code>-V</code></dt>
<dd> Show version of the program and exit.</dd>
<dt><code>-h</code></dt>
<dd> Show summary of options.</dd>
<dt><i>pattern</i></dt>
<dd> If this argument is set, only fonts matching <i>pattern</i> are displayed.</dd>
<dt><i>element</i></dt>
<dd> If set, the <i>element</i> property is displayed for matching fonts.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>fc-list</code></dt>
<dd> Lists all font faces.</dd>
<dt><code>fc-list :lang=hi</code></dt>
<dd> Lists font faces that cover Hindi.</dd>
<dt><code>fc-list : family style file spacing</code></dt>
<dd> Lists the filename and spacing value for each font face. &#8220;:&#8221; is an empty pattern that matches all fonts.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fc-match/">fc-match</a></code>(1) <code><a href="/docs/linux/man/3-fcfontlist/">FcFontList</a></code>(3) <code><a href="/docs/linux/man/3-fcpatternformat/">FcPatternFormat</a></code>(3) <code><a href="/docs/linux/man/1-fc-cat/">fc-cat</a></code>(1) <code><a href="/docs/linux/man/1-fc-cache/">fc-cache</a></code>(1) <code><a href="/docs/linux/man/1-fc-pattern/">fc-pattern</a></code>(1) <code><a href="/docs/linux/man/1-fc-query/">fc-query</a></code>(1) <code><a href="/docs/linux/man/1-fc-scan/">fc-scan</a></code>(1) </p>
<p> The fontconfig user&#8217;s guide, in HTML format: <i>/usr/share/doc/fontconfig/fontconfig-user.html</i>.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Keith Packard &lt;keithp [at] keithp.com&gt; and Josselin Mouette &lt;joss [at] debian.org&gt;. </p>
