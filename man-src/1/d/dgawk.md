---
title: "dgawk(1)"
name: "dgawk"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dgawk/"
description: "gawk – pattern scanning and processing language"
---
<h2>NAME</h2>
<p> gawk - pattern scanning and processing language  </p>
<h2>SYNOPSIS</h2>
<p> <code>gawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] <code>-f</code> <i>program-file</i> [ <code>--</code> ] file ... <br />
 <code>gawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] [ <code>--</code> ] <i>program-text</i> file ... </p>
<p> <code>pgawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] <code>-f</code> <i>program-file</i> [ <code>--</code> ] file ... <br />
 <code>pgawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] [ <code>--</code> ] <i>program-text</i> file ... </p>
<p> <code>dgawk</code> [ <font SIZE="-1">POSIX</font> or <font SIZE="-1">GNU</font> style options ] <code>-f</code> <i>program-file</i> [ <code>--</code> ] file ...  </p>
<h2>DESCRIPTION</h2>
<p> <i>Gawk</i> is the <font SIZE="-1">GNU</font> Project&#8217;s implementation of the <font SIZE="-1">AWK</font> programming language. It conforms to the definition of the language in the <font SIZE="-1">POSIX</font> 1003.1 Standard. This version in turn is based on the description in <i>The AWK Programming Language</i>, by Aho, Kernighan, and Weinberger. <i>Gawk</i> provides the additional features found in the current version of <font SIZE="-1">UNIX</font> <i>awk</i> and a number of <font SIZE="-1">GNU</font>-specific extensions. </p>
<p> The command line consists of options to <i>gawk</i> itself, the <font SIZE="-1">AWK</font> program text (if not supplied via the <code>-f</code> or <code>--file</code> options), and values to be made available in the <code>ARGC</code> and <code>ARGV</code> pre-defined <font SIZE="-1">AWK</font> variables. </p>
<p> <i>Pgawk</i> is the profiling version of <i>gawk</i>. It is identical in every way to <i>gawk</i>, except that programs run more slowly, and it automatically produces an execution profile in the file <code>awkprof.out</code> when done. See the <code>--profile</code> option, below. </p>
<p> <i>Dgawk</i> is an <i>awk</i> debugger. Instead of running the program directly, it loads the AWK source code and then prompts for debugging commands. Unlike <i>gawk</i> and <i>pgawk</i>, <i>dgawk</i> only processes AWK program source provided with the <code>-f</code> option. The debugger is documented in <i>GAWK: Effective AWK Programming</i>.  </p>
<h2>OPTION FORMAT</h2>
<p> <i>Gawk</i> options may be either traditional <font SIZE="-1">POSIX</font>-style one letter options, or <font SIZE="-1">GNU</font>-style long options. <font SIZE="-1">POSIX</font> options start with a single ``-&#8216;&#8216;, while long options start with ``--&#8216;&#8216;. Long options are provided for both <font SIZE="-1">GNU</font>-specific features and for <font SIZE="-1">POSIX</font>-mandated features. </p>
<p> <i>Gawk</i>- specific options are typically used in long-option form. Arguments to long options are either joined with the option by an <code>=</code> sign, with no intervening spaces, or they may be provided in the next command line argument. Long options may be abbreviated, as long as the abbreviation remains unique. </p>
<p> Additionally, each long option has a corresponding short option, so that the option&#8217;s functionality may be used from within <code>#!</code> executable scripts.  </p>
<h2>OPTIONS</h2>
<p> <i>Gawk</i> accepts the following options. Standard options are listed first, followed by options for <i>gawk</i> extensions, listed alphabetically by short option. </p>
<dl>
<dd> <p> <code>-f</code><i> program-file</i> </p>
 </dd>
<dd> <p> <code>--file</code><i> program-file</i> Read the <font SIZE="-1">AWK</font> program source from the file <i>program-file</i>, instead of from the first command line argument. Multiple <code>-f</code> (or <code>--file</code>) options may be used. </p>
 </dd>
<dd> <p> <code>-F</code><i> fs</i> </p>
 </dd>
<dd> <p> <code>--field-separator</code><i> fs</i> Use <i>fs</i> for the input field separator (the value of the <code>FS</code> predefined variable). </p>
 </dd>
<dd> <p> <code>-v</code><i> var</i><code>=</code><i>val</i> </p>
 </dd>
<dd> <p> <code>--assign </code><i>var</i><code>=</code><i>val</i> Assign the value <i>val</i> to the variable <i>var</i>, before execution of the program begins. Such variable values are available to the <code>BEGIN</code> block of an <font SIZE="-1">AWK</font> program. </p>
 </dd>
<dd> <p> <code>-b</code> </p>
 </dd>
<dd> <p> <code>--characters-as-bytes</code> Treat all input data as single-byte characters. In other words, don&#8217;t pay any attention to the locale information when attempting to process strings as multibyte characters. The <code>--posix</code> option overrides this one. </p>
 </dd>
<dd> <p> <code>-c</code> </p>
 </dd>
<dd> <p> <code>--traditional</code> Run in <i>compatibility</i> mode. In compatibility mode, <i>gawk</i> behaves identically to <font SIZE="-1">UNIX</font> <i>awk</i>; none of the <font SIZE="-1">GNU</font>-specific extensions are recognized. See <code>GNU EXTENSIONS</code>, below, for more information. </p>
 </dd>
<dd> <p> <code>-C</code> </p>
 </dd>
<dd> <p> <code>--copyright</code> Print the short version of the <font SIZE="-1">GNU</font> copyright information message on the standard output and exit successfully. </p>
 </dd>
<dd> <p> <code>-d</code>[<i>file</i>] </p>
 </dd>
<dd> <p> <code>--dump-variables</code>[<code>=</code><i>file</i>] Print a sorted list of global variables, their types and final values to <i>file</i>. If no <i>file</i> is provided, <i>gawk</i> uses a file named <code>awkvars.out</code> in the current directory. </p>
<p> Having a list of all the global variables is a good way to look for typographical errors in your programs. You would also use this option if you have a large program with a lot of functions, and you want to be sure that your functions don&#8217;t inadvertently use global variables that you meant to be local. (This is a particularly easy mistake to make with simple variable names like <code>i</code>, <code>j</code>, and so on.) </p>
 </dd>
<dd> <p> <code>-e </code><i>program-text</i> </p>
 </dd>
<dd> <p> <code>--source</code><i> program-text</i> Use <i>program-text</i> as <font SIZE="-1">AWK</font> program source code. This option allows the easy intermixing of library functions (used via the <code>-f</code> and <code>--file</code> options) with source code entered on the command line. It is intended primarily for medium to large <font SIZE="-1">AWK</font> programs used in shell scripts. </p>
 </dd>
<dd> <p> <code>-E </code><i>file</i> </p>
 </dd>
<dd> <p> <code>--exec</code><i> file</i> Similar to <code>-f</code>, however, this is option is the last one processed. This should be used with <code>#!</code> scripts, particularly for CGI applications, to avoid passing in options or source code (!) on the command line from a URL. This option disables command-line variable assignments. </p>
 </dd>
<dd> <p> <code>-g</code> </p>
 </dd>
<dd> <p> <code>--gen-pot</code> Scan and parse the <font SIZE="-1">AWK</font> program, and generate a <font SIZE="-1">GNU</font> <code>.pot</code> (Portable Object Template) format file on standard output with entries for all localizable strings in the program. The program itself is not executed. See the <font SIZE="-1">GNU</font> <i>gettext</i> distribution for more information on <code>.pot</code> files. </p>
 </dd>
<dd> <p> <code>-h</code> </p>
 </dd>
<dd> <p> <code>--help</code> Print a relatively short summary of the available options on the standard output. (Per the <i>GNU Coding Standards</i>, these options cause an immediate, successful exit.) </p>
 </dd>
<dd> <p> <code>-L </code>[<i>value</i>] </p>
 </dd>
<dd> <p> <code>--lint</code>[<code>=</code><i>value</i>] Provide warnings about constructs that are dubious or non-portable to other <font SIZE="-1">AWK</font> implementations. With an optional argument of <code>fatal</code>, lint warnings become fatal errors. This may be drastic, but its use will certainly encourage the development of cleaner <font SIZE="-1">AWK</font> programs. With an optional argument of <code>invalid</code>, only warnings about things that are actually invalid are issued. (This is not fully implemented yet.) </p>
 </dd>
<dd> <p> <code>-n</code> </p>
 </dd>
<dd> <p> <code>--non-decimal-data</code> Recognize octal and hexadecimal values in input data. <i>Use this option with great caution!</i> </p>
 </dd>
<dd> <p> <code>-N</code> </p>
 </dd>
<dd> <p> <code>--use-lc-numeric</code> This forces <i>gawk</i> to use the locale&#8217;s decimal point character when parsing input data. Although the POSIX standard requires this behavior, and <i>gawk</i> does so when <code>--posix</code> is in effect, the default is to follow traditional behavior and use a period as the decimal point, even in locales where the period is not the decimal point character. This option overrides the default behavior, without the full draconian strictness of the <code>--posix</code> option. </p>
 </dd>
<dd> <p> <code>-O</code> </p>
 </dd>
<dd> <p> <code>--optimize</code> Enable optimizations upon the internal representation of the program. Currently, this includes just simple constant-folding. The <i>gawk</i> maintainer hopes to add additional optimizations over time. </p>
 </dd>
<dd> <p> <code>-p</code>[<i>prof_file</i>] </p>
 </dd>
<dd> <p> <code>--profile</code>[<code>=</code><i>prof_file</i>] Send profiling data to <i>prof_file</i>. The default is <code>awkprof.out</code>. When run with <i>gawk</i>, the profile is just a ``pretty printed&#8217;&#8216; version of the program. When run with <i>pgawk</i>, the profile contains execution counts of each statement in the program in the left margin and function call counts for each user-defined function. </p>
 </dd>
<dd> <p> <code>-P</code> </p>
 </dd>
<dd> <p> <code>--posix</code> This turns on <i>compatibility</i> mode, with the following additional restrictions: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>\x</code> escape sequences are not recognized. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Only space and tab act as field separators when <code>FS</code> is set to a single space, newline does not. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You cannot continue lines after <code>?</code> and <code>:</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The synonym <code>func</code> for the keyword <code>function</code> is not recognized. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The operators <code>**</code> and <code>**=</code> cannot be used in place of <code>^</code> and <code>^=</code>. </p>
 </dd></dl>
</dl>
<dd> <p> <code>-r</code> </p>
 </dd>
<dd> <p> <code>--re-interval</code> Enable the use of <i>interval expressions</i> in regular expression matching (see <code>Regular Expressions</code>, below). Interval expressions were not traditionally available in the <font SIZE="-1">AWK</font> language. The <font SIZE="-1">POSIX</font> standard added them, to make <i>awk</i> and <i>egrep</i> consistent with each other. They are enabled by default, but this option remains for use with <code>--traditional</code>. </p>
 </dd>
<dd> <p> <code>-R</code> </p>
 </dd>
<dd> <p> <code>--command</code><i> file</i> <i>Dgawk</i> only. Read stored debugger commands from <i>file</i>. </p>
 </dd>
<dd> <p> <code>-S</code> </p>
 </dd>
<dd> <p> <code>--sandbox</code> Runs <i>gawk</i> in sandbox mode, disabling the <code>system()</code> function, input redirection with <code>getline</code>, output redirection with <code>print</code> and <code>printf</code>, and loading dynamic extensions. Command execution (through pipelines) is also disabled. This effectively blocks a script from accessing local resources (except for the files specified on the command line). </p>
 </dd>
<dd> <p> <code>-t</code> </p>
 </dd>
<dd> <p> <code>--lint-old</code> Provide warnings about constructs that are not portable to the original version of Unix <i>awk</i>. </p>
 </dd>
<dd> <p> <code>-V</code> </p>
 </dd>
<dd> <p> <code>--version</code> Print version information for this particular copy of <i>gawk</i> on the standard output. This is useful mainly for knowing if the current copy of <i>gawk</i> on your system is up to date with respect to whatever the Free Software Foundation is distributing. This is also useful when reporting bugs. (Per the <i>GNU Coding Standards</i>, these options cause an immediate, successful exit.) </p>
 </dd>
<dt><code>--</code></dt>
<dd> <p> Signal the end of options. This is useful to allow further arguments to the <font SIZE="-1">AWK</font> program itself to start with a ``-&#8216;&#8216;. This provides consistency with the argument parsing convention used by most other <font SIZE="-1">POSIX</font> programs. </p>
 </dd></dl>
