---

title: "fc-match(1)"
name: "fc-match"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fc-match/"
description: "fc-match – match available fonts"
---

<p> <code>fc-match</code> [ <code>-asvVh</code> ] [ <code>&#8211;all</code> ] [ <code>&#8211;sort</code> ] [ <code>&#8211;verbose</code> ] [ <code> [ -f </code><i>format</i><code> ] [ &#8211;format </code><i>format</i><code> ] </code> ] [ <code>&#8211;version</code> ] [ <code>&#8211;help</code> ] </p>
<p>&nbsp;[&nbsp;<i>pattern</i><code>&nbsp;<wbr>&nbsp;[&nbsp;</code><i>element</i><i>&#8230;</i><code>&nbsp;]&nbsp;<wbr>&nbsp;</code>&nbsp;]&nbsp;</p>
<p> <code>fc-match</code> matches <i>pattern</i> (empty pattern by default) using the normal fontconfig matching rules to find the best font available. If <code>&#8211;sort</code> is given, the sorted list of best matching fonts is displayed. The <code>&#8211;all</code> option works like <code>&#8211;sort</code> except that no pruning is done on the list of fonts. </p>
<p> If any elements are specified, only those are printed. Otherwise short file name, family, and style are printed, unless verbose output is requested.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-a</code></dt>
<dd> Displays sorted list of best matching fonts, but do not do any pruning on the list.</dd>
<dt><code>-s</code></dt>
<dd> Displays sorted list of best matching fonts.</dd>
<dt><code>-v</code></dt>
<dd> Print verbose output of the whole font pattern for each match, or <i>element</i>s if any is provided.</dd>
<dt><code>-f</code></dt>
<dd> Format output according to the format specifier <i>format</i>.</dd>
<dt><code>-V</code></dt>
<dd> Show version of the program and exit.</dd>
<dt><code>-h</code></dt>
<dd> Show summary of options.</dd>
<dt><i>pattern</i></dt>
<dd> Displays fonts matching <i>pattern</i> (uses empty pattern by default).</dd>
<dt><i>element</i></dt>
<dd> If set, the <i>element</i> property is displayed for matching fonts.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fc-list/">fc-list</a></code>(1) <code><a href="/docs/linux/man/3-fcfontmatch/">FcFontMatch</a></code>(3) <code><a href="/docs/linux/man/3-fcfontsort/">FcFontSort</a></code>(3) <code><a href="/docs/linux/man/3-fcpatternformat/">FcPatternFormat</a></code>(3) <code><a href="/docs/linux/man/1-fc-cat/">fc-cat</a></code>(1) <code><a href="/docs/linux/man/1-fc-cache/">fc-cache</a></code>(1) <code><a href="/docs/linux/man/1-fc-pattern/">fc-pattern</a></code>(1) <code><a href="/docs/linux/man/1-fc-query/">fc-query</a></code>(1) <code><a href="/docs/linux/man/1-fc-scan/">fc-scan</a></code>(1) </p>
<p> The fontconfig user&#8217;s guide, in HTML format: <i>/usr/share/doc/fontconfig/fontconfig-user.html</i>.</p>
<h2>AUTHOR</h2>
<p> This manual page was updated by Patrick Lam &lt;plam [at] csail.mit.edu&gt;. </p>
