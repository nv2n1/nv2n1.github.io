---
title: "shtoolize(1)"
name: "shtoolize"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtoolize/"
description: "shtoolize – Build individual GNU shtool scripts"
---

<h2 class="name">NAME</h2>
<p> shtoolize &#8211; Build individual GNU shtool scripts </p>
<h2>VERSION</h2>
<p> <font SIZE="-1">GNU</font> shtool <font SIZE="-1">2.0.8 (18-Jul-2008)</font></p>
<h2>SYNOPSIS</h2>
<p> <code>shtoolize</code> [<code>-h</code>] [<code>-v</code>] [<code>-q</code>] [<code>-o</code> <i>script</i>] <i>module</i> [ <i>module</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>shtoolize</code> program builds individual <font SIZE="-1">GNU </font><code>shtool</code> scripts (written to the default output file <tt>&quot;shtool&quot;</tt> or to the specified <i>script</i>) out of one or more <code>shtool</code> ingredient <i>module</i>s. Available <i>module</i>s are: </p>
<pre>
 echo       Print string with optional construct expansion
 mdate      Pretty-print modification time of a file or dir
 table      Pretty print a field-separated list as a table
 prop       Display progress with a running propeller
 move       Move files with simultan substitution
 install    Install a program, script or datafile
 mkdir      Make one or more directories
 mkln       Make link with calculation of relative paths
 mkshadow   Make a shadow tree
 fixperm    Fix file permissions inside a source tree
 rotate     Rotate a logfile
 tarball    Roll distribution tarballs
 subst      Apply <a href="//www.systutorials.com/docs/linux/man/1-sed/">sed</a>(1) substitution operations
 platform   Platform identification utility
 arx        Extended archive command
 slo        Separate linker options by library class
 scpp       Sharing C Pre-Processor
 version    Generate and maintain a version information file
 path       Deal with program paths
</pre>
<p> Additionally there is a pseudo-module &#8220;<tt>&quot;all&quot;</tt>&#8221; which can be used as a short-hand for &#8220;<tt>&quot;echo mdate table prop move install mkdir mkln mkshadow fixperm platform arx slo scpp version path&quot;</tt>&#8221;, i.e. to build a <code>shtool</code> script with all modules in the standard order. An installed <code>shtool</code> is usually built this way via &#8220;<tt>&quot;shtoolize -o shtool all&quot;</tt>&#8221;. </p>
<p> Use the <code>shtoolize</code> program to build individual <code>shtool</code> scripts in case you want a smaller sized script and you don&#8217;t need all of the available <code>shtool</code> functionality. For instance for the classical <code>Autoconf</code> based free software package a <tt>&quot;shtool&quot;</tt> script build via &#8220;<tt>&quot;shtoolize -o shtool install mkdir&quot;</tt>&#8221; might be sufficient.</p>
<h2>OPTIONS</h2>
<p> The following command line options exist:</p>
<dl>
<dt><code>-h</code></p>
<dd> Displays a short help page describing the usage of <code>shtoolize</code>.</p>
<dt><code>-v</code></p>
<dd> Displays the version number of <code>shtoolize</code>/<code>shtool</code>.</p>
<dt><code>-q</code></p>
<dd> Displays no processing information.</p>
<dt><code>-o</code> <i>script</i></p>
<dd> Writes the output to file <i>script</i> instead to file &#8220;<tt>&quot;shtool&quot;</tt>&#8221;.</dl>
<h2>EXAMPLE</h2>
<p> The typical free software package which is based on <font SIZE="-1">GNU </font><code>libtool</code> and <font SIZE="-1">GNU </font><code>shtool</code> one uses a <tt>&quot;Makefile&quot;</tt> entry like the following: </p>
<pre>
 #   Makefile entry for upgrading GNU tools
 upgrade-tools:
     libtoolize -f -c
     shtoolize -q all
</pre>
<p> This upgrades the three files <tt>&quot;ltmain.sh&quot;</tt>, <tt>&quot;ltconfig&quot;</tt> and <tt>&quot;shtool&quot;</tt> in the current source tree to the latest versions.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1).</p>
<h2>AUTHOR</h2>
<pre>
 Ralf S. Engelschall
 rse [at] engelschall.com
 <a rel="nofollow" href="http://www.engelschall.com">www.engelschall.com</a>
</pre>
<h2>Index</h2>
