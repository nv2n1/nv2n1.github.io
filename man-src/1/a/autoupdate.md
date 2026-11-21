---

title: "autoupdate(1)"
name: "autoupdate"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autoupdate/"
description: "autoupdate – Update a configure.ac to a newer Autoconf"
---

<p> autoupdate &#8211; Update a configure.ac to a newer Autoconf </p>
<h2>SYNOPSIS</h2>
<p> <code>autoupdate</code> [<i>,OPTION/</i>]&#8230; [<i>,TEMPLATE-FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Update each TEMPLATE-FILE if given, or &#8216;configure.ac&#8217; if present, or else &#8216;configure.in&#8217;, to the syntax of the current version of Autoconf. The original files are backed up.</p>
<h3>Operation modes:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> print this help, then exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print version number, then exit</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> verbosely report processing</dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> don&#8217;t remove temporary files</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> consider all files obsolete</dd></dl>
<h3>Library directories:</h3>
<dl>
<dt><code>-B</code>, <code>&#8211;prepend-include</code>=<i>,DIR/</i></dt>
<dd> prepend directory DIR to search path</dd>
<dt><code>-I</code>, <code>&#8211;include</code>=<i>,DIR/</i></dt>
<dd> append directory DIR to search path</dd></dl>
<h2>AUTHOR</h2>
<p> Written by David J. MacKenzie and Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-autoconf [at] gnu.org&gt;.<br />
 GNU Autoconf home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/autoconf/">https://www.gnu.org/software/autoconf/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+/Autoconf: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;, &lt;<a rel="nofollow" href="https://gnu.org/licenses/exceptions.html">https://gnu.org/licenses/exceptions.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autoconf/">autoconf</a></code>(1), <code><a href="/docs/linux/man/1-automake/">automake</a></code>(1), <code><a href="/docs/linux/man/1-autoreconf/">autoreconf</a></code>(1), <code><a href="/docs/linux/man/1-autoupdate/">autoupdate</a></code>(1), <code><a href="/docs/linux/man/1-autoheader/">autoheader</a></code>(1), <code><a href="/docs/linux/man/1-autoscan/">autoscan</a></code>(1), <code><a href="/docs/linux/man/1-config-guess/">config.guess</a></code>(1), <code><a href="/docs/linux/man/1-config-sub/">config.sub</a></code>(1), <code><a href="/docs/linux/man/1-ifnames/">ifnames</a></code>(1), <code><a href="/docs/linux/man/1-libtool/">libtool</a></code>(1). </p>
<p> The full documentation for <code>autoupdate</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>autoupdate</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info autoupdate</code></dd></dl>
<p> should give you access to the complete manual. </p>
