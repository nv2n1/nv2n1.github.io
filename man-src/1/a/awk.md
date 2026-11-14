---
title: "awk(1)"
name: "awk"
section: "1"
letter: "a"
url: "/docs/linux/man/1-awk/"
description: "gawk – pattern scanning and processing language"
---

<h2 class="name">NAME</h2>
<p> gawk &#8211; pattern scanning and processing language </p>
<h2>SYNOPSIS</h2>
<p> <code>gawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] <code>-f</code> <i>program-file</i> [ <code>&#8212;</code> ] file &#8230;<br />
 <code>gawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] [ <code>&#8212;</code> ] <i>program-text</i> file &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>Gawk</i> is the <font SIZE="-1">GNU</font> Project&#8217;s implementation of the <font SIZE="-1">AWK</font> programming language. It conforms to the definition of the language in the <font SIZE="-1">POSIX</font> 1003.1 standard. This version in turn is based on the description in <i>The AWK Programming Language</i>, by Aho, Kernighan, and Weinberger. <i>Gawk</i> provides the additional features found in the current version of Brian Kernighan&#8217;s <i>awk</i> and numerous <font SIZE="-1">GNU</font>-specific extensions. </p>
<p> The command line consists of options to <i>gawk</i> itself, the <font SIZE="-1">AWK</font> program text (if not supplied via the <code>-f</code> or <code>&#8211;include</code> options), and values to be made available in the <code>ARGC</code> and <code>ARGV</code> pre-defined <font SIZE="-1">AWK</font> variables. </p>
<p> When <i>gawk</i> is invoked with the <code>&#8211;profile</code> option, it starts gathering profiling statistics from the execution of the program. <i>Gawk</i> runs more slowly in this mode, and automatically produces an execution profile in the file <code>awkprof.out</code> when done. See the <code>&#8211;profile</code> option, below. </p>
<p> <i>Gawk</i> also has an integrated debugger. An interactive debugging session can be started by supplying the <code>&#8211;debug</code> option to the command line. In this mode of execution, <i>gawk</i> loads the AWK source code and then prompts for debugging commands. <i>Gawk</i> can only debug AWK program source provided with the <code>-f</code> and <code>&#8211;include</code> options. The debugger is documented in <i>GAWK: Effective AWK Programming</i>.</p>
<h2>OPTION FORMAT</h2>
<p> <i>Gawk</i> options may be either traditional <font SIZE="-1">POSIX</font>-style one letter options, or <font SIZE="-1">GNU</font>-style long options. <font SIZE="-1">POSIX</font> options start with a single &#8220;-&#8221;, while long options start with &#8220;&#8211;&#8221;. Long options are provided for both <font SIZE="-1">GNU</font>-specific features and for <font SIZE="-1">POSIX</font>-mandated features. </p>
<p> <i>Gawk</i>-specific options are typically used in long-option form. Arguments to long options are either joined with the option by an <code>=</code> sign, with no intervening spaces, or they may be provided in the next command line argument. Long options may be abbreviated, as long as the abbreviation remains unique. </p>
<p> Additionally, every long option has a corresponding short option, so that the option&#8217;s functionality may be used from within <code>#!</code> executable scripts.</p>
<h2>OPTIONS</h2>
<p> <i>Gawk</i> accepts the following options. Standard options are listed first, followed by options for <i>gawk</i> extensions, listed alphabetically by short option.</p>
<dl>
<dt><code>-f</code><i> program-file</i></p>
<dd>
<dt><code>&#8211;file</code><i> program-file</i></p>
<dd> Read the <font SIZE="-1">AWK</font> program source from the file <i>program-file</i>, instead of from the first command line argument. Multiple <code>-f</code> (or <code>&#8211;file</code>) options may be used. Files read with <code>-f</code> are treated as if they begin with an implicit <code>@namespace &quot;awk&quot;</code> statement.</p>
<dt><code>-F</code><i> fs</i></p>
<dd>
<dt><code>&#8211;field-separator</code><i> fs</i></p>
<dd> Use <i>fs</i> for the input field separator (the value of the <code>FS</code> predefined variable).</p>
<dt>
<dd> <code>-v</code><i> var</i><code>=</code><i>val</i></p>
<dt>
<dd> <code>&#8211;assign </code><i>var</i><code>=</code><i>val</i> Assign the value <i>val</i> to the variable <i>var</i>, before execution of the program begins. Such variable values are available to the <code>BEGIN</code> rule of an <font SIZE="-1">AWK</font> program.</p>
<dt><code>-b</code></p>
<dd>
<dt><code>&#8211;characters-as-bytes</code></p>
<dd> Treat all input data as single-byte characters. In other words, don&#8217;t pay any attention to the locale information when attempting to process strings as multibyte characters. The <code>&#8211;posix</code> option overrides this one.</p>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;traditional</code></p>
<dd> Run in <i>compatibility</i> mode. In compatibility mode, <i>gawk</i> behaves identically to Brian Kernighan&#8217;s <i>awk</i>; none of the <font SIZE="-1">GNU</font>-specific extensions are recognized. See <code>GNU EXTENSIONS</code>, below, for more information.</p>
<dt><code>-C</code></p>
<dd>
<dt><code>&#8211;copyright</code></p>
<dd> Print the short version of the <font SIZE="-1">GNU</font> copyright information message on the standard output and exit successfully.</p>
<dt>
<dd> <code>-d</code>[<i>file</i>]</p>
<dt>
<dd> <code>&#8211;dump-variables</code>[<code>=</code><i>file</i>] Print a sorted list of global variables, their types and final values to <i>file</i>. If no <i>file</i> is provided, <i>gawk</i> uses a file named <code>awkvars.out</code> in the current directory. </p>
<p> Having a list of all the global variables is a good way to look for typographical errors in your programs. You would also use this option if you have a large program with a lot of functions, and you want to be sure that your functions don&#8217;t inadvertently use global variables that you meant to be local. (This is a particularly easy mistake to make with simple variable names like <code>i</code>, <code>j</code>, and so on.)</p>
<dt>
<dd> <code>-D</code>[<i>file</i>]</p>
<dt>
<dd> <code>&#8211;debug</code>[<code>=</code><i>file</i>] Enable debugging of <font SIZE="-1">AWK</font> programs. By default, the debugger reads commands interactively from the keyboard (standard input). The optional <i>file</i> argument specifies a file with a list of commands for the debugger to execute non-interactively.</p>
<dt><code>-e </code><i>program-text</i></p>
<dd>
<dt><code>&#8211;source</code><i> program-text</i></p>
<dd> Use <i>program-text</i> as <font SIZE="-1">AWK</font> program source code. This option allows the easy intermixing of library functions (used via the <code>-f</code> and <code>&#8211;include</code> options) with source code entered on the command line. It is intended primarily for medium to large <font SIZE="-1">AWK</font> programs used in shell scripts. Each argument supplied via <code>-e</code> is treated as if it begins with an implicit <code>@namespace &quot;awk&quot;</code> statement.</p>
<dt><code>-E </code><i>file</i></p>
<dd>
<dt><code>&#8211;exec</code><i> file</i></p>
<dd> Similar to <code>-f</code>, however, this is option is the last one processed. This should be used with <code>#!</code> scripts, particularly for CGI applications, to avoid passing in options or source code (!) on the command line from a URL. This option disables command-line variable assignments.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;gen-pot</code></p>
<dd> Scan and parse the <font SIZE="-1">AWK</font> program, and generate a <font SIZE="-1">GNU</font> <code>.pot</code> (Portable Object Template) format file on standard output with entries for all localizable strings in the program. The program itself is not executed. See the <font SIZE="-1">GNU</font> <i>gettext</i> distribution for more information on <code>.pot</code> files.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Print a relatively short summary of the available options on the standard output. (Per the <i>GNU Coding Standards</i>, these options cause an immediate, successful exit.)</p>
<dt><code>-i </code><i>include-file</i></p>
<dd>
<dt><code>&#8211;include</code><i> include-file</i></p>
<dd> Load an awk source library. This searches for the library using the <code>AWKPATH</code> environment variable. If the initial search fails, another attempt will be made after appending the <code>.awk</code> suffix. The file will be loaded only once (i.e., duplicates are eliminated), and the code does not constitute the main program source. Files read with <code>&#8211;include</code> are treated as if they begin with an implicit <code>@namespace &quot;awk&quot;</code> statement.</p>
<dt><code>-l </code><i>lib</i></p>
<dd>
<dt><code>&#8211;load</code><i> lib</i></p>
<dd> Load a <i>gawk</i> extension from the shared library <i>lib</i>. This searches for the library using the <code>AWKLIBPATH</code> environment variable. If the initial search fails, another attempt will be made after appending the default shared library suffix for the platform. The library initialization routine is expected to be named <code>dl_load()</code>.</p>
<dt><code>-L </code>[<i>value</i>]</p>
<dd>
<dt><code>&#8211;lint</code>[<code>=</code><i>value</i>]</p>
<dd> Provide warnings about constructs that are dubious or non-portable to other <font SIZE="-1">AWK</font> implementations. With an optional argument of <code>fatal</code>, lint warnings become fatal errors. This may be drastic, but its use will certainly encourage the development of cleaner <font SIZE="-1">AWK</font> programs. With an optional argument of <code>invalid</code>, only warnings about things that are actually invalid are issued. (This is not fully implemented yet.) With an optional argument of <code>no-ext</code>, warnings about <i>gawk</i> extensions are disabled.</p>
<dt><code>-M</code></p>
<dd>
<dt><code>&#8211;bignum</code></p>
<dd> Force arbitrary precision arithmetic on numbers. This option has no effect if <i>gawk</i> is not compiled to use the GNU MPFR and GMP libraries. (In such a case, <i>gawk</i> issues a warning.)</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;non-decimal-data</code></p>
<dd> Recognize octal and hexadecimal values in input data. <i>Use this option with great caution!</i></p>
<dt><code>-N</code></p>
<dd>
<dt><code>&#8211;use-lc-numeric</code></p>
<dd> Force <i>gawk</i> to use the locale&#8217;s decimal point character when parsing input data. Although the POSIX standard requires this behavior, and <i>gawk</i> does so when <code>&#8211;posix</code> is in effect, the default is to follow traditional behavior and use a period as the decimal point, even in locales where the period is not the decimal point character. This option overrides the default behavior, without the full draconian strictness of the <code>&#8211;posix</code> option.</p>
<dt>
<dd> <code>-o</code>[<i>file</i>]</p>
<dt>
<dd> <code>&#8211;pretty-print</code>[<code>=</code><i>file</i>] Output a pretty printed version of the program to <i>file</i>. If no <i>file</i> is provided, <i>gawk</i> uses a file named <code>awkprof.out</code> in the current directory. This option implies <code>&#8211;no-optimize</code>.</p>
<dt><code>-O</code></p>
<dd>
<dt><code>&#8211;optimize</code></p>
<dd> Enable <i>gawk</i>&#8216;s default optimizations upon the internal representation of the program. Currently, this just includes simple constant folding. This option is on by default.</p>
<dt>
<dd> <code>-p</code>[<i>prof-file</i>]</p>
<dt>
<dd> <code>&#8211;profile</code>[<code>=</code><i>prof-file</i>] Start a profiling session, and send the profiling data to <i>prof-file</i>. The default is <code>awkprof.out</code>. The profile contains execution counts of each statement in the program in the left margin and function call counts for each user-defined function. This option implies <code>&#8211;no-optimize</code>.</p>
<dt><code>-P</code></p>
<dd>
<dt><code>&#8211;posix</code></p>
<dd> This turns on <i>compatibility</i> mode, with the following additional restrictions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>
