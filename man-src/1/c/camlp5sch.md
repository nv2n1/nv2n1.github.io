---
title: "camlp5sch(1)"
name: "camlp5sch"
section: "1"
letter: "c"
url: "/docs/linux/man/1-camlp5sch/"
description: "camlp5 – Pre-Precessor-Pretty-Printer for OCaml mkcamlp5 – Create custom camlp5 mkcamlp5.opt – Create custom camlp5 (native code) ocpp5 – Universal preprocessor"
---

<h2>NAME</h2>
<p> camlp5 &#8211; Pre-Precessor-Pretty-Printer for OCaml<br />
 mkcamlp5 &#8211; Create custom camlp5<br />
 mkcamlp5.opt &#8211; Create custom camlp5 (native code)<br />
 ocpp5 &#8211; Universal preprocessor </p>
<h2>SYNOPSIS</h2>
<p> <code>camlp5</code> [ load-options ] [&#8211;] [ other-options ]<br />
 <code>camlp5o</code> [ load-options ] [&#8211;] [ other-options ]<br />
 <code>camlp5r</code> [ load-options ] [&#8211;] [ other-options ]<br />
 <code>camlp5sch</code> [ load-options ] [&#8211;] [ other-options ]<br />
 <code>camlp5o.cma</code><br />
 <code>camlp5r.cma</code><br />
 <code>camlp5sch.cma</code><br />
 <code>mkcamlp5</code><br />
 <code>mkcamlp5.opt</code><br />
 <code>ocpp5</code> [ load-options ] file </p>
<p> <code>camlp5o.opt</code> [&#8211;] [ other-options ]<br />
 <code>camlp5r.opt</code> [&#8211;] [ other-options ] </p>
<h2>DESCRIPTION</h2>
<p> <code>camlp5</code> is a Pre-Processor-Pretty-Printer for OCaml, parsing a source file and printing some result on standard output. </p>
<p> <code>camlp5o,</code> <code>camlp5r</code> and <code>camlp5sch</code> are versions of <code>camlp5</code> with some files already loaded (see further). </p>
<p> <code>camlp5o.cma,</code> <code>camlp5r.cma</code> and <code>camlp5sch.cma</code> are files to be loaded in ocaml toplevel to use the camlp5 machinery </p>
<p> <code>mkcamlp5</code> and <code>mkcamlp5.opt</code> creates camlp5 executables with almost the same options than ocamlmktop. See further. </p>
<p> <code>ocpp5</code> is an universal preprocessor, treating any kind of source file, generating the same text with the possible quotations expanded. </p>
<p> <code>camlp5o.opt</code> and <code>camlp5r.opt</code> are versions of camlp5o and camlp5r compiled by the native-code compiler ocamlopt. They are faster but not extensible. And they are not available in all installations of camlp5. </p>
<h2>LOAD OPTIONS</h2>
<p> The load options select parsing and printing actions recorded in OCaml object files (ending with .cmo or .cma). Several usage of these options are authorized. They must precede the other options. </p>
<p> An optionnal <code>&#8212;</code> may end the load options. </p>
<dl>
<dt><code>-I&nbsp;<wbr></code><i>directory</i></p>
<dd> Add <i>directory</i> in the search path for files loaded. Unless the option -nolib is used, the camlp5 library directory is appended to the path. Warning: there is no automatic search in the current directory: add &quot;-I .&quot; for this.</p>
<dt><code>-where</code></p>
<dd> Print camlp5 library directory name and exit.</p>
<dt><code>-nolib</code></p>
<dd> No automatic search for objects files in camlp5 library directory.</p>
<dt><code>object-file</code></p>
<dd> The file is loaded in camlp5 core. </p>
</dl>
<h2>OTHER OPTIONS</h2>
<p> The others options are: </p>
<dl>
<dt><i>file</i></p>
<dd> Treat <i>file</i> as an interface file if it ends with .mli and as an implementation file if it ends with .ml. </p>
<dt><code>-intf&nbsp;<wbr></code><i>file</i></p>
<dd> Treat <i>file</i> as an interface file, whatever its extension.</p>
<dt><code>-impl&nbsp;<wbr></code><i>file</i></p>
<dd> Treat <i>file</i> as an implementation file, whatever its extension.</p>
<dt><code>-unsafe</code></p>
<dd> Generate unsafe accesses to arrays and strings.</p>
<dt><code>-noassert</code></p>
<dd> Do not compile assertion checks.</p>
<dt><code>-verbose</code></p>
<dd> More verbose in parsing errors.</p>
<dt><code>-QD&nbsp;<wbr></code><i>file</i></p>
<dd> Dump in <i>file</i> in case of syntax error in the result of a quotation expansion.</p>
<dt><code>-o&nbsp;<wbr></code><i>out-file</i></p>
<dd> Print the result on out-file instead of standard output. File is opened with open_out_bin (see OCaml library Pervasives).</p>
<dt><code>-v</code></p>
<dd> Print the version number and exit.</p>
<dt><code>-help</code></p>
<dd> Print the available options and exit. This print includes the options possibly added by the loaded object files. </p>
</dl>
<p> The others options can be extended by loaded object files. The provided files add the following options: </p>
<dl>
<dt><code>-l&nbsp;<wbr></code><i>line-length</i></p>
<dd> Added by pr_o.cmo and pr_r.cmo: set the line length (default 78).</p>
<dt><code>-sep&nbsp;<wbr></code><i>string</i></p>
<dd> Added by pr_o.cmo and pr_r.cmo: print this string between phrases instead of comments.</p>
<dt><code>-no_ss</code></p>
<dd> Added by pr_o.cmo: do not print double semicolons</p>
<dt><code>-D&nbsp;<wbr></code><i>ident</i></p>
<dd> Added by pa_macro.cmo: define the ident.</p>
<dt><code>-U&nbsp;<wbr></code><i>ident</i></p>
<dd> Added by pa_macro.cmo: undefine the ident. </p>
</dl>
<h2>PROVIDED FILES</h2>
<p> These files are installed in the directory /usr/lib64/ocaml/camlp5. </p>
<p> Parsing files: </p>
<pre><code>
 pa_r.cmo: revised syntax
 pa_rp.cmo: streams and parsers
 pa_lexer.cmo: lexers
 pa_o.cmo: normal syntax
 pa_op.cmo: streams and parsers
 pa_oop.cmo: streams and parsers (without code optimization)
 pa_scheme.cmo: scheme syntax
 pa_extend.cmo: syntax extension for grammars
 pa_extfold.cmo: extension of pa_extend with FOLD0 and FOLD1
 pa_extfun.cmo: syntax extension for extensible functions
 pa_extprint.cmo: syntax extensions for extensible printers
 pa_pprintf.cmo: syntax extension for pprintf statement
 pa_fstream.cmo: syntax extension for functional streams
 pa_macro.cmo: add macros (ifdef, define)
 like in C
         pa_lefteval.cmo : left -
     to - right evaluation of parameters pa_pragma.cmo : directive #pragma
</code></pre>
<p> Printing files: </p>
<pre>
 pr_r.cmo: revised syntax without objects and labels
 pr_ro.cmo: revised syntax for objects and labels
 pr_rp.cmo: try to rebuild streams and parsers syntax
 pr_o.cmo: normal syntax
 pr_op.cmo: try to rebuild streams and parsers syntax
 pr_scheme.cmo: Scheme syntax
 pr_schemep.cmo: try to rebuild streams and parsers syntax
 pr_extend.cmo: try to rebuild EXTEND statements
 pr_extfun.cmo: try to rebuild extfun statements
 pr_extprint.cmo: try to rebuild EXTEND_PRINTER statements
 pr_dump.cmo: dump syntax tree for ocaml compiler
 pr_depend.cmo: file dependencies
 pr_null.cmo: no output
</pre>
<p> Quotation expanders: </p>
<pre>
 q_MLast.cmo: syntax tree nodes (in revised syntax)
 q_ast.cmo: syntax tree nodes in user full syntax
 q_phony.cmo: keeping quotations for pretty printing
</pre>
<p> The command <code>camlp5o</code> is a shortcut for: </p>
<pre>
 camlp5 pa_o.cmo pa_op.cmo pr_dump.cmo
</pre>
<p> The command <code>camlp5r</code> is a shortcut for: </p>
<pre>
 camlp5 pa_r.cmo pa_rp.cmo pr_dump.cmo
</pre>
<p> The command <code>camlp5sch</code> is a shortcut for: </p>
<pre>
 camlp5 pa_scheme.cmo pr_dump.cmo
</pre>
<p> The file <code>camlp5o.cma</code> can be loaded in the toplevel to start camlp5 with OCaml syntax. </p>
<p> The file <code>camlp5r.cma</code> can be loaded in the toplevel to start camlp5 with revised syntax. </p>
<p> The file <code>camlp5sch.cma</code> can be loaded in the toplevel to start camlp5 with Scheme syntax. </p>
<h2>MKCAMLP5</h2>
<p> <code>mkcamlp5</code> and <code>mkcamlp5.opt</code> creates camlp5 executables with almost the same options than ocamlmktop. The version <code>mkcamlp5.opt</code> can create native code executables, faster but not extensible. </p>
<p> For mkcamlp5, the interfaces to be visible must be explicitly added in the command line as &quot;.cmi&quot; files. For example, how to add the the OCaml module &quot;str&quot;: </p>
<pre>
 mkcamlp5 -custom str.cmi str.cma -cclib -lstr -o camlp5str
</pre>
<h2>ENVIRONMENT VARIABLE</h2>
<p> The following environment variable is also consulted: </p>
<dl>
<dt><code>CAMLP5PARAM</code></p>
<dd> Set the grammars parsing algorithm parameters. This variable must be a sequence of parameter specifications. A parameter specification is a letter optionally followed by an = and a value. There are four possible parameters: </p>
<dt><code>b</code>&nbsp;<wbr>(backtrack)</p>
<dd> Set the backtrack algorithm as default.</p>
<dt><code>t</code>&nbsp;<wbr>(trace)</p>
<dd> Trace symbols (terminals and non-terminals) while parsing with backtracking.</p>
<dt><code>y</code>&nbsp;<wbr>(trace-stalling)</p>
<dd> In backtracking, trace the advance in the input stream (number of unfrozen tokens) and the possible stalling (number of tokens tests).</p>
<dt><code>l</code>&nbsp;<wbr>(maximum-stalling)</p>
<dd> Set the maximum stalling value. </p>
</dl>
<h2>FILES</h2>
<p> Library directory of camlp5 in the present installation:<br />
 /usr/lib64/ocaml/camlp5 </p>
<h2>SEE ALSO</h2>
<p> Camlp5 &#8211; Reference Manual<br />
 <a href="/docs/linux/man/1-ocamlc/">ocamlc</a>(1), <a href="/docs/linux/man/1-ocaml/">ocaml</a>(1), <a href="/docs/linux/man/1-ocamlmktop/">ocamlmktop</a>(1). </p>
<h2>AUTHOR</h2>
<p> Daniel de Rauglaudre, INRIA Rocquencourt. </p>
<h2>Index</h2>
