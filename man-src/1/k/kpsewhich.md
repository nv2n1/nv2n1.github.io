---
title: "kpsewhich(1)"
name: "kpsewhich"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kpsewhich/"
description: "kpsewhich – standalone path lookup and and expansion for kpathsea"
---

<h2 class="name">NAME</h2>
<p> kpsewhich &#8211; standalone path lookup and and expansion for kpathsea </p>
<h2>SYNOPSIS</h2>
<p> <code>kpsewhich</code> [<i>options</i>] [<i>filenames</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Kpathsea: A library for path searching</i>. </p>
<p> <code>kpsewhich</code> is used as a standalone front-end of the kpathsea library that can be used to examine variables and find files. When the <code>-format</code> option is not given, the search path used when looking for a file is inferred from the name given, by looking for a known extension. If no known extension is found, the search path for TeX source files is used.</p>
<h2>OPTIONS</h2>
<p> <code>kpsewhich</code> accepts the following options:</p>
<dl>
<dt><code>-debug</code><i>&nbsp;num</i></p>
<dd> Set debugging flags.</p>
<dt><code>-D</code><i>&nbsp;num</i></p>
<dd> Use a base resolution of <i>num</i>; the default, set by the installer, is typically 600.</p>
<dt><code>-dpi</code><i>&nbsp;num</i></p>
<dd> As <code>-D.</code></p>
<dt><code>-engine</code><i>&nbsp;string</i></p>
<dd> Set <i>$engine</i> in the environment, which is used in some search paths.</p>
<dt><code>-expand-braces</code><i>&nbsp;string</i></p>
<dd> Print variable and brace expansion of <i>string</i>.</p>
<dt><code>-expand-path</code><i>&nbsp;string</i></p>
<dd> Print complete path expansion of <i>string</i>.</p>
<dt><code>-expand-var</code><i>&nbsp;string</i></p>
<dd> Print variable expansion of <i>string</i>.</p>
<dt><code>-format</code><i>&nbsp;name</i></p>
<dd> Use file type <i>name</i>. See the info manual for a list of valid names, or use the <code>-help</code> option to print the list.</p>
<dt><code>-help</code></p>
<dd> Print help message and exit.</p>
<dt><code>-interactive</code></p>
<dd> Ask for additional filenames to look up.</p>
<dt><code>-mktex</code><i>&nbsp;fmt</i></p>
<dd> enable mktex<i>fmt</i> generation. (<i>fmt</i>=pk/mf/tex/tfm)</p>
<dt><code>-mode</code><i>&nbsp;string</i></p>
<dd> Set device name for <i>$MAKETEX_MODE</i> to <i>string</i>; no default.</p>
<dt><code>-must-exist</code></p>
<dd> Search the disk as well as ls-R if necessary.</p>
<dt><code>-no-mktex</code><i>&nbsp;fmt</i></p>
<dd> disable mktex<i>fmt</i> generation. (<i>fmt</i>=pk/mf/tex/tfm)</p>
<dt><code>-path</code><i>&nbsp;string</i></p>
<dd> Search in the path <i>string</i>.</p>
<dt><code>-progname</code><i>&nbsp;string</i></p>
<dd> Set program name to <i>string</i>.</p>
<dt><code>-show-path</code><i>&nbsp;name</i></p>
<dd> Output search path for file type <i>name</i>. See the info manual for a list of valid names, or use the <code>-help</code> option to print the list.</p>
<dt><code>-var-value</code><i>&nbsp;variable</i></p>
<dd> Print the expansion of <i>variable</i>.</p>
<dt><code>-version</code></p>
<dd> Print version information and exit.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mktexlsr/">mktexlsr</a></code>(1), <code><a href="/docs/linux/man/1-mktexmf/">mktexmf</a></code>(1), <code><a href="/docs/linux/man/1-mktexpk/">mktexpk</a></code>(1), <code><a href="/docs/linux/man/1-mktextfm/">mktextfm</a></code>(1). </p>
<h2>Index</h2>
