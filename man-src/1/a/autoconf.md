---
title: "autoconf(1)"
name: "autoconf"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autoconf/"
description: "autoconf – Generate configuration scripts"
---

<h2 class="name">NAME</h2>
<p> autoconf &#8211; Generate configuration scripts </p>
<h2>SYNOPSIS</h2>
<p> <code>autoconf</code> [<i>,OPTION/</i>]&#8230; [<i>,TEMPLATE-FILE/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Generate a configuration script from a TEMPLATE-FILE if given, or &#8216;configure.ac&#8217; if present, or else &#8216;configure.in&#8217;. Output is sent to the standard output if TEMPLATE-FILE is given, else into &#8216;configure&#8217;.</p>
<h3>Operation modes:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> print this help, then exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> print version number, then exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> verbosely report processing</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> don&#8217;t remove temporary files</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> consider all files obsolete</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> save output in FILE (stdout is the default)</p>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>,CATEGORY/</i></p>
<dd> report the warnings falling in CATEGORY</dl>
<h3>Warning categories include:</h3>
<dl>
<dt>cross</p>
<dd> cross compilation issues</p>
<dt>gnu</p>
<dd> GNU coding standards (default in gnu and gnits modes)</p>
<dt>obsolete</p>
<dd> obsolete features or constructions (default)</p>
<dt>override</p>
<dd> user redefinitions of Automake rules or variables</p>
<dt>portability</p>
<dd> portability issues (default in gnu and gnits modes)</p>
<dt>portability-recursive</p>
<dd> nested Make variables (default with <code>-Wportability</code>)</p>
<dt>extra-portability</p>
<dd> extra portability issues related to obscure tools</p>
<dt>syntax</p>
<dd> dubious syntactic constructs (default)</p>
<dt>unsupported</p>
<dd> unsupported or incomplete features (default)</p>
<dt>all</p>
<dd> all the warnings</p>
<dt>no-CATEGORY</p>
<dd> turn off warnings in CATEGORY</p>
<dt>none</p>
<dd> turn off all the warnings</dl>
<p> The environment variables &#8216;M4&#8217; and &#8216;WARNINGS&#8217; are honored.</p>
<h3>Library directories:</h3>
<dl>
<dt><code>-B</code>, <code>&#8211;prepend-include</code>=<i>,DIR/</i></p>
<dd> prepend directory DIR to search path</p>
<dt><code>-I</code>, <code>&#8211;include</code>=<i>,DIR/</i></p>
<dd> append directory DIR to search path</dl>
<h3>Tracing:</h3>
<dl>
<dt><code>-t</code>, <code>&#8211;trace</code>=<i>,MACRO[/</i>:FORMAT]</p>
<dd> report the list of calls to MACRO</p>
<dt><code>-i</code>, <code>&#8211;initialization</code></p>
<dd> also trace Autoconf&#8217;s initialization process</dl>
<p> In tracing mode, no configuration script is created. FORMAT defaults to &#8216;$f:$l:$n:$%&#8217;; see &#8216;autom4te <code>&#8211;help</code>&#8216; for information about FORMAT.</p>
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
<p> The full documentation for <code>autoconf</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>autoconf</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info autoconf</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
