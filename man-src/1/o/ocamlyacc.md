---
title: "ocamlyacc(1)"
name: "ocamlyacc"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlyacc/"
description: "ocamlyacc – The OCaml parser generator"
---

<h2 class="name">NAME</h2>
<p> ocamlyacc &#8211; The OCaml parser generator</p>
<h2>SYNOPSIS</h2>
<p> <code>ocamlyacc</code> [ <code>-b</code><i>prefix</i> ] [ <code>-q</code> ] [ <code>-v</code> ] [ <code>-version</code> ] [ <code>-vnum</code> ] <i>filename.mly</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-ocamlyacc/">ocamlyacc</a></code>(1) command produces a parser from a <a href="/docs/linux/man/1-lalr/">LALR</a>(1) context-free grammar specification with attached semantic actions, in the style of <code><a href="/docs/linux/man/1-yacc/">yacc</a></code>(1). Assuming the input file is <i>grammar</i>.mly, running <code>ocamlyacc</code> produces OCaml code for a parser in the file <i>grammar</i>.ml, and its interface in file <i>grammar</i>.mli. </p>
<p> The generated module defines one parsing function per entry point in the grammar. These functions have the same names as the entry points. Parsing functions take as arguments a lexical analyzer (a function from lexer buffers to tokens) and a lexer buffer, and return the semantic attribute of the corresponding entry point. Lexical analyzer functions are usually generated from a lexer specification by the <code><a href="/docs/linux/man/1-ocamllex/">ocamllex</a></code>(1) program. Lexer buffers are an abstract data type implemented in the standard library module Lexing. Tokens are values from the concrete type token, defined in the interface file <i>grammar</i>.mli produced by <code><a href="/docs/linux/man/1-ocamlyacc/">ocamlyacc</a></code>(1). </p>
<h2>OPTIONS</h2>
<p> The <code><a href="/docs/linux/man/1-ocamlyacc/">ocamlyacc</a></code>(1) command recognizes the following options:</p>
<dl>
<dt><code>-b</code><i>prefix</i></p>
<dd> Name the output files <i>prefix</i>.ml, <i>prefix</i>.mli, <i>prefix</i>.output, instead of the default naming convention.</p>
<dt><code>-q</code></p>
<dd> This option has no effect.</p>
<dt><code>-v</code></p>
<dd> Generate a description of the parsing tables and a report on conflicts resulting from ambiguities in the grammar. The description is put in file <i>grammar</i>.output.</p>
<dt><code>-version</code></p>
<dd> Print version string and exit.</p>
<dt><code>-vnum</code></p>
<dd> Print short version number and exit.</p>
<dt><code>&#8211;</code></p>
<dd> Read the grammar specification from standard input. The default output file names are stdin.ml and stdin.mli.</p>
<dt><code>&#8212;</code><i>&nbsp;<wbr>file</i></p>
<dd> Process <i>file</i> as the grammar specification, even if its name starts with a dash (-) character. This option must be the last on the command line. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamllex/">ocamllex</a></code>(1).<br />
 <i>The OCaml user&#8217;s manual</i>, chapter &quot;Lexer and parser generators&quot;. </p>
<h2>Index</h2>
