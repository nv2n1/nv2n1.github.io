---
title: "shtool-version(1)"
name: "shtool-version"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-version/"
description: "shtool version – GNU shtool maintain version information file"
---

<h2 class="name">NAME</h2>
<p> shtool version &#8211; GNU shtool maintain version information file </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool version</code> [<code>-l</code>|<code>&#8211;language</code> <i>lang</i>] [<code>-n</code>|<code>&#8211;name</code> <i>name</i>] [<code>-p</code>|<code>&#8211;prefix</code> <i>prefix</i>] [<code>-s</code>|<code>&#8211;set</code> <i>version</i>] [<code>-e</code>|<code>&#8211;edit</code>] [<code>-i</code>|<code>&#8211;increase</code> <i>knob</i>] [<code>-d</code>|<code>&#8211;display</code> <i>type</i>] <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> This command displays and maintains version information in <i>file</i>. </p>
<p> The version is always described with a triple &lt;<i>version</i>,<i>revision</i>,<i>level</i>&gt; and is represented by a string which always matches the regular expression &quot;<tt>&quot;[0-9]+\.[0-9]+[sabp.][0-9]+&quot;</tt>&quot;. </p>
<p> The hexadecimal format for a version <tt>&quot;v.rtl&quot;</tt> is <tt>&quot;VVRRTLL&quot;</tt> where <tt>&quot;VV&quot;</tt> and <tt>&quot;RR&quot;</tt> directly correspond to <tt>&quot;v&quot;</tt> and <tt>&quot;r&quot;</tt>, <tt>&quot;T&quot;</tt> encodes the level type as <tt>9</tt>, <tt>2</tt>, <tt>1</tt>, <tt>0</tt> (representing <tt>&quot;s&quot;</tt>, <tt>&quot;p&quot;</tt>/<tt>&quot;.&quot;</tt>, <tt>&quot;b&quot;</tt>, <tt>&quot;a&quot;</tt> in this order) and <tt>&quot;LL&quot;</tt> is either directly corresponding to <tt>&quot;l&quot;</tt> or set to <tt>99</tt> if level type is <tt>&quot;s&quot;</tt>.</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print verbose information during processing.</p>
<dt><code>-l</code>, <code>&#8211;language</code> <i>lang</i></p>
<dd> Choose format of version file <i>file</i>. <i>lang</i>=&quot;<tt>&quot;txt&quot;</tt>&quot;, <font SIZE="-1">ANSI C </font>(<i>lang</i>=&#8220;c&#8221;), M4 (<i>lang</i>=&#8220;m4&#8221;), Perl (<i>lang</i>=&#8220;perl&#8221;) or Python (<i>lang</i>=&#8220;python&#8221;). Default is <tt>&quot;txt&quot;</tt>.</p>
<dt><code>-n</code>, <code>&#8211;name</code> <i>name</i></p>
<dd> Name the program the version is maintained for. Default is <tt>&quot;unknown&quot;</tt>.</p>
<dt><code>-p</code>, <code>&#8211;prefix</code> <i>prefix</i> =item <code>-s</code>, <code>&#8211;set</code> <i>version</i></p>
<dd> Set the version to <i>version</i>.</p>
<dt><code>-e</code>, <code>&#8211;edit</code></p>
<dd> Interactively enter a new version.</p>
<dt><code>-i</code>, <code>&#8211;increase</code> <i>knob</i></p>
<dd> When option &#8220;<code>-i</code>&#8221; is used, the current version in <i>file</i> is updated by increasing one element of the version where <i>knob</i> can be one of the following: &#8220;<tt>&quot;v&quot;</tt>&#8221; for increasing the version by 1 (and resetting revision and level to 0), &#8220;<tt>&quot;r&quot;</tt>&#8221; for increasing the revision by 1 (and resetting level to 0) or &#8220;<tt>&quot;l&quot;</tt>&#8221; for increasing the level by 1.</p>
<dt><code>-d</code>, <code>&#8211;display</code> <i>type</i></p>
<dd> Control the display type: &quot;<tt>&quot;short&quot;</tt>&#8220; for a short version display, &#8221;<tt>&quot;long&quot;</tt>&#8220; for a longer version display, &#8221;<tt>&quot;hex&quot;</tt>&#8220; for a hexadecimal display of the version and &#8221;<tt>&quot;libtool&quot;</tt>&quot; for a format suitable for use with <font SIZE="-1">GNU</font> libtool.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 shtool version -l c -n FooBar -p foobar -s 1.2b3 version.c
 #   configure.in
 V=`shtool version -l c -d long version.c`
 echo &quot;Configuring FooBar, Version $V&quot;
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>version</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1994 for <font SIZE="-1"><code>OSSP</code></font><code> eperl</code>. It was later rewritten from scratch for inclusion into <font SIZE="-1"><code>GNU</code></font><code> shtool</code>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1). </p>
<h2>Index</h2>
