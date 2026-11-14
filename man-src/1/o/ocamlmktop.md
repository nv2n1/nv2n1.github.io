---
title: "ocamlmktop(1)"
name: "ocamlmktop"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlmktop/"
description: "ocamlmktop – Building custom toplevel systems"
---

<h2 class="name">NAME</h2>
<p> ocamlmktop &#8211; Building custom toplevel systems</p>
<h2>SYNOPSIS</h2>
<p> <code>ocamlmktop</code> [ <code>-v</code>|<code>-version</code>|<code>-vnum</code> ] [ <code>-cclib</code><i>&nbsp;<wbr>libname</i> ] [ <code>-ccopt</code><i>&nbsp;<wbr>option</i> ] [ <code>-custom</code> [ <code>-o</code><i>&nbsp;<wbr>exec-file</i> ] [ <code>-I</code><i>&nbsp;<wbr>lib-dir</i> ] <i>filename &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-ocamlmktop/">ocamlmktop</a></code>(1) command builds OCaml toplevels that contain user code preloaded at start-up. The <code><a href="/docs/linux/man/1-ocamlmktop/">ocamlmktop</a></code>(1) command takes as argument a set of <i>x</i>.cmo and <i>x</i>.cma files, and links them with the object files that implement the OCaml toplevel. If the <code>-custom</code> flag is given, C object files and libraries (.o and .a files) can also be given on the command line and are linked in the resulting toplevel. </p>
<h2>OPTIONS</h2>
<p> The following command-line options are recognized by <code><a href="/docs/linux/man/1-ocamlmktop/">ocamlmktop</a></code>(1).</p>
<dl>
<dt><code>-v</code></p>
<dd> Print the version string of the compiler and exit.</p>
<dt><code>-vnum</code>&nbsp;<wbr>or&nbsp;<wbr><code>-version</code></p>
<dd> Print the version number of the compiler in short form and exit.</p>
<dt><code>-cclib -l</code><i>libname</i></p>
<dd> Pass the <code>-l</code><i>libname</i> option to the C linker when linking in &#8220;custom runtime&#8221; mode (see the corresponding option for <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1).</p>
<dt><code>-ccopt</code></p>
<dd> Pass the given option to the C compiler and linker, when linking in &#8220;custom runtime&#8221; mode. See the corresponding option for <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1).</p>
<dt><code>-custom</code></p>
<dd> Link in &#8220;custom runtime&#8221; mode. See the corresponding option for <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1).</p>
<dt><code>-I</code><i>&nbsp;<wbr>directory</i></p>
<dd> Add the given directory to the list of directories searched for compiled interface files (.cmo and .cma).</p>
<dt><code>-o</code><i>&nbsp;<wbr>exec-file</i></p>
<dd> Specify the name of the toplevel file produced by the linker. The default is is <code>a.out</code>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1). </p>
<h2>Index</h2>
