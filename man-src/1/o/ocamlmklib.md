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
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-cclib&nbsp;<wbr></code><i>lib</i></dt>
<dd> C library passed to ocamlc <code>-a</code> or <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) <code>-a</code> only.</dd>
<dt><code>-ccopt&nbsp;<wbr></code><i>opt</i></dt>
<dd> C option passed to <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) <code>-a</code> or <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) <code>-a</code> only.</dd>
<dt><code>-custom</code></dt>
<dd> Disable dynamic loading.</dd>
<dt><code>-dllpath&nbsp;<wbr></code><i>dir</i></dt>
<dd> Add <i>dir</i> to the run-time search path for DLLs.</dd>
<dt><code>-I&nbsp;<wbr></code><i>dir</i></dt>
<dd> Add <i>dir</i> to the path searched for Caml object files.</dd>
<dt><code>-failsafe</code></dt>
<dd> Fall back to static linking if DLL construction failed.</dd>
<dt><code>-ldopt opt</code></dt>
<dd> C option passed to the shared linker only.</dd>
<dt><code>-linkall</code></dt>
<dd> Build Caml archive with link-all behavior.</dd>
<dt><code>-l</code><i>lib</i></dt>
<dd> Specify a dependent C library.</dd>
<dt><code>-L</code><i>dir</i></dt>
<dd> Add <i>dir</i> to the path searched for C libraries.</dd>
<dt><code>-ocamlc&nbsp;<wbr></code><i>cmd</i></dt>
<dd> Use <i>cmd</i> in place of <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1).</dd>
<dt><code>-ocamlopt&nbsp;<wbr></code><i>cmd</i></dt>
<dd> Use <i>cmd</i> in place of <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1).</dd>
<dt><code>-o&nbsp;<wbr></code><i>name</i></dt>
<dd> Generated Caml library is named <i>name</i>.cma or <i>name</i>.cmxa.</dd>
<dt><code>-oc&nbsp;<wbr></code><i>name</i></dt>
<dd> Generated C library is named dll<i>name</i>.so or lib<i>name</i>.a.</dd>
<dt><code>-rpath&nbsp;<wbr></code><i>dir</i></dt>
<dd> Same as <code>-dllpath</code> <i>dir</i>.</dd>
<dt><code>-R</code><i>dir</i></dt>
<dd> Same as <code>-rpath</code>.</dd>
<dt><code>-verbose</code></dt>
<dd> Print commands before executing them.</dd>
<dt><code>-Wl</code>, <code>-rpath </code><i>dir</dt>
<dd> Same as </i><code>-dllpath</code> <i>dir</i>.</dd>
<dt><code>-Wl</code>, <code>-rpath -Wl </code><i>dir</dt>
<dd> Same as </i><code>-dllpath</code> <i>dir</i>.</dd>
<dt><code>-Wl</code>, <code>-R</code><i>dir</dt>
<dd> Same as </i><code>-dllpath</code> <i>dir</i>.</dd>
<dt><code>-F</code><i>dir</i></dt>
<dd> Specify a framework directory (MacOSX).</dd>
<dt><code>-framework&nbsp;<wbr></code><i>name</i></dt>
<dd> Use framework <i>name</i> (MacOSX).</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1), <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Samuel Mimram &lt;samuel.mimram [at] ens-lyon.org&gt;, for the Debian project (but may be used by others). </p>
