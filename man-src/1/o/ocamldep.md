---

title: "ocamldep(1)"
name: "ocamldep"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamldep/"
description: "ocamldep – Dependency generator for OCaml"
---

<p> ocamldep &#8211; Dependency generator for OCaml</p>
<h2>SYNOPSIS</h2>
<p> <code>ocamldep</code> [ <i>options</i> ] <i>filename &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-ocamldep/">ocamldep</a></code>(1) command scans a set of OCaml source files (.ml and .mli files) for references to external compilation units, and outputs dependency lines in a format suitable for the <code><a href="/docs/linux/man/1-make/">make</a></code>(1) utility. This ensures that make will compile the source files in the correct order, and recompile those files that need to when a source file is modified. </p>
<p> The typical usage is: </p>
<p> ocamldep <i>options</i> *.mli *.ml &gt; .depend </p>
<p> where .depend is the file that should contain the dependencies. </p>
<p> Dependencies are generated both for compiling with the bytecode compiler <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) and with the native-code compiler <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1). </p>
<h2>OPTIONS</h2>
<p> The following command-line options are recognized by <code><a href="/docs/linux/man/1-ocamldep/">ocamldep</a></code>(1).</p>
<dl>
<dt><code>-absname</code></dt>
<dd> Show absolute filenames in error messages.</dd>
<dt><code>-I</code><i>&nbsp;<wbr>directory</i></dt>
<dd> Add the given directory to the list of directories searched for source files. If a source file foo.ml mentions an external compilation unit Bar, a dependency on that unit&#8217;s interface bar.cmi is generated only if the source for bar is found in the current directory or in one of the directories specified with <code>-I</code>. Otherwise, Bar is assumed to be a module from the standard library, and no dependencies are generated. For programs that span multiple directories, it is recommended to pass <code><a href="/docs/linux/man/1-ocamldep/">ocamldep</a></code>(1) the same <code>-I</code> options that are passed to the compiler.</dd>
<dt><code>-ml-synonym</code><i>&nbsp;<wbr>.ext</i></dt>
<dd> Consider the given extension (with leading dot) to be a synonym for .ml.</dd>
<dt><code>-mli-synonym</code><i>&nbsp;<wbr>.ext</i></dt>
<dd> Consider the given extension (with leading dot) to be a synonym for .mli.</dd>
<dt><code>-modules</code></dt>
<dd> Output raw dependencies of the form <i>filename</i>:<i>&nbsp;<wbr>Module1 Module2</i>&nbsp;<wbr>&#8230;<i>&nbsp;<wbr>ModuleN</i> where <i>Module1</i>, &#8230;,<i>&nbsp;<wbr>ModuleN</i> are the names of the compilation units referenced within the file <i>filename</i>, but these names are not resolved to source file names. Such raw dependencies cannot be used by <code><a href="/docs/linux/man/1-make/">make</a></code>(1), but can be post-processed by other tools such as <code>Omake</code>(1).</dd>
<dt><code>-native</code></dt>
<dd> Generate dependencies for a pure native-code program (no bytecode version). When an implementation file (.ml file) has no explicit interface file (.mli file), <code><a href="/docs/linux/man/1-ocamldep/">ocamldep</a></code>(1) generates dependencies on the bytecode compiled file (.cmo file) to reflect interface changes. This can cause unnecessary bytecode recompilations for programs that are compiled to native-code only. The flag <code>-native</code> causes dependencies on native compiled files (.cmx) to be generated instead of on .cmo files. (This flag makes no difference if all source files have explicit .mli interface files.)</dd>
<dt><code>-pp</code><i>&nbsp;<wbr>command</i></dt>
<dd> Cause <code><a href="/docs/linux/man/1-ocamldep/">ocamldep</a></code>(1) to call the given <i>command</i> as a preprocessor for each source file.</dd>
<dt><code>-ppx</code><i>&nbsp;<wbr>command</i></dt>
<dd> Pipe abstract syntax tree through preprocessor <i>command</i>.</dd>
<dt><code>-slash</code></dt>
<dd> Under Unix, this option does nothing.</dd>
<dt><code>-version</code></dt>
<dd> Print version string and exit.</dd>
<dt><code>-vnum</code></dt>
<dd> Print short version number and exit.</dd>
<dt><code>-help</code>&nbsp;<wbr>or<code>&nbsp;<wbr>&#8211;help</code></dt>
<dd> Display a short usage summary and exit. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1), <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1).<br/>
 <i>The OCaml user&#8217;s manual</i>, chapter &quot;Dependency generator&quot;. </p>
