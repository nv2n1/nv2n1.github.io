---
title: "shtool(1)"
name: "shtool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool/"
description: "GNU shtool – The GNU Portable Shell Tool"
---

<h2 class="name">NAME</h2>
<p> GNU shtool &#8211; The GNU Portable Shell Tool </p>
<h2>VERSION</h2>
<p> <font SIZE="-1">GNU</font> shtool <font SIZE="-1">2.0.8 (18-Jul-2008)</font></p>
<h2>SYNOPSIS</h2>
<p> <code>shtool</code> [ <i>global_options</i> ] <i>command</i> [ <i>command_options</i> ] [ <i>command_args</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1"><code>GNU</code></font><code> shtool</code> is a compilation of small but very stable and portable shell scripts into a single shell tool. All ingredients were in successful use over many years in various free software projects. The compiled <code>shtool</code> script is intended to be used inside the source tree of those free software packages. There it can take over various (usually non-portable) tasks related to the building and installation of such packages.</p>
<h2>GLOBAL OPTIONS</h2>
<p> The following <i>global options</i> are available for <code>shtool</code>. Any <i>command</i>s are ignored if one of them is present on the <code>shtool</code> command line.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Displays a short help page describing the usage of <code>shtool</code> and it&#8217;s ingredient <i>command</i>s in a compact way.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Displays the version number of <code>shtool</code>.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Displays shell trace messages for debugging purposes.</p>
<dt><code>-r</code>, <code>&#8211;recreate</code></p>
<dd> Recreate the <code>shtool</code> script with its own individual <i><a href="/docs/linux/man/1-shtoolize/">shtoolize</a></i>(1) call.</dl>
<h2>COMMANDS</h2>
<p> The following <i>command</i>s are provided by <code>shtool</code>. They are all called via &quot;<tt>&quot;shtool&quot;</tt> <i>command</i>&quot;. Any command options <i>command_opts</i> and arguments <i>command_args</i> are specific to the particular <i>command</i> and are described in the corresponding manual page <code>shtool_</code><i><a href="/docs/linux/man/1-command/">command</a></i>(1). The commands are listed here sorted by topic, i.e., related commands are listed side-by-side.</p>
<dl>
<dt><code>echo</code></p>
<dd> <i><a href="/docs/linux/man/1-echo/">echo</a></i>(1) style print command providing special expansion constructs (terminal bold mode, environment details, date) and newline control.</p>
<dt><code>mdate</code></p>
<dd> Pretty-printing of the last modification time of a file or directory.</p>
<dt><code>table</code></p>
<dd> Pretty-printing a field-separated list as a two-dimensional table.</p>
<dt><code>prop</code></p>
<dd> Displaying of a processing indication though a running terminal character propeller.</p>
<dt><code>move</code></p>
<dd> <i><a href="/docs/linux/man/1-mv/">mv</a></i>(1) style command for renaming/moving multiple files at once and allowing source files just to be deleted if contents did not change.</p>
<dt><code>install</code></p>
<dd> <i><a href="/docs/linux/man/1-install/">install</a></i>(1) style command for installing a program, script or data file in a portable way.</p>
<dt><code>mkdir</code></p>
<dd> <i><a href="/docs/linux/man/1-mkdir/">mkdir</a></i>(1) style command providing support for automatical parent directory creation, directory permission control and smart skipping if directory already exists.</p>
<dt><code>mkln</code></p>
<dd> <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1) style command providing automatic calculation and usage of relative links if possible.</p>
<dt><code>mkshadow</code></p>
<dd> Creation of a shadow filesystem tree by the help of symbolic links.</p>
<dt><code>fixperm</code></p>
<dd> Fixing of file permissions in a source tree by cleaning up the permission bits.</p>
<dt><code>rotate</code></p>
<dd> Rotate a logfile.</p>
<dt><code>tarball</code></p>
<dd> Roll standardized distribution tarballs.</p>
<dt><code>subst</code></p>
<dd> Apply <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) substitution operations.</p>
<dt><code>platform</code></p>
<dd> Determines platform identification information.</p>
<dt><code>arx</code></p>
<dd> Extended archive command which can even put existing archives into an archive.</p>
<dt><code>slo</code></p>
<dd> Separate linker options by library class.</p>
<dt><code>scpp</code></p>
<dd> An additional C source file pre-processor for sharing <i><a href="/docs/linux/man/1-cpp/">cpp</a></i>(1) code, internal variables and internal functions.</p>
<dt><code>version</code></p>
<dd> Maintain a version information file in either Text, C/C<font SIZE="-2">++</font>, Perl or Python. format.</p>
<dt><code>path</code></p>
<dd> Deal with shell path variables.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtoolize/">shtoolize</a></i>(1), <i><a href="/docs/linux/man/1-shtool-arx/">shtool-arx</a></i>(1), <i><a href="/docs/linux/man/1-shtool-echo/">shtool-echo</a></i>(1), <i><a href="/docs/linux/man/1-shtool-fixperm/">shtool-fixperm</a></i>(1), <i><a href="/docs/linux/man/1-shtool-install/">shtool-install</a></i>(1), <i><a href="/docs/linux/man/1-shtool-mdate/">shtool-mdate</a></i>(1), <i><a href="/docs/linux/man/1-shtool-mkdir/">shtool-mkdir</a></i>(1), <i><a href="/docs/linux/man/1-shtool-mkln/">shtool-mkln</a></i>(1), <i><a href="/docs/linux/man/1-shtool-mkshadow/">shtool-mkshadow</a></i>(1), <i><a href="/docs/linux/man/1-shtool-move/">shtool-move</a></i>(1), <i><a href="/docs/linux/man/1-shtool-path/">shtool-path</a></i>(1), <i><a href="/docs/linux/man/1-shtool-platform/">shtool-platform</a></i>(1), <i><a href="/docs/linux/man/1-shtool-prop/">shtool-prop</a></i>(1), <i><a href="/docs/linux/man/1-shtool-rotate/">shtool-rotate</a></i>(1), <i><a href="/docs/linux/man/1-shtool-scpp/">shtool-scpp</a></i>(1), <i><a href="/docs/linux/man/1-shtool-slo/">shtool-slo</a></i>(1), <i><a href="/docs/linux/man/1-shtool-subst/">shtool-subst</a></i>(1), <i><a href="/docs/linux/man/1-shtool-table/">shtool-table</a></i>(1), <i><a href="/docs/linux/man/1-shtool-tarball/">shtool-tarball</a></i>(1), <i><a href="/docs/linux/man/1-shtool-version/">shtool-version</a></i>(1).</p>
<h2>HISTORY</h2>
<p> Some scripts contained in <font SIZE="-1">GNU </font><code>shtool</code> were already written in 1994 by <i>Ralf S. Engelschall</i> for use inside some private source trees. Then they evolved into more elaborated versions over the years and were used in various free software projects like ePerl, <font SIZE="-1">WML,</font> iSelect, gFONT, etc. They were complemented with other scripts from the author which he wrote in March 1998 for the &#8220;Apache Autoconf-style Interface&#8221; (<font SIZE="-1">APACI</font>) for Apache 1.3. In April 1999 the <code>shtool</code> package was created out of the accumulated master versions of the scripts and in June 1999 it entered the status of an official <font SIZE="-1">GNU</font> program and this way finally joined the group of <font SIZE="-1">GNU </font><code>autoconf</code>, <font SIZE="-1">GNU </font><code>automake</code> and <font SIZE="-1">GNU </font><code>libtool</code>.</p>
<h2>AUTHOR</h2>
<pre>
 Ralf S. Engelschall
 rse [at] engelschall.com
 <a rel="nofollow" href="http://www.engelschall.com">www.engelschall.com</a>
</pre>
<h2>Index</h2>
