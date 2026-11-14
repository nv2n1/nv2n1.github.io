---
title: "grub2-syslinux2cfg(1)"
name: "grub2-syslinux2cfg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub2-syslinux2cfg/"
description: "grub-syslinux2cfg — Transform a syslinux config file into a GRUB config."
---

<h2>NAME</h2>
<p> <code>grub-syslinux2cfg</code> &#8212; Transform a syslinux config file into a GRUB config. </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-syslinux2cfg</code> [-c | &#8211;cwd=DIR<i>] [-r | &#8211;root=DIR</i>] [-v | &#8211;verbose]</p>
<dl>
<dt>
<dd> [-t | &#8211;target-root=<i>DIR</i>] [-T | &#8211;target-cwd=<i>DIR</i>]</dl>
<dl>
<dt>
<dd> [-o | &#8211;output=<i>FILE</i>] [[-i | &#8211;isolinux] |</dl>
<dl>
<dt>
<dd>
&nbsp;<wbr>[-s | &#8211;syslinux]&nbsp;<wbr>|</dl>
<dl>
<dt>
<dd>
&nbsp;<wbr>[-p | &#8211;pxelinux]]&nbsp;<wbr><i>FILE</i> </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>grub-syslinux2cfg</code> builds a GRUB configuration file out of an existing syslinux configuration file. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;cwd=<i>DIR</i></p>
<dd> Set <i>DIR</i> as syslinux&#8217;s working directory. The default is to use the parent directory of the input file. </p>
<dt>&#8211;root=<i>DIR</i></p>
<dd> Set <i>DIR</i> as the root directory of the syslinux disk. The default value is &quot;/&quot;. </p>
<dt>&#8211;verbose</p>
<dd> Print verbose messages. </p>
<dt>&#8211;target-root=<i>DIR</i></p>
<dd> Root directory as it will be seen at runtime. The default value is &quot;/&quot;. </p>
<dt>&#8211;target-cwd=<i>DIR</i></p>
<dd> Working directory of syslinux as it will be seen at runtime. The default value is the parent directory of the input file. </p>
<dt>&#8211;output=<i>FILE</i></p>
<dd> Write the new config file to <i>FILE</i>. The default value is standard output. </p>
<dt>&#8211;isolinux</p>
<dd> Assume that the input file is an isolinux configuration file. </p>
<dt>&#8211;pxelinux</p>
<dd> Assume that the input file is a pxelinux configuration file. </p>
<dt>&#8211;syslinux</p>
<dd> Assume that the input file is a syslinux configuration file. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code>info grub</code> </p>
<h2>Index</h2>
