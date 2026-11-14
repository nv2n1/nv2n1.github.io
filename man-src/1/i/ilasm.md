---
title: "ilasm(1)"
name: "ilasm"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ilasm/"
description: "ilasm, ilasm2 – Mono IL assembler"
---

<h2>NAME</h2>
<p> ilasm, ilasm2 &#8211; Mono IL assembler</p>
<h2>SYNOPSIS</h2>
<p> <code>ilasm</code> [option] [source-files] </p>
<p> <code>ilasm2</code> [option] [source-files]</p>
<h2>DESCRIPTION</h2>
<p> ilasm is the Mono ILAsm assembler. You can pass one or more options to drive the compiler, and a set of source files. </p>
<p> Use <i>ilasm</i> to generate 1.0 assemblies and use <i>ilasm2</i> to assemble programs that use the 2.0 features (generics). </p>
<p> The Mono ILAsm assembler accepts options starting with / or &#8211; for mosted options. </p>
<p> The Mono ILAsm assembler generates images (.exe and .dll files) that contain CIL byte code that can be executed by any system that implemented a Common Language Infrastructure virtual machine.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>//output:&lt;file_name&gt;</code></p>
<dd> Specify the output file name.</p>
<dt><code>//exe </code></p>
<dd> Generate an exe</p>
<dt><code>//dll</code></p>
<dd> Generate a library</p>
<dt><code>//scan_only</code></p>
<dd> Just scan the IL code and display tokens.</p>
<dt><code>//show_tokens</code></p>
<dd> Show tokens as they are parsed.</p>
<dt><code>//show_method_def </code></p>
<dd> Display method information when a method is defined.</p>
<dt><code>//show_method_ref</code></p>
<dd> Display method information when a method is referenced</p>
<dt><code>//key:KEYFILE</code></p>
<dd> Strongname (sign) the output assembly using the key pair present in the specified strong name key file (snk). A full key pair is required (i.e. delay signing is done using a .publickey directive in the sources).</p>
<dt><code>//key:@CONTAINER</code></p>
<dd> Strongname (sign) the output assembly using the key pair present in the specified container.</p>
<dt><code>&#8211;about</code></p>
<dd> Display information about ilasm</p>
<dt><code>&#8211;version</code></p>
<dd> Display ilasm version</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mono/">mono</a>(1),</code><a href="/docs/linux/man/1-mcs/">mcs</a>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2004, 2007 Novell, Inc (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a></p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit: <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