<p> In compatibility mode, any other options are flagged as invalid, but are otherwise ignored. In normal operation, as long as program text has been supplied, unknown options are passed on to the <font SIZE="-1">AWK</font> program in the <code>ARGV</code> array for processing. This is particularly useful for running <font SIZE="-1">AWK</font> programs via the ``#!&#8216;&#8216; executable interpreter mechanism.  </p>
<h2>AWK PROGRAM EXECUTION</h2>
<p> An <font SIZE="-1">AWK</font> program consists of a sequence of pattern-action statements and optional function definitions. </p>
<dl>
<dd> <p> <code>@include &quot;</code><i>filename</i><code>&quot; </code><i>pattern</i><code><code>&nbsp;<wbr></code>{ </code><i>action statements</i><code> }</code><br />
 <br />
 <code>function </code><i>name</i><code>(</code><i>parameter list</i><code>) { </code><i>statements</i><code> }</code> </p>
 </dd></dl>
<p> <i>Gawk</i> first reads the program source from the <i>program-file</i>(s) if specified, from arguments to <code>--source</code>, or from the first non-option argument on the command line. The <code>-f</code> and <code>--source</code> options may be used multiple times on the command line. <i>Gawk</i> reads the program text as if all the <i>program-file</i>s and command line source texts had been concatenated together. This is useful for building libraries of <font SIZE="-1">AWK</font> functions, without having to include them in each new <font SIZE="-1">AWK</font> program that uses them. It also provides the ability to mix library functions with command line programs. </p>
<p> In addition, lines beginning with <code>@include</code> may be used to include other source files into your program, making library use even easier. </p>
<p> The environment variable <code>AWKPATH</code> specifies a search path to use when finding source files named with the <code>-f</code> option. If this variable does not exist, the default path is <code>&quot;.:/usr/local/share/awk&quot;</code>. (The actual directory may vary, depending upon how <i>gawk</i> was built and installed.) If a file name given to the <code>-f</code> option contains a ``/&#8216;&#8216; character, no path search is performed. </p>
<p> <i>Gawk</i> executes <font SIZE="-1">AWK</font> programs in the following order. First, all variable assignments specified via the <code>-v</code> option are performed. Next, <i>gawk</i> compiles the program into an internal form. Then, <i>gawk</i> executes the code in the <code>BEGIN</code> block(s) (if any), and then proceeds to read each file named in the <code>ARGV</code> array (up to <code>ARGV[ARGC]</code>). If there are no files named on the command line, <i>gawk</i> reads the standard input. </p>
<p> If a filename on the command line has the form <i>var</i><code>=</code><i>val</i> it is treated as a variable assignment. The variable <i>var</i> will be assigned the value <i>val</i>. (This happens after any <code>BEGIN</code> block(s) have been run.) Command line variable assignment is most useful for dynamically assigning values to the variables <font SIZE="-1">AWK</font> uses to control how input is broken into fields and records. It is also useful for controlling state if multiple passes are needed over a single data file. </p>
<p> If the value of a particular element of <code>ARGV</code> is empty (<code>&quot;&quot;</code>), <i>gawk</i> skips over it. </p>
<p> For each input file, if a <code>BEGINFILE</code> rule exists, <i>gawk</i> executes the associated code before processing the contents of the file. Similarly, <i>gawk</i> executes the code associated with <code>ENDFILE</code> after processing the file. </p>
<p> For each record in the input, <i>gawk</i> tests to see if it matches any <i>pattern</i> in the <font SIZE="-1">AWK</font> program. For each pattern that the record matches, the associated <i>action</i> is executed. The patterns are tested in the order they occur in the program. </p>
<p> Finally, after all the input is exhausted, <i>gawk</i> executes the code in the <code>END</code> block(s) (if any).  </p>
<h3>Command Line Directories</h3>
<p> According to POSIX, files named on the <i>awk</i> command line must be text files. The behavior is ``undefined&#8217;&#8216; if they are not. Most versions of <i>awk</i> treat a directory on the command line as a fatal error. </p>
<p> Starting with version 4.0 of <i>gawk</i>, a directory on the command line produces a warning, but is otherwise skipped. If either of the <code>--posix</code> or <code>--traditional</code> options is given, then <i>gawk</i> reverts to treating directories on the command line as a fatal error.  </p>
<h2>VARIABLES, RECORDS AND FIELDS</h2>
<p> <font SIZE="-1">AWK</font> variables are dynamic; they come into existence when they are first used. Their values are either floating-point numbers or strings, or both, depending upon how they are used. <font SIZE="-1">AWK</font> also has one dimensional arrays; arrays with multiple dimensions may be simulated. Several pre-defined variables are set as a program runs; these are described as needed and summarized below.  </p>
<h3>Records</h3>
<p> Normally, records are separated by newline characters. You can control how records are separated by assigning values to the built-in variable <code>RS</code>. If <code>RS</code> is any single character, that character separates records. Otherwise, <code>RS</code> is a regular expression. Text in the input that matches this regular expression separates the record. However, in compatibility mode, only the first character of its string value is used for separating records. If <code>RS</code> is set to the null string, then records are separated by blank lines. When <code>RS</code> is set to the null string, the newline character always acts as a field separator, in addition to whatever value <code>FS</code> may have.  </p>
<h3>Fields</h3>
<p> As each input record is read, <i>gawk</i> splits the record into <i>fields</i>, using the value of the <code>FS</code> variable as the field separator. If <code>FS</code> is a single character, fields are separated by that character. If <code>FS</code> is the null string, then each individual character becomes a separate field. Otherwise, <code>FS</code> is expected to be a full regular expression. In the special case that <code>FS</code> is a single space, fields are separated by runs of spaces and/or tabs and/or newlines. (But see the section <code>POSIX COMPATIBILITY</code>, below). <code>NOTE</code>: The value of <code>IGNORECASE</code> (see below) also affects how fields are split when <code>FS</code> is a regular expression, and how records are separated when <code>RS</code> is a regular expression. </p>
<p> If the <code>FIELDWIDTHS</code> variable is set to a space separated list of numbers, each field is expected to have fixed width, and <i>gawk</i> splits up the record using the specified widths. The value of <code>FS</code> is ignored. Assigning a new value to <code>FS</code> or <code>FPAT</code> overrides the use of <code>FIELDWIDTHS</code>. </p>
<p> Similarly, if the <code>FPAT</code> variable is set to a string representing a regular expression, each field is made up of text that matches that regular expression. In this case, the regular expression describes the fields themselves, instead of the text that separates the fields. Assigning a new value to <code>FS</code> or <code>FIELDWIDTHS</code> overrides the use of <code>FPAT</code>. </p>
<p> Each field in the input record may be referenced by its position, <code>$1</code>, <code>$2</code>, and so on. <code>$0</code> is the whole record. Fields need not be referenced by constants: </p>
<dl>
<dd> <p> <code> n = 5 <br />
 print $n </code> </p>
 </dd></dl>
<p> prints the fifth field in the input record. </p>
<p> The variable <code>NF</code> is set to the total number of fields in the input record. </p>
<p> References to non-existent fields (i.e. fields after <code>$NF</code>) produce the null-string. However, assigning to a non-existent field (e.g., <code>$(NF+2) = 5</code>) increases the value of <code>NF</code>, creates any intervening fields with the null string as their value, and causes the value of <code>$0</code> to be recomputed, with the fields being separated by the value of <code>OFS</code>. References to negative numbered fields cause a fatal error. Decrementing <code>NF</code> causes the values of fields past the new value to be lost, and the value of <code>$0</code> to be recomputed, with the fields being separated by the value of <code>OFS</code>. </p>
<p> Assigning a value to an existing field causes the whole record to be rebuilt when <code>$0</code> is referenced. Similarly, assigning a value to <code>$0</code> causes the record to be resplit, creating new values for the fields.  </p>
<h3>Built-in Variables</h3>
<p> <i>Gawk</i>&#8216;s built-in variables are: </p>
<dl>
<dt><code>ARGC</code></dt>
<dd> <p> The number of command line arguments (does not include options to <i>gawk</i>, or the program source). </p>
 </dd>
<dt><code>ARGIND</code></dt>
<dd> <p> The index in <code>ARGV</code> of the current file being processed. </p>
 </dd>
<dt><code>ARGV</code></dt>
<dd> <p> Array of command line arguments. The array is indexed from 0 to <code>ARGC</code> - 1. Dynamically changing the contents of <code>ARGV</code> can control the files used for data. </p>
 </dd>
<dt><code>BINMODE</code></dt>
<dd> <p> On non-POSIX systems, specifies use of ``binary&#8217;&#8216; mode for all file I/O. Numeric values of 1, 2, or 3, specify that input files, output files, or all files, respectively, should use binary I/O. String values of <code>&quot;r&quot;</code>, or <code>&quot;w&quot;</code> specify that input files, or output files, respectively, should use binary I/O. String values of <code>&quot;rw&quot;</code> or <code>&quot;wr&quot;</code> specify that all files should use binary I/O. Any other string value is treated as <code>&quot;rw&quot;</code>, but generates a warning message. </p>
 </dd>
<dt><code>CONVFMT</code></dt>
<dd> <p> The conversion format for numbers, <code>&quot;%.6g&quot;</code>, by default. </p>
 </dd>
<dt><code>ENVIRON</code></dt>
<dd> <p> An array containing the values of the current environment. The array is indexed by the environment variables, each element being the value of that variable (e.g., <code>ENVIRON[&quot;HOME&quot;]</code> might be <code>/home/arnold</code>). Changing this array does not affect the environment seen by programs which <i>gawk</i> spawns via redirection or the <code>system()</code> function. </p>
 </dd>
<dt><code>ERRNO</code></dt>
<dd> <p> If a system error occurs either doing a redirection for <code>getline</code>, during a read for <code>getline</code>, or during a <code>close()</code>, then <code>ERRNO</code> will contain a string describing the error. The value is subject to translation in non-English locales. </p>
 </dd>
<dt><code>FIELDWIDTHS</code></dt>
<dd> <p> A whitespace separated list of field widths. When set, <i>gawk</i> parses the input into fields of fixed width, instead of using the value of the <code>FS</code> variable as the field separator. See <code>Fields</code>, above. </p>
 </dd>
<dt><code>FILENAME</code></dt>
<dd> <p> The name of the current input file. If no files are specified on the command line, the value of <code>FILENAME</code> is ``-&#8216;&#8216;. However, <code>FILENAME</code> is undefined inside the <code>BEGIN</code> block (unless set by <code>getline</code>). </p>
 </dd>
<dt><code>FNR</code></dt>
<dd> <p> The input record number in the current input file. </p>
 </dd>
<dt><code>FPAT</code></dt>
<dd> <p> A regular expression describing the contents of the fields in a record. When set, <i>gawk</i> parses the input into fields, where the fields match the regular expression, instead of using the value of the <code>FS</code> variable as the field separator. See <code>Fields</code>, above. </p>
 </dd>
<dt><code>FS</code></dt>
<dd> <p> The input field separator, a space by default. See <code>Fields</code>, above. </p>
 </dd>
<dt><code>IGNORECASE</code></dt>
<dd> <p> Controls the case-sensitivity of all regular expression and string operations. If <code>IGNORECASE</code> has a non-zero value, then string comparisons and pattern matching in rules, field splitting with <code>FS</code> and <code>FPAT</code>, record separating with <code>RS</code>, regular expression matching with <code>~</code> and <code>!~</code>, and the <code>gensub()</code>, <code>gsub()</code>, <code>index()</code>, <code>match()</code>, <code>patsplit()</code>, <code>split()</code>, and <code>sub()</code> built-in functions all ignore case when doing regular expression operations. <code>NOTE</code>: Array subscripting is <i>not</i> affected. However, the <code>asort()</code> and <code>asorti()</code> functions are affected. </p>
<p> Thus, if <code>IGNORECASE</code> is not equal to zero, <code>/aB/</code> matches all of the strings <code>&quot;ab&quot;</code>, <code>&quot;aB&quot;</code>, <code>&quot;Ab&quot;</code>, and <code>&quot;AB&quot;</code>. As with all <font SIZE="-1">AWK</font> variables, the initial value of <code>IGNORECASE</code> is zero, so all regular expression and string operations are normally case-sensitive. </p>
 </dd>
<dt><code>LINT</code></dt>
<dd> <p> Provides dynamic control of the <code>--lint</code> option from within an <font SIZE="-1">AWK</font> program. When true, <i>gawk</i> prints lint warnings. When false, it does not. When assigned the string value <code>&quot;fatal&quot;</code>, lint warnings become fatal errors, exactly like <code>--lint=fatal</code>. Any other true value just prints warnings. </p>
 </dd>
<dt><code>NF</code></dt>
<dd> <p> The number of fields in the current input record. </p>
 </dd>
<dt><code>NR</code></dt>
<dd> <p> The total number of input records seen so far. </p>
 </dd>
<dt><code>OFMT</code></dt>
<dd> <p> The output format for numbers, <code>&quot;%.6g&quot;</code>, by default. </p>
 </dd>
