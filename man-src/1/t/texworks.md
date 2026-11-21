---
title: "texworks(1)"
name: "texworks"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texworks/"
description: "texworks – a simple TeX front-end program"
---

<h2 class="name">NAME</h2>
<p> <code>texworks</code> &#8211; a simple TeX front-end program</p>
<h2>SYNOPSIS</h2>
<p> <code>texworks</code> [OPTIONS] [FILES] </p>
<h2>DESCRIPTION</h2>
<p> <code>TeXworks</code> is an environment for authoring TeX (LaTeX, ConTeXt, etc) documents, with a Unicode-based, TeX-aware editor, integrated PDF viewer, and a clean, simple interface accessible to casual and non-technical users. </p>
<p> It is inspired by Dick Koch&#8217;s award-winning TeXShop program for Mac OS X, which has made quality typesetting through TeX accessible to a wider community of users, without a technical or intimidating face. The goal of <code>TeXworks</code> is to deliver a similarly integrated, easy-to-use environment for users on other platforms, especially GNU/Linux and Windows. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help, -?</code></dt>
<dd> Display a short overview over all command line options</dd>
<dt><code>&#8211;position=, -p</code></dt>
<dd> Open the next specified file at the given position (line or page)</dd>
<dt><code>&#8211;version, -v</code></dt>
<dd> Display version information </dd>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>TW_INIPATH</dt>
<dd> Overrides the location of the preferences file.</dd>
<dt>TW_LIBPATH</dt>
<dd> Overrides the location of the additional configuration and library files.</dd>
<dt>TW_DICPATH</dt>
<dd> Overrides the location of dictionary files.</dd>
<dt>TW_HELPPATH</dt>
<dd> Overrides the location of help files.</dd>
<dt>TW_PLUGINPATH</dt>
<dd> Overrides the location of plugins. </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>~/.config/TUG/TeXworks.conf</i></dt>
<dd> Text file to store the preferences.</dd>
<dt><i>~/.TeXworks/*</i></dt>
<dd> Additional configuration and library files (e.g. for auto completion, templates, etc.).</dd>
<dt><i>/usr/local/bin/texworks-setup.ini</i></dt>
<dd> Setup file to override the location of the files mentioned above (e.g. for enabling portable operation). </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code>TeXworks</code> homepage: <a rel="nofollow" href="http://tug.org/texworks/">http://tug.org/texworks/</a> </p>
<p> <code>TeXworks</code> development: <a rel="nofollow" href="https://github.com/TeXworks/texworks">https://github.com/TeXworks/texworks</a> </p>
<h2>BUGS</h2>
<p> If you find a bug, please report it at <a rel="nofollow" href="https://github.com/TeXworks/texworks/issues">https://github.com/TeXworks/texworks/issues</a> </p>
<h2>AUTHORS</h2>
<p> Jonathan Kew, Stefan Löffler, Charlie Sharpsteen, and others </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007-2016 Jonathan Kew, Stefan Löffler, Charlie Sharpsteen </p>
<p> License GPLv2+: GNU GPL (version 2 or later) &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt; </p>
<p> This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
