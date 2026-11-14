---
title: "initex(1)"
name: "initex"
section: "1"
letter: "i"
url: "/docs/linux/man/1-initex/"
description: "tex, initex – text formatting and typesetting"
---

<h2 class="name">NAME</h2>
<p> tex, initex &#8211; text formatting and typesetting </p>
<h2>SYNOPSIS</h2>
<p> <code>tex</code> [<i>options</i>] [<i></i><code>&amp;</code>format] [<i>file</i>|<i></i><code>\</code>commands]</p>
<h2>DESCRIPTION</h2>
<p> Run the TeX typesetter on <i>file</i>, usually creating <i>file.dvi</i>. If the file argument has no extension, &quot;.tex&quot; will be appended to it. Instead of a filename, a set of TeX commands can be given, the first of which must start with a backslash. With a <code>&amp;</code><i>format</i> argument TeX uses a different set of precompiled commands, contained in <i>format</i><code>.fmt</code>; it is usually better to use the <code>-fmt</code> <i>format</i> option instead. </p>
<p> TeX formats the interspersed text and commands contained in the named files and outputs a typesetter independent file (called <i>DVI</i>, which is short for <i>DeVice Independent</i>). TeX&#8217;s capabilities and language are described in <i>The TeXbook</i>. TeX is normally used with a large body of precompiled macros, and there are several specific formatting systems, such as LaTeX, which require the support of several macro files. </p>
<p> This version of TeX looks at its command line to see what name it was called under. If they exist, then both <code>initex</code> and <code>virtex</code> are symbolic links to the <code>tex</code> executable. When called as <code>initex</code> (or when the <code>-ini</code> option is given) it can be used to precompile macros into a <i>.fmt</i> file. When called as <code>virtex</code> it will use the <i>plain</i> format. When called under any other name, TeX will use that name as the name of the format to use. For example, when called as <code>tex</code> the <i>tex</i> format is used, which is identical to the <i>plain</i> format. The commands defined by the <i>plain</i> format are documented in <i>The TeXbook</i>. Other formats that are often available include <i>latex</i> and <i>amstex</i>. </p>
<p> The non-option command line arguments to the TeX program are passed to it as the first input line. (But it is often easier to type extended arguments as the first input line, since UNIX shells tend to gobble up or misinterpret TeX&#8217;s favorite symbols, like backslashes, unless you quote them.) As described in <i>The TeXbook</i>, that first line should begin with a filename, a <i>
