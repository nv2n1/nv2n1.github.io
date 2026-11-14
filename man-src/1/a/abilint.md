---
title: "abilint(1)"
name: "abilint"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abilint/"
description: "abilint – validate an abigail ABI representation"
---

<h2>NAME</h2>
<p> abilint &#8211; validate an abigail ABI representation </p>
<p> abilint parses the native XML representation of an ABI as emitted by <code>abidw</code>. Once it has parsed the XML representation of the ABI, <code>abilint</code> builds and in-memory model from it. It then tries to save it back to an XML form, to standard output. If that read-write operation succeeds chances are the input XML ABI representation is meaningful. </p>
<p> Note that the main intent of this tool to help debugging issues in the underlying Libabigail library. </p>
<p> Note also that <code>abilint</code> can also read an <i>ELF</i> input file, build the in-memory model for its ABI, and serialize that model back into XML to standard output. In that case, the <i>ELF</i> input file must be accompanied with its debug information in the <i>DWARF</i> format.</p>
<h2>INVOCATION</h2>
<pre><code>
abilint[options][&lt;abi - file1&gt;]
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;help</code> </p>
<p> Display a short help message and exits.</p>
<dt>&bull;</p>
<dd> <i>&#8211;version | -v</i> </p>
<p> Display the version of the program and exit.</p>
<dt>&bull;</p>
<dd> <code>&#8211;debug-info-dir</code> &lt;<i>path</i>&gt; </p>
<p> When reading an <i>ELF</i> input file which debug information is split out into a separate file, this options tells <code>abilint</code> where to find that separate debug information file. </p>
<p> Note that <i>path</i> must point to the root directory under which the debug information is arranged in a tree-like manner. Under Red Hat based systems, that directory is usually <code>&lt;root&gt;/usr/lib/debug</code>. </p>
<p> Note also that this option is not mandatory for split debug information installed by your system&#8217;s package manager because then <code>abidiff</code> knows where to find it.</p>
<dt>&bull;</p>
<dd> <code>&#8211;diff</code> </p>
<p> For XML inputs, perform a text diff between the input and the memory model saved back to disk. This can help to spot issues in the handling of the XML format by the underlying Libabigail library.</p>
<dt>&bull;</p>
<dd> <code>&#8211;noout</code> </p>
<p> Do not display anything on standard output. The return code of the command is the only way to know if the command succeeded.</p>
<dt>&bull;</p>
<dd> <code>&#8211;suppressions | suppr</code> &lt;<i>path-to-suppression-specifications-file</i>&gt; </p>
<p> Use a <i>suppression specification</i> file located at <i>path-to-suppression-specifications-file</i>. Note that this option can appear multiple times on the command line. In that case, all of the provided suppression specification files are taken into account. ABI artifacts matched by the suppression specifications are suppressed from the output of this tool.</p>
<dt>&bull;</p>
<dd> <code>&#8211;headers-dir | &#8211;hd</code> &lt;headers-directory-path-1&gt; </p>
<p> Specifies where to find the public headers of the first shared library that the tool has to consider. The tool will thus filter out types that are not defined in public headers.</p>
<dt>&bull;</p>
<dd> <code>&#8211;stdin | &#8212;</code> </p>
<p> Read the input content from standard input.</p>
<dt>&bull;</p>
<dd> <code>&#8211;tu</code> </p>
<p> Expect the input XML to represent a single translation unit.</dl>
<h2>AUTHOR</h2>
<p> Dodji Seketeli</p>
<h2>COPYRIGHT</h2>
<p> 2014-2016, Red Hat, Inc. </p>
<h2>Index</h2>
