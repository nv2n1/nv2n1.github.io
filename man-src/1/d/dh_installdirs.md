---

title: "dh_installdirs(1)"
name: "dh_installdirs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installdirs/"
description: "dh_installdirs – create subdirectories in package build directories"
---

<p> <code>dh_installdirs</code> [<i>debhelper options</i>] [<code>-A</code>] [<i>dir</i> &#8230;]</p>
<p> <code>dh_installdirs</code> is a debhelper program that is responsible for creating subdirectories in package build directories. </p>
<p> Many packages can get away with omitting the call to <code>dh_installdirs</code> completely. Notably, other <code>dh_*</code> commands are expected to create directories as needed.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.dirs</dt>
<dd> Lists directories to be created in <i>package</i>. </dd>
<p> Generally, there is no need to list directories created by the upstream build system or directories needed by other <code>debhelper</code> commands.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></dt>
<dd> Create any directories specified by command line parameters in <font SIZE="-1">ALL</font> packages acted on, not just the first.</dd>
<dt><i>dir</i> &#8230;</dt>
<dd> Create these directories in the package build directory of the first package acted on. (Or in all packages if <code>-A</code> is specified.)</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
