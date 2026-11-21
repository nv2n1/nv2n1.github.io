---
title: "ngettext(1)"
name: "ngettext"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ngettext/"
description: "ngettext – translate message and choose plural form"
---

<h2>SYNOPSIS</h2>
<p> <code>ngettext</code> [<i>,OPTION/</i>] [<i>,TEXTDOMAIN/</i>] <i>,MSGID MSGID-PLURAL COUNT/</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>ngettext</code> program translates a natural language message into the user&#8217;s language, by looking up the translation in a message catalog, and chooses the appropriate plural form, which depends on the number <i>COUNT</i> and the language of the message catalog where the translation was found. </p>
<p> Display native language translation of a textual message whose grammatical form depends on a number.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;domain</code>=<i>,TEXTDOMAIN/</i></dt>
<dd> retrieve translated message from TEXTDOMAIN</dd>
<dt><code>-c</code>, <code>&#8211;context</code>=<i>,CONTEXT/</i></dt>
<dd> specify context for MSGID</dd>
<dt><code>-e</code></dt>
<dd> enable expansion of some escape sequences</dd>
<dt><code>-E</code></dt>
<dd> (ignored for compatibility)</dd>
<dt>[TEXTDOMAIN]</dt>
<dd> retrieve translated message from TEXTDOMAIN</dd>
<dt>MSGID MSGID-PLURAL</dt>
<dd> translate MSGID (singular) / MSGID-PLURAL (plural)</dd>
<dt>COUNT</dt>
<dd> choose singular/plural form based on this value</dd></dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> display version information and exit</dd></dl>
<p> If the TEXTDOMAIN parameter is not given, the domain is determined from the environment variable TEXTDOMAIN. If the message catalog is not found in the regular directory, another location can be specified with the environment variable TEXTDOMAINDIR. Standard search directory: /usr/share/locale</p>
<h2>AUTHOR</h2>
<p> Written by Ulrich Drepper.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs in the bug tracker at &lt;<a rel="nofollow" href="https://savannah.gnu.org/projects/gettext">https://savannah.gnu.org/projects/gettext</a>&gt; or by email to &lt;bug-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-1997, 2000-2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>ngettext</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>ngettext</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info ngettext</code></dd></dl>
<p> should give you access to the complete manual. </p>
