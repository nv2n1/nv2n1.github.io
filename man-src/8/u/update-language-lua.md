---
title: "update-language-lua(8)"
name: "update-language-lua"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-language-lua/"
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
<dt><code>-c</code>, <code>&#8211;conf-file</code>=<i>,FILE/</i></dt>
<dd>file giving additional hyphen specifications</dd>
<dt> <code>-o</code>, <code>&#8211;output-file</code>=<i>,FILE/</i> file to write the output to</dt>
<dt><code>-d</code>, <code>&#8211;output-dir</code>=<i>,DIR/</i></dt>
<dd>
</dd><dd>directory where files are written</dd>
<dt><code>&#8211;checks</code></dt>
<dd>perform sanity checks on the generated config file</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd>don&#8217;t write anything to the standard output during normal operation</dd>
<dt><code>-h</code>, -?, <code>&#8211;help</code></dt>
<dd>display this help message and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd>output version information and exit</dd></dl>
<h2>Files</h2>
<p>The default output directory is</p>
<dl>
<dd><i>,/var/lib/texmf/tex/generic/config/</i></dd></dl>
<p> The default output files are</p>
<dl>
<dt>for update-language-dat</dt>
<dd>language.dat</dd>
<dt>for update-language-def</dt>
<dd>language.def</dd>
<dt>for update-language-lua</dt>
<dd>language.dat.lua</dd></dl>
<p> If <code>-o</code>/&#8211;output-file is given, it overrides all defaults.</p>
