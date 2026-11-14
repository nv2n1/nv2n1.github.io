---
title: "gettext(1)"
name: "gettext"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gettext/"
description: "gettext – translate message"
---

<h2 class="name">NAME</h2>
<p> gettext &#8211; translate message </p>
<h2>SYNOPSIS</h2>
<p> <code>gettext</code> [<i>,OPTION/</i>] [[<i>,TEXTDOMAIN/</i>] <i>,MSGID/</i>]<br />
 <code>gettext</code> [<i>,OPTION/</i>] <i>,-s /</i>[<i>,MSGID/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>gettext</code> program translates a natural language message into the user&#8217;s language, by looking up the translation in a message catalog. </p>
<p> Display native language translation of a textual message.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;domain</code>=<i>,TEXTDOMAIN/</i></p>
<dd> retrieve translated messages from TEXTDOMAIN</p>
<dt><code>-c</code>, <code>&#8211;context</code>=<i>,CONTEXT/</i></p>
<dd> specify context for MSGID</p>
<dt><code>-e</code></p>
<dd> enable expansion of some escape sequences</p>
<dt><code>-n</code></p>
<dd> suppress trailing newline</p>
<dt><code>-E</code></p>
<dd> (ignored for compatibility)</p>
<dt>[TEXTDOMAIN] MSGID</p>
<dd> retrieve translated message corresponding to MSGID from TEXTDOMAIN</dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> display version information and exit</dl>
<p> If the TEXTDOMAIN parameter is not given, the domain is determined from the environment variable TEXTDOMAIN. If the message catalog is not found in the regular directory, another location can be specified with the environment variable TEXTDOMAINDIR. When used with the <code>-s</code> option the program behaves like the &#8216;echo&#8217; command. But it does not simply copy its arguments to stdout. Instead those messages found in the selected catalog are translated. Standard search directory: /usr/share/locale</p>
<h2>AUTHOR</h2>
<p> Written by Ulrich Drepper.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs in the bug tracker at &lt;<a rel="nofollow" href="https://savannah.gnu.org/projects/gettext">https://savannah.gnu.org/projects/gettext</a>&gt; or by email to &lt;bug-gettext [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1995-2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gettext</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gettext</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gettext</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
