---
title: "update-language-def(8)"
name: "update-language-def"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-language-def/"
description: "update-language – generate hyphenation configuration for TeX engines"
---

<p>update-language &#8211; generate hyphenation configuration for TeX engines</p>
<h2>Synopsis</h2>
<p><code>update-language(-dat,-def,-lua)</code> [<i>,OPTIONS /</i>&#8230;]</p>
<h2>Description</h2>
<p>Generate hyphenation configuration files language.dat, .def, .dat.lua </p>
<p> When called as update-language, all three configurations files are generated. Otherwise only the selected one.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;conf-file</code>=<i>,FILE/</i></p>
<dd>file giving additional hyphen specifications</p>
<dt> <code>-o</code>, <code>&#8211;output-file</code>=<i>,FILE/</i> file to write the output to</p>
<dt><code>-d</code>, <code>&#8211;output-dir</code>=<i>,DIR/</i></p>
<dd>
<dd>directory where files are written</p>
<dt><code>&#8211;checks</code></p>
<dd>perform sanity checks on the generated config file</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>don&#8217;t write anything to the standard output during normal operation</p>
<dt><code>-h</code>, -?, <code>&#8211;help</code></p>
<dd>display this help message and exit</p>
<dt><code>&#8211;version</code></p>
<dd>output version information and exit</dl>
<h2>Files</h2>
<p>The default output directory is</p>
<dl>
<dd><i>,/var/lib/texmf/tex/generic/config/</i></dl>
<p> The default output files are</p>
<dl>
<dt>for update-language-dat</p>
<dd>language.dat</p>
<dt>for update-language-def</p>
<dd>language.def</p>
<dt>for update-language-lua</p>
<dd>language.dat.lua</dl>
<p> If <code>-o</code>/&#8211;output-file is given, it overrides all defaults.</p>
