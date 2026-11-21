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
<dt><code>-c</code>, <code>&#8211;copy</code></dt>
<dd> copy files rather than symlinking them</dd>
<dt><code>&#8211;debug</code></dt>
<dd> enable verbose shell tracing</dd>
<dt><code>-n</code>, <code>&#8211;dry-run</code></dt>
<dd> print commands rather than running them</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> replace existing files</dd>
<dt><code>-i</code>, <code>&#8211;install</code></dt>
<dd> copy missing auxiliary files</dd>
<dt><code>&#8211;ltdl</code>[=<i>,DIR/</i>]</dt>
<dd> install libltdl sources [default: libltdl]</dd>
<dt><code>&#8211;no-warnings</code></dt>
<dd> equivalent to &#8216;-Wnone&#8217;</dd>
<dt><code>&#8211;nonrecursive</code></dt>
<dd> prepare ltdl for non-recursive make</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> work silently</dd>
<dt><code>&#8211;recursive</code></dt>
<dd> prepare ltdl for recursive make</dd>
<dt><code>&#8211;subproject</code></dt>
<dd> prepare ltdl to configure and build independently</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> verbosely report processing</dd>
<dt><code>&#8211;version</code></dt>
<dd> print version information and exit</dd>
<dt><code>-W</code>, <code>&#8211;warnings</code>=<i>,CATEGORY/</i></dt>
<dd> report the warnings falling in CATEGORY [all]</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> print short or long help message</dd></dl>
<h3>Warning categories include:</h3>
<dl>
<dt>&#8216;all&#8217;</dt>
<dd> show all warnings</dd>
<dt>&#8216;none&#8217;</dt>
<dd> turn off all the warnings</dd>
<dt>&#8216;error&#8217;</dt>
<dd> warnings are treated as fatal errors</dd>
<dt>&#8216;environment&#8217;</dt>
<dd> show warnings about LIBTOOLIZE_OPTIONS content</dd>
<dt>&#8216;file&#8217;</dt>
<dd> show warnings about file copying and linking</dd></dl>
<p> The following space or comma delimited options can be passed to libtoolize via the environment variable LIBTOOLIZE_OPTIONS, unknown environment options are ignored:</p>
<dl>
<dt><code>&#8211;debug</code></dt>
<dd> enable verbose shell tracing</dd>
<dt><code>&#8211;no-warnings</code></dt>
<dd> don&#8217;t display warning messages</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> work silently</dd>
<dt><code>&#8211;verbose</code></dt>
<dd> verbosely report processing</dd></dl>
<p> You must &#8216;cd&#8217; to the top directory of your package before you run &#8216;libtoolize&#8217;. </p>
<p> When reporting a bug, please describe a test case to reproduce it and include the following information:</p>
<dl>
<dt>host-triplet:</dt>
<dd> x86_64-pc-linux-gnu</dd>
<dt>version:</dt>
<dd> libtoolize (GNU libtool) 2.4.6 Debian-2.4.6-15build2</dd>
<dt>automake:</dt>
<dd> automake (GNU automake) 1.16.5</dd>
<dt>autoconf:</dt>
<dd> autoconf (GNU Autoconf) 2.71</dd></dl>
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
</dt><dd> <code>info libtoolize</code></dd></dl>
<p> should give you access to the complete manual. </p>
