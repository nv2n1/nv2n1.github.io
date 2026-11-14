---
title: "depmod(8)"
name: "depmod"
section: "8"
letter: "d"
url: "/docs/linux/man/8-depmod/"
description: "depmod – Generate modules.dep and map files."
---

<p>depmod &#8211; Generate modules.dep and map files.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>depmod</code> [<code>-b&nbsp;</code><i>basedir</i>] [<code>-e</code>] [<code>-E&nbsp;</code><i>Module.symvers</i>] [<code>-F&nbsp;</code><i>System.map</i>] [<code>-n</code>] [<code>-v</code>] [<code>-A</code>] [<code>-P&nbsp;</code><i>prefix</i>] [<code>-w</code>] [<i>version</i>]</p>
<dt> <code>depmod</code> [<code>-e</code>] [<code>-E&nbsp;</code><i>Module.symvers</i>] [<code>-F&nbsp;</code><i>System.map</i>] [<code>-n</code>] [<code>-v</code>] [<code>-P&nbsp;</code><i>prefix</i>] [<code>-w</code>] [<i>version</i>] [<i>filename</i>&#8230;]</dl>
<h2>Description</h2>
<dd>Linux kernel modules can provide services (called &quot;symbols&quot;) for other modules to use (using one of the EXPORT_SYMBOL variants in the code). If a second module uses this symbol, that second module clearly depends on the first module. These dependencies can get quite complex. </p>
<p> <code>depmod</code> creates a list of module dependencies by reading each module under /lib/modules/<i>version</i> and determining what symbols it exports and what symbols it needs. By default, this list is written to modules.dep, and a binary hashed version named modules.dep.bin, in the same directory. If filenames are given on the command line, only those modules are examined (which is rarely useful unless all modules are listed). <code>depmod</code> also creates a list of symbols provided by modules in the file named modules.symbols and its binary hashed version, modules.symbols.bin. Finally, <code>depmod</code> will output a file named modules.devname if modules supply special device names (devname) that should be populated in /dev on boot (by a utility such as systemd-tmpfiles). </p>
<p> If a <i>version</i> is provided, then that kernel version&#8217;s module directory is used rather than the current kernel version (as returned by <code>uname -r</code>).</p>
<h2>Options</h2>
<p><code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dd>Probe all modules. This option is enabled by default if no file names are given in the command-line.</dl>
<p> <code>-A</code>, <code>&#8211;quick</code></p>
<dl>
<dd>This option scans to see if any modules are newer than the modules.dep file before any work is done: if not, it silently exits rather than regenerating the files.</dl>
<p> <code>-b </code><i>basedir</i>, <code>&#8211;basedir </code><i>basedir</i></p>
<dl>
<dd>If your modules are not currently in the (normal) directory /lib/modules/<i>version</i>, but in a staging area, you can specify a <i>basedir</i> which is prepended to the directory name. This <i>basedir</i> is stripped from the resulting modules.dep file, so it is ready to be moved into the normal location. Use this option if you are a distribution vendor who needs to pre-generate the meta-data files rather than running depmod again later.</dl>
<p> <code>-C</code>, <code>&#8211;config </code><i>file or directory</i></p>
<dl>
<dd>This option overrides the default configuration directory at /etc/depmod.d/.</dl>
<p> <code>-e</code>, <code>&#8211;errsyms</code></p>
<dl>
<dd>When combined with the <code>-F</code> option, this reports any symbols which a module needs which are not supplied by other modules or the kernel. Normally, any symbols not provided by modules are assumed to be provided by the kernel (which should be true in a perfect world), but this assumption can break especially when additionally updated third party drivers are not correctly installed or were built incorrectly.</dl>
<p> <code>-E</code>, <code>&#8211;symvers</code></p>
<dl>
<dd>When combined with the <code>-e</code> option, this reports any symbol versions supplied by modules that do not match with the symbol versions provided by the kernel in its Module.symvers. This option is mutually incompatible with <code>-F</code>.</dl>
<p> <code>-F</code>, <code>&#8211;filesyms </code><i>System.map</i></p>
<dl>
<dd>Supplied with the System.map produced when the kernel was built, this allows the <code>-e</code> option to report unresolved symbols. This option is mutually incompatible with <code>-E</code>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print the help message and exit.</dl>
<p> <code>-n</code>, <code>&#8211;show</code>, <code>&#8211;dry-run</code></p>
<dl>
<dd>This sends the resulting modules.dep and the various map files to standard output rather than writing them into the module directory.</dl>
<p> <code>-P</code></p>
<dl>
<dd>Some architectures prefix symbols with an extraneous character. This specifies a prefix character (for example &#8216;_&#8217;) to ignore.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>In verbose mode, <code>depmod</code> will print (to stdout) all the symbols each module depends on and the module&#8217;s file name which provides that symbol.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Show version of program and exit. See below for caveats when run on older kernels.</dl>
<p> <code>-w</code></p>
<dl>
<dd>Warn on duplicate dependencies, aliases, symbol versions, etc.</dl>
<h2>Copyright</h2>
<p>This manual page originally Copyright 2002, Rusty Russell, IBM Corporation. Portions Copyright Jon Masters, and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-depmod-d/">depmod.d</a></code>(5), <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8), <code><a href="/docs/linux/man/5-modules-dep/">modules.dep</a></code>(5)</p>
<h2>Authors</h2>
<p><code>Jon Masters</code> &lt;jcm [at] jonmasters.org&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Robby Workman</code> &lt;rworkman [at] slackware.com&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Lucas De Marchi</code> &lt;lucas.de.marchi [at] gmail.com&gt;</p>
<dl>
<dd>Developer</dl>