<dt><code>OFS</code></dt>
<dd> <p> The output field separator, a space by default. </p>
 </dd>
<dt><code>ORS</code></dt>
<dd> <p> The output record separator, by default a newline. </p>
 </dd>
<dt><code>PROCINFO</code></dt>
<dd> <p> The elements of this array provide access to information about the running <font SIZE="-1">AWK</font> program. On some systems, there may be elements in the array, <code>&quot;group1&quot;</code> through <code>&quot;group</code><i>n</i><code>&quot;</code> for some <i>n</i>, which is the number of supplementary groups that the process has. Use the <code>in</code> operator to test for these elements. The following elements are guaranteed to be available: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>PROCINFO[&quot;egid&quot;]</code></dt>
<dd> <p> the value of the <i><a href="/docs/linux/man/2-getegid/">getegid</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;strftime&quot;]</code></dt>
<dd> <p> The default time format string for <code>strftime()</code>. </p>
 </dd>
<dt><code>PROCINFO[&quot;euid&quot;]</code></dt>
<dd> <p> the value of the <i><a href="/docs/linux/man/2-geteuid/">geteuid</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;FS&quot;]</code></dt>
<dd> <p> <code>&quot;FS&quot;</code> if field splitting with <code>FS</code> is in effect, <code>&quot;FPAT&quot;</code> if field splitting with <code>FPAT</code> is in effect, or <code>&quot;FIELDWIDTHS&quot;</code> if field splitting with <code>FIELDWIDTHS</code> is in effect. </p>
 </dd>
<dt><code>PROCINFO[&quot;gid&quot;]</code></dt>
<dd> <p> the value of the <i><a href="/docs/linux/man/2-getgid/">getgid</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;pgrpid&quot;]</code></dt>
<dd> <p> the process group ID of the current process. </p>
 </dd>
<dt><code>PROCINFO[&quot;pid&quot;]</code></dt>
<dd> <p> the process ID of the current process. </p>
 </dd>
<dt><code>PROCINFO[&quot;ppid&quot;]</code></dt>
<dd> <p> the parent process ID of the current process. </p>
 </dd>
<dt><code>PROCINFO[&quot;uid&quot;]</code></dt>
<dd> <p> the value of the <i><a href="/docs/linux/man/2-getuid/">getuid</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;sorted_in&quot;]</code></dt>
<dd> <p> If this element exists in <code>PROCINFO</code>, then its value controls the order in which array elements are traversed in <code>for</code> loops. Supported values are <code>&quot;@ind_str_asc&quot;</code>, <code>&quot;@ind_num_asc&quot;</code>, <code>&quot;@val_type_asc&quot;</code>, <code>&quot;@val_str_asc&quot;</code>, <code>&quot;@val_num_asc&quot;</code>, <code>&quot;@ind_str_desc&quot;</code>, <code>&quot;@ind_num_desc&quot;</code>, <code>&quot;@val_type_desc&quot;</code>, <code>&quot;@val_str_desc&quot;</code>, <code>&quot;@val_num_desc&quot;</code>, and <code>&quot;@unsorted&quot;</code>. The value can also be the name of any comparison function defined as follows: </p>
 </dd></dl>
<dl>
<dd> <p> <code>function cmp_func(i1, v1, i2, v2)</code> </p>
 </dd></dl>
<p> where <i>i1</i> and <i>i2</i> are the indices, and <i>v1</i> and <i>v2</i> are the corresponding values of the two elements being compared. It should return a number less than, equal to, or greater than 0, depending on how the elements of the array are to be ordered. </p>
<dl>
<dt><code>PROCINFO[&quot;version&quot;]</code></dt>
<dd> <p> the version of <i>gawk</i>. </p>
 </dd></dl>
</dl>
<dt><code>RS</code></dt>
<dd> <p> The input record separator, by default a newline. </p>
 </dd>
<dt><code>RT</code></dt>
<dd> <p> The record terminator. <i>Gawk</i> sets <code>RT</code> to the input text that matched the character or regular expression specified by <code>RS</code>. </p>
 </dd>
<dt><code>RSTART</code></dt>
<dd> <p> The index of the first character matched by <code>match()</code>; 0 if no match. (This implies that character indices start at one.) </p>
 </dd>
<dt><code>RLENGTH</code></dt>
<dd> <p> The length of the string matched by <code>match()</code>; -1 if no match. </p>
 </dd>
<dt><code>SUBSEP</code></dt>
<dd> <p> The character used to separate multiple subscripts in array elements, by default <code>&quot;\034&quot;</code>. </p>
 </dd>
<dt><code>TEXTDOMAIN</code></dt>
<dd> <p> The text domain of the <font SIZE="-1">AWK</font> program; used to find the localized translations for the program&#8217;s strings. </p>
 </dd></dl>
<h3>Arrays</h3>
<p> Arrays are subscripted with an expression between square brackets (<code>[</code> and <code>]</code>). If the expression is an expression list (<i>expr</i>, <i>expr</i> ...) then the array subscript is a string consisting of the concatenation of the (string) value of each expression, separated by the value of the <code>SUBSEP</code> variable. This facility is used to simulate multiply dimensioned arrays. For example: </p>
<dl>
<dd> <p> <code> i = &quot;A&quot;; j = &quot;B&quot;; k = &quot;C&quot; <br />
 x[i, j, k] = &quot;hello, world\n&quot; </code> </p>
 </dd></dl>
<p> assigns the string <code>&quot;hello, world\n&quot;</code> to the element of the array <code>x</code> which is indexed by the string <code>&quot;A\034B\034C&quot;</code>. All arrays in <font SIZE="-1">AWK</font> are associative, i.e. indexed by string values. </p>
<p> The special operator <code>in</code> may be used to test if an array has an index consisting of a particular value: </p>
<dl>
<dd> <pre><code>if (val in array)
        print array[val]
</code></pre>
 </dd></dl>
<p> If the array has multiple subscripts, use <code>(i, j) in array</code>. </p>
<p> The <code>in</code> construct may also be used in a <code>for</code> loop to iterate over all the elements of an array. </p>
<p> An element may be deleted from an array using the <code>delete</code> statement. The <code>delete</code> statement may also be used to delete the entire contents of an array, just by specifying the array name without a subscript. </p>
<p> <i>gawk</i> supports true multidimensional arrays. It does not require that such arrays be ``rectangular&#8217;&#8216; as in C or C++. For example: </p>
<dl>
<dd> <pre><code>a[1] = 5
a[2][1] = 6
a[2][2] = 7
</code></pre>
 </dd></dl>
<h3>Variable Typing And Conversion</h3>
<p> Variables and fields may be (floating point) numbers, or strings, or both. How the value of a variable is interpreted depends upon its context. If used in a numeric expression, it will be treated as a number; if used as a string it will be treated as a string. </p>
<p> To force a variable to be treated as a number, add 0 to it; to force it to be treated as a string, concatenate it with the null string. </p>
<p> When a string must be converted to a number, the conversion is accomplished using <i><a href="/docs/linux/man/3-strtod/">strtod</a></i>(3). A number is converted to a string by using the value of <code>CONVFMT</code> as a format string for <i><a href="/docs/linux/man/3-sprintf/">sprintf</a></i>(3), with the numeric value of the variable as the argument. However, even though all numbers in <font SIZE="-1">AWK</font> are floating-point, integral values are <i>always</i> converted as integers. Thus, given </p>
<dl>
<dd> <pre><code>CONVFMT = &quot;%2.2f&quot;
a = 12
b = a &quot;&quot;
</code></pre>
 </dd></dl>
<p> the variable <code>b</code> has a string value of <code>&quot;12&quot;</code> and not <code>&quot;12.00&quot;</code>. </p>
<p> <code>NOTE</code>: When operating in POSIX mode (such as with the <code>--posix</code> command line option), beware that locale settings may interfere with the way decimal numbers are treated: the decimal separator of the numbers you are feeding to <i>gawk</i> must conform to what your locale would expect, be it a comma (,) or a period (.). </p>
<p> <i>Gawk</i> performs comparisons as follows: If two variables are numeric, they are compared numerically. If one value is numeric and the other has a string value that is a ``numeric string,&#8216;&#8216; then comparisons are also done numerically. Otherwise, the numeric value is converted to a string and a string comparison is performed. Two strings are compared, of course, as strings. </p>
<p> Note that string constants, such as <code>&quot;57&quot;</code>, are <i>not</i> numeric strings, they are string constants. The idea of ``numeric string&#8217;&#8216; only applies to fields, <code>getline</code> input, <code>FILENAME</code>, <code>ARGV</code> elements, <code>ENVIRON</code> elements and the elements of an array created by <code>split()</code> or <code>patsplit()</code> that are numeric strings. The basic idea is that <i>user input</i>, and only user input, that looks numeric, should be treated that way. </p>
<p> Uninitialized variables have the numeric value 0 and the string value &quot;&quot; (the null, or empty, string).  </p>
<h3>Octal and Hexadecimal Constants</h3>
<p> You may use C-style octal and hexadecimal constants in your AWK program source code. For example, the octal value <code>011</code> is equal to decimal <code>9</code>, and the hexadecimal value <code>0x11</code> is equal to decimal 17.  </p>
<h3>String Constants</h3>
<p> String constants in <font SIZE="-1">AWK</font> are sequences of characters enclosed between double quotes (like <code>&quot;value&quot;</code>). Within strings, certain <i>escape sequences</i> are recognized, as in C. These are: </p>
<dl>
<dt><code>\\</code></dt>
<dd> <p> A literal backslash. </p>
 </dd>
<dt><code>\a</code></dt>
<dd> <p> The ``alert&#8217;&#8216; character; usually the <font SIZE="-1">ASCII</font> <font SIZE="-1">BEL</font> character. </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> backspace. </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> form-feed. </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> newline. </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> carriage return. </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> horizontal tab. </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> vertical tab. </p>
 </dd>
<dt><code>\x</code><i>hex digits</i></dt>
<dd> <p> The character represented by the string of hexadecimal digits following the <code>\x</code>. As in <font SIZE="-1">ANSI</font> C, all following hexadecimal digits are considered part of the escape sequence. (This feature should tell us something about language design by committee.) E.g., <code>&quot;\x1B&quot;</code> is the <font SIZE="-1">ASCII</font> <font SIZE="-1">ESC</font> (escape) character. </p>
 </dd>
<dt><code>\</code><i>ddd</i></dt>
<dd> <p> The character represented by the 1-, 2-, or 3-digit sequence of octal digits. E.g., <code>&quot;\033&quot;</code> is the <font SIZE="-1">ASCII</font> <font SIZE="-1">ESC</font> (escape) character. </p>
 </dd>
<dt><code>\</code><i>c</i></dt>
<dd> <p> The literal character <i>c</i>. </p>
 </dd></dl>
<p> The escape sequences may also be used inside constant regular expressions (e.g., <code>/[&nbsp;<wbr>\t\f\n\r\v]/</code> matches whitespace characters). </p>
<p> In compatibility mode, the characters represented by octal and hexadecimal escape sequences are treated literally when used in regular expression constants. Thus, <code>/a\52b/</code> is equivalent to <code>/a\*b/</code>.  </p>
<h2>PATTERNS AND ACTIONS</h2>
<p> <font SIZE="-1">AWK</font> is a line-oriented language. The pattern comes first, and then the action. Action statements are enclosed in <code>{</code> and <code>}</code>. Either the pattern may be missing, or the action may be missing, but, of course, not both. If the pattern is missing, the action is executed for every single record of input. A missing action is equivalent to </p>
<dl>
<dd> <p> <code>{ print }</code> </p>
 </dd></dl>
<p> which prints the entire record. </p>
<p> Comments begin with the <code>#</code> character, and continue until the end of the line. Blank lines may be used to separate statements. Normally, a statement ends with a newline, however, this is not the case for lines ending in a comma, <code>{</code>, <code>?</code>, <code>:</code>, <code>&amp;&amp;</code>, or <code>||</code>. Lines ending in <code>do</code> or <code>else</code> also have their statements automatically continued on the following line. In other cases, a line can be continued by ending it with a ``\&#8216;&#8216;, in which case the newline is ignored. </p>
<p> Multiple statements may be put on one line by separating them with a ``;&#8216;&#8216;. This applies to both the statements within the action part of a pattern-action pair (the usual case), and to the pattern-action statements themselves.  </p>
<h3>Patterns</h3>
<p> <font SIZE="-1">AWK</font> patterns may be one of the following: </p>
<dl>
<dd> <pre><code>
 BEGIN 
 END 
 BEGINFILE 
 ENDFILE 
 /  regular expression  / 
 relational expression 
 pattern   &amp;&amp;  pattern 
 pattern   ||  pattern 
 pattern   ?  pattern   :  pattern 
 (  pattern  ) 
 !   pattern 
 pattern1  ,  pattern2 
</code></pre>
 </dd></dl>
