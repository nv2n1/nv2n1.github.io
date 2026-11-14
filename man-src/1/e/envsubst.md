---
title: "envsubst(1)"
name: "envsubst"
section: "1"
letter: "e"
url: "/docs/linux/man/1-envsubst/"
description: "envsubst – substitutes environment variables in shell format strings"
---

<h2 class="name">NAME</h2>
<p> envsubst &#8211; substitutes environment variables in shell format strings </p>
<h2>SYNOPSIS</h2>
<p> <code>envsubst</code> [<i>,OPTION/</i>] [<i>,SHELL-FORMAT/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Substitutes the values of environment variables.</p>
<h3>Operation mode:</h3>
<dl>
<dt><code>-v</code>, <code>&#8211;variables</code></p>
<dd> output the variables occurring in SHELL-FORMAT</dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> In normal operation mode, standard input is copied to standard output, with references to environment variables of the form $VARIABLE or ${VARIABLE} being replaced with the corresponding values. If a SHELL-FORMAT is given, only those environment variables that are referenced in SHELL-FORMAT are substituted; otherwise all environment variables references occurring in standard input are substituted. </p>
<p> When <code>&#8211;variables</code> is used, standard input is ignored, and the output consists of the environment variables that are referenced in SHELL-FORMAT, one per line.</p>
<h2>AUTHOR</h2>
<p> Written by Bruno Haible.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs in the bug tracker at &lt;<a rel="nofollow" href="https://savannah.gnu.org/projects/gettext">https://savannah.gnu.org/projects/gettext</a>&gt; or by email to &lt;bug-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2003-2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>envsubst</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>envsubst</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info envsubst</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
