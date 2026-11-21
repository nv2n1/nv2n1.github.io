---

title: "fc-query(1)"
name: "fc-query"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fc-query/"
---

<p> fc-query &#8211; query font files </p>
<h2>SYNOPSIS</h2>
<p> <code>fc-query</code> [ <code>-Vh</code> ] </p>
<p> <br />
&nbsp;[&nbsp;<code>&nbsp;[&nbsp;-b&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;--ignore-blanks&nbsp;]&nbsp;</code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;<code>&nbsp;[&nbsp;-i&nbsp;</code><i>index</i><code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;--index&nbsp;</code><i>index</i><code>&nbsp;]&nbsp;</code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;<code>&nbsp;[&nbsp;-f&nbsp;</code><i>format</i><code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;--format&nbsp;</code><i>format</i><code>&nbsp;]&nbsp;</code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;<code>--version</code>&nbsp;]&nbsp;<wbr>&nbsp;[&nbsp;<code>--help</code>&nbsp;]&nbsp;<wbr>&nbsp;<i>font-file</i><i>...</i>  </p>
<h2>DESCRIPTION</h2>
<p> <code>fc-query</code> queries <i>font-file</i>(s) using the normal fontconfig rules and prints out font pattern for each face found. If <code>--index</code> is given, only one face of each file is queried, otherwise all faces are queried.  </p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. </p>
<dl>
<dt><code>-b</code></dt>
<dd> <p> Ignore blanks to compute languages </p>
 </dd>
<dt><code>-i</code></dt>
<dd> <p> Only query face indexed <i>index</i> of each file. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Format output according to the format specifier <i>format</i>. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> Show version of the program and exit. </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> Show summary of options. </p>
 </dd>
<dt><i>font-file</i></dt>
<dd> <p> Query <i>font-file</i> for font faces. </p>
 </dd></dl>
<h2>RETURN CODES</h2>
<p> <code>fc-query</code> returns error code 0 for successful parsing, or 1 if any errors occured or if at least one font face could not be opened.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fc-scan/">fc-scan</a></code>(1) <code><a href="/docs/linux/man/3-FcFreeTypeQuery/">FcFreeTypeQuery</a></code>(3) <code><a href="/docs/linux/man/3-FcPatternFormat/">FcPatternFormat</a></code>(3) <code><a href="/docs/linux/man/1-fc-cat/">fc-cat</a></code>(1) <code><a href="/docs/linux/man/1-fc-cache/">fc-cache</a></code>(1) <code><a href="/docs/linux/man/1-fc-list/">fc-list</a></code>(1) <code><a href="/docs/linux/man/1-fc-match/">fc-match</a></code>(1) <code><a href="/docs/linux/man/1-fc-pattern/">fc-pattern</a></code>(1) </p>
<p> The fontconfig user&#8217;s guide, in HTML format: <i>/usr/share/doc/fontconfig/fontconfig-user.html</i>.  </p>
<h2>AUTHOR</h2>
<p> This manual page was updated by Behdad Esfahbod &lt;behdad [at] behdad.org&gt;. </p>