<p> <code>BEGIN</code> and <code>END</code> are two special kinds of patterns which are not tested against the input. The action parts of all <code>BEGIN</code> patterns are merged as if all the statements had been written in a single <code>BEGIN</code> block. They are executed before any of the input is read. Similarly, all the <code>END</code> blocks are merged, and executed when all the input is exhausted (or when an <code>exit</code> statement is executed). <code>BEGIN</code> and <code>END</code> patterns cannot be combined with other patterns in pattern expressions. <code>BEGIN</code> and <code>END</code> patterns cannot have missing action parts. </p>
<p> <code>BEGINFILE</code> and <code>ENDFILE</code> are additional special patterns whose bodies are executed before reading the first record of each command line input file and after reading the last record of each file. Inside the <code>BEGINFILE</code> rule, the value of <code>ERRNO</code> will be the empty string if the file could be opened successfully. Otherwise, there is some problem with the file and the code should use <code>nextfile</code> to skip it. If that is not done, <i>gawk</i> produces its usual fatal error for files that cannot be opened. </p>
<p> For <code>/</code><i>regular expression</i><code>/</code> patterns, the associated statement is executed for each input record that matches the regular expression. Regular expressions are the same as those in <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1), and are summarized below. </p>
<p> A <i>relational expression</i> may use any of the operators defined below in the section on actions. These generally test whether certain fields match certain regular expressions. </p>
<p> The <code>&amp;&amp;</code>, <code>||</code>, and <code>!</code> operators are logical AND, logical OR, and logical NOT, respectively, as in C. They do short-circuit evaluation, also as in C, and are used for combining more primitive pattern expressions. As in most languages, parentheses may be used to change the order of evaluation. </p>
<p> The <code>?:</code> operator is like the same operator in C. If the first pattern is true then the pattern used for testing is the second pattern, otherwise it is the third. Only one of the second and third patterns is evaluated. </p>
<p> The <i>pattern1</i><code>, </code><i>pattern2</i> form of an expression is called a <i>range pattern</i>. It matches all input records starting with a record that matches <i>pattern1</i>, and continuing until a record that matches <i>pattern2</i>, inclusive. It does not combine with any other sort of pattern expression.  </p>
<h3>Regular Expressions</h3>
<p> Regular expressions are the extended kind found in <i>egrep</i>. They are composed of characters as follows: </p>
<dl>
<dt><i>c</i></dt>
<dd> <p> matches the non-metacharacter <i>c</i>. </p>
 </dd>
<dt><i>\c</i></dt>
<dd> <p> matches the literal character <i>c</i>. </p>
 </dd>
<dt><code>.</code></dt>
<dd> <p> matches any character <i>including</i> newline. </p>
 </dd>
<dt><code>^</code></dt>
<dd> <p> matches the beginning of a string. </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> matches the end of a string. </p>
 </dd>
<dt><code>[</code><i>abc...</i><code>]</code></dt>
<dd> <p> character list, matches any of the characters <i>abc...</i>. </p>
 </dd>
<dt><code>[^</code><i>abc...</i><code>]</code></dt>
<dd> <p> negated character list, matches any character except <i>abc...</i>. </p>
 </dd>
<dt><i>r1</i><code>|</code><i>r2</i></dt>
<dd> <p> alternation: matches either <i>r1</i> or <i>r2</i>. </p>
 </dd>
<dt><i>r1r2</i></dt>
<dd> <p> concatenation: matches <i>r1</i>, and then <i>r2</i>. </p>
 </dd>
<dt><i>r</i><code>+</code></dt>
<dd> <p> matches one or more <i>r</i>&#8216;s. </p>
 </dd>
<dt><i>r</i><code>*</code></dt>
<dd> <p> matches zero or more <i>r</i>&#8216;s. </p>
 </dd>
<dt><i>r</i><code>?</code></dt>
<dd> <p> matches zero or one <i>r</i>&#8216;s. </p>
 </dd>
<dt><code>(</code><i>r</i><code>)</code></dt>
<dd> <p> grouping: matches <i>r</i>. </p>
 </dd>
<dd> <p> <i>r</i><code>{</code><i>n</i><code>}</code> </p>
 </dd>
<dd> <p> <i>r</i><code>{</code><i>n</i><code>,}</code> </p>
 </dd>
<dd> <p> <i>r</i><code>{</code><i>n</i><code>,</code><i>m</i><code>}</code> One or two numbers inside braces denote an <i>interval expression</i>. If there is one number in the braces, the preceding regular expression <i>r</i> is repeated <i>n</i> times. If there are two numbers separated by a comma, <i>r</i> is repeated <i>n</i> to <i>m</i> times. If there is one number followed by a comma, then <i>r</i> is repeated at least <i>n</i> times. </p>
 </dd>
<dt><code>\y</code></dt>
<dd> <p> matches the empty string at either the beginning or the end of a word. </p>
 </dd>
<dt><code>\B</code></dt>
<dd> <p> matches the empty string within a word. </p>
 </dd>
<dt><code>\&lt;</code></dt>
<dd> <p> matches the empty string at the beginning of a word. </p>
 </dd>
<dt><code>\&gt;</code></dt>
<dd> <p> matches the empty string at the end of a word. </p>
 </dd>
<dt><code>\s</code></dt>
<dd> <p> matches any whitespace character. </p>
 </dd>
<dt><code>\S</code></dt>
<dd> <p> matches any nonwhitespace character. </p>
 </dd>
<dt><code>\w</code></dt>
<dd> <p> matches any word-constituent character (letter, digit, or underscore). </p>
 </dd>
<dt><code>\W</code></dt>
<dd> <p> matches any character that is not word-constituent. </p>
 </dd>
<dt><code>\`</code></dt>
<dd> <p> matches the empty string at the beginning of a buffer (string). </p>
 </dd>
<dt><code>\&#8216;</code></dt>
<dd> <p> matches the empty string at the end of a buffer. </p>
 </dd></dl>
<p> The escape sequences that are valid in string constants (see below) are also valid in regular expressions. </p>
<p> <i>Character classes</i> are a feature introduced in the <font SIZE="-1">POSIX</font> standard. A character class is a special notation for describing lists of characters that have a specific attribute, but where the actual characters themselves can vary from country to country and/or from character set to character set. For example, the notion of what is an alphabetic character differs in the USA and in France. </p>
<p> A character class is only valid in a regular expression <i>inside</i> the brackets of a character list. Character classes consist of <code>[:</code>, a keyword denoting the class, and <code>:]</code>. The character classes defined by the <font SIZE="-1">POSIX</font> standard are: </p>
<dl>
<dt><code>[:alnum:]</code></dt>
<dd> <p> Alphanumeric characters. </p>
 </dd>
<dt><code>[:alpha:]</code></dt>
<dd> <p> Alphabetic characters. </p>
 </dd>
<dt><code>[:blank:]</code></dt>
<dd> <p> Space or tab characters. </p>
 </dd>
<dt><code>[:cntrl:]</code></dt>
<dd> <p> Control characters. </p>
 </dd>
<dt><code>[:digit:]</code></dt>
<dd> <p> Numeric characters. </p>
 </dd>
<dt><code>[:graph:]</code></dt>
<dd> <p> Characters that are both printable and visible. (A space is printable, but not visible, while an <code>a</code> is both.) </p>
 </dd>
<dt><code>[:lower:]</code></dt>
<dd> <p> Lowercase alphabetic characters. </p>
 </dd>
<dt><code>[:print:]</code></dt>
<dd> <p> Printable characters (characters that are not control characters.) </p>
 </dd>
<dt><code>[:punct:]</code></dt>
<dd> <p> Punctuation characters (characters that are not letter, digits, control characters, or space characters). </p>
 </dd>
<dt><code>[:space:]</code></dt>
<dd> <p> Space characters (such as space, tab, and formfeed, to name a few). </p>
 </dd>
<dt><code>[:upper:]</code></dt>
<dd> <p> Uppercase alphabetic characters. </p>
 </dd>
<dt><code>[:xdigit:]</code></dt>
<dd> <p> Characters that are hexadecimal digits. </p>
 </dd></dl>
<p> For example, before the <font SIZE="-1">POSIX</font> standard, to match alphanumeric characters, you would have had to write <code>/[A-Za-z0-9]/</code>. If your character set had other alphabetic characters in it, this would not match them, and if your character set collated differently from <font SIZE="-1">ASCII</font>, this might not even match the <font SIZE="-1">ASCII</font> alphanumeric characters. With the <font SIZE="-1">POSIX</font> character classes, you can write <code>/[[:alnum:]]/</code>, and this matches the alphabetic and numeric characters in your character set, no matter what it is. </p>
<p> Two additional special sequences can appear in character lists. These apply to non-<font SIZE="-1">ASCII</font> character sets, which can have single symbols (called <i>collating elements</i>) that are represented with more than one character, as well as several characters that are equivalent for <i>collating</i>, or sorting, purposes. (E.g., in French, a plain ``e&#8217;&#8216; and a grave-accented ``e`&#8216;&#8216; are equivalent.) </p>
<dl>
<dt>Collating Symbols</dt>
<dd> <p> A collating symbol is a multi-character collating element enclosed in <code>[.</code> and <code>.]</code>. For example, if <code>ch</code> is a collating element, then <code>[[.ch.]]</code> is a regular expression that matches this collating element, while <code>[ch]</code> is a regular expression that matches either <code>c</code> or <code>h</code>. </p>
 </dd>
<dt>Equivalence Classes</dt>
<dd> <p> An equivalence class is a locale-specific name for a list of characters that are equivalent. The name is enclosed in <code>[=</code> and <code>=]</code>. For example, the name <code>e</code> might be used to represent all of ``e,&#8216;&#8216; ``e&#8217;,&#8216;&#8216; and ``e`.&#8216;&#8216; In this case, <code>[[=e=]]</code> is a regular expression that matches any of <code>e</code>, <code>e&#8217;</code>, or <code>e`</code>. </p>
 </dd></dl>
