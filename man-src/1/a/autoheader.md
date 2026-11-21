---

title: "autoheader(1)"
name: "autoheader"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autoheader/"
description: "autoheader – Create a template header for configure"
---

<p> <code>autoheader</code> [<i>,OPTION/</i>]&#8230; [<i>,TEMPLATE-FILE/</i>]</p>
<p> Create a template file of C &#8216;#define&#8217; statements for &#8216;configure&#8217; to use. To this end, scan TEMPLATE-FILE, or &#8216;configure.ac&#8217; if present, or else &#8216;configure.in&#8217;.</p>
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
<dd> consider all files obsolete</dd>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>,CATEGORY/</i></dt>
<dd> report the warnings falling in CATEGORY</dd></dl>
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
<h3>Library directories:</h3>
<dl>
<dt><code>-B</code>, <code>&#8211;prepend-include</code>=<i>,DIR/</i></dt>
<dd> prepend directory DIR to search path</dd>
<dt><code>-I</code>, <code>&#8211;include</code>=<i>,DIR/</i></dt>
<dd> append directory DIR to search path</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Roland McGrath and Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-autoconf [at] gnu.org&gt;.<br />
 GNU Autoconf home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/autoconf/">https://www.gnu.org/software/autoconf/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+/Autoconf: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;, &lt;<a rel="nofollow" href="https://gnu.org/licenses/exceptions.html">https://gnu.org/licenses/exceptions.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autoconf/">autoconf</a></code>(1), <code><a href="/docs/linux/man/1-automake/">automake</a></code>(1), <code><a href="/docs/linux/man/1-autoreconf/">autoreconf</a></code>(1), <code><a href="/docs/linux/man/1-autoupdate/">autoupdate</a></code>(1), <code><a href="/docs/linux/man/1-autoheader/">autoheader</a></code>(1), <code><a href="/docs/linux/man/1-autoscan/">autoscan</a></code>(1), <code><a href="/docs/linux/man/1-config-guess/">config.guess</a></code>(1), <code><a href="/docs/linux/man/1-config-sub/">config.sub</a></code>(1), <code><a href="/docs/linux/man/1-ifnames/">ifnames</a></code>(1), <code><a href="/docs/linux/man/1-libtool/">libtool</a></code>(1). </p>
<p> The full documentation for <code>autoheader</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>autoheader</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info autoheader</code></dd></dl>
<p> should give you access to the complete manual. </p>
