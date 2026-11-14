---
title: "libtoolize(1)"
name: "libtoolize"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libtoolize/"
description: "libtoolize – Prepare a package to use libtool"
---

<h2 class="name">NAME</h2>
<p> libtoolize &#8211; Prepare a package to use libtool </p>
<h2>SYNOPSIS</h2>
<p> <code>libtoolize</code> [<i>,OPTION/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Prepare a package to use libtool.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;copy</code></p>
<dd> copy files rather than symlinking them</p>
<dt><code>&#8211;debug</code></p>
<dd> enable verbose shell tracing</p>
<dt><code>-n</code>, <code>&#8211;dry-run</code></p>
<dd> print commands rather than running them</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> replace existing files</p>
<dt><code>-i</code>, <code>&#8211;install</code></p>
<dd> copy missing auxiliary files</p>
<dt><code>&#8211;ltdl</code>[=<i>,DIR/</i>]</p>
<dd> install libltdl sources [default: libltdl]</p>
<dt><code>&#8211;no-warnings</code></p>
<dd> equivalent to &#8216;-Wnone&#8217;</p>
<dt><code>&#8211;nonrecursive</code></p>
<dd> prepare ltdl for non-recursive make</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> work silently</p>
<dt><code>&#8211;recursive</code></p>
<dd> prepare ltdl for recursive make</p>
<dt><code>&#8211;subproject</code></p>
<dd> prepare ltdl to configure and build independently</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> verbosely report processing</p>
<dt><code>&#8211;version</code></p>
<dd> print version information and exit</p>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>,CATEGORY/</i></p>
<dd> report the warnings falling in CATEGORY [all]</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> print short or long help message</dl>
<h3>Warning categories include:</h3>
<dl>
<dt>&#8216;all&#8217;</p>
<dd> show all warnings</p>
<dt>&#8216;none&#8217;</p>
<dd> turn off all the warnings</p>
<dt>&#8216;error&#8217;</p>
<dd> warnings are treated as fatal errors</p>
<dt>&#8216;environment&#8217;</p>
<dd> show warnings about LIBTOOLIZE_OPTIONS content</p>
<dt>&#8216;file&#8217;</p>
<dd> show warnings about file copying and linking</dl>
<p> The following space or comma delimited options can be passed to libtoolize via the environment variable LIBTOOLIZE_OPTIONS, unknown environment options are ignored:</p>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> enable verbose shell tracing</p>
<dt><code>&#8211;no-warnings</code></p>
<dd> don&#8217;t display warning messages</p>
<dt><code>&#8211;quiet</code></p>
<dd> work silently</p>
<dt><code>&#8211;verbose</code></p>
<dd> verbosely report processing</dl>
<p> You must &#8216;cd&#8217; to the top directory of your package before you run &#8216;libtoolize&#8217;. </p>
<p> When reporting a bug, please describe a test case to reproduce it and include the following information:</p>
<dl>
<dt>host-triplet:</p>
<dd> x86_64-pc-linux-gnu</p>
<dt>version:</p>
<dd> libtoolize (GNU libtool) 2.4.6 Debian-2.4.6-15build2</p>
<dt>automake:</p>
<dd> automake (GNU automake) 1.16.5</p>
<dt>autoconf:</p>
<dd> autoconf (GNU Autoconf) 2.71</dl>
<h2>AUTHOR</h2>
<p> Written by Gary V. Vaughan &lt;gary [at] gnu.org&gt;, 2003</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-libtool [at] gnu.org&gt;.<br />
 GNU libtool home page: &lt;<a rel="nofollow" href="https://www.gnu.org/software/libtool/">https://www.gnu.org/software/libtool/</a>&gt;.<br />
 General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2015 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>libtoolize</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libtoolize</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info libtoolize</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
