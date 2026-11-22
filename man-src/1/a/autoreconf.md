---

title: "autoreconf(1)"
name: "autoreconf"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autoreconf/"
description: "autoreconf – Update generated configuration files"
---

<p> autoreconf &#8211; Update generated configuration files </p>
<h2>SYNOPSIS</h2>
<p> <code>autoreconf</code> [<i>,OPTION/</i>]&#8230; [<i>,DIRECTORY/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Run &#8216;autoconf&#8217; and, when needed, &#8216;aclocal&#8217;, &#8216;autoheader&#8217;, &#8216;automake&#8217;, &#8216;autopoint&#8217; (formerly &#8216;gettextize&#8217;), &#8216;libtoolize&#8217;, &#8216;intltoolize&#8217;, and &#8216;gtkdocize&#8217; to regenerate the GNU Build System files in specified DIRECTORIES and their subdirectories (defaulting to &#8216;.&#8217;). </p>
<p> By default, it only remakes those files that are older than their sources. If you install new versions of the GNU Build System, you can make &#8216;autoreconf&#8217; remake all of the files by giving it the &#8216;&#8211;force&#8217; option.</p>
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
<dd> consider all generated and standard files obsolete</dd>
<dt><code>-i</code>, <code>&#8211;install</code></dt>
<dd> copy missing standard auxiliary files</dd>
<dt><code>&#8211;no-recursive</code></dt>
<dd> don&#8217;t rebuild sub-packages</dd>
<dt><code>-s</code>, <code>&#8211;symlink</code></dt>
<dd> with <code>-i</code>, install symbolic links instead of copies</dd>
<dt><code>-m</code>, <code>&#8211;make</code></dt>
<dd> when applicable, re-run ./configure &amp;&amp; make</dd>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>,CATEGORY/</i></dt>
<dd> report the warnings falling in CATEGORY [syntax]</dd></dl>
<h3>Warning categories include:</h3>
<dl>
<dt>cross</dt>
<dd> cross compilation issues</dd>
<dt>gnu</dt>
<dd> GNU coding standards (default in gnu and gnits modes)</dd>
<dt>obsolete</dt>
<dd> obsolete features or constructions (default)</dd>
<dt>override</dt>
<dd> user redefinitions of Automake rules or variables</dd>
<dt>portability</dt>
<dd> portability issues (default in gnu and gnits modes)</dd>
<dt>portability-recursive</dt>
<dd> nested Make variables (default with <code>-Wportability</code>)</dd>
<dt>extra-portability</dt>
<dd> extra portability issues related to obscure tools</dd>
<dt>syntax</dt>
<dd> dubious syntactic constructs (default)</dd>
<dt>unsupported</dt>
<dd> unsupported or incomplete features (default)</dd>
<dt>all</dt>
<dd> all the warnings</dd>
<dt>no-CATEGORY</dt>
<dd> turn off warnings in CATEGORY</dd>
<dt>none</dt>
<dd> turn off all the warnings</dd>
<dt>error</dt>
<dd> treat warnings as errors</dd></dl>
<p> The environment variable &#8216;WARNINGS&#8217; is honored. Some subtools might support other warning types, using &#8216;all&#8217; is encouraged.</p>
<h3>Library directories:</h3>
<dl>
<dt><code>-B</code>, <code>&#8211;prepend-include</code>=<i>,DIR/</i></dt>
<dd> prepend directory DIR to search path</dd>
<dt><code>-I</code>, <code>&#8211;include</code>=<i>,DIR/</i></dt>
<dd> append directory DIR to search path</dd></dl>
<p> The environment variables AUTOCONF, ACLOCAL, AUTOHEADER, AUTOM4TE, AUTOMAKE, AUTOPOINT, GTKDOCIZE, INTLTOOLIZE, LIBTOOLIZE, M4, and MAKE are honored.</p>
<h2>AUTHOR</h2>
<p> Written by David J. MacKenzie and Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-autoconf [at] gnu.org&gt;.<br/>
 GNU Autoconf home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/autoconf/">https://www.gnu.org/software/autoconf/</a>&gt;.<br/>
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+/Autoconf: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;, &lt;<a rel="nofollow" href="https://gnu.org/licenses/exceptions.html">https://gnu.org/licenses/exceptions.html</a>&gt;<br/>
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autoconf/">autoconf</a></code>(1), <code><a href="/docs/linux/man/1-automake/">automake</a></code>(1), <code><a href="/docs/linux/man/1-autoreconf/">autoreconf</a></code>(1), <code><a href="/docs/linux/man/1-autoupdate/">autoupdate</a></code>(1), <code><a href="/docs/linux/man/1-autoheader/">autoheader</a></code>(1), <code><a href="/docs/linux/man/1-autoscan/">autoscan</a></code>(1), <code><a href="/docs/linux/man/1-config-guess/">config.guess</a></code>(1), <code><a href="/docs/linux/man/1-config-sub/">config.sub</a></code>(1), <code><a href="/docs/linux/man/1-ifnames/">ifnames</a></code>(1), <code><a href="/docs/linux/man/1-libtool/">libtool</a></code>(1). </p>
<p> The full documentation for <code>autoreconf</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>autoreconf</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info autoreconf</code></dd></dl>
<p> should give you access to the complete manual. </p>
