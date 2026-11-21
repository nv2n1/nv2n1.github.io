---
title: "ecl(1)"
name: "ecl"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecl/"
description: "ecl – Embeddable Common LISP"
---

<h2>SYNOPSIS</h2>
<p> <code>ecl</code> [<code>-dir</code> <i>dir</i>] [<code>-load</code> <i>file</i>] [<code>-eval</code> <i>expr</i>]<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code>-compile</code> <i>file</i><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [<code>-o</code> <i>ofile</i>] [<code>-c</code> [<i>cfile</i>]] [<code>-h</code> [<i>hfile</i>]] [<code>-data</code> [<i>datafile</i>]] [<code>-s</code>] [<code>-q</code>]] </p>
<h2>DESCRIPTION</h2>
<p> ECL stands for Embeddable Common-Lisp. The ECL project is an effort to modernize Giuseppe Attardi&#8217;s ECL environment to produce an implementation of the Common-Lisp language which complies to the ANSI X3J13 definition of the language. </p>
<p> The current ECL implementation features:</p>
<dl>
<dt>*</dt>
<dd> A bytecodes compiler and interpreter.</dd>
<dt>*</dt>
<dd> A translator to C.</dd>
<dt>*</dt>
<dd> An interface to foreign functions.</dd>
<dt>*</dt>
<dd> A dynamic loader.</dd>
<dt>*</dt>
<dd> The possibility to build standalone executables.</dd>
<dt>*</dt>
<dd> The Common-Lisp Object System (CLOS).</dd>
<dt>*</dt>
<dd> Conditions and restarts for handling errors.</dd>
<dt>*</dt>
<dd> Sockets as ordinary streams.</dd>
<dt>*</dt>
<dd> The Gnu Multiprecision library for fast bignum operations.</dd>
<dt>*</dt>
<dd> A simple conservative mark &amp; sweep garbage collector.</dd>
<dt>*</dt>
<dd> The Boehm-Weiser garbage collector. </dd>
</dl>
<p> <code>ecl</code> without any argument gives you the interactive lisp.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-shell</code><i> file</i></dt>
<dd> Executes the given file and exits, without providing a read-eval-print loop. If you want to use lisp as a scripting language, you can write <code>#!/usr/bin/ecl -shell</code> on the first line of the file to be executed, and then ECL will be automatically invoked.</dd>
<dt><code>-norc</code></dt>
<dd> Do not try to load the file <i>~/.eclrc</i> at startup.</dd>
<dt><code>-dir</code></dt>
<dd> Use <i>dir</i> as system directory.</dd>
<dt><code>-load</code><i> file</i></dt>
<dd> Loads <i>file</i> before entering the read-eval-print loop.</dd>
<dt><code>-eval</code><i> expr</i></dt>
<dd> Evaluates <i>expr</i> before entering the read-eval-print loop.</dd>
<dt><code>-compile</code><i> file</i></dt>
<dd> Translates <i>file</i> to C and invokes the local C compiler to produce a shared library with .fas as extension per default.</dd>
<dt><code>-o</code><i> ofile</i></dt>
<dd> When compiling <i>file</i> name the resulting shared library <i>ofile</i>.</dd>
<dt><code>-c</code><i> cfile</i></dt>
<dd> When compiling name the intermediary C file <i>cfile</i> and do not delete it afterwards.</dd>
<dt><code>-h</code><i> hfile</i></dt>
<dd> When compiling name the intermediary C header <i>hfile</i> and do not delete it afterwards.</dd>
<dt><code>-data</code><i> [datafile]</i></dt>
<dd> Dumps compiler data into <i>datafile</i> or, if not supplied, into a file named after the source file, but with .data as extension.</dd>
<dt><code>-s</code></dt>
<dd> Produce a linkable object file. It cannot be loaded with load, but it can be used to build libraries or standalone executable programs.</dd>
<dt><code>-q</code></dt>
<dd> Produce less notes when compiling. </dd>
</dl>
<p> The options <code>-load,</code> <code>-shell,</code> and <code>-eval</code> may appear any number of times, and they are combined and processed from left to right.</p>
<h2>AUTHORS</h2>
<p> The original version was developed by Giuseppe Attardi starting from the Kyoto Common Lisp implementation by Taiichi Yuasa and Masami Hagiya. The current maintainer of ECL is Juan Jose Garcia Ripoll, who can be reached at the ECL mailing list.</p>
<h2>FILES</h2>
<dl>
<dt><code>~/.ecl, ~/.eclrc</code></dt>
<dd> Default initialization files loaded at startup unless the option <code>-norc</code> is provided. (if they exist).</dd></dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
</dt><dd> ANSI Common Lisp standard X3.226-1994</dd>
<dt>
</dt><dd> The Common Lisp HyperSpec</dd></dl>
<h2>BUGS</h2>
<p> Probably some. Report them! </p>
