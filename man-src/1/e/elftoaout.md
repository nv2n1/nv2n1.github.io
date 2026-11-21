---
title: "elftoaout(1)"
name: "elftoaout"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elftoaout/"
description: "elftoaout – ELF to a.out convertor"
---

<h2>NAME</h2>
<p> elftoaout &#8211; ELF to a.out convertor</p>
<h2>SYNOPSIS</h2>
<p> <code>elftoaout</code> [ <code>-b</code> ] [ <code>-o</code> <i>outfile</i> ] [ <code>-V</code> ] <i>infile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>elftoaout</code> converts a 32bit or 64bit SPARC ELF image to a.out format. This is needed for SPARC bootstraps, as Sun PROM expects a.out image when booting via net or tape or from the disk. On the disk, most of the people use <code>SILO, </code> which uses <i>elftoaout</i> to create first stage loader, but understands ELF format, so you don&#8217;t need to convert a kernel if you will boot it with <code>SILO.</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-b</i></dt>
<dd> <code>sun4</code> format. Unlike other PROMs ( <code>sun4[cdemu]</code> ), sun4 PROM does not understand the 32bit <code>a.out</code> header and thus this option strips the header from the image. Other PROMs need such a header, so use this only if you are building an image for <code>sun4</code> or other architectures that explicitly reqire a headerless image.</dd>
<dt><i>-V</i></dt>
<dd> Print <code>elftoaout</code> version and exit.</dd>
<dt><i>-o outfile</i></dt>
<dd> Specify output file name, instead of the default <code>a.out</code></dd>
<dt><i>-c</i></dt>
<dd> Compute an image checksum and store it in a.out header.</dd>
<dt><i>infile</i></dt>
<dd> Required parameter which specifies the ELF image to be converted.</dd></dl>
<h2>BUGS</h2>
<p> This utility can handle just a couple of specific cases needed for kernel and SILO conversions, but is not able to to convert all <code>ELF </code> binaries to <code>a.out.</code> It can only convert static binaries and has a couple of other limitations.</p>
<h2>AUTHOR</h2>
<p> <code>elftoaout</code> has been written by Pete A. Zaitcev &lt;zaitcev [at] vger.rutgers.edu&gt;, support for 64bit ELF has been added by Jakub Jelinek &lt;jj [at] ultra.linux.cz&gt;.</p>
<h2>AVAILABILITY</h2>
<p> <code>elftoaout</code> is available for anonymous ftp from sunsite.mff.cuni.cz in /OS/Linux/Sparc/local/elftoaout/.</p>
<h2>SEE ALSO</h2>
<p> <code>silo</code>(8) </p>
