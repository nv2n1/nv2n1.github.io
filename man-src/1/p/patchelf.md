---
title: "patchelf(1)"
name: "patchelf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-patchelf/"
description: "patchelf – Modify ELF files"
---

<h2>NAME</h2>
<p> patchelf &#8211; Modify ELF files </p>
<h2>SYNOPSIS</h2>
<p> <code>patchelf</code> <i>OPTION</i> <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> PatchELF is a simple utility for modifying existing ELF executables and libraries. It can change the dynamic loader (&quot;ELF interpreter&quot;) of executables and change the RPATH of executables and libraries. </p>
<h2>OPTIONS</h2>
<p> The single option given operates on a given FILE, editing in place. </p>
<dl>
<dt>&#8211;set-interpreter INTERPRETER</dt>
<dd> Change the dynamic loader (&quot;ELF interpreter&quot;) of executable given to INTERPRETER. </dd>
<dt>&#8211;print-intepreter</dt>
<dd> Prints the ELF interpreter of the executable. </dd>
<dt>&#8211;set-rpath RPATH</dt>
<dd> Change the RPATH of the executable or library to RPATH. </dd>
<dt>&#8211;shrink-rpath</dt>
<dd> Remove from the RPATH all directories that do not contain a library referenced by DT_NEEDED fields of the executable or library. </dd>
<p> For instance, if an executable references one library libfoo.so, has an RPATH &quot;/lib:/usr/lib:/foo/lib&quot;, and libfoo.so can only be found in /foo/lib, then the new RPATH will be &quot;/foo/lib&quot;. </p>
<dt>&#8211;print-rpath</dt>
<dd> Prints the RPATH for an executable or library. </dd>
<dt>&#8211;force-rpath</dt>
<dd> Forces the use of the obsolete DT_RPATH in the file instead of DT_RUNPATH. By default DT_RPATH is converted to DT_RUNPATH. </dd>
<dt>&#8211;debug</dt>
<dd> Prints details of the changes made to the input file. </dd>
<dt>&#8211;version</dt>
<dd> Shows the version of patchelf. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Eelco Dolstra &lt;e.dolstra [at] tudelft.nl&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-elf/">elf</a></code>(5), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8) </p>
