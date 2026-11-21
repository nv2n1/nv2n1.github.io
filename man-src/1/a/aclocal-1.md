---

title: "aclocal-1(1)"
name: "aclocal-1"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aclocal-1/"
description: "aclocal – manual page for aclocal 1.13.4"
---

<h2>NAME</h2>
<p> aclocal &#8211; manual page for aclocal 1.13.4</p>
<p> <code>aclocal</code> [<i>OPTION</i>]&#8230;</p>
<p> Generate &#8216;aclocal.m4&#8217; by scanning &#8216;configure.ac&#8217; or &#8216;configure.in&#8217;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;automake-acdir</code>=<i>DIR</i></dt>
<dd> directory holding automake-provided m4 files</dd>
<dt><code>&#8211;system-acdir</code>=<i>DIR</i></dt>
<dd> directory holding third-party system-wide files</dd>
<dt><code>&#8211;diff</code>[=<i>COMMAND</i>]</dt>
<dd> run COMMAND [diff <code>-u]</code> on M4 files that would be changed (implies <code>&#8211;install</code> and <code>&#8211;dry-run</code>)</dd>
<dt><code>&#8211;dry-run</code></dt>
<dd> pretend to, but do not actually update any file</dd>
<dt><code>&#8211;force</code></dt>
<dd> always update output file</dd>
<dt><code>&#8211;help</code></dt>
<dd> print this help, then exit</dd>
<dt><code>-I</code> DIR</dt>
<dd> add directory to search list for .m4 files</dd>
<dt><code>&#8211;install</code></dt>
<dd> copy third-party files to the first <code>-I</code> directory</dd>
<dt><code>&#8211;output</code>=<i>FILE</i></dt>
<dd> put output in FILE (default aclocal.m4)</dd>
<dt><code>&#8211;print-ac-dir</code></dt>
<dd> print name of directory holding system-wide third-party m4 files, then exit</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> don&#8217;t be silent</dd>
<dt><code>&#8211;version</code></dt>
<dd> print version number, then exit</dd>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>CATEGORY</i></dt>
<dd> report the warnings falling in CATEGORY</dd></dl>
<h3>Warning categories include:</h3>
<dl>
<dt>syntax</dt>
<dd> dubious syntactic constructs (default)</dd>
<dt>unsupported</dt>
<dd> unknown macros (default)</dd>
<dt>all</dt>
<dd> all the warnings (default)</dd>
<dt>no-CATEGORY</dt>
<dd> turn off warnings in CATEGORY</dd>
<dt>none</dt>
<dd> turn off all the warnings</dd>
<dt>error</dt>
<dd> treat warnings as errors</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Tom Tromey &lt;tromey [at] redhat.com&gt;</p>
<dl>
<dt>
</dt><dd> and Alexandre Duret-Lutz &lt;adl [at] gnu.org&gt;.</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-automake [at] gnu.org&gt;.<br />
 GNU Automake home page: &lt;<a rel="nofollow" href="http://www.gnu.org/software/automake/">http://www.gnu.org/software/automake/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Free Software Foundation, Inc. License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl-2.0.html">http://gnu.org/licenses/gpl-2.0.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>aclocal</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>aclocal</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info aclocal</code></dd></dl>
<p> should give you access to the complete manual. </p>
