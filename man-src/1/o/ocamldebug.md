---

title: "ocamldebug(1)"
name: "ocamldebug"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamldebug/"
description: "ocamldebug – the OCaml source-level replay debugger."
---

<p> ocamldebug &#8211; the OCaml source-level replay debugger. </p>
<h2>SYNOPSIS</h2>
<p> <code>ocamldebug</code> [&nbsp;<wbr><i>options</i>&nbsp;<wbr>]&nbsp;<wbr><i>program</i>&nbsp;<wbr>[&nbsp;<wbr><i>arguments</i>&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ocamldebug</code> is the OCaml source-level replay debugger. </p>
<p> Before the debugger can be used, the program must be compiled and linked with the <code>-g</code> option: all .cmo and .cma files that are part of the program should have been created with <code>ocamlc -g</code>, and they must be linked together with <code>ocamlc -g</code>. </p>
<p> Compiling with <code>-g</code> entails no penalty on the running time of programs: object files and bytecode executable files are bigger and take longer to produce, but the executable files run at exactly the same speed as if they had been compiled without <code>-g</code>. </p>
<h2>OPTIONS</h2>
<p> A summary of options are included below. For a complete description, see the html documentation in the ocaml-doc package.</p>
<dl>
<dt><code>-c</code><i>&nbsp;<wbr>count</i></dt>
<dd> Set the maximum number of simultaneously live checkpoints to <i>count</i>.</dd>
<dt><code>-cd</code><i>&nbsp;<wbr>dir</i></dt>
<dd> Run the debugger program from the working directory <i>dir</i>, instead of the current working directory. (See also the <code>cd</code> command.)</dd>
<dt><code>-emacs</code></dt>
<dd> Tell the debugger it is executed under Emacs. (See <i>The OCaml user&#8217;s manual</i> for information on how to run the debugger under Emacs.) Implies <code>-machine-readable</code>.</dd>
<dt><code>-I</code><i>&nbsp;<wbr>directory</i></dt>
<dd> Add <i>directory</i> to the list of directories searched for source files and compiled files. (See also the <code>directory</code> command.)</dd>
<dt><code>-machine-readable</code></dt>
<dd> Print information in a format more suitable for machines instead of human operators where applicable. For example, when describing a location in a program, such as when printing a backtrace, print the program counter and character offset in a file instead of the filename, line number, and character offset in that line.</dd>
<dt><code>-s</code><i>&nbsp;<wbr>socket</i></dt>
<dd> Use <i>socket</i> for communicating with the debugged program. See the description of the command <code>set socket</code> in <i>The OCaml user&#8217;s manual</i> for the format of <i>socket</i>.</dd>
<dt><code>-version</code></dt>
<dd> Print version string and exit.</dd>
<dt><code>-vnum</code></dt>
<dd> Print short version number and exit.</dd>
<dt><code>-help</code>&nbsp;<wbr>or<code>&nbsp;<wbr>&#8211;help</code></dt>
<dd> Display a short usage summary and exit.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1)<br />
 <i>The OCaml user&#8217;s manual</i>, chapter &quot;The debugger&quot;.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Sven LUTHER &lt;luther [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
