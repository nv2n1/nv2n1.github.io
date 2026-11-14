---
title: "dgawk(1)"
name: "dgawk"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dgawk/"
description: "gawk – pattern scanning and processing language"
---

<h2>NAME</h2>
<p> gawk &#8211; pattern scanning and processing language</p>
<h2>SYNOPSIS</h2>
<p> <code>gawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] <code>-f</code> <i>program-file</i> [ <code>&#8212;</code> ] file &#8230;<br />
 <code>gawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] [ <code>&#8212;</code> ] <i>program-text</i> file &#8230; </p>
<p> <code>pgawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] <code>-f</code> <i>program-file</i> [ <code>&#8212;</code> ] file &#8230;<br />
 <code>pgawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] [ <code>&#8212;</code> ] <i>program-text</i> file &#8230; </p>
<p> <code>dgawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] <code>-f</code> <i>program-file</i> [ <code>&#8212;</code> ] file &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>Gawk</i> is the <font SIZE="-1">GNU</font> Project&#8217;s implementation of the <font SIZE="-1">AWK</font> programming language. It conforms to the definition of the language in the <font SIZE="-1">POSIX</font> 1003.1 Standard. This version in turn is based on the description in <i>The AWK Programming Language</i>, by Aho, Kernighan, and Weinberger. <i>Gawk</i> provides the additional features found in the current version of <font SIZE="-1">UNIX</font> <i>awk</i> and a number of <font SIZE="-1">GNU</font>-specific extensions. </p>
<p> The command line consists of options to <i>gawk</i> itself, the <font SIZE="-1">AWK</font> program text (if not supplied via the <code>-f</code> or <code>&#8211;file</code> options), and values to be made available in the <code>ARGC</code> and <code>ARGV</code> pre-defined <font SIZE="-1">AWK</font> variables. </p>
<p> <i>Pgawk</i> is the profiling version of <i>gawk</i>. It is identical in every way to <i>gawk</i>, except that programs run more slowly, and it automatically produces an execution profile in the file <code>awkprof.out</code> when done. See the <code>&#8211;profile</code> option, below. </p>
<p> <i>Dgawk</i> is an <i>awk</i> debugger. Instead of running the program directly, it loads the AWK source code and then prompts for debugging commands. Unlike <i>gawk</i> and <i>pgawk</i>, <i>dgawk</i> only processes AWK program source provided with the <code>-f</code> option. The debugger is documented in <i>GAWK: Effective AWK Programming</i>.</p>
<h2>OPTION FORMAT</h2>
<p> <i>Gawk</i> options may be either traditional <font SIZE="-1">POSIX</font>-style one letter options, or <font SIZE="-1">GNU</font>-style long options. <font SIZE="-1">POSIX</font> options start with a single &#8220;-&#8221;, while long options start with &#8220;&#8211;&#8221;. Long options are provided for both <font SIZE="-1">GNU</font>-specific features and for <font SIZE="-1">POSIX</font>-mandated features. </p>
<p> <i>Gawk</i>&#8211; specific options are typically used in long-option form. Arguments to long options are either joined with the option by an <code>=</code> sign, with no intervening spaces, or they may be provided in the next command line argument. Long options may be abbreviated, as long as the abbreviation remains unique. </p>
<p> Additionally, each long option has a corresponding short option, so that the option&#8217;s functionality may be used from within <code>#!</code> executable scripts.</p>
<h2>OPTIONS</h2>
<p> <i>Gawk</i> accepts the following options. Standard options are listed first, followed by options for <i>gawk</i> extensions, listed alphabetically by short option.</p>
<dl>
<dt>
<dd> <code>-f</code><i> program-file</i></p>
<dt>
<dd> <code>&#8211;file</code><i> program-file</i> Read the <font SIZE="-1">AWK</font> program source from the file <i>program-file</i>, instead of from the first command line argument. Multiple <code>-f</code> (or <code>&#8211;file</code>) options may be used.</p>
<dt>
<dd> <code>-F</code><i> fs</i></p>
<dt>
<dd> <code>&#8211;field-separator</code><i> fs</i> Use <i>fs</i> for the input field separator (the value of the <code>FS</code> predefined variable).</p>
<dt>
<dd> <code>-v</code><i> var</i><code>=</code><i>val</i></p>
<dt>
<dd> <code>&#8211;assign </code><i>var</i><code>=</code><i>val</i> Assign the value <i>val</i> to the variable <i>var</i>, before execution of the program begins. Such variable values are available to the <code>BEGIN</code> block of an <font SIZE="-1">AWK</font> program.</p>
<dt>
<dd> <code>-b</code></p>
<dt>
<dd> <code>&#8211;characters-as-bytes</code> Treat all input data as single-byte characters. In other words, don&#8217;t pay any attention to the locale information when attempting to process strings as multibyte characters. The <code>&#8211;posix</code> option overrides this one.</p>
<dt>
<dd> <code>-c</code></p>
<dt>
<dd> <code>&#8211;traditional</code> Run in <i>compatibility</i> mode. In compatibility mode, <i>gawk</i> behaves identically to <font SIZE="-1">UNIX</font> <i>awk</i>; none of the <font SIZE="-1">GNU</font>-specific extensions are recognized. See <code>GNU EXTENSIONS</code>, below, for more information.</p>
<dt>
<dd> <code>-C</code></p>
<dt>
<dd> <code>&#8211;copyright</code> Print the short version of the <font SIZE="-1">GNU</font> copyright information message on the standard output and exit successfully.</p>
<dt>
<dd> <code>-d</code>[<i>file</i>]</p>
<dt>
<dd> <code>&#8211;dump-variables</code>[<code>=</code><i>file</i>] Print a sorted list of global variables, their types and final values to <i>file</i>. If no <i>file</i> is provided, <i>gawk</i> uses a file named <code>awkvars.out</code> in the current directory. </p>
<p> Having a list of all the global variables is a good way to look for typographical errors in your programs. You would also use this option if you have a large program with a lot of functions, and you want to be sure that your functions don&#8217;t inadvertently use global variables that you meant to be local. (This is a particularly easy mistake to make with simple variable names like <code>i</code>, <code>j</code>, and so on.)</p>
<dt>
<dd> <code>-e </code><i>program-text</i></p>
<dt>
<dd> <code>&#8211;source</code><i> program-text</i> Use <i>program-text</i> as <font SIZE="-1">AWK</font> program source code. This option allows the easy intermixing of library functions (used via the <code>-f</code> and <code>&#8211;file</code> options) with source code entered on the command line. It is intended primarily for medium to large <font SIZE="-1">AWK</font> programs used in shell scripts.</p>
<dt>
<dd> <code>-E </code><i>file</i></p>
<dt>
<dd> <code>&#8211;exec</code><i> file</i> Similar to <code>-f</code>, however, this is option is the last one processed. This should be used with <code>#!</code> scripts, particularly for CGI applications, to avoid passing in options or source code (!) on the command line from a URL. This option disables command-line variable assignments.</p>
<dt>
<dd> <code>-g</code></p>
<dt>
<dd> <code>&#8211;gen-pot</code> Scan and parse the <font SIZE="-1">AWK</font> program, and generate a <font SIZE="-1">GNU</font> <code>.pot</code> (Portable Object Template) format file on standard output with entries for all localizable strings in the program. The program itself is not executed. See the <font SIZE="-1">GNU</font> <i>gettext</i> distribution for more information on <code>.pot</code> files.</p>
<dt>
<dd> <code>-h</code></p>
<dt>
<dd> <code>&#8211;help</code> Print a relatively short summary of the available options on the standard output. (Per the <i>GNU Coding Standards</i>, these options cause an immediate, successful exit.)</p>
<dt>
<dd> <code>-L </code>[<i>value</i>]</p>
<dt>
<dd> <code>&#8211;lint</code>[<code>=</code><i>value</i>] Provide warnings about constructs that are dubious or non-portable to other <font SIZE="-1">AWK</font> implementations. With an optional argument of <code>fatal</code>, lint warnings become fatal errors. This may be drastic, but its use will certainly encourage the development of cleaner <font SIZE="-1">AWK</font> programs. With an optional argument of <code>invalid</code>, only warnings about things that are actually invalid are issued. (This is not fully implemented yet.)</p>
<dt>
<dd> <code>-n</code></p>
<dt>
<dd> <code>&#8211;non-decimal-data</code> Recognize octal and hexadecimal values in input data. <i>Use this option with great caution!</i></p>
<dt>
<dd> <code>-N</code></p>
<dt>
<dd> <code>&#8211;use-lc-numeric</code> This forces <i>gawk</i> to use the locale&#8217;s decimal point character when parsing input data. Although the POSIX standard requires this behavior, and <i>gawk</i> does so when <code>&#8211;posix</code> is in effect, the default is to follow traditional behavior and use a period as the decimal point, even in locales where the period is not the decimal point character. This option overrides the default behavior, without the full draconian strictness of the <code>&#8211;posix</code> option.</p>
<dt>
<dd> <code>-O</code></p>
<dt>
<dd> <code>&#8211;optimize</code> Enable optimizations upon the internal representation of the program. Currently, this includes just simple constant-folding. The <i>gawk</i> maintainer hopes to add additional optimizations over time.</p>
<dt>
<dd> <code>-p</code>[<i>prof_file</i>]</p>
<dt>
<dd> <code>&#8211;profile</code>[<code>=</code><i>prof_file</i>] Send profiling data to <i>prof_file</i>. The default is <code>awkprof.out</code>. When run with <i>gawk</i>, the profile is just a &#8220;pretty printed&#8221; version of the program. When run with <i>pgawk</i>, the profile contains execution counts of each statement in the program in the left margin and function call counts for each user-defined function.</p>
<dt>
<dd> <code>-P</code></p>
<dt>
<dd> <code>&#8211;posix</code> This turns on <i>compatibility</i> mode, with the following additional restrictions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <code>
