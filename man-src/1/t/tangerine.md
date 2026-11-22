---

title: "tangerine(1)"
name: "tangerine"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tangerine/"
description: "tangerine – Perl dependency metadata tool"
---

<p> tangerine &#8211; Perl dependency metadata tool </p>
<h2>SYNOPSIS</h2>
<p> tangerine [options] &lt;files or directories&gt;</p>
<h2>DESCRIPTION</h2>
<p> This utility attempts to examine and analyze perl files, directories or perl distribution archives, reporting provided modules, and compile-time and run-time depencies. </p>
<p> In the <code>diff</code> mode it reports differences between two directories or perl distribution archives.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;all|-a</code></dt>
<dd> Examine all recursively discovered files. By default, only perl files are considered.</dd>
<dt><code>&#8211;compact|-c</code></dt>
<dd> Do not list dependencies provides by the examined set.</dd>
<dt><code>&#8211;diff|-d </code><code>FOO BAR</code></dt>
<dd> Examine <i></i><i>FOO</i><i></i> and <i></i><i>BAR</i><i></i> and report metadata differences, ignoring line numbers. These can be directories or distribution tarballs.</dd>
<dt><code>&#8211;files|-f</code></dt>
<dd> Report findings per file instead of per module. This option has no effect with <code>&#8211;compact</code>.</dd>
<dt><code>&#8211;jobs|-j </code><code>NUM</code></dt>
<dd> Defines the number of workers used for parallel processing. By default, the optimal number of workers is determined automatically.</dd>
<dt><code>&#8211;help|-h</code></dt>
<dd> Display this help.</dd>
<dt><code>&#8211;mode|-m </code><code>MODE</code></dt>
<dd> Only look for this specific metadata. Valid options are <i>compile</i> (modules required at compile time), <i>runtime</i> (modules required at runtime), <i>package</i> (modules provided) and <i>all</i>. For backwards compatibility, <i>p|prov</i>, <i>r|req</i> and <i>u|use</i> are also understood. This option is automatically set to <i>all</i> if <code>&#8211;compact</code> is also used. Defaults to <i>all</i>.</dd>
<dt><code>&#8211;verbose|-v</code></dt>
<dd> Be a little more verbose where it makes sense.</dd></dl>
<h2>EXAMPLES</h2>
<pre>
    tangerine -c Makefile.PL lib/ t/
    tangerine --mode=compile inc/
    tangerine -d Foo-0.01.tar.gz Foo-0.02.tar.gz
</pre>
<h2>AUTHOR AND LICENSE</h2>
<p> Copyright (c) 2014-2015 Petr Xabata &lt;contyk [at] redhat.com&gt; </p>
<p> See the LICENSE files for licensing details. </p>