<p> These features are very valuable in non-English speaking locales. The library functions that <i>gawk</i> uses for regular expression matching currently only recognize <font SIZE="-1">POSIX</font> character classes; they do not recognize collating symbols or equivalence classes. </p>
<p> The <code>\y</code>, <code>\B</code>, <code>\&lt;</code>, <code>\&gt;</code>, <code>\s</code>, <code>\S</code>, <code>\w</code>, <code>\W</code>, <code>\`</code>, and <code>\&#8216;</code> operators are specific to <i>gawk</i>; they are extensions based on facilities in the <font SIZE="-1">GNU</font> regular expression libraries. </p>
<p> The various command line options control how <i>gawk</i> interprets characters in regular expressions. </p>
<dl>
<dt>No options</dt>
<dd> <p> In the default case, <i>gawk</i> provide all the facilities of <font SIZE="-1">POSIX</font> regular expressions and the <font SIZE="-1">GNU</font> regular expression operators described above. </p>
 </dd>
<dt><code>--posix</code></dt>
<dd> <p> Only <font SIZE="-1">POSIX</font> regular expressions are supported, the <font SIZE="-1">GNU</font> operators are not special. (E.g., <code>\w</code> matches a literal <code>w</code>). </p>
 </dd>
<dt><code>--traditional</code></dt>
<dd> <p> Traditional Unix <i>awk</i> regular expressions are matched. The <font SIZE="-1">GNU</font> operators are not special, and interval expressions are not available. Characters described by octal and hexadecimal escape sequences are treated literally, even if they represent regular expression metacharacters. </p>
 </dd>
<dt><code>--re-interval</code></dt>
<dd> <p> Allow interval expressions in regular expressions, even if <code>--traditional</code> has been provided. </p>
 </dd></dl>
<h3>Actions</h3>
<p> Action statements are enclosed in braces, <code>{</code> and <code>}</code>. Action statements consist of the usual assignment, conditional, and looping statements found in most languages. The operators, control statements, and input/output statements available are patterned after those in C.  </p>
<h3>Operators</h3>
<p> The operators in <font SIZE="-1">AWK</font>, in order of decreasing precedence, are </p>
<dl>
<dt><code>(</code>...<code>)</code></dt>
<dd> <p> Grouping </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> Field reference. </p>
 </dd>
<dt><code>++ --</code></dt>
<dd> <p> Increment and decrement, both prefix and postfix. </p>
 </dd>
<dt><code>^</code></dt>
<dd> <p> Exponentiation (<code>**</code> may also be used, and <code>**=</code> for the assignment operator). </p>
 </dd>
<dt><code>+ - !</code></dt>
<dd> <p> Unary plus, unary minus, and logical negation. </p>
 </dd>
<dt><code>* / %</code></dt>
<dd> <p> Multiplication, division, and modulus. </p>
 </dd>
<dt><code>+ -</code></dt>
<dd> <p> Addition and subtraction. </p>
 </dd>
<dt><i>space</i></dt>
<dd> <p> String concatenation. </p>
 </dd>
<dt><code>| |&amp;</code></dt>
<dd> <p> Piped I/O for <code>getline</code>, <code>print</code>, and <code>printf</code>. </p>
 </dd>
<dt><code>&lt; &gt; &lt;= &gt;= != ==</code></dt>
<dd> <p> The regular relational operators. </p>
 </dd>
<dt><code>~ !~</code></dt>
<dd> <p> Regular expression match, negated match. <code>NOTE</code>: Do not use a constant regular expression (<code>/foo/</code>) on the left-hand side of a <code>~</code> or <code>!~</code>. Only use one on the right-hand side. The expression <code>/foo/ ~ </code><i>exp</i> has the same meaning as <code>(($0 ~ /foo/) ~ </code><i>exp</i><code>)</code>. This is usually <i>not</i> what was intended. </p>
 </dd>
<dt><code>in</code></dt>
<dd> <p> Array membership. </p>
 </dd>
<dt><code>&amp;&amp;</code></dt>
<dd> <p> Logical AND. </p>
 </dd>
<dt><code>||</code></dt>
<dd> <p> Logical OR. </p>
 </dd>
<dt><code>?:</code></dt>
<dd> <p> The C conditional expression. This has the form <i>expr1</i><code> ? </code><i>expr2</i><code> : </code><i>expr3</i>. If <i>expr1</i> is true, the value of the expression is <i>expr2</i>, otherwise it is <i>expr3</i>. Only one of <i>expr2</i> and <i>expr3</i> is evaluated. </p>
 </dd>
<dt><code>= += -= *= /= %= ^=</code></dt>
<dd> <p> Assignment. Both absolute assignment <code>(</code><i>var</i><code> = </code><i>value</i><code>)</code> and operator-assignment (the other forms) are supported. </p>
 </dd></dl>
<h3>Control Statements</h3>
<p> The control statements are as follows: </p>
<dl>
<dd> <pre><code>
 if (  condition  )  statement  [ else   statement ]
 while (  condition  )  statement 
 do  statement  while (  condition  ) 
 for (  expr1  ;  expr2  ;  expr3  )  statement 
 for (  var  in   array  )  statement 
 break 
 continue 
 delete  array  [  index  ] 
 delete  array 
 exit  [ expression  ]
 {  statements  } 
 switch (  expression  ) {
case  value  |  regex   :  statement
...
 [ default:  statement ]
 } 
</code></pre>
 </dd></dl>
<h3>I/O Statements</h3>
<p> The input/output statements are as follows: </p>
<dl>
<dt><code>close(</code><i>file </i>[<code>, </code><i>how</i>]<code>)</code></dt>
<dd> <p> Close file, pipe or co-process. The optional <i>how</i> should only be used when closing one end of a two-way pipe to a co-process. It must be a string value, either <code>&quot;to&quot;</code> or <code>&quot;from&quot;</code>. </p>
 </dd>
<dt><code>getline</code></dt>
<dd> <p> Set <code>$0</code> from next input record; set <code>NF</code>, <code>NR</code>, <code>FNR</code>. </p>
 </dd>
<dt><code>getline &lt;</code><i>file</i></dt>
<dd> <p> Set <code>$0</code> from next record of <i>file</i>; set <code>NF</code>. </p>
 </dd>
<dt><code>getline</code><i> var</i></dt>
<dd> <p> Set <i>var</i> from next input record; set <code>NR</code>, <code>FNR</code>. </p>
 </dd>
<dt><code>getline</code><i> var</i><code> &lt;</code><i>file</i></dt>
<dd> <p> Set <i>var</i> from next record of <i>file</i>. </p>
 </dd>
<dt><i>command</i><code> | getline </code>[<i>var</i>]</dt>
<dd> <p> Run <i>command</i> piping the output either into <code>$0</code> or <i>var</i>, as above. </p>
 </dd>
<dt><i>command</i><code> |&amp; getline </code>[<i>var</i>]</dt>
<dd> <p> Run <i>command</i> as a co-process piping the output either into <code>$0</code> or <i>var</i>, as above. Co-processes are a <i>gawk</i> extension. (<i>command</i> can also be a socket. See the subsection <code>Special File Names</code>, below.) </p>
 </dd>
<dt><code>next</code></dt>
<dd> <p> Stop processing the current input record. The next input record is read and processing starts over with the first pattern in the <font SIZE="-1">AWK</font> program. If the end of the input data is reached, the <code>END</code> block(s), if any, are executed. </p>
 </dd>
<dt><code>nextfile</code></dt>
<dd> <p> Stop processing the current input file. The next input record read comes from the next input file. <code>FILENAME</code> and <code>ARGIND</code> are updated, <code>FNR</code> is reset to 1, and processing starts over with the first pattern in the <font SIZE="-1">AWK</font> program. If the end of the input data is reached, the <code>END</code> block(s), if any, are executed. </p>
 </dd>
<dt><code>print</code></dt>
<dd> <p> Print the current record. The output record is terminated with the value of the <code>ORS</code> variable. </p>
 </dd>
<dt><code>print</code><i> expr-list</i></dt>
<dd> <p> Print expressions. Each expression is separated by the value of the <code>OFS</code> variable. The output record is terminated with the value of the <code>ORS</code> variable. </p>
 </dd>
<dt><code>print</code><i> expr-list</i><code> &gt;</code><i>file</i></dt>
<dd> <p> Print expressions on <i>file</i>. Each expression is separated by the value of the <code>OFS</code> variable. The output record is terminated with the value of the <code>ORS</code> variable. </p>
 </dd>
<dt><code>printf</code><i> fmt, expr-list</i></dt>
<dd> <p> Format and print. See <code>The </code><i>printf </i><code>Statement</code>, below. </p>
 </dd>
<dt><code>printf</code><i> fmt, expr-list</i><code> &gt;</code><i>file</i></dt>
<dd> <p> Format and print on <i>file</i>. </p>
 </dd>
<dt><code>system(</code><i>cmd-line</i><code>)</code></dt>
<dd> <p> Execute the command <i>cmd-line</i>, and return the exit status. (This may not be available on non-<font SIZE="-1">POSIX</font> systems.) </p>
 </dd>
<dt><code>fflush(</code>[<i>file</i>]<code>)</code></dt>
<dd> <p> Flush any buffers associated with the open output file or pipe <i>file</i>. If <i>file</i> is missing or if it is the null string, then flush all open output files and pipes. </p>
 </dd></dl>
<p> Additional output redirections are allowed for <code>print</code> and <code>printf</code>. </p>
<dl>
<dt><code>print ... &gt;&gt;</code><i> file</i></dt>
<dd> <p> Appends output to the <i>file</i>. </p>
 </dd>
<dt><code>print ... |</code><i> command</i></dt>
<dd> <p> Writes on a pipe. </p>
 </dd>
<dt><code>print ... |&amp;</code><i> command</i></dt>
<dd> <p> Sends data to a co-process or socket. (See also the subsection <code>Special File Names</code>, below.) </p>
 </dd></dl>
<p> The <code>getline</code> command returns 1 on success, 0 on end of file, and -1 on an error. Upon an error, <code>ERRNO</code> contains a string describing the problem. </p>
<p> <code>NOTE</code>: Failure in opening a two-way socket will result in a non-fatal error being returned to the calling function. If using a pipe, co-process, or socket to <code>getline</code>, or from <code>print</code> or <code>printf</code> within a loop, you <i>must</i> use <code>close()</code> to create new instances of the command or socket. <font SIZE="-1">AWK</font> does not automatically close pipes, sockets, or co-processes when they return EOF.  </p>
<i></i><h3>The printf Statement</h3>
<p> The <font SIZE="-1">AWK</font> versions of the <code>printf</code> statement and <code>sprintf()</code> function (see below) accept the following conversion specification formats: </p>
<dl>
<dt><code>%c</code></dt>
<dd> <p> A single character. If the argument used for <code>%c</code> is numeric, it is treated as a character and printed. Otherwise, the argument is assumed to be a string, and the only first character of that string is printed. </p>
 </dd>
<dt><code>%d</code>,<code> %i</code></dt>
<dd> <p> A decimal number (the integer part). </p>
 </dd>
<dt><code>%e</code>,<code> %E</code></dt>
<dd> <p> A floating point number of the form <code>[-]d.dddddde[+-]dd</code>. The <code>%E</code> format uses <code>E</code> instead of <code>e</code>. </p>
 </dd>
<dt><code>%f</code>,<code> %F</code></dt>
<dd> <p> A floating point number of the form <code>[-]ddd.dddddd</code>. If the system library supports it, <code>%F</code> is available as well. This is like <code>%f</code>, but uses capital letters for special ``not a number&#8217;&#8216; and ``infinity&#8217;&#8216; values. If <code>%F</code> is not available, <i>gawk</i> uses <code>%f</code>. </p>
 </dd>
<dt><code>%g</code>,<code> %G</code></dt>
<dd> <p> Use <code>%e</code> or <code>%f</code> conversion, whichever is shorter, with nonsignificant zeros suppressed. The <code>%G</code> format uses <code>%E</code> instead of <code>%e</code>. </p>
 </dd>
<dt><code>%o</code></dt>
<dd> <p> An unsigned octal number (also an integer). </p>
 </dd>
<dd> <p> <code>%u</code> An unsigned decimal number (again, an integer). </p>
 </dd>
<dt><code>%s</code></dt>
<dd> <p> A character string. </p>
 </dd>
<dt><code>%x</code>,<code> %X</code></dt>
<dd> <p> An unsigned hexadecimal number (an integer). The <code>%X</code> format uses <code>ABCDEF</code> instead of <code>abcdef</code>. </p>
 </dd>
<dt><code>%%</code></dt>
<dd> <p> A single <code>%</code> character; no argument is converted. </p>
 </dd></dl>
<p> Optional, additional parameters may lie between the <code>%</code> and the control letter: </p>
<dl>
<dt><i>count</i><code>$</code></dt>
<dd> <p> Use the <i>count</i>&#8216;th argument at this point in the formatting. This is called a <i>positional specifier</i> and is intended primarily for use in translated versions of format strings, not in the original text of an AWK program. It is a <i>gawk</i> extension. </p>
 </dd>
<dt><code>-</code></dt>
<dd> <p> The expression should be left-justified within its field. </p>
 </dd>
<dt><i>space</i></dt>
<dd> <p> For numeric conversions, prefix positive values with a space, and negative values with a minus sign. </p>
 </dd>
<dt><code>+</code></dt>
<dd> <p> The plus sign, used before the width modifier (see below), says to always supply a sign for numeric conversions, even if the data to be formatted is positive. The <code>+</code> overrides the space modifier. </p>
 </dd>
<dt><code>#</code></dt>
<dd> <p> Use an ``alternate form&#8217;&#8216; for certain control letters. For <code>%o</code>, supply a leading zero. For <code>%x</code>, and <code>%X</code>, supply a leading <code>0x</code> or <code>0X</code> for a nonzero result. For <code>%e</code>, <code>%E</code>, <code>%f</code> and <code>%F</code>, the result always contains a decimal point. For <code>%g</code>, and <code>%G</code>, trailing zeros are not removed from the result. </p>
 </dd>
<dt><code>0</code></dt>
<dd> <p> A leading <code>0</code> (zero) acts as a flag, that indicates output should be padded with zeroes instead of spaces. This applies only to the numeric output formats. This flag only has an effect when the field width is wider than the value to be printed. </p>
 </dd>
<dt><i>width</i></dt>
<dd> <p> The field should be padded to this width. The field is normally padded with spaces. If the <code>0</code> flag has been used, it is padded with zeroes. </p>
 </dd>
<dt><code>.</code><i>prec</i></dt>
<dd> <p> A number that specifies the precision to use when printing. For the <code>%e</code>, <code>%E</code>, <code>%f</code> and <code>%F</code>, formats, this specifies the number of digits you want printed to the right of the decimal point. For the <code>%g</code>, and <code>%G</code> formats, it specifies the maximum number of significant digits. For the <code>%d</code>, <code>%i</code>, <code>%o</code>, <code>%u</code>, <code>%x</code>, and <code>%X</code> formats, it specifies the minimum number of digits to print. For <code>%s</code>, it specifies the maximum number of characters from the string that should be printed. </p>
 </dd></dl>
<p> The dynamic <i>width</i> and <i>prec</i> capabilities of the <font SIZE="-1">ANSI</font> C <code>printf()</code> routines are supported. A <code>*</code> in place of either the <code>width</code> or <code>prec</code> specifications causes their values to be taken from the argument list to <code>printf</code> or <code>sprintf()</code>. To use a positional specifier with a dynamic width or precision, supply the <i>count</i><code>$</code> after the <code>*</code> in the format string. For example, <code>&quot;%3$*2$.*1$s&quot;</code>.  </p>
<h3>Special File Names</h3>
<p> When doing I/O redirection from either <code>print</code> or <code>printf</code> into a file, or via <code>getline</code> from a file, <i>gawk</i> recognizes certain special filenames internally. These filenames allow access to open file descriptors inherited from <i>gawk</i>&#8216;s parent process (usually the shell). These file names may also be used on the command line to name data files. The filenames are: </p>
<dl>
<dt><code>/dev/stdin</code></dt>
<dd> <p> The standard input. </p>
 </dd>
<dt><code>/dev/stdout</code></dt>
<dd> <p> The standard output. </p>
 </dd>
<dt><code>/dev/stderr</code></dt>
<dd> <p> The standard error output. </p>
 </dd>
<dt><code>/dev/fd/</code><i>n</i></dt>
<dd> <p> The file associated with the open file descriptor <i>n</i>. </p>
 </dd></dl>
<p> These are particularly useful for error messages. For example: </p>
<dl>
<dd> <p> <code> print &quot;You blew it!&quot; &gt; &quot;/dev/stderr&quot; </code> </p>
 </dd></dl>
<p> whereas you would otherwise have to use </p>
<dl>
<dd> <p> <code> print &quot;You blew it!&quot; | &quot;cat 1&gt;&amp;2&quot; </code> </p>
 </dd></dl>
<p> The following special filenames may be used with the <code>|&amp;</code> co-process operator for creating TCP/IP network connections: </p>
<dl>
<dd> <p> <code>/inet/tcp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i> </p>
 </dd>
<dd> <p> <code>/inet4/tcp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i> </p>
 </dd>
<dd> <p> <code>/inet6/tcp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i> Files for a TCP/IP connection on local port <i>lport</i> to remote host <i>rhost</i> on remote port <i>rport</i>. Use a port of <code>0</code> to have the system pick a port. Use <code>/inet4</code> to force an IPv4 connection, and <code>/inet6</code> to force an IPv6 connection. Plain <code>/inet</code> uses the system default (most likely IPv4). </p>
 </dd>
<dd> <p> <code>/inet/udp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i> </p>
 </dd>
<dd> <p> <code>/inet4/udp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i> </p>
 </dd>
<dd> <p> <code>/inet6/udp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i> Similar, but use UDP/IP instead of TCP/IP. </p>
 </dd></dl>
<h3>Numeric Functions</h3>
<p> <font SIZE="-1">AWK</font> has the following built-in arithmetic functions: </p>
<dl>
<dt><code>atan2(</code><i>y</i><code>,</code><i> x</i><code>)</code></dt>
<dd> <p> Return the arctangent of <i>y/x</i> in radians. </p>
 </dd>
<dt><code>cos(</code><i>expr</i><code>)</code></dt>
<dd> <p> Return the cosine of <i>expr</i>, which is in radians. </p>
 </dd>
<dt><code>exp(</code><i>expr</i><code>)</code></dt>
<dd> <p> The exponential function. </p>
 </dd>
<dt><code>int(</code><i>expr</i><code>)</code></dt>
<dd> <p> Truncate to integer. </p>
 </dd>
<dt><code>log(</code><i>expr</i><code>)</code></dt>
<dd> <p> The natural logarithm function. </p>
 </dd>
<dt><code>rand()</code></dt>
<dd> <p> Return a random number <i>N</i>, between 0 and 1, such that 0 &le; <i>N</i> &lt; 1. </p>
 </dd>
<dt><code>sin(</code><i>expr</i><code>)</code></dt>
<dd> <p> Return the sine of <i>expr</i>, which is in radians. </p>
 </dd>
<dt><code>sqrt(</code><i>expr</i><code>)</code></dt>
<dd> <p> The square root function. </p>
 </dd>
<dt><code>srand(</code>[<i>expr</i>]<code>)</code></dt>
<dd> <p> Use <i>expr</i> as the new seed for the random number generator. If no <i>expr</i> is provided, use the time of day. The return value is the previous seed for the random number generator. </p>
 </dd></dl>
<h3>String Functions</h3>
<p> <i>Gawk</i> has the following built-in string functions: </p>
<dl>
<dt><code>asort(</code><i>s </i>[<code>, </code><i>d</i> [<code>, </code><i>how</i>] ]<code>)</code></dt>
<dd> <p> Return the number of elements in the source array <i>s</i>. Sort the contents of <i>s</i> using <i>gawk</i>&#8216;s normal rules for comparing values, and replace the indices of the sorted values <i>s</i> with sequential integers starting with 1. If the optional destination array <i>d</i> is specified, then first duplicate <i>s</i> into <i>d</i>, and then sort <i>d</i>, leaving the indices of the source array <i>s</i> unchanged. The optional string <i>how</i> controls the direction and the comparison mode. Valid values for <i>how</i> are any of the strings valid for <code>PROCINFO[&quot;sorted_in&quot;]</code>. It can also be the name of a user-defined comparison function as described in <code>PROCINFO[&quot;sorted_in&quot;]</code>. </p>
 </dd>
<dt><code>asorti(</code><i>s </i>[<code>, </code><i>d</i> [<code>, </code><i>how</i>] ]<code>)</code></dt>
<dd> <p> Return the number of elements in the source array <i>s</i>. The behavior is the same as that of <code>asort()</code>, except that the array <i>indices</i> are used for sorting, not the array values. When done, the array is indexed numerically, and the values are those of the original indices. The original values are lost; thus provide a second array if you wish to preserve the original. The purpose of the optional string <i>how</i> is the same as described in <code>asort()</code> above. </p>
 </dd>
<dt><code>gensub(</code><i>r</i><code>, </code><i>s</i><code>, </code><i>h </i>[<code>, </code><i>t</i>]<code>)</code></dt>
<dd> <p> Search the target string <i>t</i> for matches of the regular expression <i>r</i>. If <i>h</i> is a string beginning with <code>g</code> or <code>G</code>, then replace all matches of <i>r</i> with <i>s</i>. Otherwise, <i>h</i> is a number indicating which match of <i>r</i> to replace. If <i>t</i> is not supplied, use <code>$0</code> instead. Within the replacement text <i>s</i>, the sequence <code>\</code><i>n</i>, where <i>n</i> is a digit from 1 to 9, may be used to indicate just the text that matched the <i>n</i>&#8216;th parenthesized subexpression. The sequence <code>\0</code> represents the entire matched text, as does the character <code>&amp;</code>. Unlike <code>sub()</code> and <code>gsub()</code>, the modified string is returned as the result of the function, and the original target string is <i>not</i> changed. </p>
 </dd>
<dt><code>gsub(</code><i>r</i><code>, </code><i>s </i>[<code>, </code><i>t</i>]<code>)</code></dt>
<dd> <p> For each substring matching the regular expression <i>r</i> in the string <i>t</i>, substitute the string <i>s</i>, and return the number of substitutions. If <i>t</i> is not supplied, use <code>$0</code>. An <code>&amp;</code> in the replacement text is replaced with the text that was actually matched. Use <code>\&amp;</code> to get a literal <code>&amp;</code>. (This must be typed as <code>&quot;\\&amp;&quot;</code>; see <i>GAWK: Effective AWK Programming</i> for a fuller discussion of the rules for <code>&amp;</code>&#8216;s and backslashes in the replacement text of <code>sub()</code>, <code>gsub()</code>, and <code>gensub()</code>.) </p>
 </dd>
<dt><code>index(</code><i>s</i><code>,</code><i> t</i><code>)</code></dt>
<dd> <p> Return the index of the string <i>t</i> in the string <i>s</i>, or 0 if <i>t</i> is not present. (This implies that character indices start at one.) </p>
 </dd>
<dt><code>length(</code>[<i>s</i>]<code>)</dt>
<dd> <p> Return the length of the string </code><i>s</i>, or the length of <code>$0</code> if <i>s</i> is not supplied. As a non-standard extension, with an array argument, <code>length()</code> returns the number of elements in the array. </p>
 </dd>
<dt><code>match(</code><i>s</i><code>, </code><i>r </i>[<code>, </code><i>a</i>]<code>)</code></dt>
<dd> <p> Return the position in <i>s</i> where the regular expression <i>r</i> occurs, or 0 if <i>r</i> is not present, and set the values of <code>RSTART</code> and <code>RLENGTH</code>. Note that the argument order is the same as for the <code>~</code> operator: <i>str</i><code> ~</code> <i>re</i>. If array <i>a</i> is provided, <i>a</i> is cleared and then elements 1 through <i>n</i> are filled with the portions of <i>s</i> that match the corresponding parenthesized subexpression in <i>r</i>. The 0&#8217;th element of <i>a</i> contains the portion of <i>s</i> matched by the entire regular expression <i>r</i>. Subscripts <code>a[</code><i>n</i><code>, &quot;start&quot;]</code>, and <code>a[</code><i>n</i><code>, &quot;length&quot;]</code> provide the starting index in the string and length respectively, of each matching substring. </p>
 </dd>
<dt><code>patsplit(</code><i>s</i><code>, </code><i>a </i>[<code>, </code><i>r</i> [<code>, </code><i>seps</i>] ]<code>)</code></dt>
<dd> <p> Split the string <i>s</i> into the array <i>a</i> and the separators array <i>seps</i> on the regular expression <i>r</i>, and return the number of fields. Element values are the portions of <i>s</i> that matched <i>r</i>. The value of <i>seps[i]</i> is the separator that appeared in front of <i>a[i+1]</i>. If <i>r</i> is omitted, <code>FPAT</code> is used instead. The arrays <i>a</i> and <i>seps</i> are cleared first. Splitting behaves identically to field splitting with <code>FPAT</code>, described above. </p>
 </dd>
<dt><code>split(</code><i>s</i><code>, </code><i>a </i>[<code>, </code><i>r</i> [<code>, </code><i>seps</i>] ]<code>)</code></dt>
<dd> <p> Split the string <i>s</i> into the array <i>a</i> and the separators array <i>seps</i> on the regular expression <i>r</i>, and return the number of fields. If <i>r</i> is omitted, <code>FS</code> is used instead. The arrays <i>a</i> and <i>seps</i> are cleared first. <i>seps[i]</i> is the field separator matched by <i>r</i> between <i>a[i]</i> and <i>a[i+1]</i>. If <i>r</i> is a single space, then leading whitespace in <i>s</i> goes into the extra array element <i>seps[0]</i> and trailing whitespace goes into the extra array element <i>seps[n]</i>, where <i>n</i> is the return value of <i>split(s, a, r, seps)</i>. Splitting behaves identically to field splitting, described above. </p>
 </dd>
<dt><code>sprintf(</code><i>fmt</i><code>,</code><i> expr-list</i><code>)</code></dt>
<dd> <p> Prints <i>expr-list</i> according to <i>fmt</i>, and returns the resulting string. </p>
 </dd>
<dt><code>strtonum(</code><i>str</i><code>)</code></dt>
<dd> <p> Examine <i>str</i>, and return its numeric value. If <i>str</i> begins with a leading <code>0</code>, <code>strtonum()</code> assumes that <i>str</i> is an octal number. If <i>str</i> begins with a leading <code>0x</code> or <code>0X</code>, <code>strtonum()</code> assumes that <i>str</i> is a hexadecimal number. Otherwise, decimal is assumed. </p>
 </dd>
<dt><code>sub(</code><i>r</i><code>, </code><i>s </i>[<code>, </code><i>t</i>]<code>)</code></dt>
<dd> <p> Just like <code>gsub()</code>, but replace only the first matching substring. </p>
 </dd>
<dt><code>substr(</code><i>s</i><code>, </code><i>i </i>[<code>, </code><i>n</i>]<code>)</code></dt>
<dd> <p> Return the at most <i>n</i>-character substring of <i>s</i> starting at <i>i</i>. If <i>n</i> is omitted, use the rest of <i>s</i>. </p>
 </dd>
<dt><code>tolower(</code><i>str</i><code>)</code></dt>
<dd> <p> Return a copy of the string <i>str</i>, with all the uppercase characters in <i>str</i> translated to their corresponding lowercase counterparts. Non-alphabetic characters are left unchanged. </p>
 </dd>
<dt><code>toupper(</code><i>str</i><code>)</code></dt>
<dd> <p> Return a copy of the string <i>str</i>, with all the lowercase characters in <i>str</i> translated to their corresponding uppercase counterparts. Non-alphabetic characters are left unchanged. </p>
 </dd></dl>
<p> <i>Gawk</i> is multibyte aware. This means that <code>index()</code>, <code>length()</code>, <code>substr()</code> and <code>match()</code> all work in terms of characters, not bytes.  </p>
<h3>Time Functions</h3>
<p> Since one of the primary uses of <font SIZE="-1">AWK</font> programs is processing log files that contain time stamp information, <i>gawk</i> provides the following functions for obtaining time stamps and formatting them. </p>
<dl>
<dt><code>mktime(</code><i>datespec</i><code>)</code></dt>
<dd> <p> Turn <i>datespec</i> into a time stamp of the same form as returned by <code>systime()</code>, and return the result. The <i>datespec</i> is a string of the form <i>YYYY MM DD HH MM SS[ DST]</i>. The contents of the string are six or seven numbers representing respectively the full year including century, the month from 1 to 12, the day of the month from 1 to 31, the hour of the day from 0 to 23, the minute from 0 to 59, the second from 0 to 60, and an optional daylight saving flag. The values of these numbers need not be within the ranges specified; for example, an hour of -1 means 1 hour before midnight. The origin-zero Gregorian calendar is assumed, with year 0 preceding year 1 and year -1 preceding year 0. The time is assumed to be in the local timezone. If the daylight saving flag is positive, the time is assumed to be daylight saving time; if zero, the time is assumed to be standard time; and if negative (the default), <code>mktime()</code> attempts to determine whether daylight saving time is in effect for the specified time. If <i>datespec</i> does not contain enough elements or if the resulting time is out of range, <code>mktime()</code> returns -1. </p>
 </dd>
<dt><code>strftime(</code>[<i>format </i>[<code>, </code><i>timestamp</i>[<code>, </code><i>utc-flag</i>]]]<code>)</code></dt>
<dd> <p> Format <i>timestamp</i> according to the specification in <i>format</i>. If <i>utc-flag</i> is present and is non-zero or non-null, the result is in UTC, otherwise the result is in local time. The <i>timestamp</i> should be of the same form as returned by <code>systime()</code>. If <i>timestamp</i> is missing, the current time of day is used. If <i>format</i> is missing, a default format equivalent to the output of <i><a href="/docs/linux/man/1-date/">date</a></i>(1) is used. The default format is available in <code>PROCINFO[strftime]</code>. See the specification for the <code>strftime()</code> function in <font SIZE="-1">ANSI</font> C for the format conversions that are guaranteed to be available. </p>
 </dd>
<dt><code>systime()</code></dt>
<dd> <p> Return the current time of day as the number of seconds since the Epoch (1970-01-01 00:00:00 UTC on <font SIZE="-1">POSIX</font> systems). </p>
 </dd></dl>
<h3>Bit Manipulations Functions</h3>
<p> <i>Gawk</i> supplies the following bit manipulation functions. They work by converting double-precision floating point values to <code>uintmax_t</code> integers, doing the operation, and then converting the result back to floating point. The functions are: </p>
<dl>
<dt><code>and(</code><i>v1</i><code>, </code><i>v2</i><code>)</code></dt>
<dd> <p> Return the bitwise AND of the values provided by <i>v1</i> and <i>v2</i>. </p>
 </dd>
<dt><code>compl(</code><i>val</i><code>)</code></dt>
<dd> <p> Return the bitwise complement of <i>val</i>. </p>
 </dd>
<dt><code>lshift(</code><i>val</i><code>, </code><i>count</i><code>)</code></dt>
<dd> <p> Return the value of <i>val</i>, shifted left by <i>count</i> bits. </p>
 </dd>
<dt><code>or(</code><i>v1</i><code>, </code><i>v2</i><code>)</code></dt>
<dd> <p> Return the bitwise OR of the values provided by <i>v1</i> and <i>v2</i>. </p>
 </dd>
<dt><code>rshift(</code><i>val</i><code>, </code><i>count</i><code>)</code></dt>
<dd> <p> Return the value of <i>val</i>, shifted right by <i>count</i> bits. </p>
 </dd>
<dt><code>xor(</code><i>v1</i><code>, </code><i>v2</i><code>)</code></dt>
<dd> <p> Return the bitwise XOR of the values provided by <i>v1</i> and <i>v2</i>. </p>
 </dd></dl>
<h3>Type Function</h3>
<p> The following function is for use with multidimensional arrays. </p>
<dl>
<dt><code>isarray(</code><i>x</i><code>)</code></dt>
<dd> <p> Return true if <i>x</i> is an array, false otherwise. </p>
 </dd></dl>
<h3>Internationalization Functions</h3>
<p> The following functions may be used from within your AWK program for translating strings at run-time. For full details, see <i>GAWK: Effective AWK Programming</i>. </p>
<dl>
<dt><code>bindtextdomain(</code><i>directory </i>[<code>, </code><i>domain</i>]<code>)</code></dt>
<dd> <p> Specify the directory where <i>gawk</i> looks for the <code>.mo</code> files, in case they will not or cannot be placed in the ``standard&#8217;&#8216; locations (e.g., during testing). It returns the directory where <i>domain</i> is ``bound.&#8216;&#8216; </p>
<p> The default <i>domain</i> is the value of <code>TEXTDOMAIN</code>. If <i>directory</i> is the null string (<code>&quot;&quot;</code>), then <code>bindtextdomain()</code> returns the current binding for the given <i>domain</i>. </p>
 </dd>
<dt><code>dcgettext(</code><i>string </i>[<code>, </code><i>domain </i>[<code>, </code><i>category</i>]]<code>)</code></dt>
<dd> <p> Return the translation of <i>string</i> in text domain <i>domain</i> for locale category <i>category</i>. The default value for <i>domain</i> is the current value of <code>TEXTDOMAIN</code>. The default value for <i>category</i> is <code>&quot;LC_MESSAGES&quot;</code>. </p>
<p> If you supply a value for <i>category</i>, it must be a string equal to one of the known locale categories described in <i>GAWK: Effective AWK Programming</i>. You must also supply a text domain. Use <code>TEXTDOMAIN</code> if you want to use the current domain. </p>
 </dd>
<dt><code>dcngettext(</code><i>string1 </i>, <i>string2 </i>, <i>number </i>[<code>, </code><i>domain </i>[<code>, </code><i>category</i>]]<code>)</code></dt>
<dd> <p> Return the plural form used for <i>number</i> of the translation of <i>string1</i> and <i>string2</i> in text domain <i>domain</i> for locale category <i>category</i>. The default value for <i>domain</i> is the current value of <code>TEXTDOMAIN</code>. The default value for <i>category</i> is <code>&quot;LC_MESSAGES&quot;</code>. </p>
<p> If you supply a value for <i>category</i>, it must be a string equal to one of the known locale categories described in <i>GAWK: Effective AWK Programming</i>. You must also supply a text domain. Use <code>TEXTDOMAIN</code> if you want to use the current domain. </p>
 </dd></dl>
<h2>USER-DEFINED FUNCTIONS</h2>
<p> Functions in <font SIZE="-1">AWK</font> are defined as follows: </p>
<dl>
<dd> <p> <code>function </code><i>name</i><code>(</code><i>parameter list</i><code>) { </code><i>statements </i><code>}</code> </p>
 </dd></dl>
<p> Functions are executed when they are called from within expressions in either patterns or actions. Actual parameters supplied in the function call are used to instantiate the formal parameters declared in the function. Arrays are passed by reference, other variables are passed by value. </p>
<p> Since functions were not originally part of the <font SIZE="-1">AWK</font> language, the provision for local variables is rather clumsy: They are declared as extra parameters in the parameter list. The convention is to separate local variables from real parameters by extra spaces in the parameter list. For example: </p>
<dl>
<dd> <pre><code>function f(p, q, a, b) # a and b are local
{
        ...
}
/abc/ { ... ; f(1, 2) ; ... }
</code></pre>
 </dd></dl>
<p> The left parenthesis in a function call is required to immediately follow the function name, without any intervening whitespace. This avoids a syntactic ambiguity with the concatenation operator. This restriction does not apply to the built-in functions listed above. </p>
<p> Functions may call each other and may be recursive. Function parameters used as local variables are initialized to the null string and the number zero upon function invocation. </p>
<p> Use <code>return</code><i> expr</i> to return a value from a function. The return value is undefined if no value is provided, or if the function returns by ``falling off&#8217;&#8216; the end. </p>
<p> As a <i>gawk</i> extension, functions may be called indirectly. To do this, assign the name of the function to be called, as a string, to a variable. Then use the variable as if it were the name of a function, prefixed with an <code>@</code> sign, like so: </p>
<dl>
<dd> <pre><code>function myfunc()
{
        print &quot;myfunc called&quot;
        ...
}
{ ...
        the_func = &quot;myfunc&quot;
        @the_func() # call through the_func to myfunc
        ...
}
</code></pre>
 </dd></dl>
<p> If <code>--lint</code> has been provided, <i>gawk</i> warns about calls to undefined functions at parse time, instead of at run time. Calling an undefined function at run time is a fatal error. </p>
<p> The word <code>func</code> may be used in place of <code>function</code>.  </p>
<h2>DYNAMICALLY LOADING NEW FUNCTIONS</h2>
<p> You can dynamically add new built-in functions to the running <i>gawk</i> interpreter. The full details are beyond the scope of this manual page; see <i>GAWK: Effective AWK Programming</i> for the details. </p>
<dl>
<dt><code>extension(</code><i>object</i><code>, </code><i>function</i><code>)</code></dt>
<dd> <p> Dynamically link the shared object file named by <i>object</i>, and invoke <i>function</i> in that object, to perform initialization. These should both be provided as strings. Return the value returned by <i>function</i>. </p>
 </dd></dl>
<p> Using this feature at the C level is not pretty, but it is unlikely to go away. Additional mechanisms may be added at some point.  </p>
<h2>SIGNALS</h2>
<p> <i>pgawk</i> accepts two signals. <code>SIGUSR1</code> causes it to dump a profile and function call stack to the profile file, which is either <code>awkprof.out</code>, or whatever file was named with the <code>--profile</code> option. It then continues to run. <code>SIGHUP</code> causes <i>pgawk</i> to dump the profile and function call stack and then exit.  </p>
<h2>INTERNATIONALIZATION</h2>
<p> String constants are sequences of characters enclosed in double quotes. In non-English speaking environments, it is possible to mark strings in the <font SIZE="-1">AWK</font> program as requiring translation to the local natural language. Such strings are marked in the <font SIZE="-1">AWK</font> program with a leading underscore (``_&#8216;&#8216;). For example, </p>
<dl>
<dd> <p> <code> gawk &#8216;BEGIN { print &quot;hello, world&quot; }&#8216; </p>
 </dd></dl>
<p> </code> always prints <code>hello, world</code>. But, </p>
<dl>
<dd> <p> <code> gawk &#8216;BEGIN { print _&quot;hello, world&quot; }&#8216; </p>
 </dd></dl>
<p> </code> might print <code>bonjour, monde</code> in France. </p>
<p> There are several steps involved in producing and running a localizable <font SIZE="-1">AWK</font> program. </p>
<dl>
<dt>1.</dt>
<dd> <p> Add a <code>BEGIN</code> action to assign a value to the <code>TEXTDOMAIN</code> variable to set the text domain to a name associated with your program: </p>
 </dd>
<dl>
<dd> <p> <code> BEGIN { TEXTDOMAIN = &quot;myprog&quot; } </code> </p>
 </dd></dl>
<p> This allows <i>gawk</i> to find the <code>.mo</code> file associated with your program. Without this step, <i>gawk</i> uses the <code>messages</code> text domain, which likely does not contain translations for your program. </p>
<dt>2.</dt>
<dd> <p> Mark all strings that should be translated with leading underscores. </p>
 </dd>
<dt>3.</dt>
<dd> <p> If necessary, use the <code>dcgettext()</code> and/or <code>bindtextdomain()</code> functions in your program, as appropriate. </p>
 </dd>
<dt>4.</dt>
<dd> <p> Run <code>gawk --gen-pot -f myprog.awk &gt; myprog.pot</code> to generate a <code>.po</code> file for your program. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Provide appropriate translations, and build and install the corresponding <code>.mo</code> files. </p>
 </dd></dl>
<p> The internationalization features are described in full detail in <i>GAWK: Effective AWK Programming</i>.  </p>
<h2>POSIX COMPATIBILITY</h2>
<p> A primary goal for <i>gawk</i> is compatibility with the <font SIZE="-1">POSIX</font> standard, as well as with the latest version of <font SIZE="-1">UNIX</font> <i>awk</i>. To this end, <i>gawk</i> incorporates the following user visible features which are not described in the <font SIZE="-1">AWK</font> book, but are part of the Bell Laboratories version of <i>awk</i>, and are in the <font SIZE="-1">POSIX</font> standard. </p>
<p> The book indicates that command line variable assignment happens when <i>awk</i> would otherwise open the argument as a file, which is after the <code>BEGIN</code> block is executed. However, in earlier implementations, when such an assignment appeared before any file names, the assignment would happen <i>before</i> the <code>BEGIN</code> block was run. Applications came to depend on this ``feature.&#8216;&#8216; When <i>awk</i> was changed to match its documentation, the <code>-v</code> option for assigning variables before program execution was added to accommodate applications that depended upon the old behavior. (This feature was agreed upon by both the Bell Laboratories and the <font SIZE="-1">GNU</font> developers.) </p>
<p> When processing arguments, <i>gawk</i> uses the special option ``--&#8216;&#8216; to signal the end of arguments. In compatibility mode, it warns about but otherwise ignores undefined options. In normal operation, such arguments are passed on to the <font SIZE="-1">AWK</font> program for it to process. </p>
<p> The <font SIZE="-1">AWK</font> book does not define the return value of <code>srand()</code>. The <font SIZE="-1">POSIX</font> standard has it return the seed it was using, to allow keeping track of random number sequences. Therefore <code>srand()</code> in <i>gawk</i> also returns its current seed. </p>
<p> Other new features are: The use of multiple <code>-f</code> options (from MKS <i>awk</i>); the <code>ENVIRON</code> array; the <code>\a</code>, and <code>\v</code> escape sequences (done originally in <i>gawk</i> and fed back into the Bell Laboratories version); the <code>tolower()</code> and <code>toupper()</code> built-in functions (from the Bell Laboratories version); and the <font SIZE="-1">ANSI</font> C conversion specifications in <code>printf</code> (done first in the Bell Laboratories version).  </p>
<h2>HISTORICAL FEATURES</h2>
<p> There is one feature of historical <font SIZE="-1">AWK</font> implementations that <i>gawk</i> supports: It is possible to call the <code>length()</code> built-in function not only with no argument, but even without parentheses! Thus, </p>
<dl>
<dd> <p> <code> a = length <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code># Holy Algol 60, Batman!<br />
 </code> </p>
 </dd></dl>
<p> is the same as either of </p>
<dl>
<dd> <p> <code> a = length() <br />
 a = length($0) </code> </p>
 </dd></dl>
<p> Using this feature is poor practice, and <i>gawk</i> issues a warning about its use if <code>--lint</code> is specified on the command line.  </p>
<h2>GNU EXTENSIONS</h2>
<p> <i>Gawk</i> has a number of extensions to <font SIZE="-1">POSIX</font> <i>awk</i>. They are described in this section. All the extensions described here can be disabled by invoking <i>gawk</i> with the <code>--traditional</code> or <code>--posix</code> options. </p>
<p> The following features of <i>gawk</i> are not available in <font SIZE="-1">POSIX</font> <i>awk</i>. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> No path search is performed for files named via the <code>-f</code> option. Therefore the <code>AWKPATH</code> environment variable is not special. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There is no facility for doing file inclusion (<i>gawk</i>&#8216;s <code>@include</code> mechanism). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>\x</code> escape sequence. (Disabled with <code>--posix</code>.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ability to continue lines after <code>?</code> and <code>:</code>. (Disabled with <code>--posix</code>.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Octal and hexadecimal constants in AWK programs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>ARGIND</code>, <code>BINMODE</code>, <code>ERRNO</code>, <code>LINT</code>, <code>RT</code> and <code>TEXTDOMAIN</code> variables are not special. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>IGNORECASE</code> variable and its side-effects are not available. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>FIELDWIDTHS</code> variable and fixed-width field splitting. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>FPAT</code> variable and field splitting based on field values. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>PROCINFO</code> array is not available. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The use of <code>RS</code> as a regular expression. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The special file names available for I/O redirection are not recognized. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>|&amp;</code> operator for creating co-processes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>BEGINFILE</code> and <code>ENDFILE</code> special patterns are not available. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ability to split out individual characters using the null string as the value of <code>FS</code>, and as the third argument to <code>split()</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An optional fourth argument to <code>split()</code> to receive the separator texts. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The optional second argument to the <code>close()</code> function. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The optional third argument to the <code>match()</code> function. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ability to use positional specifiers with <code>printf</code> and <code>sprintf()</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ability to pass an array to <code>length()</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The use of <code>delete</code><i> array</i> to delete the entire contents of an array. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The use of <code>nextfile</code> to abandon processing of the current input file. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>and()</code>, <code>asort()</code>, <code>asorti()</code>, <code>bindtextdomain()</code>, <code>compl()</code>, <code>dcgettext()</code>, <code>dcngettext()</code>, <code>gensub()</code>, <code>lshift()</code>, <code>mktime()</code>, <code>or()</code>, <code>patsplit()</code>, <code>rshift()</code>, <code>strftime()</code>, <code>strtonum()</code>, <code>systime()</code> and <code>xor()</code> functions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Localizable strings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Adding new built-in functions dynamically with the <code>extension()</code> function. </p>
 </dd></dl>
<p> The <font SIZE="-1">AWK</font> book does not define the return value of the <code>close()</code> function. <i>Gawk</i>&#8216;s <code>close()</code> returns the value from <i><a href="/docs/linux/man/3-fclose/">fclose</a></i>(3), or <i><a href="/docs/linux/man/3-pclose/">pclose</a></i>(3), when closing an output file or pipe, respectively. It returns the process&#8217;s exit status when closing an input pipe. The return value is -1 if the named file, pipe or co-process was not opened with a redirection. </p>
<p> When <i>gawk</i> is invoked with the <code>--traditional</code> option, if the <i>fs</i> argument to the <code>-F</code> option is ``t&#8217;&#8216;, then <code>FS</code> is set to the tab character. Note that typing <code>gawk -F\t ...</code> simply causes the shell to quote the ``t,&#8216;&#8216; and does not pass ``\t&#8217;&#8216; to the <code>-F</code> option. Since this is a rather ugly special case, it is not the default behavior. This behavior also does not occur if <code>--posix</code> has been specified. To really get a tab character as the field separator, it is best to use single quotes: <code>gawk -F&#8217;\t&#8217; ...</code>.  </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The <code>AWKPATH</code> environment variable can be used to provide a list of directories that <i>gawk</i> searches when looking for files named via the <code>-f</code> and <code>--file</code> options. </p>
<p> For socket communication, two special environment variables can be used to control the number of retries (<code>GAWK_SOCK_RETRIES</code>), and the interval between retries (<code>GAWK_MSEC_SLEEP</code>). The interval is in milliseconds. On systems that do not support <i><a href="/docs/linux/man/3-usleep/">usleep</a></i>(3), the value is rounded up to an integral number of seconds. </p>
<p> If <code>POSIXLY_CORRECT</code> exists in the environment, then <i>gawk</i> behaves exactly as if <code>--posix</code> had been specified on the command line. If <code>--lint</code> has been specified, <i>gawk</i> issues a warning message to this effect.  </p>
<h2>EXIT STATUS</h2>
<p> If the <code>exit</code> statement is used with a value, then <i>gawk</i> exits with the numeric value given to it. </p>
<p> Otherwise, if there were no problems during execution, <i>gawk</i> exits with the value of the C constant <code>EXIT_SUCCESS</code>. This is usually zero. </p>
<p> If an error occurs, <i>gawk</i> exits with the value of the C constant <code>EXIT_FAILURE</code>. This is usually one. </p>
<p> If <i>gawk</i> exits because of a fatal error, the exit status is 2. On non-POSIX systems, this value may be mapped to <code>EXIT_FAILURE</code>.  </p>
<h2>VERSION INFORMATION</h2>
<p> This man page documents <i>gawk</i>, version 4.0.  </p>
<h2>AUTHORS</h2>
<p> The original version of <font SIZE="-1">UNIX</font> <i>awk</i> was designed and implemented by Alfred Aho, Peter Weinberger, and Brian Kernighan of Bell Laboratories. Brian Kernighan continues to maintain and enhance it. </p>
<p> Paul Rubin and Jay Fenlason, of the Free Software Foundation, wrote <i>gawk</i>, to be compatible with the original version of <i>awk</i> distributed in Seventh Edition <font SIZE="-1">UNIX</font>. John Woods contributed a number of bug fixes. David Trueman, with contributions from Arnold Robbins, made <i>gawk</i> compatible with the new version of <font SIZE="-1">UNIX</font> <i>awk</i>. Arnold Robbins is the current maintainer. </p>
<p> The initial DOS port was done by Conrad Kwok and Scott Garfinkle. Scott Deifik maintains the port to MS-DOS using DJGPP. Eli Zaretskii maintains the port to MS-Windows using MinGW. Pat Rankin did the port to VMS, and Michal Jaegermann did the port to the Atari ST. The port to OS/2 was done by Kai Uwe Rommel, with contributions and help from Darrel Hankerson. Andreas Buening now maintains the OS/2 port. The late Fred Fish supplied support for the Amiga, and Martin Brown provided the BeOS port. Stephen Davies provided the original Tandem port, and Matthew Woehlke provided changes for Tandem&#8217;s POSIX-compliant systems. Dave Pitts provided the port to z/OS. </p>
<p> See the <i>README</i> file in the <i>gawk</i> distribution for up-to-date information about maintainers and which ports are currently supported.  </p>
<h2>BUG REPORTS</h2>
<p> If you find a bug in <i>gawk</i>, please send electronic mail to <code>bug-gawk [at] gnu.org</code>. Please include your operating system and its revision, the version of <i>gawk</i> (from <code>gawk --version</code>), which C compiler you used to compile it, and a test program and data that are as small as possible for reproducing the problem. </p>
<p> Before sending a bug report, please do the following things. First, verify that you have the latest version of <i>gawk</i>. Many bugs (usually subtle ones) are fixed at each release, and if yours is out of date, the problem may already have been solved. Second, please see if setting the environment variable <code>LC_ALL</code> to <code>LC_ALL=C</code> causes things to behave as you expect. If so, it&#8217;s a locale issue, and may or may not really be a bug. Finally, please read this man page and the reference manual carefully to be sure that what you think is a bug really is, instead of just a quirk in the language. </p>
<p> Whatever you do, do <code>NOT</code> post a bug report in <code>comp.lang.awk</code>. While the <i>gawk</i> developers occasionally read this newsgroup, posting bug reports there is an unreliable way to report bugs. Instead, please use the electronic mail addresses given above. </p>
<p> If you&#8217;re using a GNU/Linux or BSD-based system, you may wish to submit a bug report to the vendor of your distribution. That&#8217;s fine, but please send a copy to the official email address as well, since there&#8217;s no guarantee that the bug report will be forwarded to the <i>gawk</i> maintainer.  </p>
<h2>BUGS</h2>
<p> The <code>-F</code> option is not necessary given the command line variable assignment feature; it remains only for backwards compatibility. </p>
<p> Syntactically invalid single character programs tend to overflow the parse stack, generating a rather unhelpful message. Such programs are surprisingly difficult to diagnose in the completely general case, and the effort to do so really is not worth it.  </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1), <i><a href="/docs/linux/man/2-getpid/">getpid</a></i>(2), <i><a href="/docs/linux/man/2-getppid/">getppid</a></i>(2), <i><a href="/docs/linux/man/2-getpgrp/">getpgrp</a></i>(2), <i><a href="/docs/linux/man/2-getuid/">getuid</a></i>(2), <i><a href="/docs/linux/man/2-geteuid/">geteuid</a></i>(2), <i><a href="/docs/linux/man/2-getgid/">getgid</a></i>(2), <i><a href="/docs/linux/man/2-getegid/">getegid</a></i>(2), <i><a href="/docs/linux/man/2-getgroups/">getgroups</a></i>(2), <i><a href="/docs/linux/man/3-usleep/">usleep</a></i>(3) </p>
<p> <i>The AWK Programming Language</i>, Alfred V. Aho, Brian W. Kernighan, Peter J. Weinberger, Addison-Wesley, 1988. ISBN 0-201-07981-X. </p>
<p> <i>GAWK: Effective AWK Programming</i>, Edition 4.0, shipped with the <i>gawk</i> source. The current version of this document is available online at <code><a rel="nofollow" href="http://www.gnu.org/software/gawk/manual">http://www.gnu.org/software/gawk/manual</a></code>.  </p>
<h2>EXAMPLES</h2>
<pre><code>Print and sort the login names of all users:
         BEGIN { FS = &quot;:&quot; }
                { print $1 | &quot;sort&quot; }
 Count lines in a file:
                 { nlines++ }
        END { print nlines }
 Precede each line by its number in the file:
         { print FNR, $0 }
 Concatenate and line number (a variation on a theme):
         { print NR, $0 }
 Run an external command for particular lines of data:
         tail -f access_log |
        awk '/myhome.html/ { system(&quot;nmap &quot; $1 &quot;&gt;&gt; logdir/myhome.html&quot;) }'
 </code></pre>
<h2>ACKNOWLEDGEMENTS</h2>
<p> Brian Kernighan of Bell Laboratories provided valuable assistance during testing and debugging. We thank him.  </p>
<h2>COPYING PERMISSIONS</h2>
<p> Copyright &#169; 1989, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2001, 2002, 2003, 2004, 2005, 2007, 2009, 2010, 2011 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this manual page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual page into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Foundation. </p>
