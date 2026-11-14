---
title: "ocamlcp(1)"
name: "ocamlcp"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlcp/"
description: "ocamlcp, ocamloptp – The OCaml profiling compilers"
---

<h2 class="name">NAME</h2>
<p> ocamlcp, ocamloptp &#8211; The OCaml profiling compilers</p>
<h2>SYNOPSIS</h2>
<p> <code>ocamlcp</code> [ <i>ocamlc options</i> ] [ <code>-P</code><i>&nbsp;<wbr>flags</i> ] <i>filename &#8230;</i> </p>
<p> <code>ocamloptp</code> [ <i>ocamlopt options</i> ] [ <code>-P</code><i>&nbsp;<wbr>flags</i> ] <i>filename &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>ocamlcp</code> and <code>ocamloptp</code> commands are front-ends to <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) and <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) that instrument the source code, adding code to record how many times functions are called, branches of conditionals are taken, etc. Execution of instrumented code produces an execution profile in the file ocamlprof.dump, which can be read using <code><a href="/docs/linux/man/1-ocamlprof/">ocamlprof</a></code>(1). </p>
<p> <code>ocamlcp</code> accepts the same arguments and options as <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) and <code>ocamloptp</code> accepts the same arguments and options as <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1). There is only one exception: in both cases, the <code>-pp</code> option is not supported. If you need to preprocess your source files, you will have to do it separately before calling <code>ocamlcp</code> or <code>ocamloptp</code>. </p>
<h2>OPTIONS</h2>
<p> In addition to the <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) or <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1) options, <code>ocamlcp</code> and <code>ocamloptp</code> accept one option to control the kind of profiling information, the <code>-P</code><i>&nbsp;<wbr>letters</i> option. The <i>letters</i> indicate which parts of the program should be profiled:</p>
<dl>
<dt><code>a</code></p>
<dd> all options</p>
<dt><code>f</code></p>
<dd> function calls : a count point is set at the beginning of each function body</p>
<dt><code>i</code></p>
<dd> <code>if</code>&nbsp;<wbr>&#8230;<code>&nbsp;<wbr>then</code>&nbsp;<wbr>&#8230;<code>&nbsp;<wbr>else</code>: count points are set in both <code>then</code>&nbsp;<wbr>and<code>&nbsp;<wbr>else</code> branches</p>
<dt><code>l</code></p>
<dd> <code>while</code>,<code>&nbsp;<wbr>for</code> loops: a count point is set at the beginning of the loop body</p>
<dt><code>m</code></p>
<dd> <code>match</code> branches: a count point is set at the beginning of the body of each branch of a pattern-matching</p>
<dt><code>t</code></p>
<dd> <code>try</code>&nbsp;<wbr>&#8230;<code>&nbsp;<wbr>with</code> branches: a count point is set at the beginning of the body of each branch of an exception catcher </p>
</dl>
<p> For instance, compiling with <code>ocamlcp -P film</code> profiles function calls, <code>if</code>&nbsp;<wbr>&#8230;<code>&nbsp;<wbr>then</code>&nbsp;<wbr>&#8230;<code>&nbsp;<wbr>else</code>&nbsp;<wbr>&#8230;, loops, and pattern matching. </p>
<p> Calling <code><a href="/docs/linux/man/1-ocamlcp/">ocamlcp</a></code>(1) or <code><a href="/docs/linux/man/1-ocamloptp/">ocamloptp</a></code>(1) without the <code>-P</code> option defaults to <code>-P fm</code>, meaning that only function calls and pattern matching are profiled. </p>
<p> Note: for compatibility with previous versions, <code><a href="/docs/linux/man/1-ocamlcp/">ocamlcp</a></code>(1) also accepts the option <code>-p</code> with the same argument and meaning as <code>-P</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1), <code><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1), <code><a href="/docs/linux/man/1-ocamlprof/">ocamlprof</a></code>(1).<br />
 <i>The OCaml user&#8217;s manual</i>, chapter &quot;Profiling&quot;. </p>
<h2>Index</h2>
