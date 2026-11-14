---
title: "abidw(1)"
name: "abidw"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abidw/"
description: "abidw – serialize the ABI of an ELF file"
---

<h2>NAME</h2>
<p> abidw &#8211; serialize the ABI of an ELF file </p>
<p> abidw reads a shared library in <i>ELF</i> format and emits an XML representation of its ABI to standard output. The emitted representation includes all the globally defined functions and variables, along with a complete representation of their types. It also includes a representation of the globally defined ELF symbols of the file. The input shared library must contain associated debug information in <i>DWARF</i> format.</p>
<h2>INVOCATION</h2>
<pre><code>
abidw[options][&lt;path - to - elf - file&gt;]
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;help | -h</code> </p>
<p> Display a short help about the command and exit.</p>
<dt>&bull;</p>
<dd> <i>&#8211;version | -v</i> </p>
<p> Display the version of the program and exit.</p>
<dt>&bull;</p>
<dd> <code>&#8211;debug-info-dir | -d</code> &lt;<i>dir-path</i>&gt; </p>
<p> In cases where the debug info for <i>path-to-elf-file</i> is in a separate file that is located in a non-standard place, this tells <code>abidw</code> where to look for that debug info file. </p>
<p> Note that <i>dir-path</i> must point to the root directory under which the debug information is arranged in a tree-like manner. Under Red Hat based systems, that directory is usually <code>&lt;root&gt;/usr/lib/debug</code>. </p>
<p> Note that this option is not mandatory for split debug information installed by your system&#8217;s package manager because then <code>abidw</code> knows where to find it.</p>
<dt>&bull;</p>
<dd> <code>&#8211;out-file</code> &lt;<i>file-path</i>&gt; </p>
<p> This option instructs <code>abidw</code> to emit the XML representation of <i>path-to-elf-file</i> into the file <i>file-path</i>, rather than emitting it to its standard output.</p>
<dt>&bull;</p>
<dd> <code>&#8211;noout</code> </p>
<p> This option instructs <code>abidw</code> to not emit the XML representation of the ABI. So it only reads the ELF and debug information, builds the internal representation of the ABI and exits. This option is usually useful for debugging purposes.</p>
<dt>&bull;</p>
<dd> <code>&#8211;suppressions | suppr</code> &lt;<i>path-to-suppression-specifications-file</i>&gt; </p>
<p> Use a <i>suppression specification</i> file located at <i>path-to-suppression-specifications-file</i>. Note that this option can appear multiple times on the command line. In that case, all of the provided suppression specification files are taken into account. ABI artifacts matched by the suppression specifications are suppressed from the output of this tool.</p>
<dt>&bull;</p>
<dd> <code>&#8211;headers-dir | &#8211;hd</code> &lt;headers-directory-path-1&gt; </p>
<p> Specifies where to find the public headers of the first shared library that the tool has to consider. The tool will thus filter out types that are not defined in public headers.</p>
<dt>&bull;</p>
<dd> <code>&#8211;check-alternate-debug-info</code> &lt;<i>elf-path</i>&gt; </p>
<p> If the debug info for the file <i>elf-path</i> contains a reference to an <i>alternate debug info</i> file, <code>abidw</code> checks that it can find that alternate debug info file. In that case, it emits a meaningful success message mentioning the full path to the alternate debug info file found. Otherwise, it emits an error code.</p>
<dt>&bull;</p>
<dd> <code>&#8211;no-show-locs</code> Do not show information about where in the <i>second shared library</i> the respective type was changed.</p>
<dt>&bull;</p>
<dd> <code>&#8211;check-alternate-debug-info-base-name</code> &lt;<i>elf-path</i>&gt; </p>
<p> Like <code>&#8211;check-alternate-debug-info</code>, but in the success message, only mention the base name of the debug info file; not its full path.</p>
<dt>&bull;</p>
<dd> <code>&#8211;load-all-types</code> </p>
<p> By default, <code>libabigail</code> (and thus <code>abidw</code>) only loads types that are reachable from functions and variables declarations that are publicly defined and exported by the binary. So only those types are present in the output of <code>abidw</code>. This option however makes <code>abidw</code> load <i>all</i> the types defined in the binaries, even those that are not reachable from public declarations.</p>
<dt>&bull;</p>
<dd> <code>&#8211;abidiff</code> Load the ABI of the ELF binary given in argument, save it in libabigail&#8217;s XML format in a temporary file; read the ABI from the temporary XML file and compare the ABI that has been read back against the ABI of the ELF binary given in argument. The ABIs should compare equal. If they don&#8217;t, the program emits a diagnostic and exits with a non-zero code. </p>
<p> This is a debugging and sanity check option.</p>
<dt>&bull;</p>
<dd> <code>&#8211;stats</code> </p>
<p> Emit statistics about various internal things.</p>
<dt>&bull;</p>
<dd> <code>&#8211;verbose</code> </p>
<p> Emit verbose logs about the progress of miscellaneous internal things.</dl>
<h2>NOTES</h2>
<h3>Alternate debug info files</h3>
<p> As of the version 4 of the DWARF specification, <i>Alternate debug information</i> is a <i>GNU</i> extension to the DWARF specification. It has however been proposed for inclusion into the upcoming version 5 of the DWARF standard. You can read more about the GNU extensions to the DWARF standard <i>here</i>.</p>
<h2>AUTHOR</h2>
<p> Dodji Seketeli</p>
<h2>COPYRIGHT</h2>
<p> 2014-2016, Red Hat, Inc. </p>
<h2>Index</h2>
<dt><a href="#lbAG">AUTHOR</a></p>
<dd>
<dt><a href="#lbAH">COPYRIGHT</a></p>
<dd></dl>
