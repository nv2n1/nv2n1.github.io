---
title: "ocamlmklib(1)"
name: "ocamlmklib"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlmklib/"
description: "ocamlmklib – generate libraries with mixed C / Caml code."
---

<h2 class="name">NAME</h2>
<p> ocamlmklib &#8211; generate libraries with mixed C / Caml code. </p>
<h2>SYNOPSIS</h2>
<p> <code>ocalmklib</code> [<i>options</i>]<i> files</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>ocamlmklib</code> command facilitates the construction of libraries containing both Caml code and C code, and usable both in static linking and dynamic linking modes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-cclib&nbsp;<wbr></code><i>lib</i></p>
<dd> C library passed to ocamlc <code>-a</code> or <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) <code>-a</code> only.</p>
<dt><code>-ccopt&nbsp;<wbr></code><i>opt</i></p>
<dd> C option passed to <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) <code>-a</code> or <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) <code>-a</code> only.</p>
<dt><code>-custom</code></p>
<dd> Disable dynamic loading.</p>
<dt><code>-dllpath&nbsp;<wbr></code><i>dir</i></p>
<dd> Add <i>dir</i> to the run-time search path for DLLs.</p>
<dt><code>-I&nbsp;<wbr></code><i>dir</i></p>
<dd> Add <i>dir</i> to the path searched for Caml object files.</p>
<dt><code>-failsafe</code></p>
<dd> Fall back to static linking if DLL construction failed.</p>
<dt><code>-ldopt opt</code></p>
<dd> C option passed to the shared linker only.</p>
<dt><code>-linkall</code></p>
<dd> Build Caml archive with link-all behavior.</p>
<dt><code>-l</code><i>lib</i></p>
<dd> Specify a dependent C library.</p>
<dt><code>-L</code><i>dir</i></p>
<dd> Add <i>dir</i> to the path searched for C libraries.</p>
<dt><code>-ocamlc&nbsp;<wbr></code><i>cmd</i></p>
<dd> Use <i>cmd</i> in place of <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1).</p>
<dt><code>-ocamlopt&nbsp;<wbr></code><i>cmd</i></p>
<dd> Use <i>cmd</i> in place of <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1).</p>
<dt><code>-o&nbsp;<wbr></code><i>name</i></p>
<dd> Generated Caml library is named <i>name</i>.cma or <i>name</i>.cmxa.</p>
<dt><code>-oc&nbsp;<wbr></code><i>name</i></p>
<dd> Generated C library is named dll<i>name</i>.so or lib<i>name</i>.a.</p>
<dt><code>-rpath&nbsp;<wbr></code><i>dir</i></p>
<dd> Same as <code>-dllpath</code> <i>dir</i>.</p>
<dt><code>-R</code><i>dir</i></p>
<dd> Same as <code>-rpath</code>.</p>
<dt><code>-verbose</code></p>
<dd> Print commands before executing them.</p>
<dt><code>-Wl</code>, <code>-rpath </code><i>dir</p>
<dd> Same as </i><code>-dllpath</code> <i>dir</i>.</p>
<dt><code>-Wl</code>, <code>-rpath -Wl </code><i>dir</p>
<dd> Same as </i><code>-dllpath</code> <i>dir</i>.</p>
<dt><code>-Wl</code>, <code>-R</code><i>dir</p>
<dd> Same as </i><code>-dllpath</code> <i>dir</i>.</p>
<dt><code>-F</code><i>dir</i></p>
<dd> Specify a framework directory (MacOSX).</p>
<dt><code>-framework&nbsp;<wbr></code><i>name</i></p>
<dd> Use framework <i>name</i> (MacOSX).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1), <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Samuel Mimram &lt;samuel.mimram [at] ens-lyon.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
