---

title: "autom4te(1)"
name: "autom4te"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autom4te/"
description: "autom4te – Generate files and scripts thanks to M4"
---

<p> <code>autom4te</code> [<i>,OPTION/</i>]&#8230; [<i>,FILES/</i>]</p>
<p> Run GNU M4 on the FILES, avoiding useless runs. Output the traces if tracing, the frozen file if freezing, otherwise the expansion of the FILES. </p>
<p> If some of the FILES are named &#8216;FILE.m4f&#8217; they are considered to be M4 frozen files of all the previous files (which are therefore not loaded). If &#8216;FILE.m4f&#8217; is not found, then &#8216;FILE.m4&#8217; will be used, together with all the previous files. </p>
<p> Some files may be optional, i.e., will only be processed if found in the include path, but then must end in &#8216;.m4?&#8217;; the question mark is not part of the actual file name.</p>
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
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></dt>
<dd> save output in FILE (defaults to &#8216;-&#8216;, stdout)</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> don&#8217;t rely on cached values</dd>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>,CATEGORY/</i></dt>
<dd> report the warnings falling in CATEGORY</dd>
<dt><code>-l</code>, <code>&#8211;language</code>=<i>,LANG/</i></dt>
<dd> specify the set of M4 macros to use</dd>
<dt><code>-C</code>, <code>&#8211;cache</code>=<i>,DIRECTORY/</i></dt>
<dd> preserve results for future runs in DIRECTORY</dd>
<dt><code>&#8211;no-cache</code></dt>
<dd> disable the cache</dd>
<dt><code>-m</code>, <code>&#8211;mode</code>=<i>,OCTAL/</i></dt>
<dd> change the non trace output file mode (0666)</dd>
<dt><code>-M</code>, <code>&#8211;melt</code></dt>
<dd> don&#8217;t use M4 frozen files</dd></dl>
<h3>Languages include:</h3>
<dl>
<dt>&#8216;Autoconf&#8217;</dt>
<dd> create Autoconf configure scripts</dd>
<dt>&#8216;Autotest&#8217;</dt>
<dd> create Autotest test suites</dd>
<dt>&#8216;M4sh&#8217;</dt>
<dd> create M4sh shell scripts</dd>
<dt>&#8216;M4sugar&#8217;</dt>
<dd> create M4sugar output</dd></dl>
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
<p> The environment variables &#8216;M4&#8217; and &#8216;WARNINGS&#8217; are honored.</p>
<h3>Library directories:</h3>
<dl>
<dt><code>-B</code>, <code>&#8211;prepend-include</code>=<i>,DIR/</i></dt>
<dd> prepend directory DIR to search path</dd>
<dt><code>-I</code>, <code>&#8211;include</code>=<i>,DIR/</i></dt>
<dd> append directory DIR to search path</dd></dl>
<h3>Tracing:</h3>
<dl>
<dt><code>-t</code>, <code>&#8211;trace</code>=<i>,MACRO[/</i>:FORMAT]</dt>
<dd> report the MACRO invocations</dd>
<dt><code>-p</code>, <code>&#8211;preselect</code>=<i>,MACRO/</i></dt>
<dd> prepare to trace MACRO in a future run</dd></dl>
<h3>Freezing:</h3>
<dl>
<dt><code>-F</code>, <code>&#8211;freeze</code></dt>
<dd> produce an M4 frozen state file for FILES</dd></dl>
<h3>FORMAT defaults to &#8216;$f:$l:$n:$%&#8217;, and can use the following escapes:</h3>
<dl>
<dt>$$</dt>
<dd> literal $</dd>
<dt>$f</dt>
<dd> file where macro was called</dd>
<dt>$l</dt>
<dd> line where macro was called</dd>
<dt>$d</dt>
<dd> nesting depth of macro call</dd>
<dt>$n</dt>
<dd> name of the macro</dd>
<dt>$NUM</dt>
<dd> argument NUM, unquoted and with newlines</dd>
<dt>$SEP@</dt>
<dd> all arguments, with newlines, quoted, and separated by SEP</dd>
<dt>$SEP*</dt>
<dd> all arguments, with newlines, unquoted, and separated by SEP</dd>
<dt>$SEP%</dt>
<dd> all arguments, without newlines, unquoted, and separated by SEP</dd></dl>
<p> SEP can be empty for the default (comma for @ and *, colon for %), a single character for that character, or {STRING} to use a string.</p>
<h2>AUTHOR</h2>
<p> Written by Akim Demaille.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-autoconf [at] gnu.org&gt;.<br />
 GNU Autoconf home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/autoconf/">https://www.gnu.org/software/autoconf/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="https://www.gnu.org/gethelp/">https://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+/Autoconf: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;, &lt;<a rel="nofollow" href="https://gnu.org/licenses/exceptions.html">https://gnu.org/licenses/exceptions.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-autoconf/">autoconf</a></code>(1), <code><a href="/docs/linux/man/1-automake/">automake</a></code>(1), <code><a href="/docs/linux/man/1-autoreconf/">autoreconf</a></code>(1), <code><a href="/docs/linux/man/1-autoupdate/">autoupdate</a></code>(1), <code><a href="/docs/linux/man/1-autoheader/">autoheader</a></code>(1), <code><a href="/docs/linux/man/1-autoscan/">autoscan</a></code>(1), <code><a href="/docs/linux/man/1-config-guess/">config.guess</a></code>(1), <code><a href="/docs/linux/man/1-config-sub/">config.sub</a></code>(1), <code><a href="/docs/linux/man/1-ifnames/">ifnames</a></code>(1), <code><a href="/docs/linux/man/1-libtool/">libtool</a></code>(1). </p>
<p> The full documentation for <code>autom4te</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>autom4te</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info autom4te</code></dd></dl>
<p> should give you access to the complete manual. </p>
