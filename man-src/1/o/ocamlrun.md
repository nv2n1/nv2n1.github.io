---
title: "ocamlrun(1)"
name: "ocamlrun"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlrun/"
description: "ocamlrun – The OCaml bytecode interpreter"
---

<h2>SYNOPSIS</h2>
<p> <code>ocamlrun</code> [ <i>options</i> ] <i>filename argument &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-ocamlrun/">ocamlrun</a></code>(1) command executes bytecode files produced by the linking phase of the <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) command. </p>
<p> The first non-option argument is taken to be the name of the file containing the executable bytecode. (That file is searched in the executable path as well as in the current directory.) The remaining arguments are passed to the OCaml program, in the string array <code>Sys.argv</code>. Element 0 of this array is the name of the bytecode executable file; elements 1 to <i>n</i> are the remaining arguments. </p>
<p> In most cases, the bytecode executable files produced by the <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) command are self-executable, and manage to launch the <code><a href="/docs/linux/man/1-ocamlrun/">ocamlrun</a></code>(1) command on themselves automatically. </p>
<h2>OPTIONS</h2>
<p> The following command-line options are recognized by <code><a href="/docs/linux/man/1-ocamlrun/">ocamlrun</a></code>(1).</p>
<dl>
<dt><code>-b</code></dt>
<dd> When the program aborts due to an uncaught exception, print a detailed &quot;back trace&quot; of the execution, showing where the exception was raised and which function calls were outstanding at this point. The back trace is printed only if the bytecode executable contains debugging information, i.e. was compiled and linked with the <code>-g</code> option to <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1) set. This option is equivalent to setting the <code>b</code> flag in the OCAMLRUNPARAM environment variable (see below).</dd>
<dt><code>-I</code><i>&nbsp;<wbr>dir</i></dt>
<dd> Search the directory <i>dir</i> for dynamically-loaded libraries, in addition to the standard search path.</dd>
<dt><code>-p</code></dt>
<dd> Print the names of the primitives known to this version of <code><a href="/docs/linux/man/1-ocamlrun/">ocamlrun</a></code>(1) and exit.</dd>
<dt><code>-v</code></dt>
<dd> Direct the memory manager to print verbose messages on standard error. This is equivalent to setting <code>v=63</code> in the OCAMLRUNPARAM environment variable (see below).</dd>
<dt><code>-version</code></dt>
<dd> Print version string and exit.</dd>
<dt><code>-vnum</code></dt>
<dd> Print short version number and exit. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variable are also consulted:</p>
<dl>
<dt><code>CAML_LD_LIBRARY_PATH</code></dt>
<dd> Additional directories to search for dynamically-loaded libraries.</dd>
<dt><code>OCAMLLIB</code></dt>
<dd> The directory containing the OCaml standard library. (If <code>OCAMLLIB</code> is not set, <code>CAMLLIB</code> will be used instead.) Used to locate the ld.conf configuration file for dynamic loading. If not set, default to the library directory specified when compiling OCaml.</dd>
<dt><code>OCAMLRUNPARAM</code></dt>
<dd> Set the runtime system options and garbage collection parameters. (If OCAMLRUNPARAM is not set, CAMLRUNPARAM will be used instead.) This variable must be a sequence of parameter specifications. A parameter specification is an option letter followed by an = sign, a decimal number (or a hexadecimal number prefixed by <code>0x</code>), and an optional multiplier. The options are documented below; the last six correspond to the fields of the <code>control</code> record documented in <i>The OCaml user&#8217;s manual,</i> chapter &quot;Standard Library&quot;, section &quot;Gc&quot;.</dd>
<dt><code>b</code></dt>
<dd> Trigger the printing of a stack backtrace when an uncaught exception aborts the program. This option takes no argument.</dd>
<dt><code>p</code></dt>
<dd> Turn on debugging support for <code>ocamlyacc</code>-generated parsers. When this option is on, the pushdown automaton that executes the parsers prints a trace of its actions. This option takes no argument.</dd>
<dt><code>R</code></dt>
<dd> Turn on randomization of all hash tables by default (see the <code>Hashtbl</code> module of the standard library). This option takes no argument.</dd>
<dt><code>h</code></dt>
<dd> The initial size of the major heap (in words).</dd>
<dt><code>a</code>&nbsp;<wbr>(allocation_policy)</dt>
<dd> The policy used for allocating in the OCaml heap. Possible values are 0 for the next-fit policy, and 1 for the first-fit policy. Next-fit is usually faster, but first-fit is better for avoiding fragmentation and the associated heap compactions.</dd>
<dt><code>s</code>&nbsp;<wbr>(minor_heap_size)</dt>
<dd> The size of the minor heap (in words).</dd>
<dt><code>i</code>&nbsp;<wbr>(major_heap_increment)</dt>
<dd> The default size increment for the major heap (in words).</dd>
<dt><code>o</code>&nbsp;<wbr>(space_overhead)</dt>
<dd> The major GC speed setting.</dd>
<dt><code>O</code>&nbsp;<wbr>(max_overhead)</dt>
<dd> The heap compaction trigger setting.</dd>
<dt><code>l</code>&nbsp;<wbr>(stack_limit)</dt>
<dd> The limit (in words) of the stack size.</dd>
<dt><code>v</code>&nbsp;<wbr>(verbose)</dt>
<dd> What GC messages to print to stderr. This is a sum of values selected from the following: </dd>
<p> <code>0x001</code> Start of major GC cycle. </p>
<p> <code>0x002</code> Minor collection and major GC slice. </p>
<p> <code>0x004</code> Growing and shrinking of the heap. </p>
<p> <code>0x008</code> Resizing of stacks and memory manager tables. </p>
<p> <code>0x010</code> Heap compaction. </p>
<p> <code>0x020</code> Change of GC parameters. </p>
<p> <code>0x040</code> Computation of major GC slice size. </p>
<p> <code>0x080</code> Calling of finalisation functions. </p>
<p> <code>0x100</code> Startup messages (loading the bytecode executable file, resolving shared libraries). </p>
<p> The multiplier is <code>k</code>, <code>M</code>, or <code>G</code>, for multiplication by 2^10, 2^20, and 2^30 respectively. For example, on a 32-bit machine under bash, the command <code>export OCAMLRUNPARAM=&#8217;s=256k,v=1&#8242;</code> tells a subsequent <code>ocamlrun</code> to set its initial minor heap size to 1 megabyte and to print a message at the start of each major GC cycle.</p>
<dt><code>CAMLRUNPARAM</code></dt>
<dd> If OCAMLRUNPARAM is not found in the environment, then CAMLRUNPARAM will be used instead. If CAMLRUNPARAM is not found, then the default values will be used.</dd>
<dt><code>PATH</code></dt>
<dd> List of directories searched to find the bytecode executable file. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamlc/">ocamlc</a></code>(1).<br />
 <i>The OCaml user&#8217;s manual</i>, chapter &quot;Runtime system&quot;. </p>
