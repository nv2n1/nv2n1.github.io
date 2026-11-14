---
title: "modinfo(8)"
name: "modinfo"
section: "8"
letter: "m"
url: "/docs/linux/man/8-modinfo/"
description: "modinfo – Show information about a Linux Kernel module"
---

<p>modinfo &#8211; Show information about a Linux Kernel module</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>modinfo</code> [<code>-0</code>] [<code>-F&nbsp;</code><i>field</i>] [<code>-k&nbsp;</code><i>kernel</i>] [modulename|filename&#8230;]</p>
<dt> <code>modinfo -V</code></p>
<dt> <code>modinfo -h</code></dl>
<h2>Description</h2>
<p><code>modinfo</code></p>
<dd>extracts information from the Linux Kernel modules given on the command line. If the module name is not a filename, then the /lib/modules/<i>version</i> directory is searched, as is also done by <code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8) when loading kernel modules. </p>
<p> <code>modinfo</code> by default lists each attribute of the module in form <i>fieldname</i> : <i>value</i>, for easy reading. The filename is listed the same way (although it&#8217;s not really an attribute). </p>
<p> This version of <code>modinfo</code> can understand modules of any Linux Kernel architecture.</p>
<h2>Options</h2>
<p><code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Print the modinfo version.</dl>
<p> <code>-F</code>, <code>&#8211;field</code></p>
<dl>
<dd>Only print this field value, one per line. This is most useful for scripts. Field names are case-insensitive. Common fields (which may not be in every module) include author, description, license, parm, depends, and alias. There are often multiple parm, alias and depends fields. The special field filename lists the filename of the module.</dl>
<p> <code>-b </code><i>basedir</i>, <code>&#8211;basedir </code><i>basedir</i></p>
<dl>
<dd>Root directory for modules, / by default.</dl>
<p> <code>-k </code><i>kernel</i></p>
<dl>
<dd>Provide information about a kernel other than the running one. This is particularly useful for distributions needing to extract information from a newly installed (but not yet running) set of kernel modules. For example, you wish to find which firmware files are needed by various modules in a new kernel for which you must make an initrd/initramfs image prior to booting.</dl>
<p> <code>-0</code>, <code>&#8211;null</code></p>
<dl>
<dd>Use the ASCII zero character to separate field values, instead of a new line. This is useful for scripts, since a new line can theoretically appear inside a field.</dl>
<p> <code>-a</code> <code>&#8211;author</code>, <code>-d</code> <code>&#8211;description</code>, <code>-l</code> <code>&#8211;license</code>, <code>-p</code> <code>&#8211;parameters</code>, <code>-n</code> <code>&#8211;filename</code></p>
<dl>
<dd>These are shortcuts for the <code>&#8211;field</code> flag&#8217;s author, description, license, parm and filename arguments, to ease the transition from the old modutils <code>modinfo</code>.</dl>
<h2>Copyright</h2>
<p>This manual page originally Copyright 2003, Rusty Russell, IBM Corporation. Maintained by Jon Masters and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8)</p>
<h2>Authors</h2>
<p><code>Jon Masters</code> &lt;jcm [at] jonmasters.org&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Lucas De Marchi</code> &lt;lucas.de.marchi [at] gmail.com&gt;</p>
<dl>
<dd>Developer</dl>
