---
title: "ocaml(1)"
name: "ocaml"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocaml/"
description: "ocaml – The OCaml interactive toplevel"
---

<h2 class="name">NAME</h2>
<p> ocaml &#8211; The OCaml interactive toplevel</p>
<h2>SYNOPSIS</h2>
<p> <code>ocaml</code> [ <i>options</i> ] [ <i>object-files</i> ] [ <i>script-file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-ocaml/">ocaml</a></code>(1) command is the toplevel system for OCaml, that permits interactive use of the OCaml system through a read-eval-print loop. In this mode, the system repeatedly reads OCaml phrases from the input, then typechecks, compiles and evaluates them, then prints the inferred type and result value, if any. The system prints a # (sharp) prompt before reading each phrase. </p>
<p> A toplevel phrase can span several lines. It is terminated by ;; (a double-semicolon). The syntax of toplevel phrases is as follows. </p>
<p> The toplevel system is started by the command <code><a href="/docs/linux/man/1-ocaml/">ocaml</a></code>(1). Phrases are read on standard input, results are printed on standard output, errors on standard error. End-of-file on standard input terminates <code><a href="/docs/linux/man/1-ocaml/">ocaml</a></code>(1). </p>
<p> If one or more <i>object-files</i> (ending in .cmo or .cma) are given, they are loaded silently before starting the toplevel. </p>
<p> If a <i>script-file</i> is given, phrases are read silently from the file, errors printed on standard error. <code><a href="/docs/linux/man/1-ocaml/">ocaml</a></code>(1) exits after the execution of the last phrase. </p>
<h2>OPTIONS</h2>
<p> The following command-line options are recognized by <code><a href="/docs/linux/man/1-ocaml/">ocaml</a></code>(1).</p>
<dl>
<dt><code>-absname</code></dt>
<dd> Show absolute filenames in error messages.</dd>
<dt><code>-I</code><i>&nbsp;<wbr>directory</i></dt>
<dd> Add the given directory to the list of directories searched for source and compiled files. By default, the current directory is searched first, then the standard library directory. Directories added with <code>-I</code> are searched after the current directory, in the order in which they were given on the command line, but before the standard library directory.</dd>
<dt>
</dt><dd> If the given directory starts with <code>+</code>, it is taken relative to the standard library directory. For instance, <code>-I&nbsp;<wbr>+labltk</code> adds the subdirectory <code>labltk</code> of the standard library to the search path.</dd>
<dt>
</dt><dd> Directories can also be added to the search path once the toplevel is running with the <code>#directory</code> directive.</dd>
<dt><code>-init</code><i>&nbsp;<wbr>file</i></dt>
<dd> Load the given file instead of the default initialization file. The default file is <code>.ocamlinit</code> in the current directory if it exists, otherwise <code>.ocamlinit</code> in the user&#8217;s home directory.</dd>
<dt><code>-labels</code></dt>
<dd> Labels are not ignored in types, labels may be used in applications, and labelled parameters can be given in any order. This is the default.</dd>
<dt><code>-no-app-funct</code></dt>
<dd> Deactivates the applicative behaviour of functors. With this option, each functor application generates new types in its result and applying the same functor twice to the same argument yields two incompatible structures.</dd>
<dt><code>-noassert</code></dt>
<dd> Do not compile assertion checks. Note that the special form <code>assert false</code> is always compiled because it is typed specially.</dd>
<dt><code>-nolabels</code></dt>
<dd> Ignore non-optional labels in types. Labels cannot be used in applications, and parameter order becomes strict.</dd>
<dt><code>-noprompt</code></dt>
<dd> Do not display any prompt when waiting for input.</dd>
<dt><code>-nopromptcont</code></dt>
<dd> Do not display the secondary prompt when waiting for continuation lines in multi-line inputs. This should be used e.g. when running <code><a href="/docs/linux/man/1-ocaml/">ocaml</a></code>(1) in an <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1) window.</dd>
<dt><code>-nostdlib</code></dt>
<dd> Do not include the standard library directory in the list of directories searched for source and compiled files.</dd>
<dt><code>-ppx</code><i>&nbsp;<wbr>command</i></dt>
<dd> After parsing, pipe the abstract syntax tree through the preprocessor <i>command</i>. The format of the input and ouput of the preprocessor are not yet documented.</dd>
<dt><code>-principal</code></dt>
<dd> Check information path during type-checking, to make sure that all types are derived in a principal way. When using labelled arguments and/or polymorphic methods, this flag is required to ensure future versions of the compiler will be able to infer types correctly, even if internal algorithms change. All programs accepted in <code>-principal</code> mode are also accepted in the default mode with equivalent types, but different binary signatures, and this may slow down type checking; yet it is a good idea to use it once before publishing source code.</dd>
<dt><code>-rectypes</code></dt>
<dd> Allow arbitrary recursive types during type-checking. By default, only recursive types where the recursion goes through an object type are supported.</dd>
<dt><code>-short-paths</code></dt>
<dd> When a type is visible under several module-paths, use the shortest one when printing the type&#8217;s name in inferred interfaces and error and warning messages.</dd>
<dt><code>-stdin</code></dt>
<dd> Read the standard input as a script file rather than starting an interactive session.</dd>
<dt><code>-strict-sequence</code></dt>
<dd> Force the left-hand part of each sequence to have type unit.</dd>
<dt><code>-unsafe</code></dt>
<dd> Turn bound checking off on array and string accesses (the <code>v.(i)</code>and<code>s.[i]</code> constructs). Programs compiled with <code>-unsafe</code> are therefore slightly faster, but unsafe: anything can happen if the program accesses an array or string outside of its bounds.</dd>
<dt><code>-version</code></dt>
<dd> Print version string and exit.</dd>
<dt><code>-vnum</code></dt>
<dd> Print short version number and exit.</dd>
<dt><code>-w</code><i>&nbsp;<wbr>warning-list</i></dt>
<dd> Enable or disable warnings according to the argument <i>warning-list</i>. See <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) for the syntax of the <i>warning-list</i> argument.</dd>
<dt><code>-warn-error</code><i>&nbsp;<wbr>warning-list</i></dt>
<dd> Mark as fatal the warnings described by the argument <i>warning-list</i>. Note that a warning is not triggered (and does not trigger an error) if it is disabled by the <code>-w</code> option. See <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) for the syntax of the <i>warning-list</i> argument.</dd>
<dt><code>-warn-help</code></dt>
<dd> Show the description of all available warning numbers.</dd>
<dt><code>&#8211;</code><i>&nbsp;<wbr>file</i></dt>
<dd> Use <i>file</i> as a script file name, even when it starts with a hyphen (-).</dd>
<dt><code>-help</code>&nbsp;<wbr>or<code>&nbsp;<wbr>&#8211;help</code></dt>
<dd> Display a short usage summary and exit. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>LC_CTYPE</code></dt>
<dd> If set to iso_8859_1, accented characters (from the ISO Latin-1 character set) in string and character literals are printed as is; otherwise, they are printed as decimal escape sequences.</dd>
<dt><code>TERM</code></dt>
<dd> When printing error messages, the toplevel system attempts to underline visually the location of the error. It consults the TERM variable to determines the type of output terminal and look up its capabilities in the terminal database. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1),<code>&nbsp;<wbr><a href="/docs/linux/man/1-ocamlopt/">ocamlopt</a></code>(1),<code>&nbsp;<wbr><a href="/docs/linux/man/1-ocamlrun/">ocamlrun</a></code>(1).<br />
 <i>The OCaml user&#8217;s manual</i>, chapter &quot;The toplevel system&quot;. </p>
