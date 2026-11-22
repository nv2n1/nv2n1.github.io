---

title: "awk(1)"
name: "awk"
section: "1"
letter: "a"
url: "/docs/linux/man/1-awk/"
description: "gawk – pattern scanning and processing language"
---

<p> gawk - pattern scanning and processing language </p>
<h2>SYNOPSIS</h2>
<p> <code>gawk</code> [ POSIX or GNU style options ] <code>-f</code> <i>program-file</i> [ <code>--</code> ] file ... <br/>
 <code>gawk</code> [ POSIX or GNU style options ] [ <code>--</code> ] <i>program-text</i> file ...  </p>
<h2>DESCRIPTION</h2>
<p> <i>Gawk</i> is the GNU Project&#8217;s implementation of the AWK programming language. It conforms to the definition of the language in the POSIX 1003.1 standard. This version in turn is based on the description in <i>The AWK Programming Language</i>, by Aho, Kernighan, and Weinberger. <i>Gawk</i> provides the additional features found in the current version of Brian Kernighan&#8217;s <i>awk</i> and numerous GNU-specific extensions. </p>
<p> The command line consists of options to <i>gawk</i> itself, the AWK program text (if not supplied via the <code>-f</code> or <code>--include</code> options), and values to be made available in the <code>ARGC</code> and <code>ARGV</code> pre-defined AWK variables. </p>
<p> When <i>gawk</i> is invoked with the <code>--profile</code> option, it starts gathering profiling statistics from the execution of the program. <i>Gawk</i> runs more slowly in this mode, and automatically produces an execution profile in the file <code>awkprof.out</code> when done. See the <code>--profile</code> option, below. </p>
<p> <i>Gawk</i> also has an integrated debugger. An interactive debugging session can be started by supplying the <code>--debug</code> option to the command line. In this mode of execution, <i>gawk</i> loads the AWK source code and then prompts for debugging commands. <i>Gawk</i> can only debug AWK program source provided with the <code>-f</code> and <code>--include</code> options. The debugger is documented in <i>GAWK: Effective AWK Programming</i>.  </p>
<h2>OPTION FORMAT</h2>
<p> <i>Gawk</i> options may be either traditional POSIX-style one letter options, or GNU-style long options. POSIX options start with a single ``-&#8216;&#8216;, while long options start with ``--&#8216;&#8216;. Long options are provided for both GNU-specific features and for POSIX-mandated features. </p>
<p> <i>Gawk</i>-specific options are typically used in long-option form. Arguments to long options are either joined with the option by an <code>=</code> sign, with no intervening spaces, or they may be provided in the next command line argument. Long options may be abbreviated, as long as the abbreviation remains unique. </p>
<p> Additionally, every long option has a corresponding short option, so that the option&#8217;s functionality may be used from within <code>#!</code> executable scripts.  </p>
<h2>OPTIONS</h2>
<p> <i>Gawk</i> accepts the following options. Standard options are listed first, followed by options for <i>gawk</i> extensions, listed alphabetically by short option. </p>
<dl>
<dt><code>-f</code><i> program-file</i></dt>
<dd>  </dd>
<dt><code>--file</code><i> program-file</i></dt>
<dd> <p> Read the AWK program source from the file <i>program-file</i>, instead of from the first command line argument. Multiple <code>-f</code> (or <code>--file</code>) options may be used. Files read with <code>-f</code> are treated as if they begin with an implicit <code>@namespace &quot;awk&quot;</code> statement. </p>
 </dd>
<dt><code>-F</code><i> fs</i></dt>
<dd>  </dd>
<dt><code>--field-separator</code><i> fs</i></dt>
<dd> <p> Use <i>fs</i> for the input field separator (the value of the <code>FS</code> predefined variable). </p>
 </dd>
<dd> <p> <code>-v</code><i> var</i><code>=</code><i>val</i> </p>
 </dd>
<dd> <p> <code>--assign </code><i>var</i><code>=</code><i>val</i> Assign the value <i>val</i> to the variable <i>var</i>, before execution of the program begins. Such variable values are available to the <code>BEGIN</code> rule of an AWK program. </p>
 </dd>
<dt><code>-b</code></dt>
<dd>  </dd>
<dt><code>--characters-as-bytes</code></dt>
<dd> <p> Treat all input data as single-byte characters. In other words, don&#8217;t pay any attention to the locale information when attempting to process strings as multibyte characters. The <code>--posix</code> option overrides this one. </p>
 </dd>
<dt><code>-c</code></dt>
<dd>  </dd>
<dt><code>--traditional</code></dt>
<dd> <p> Run in <i>compatibility</i> mode. In compatibility mode, <i>gawk</i> behaves identically to Brian Kernighan&#8217;s <i>awk</i>; none of the GNU-specific extensions are recognized. See <code>GNU EXTENSIONS</code>, below, for more information. </p>
 </dd>
<dt><code>-C</code></dt>
<dd>  </dd>
<dt><code>--copyright</code></dt>
<dd> <p> Print the short version of the GNU copyright information message on the standard output and exit successfully. </p>
 </dd>
<dd> <p> <code>-d</code>[<i>file</i>] </p>
 </dd>
<dd> <p> <code>--dump-variables</code>[<code>=</code><i>file</i>] Print a sorted list of global variables, their types and final values to <i>file</i>. If no <i>file</i> is provided, <i>gawk</i> uses a file named <code>awkvars.out</code> in the current directory. </p>
<p> Having a list of all the global variables is a good way to look for typographical errors in your programs. You would also use this option if you have a large program with a lot of functions, and you want to be sure that your functions don&#8217;t inadvertently use global variables that you meant to be local. (This is a particularly easy mistake to make with simple variable names like <code>i</code>, <code>j</code>, and so on.) </p>
 </dd>
<dd> <p> <code>-D</code>[<i>file</i>] </p>
 </dd>
<dd> <p> <code>--debug</code>[<code>=</code><i>file</i>] Enable debugging of AWK programs. By default, the debugger reads commands interactively from the keyboard (standard input). The optional <i>file</i> argument specifies a file with a list of commands for the debugger to execute non-interactively. </p>
 </dd>
<dt><code>-e </code><i>program-text</i></dt>
<dd>  </dd>
<dt><code>--source</code><i> program-text</i></dt>
<dd> <p> Use <i>program-text</i> as AWK program source code. This option allows the easy intermixing of library functions (used via the <code>-f</code> and <code>--include</code> options) with source code entered on the command line. It is intended primarily for medium to large AWK programs used in shell scripts. Each argument supplied via <code>-e</code> is treated as if it begins with an implicit <code>@namespace &quot;awk&quot;</code> statement. </p>
 </dd>
<dt><code>-E </code><i>file</i></dt>
<dd>  </dd>
<dt><code>--exec</code><i> file</i></dt>
<dd> <p> Similar to <code>-f</code>, however, this is option is the last one processed. This should be used with <code>#!</code> scripts, particularly for CGI applications, to avoid passing in options or source code (!) on the command line from a URL. This option disables command-line variable assignments. </p>
 </dd>
<dt><code>-g</code></dt>
<dd>  </dd>
<dt><code>--gen-pot</code></dt>
<dd> <p> Scan and parse the AWK program, and generate a GNU <code>.pot</code> (Portable Object Template) format file on standard output with entries for all localizable strings in the program. The program itself is not executed. See the GNU <i>gettext</i> distribution for more information on <code>.pot</code> files. </p>
 </dd>
<dt><code>-h</code></dt>
<dd>  </dd>
<dt><code>--help</code></dt>
<dd> <p> Print a relatively short summary of the available options on the standard output. (Per the <i>GNU Coding Standards</i>, these options cause an immediate, successful exit.) </p>
 </dd>
<dt><code>-i </code><i>include-file</i></dt>
<dd>  </dd>
<dt><code>--include</code><i> include-file</i></dt>
<dd> <p> Load an awk source library. This searches for the library using the <code>AWKPATH</code> environment variable. If the initial search fails, another attempt will be made after appending the <code>.awk</code> suffix. The file will be loaded only once (i.e., duplicates are eliminated), and the code does not constitute the main program source. Files read with <code>--include</code> are treated as if they begin with an implicit <code>@namespace &quot;awk&quot;</code> statement. </p>
 </dd>
<dt><code>-l </code><i>lib</i></dt>
<dd>  </dd>
<dt><code>--load</code><i> lib</i></dt>
<dd> <p> Load a <i>gawk</i> extension from the shared library <i>lib</i>. This searches for the library using the <code>AWKLIBPATH</code> environment variable. If the initial search fails, another attempt will be made after appending the default shared library suffix for the platform. The library initialization routine is expected to be named <code>dl_load()</code>. </p>
 </dd>
<dt><code>-L </code>[<i>value</i>] </dt>
<dd>  </dd>
<dt><code>--lint</code>[<code>=</code><i>value</i>] </dt>
<dd> <p> Provide warnings about constructs that are dubious or non-portable to other AWK implementations. With an optional argument of <code>fatal</code>, lint warnings become fatal errors. This may be drastic, but its use will certainly encourage the development of cleaner AWK programs. With an optional argument of <code>invalid</code>, only warnings about things that are actually invalid are issued. (This is not fully implemented yet.) With an optional argument of <code>no-ext</code>, warnings about <i>gawk</i> extensions are disabled. </p>
 </dd>
<dt><code>-M</code></dt>
<dd>  </dd>
<dt><code>--bignum</code></dt>
<dd> <p> Force arbitrary precision arithmetic on numbers. This option has no effect if <i>gawk</i> is not compiled to use the GNU MPFR and GMP libraries. (In such a case, <i>gawk</i> issues a warning.) </p>
 </dd>
<dt><code>-n</code></dt>
<dd>  </dd>
<dt><code>--non-decimal-data</code></dt>
<dd> <p> Recognize octal and hexadecimal values in input data. <i>Use this option with great caution!</i> </p>
 </dd>
<dt><code>-N</code></dt>
<dd>  </dd>
<dt><code>--use-lc-numeric</code></dt>
<dd> <p> Force <i>gawk</i> to use the locale&#8217;s decimal point character when parsing input data. Although the POSIX standard requires this behavior, and <i>gawk</i> does so when <code>--posix</code> is in effect, the default is to follow traditional behavior and use a period as the decimal point, even in locales where the period is not the decimal point character. This option overrides the default behavior, without the full draconian strictness of the <code>--posix</code> option. </p>
 </dd>
<dd> <p> <code>-o</code>[<i>file</i>] </p>
 </dd>
<dd> <p> <code>--pretty-print</code>[<code>=</code><i>file</i>] Output a pretty printed version of the program to <i>file</i>. If no <i>file</i> is provided, <i>gawk</i> uses a file named <code>awkprof.out</code> in the current directory. This option implies <code>--no-optimize</code>. </p>
 </dd>
<dt><code>-O</code></dt>
<dd>  </dd>
<dt><code>--optimize</code></dt>
<dd> <p> Enable <i>gawk</i>&#8216;s default optimizations upon the internal representation of the program. Currently, this just includes simple constant folding. This option is on by default. </p>
 </dd>
<dd> <p> <code>-p</code>[<i>prof-file</i>] </p>
 </dd>
<dd> <p> <code>--profile</code>[<code>=</code><i>prof-file</i>] Start a profiling session, and send the profiling data to <i>prof-file</i>. The default is <code>awkprof.out</code>. The profile contains execution counts of each statement in the program in the left margin and function call counts for each user-defined function. This option implies <code>--no-optimize</code>. </p>
 </dd>
<dt><code>-P</code></dt>
<dd>  </dd>
<dt><code>--posix</code></dt>
<dd> <p> This turns on <i>compatibility</i> mode, with the following additional restrictions: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>\x</code> escape sequences are not recognized. </p>
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
<dt><code>-r</code></dt>
<dd>  </dd>
<dt><code>--re-interval</code></dt>
<dd> <p> Enable the use of <i>interval expressions</i> in regular expression matching (see <code>Regular Expressions</code>, below). Interval expressions were not traditionally available in the AWK language. The POSIX standard added them, to make <i>awk</i> and <i>egrep</i> consistent with each other. They are enabled by default, but this option remains for use together with <code>--traditional</code>. </p>
 </dd>
<dt><code>-s</code></dt>
<dd>  </dd>
<dt><code>--no-optimize</code></dt>
<dd> <p> Disable <i>gawk</i>&#8216;s default optimizations upon the internal representation of the program. </p>
 </dd>
<dt><code>-S</code></dt>
<dd>  </dd>
<dt><code>--sandbox</code></dt>
<dd> <p> Run <i>gawk</i> in sandbox mode, disabling the <code>system()</code> function, input redirection with <code>getline</code>, output redirection with <code>print</code> and <code>printf</code>, and loading dynamic extensions. Command execution (through pipelines) is also disabled. This effectively blocks a script from accessing local resources, except for the files specified on the command line. </p>
 </dd>
<dt><code>-t</code></dt>
<dd>  </dd>
<dt><code>--lint-old</code></dt>
<dd> <p> Provide warnings about constructs that are not portable to the original version of UNIX <i>awk</i>. </p>
 </dd>
<dt><code>-V</code></dt>
<dd>  </dd>
<dt><code>--version</code></dt>
<dd> <p> Print version information for this particular copy of <i>gawk</i> on the standard output. This is useful mainly for knowing if the current copy of <i>gawk</i> on your system is up to date with respect to whatever the Free Software Foundation is distributing. This is also useful when reporting bugs. (Per the <i>GNU Coding Standards</i>, these options cause an immediate, successful exit.) </p>
 </dd>
<dt><code>--</code></dt>
<dd> <p> Signal the end of options. This is useful to allow further arguments to the AWK program itself to start with a ``-&#8216;&#8216;. This provides consistency with the argument parsing convention used by most other POSIX programs. </p>
 </dd></dl>
<p> In compatibility mode, any other options are flagged as invalid, but are otherwise ignored. In normal operation, as long as program text has been supplied, unknown options are passed on to the AWK program in the <code>ARGV</code> array for processing. This is particularly useful for running AWK programs via the <code>#!</code> executable interpreter mechanism. </p>
<p> For POSIX compatibility, the <code>-W</code> option may be used, followed by the name of a long option.  </p>
<h2>AWK PROGRAM EXECUTION</h2>
<p> An AWK program consists of a sequence of optional directives, pattern-action statements, and optional function definitions. </p>
<dl>
<dd> <p> <code>@include &quot;</code><i>filename</i><code>&quot; <br/>
 @load &quot;</code><i>filename</i><code>&quot; <br/>
 @namespace &quot;</code><i>name</i><code>&quot; <br/>
 </code><i>pattern</i><code><code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code>{ </code><i>action statements</i><code> }</code><br/>
 <br/>
 <code>function </code><i>name</i><code>(</code><i>parameter list</i><code>) { </code><i>statements</i><code> }</code> </p>
 </dd></dl>
<p> <i>Gawk</i> first reads the program source from the <i>program-file</i>(s) if specified, from arguments to <code>--source</code>, or from the first non-option argument on the command line. The <code>-f</code> and <code>--source</code> options may be used multiple times on the command line. <i>Gawk</i> reads the program text as if all the <i>program-file</i>s and command line source texts had been concatenated together. This is useful for building libraries of AWK functions, without having to include them in each new AWK program that uses them. It also provides the ability to mix library functions with command line programs. </p>
<p> In addition, lines beginning with <code>@include</code> may be used to include other source files into your program, making library use even easier. This is equivalent to using the <code>--include</code> option. </p>
<p> Lines beginning with <code>@load</code> may be used to load extension functions into your program. This is equivalent to using the <code>--load</code> option. </p>
<p> The environment variable <code>AWKPATH</code> specifies a search path to use when finding source files named with the <code>-f</code> and <code>--include</code> options. If this variable does not exist, the default path is <code>&quot;.:/usr/local/share/awk&quot;</code>. (The actual directory may vary, depending upon how <i>gawk</i> was built and installed.) If a file name given to the <code>-f</code> option contains a ``/&#8216;&#8216; character, no path search is performed. </p>
<p> The environment variable <code>AWKLIBPATH</code> specifies a search path to use when finding source files named with the <code>--load</code> option. If this variable does not exist, the default path is <code>&quot;/usr/local/lib/gawk&quot;</code>. (The actual directory may vary, depending upon how <i>gawk</i> was built and installed.) </p>
<p> <i>Gawk</i> executes AWK programs in the following order. First, all variable assignments specified via the <code>-v</code> option are performed. Next, <i>gawk</i> compiles the program into an internal form. Then, <i>gawk</i> executes the code in the <code>BEGIN</code> rule(s) (if any), and then proceeds to read each file named in the <code>ARGV</code> array (up to <code>ARGV[ARGC-1]</code>). If there are no files named on the command line, <i>gawk</i> reads the standard input. </p>
<p> If a filename on the command line has the form <i>var</i><code>=</code><i>val</i> it is treated as a variable assignment. The variable <i>var</i> will be assigned the value <i>val</i>. (This happens after any <code>BEGIN</code> rule(s) have been run.) Command line variable assignment is most useful for dynamically assigning values to the variables AWK uses to control how input is broken into fields and records. It is also useful for controlling state if multiple passes are needed over a single data file. </p>
<p> If the value of a particular element of <code>ARGV</code> is empty (<code>&quot;&quot;</code>), <i>gawk</i> skips over it. </p>
<p> For each input file, if a <code>BEGINFILE</code> rule exists, <i>gawk</i> executes the associated code before processing the contents of the file. Similarly, <i>gawk</i> executes the code associated with <code>ENDFILE</code> after processing the file. </p>
<p> For each record in the input, <i>gawk</i> tests to see if it matches any <i>pattern</i> in the AWK program. For each pattern that the record matches, <i>gawk</i> executes the associated <i>action</i>. The patterns are tested in the order they occur in the program. </p>
<p> Finally, after all the input is exhausted, <i>gawk</i> executes the code in the <code>END</code> rule(s) (if any).  </p>
<h3>Command Line Directories</h3>
<p> According to POSIX, files named on the <i>awk</i> command line must be text files. The behavior is ``undefined&#8217;&#8216; if they are not. Most versions of <i>awk</i> treat a directory on the command line as a fatal error. </p>
<p> Starting with version 4.0 of <i>gawk</i>, a directory on the command line produces a warning, but is otherwise skipped. If either of the <code>--posix</code> or <code>--traditional</code> options is given, then <i>gawk</i> reverts to treating directories on the command line as a fatal error.  </p>
<h2>VARIABLES, RECORDS AND FIELDS</h2>
<p> AWK variables are dynamic; they come into existence when they are first used. Their values are either floating-point numbers or strings, or both, depending upon how they are used. Additionally, <i>gawk</i> allows variables to have regular-expression type. AWK also has one dimensional arrays; arrays with multiple dimensions may be simulated. <i>Gawk</i> provides true arrays of arrays; see <code>Arrays</code>, below. Several pre-defined variables are set as a program runs; these are described as needed and summarized below.  </p>
<h3>Records</h3>
<p> Normally, records are separated by newline characters. You can control how records are separated by assigning values to the built-in variable <code>RS</code>. If <code>RS</code> is any single character, that character separates records. Otherwise, <code>RS</code> is a regular expression. Text in the input that matches this regular expression separates the record. However, in compatibility mode, only the first character of its string value is used for separating records. If <code>RS</code> is set to the null string, then records are separated by empty lines. When <code>RS</code> is set to the null string, the newline character always acts as a field separator, in addition to whatever value <code>FS</code> may have.  </p>
<h3>Fields</h3>
<p> As each input record is read, <i>gawk</i> splits the record into <i>fields</i>, using the value of the <code>FS</code> variable as the field separator. If <code>FS</code> is a single character, fields are separated by that character. If <code>FS</code> is the null string, then each individual character becomes a separate field. Otherwise, <code>FS</code> is expected to be a full regular expression. In the special case that <code>FS</code> is a single space, fields are separated by runs of spaces and/or tabs and/or newlines. <code>NOTE</code>: The value of <code>IGNORECASE</code> (see below) also affects how fields are split when <code>FS</code> is a regular expression, and how records are separated when <code>RS</code> is a regular expression. </p>
<p> If the <code>FIELDWIDTHS</code> variable is set to a space-separated list of numbers, each field is expected to have fixed width, and <i>gawk</i> splits up the record using the specified widths. Each field width may optionally be preceded by a colon-separated value specifying the number of characters to skip before the field starts. The value of <code>FS</code> is ignored. Assigning a new value to <code>FS</code> or <code>FPAT</code> overrides the use of <code>FIELDWIDTHS</code>. </p>
<p> Similarly, if the <code>FPAT</code> variable is set to a string representing a regular expression, each field is made up of text that matches that regular expression. In this case, the regular expression describes the fields themselves, instead of the text that separates the fields. Assigning a new value to <code>FS</code> or <code>FIELDWIDTHS</code> overrides the use of <code>FPAT</code>. </p>
<p> Each field in the input record may be referenced by its position: <code>$1</code>, <code>$2</code>, and so on. <code>$0</code> is the whole record, including leading and trailing whitespace. Fields need not be referenced by constants: </p>
<dl>
<dd> <p> <code> n = 5 <br/>
 print $n </code> </p>
 </dd></dl>
<p> prints the fifth field in the input record. </p>
<p> The variable <code>NF</code> is set to the total number of fields in the input record. </p>
<p> References to non-existent fields (i.e., fields after <code>$NF</code>) produce the null string. However, assigning to a non-existent field (e.g., <code>$(NF+2) = 5</code>) increases the value of <code>NF</code>, creates any intervening fields with the null string as their values, and causes the value of <code>$0</code> to be recomputed, with the fields being separated by the value of <code>OFS</code>. References to negative numbered fields cause a fatal error. Decrementing <code>NF</code> causes the values of fields past the new value to be lost, and the value of <code>$0</code> to be recomputed, with the fields being separated by the value of <code>OFS</code>. </p>
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
<dd> <p> An array containing the values of the current environment. The array is indexed by the environment variables, each element being the value of that variable (e.g., <code>ENVIRON[&quot;HOME&quot;]</code> might be <code>&quot;/home/arnold&quot;</code>). </p>
<p> In POSIX mode, changing this array does not affect the environment seen by programs which <i>gawk</i> spawns via redirection or the <code>system()</code> function. Otherwise, <i>gawk</i> updates its real environment so that programs it spawns see the changes. </p>
 </dd>
<dt><code>ERRNO</code></dt>
<dd> <p> If a system error occurs either doing a redirection for <code>getline</code>, during a read for <code>getline</code>, or during a <code>close()</code>, then <code>ERRNO</code> is set to a string describing the error. The value is subject to translation in non-English locales. If the string in <code>ERRNO</code> corresponds to a system error in the <i><a href="/docs/linux/man/3-errno/">errno</a></i>(3) variable, then the numeric value can be found in <code>PROCINFO[errno].</code> For non-system errors, <code>PROCINFO[errno]</code> will be zero. </p>
 </dd>
<dt><code>FIELDWIDTHS</code></dt>
<dd> <p> A whitespace-separated list of field widths. When set, <i>gawk</i> parses the input into fields of fixed width, instead of using the value of the <code>FS</code> variable as the field separator. Each field width may optionally be preceded by a colon-separated value specifying the number of characters to skip before the field starts. See <code>Fields</code>, above. </p>
 </dd>
<dt><code>FILENAME</code></dt>
<dd> <p> The name of the current input file. If no files are specified on the command line, the value of <code>FILENAME</code> is ``-&#8216;&#8216;. However, <code>FILENAME</code> is undefined inside the <code>BEGIN</code> rule (unless set by <code>getline</code>). </p>
 </dd>
<dt><code>FNR</code></dt>
<dd> <p> The input record number in the current input file. </p>
 </dd>
<dt><code>FPAT</code></dt>
<dd> <p> A regular expression describing the contents of the fields in a record. When set, <i>gawk</i> parses the input into fields, where the fields match the regular expression, instead of using the value of <code>FS</code> as the field separator. See <code>Fields</code>, above. </p>
 </dd>
<dt><code>FS</code></dt>
<dd> <p> The input field separator, a space by default. See <code>Fields</code>, above. </p>
 </dd>
<dt><code>FUNCTAB</code></dt>
<dd> <p> An array whose indices and corresponding values are the names of all the user-defined or extension functions in the program. <code>NOTE</code>: You may not use the <code>delete</code> statement with the <code>FUNCTAB</code> array. </p>
 </dd>
<dt><code>IGNORECASE</code></dt>
<dd> <p> Controls the case-sensitivity of all regular expression and string operations. If <code>IGNORECASE</code> has a non-zero value, then string comparisons and pattern matching in rules, field splitting with <code>FS</code> and <code>FPAT</code>, record separating with <code>RS</code>, regular expression matching with <code>~</code> and <code>!~</code>, and the <code>gensub()</code>, <code>gsub()</code>, <code>index()</code>, <code>match()</code>, <code>patsplit()</code>, <code>split()</code>, and <code>sub()</code> built-in functions all ignore case when doing regular expression operations. <code>NOTE</code>: Array subscripting is <i>not</i> affected. However, the <code>asort()</code> and <code>asorti()</code> functions are affected. </p>
<p> Thus, if <code>IGNORECASE</code> is not equal to zero, <code>/aB/</code> matches all of the strings <code>&quot;ab&quot;</code>, <code>&quot;aB&quot;</code>, <code>&quot;Ab&quot;</code>, and <code>&quot;AB&quot;</code>. As with all AWK variables, the initial value of <code>IGNORECASE</code> is zero, so all regular expression and string operations are normally case-sensitive. </p>
 </dd>
<dt><code>LINT</code></dt>
<dd> <p> Provides dynamic control of the <code>--lint</code> option from within an AWK program. When true, <i>gawk</i> prints lint warnings. When false, it does not. The values allowed for the <code>--lint</code> option may also be assigned to <code>LINT</code>, with the same effects. Any other true value just prints warnings. </p>
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
<dt><code>PREC</code></dt>
<dd> <p> The working precision of arbitrary precision floating-point numbers, 53 by default. </p>
 </dd>
<dt><code>PROCINFO</code></dt>
<dd> <p> The elements of this array provide access to information about the running AWK program. On some systems, there may be elements in the array, <code>&quot;group1&quot;</code> through <code>&quot;group</code><i>n</i><code>&quot;</code> for some <i>n</i>, which is the number of supplementary groups that the process has. Use the <code>in</code> operator to test for these elements. The following elements are guaranteed to be available: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>PROCINFO[&quot;argv&quot;]</code></dt>
<dd> <p> The command line arguments as received by <i>gawk</i> at the C-language level. The subscripts start from zero. </p>
 </dd>
<dt><code>PROCINFO[&quot;egid&quot;]</code></dt>
<dd> <p> The value of the <i><a href="/docs/linux/man/2-getegid/">getegid</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;errno&quot;]</code></dt>
<dd> <p> The value of <i><a href="/docs/linux/man/3-errno/">errno</a></i>(3) when <code>ERRNO</code> is set to the associated error message. </p>
 </dd>
<dt><code>PROCINFO[&quot;euid&quot;]</code></dt>
<dd> <p> The value of the <i><a href="/docs/linux/man/2-geteuid/">geteuid</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;FS&quot;]</code></dt>
<dd> <p> <code>&quot;FS&quot;</code> if field splitting with <code>FS</code> is in effect, <code>&quot;FPAT&quot;</code> if field splitting with <code>FPAT</code> is in effect, <code>&quot;FIELDWIDTHS&quot;</code> if field splitting with <code>FIELDWIDTHS</code> is in effect, or <code>&quot;API&quot;</code> if API input parser field splitting is in effect. </p>
 </dd>
<dt><code>PROCINFO[&quot;gid&quot;]</code></dt>
<dd> <p> The value of the <i><a href="/docs/linux/man/2-getgid/">getgid</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;identifiers&quot;]</code></dt>
<dd> <p> A subarray, indexed by the names of all identifiers used in the text of the AWK program. The values indicate what <i>gawk</i> knows about the identifiers after it has finished parsing the program; they are <i>not</i> updated while the program runs. For each identifier, the value of the element is one of the following: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>&quot;array&quot;</code></dt>
<dd> <p> The identifier is an array. </p>
 </dd>
<dt><code>&quot;builtin&quot;</code></dt>
<dd> <p> The identifier is a built-in function. </p>
 </dd>
<dt><code>&quot;extension&quot;</code></dt>
<dd> <p> The identifier is an extension function loaded via <code>@load</code> or <code>--load</code>. </p>
 </dd>
<dt><code>&quot;scalar&quot;</code></dt>
<dd> <p> The identifier is a scalar. </p>
 </dd>
<dt><code>&quot;untyped&quot;</code></dt>
<dd> <p> The identifier is untyped (could be used as a scalar or array, <i>gawk</i> doesn&#8217;t know yet). </p>
 </dd>
<dt><code>&quot;user&quot;</code></dt>
<dd> <p> The identifier is a user-defined function. </p>
 </dd></dl>
</dl>
<dt><code>PROCINFO[&quot;pgrpid&quot;]</code></dt>
<dd> <p> The value of the <i><a href="/docs/linux/man/2-getpgrp/">getpgrp</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;pid&quot;]</code></dt>
<dd> <p> The value of the <i><a href="/docs/linux/man/2-getpid/">getpid</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;platform&quot;]</code></dt>
<dd> <p> A string indicating the platform for which <i>gawk</i> was compiled. It is one of: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>&quot;djgpp&quot;</code>, <code>&quot;mingw&quot;</code></dt>
<dd> <p> Microsoft Windows, using either DJGPP, or MinGW, respectively. </p>
 </dd>
<dt><code>&quot;os2&quot;</code></dt>
<dd> <p> OS/2. </p>
 </dd>
<dt><code>&quot;posix&quot;</code></dt>
<dd> <p> GNU/Linux, Cygwin, Mac OS X, and legacy Unix systems. </p>
 </dd>
<dt><code>&quot;vms&quot;</code></dt>
<dd> <p> OpenVMS or Vax/VMS. </p>
 </dd></dl>
</dl>
<dt><code>PROCINFO[&quot;ppid&quot;]</code></dt>
<dd> <p> The value of the <i><a href="/docs/linux/man/2-getppid/">getppid</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;strftime&quot;]</code></dt>
<dd> <p> The default time format string for <code>strftime()</code>. Changing its value affects how <code>strftime()</code> formats time values when called with no arguments. </p>
 </dd>
<dt><code>PROCINFO[&quot;uid&quot;]</code></dt>
<dd> <p> The value of the <i><a href="/docs/linux/man/2-getuid/">getuid</a></i>(2) system call. </p>
 </dd>
<dt><code>PROCINFO[&quot;version&quot;]</code></dt>
<dd> <p> The version of <i>gawk</i>. </p>
 </dd></dl>
<p> The following elements are present if loading dynamic extensions is available: </p>
<dl>
<dt><code>PROCINFO[&quot;api_major&quot;]</code></dt>
<dd> <p> The major version of the extension API. </p>
 </dd>
<dt><code>PROCINFO[&quot;api_minor&quot;]</code></dt>
<dd> <p> The minor version of the extension API. </p>
 </dd></dl>
<p> The following elements are available if MPFR support is compiled into <i>gawk</i>: </p>
<dl>
<dt><code>PROCINFO[&quot;gmp_version&quot;]</code></dt>
<dd> <p> The version of the GNU GMP library used for arbitrary precision number support in <i>gawk</i>. </p>
 </dd>
<dt><code>PROCINFO[&quot;mpfr_version&quot;]</code></dt>
<dd> <p> The version of the GNU MPFR library used for arbitrary precision number support in <i>gawk</i>. </p>
 </dd>
<dt><code>PROCINFO[&quot;prec_max&quot;]</code></dt>
<dd> <p> The maximum precision supported by the GNU MPFR library for arbitrary precision floating-point numbers. </p>
 </dd>
<dt><code>PROCINFO[&quot;prec_min&quot;]</code></dt>
<dd> <p> The minimum precision allowed by the GNU MPFR library for arbitrary precision floating-point numbers. </p>
 </dd></dl>
<p> The following elements may set by a program to change <i>gawk</i>&#8216;s behavior: </p>
<dl>
<dt><code>PROCINFO[&quot;NONFATAL&quot;]</code></dt>
<dd> <p> If this exists, then I/O errors for all redirections become nonfatal. </p>
 </dd>
<dt><code>PROCINFO[&quot;</code><i>name</i><code>&quot;, &quot;NONFATAL&quot;]</code></dt>
<dd> <p> Make I/O errors for <i>name</i> be nonfatal. </p>
 </dd>
<dt><code>PROCINFO[&quot;</code><i>command</i><code>&quot;, &quot;pty&quot;]</code></dt>
<dd> <p> Use a pseudo-tty for two-way communication with <i>command</i> instead of setting up two one-way pipes. </p>
 </dd>
<dt><code>PROCINFO[&quot;</code><i>input</i><code>&quot;, &quot;READ_TIMEOUT&quot;]</code></dt>
<dd> <p> The timeout in milliseconds for reading data from <i>input</i>, where <i>input</i> is a redirection string or a filename. A value of zero or less than zero means no timeout. </p>
 </dd>
<dt><code>PROCINFO[&quot;</code><i>input</i><code>&quot;, &quot;RETRY&quot;]</code></dt>
<dd> <p> If an I/O error that may be retried occurs when reading data from <i>input</i>, and this array entry exists, then <code>getline</code> returns -2 instead of following the default behavior of returning -1 and configuring <i>input</i> to return no further data. An I/O error that may be retried is one where <i><a href="/docs/linux/man/3-errno/">errno</a></i>(3) has the value EAGAIN, EWOULDBLOCK, EINTR, or ETIMEDOUT. This may be useful in conjunction with <code>PROCINFO[&quot;</code><i>input</i><code>&quot;, &quot;READ_TIMEOUT&quot;]</code> or in situations where a file descriptor has been configured to behave in a non-blocking fashion. </p>
 </dd>
<dt><code>PROCINFO[&quot;sorted_in&quot;]</code></dt>
<dd> <p> If this element exists in <code>PROCINFO</code>, then its value controls the order in which array elements are traversed in <code>for</code> loops. Supported values are <code>&quot;@ind_str_asc&quot;</code>, <code>&quot;@ind_num_asc&quot;</code>, <code>&quot;@val_type_asc&quot;</code>, <code>&quot;@val_str_asc&quot;</code>, <code>&quot;@val_num_asc&quot;</code>, <code>&quot;@ind_str_desc&quot;</code>, <code>&quot;@ind_num_desc&quot;</code>, <code>&quot;@val_type_desc&quot;</code>, <code>&quot;@val_str_desc&quot;</code>, <code>&quot;@val_num_desc&quot;</code>, and <code>&quot;@unsorted&quot;</code>. The value can also be the name (as a <i>string</i>) of any comparison function defined as follows: </p>
<p> <code>function cmp_func(i1, v1, i2, v2)</code> </p>
<p> where <i>i1</i> and <i>i2</i> are the indices, and <i>v1</i> and <i>v2</i> are the corresponding values of the two elements being compared. It should return a number less than, equal to, or greater than 0, depending on how the elements of the array are to be ordered. </p>
 </dd></dl>
</dl>
<dt><code>ROUNDMODE</code></dt>
<dd> <p> The rounding mode to use for arbitrary precision arithmetic on numbers, by default <code>&quot;N&quot;</code> (IEEE-754 roundTiesToEven mode). The accepted values are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>&quot;A&quot;</code> or <code>&quot;a&quot;</code></dt>
<dd> <p> for rounding away from zero. These are only available if your version of the GNU MPFR library supports rounding away from zero. </p>
 </dd>
<dt><code>&quot;D&quot;</code> or <code>&quot;d&quot;</code></dt>
<dd> <p> for roundTowardNegative. </p>
 </dd>
<dt><code>&quot;N&quot;</code> or <code>&quot;n&quot;</code></dt>
<dd> <p> for roundTiesToEven. </p>
 </dd>
<dt><code>&quot;U&quot;</code> or <code>&quot;u&quot;</code></dt>
<dd> <p> for roundTowardPositive. </p>
 </dd>
<dt><code>&quot;Z&quot;</code> or <code>&quot;z&quot;</code></dt>
<dd> <p> for roundTowardZero. </p>
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
<dd> <p> The string used to separate multiple subscripts in array elements, by default <code>&quot;\034&quot;</code>. </p>
 </dd>
<dt><code>SYMTAB</code></dt>
<dd> <p> An array whose indices are the names of all currently defined global variables and arrays in the program. The array may be used for indirect access to read or write the value of a variable: </p>
<pre><code>foo = 5
SYMTAB[&quot;foo&quot;] = 4
print foo # prints 4
</code></pre>
<p> The <code>typeof()</code> function may be used to test if an element in <code>SYMTAB</code> is an array. You may not use the <code>delete</code> statement with the <code>SYMTAB</code> array, nor assign to elements with an index that is not a variable name. </p>
 </dd>
<dt><code>TEXTDOMAIN</code></dt>
<dd> <p> The text domain of the AWK program; used to find the localized translations for the program&#8217;s strings. </p>
 </dd></dl>
<h3>Arrays</h3>
<p> Arrays are subscripted with an expression between square brackets (<code>[</code> and <code>]</code>). If the expression is an expression list (<i>expr</i>, <i>expr</i> ...) then the array subscript is a string consisting of the concatenation of the (string) value of each expression, separated by the value of the <code>SUBSEP</code> variable. This facility is used to simulate multiply dimensioned arrays. For example: </p>
<dl>
<dd> <p> <code> i = &quot;A&quot;; j = &quot;B&quot;; k = &quot;C&quot; <br/>
 x[i, j, k] = &quot;hello, world\n&quot; </code> </p>
 </dd></dl>
<p> assigns the string <code>&quot;hello, world\n&quot;</code> to the element of the array <code>x</code> which is indexed by the string <code>&quot;A\034B\034C&quot;</code>. All arrays in AWK are associative, i.e., indexed by string values. </p>
<p> The special operator <code>in</code> may be used to test if an array has an index consisting of a particular value: </p>
<dl>
<dd> <pre><code>if (val in array)
        print array[val]
</code></pre>
 </dd></dl>
<p> If the array has multiple subscripts, use <code>(i, j) in array</code>. </p>
<p> The <code>in</code> construct may also be used in a <code>for</code> loop to iterate over all the elements of an array. However, the <code>(i, j) in array</code> construct only works in tests, not in <code>for</code> loops. </p>
<p> An element may be deleted from an array using the <code>delete</code> statement. The <code>delete</code> statement may also be used to delete the entire contents of an array, just by specifying the array name without a subscript. </p>
<p> <i>gawk</i> supports true multidimensional arrays. It does not require that such arrays be ``rectangular&#8217;&#8216; as in C or C++. For example: </p>
<dl>
<dd> <pre><code>a[1] = 5
a[2][1] = 6
a[2][2] = 7
</code></pre>
 </dd></dl>
<p> <code>NOTE</code>: You may need to tell <i>gawk</i> that an array element is really a subarray in order to use it where <i>gawk</i> expects an array (such as in the second argument to <code>split()</code>). You can do this by creating an element in the subarray and then deleting it with the <code>delete</code> statement.  </p>
<h3>Namespaces</h3>
<p> <i>Gawk</i> provides a simple <i>namespace</i> facility to help work around the fact that all variables in AWK are global. </p>
<p> A <i>qualified name</i> consists of a two simple identifiers joined by a double colon (<code>::</code>). The left-hand identifier represents the namespace and the right-hand identifier is the variable within it. All simple (non-qualified) names are considered to be in the ``current&#8217;&#8216; namespace; the default namespace is <code>awk</code>. However, simple identifiers consisting solely of uppercase letters are forced into the <code>awk</code> namespace, even if the current namespace is different. </p>
<p> You change the current namespace with an <code>@namespace &quot;</code><i>name</i><code>&quot;</code> directive. </p>
<p> The standard predefined builtin function names may not be used as namespace names. The names of additional functions provided by <i>gawk</i> may be used as namespace names or as simple identifiers in other namespaces. For more details, see <i>GAWK: Effective AWK Programming</i>.  </p>
<h3>Variable Typing And Conversion</h3>
<p> Variables and fields may be (floating point) numbers, or strings, or both. They may also be regular expressions. How the value of a variable is interpreted depends upon its context. If used in a numeric expression, it will be treated as a number; if used as a string it will be treated as a string. </p>
<p> To force a variable to be treated as a number, add zero to it; to force it to be treated as a string, concatenate it with the null string. </p>
<p> Uninitialized variables have the numeric value zero and the string value &quot;&quot; (the null, or empty, string). </p>
<p> When a string must be converted to a number, the conversion is accomplished using <i><a href="/docs/linux/man/3-strtod/">strtod</a></i>(3). A number is converted to a string by using the value of <code>CONVFMT</code> as a format string for <i><a href="/docs/linux/man/3-sprintf/">sprintf</a></i>(3), with the numeric value of the variable as the argument. However, even though all numbers in AWK are floating-point, integral values are <i>always</i> converted as integers. Thus, given </p>
<dl>
<dd> <pre><code>CONVFMT = &quot;%2.2f&quot;
a = 12
b = a &quot;&quot;
</code></pre>
 </dd></dl>
<p> the variable <code>b</code> has a string value of <code>&quot;12&quot;</code> and not <code>&quot;12.00&quot;</code>. </p>
<p> <code>NOTE</code>: When operating in POSIX mode (such as with the <code>--posix</code> option), beware that locale settings may interfere with the way decimal numbers are treated: the decimal separator of the numbers you are feeding to <i>gawk</i> must conform to what your locale would expect, be it a comma (,) or a period (.). </p>
<p> <i>Gawk</i> performs comparisons as follows: If two variables are numeric, they are compared numerically. If one value is numeric and the other has a string value that is a ``numeric string,&#8216;&#8216; then comparisons are also done numerically. Otherwise, the numeric value is converted to a string and a string comparison is performed. Two strings are compared, of course, as strings. </p>
<p> Note that string constants, such as <code>&quot;57&quot;</code>, are <i>not</i> numeric strings, they are string constants. The idea of ``numeric string&#8217;&#8216; only applies to fields, <code>getline</code> input, <code>FILENAME</code>, <code>ARGV</code> elements, <code>ENVIRON</code> elements and the elements of an array created by <code>split()</code> or <code>patsplit()</code> that are numeric strings. The basic idea is that <i>user input</i>, and only user input, that looks numeric, should be treated that way.  </p>
<h3>Octal and Hexadecimal Constants</h3>
<p> You may use C-style octal and hexadecimal constants in your AWK program source code. For example, the octal value <code>011</code> is equal to decimal <code>9</code>, and the hexadecimal value <code>0x11</code> is equal to decimal 17.  </p>
<h3>String Constants</h3>
<p> String constants in AWK are sequences of characters enclosed between double quotes (like <code>&quot;value&quot;</code>). Within strings, certain <i>escape sequences</i> are recognized, as in C. These are: </p>
<dl>
<dt><code>\\</code></dt>
<dd> <p> A literal backslash. </p>
 </dd>
<dt><code>\a</code></dt>
<dd> <p> The ``alert&#8217;&#8216; character; usually the ASCII BEL character. </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> Backspace. </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> Form-feed. </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> Newline. </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> Carriage return. </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> Horizontal tab. </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> Vertical tab. </p>
 </dd>
<dt><code>\x</code><i>hex digits</i></dt>
<dd> <p> The character represented by the string of hexadecimal digits following the <code>\x</code>. Up to two following hexadecimal digits are considered part of the escape sequence. E.g., <code>&quot;\x1B&quot;</code> is the ASCII ESC (escape) character. </p>
 </dd>
<dt><code>\</code><i>ddd</i></dt>
<dd> <p> The character represented by the 1-, 2-, or 3-digit sequence of octal digits. E.g., <code>&quot;\033&quot;</code> is the ASCII ESC (escape) character. </p>
 </dd>
<dt><code>\</code><i>c</i></dt>
<dd> <p> The literal character <i>c</i>. </p>
 </dd></dl>
<p> In compatibility mode, the characters represented by octal and hexadecimal escape sequences are treated literally when used in regular expression constants. Thus, <code>/a\52b/</code> is equivalent to <code>/a\*b/</code>.  </p>
<h3>Regexp Constants</h3>
<p> A regular expression constant is a sequence of characters enclosed between forward slashes (like <code>/value/</code>). Regular expression matching is described more fully below; see <code>Regular Expressions</code>. </p>
<p> The escape sequences described earlier may also be used inside constant regular expressions (e.g., <code>/[&nbsp;\t\f\n\r\v]/</code> matches whitespace characters). </p>
<p> <i>Gawk</i> provides <i>strongly typed</i> regular expression constants. These are written with a leading <code>@</code> symbol (like so: <code>@/value/</code>). Such constants may be assigned to scalars (variables, array elements) and passed to user-defined functions. Variables that have been so assigned have regular expression type.  </p>
<h2>PATTERNS AND ACTIONS</h2>
<p> AWK is a line-oriented language. The pattern comes first, and then the action. Action statements are enclosed in <code>{</code> and <code>}</code>. Either the pattern may be missing, or the action may be missing, but, of course, not both. If the pattern is missing, the action executes for every single record of input. A missing action is equivalent to </p>
<dl>
<dd> <p> <code>{ print }</code> </p>
 </dd></dl>
<p> which prints the entire record. </p>
<p> Comments begin with the <code>#</code> character, and continue until the end of the line. Empty lines may be used to separate statements. Normally, a statement ends with a newline, however, this is not the case for lines ending in a comma, <code>{</code>, <code>?</code>, <code>:</code>, <code>&amp;&amp;</code>, or <code>||</code>. Lines ending in <code>do</code> or <code>else</code> also have their statements automatically continued on the following line. In other cases, a line can be continued by ending it with a ``\&#8216;&#8216;, in which case the newline is ignored. However, a ``\&#8216;&#8216; after a <code>#</code> is not special. </p>
<p> Multiple statements may be put on one line by separating them with a ``;&#8216;&#8216;. This applies to both the statements within the action part of a pattern-action pair (the usual case), and to the pattern-action statements themselves.  </p>
<h3>Patterns</h3>
<p> AWK patterns may be one of the following: </p>
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
<p> <code>BEGIN</code> and <code>END</code> are two special kinds of patterns which are not tested against the input. The action parts of all <code>BEGIN</code> patterns are merged as if all the statements had been written in a single <code>BEGIN</code> rule. They are executed before any of the input is read. Similarly, all the <code>END</code> rules are merged, and executed when all the input is exhausted (or when an <code>exit</code> statement is executed). <code>BEGIN</code> and <code>END</code> patterns cannot be combined with other patterns in pattern expressions. <code>BEGIN</code> and <code>END</code> patterns cannot have missing action parts. </p>
<p> <code>BEGINFILE</code> and <code>ENDFILE</code> are additional special patterns whose actions are executed before reading the first record of each command-line input file and after reading the last record of each file. Inside the <code>BEGINFILE</code> rule, the value of <code>ERRNO</code> is the empty string if the file was opened successfully. Otherwise, there is some problem with the file and the code should use <code>nextfile</code> to skip it. If that is not done, <i>gawk</i> produces its usual fatal error for files that cannot be opened. </p>
<p> For <code>/</code><i>regular expression</i><code>/</code> patterns, the associated statement is executed for each input record that matches the regular expression. Regular expressions are the same as those in <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1), and are summarized below. </p>
<p> A <i>relational expression</i> may use any of the operators defined below in the section on actions. These generally test whether certain fields match certain regular expressions. </p>
<p> The <code>&amp;&amp;</code>, <code>||</code>, and <code>!</code> operators are logical AND, logical OR, and logical NOT, respectively, as in C. They do short-circuit evaluation, also as in C, and are used for combining more primitive pattern expressions. As in most languages, parentheses may be used to change the order of evaluation. </p>
<p> The <code>?:</code> operator is like the same operator in C. If the first pattern is true then the pattern used for testing is the second pattern, otherwise it is the third. Only one of the second and third patterns is evaluated. </p>
<p> The <i>pattern1</i><code>, </code><i>pattern2</i> form of an expression is called a <i>range pattern</i>. It matches all input records starting with a record that matches <i>pattern1</i>, and continuing until a record that matches <i>pattern2</i>, inclusive. It does not combine with any other sort of pattern expression.  </p>
<h3>Regular Expressions</h3>
<p> Regular expressions are the extended kind found in <i>egrep</i>. They are composed of characters as follows: </p>
<dl>
<dt><i>c</i></dt>
<dd> <p> Matches the non-metacharacter <i>c</i>. </p>
 </dd>
<dt><i>\c</i></dt>
<dd> <p> Matches the literal character <i>c</i>. </p>
 </dd>
<dt><code>.</code></dt>
<dd> <p> Matches any character <i>including</i> newline. </p>
 </dd>
<dt><code>^</code></dt>
<dd> <p> Matches the beginning of a string. </p>
 </dd>
<dt><code>$</code></dt>
<dd> <p> Matches the end of a string. </p>
 </dd>
<dt><code>[</code><i>abc...</i><code>]</code></dt>
<dd> <p> A character list: matches any of the characters <i>abc...</i>. You may include a range of characters by separating them with a dash. To include a literal dash in the list, put it first or last. </p>
 </dd>
<dt><code>[^</code><i>abc...</i><code>]</code></dt>
<dd> <p> A negated character list: matches any character except <i>abc...</i>. </p>
 </dd>
<dt><i>r1</i><code>|</code><i>r2</i></dt>
<dd> <p> Alternation: matches either <i>r1</i> or <i>r2</i>. </p>
 </dd>
<dt><i>r1r2</i></dt>
<dd> <p> Concatenation: matches <i>r1</i>, and then <i>r2</i>. </p>
 </dd>
<dt><i>r</i><code>+</code></dt>
<dd> <p> Matches one or more <i>r</i>&#8216;s. </p>
 </dd>
<dt><i>r</i><code>*</code></dt>
<dd> <p> Matches zero or more <i>r</i>&#8216;s. </p>
 </dd>
<dt><i>r</i><code>?</code></dt>
<dd> <p> Matches zero or one <i>r</i>&#8216;s. </p>
 </dd>
<dt><code>(</code><i>r</i><code>)</code></dt>
<dd> <p> Grouping: matches <i>r</i>. </p>
 </dd>
<dd> <p> <i>r</i><code>{</code><i>n</i><code>}</code> </p>
 </dd>
<dd> <p> <i>r</i><code>{</code><i>n</i><code>,}</code> </p>
 </dd>
<dd> <p> <i>r</i><code>{</code><i>n</i><code>,</code><i>m</i><code>}</code> One or two numbers inside braces denote an <i>interval expression</i>. If there is one number in the braces, the preceding regular expression <i>r</i> is repeated <i>n</i> times. If there are two numbers separated by a comma, <i>r</i> is repeated <i>n</i> to <i>m</i> times. If there is one number followed by a comma, then <i>r</i> is repeated at least <i>n</i> times. </p>
 </dd>
<dt><code>\y</code></dt>
<dd> <p> Matches the empty string at either the beginning or the end of a word. </p>
 </dd>
<dt><code>\B</code></dt>
<dd> <p> Matches the empty string within a word. </p>
 </dd>
<dt><code>\&lt;</code></dt>
<dd> <p> Matches the empty string at the beginning of a word. </p>
 </dd>
<dt><code>\&gt;</code></dt>
<dd> <p> Matches the empty string at the end of a word. </p>
 </dd>
<dt><code>\s</code></dt>
<dd> <p> Matches any whitespace character. </p>
 </dd>
<dt><code>\S</code></dt>
<dd> <p> Matches any nonwhitespace character. </p>
 </dd>
<dt><code>\w</code></dt>
<dd> <p> Matches any word-constituent character (letter, digit, or underscore). </p>
 </dd>
<dt><code>\W</code></dt>
<dd> <p> Matches any character that is not word-constituent. </p>
 </dd>
<dt><code>\`</code></dt>
<dd> <p> Matches the empty string at the beginning of a buffer (string). </p>
 </dd>
<dt><code>\&#8216;</code></dt>
<dd> <p> Matches the empty string at the end of a buffer. </p>
 </dd></dl>
<p> The escape sequences that are valid in string constants (see <code>String Constants</code>) are also valid in regular expressions. </p>
<p> <i>Character classes</i> are a feature introduced in the POSIX standard. A character class is a special notation for describing lists of characters that have a specific attribute, but where the actual characters themselves can vary from country to country and/or from character set to character set. For example, the notion of what is an alphabetic character differs in the USA and in France. </p>
<p> A character class is only valid in a regular expression <i>inside</i> the brackets of a character list. Character classes consist of <code>[:</code>, a keyword denoting the class, and <code>:]</code>. The character classes defined by the POSIX standard are: </p>
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
<p> For example, before the POSIX standard, to match alphanumeric characters, you would have had to write <code>/[A-Za-z0-9]/</code>. If your character set had other alphabetic characters in it, this would not match them, and if your character set collated differently from ASCII, this might not even match the ASCII alphanumeric characters. With the POSIX character classes, you can write <code>/[[:alnum:]]/</code>, and this matches the alphabetic and numeric characters in your character set, no matter what it is. </p>
<p> Two additional special sequences can appear in character lists. These apply to non-ASCII character sets, which can have single symbols (called <i>collating elements</i>) that are represented with more than one character, as well as several characters that are equivalent for <i>collating</i>, or sorting, purposes. (E.g., in French, a plain ``e&#8217;&#8216; and a grave-accented ``e`&#8216;&#8216; are equivalent.) </p>
<dl>
<dt>Collating Symbols</dt>
<dd> <p> A collating symbol is a multi-character collating element enclosed in <code>[.</code> and <code>.]</code>. For example, if <code>ch</code> is a collating element, then <code>[[.ch.]]</code> is a regular expression that matches this collating element, while <code>[ch]</code> is a regular expression that matches either <code>c</code> or <code>h</code>. </p>
 </dd>
<dt>Equivalence Classes</dt>
<dd> <p> An equivalence class is a locale-specific name for a list of characters that are equivalent. The name is enclosed in <code>[=</code> and <code>=]</code>. For example, the name <code>e</code> might be used to represent all of ``e&#8217;&#8216;, ``e&#8217;&#8216;&#8216;, and ``e`&#8216;&#8216;. In this case, <code>[[=e=]]</code> is a regular expression that matches any of <code>e</code>, <code>e&#8217;</code>, or <code>e`</code>. </p>
 </dd></dl>
<p> These features are very valuable in non-English speaking locales. The library functions that <i>gawk</i> uses for regular expression matching currently only recognize POSIX character classes; they do not recognize collating symbols or equivalence classes. </p>
<p> The <code>\y</code>, <code>\B</code>, <code>\&lt;</code>, <code>\&gt;</code>, <code>\s</code>, <code>\S</code>, <code>\w</code>, <code>\W</code>, <code>\`</code>, and <code>\&#8216;</code> operators are specific to <i>gawk</i>; they are extensions based on facilities in the GNU regular expression libraries. </p>
<p> The various command line options control how <i>gawk</i> interprets characters in regular expressions. </p>
<dl>
<dt>No options</dt>
<dd> <p> In the default case, <i>gawk</i> provides all the facilities of POSIX regular expressions and the GNU regular expression operators described above. </p>
 </dd>
<dt><code>--posix</code></dt>
<dd> <p> Only POSIX regular expressions are supported, the GNU operators are not special. (E.g., <code>\w</code> matches a literal <code>w</code>). </p>
 </dd>
<dt><code>--traditional</code></dt>
<dd> <p> Traditional UNIX <i>awk</i> regular expressions are matched. The GNU operators are not special, and interval expressions are not available. Characters described by octal and hexadecimal escape sequences are treated literally, even if they represent regular expression metacharacters. </p>
 </dd>
<dt><code>--re-interval</code></dt>
<dd> <p> Allow interval expressions in regular expressions, even if <code>--traditional</code> has been provided. </p>
 </dd></dl>
<h3>Actions</h3>
<p> Action statements are enclosed in braces, <code>{</code> and <code>}</code>. Action statements consist of the usual assignment, conditional, and looping statements found in most languages. The operators, control statements, and input/output statements available are patterned after those in C.  </p>
<h3>Operators</h3>
<p> The operators in AWK, in order of decreasing precedence, are: </p>
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
<dt><code>&lt; &gt; &lt;= &gt;= == !=</code></dt>
<dd> <p> The regular relational operators. </p>
 </dd>
<dt><code>~ !~</code></dt>
<dd> <p> Regular expression match, negated match. <code>NOTE</code>: Do not use a constant regular expression (<code>/foo/</code>) on the left-hand side of a <code>~</code> or <code>!~</code>. Only use one on the right-hand side. The expression <code>/foo/ ~ </code><i>exp</i> has the same meaning as <code>(($0 ~ /foo/) ~ </code><i>exp</i><code>)</code>. This is usually <i>not</i> what you want. </p>
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
<dd> <p> Close file, pipe or coprocess. The optional <i>how</i> should only be used when closing one end of a two-way pipe to a coprocess. It must be a string value, either <code>&quot;to&quot;</code> or <code>&quot;from&quot;</code>. </p>
 </dd>
<dt><code>getline</code></dt>
<dd> <p> Set <code>$0</code> from the next input record; set <code>NF</code>, <code>NR</code>, <code>FNR</code>, <code>RT</code>. </p>
 </dd>
<dt><code>getline &lt;</code><i>file</i></dt>
<dd> <p> Set <code>$0</code> from the next record of <i>file</i>; set <code>NF</code>, <code>RT</code>. </p>
 </dd>
<dt><code>getline</code><i> var</i></dt>
<dd> <p> Set <i>var</i> from the next input record; set <code>NR</code>, <code>FNR</code>, <code>RT</code>. </p>
 </dd>
<dt><code>getline</code><i> var</i><code> &lt;</code><i>file</i></dt>
<dd> <p> Set <i>var</i> from the next record of <i>file</i>; set <code>RT</code>. </p>
 </dd>
<dt><i>command</i><code> | getline </code>[<i>var</i>]</dt>
<dd> <p> Run <i>command</i>, piping the output either into <code>$0</code> or <i>var</i>, as above, and <code>RT</code>. </p>
 </dd>
<dt><i>command</i><code> |&amp; getline </code>[<i>var</i>]</dt>
<dd> <p> Run <i>command</i> as a coprocess piping the output either into <code>$0</code> or <i>var</i>, as above, and <code>RT</code>. Coprocesses are a <i>gawk</i> extension. (The <i>command</i> can also be a socket. See the subsection <code>Special File Names</code>, below.) </p>
 </dd>
<dt><code>next</code></dt>
<dd> <p> Stop processing the current input record. Read the next input record and start processing over with the first pattern in the AWK program. Upon reaching the end of the input data, execute any <code>END</code> rule(s). </p>
 </dd>
<dt><code>nextfile</code></dt>
<dd> <p> Stop processing the current input file. The next input record read comes from the next input file. Update <code>FILENAME</code> and <code>ARGIND</code>, reset <code>FNR</code> to 1, and start processing over with the first pattern in the AWK program. Upon reaching the end of the input data, execute any <code>ENDFILE</code> and <code>END</code> rule(s). </p>
 </dd>
<dt><code>print</code></dt>
<dd> <p> Print the current record. The output record is terminated with the value of <code>ORS</code>. </p>
 </dd>
<dt><code>print</code><i> expr-list</i></dt>
<dd> <p> Print expressions. Each expression is separated by the value of <code>OFS</code>. The output record is terminated with the value of <code>ORS</code>. </p>
 </dd>
<dt><code>print</code><i> expr-list</i><code> &gt;</code><i>file</i></dt>
<dd> <p> Print expressions on <i>file</i>. Each expression is separated by the value of <code>OFS</code>. The output record is terminated with the value of <code>ORS</code>. </p>
 </dd>
<dt><code>printf</code><i> fmt, expr-list</i></dt>
<dd> <p> Format and print. See <code>The </code><i>printf </i><code>Statement</code>, below. </p>
 </dd>
<dt><code>printf</code><i> fmt, expr-list</i><code> &gt;</code><i>file</i></dt>
<dd> <p> Format and print on <i>file</i>. </p>
 </dd>
<dt><code>system(</code><i>cmd-line</i><code>)</code></dt>
<dd> <p> Execute the command <i>cmd-line</i>, and return the exit status. (This may not be available on non-POSIX systems.) See <i>GAWK: Effective AWK Programming</i> for the full details on the exit status. </p>
 </dd>
<dt><code>fflush(</code>[<i>file</i>]<code>)</code></dt>
<dd> <p> Flush any buffers associated with the open output file or pipe <i>file</i>. If <i>file</i> is missing or if it is the null string, then flush all open output files and pipes. </p>
 </dd></dl>
<p> Additional output redirections are allowed for <code>print</code> and <code>printf</code>. </p>
<dl>
<dt><code>print ... &gt;&gt;</code><i> file</i></dt>
<dd> <p> Append output to the <i>file</i>. </p>
 </dd>
<dt><code>print ... |</code><i> command</i></dt>
<dd> <p> Write on a pipe. </p>
 </dd>
<dt><code>print ... |&amp;</code><i> command</i></dt>
<dd> <p> Send data to a coprocess or socket. (See also the subsection <code>Special File Names</code>, below.) </p>
 </dd></dl>
<p> The <code>getline</code> command returns 1 on success, zero on end of file, and -1 on an error. If the <i><a href="/docs/linux/man/3-errno/">errno</a></i>(3) value indicates that the I/O operation may be retried, and <code>PROCINFO[&quot;</code><i>input</i>&quot;, &quot;RETRY&quot;] is set, then -2 is returned instead of -1, and further calls to <code>getline</code> may be attempted. Upon an error, <code>ERRNO</code> is set to a string describing the problem. </p>
<p> <code>NOTE</code>: Failure in opening a two-way socket results in a non-fatal error being returned to the calling function. If using a pipe, coprocess, or socket to <code>getline</code>, or from <code>print</code> or <code>printf</code> within a loop, you <i>must</i> use <code>close()</code> to create new instances of the command or socket. AWK does not automatically close pipes, sockets, or coprocesses when they return EOF.  </p>
<i></i><h3>The printf Statement</h3>
<p> The AWK versions of the <code>printf</code> statement and <code>sprintf()</code> function (see below) accept the following conversion specification formats: </p>
<dl>
<dt><code>%a</code>,<code> %A</code></dt>
<dd> <p> A floating point number of the form [<code>-</code>]<code>0x</code><i>h</i><code>.</code><i>hhhh</i><code>p+-</code><i>dd</i> (C99 hexadecimal floating point format). For <code>%A</code>, uppercase letters are used instead of lowercase ones. </p>
 </dd>
<dt><code>%c</code></dt>
<dd> <p> A single character. If the argument used for <code>%c</code> is numeric, it is treated as a character and printed. Otherwise, the argument is assumed to be a string, and the only first character of that string is printed. </p>
 </dd>
<dt><code>%d</code>,<code> %i</code></dt>
<dd> <p> A decimal number (the integer part). </p>
 </dd>
<dt><code>%e</code>,<code> %E</code></dt>
<dd> <p> A floating point number of the form [<code>-</code>]<i>d</i><code>.</code><i>dddddd</i><code>e</code>[<code>+-</code>]<i>dd</i>. The <code>%E</code> format uses <code>E</code> instead of <code>e</code>. </p>
 </dd>
<dt><code>%f</code>,<code> %F</code></dt>
<dd> <p> A floating point number of the form [<code>-</code>]<i>ddd</i><code>.</code><i>dddddd</i>. If the system library supports it, <code>%F</code> is available as well. This is like <code>%f</code>, but uses capital letters for special ``not a number&#8217;&#8216; and ``infinity&#8217;&#8216; values. If <code>%F</code> is not available, <i>gawk</i> uses <code>%f</code>. </p>
 </dd>
<dt><code>%g</code>,<code> %G</code></dt>
<dd> <p> Use <code>%e</code> or <code>%f</code> conversion, whichever is shorter, with nonsignificant zeros suppressed. The <code>%G</code> format uses <code>%E</code> instead of <code>%e</code>. </p>
 </dd>
<dt><code>%o</code></dt>
<dd> <p> An unsigned octal number (also an integer). </p>
 </dd>
<dt><code>%u</code></dt>
<dd> <p> An unsigned decimal number (again, an integer). </p>
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
<dd> <p> A leading <code>0</code> (zero) acts as a flag, indicating that output should be padded with zeroes instead of spaces. This applies only to the numeric output formats. This flag only has an effect when the field width is wider than the value to be printed. </p>
 </dd>
<dt><code>&#8216;</code></dt>
<dd> <p> A single quote character instructs <i>gawk</i> to insert the locale&#8217;s thousands-separator character into decimal numbers, and to also use the locale&#8217;s decimal point character with floating point formats. This requires correct locale support in the C library and in the definition of the current locale. </p>
 </dd>
<dt><i>width</i></dt>
<dd> <p> The field should be padded to this width. The field is normally padded with spaces. With the <code>0</code> flag, it is padded with zeroes. </p>
 </dd>
<dt><code>.</code><i>prec</i></dt>
<dd> <p> A number that specifies the precision to use when printing. For the <code>%e</code>, <code>%E</code>, <code>%f</code> and <code>%F</code>, formats, this specifies the number of digits you want printed to the right of the decimal point. For the <code>%g</code>, and <code>%G</code> formats, it specifies the maximum number of significant digits. For the <code>%d</code>, <code>%i</code>, <code>%o</code>, <code>%u</code>, <code>%x</code>, and <code>%X</code> formats, it specifies the minimum number of digits to print. For the <code>%s </code> format, it specifies the maximum number of characters from the string that should be printed. </p>
 </dd></dl>
<p> The dynamic <i>width</i> and <i>prec</i> capabilities of the ISO C <code>printf()</code> routines are supported. A <code>*</code> in place of either the <i>width</i> or <i>prec</i> specifications causes their values to be taken from the argument list to <code>printf</code> or <code>sprintf()</code>. To use a positional specifier with a dynamic width or precision, supply the <i>count</i><code>$</code> after the <code>*</code> in the format string. For example, <code>&quot;%3$*2$.*1$s&quot;</code>.  </p>
<h3>Special File Names</h3>
<p> When doing I/O redirection from either <code>print</code> or <code>printf</code> into a file, or via <code>getline</code> from a file, <i>gawk</i> recognizes certain special filenames internally. These filenames allow access to open file descriptors inherited from <i>gawk</i>&#8216;s parent process (usually the shell). These file names may also be used on the command line to name data files. The filenames are: </p>
<dl>
<dt><code>-</code></dt>
<dd> <p> The standard input. </p>
 </dd>
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
<p> The following special filenames may be used with the <code>|&amp;</code> coprocess operator for creating TCP/IP network connections: </p>
<dl>
<dt><code>/inet/tcp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i></dt>
<dd>  </dd>
<dt><code>/inet4/tcp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i></dt>
<dd>  </dd>
<dt><code>/inet6/tcp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i></dt>
<dd> <p> Files for a TCP/IP connection on local port <i>lport</i> to remote host <i>rhost</i> on remote port <i>rport</i>. Use a port of <code>0</code> to have the system pick a port. Use <code>/inet4</code> to force an IPv4 connection, and <code>/inet6</code> to force an IPv6 connection. Plain <code>/inet</code> uses the system default (most likely IPv4). Usable only with the <code>|&amp;</code> two-way I/O operator. </p>
 </dd>
<dt><code>/inet/udp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i></dt>
<dd>  </dd>
<dt><code>/inet4/udp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i></dt>
<dd>  </dd>
<dt><code>/inet6/udp/</code><i>lport</i><code>/</code><i>rhost</i><code>/</code><i>rport</i></dt>
<dd> <p> Similar, but use UDP/IP instead of TCP/IP. </p>
 </dd></dl>
<h3>Numeric Functions</h3>
<p> AWK has the following built-in arithmetic functions: </p>
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
<dd> <p> Return a random number <i>N</i>, between zero and one, such that 0 &le; <i>N</i> &lt; 1. </p>
 </dd>
<dt><code>sin(</code><i>expr</i><code>)</code></dt>
<dd> <p> Return the sine of <i>expr</i>, which is in radians. </p>
 </dd>
<dt><code>sqrt(</code><i>expr</i><code>)</code></dt>
<dd> <p> Return the square root of <i>expr</i>. </p>
 </dd>
<dt><code>srand(</code>[<i>expr</i>]<code>)</code></dt>
<dd> <p> Use <i>expr</i> as the new seed for the random number generator. If no <i>expr</i> is provided, use the time of day. Return the previous seed for the random number generator. </p>
 </dd></dl>
<h3>String Functions</h3>
<p> <i>Gawk</i> has the following built-in string functions: </p>
<dl>
<dt><code>asort(</code><i>s </i>[<code>, </code><i>d</i> [<code>, </code><i>how</i>] ]<code>)</code></dt>
<dd> <p> Return the number of elements in the source array <i>s</i>. Sort the contents of <i>s</i> using <i>gawk</i>&#8216;s normal rules for comparing values, and replace the indices of the sorted values <i>s</i> with sequential integers starting with 1. If the optional destination array <i>d</i> is specified, first duplicate <i>s</i> into <i>d</i>, and then sort <i>d</i>, leaving the indices of the source array <i>s</i> unchanged. The optional string <i>how</i> controls the direction and the comparison mode. Valid values for <i>how</i> are any of the strings valid for <code>PROCINFO[&quot;sorted_in&quot;]</code>. It can also be the name of a user-defined comparison function as described in <code>PROCINFO[&quot;sorted_in&quot;]</code>. </p>
 </dd>
<dt><code>asorti(</code><i>s </i>[<code>, </code><i>d</i> [<code>, </code><i>how</i>] ]<code>)</code></dt>
<dd> <p> Return the number of elements in the source array <i>s</i>. The behavior is the same as that of <code>asort()</code>, except that the array <i>indices</i> are used for sorting, not the array values. When done, the array is indexed numerically, and the values are those of the original indices. The original values are lost; thus provide a second array if you wish to preserve the original. The purpose of the optional string <i>how</i> is the same as described previously for <code>asort()</code>. </p>
 </dd>
<dt><code>gensub(</code><i>r</i><code>, </code><i>s</i><code>, </code><i>h </i>[<code>, </code><i>t</i>]<code>)</code></dt>
<dd> <p> Search the target string <i>t</i> for matches of the regular expression <i>r</i>. If <i>h</i> is a string beginning with <code>g</code> or <code>G</code>, then replace all matches of <i>r</i> with <i>s</i>. Otherwise, <i>h</i> is a number indicating which match of <i>r</i> to replace. If <i>t</i> is not supplied, use <code>$0</code> instead. Within the replacement text <i>s</i>, the sequence <code>\</code><i>n</i>, where <i>n</i> is a digit from 1 to 9, may be used to indicate just the text that matched the <i>n</i>&#8216;th parenthesized subexpression. The sequence <code>\0</code> represents the entire matched text, as does the character <code>&amp;</code>. Unlike <code>sub()</code> and <code>gsub()</code>, the modified string is returned as the result of the function, and the original target string is <i>not</i> changed. </p>
 </dd>
<dt><code>gsub(</code><i>r</i><code>, </code><i>s </i>[<code>, </code><i>t</i>]<code>)</code></dt>
<dd> <p> For each substring matching the regular expression <i>r</i> in the string <i>t</i>, substitute the string <i>s</i>, and return the number of substitutions. If <i>t</i> is not supplied, use <code>$0</code>. An <code>&amp;</code> in the replacement text is replaced with the text that was actually matched. Use <code>\&amp;</code> to get a literal <code>&amp;</code>. (This must be typed as <code>&quot;\\&amp;&quot;</code>; see <i>GAWK: Effective AWK Programming</i> for a fuller discussion of the rules for ampersands and backslashes in the replacement text of <code>sub()</code>, <code>gsub()</code>, and <code>gensub()</code>.) </p>
 </dd>
<dt><code>index(</code><i>s</i><code>,</code><i> t</i><code>)</code></dt>
<dd> <p> Return the index of the string <i>t</i> in the string <i>s</i>, or zero if <i>t</i> is not present. (This implies that character indices start at one.) It is a fatal error to use a regexp constant for <i>t</i>. </p>
 </dd>
<dt><code>length(</code>[<i>s</i>]<code>)</dt>
<dd> <p> Return the length of the string </code><i>s</i>, or the length of <code>$0</code> if <i>s</i> is not supplied. As a non-standard extension, with an array argument, <code>length()</code> returns the number of elements in the array. </p>
 </dd>
<dt><code>match(</code><i>s</i><code>, </code><i>r </i>[<code>, </code><i>a</i>]<code>)</code></dt>
<dd> <p> Return the position in <i>s</i> where the regular expression <i>r</i> occurs, or zero if <i>r</i> is not present, and set the values of <code>RSTART</code> and <code>RLENGTH</code>. Note that the argument order is the same as for the <code>~</code> operator: <i>str</i><code> ~</code> <i>re</i>. If array <i>a</i> is provided, <i>a</i> is cleared and then elements 1 through <i>n</i> are filled with the portions of <i>s</i> that match the corresponding parenthesized subexpression in <i>r</i>. The zero&#8217;th element of <i>a</i> contains the portion of <i>s</i> matched by the entire regular expression <i>r</i>. Subscripts <code>a[</code><i>n</i><code>, &quot;start&quot;]</code>, and <code>a[</code><i>n</i><code>, &quot;length&quot;]</code> provide the starting index in the string and length respectively, of each matching substring. </p>
 </dd>
<dt><code>patsplit(</code><i>s</i><code>, </code><i>a </i>[<code>, </code><i>r</i> [<code>, </code><i>seps</i>] ]<code>)</code></dt>
<dd> <p> Split the string <i>s</i> into the array <i>a</i> and the separators array <i>seps</i> on the regular expression <i>r</i>, and return the number of fields. Element values are the portions of <i>s</i> that matched <i>r</i>. The value of <code>seps[</code><i>i</i><code>]</code> is the possibly null separator that appeared after <code>a[</code><i>i</i><code>]</code>. The value of <code>seps[0]</code> is the possibly null leading separator. If <i>r</i> is omitted, <code>FPAT</code> is used instead. The arrays <i>a</i> and <i>seps</i> are cleared first. Splitting behaves identically to field splitting with <code>FPAT</code>, described above. </p>
 </dd>
<dt><code>split(</code><i>s</i><code>, </code><i>a </i>[<code>, </code><i>r</i> [<code>, </code><i>seps</i>] ]<code>)</code></dt>
<dd> <p> Split the string <i>s</i> into the array <i>a</i> and the separators array <i>seps</i> on the regular expression <i>r</i>, and return the number of fields. If <i>r</i> is omitted, <code>FS</code> is used instead. The arrays <i>a</i> and <i>seps</i> are cleared first. <code>seps[</code><i>i</i><code>]</code> is the field separator matched by <i>r</i> between <code>a[</code><i>i</i><code>]</code> and <code>a[</code><i>i</i><code>+1]</code>. If <i>r</i> is a single space, then leading whitespace in <i>s</i> goes into the extra array element <code>seps[0]</code> and trailing whitespace goes into the extra array element <code>seps[</code><i>n</i><code>]</code>, where <i>n</i> is the return value of <code>split(</code><i>s</i><code>, </code><i>a</i><code>, </code><i>r</i><code>, </code><i>seps</i><code>)</code>. Splitting behaves identically to field splitting, described above. In particular, if <i>r</i> is a single-character string, that string acts as the separator, even if it happens to be a regular expression metacharacter. </p>
 </dd>
<dt><code>sprintf(</code><i>fmt</i><code>,</code><i> expr-list</i><code>)</code></dt>
<dd> <p> Print <i>expr-list</i> according to <i>fmt</i>, and return the resulting string. </p>
 </dd>
<dt><code>strtonum(</code><i>str</i><code>)</code></dt>
<dd> <p> Examine <i>str</i>, and return its numeric value. If <i>str</i> begins with a leading <code>0</code>, treat it as an octal number. If <i>str</i> begins with a leading <code>0x</code> or <code>0X</code>, treat it as a hexadecimal number. Otherwise, assume it is a decimal number. </p>
 </dd>
<dt><code>sub(</code><i>r</i><code>, </code><i>s </i>[<code>, </code><i>t</i>]<code>)</code></dt>
<dd> <p> Just like <code>gsub()</code>, but replace only the first matching substring. Return either zero or one. </p>
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
<p> Since one of the primary uses of AWK programs is processing log files that contain time stamp information, <i>gawk</i> provides the following functions for obtaining time stamps and formatting them. </p>
<dl>
<dt><code>mktime(</code><i>datespec</i> [<code>, </code><i>utc-flag</i>]<code>)</code></dt>
<dd> <p> Turn <i>datespec</i> into a time stamp of the same form as returned by <code>systime()</code>, and return the result. The <i>datespec</i> is a string of the form <i>YYYY MM DD HH MM SS[ DST]</i>. The contents of the string are six or seven numbers representing respectively the full year including century, the month from 1 to 12, the day of the month from 1 to 31, the hour of the day from 0 to 23, the minute from 0 to 59, the second from 0 to 60, and an optional daylight saving flag. The values of these numbers need not be within the ranges specified; for example, an hour of -1 means 1 hour before midnight. The origin-zero Gregorian calendar is assumed, with year 0 preceding year 1 and year -1 preceding year 0. If <i>utc-flag</i> is present and is non-zero or non-null, the time is assumed to be in the UTC time zone; otherwise, the time is assumed to be in the local time zone. If the <i>DST</i> daylight saving flag is positive, the time is assumed to be daylight saving time; if zero, the time is assumed to be standard time; and if negative (the default), <code>mktime()</code> attempts to determine whether daylight saving time is in effect for the specified time. If <i>datespec</i> does not contain enough elements or if the resulting time is out of range, <code>mktime()</code> returns -1. </p>
 </dd>
<dt><code>strftime(</code>[<i>format </i>[<code>, </code><i>timestamp</i>[<code>, </code><i>utc-flag</i>]]]<code>)</code></dt>
<dd> <p> Format <i>timestamp</i> according to the specification in <i>format</i>. If <i>utc-flag</i> is present and is non-zero or non-null, the result is in UTC, otherwise the result is in local time. The <i>timestamp</i> should be of the same form as returned by <code>systime()</code>. If <i>timestamp</i> is missing, the current time of day is used. If <i>format</i> is missing, a default format equivalent to the output of <i><a href="/docs/linux/man/1-date/">date</a></i>(1) is used. The default format is available in <code>PROCINFO[strftime]</code>. See the specification for the <code>strftime()</code> function in ISO C for the format conversions that are guaranteed to be available. </p>
 </dd>
<dt><code>systime()</code></dt>
<dd> <p> Return the current time of day as the number of seconds since the Epoch (1970-01-01 00:00:00 UTC on POSIX systems). </p>
 </dd></dl>
<h3>Bit Manipulations Functions</h3>
<p> <i>Gawk</i> supplies the following bit manipulation functions. They work by converting double-precision floating point values to <code>uintmax_t</code> integers, doing the operation, and then converting the result back to floating point. </p>
<p> <code>NOTE</code>: Passing negative operands to any of these functions causes a fatal error. </p>
<p> The functions are: </p>
<dl>
<dt><code>and(</code><i>v1</i><code>, </code><i>v2 </i>[, ...]<code>)</code></dt>
<dd> <p> Return the bitwise AND of the values provided in the argument list. There must be at least two. </p>
 </dd>
<dt><code>compl(</code><i>val</i><code>)</code></dt>
<dd> <p> Return the bitwise complement of <i>val</i>. </p>
 </dd>
<dt><code>lshift(</code><i>val</i><code>, </code><i>count</i><code>)</code></dt>
<dd> <p> Return the value of <i>val</i>, shifted left by <i>count</i> bits. </p>
 </dd>
<dt><code>or(</code><i>v1</i><code>, </code><i>v2 </i>[, ...]<code>)</code></dt>
<dd> <p> Return the bitwise OR of the values provided in the argument list. There must be at least two. </p>
 </dd>
<dt><code>rshift(</code><i>val</i><code>, </code><i>count</i><code>)</code></dt>
<dd> <p> Return the value of <i>val</i>, shifted right by <i>count</i> bits. </p>
 </dd>
<dt><code>xor(</code><i>v1</i><code>, </code><i>v2 </i>[, ...]<code>)</code></dt>
<dd> <p> Return the bitwise XOR of the values provided in the argument list. There must be at least two. </p>
 </dd></dl>
<h3>Type Functions</h3>
<p> The following functions provide type related information about their arguments. </p>
<dl>
<dt><code>isarray(</code><i>x</i><code>)</code></dt>
<dd> <p> Return true if <i>x</i> is an array, false otherwise. This function is mainly for use with the elements of multidimensional arrays and with function parameters. </p>
 </dd>
<dt><code>typeof(</code><i>x</i><code>)</code></dt>
<dd> <p> Return a string indicating the type of <i>x</i>. The string will be one of <code>&quot;array&quot;</code>, <code>&quot;number&quot;</code>, <code>&quot;regexp&quot;</code>, <code>&quot;string&quot;</code>, <code>&quot;strnum&quot;</code>, <code>&quot;unassigned&quot;</code>, or <code>&quot;undefined&quot;</code>. </p>
 </dd></dl>
<h3>Internationalization Functions</h3>
<p> The following functions may be used from within your AWK program for translating strings at run-time. For full details, see <i>GAWK: Effective AWK Programming</i>. </p>
<dl>
<dt><code>bindtextdomain(</code><i>directory </i>[<code>, </code><i>domain</i>]<code>)</code></dt>
<dd> <p> Specify the directory where <i>gawk</i> looks for the <code>.gmo</code> files, in case they will not or cannot be placed in the ``standard&#8217;&#8216; locations (e.g., during testing). It returns the directory where <i>domain</i> is ``bound.&#8216;&#8216; </p>
<p> The default <i>domain</i> is the value of <code>TEXTDOMAIN</code>. If <i>directory</i> is the null string (<code>&quot;&quot;</code>), then <code>bindtextdomain()</code> returns the current binding for the given <i>domain</i>. </p>
 </dd>
<dt><code>dcgettext(</code><i>string </i>[<code>, </code><i>domain </i>[<code>, </code><i>category</i>]]<code>)</code></dt>
<dd> <p> Return the translation of <i>string</i> in text domain <i>domain</i> for locale category <i>category</i>. The default value for <i>domain</i> is the current value of <code>TEXTDOMAIN</code>. The default value for <i>category</i> is <code>&quot;LC_MESSAGES&quot;</code>. </p>
<p> If you supply a value for <i>category</i>, it must be a string equal to one of the known locale categories described in <i>GAWK: Effective AWK Programming</i>. You must also supply a text domain. Use <code>TEXTDOMAIN</code> if you want to use the current domain. </p>
 </dd>
<dt><code>dcngettext(</code><i>string1</i><code>, </code><i>string2</i><code>, </code><i>number </i>[<code>, </code><i>domain </i>[<code>, </code><i>category</i>]]<code>)</code></dt>
<dd> <p> Return the plural form used for <i>number</i> of the translation of <i>string1</i> and <i>string2</i> in text domain <i>domain</i> for locale category <i>category</i>. The default value for <i>domain</i> is the current value of <code>TEXTDOMAIN</code>. The default value for <i>category</i> is <code>&quot;LC_MESSAGES&quot;</code>. </p>
<p> If you supply a value for <i>category</i>, it must be a string equal to one of the known locale categories described in <i>GAWK: Effective AWK Programming</i>. You must also supply a text domain. Use <code>TEXTDOMAIN</code> if you want to use the current domain. </p>
 </dd></dl>
<h2>USER-DEFINED FUNCTIONS</h2>
<p> Functions in AWK are defined as follows: </p>
<dl>
<dd> <p> <code>function </code><i>name</i><code>(</code><i>parameter list</i><code>) { </code><i>statements </i><code>}</code> </p>
 </dd></dl>
<p> Functions execute when they are called from within expressions in either patterns or actions. Actual parameters supplied in the function call are used to instantiate the formal parameters declared in the function. Arrays are passed by reference, other variables are passed by value. </p>
<p> Since functions were not originally part of the AWK language, the provision for local variables is rather clumsy: They are declared as extra parameters in the parameter list. The convention is to separate local variables from real parameters by extra spaces in the parameter list. For example: </p>
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
<p> As of version 4.1.2, this works with user-defined functions, built-in functions, and extension functions. </p>
<p> If <code>--lint</code> has been provided, <i>gawk</i> warns about calls to undefined functions at parse time, instead of at run time. Calling an undefined function at run time is a fatal error. </p>
<p> The word <code>func</code> may be used in place of <code>function</code>, although this is deprecated.  </p>
<h2>DYNAMICALLY LOADING NEW FUNCTIONS</h2>
<p> You can dynamically add new functions written in C or C++ to the running <i>gawk</i> interpreter with the <code>@load</code> statement. The full details are beyond the scope of this manual page; see <i>GAWK: Effective AWK Programming</i>.  </p>
<h2>SIGNALS</h2>
<p> The <i>gawk</i> profiler accepts two signals. <code>SIGUSR1</code> causes it to dump a profile and function call stack to the profile file, which is either <code>awkprof.out</code>, or whatever file was named with the <code>--profile</code> option. It then continues to run. <code>SIGHUP</code> causes <i>gawk</i> to dump the profile and function call stack and then exit.  </p>
<h2>INTERNATIONALIZATION</h2>
<p> String constants are sequences of characters enclosed in double quotes. In non-English speaking environments, it is possible to mark strings in the AWK program as requiring translation to the local natural language. Such strings are marked in the AWK program with a leading underscore (``_&#8216;&#8216;). For example, </p>
<dl>
<dd> <p> <code> gawk &#8216;BEGIN { print &quot;hello, world&quot; }&#8216; </p>
 </dd></dl>
<p> </code> always prints <code>hello, world</code>. But, </p>
<dl>
<dd> <p> <code> gawk &#8216;BEGIN { print _&quot;hello, world&quot; }&#8216; </p>
 </dd></dl>
<p> </code> might print <code>bonjour, monde</code> in France. </p>
<p> There are several steps involved in producing and running a localizable AWK program. </p>
<dl>
<dt>1.</dt>
<dd> <p> Add a <code>BEGIN</code> action to assign a value to the <code>TEXTDOMAIN</code> variable to set the text domain to a name associated with your program: </p>
<p> <code> BEGIN { TEXTDOMAIN = &quot;myprog&quot; } </code> </p>
<p> This allows <i>gawk</i> to find the <code>.gmo</code> file associated with your program. Without this step, <i>gawk</i> uses the <code>messages</code> text domain, which likely does not contain translations for your program. </p>
 </dd>
<dt>2.</dt>
<dd> <p> Mark all strings that should be translated with leading underscores. </p>
 </dd>
<dt>3.</dt>
<dd> <p> If necessary, use the <code>dcgettext()</code> and/or <code>bindtextdomain()</code> functions in your program, as appropriate. </p>
 </dd>
<dt>4.</dt>
<dd> <p> Run <code>gawk --gen-pot -f myprog.awk &gt; myprog.pot</code> to generate a <code>.pot</code> file for your program. </p>
 </dd>
<dt>5.</dt>
<dd> <p> Provide appropriate translations, and build and install the corresponding <code>.gmo</code> files. </p>
 </dd></dl>
<p> The internationalization features are described in full detail in <i>GAWK: Effective AWK Programming</i>.  </p>
<h2>POSIX COMPATIBILITY</h2>
<p> A primary goal for <i>gawk</i> is compatibility with the POSIX standard, as well as with the latest version of Brian Kernighan&#8217;s <i>awk</i>. To this end, <i>gawk</i> incorporates the following user visible features which are not described in the AWK book, but are part of the Brian Kernighan&#8217;s version of <i>awk</i>, and are in the POSIX standard. </p>
<p> The book indicates that command line variable assignment happens when <i>awk</i> would otherwise open the argument as a file, which is after the <code>BEGIN</code> rule is executed. However, in earlier implementations, when such an assignment appeared before any file names, the assignment would happen <i>before</i> the <code>BEGIN</code> rule was run. Applications came to depend on this ``feature.&#8216;&#8216; When <i>awk</i> was changed to match its documentation, the <code>-v</code> option for assigning variables before program execution was added to accommodate applications that depended upon the old behavior. (This feature was agreed upon by both the Bell Laboratories developers and the GNU developers.) </p>
<p> When processing arguments, <i>gawk</i> uses the special option ``--&#8216;&#8216; to signal the end of arguments. In compatibility mode, it warns about but otherwise ignores undefined options. In normal operation, such arguments are passed on to the AWK program for it to process. </p>
<p> The AWK book does not define the return value of <code>srand()</code>. The POSIX standard has it return the seed it was using, to allow keeping track of random number sequences. Therefore <code>srand()</code> in <i>gawk</i> also returns its current seed. </p>
<p> Other features are: The use of multiple <code>-f</code> options (from MKS <i>awk</i>); the <code>ENVIRON</code> array; the <code>\a</code>, and <code>\v</code> escape sequences (done originally in <i>gawk</i> and fed back into the Bell Laboratories version); the <code>tolower()</code> and <code>toupper()</code> built-in functions (from the Bell Laboratories version); and the ISO C conversion specifications in <code>printf</code> (done first in the Bell Laboratories version).  </p>
<h2>HISTORICAL FEATURES</h2>
<p> There is one feature of historical AWK implementations that <i>gawk</i> supports: It is possible to call the <code>length()</code> built-in function not only with no argument, but even without parentheses! Thus, </p>
<dl>
<dd> <p> <code> a = length <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</code># Holy Algol 60, Batman!<br/>
 </code> </p>
 </dd></dl>
<p> is the same as either of </p>
<dl>
<dd> <p> <code> a = length() <br/>
 a = length($0) </code> </p>
 </dd></dl>
<p> Using this feature is poor practice, and <i>gawk</i> issues a warning about its use if <code>--lint</code> is specified on the command line.  </p>
<h2>GNU EXTENSIONS</h2>
<p> <i>Gawk</i> has a too-large number of extensions to POSIX <i>awk</i>. They are described in this section. All the extensions described here can be disabled by invoking <i>gawk</i> with the <code>--traditional</code> or <code>--posix</code> options. </p>
<p> The following features of <i>gawk</i> are not available in POSIX <i>awk</i>. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> No path search is performed for files named via the <code>-f</code> option. Therefore the <code>AWKPATH</code> environment variable is not special. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There is no facility for doing file inclusion (<i>gawk</i>&#8216;s <code>@include</code> mechanism). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There is no facility for dynamically adding new functions written in C (<i>gawk</i>&#8216;s <code>@load</code> mechanism). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>\x</code> escape sequence. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ability to continue lines after <code>?</code> and <code>:</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Octal and hexadecimal constants in AWK programs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>ARGIND</code>, <code>BINMODE</code>, <code>ERRNO</code>, <code>LINT</code>, <code>PREC</code>, <code>ROUNDMODE</code>, <code>RT</code> and <code>TEXTDOMAIN</code> variables are not special. </p>
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
<dd> <p> The <code>FUNCTAB</code>, <code>SYMTAB</code>, and <code>PROCINFO</code> arrays are not available. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The use of <code>RS</code> as a regular expression. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The special file names available for I/O redirection are not recognized. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>|&amp;</code> operator for creating coprocesses. </p>
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
<dd> <p> The <code>and()</code>, <code>asort()</code>, <code>asorti()</code>, <code>bindtextdomain()</code>, <code>compl()</code>, <code>dcgettext()</code>, <code>dcngettext()</code>, <code>gensub()</code>, <code>lshift()</code>, <code>mktime()</code>, <code>or()</code>, <code>patsplit()</code>, <code>rshift()</code>, <code>strftime()</code>, <code>strtonum()</code>, <code>systime()</code> and <code>xor()</code> functions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Localizable strings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Non-fatal I/O. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Retryable I/O. </p>
 </dd></dl>
<p> The AWK book does not define the return value of the <code>close()</code> function. <i>Gawk</i>&#8216;s <code>close()</code> returns the value from <i><a href="/docs/linux/man/3-fclose/">fclose</a></i>(3), or <i><a href="/docs/linux/man/3-pclose/">pclose</a></i>(3), when closing an output file or pipe, respectively. It returns the process&#8217;s exit status when closing an input pipe. The return value is -1 if the named file, pipe or coprocess was not opened with a redirection. </p>
<p> When <i>gawk</i> is invoked with the <code>--traditional</code> option, if the <i>fs</i> argument to the <code>-F</code> option is ``t&#8217;&#8216;, then <code>FS</code> is set to the tab character. Note that typing <code>gawk -F\t ...</code> simply causes the shell to quote the ``t,&#8216;&#8216; and does not pass ``\t&#8217;&#8216; to the <code>-F</code> option. Since this is a rather ugly special case, it is not the default behavior. This behavior also does not occur if <code>--posix</code> has been specified. To really get a tab character as the field separator, it is best to use single quotes: <code>gawk -F&#8217;\t&#8217; ...</code>.  </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The <code>AWKPATH</code> environment variable can be used to provide a list of directories that <i>gawk</i> searches when looking for files named via the <code>-f</code>, <code>--file</code>, <code>-i</code> and <code>--include</code> options, and the <code>@include</code> directive. If the initial search fails, the path is searched again after appending <code>.awk</code> to the filename. </p>
<p> The <code>AWKLIBPATH</code> environment variable can be used to provide a list of directories that <i>gawk</i> searches when looking for files named via the <code>-l</code> and <code>--load</code> options. </p>
<p> The <code>GAWK_READ_TIMEOUT</code> environment variable can be used to specify a timeout in milliseconds for reading input from a terminal, pipe or two-way communication including sockets. </p>
<p> For connection to a remote host via socket, <code>GAWK_SOCK_RETRIES</code> controls the number of retries, and <code>GAWK_MSEC_SLEEP</code> the interval between retries. The interval is in milliseconds. On systems that do not support <i><a href="/docs/linux/man/3-usleep/">usleep</a></i>(3), the value is rounded up to an integral number of seconds. </p>
<p> If <code>POSIXLY_CORRECT</code> exists in the environment, then <i>gawk</i> behaves exactly as if <code>--posix</code> had been specified on the command line. If <code>--lint</code> has been specified, <i>gawk</i> issues a warning message to this effect.  </p>
<h2>EXIT STATUS</h2>
<p> If the <code>exit</code> statement is used with a value, then <i>gawk</i> exits with the numeric value given to it. </p>
<p> Otherwise, if there were no problems during execution, <i>gawk</i> exits with the value of the C constant <code>EXIT_SUCCESS</code>. This is usually zero. </p>
<p> If an error occurs, <i>gawk</i> exits with the value of the C constant <code>EXIT_FAILURE</code>. This is usually one. </p>
<p> If <i>gawk</i> exits because of a fatal error, the exit status is 2. On non-POSIX systems, this value may be mapped to <code>EXIT_FAILURE</code>.  </p>
<h2>VERSION INFORMATION</h2>
<p> This man page documents <i>gawk</i>, version 5.1.  </p>
<h2>AUTHORS</h2>
<p> The original version of UNIX <i>awk</i> was designed and implemented by Alfred Aho, Peter Weinberger, and Brian Kernighan of Bell Laboratories. Brian Kernighan continues to maintain and enhance it. </p>
<p> Paul Rubin and Jay Fenlason, of the Free Software Foundation, wrote <i>gawk</i>, to be compatible with the original version of <i>awk</i> distributed in Seventh Edition UNIX. John Woods contributed a number of bug fixes. David Trueman, with contributions from Arnold Robbins, made <i>gawk</i> compatible with the new version of UNIX <i>awk</i>. Arnold Robbins is the current maintainer. </p>
<p> See <i>GAWK: Effective AWK Programming</i> for a full list of the contributors to <i>gawk</i> and its documentation. </p>
<p> See the <code>README</code> file in the <i>gawk</i> distribution for up-to-date information about maintainers and which ports are currently supported.  </p>
<h2>BUG REPORTS</h2>
<p> If you find a bug in <i>gawk</i>, please send electronic mail to <code>bug-gawk [at] gnu.org</code>. Please include your operating system and its revision, the version of <i>gawk</i> (from <code>gawk --version</code>), which C compiler you used to compile it, and a test program and data that are as small as possible for reproducing the problem. </p>
<p> Before sending a bug report, please do the following things. First, verify that you have the latest version of <i>gawk</i>. Many bugs (usually subtle ones) are fixed at each release, and if yours is out of date, the problem may already have been solved. Second, please see if setting the environment variable <code>LC_ALL</code> to <code>LC_ALL=C</code> causes things to behave as you expect. If so, it&#8217;s a locale issue, and may or may not really be a bug. Finally, please read this man page and the reference manual carefully to be sure that what you think is a bug really is, instead of just a quirk in the language. </p>
<p> Whatever you do, do <code>NOT</code> post a bug report in <code>comp.lang.awk</code>. While the <i>gawk</i> developers occasionally read this newsgroup, posting bug reports there is an unreliable way to report bugs. Similarly, do <code>NOT</code> use a web forum (such as Stack Overflow) for reporting bugs. Instead, please use the electronic mail addresses given above. Really. </p>
<p> If you&#8217;re using a GNU/Linux or BSD-based system, you may wish to submit a bug report to the vendor of your distribution. That&#8217;s fine, but please send a copy to the official email address as well, since there&#8217;s no guarantee that the bug report will be forwarded to the <i>gawk</i> maintainer.  </p>
<h2>BUGS</h2>
<p> The <code>-F</code> option is not necessary given the command line variable assignment feature; it remains only for backwards compatibility.  </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1), <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1), <i><a href="/docs/linux/man/2-getpid/">getpid</a></i>(2), <i><a href="/docs/linux/man/2-getppid/">getppid</a></i>(2), <i><a href="/docs/linux/man/2-getpgrp/">getpgrp</a></i>(2), <i><a href="/docs/linux/man/2-getuid/">getuid</a></i>(2), <i><a href="/docs/linux/man/2-geteuid/">geteuid</a></i>(2), <i><a href="/docs/linux/man/2-getgid/">getgid</a></i>(2), <i><a href="/docs/linux/man/2-getegid/">getegid</a></i>(2), <i><a href="/docs/linux/man/2-getgroups/">getgroups</a></i>(2), <i><a href="/docs/linux/man/3-printf/">printf</a></i>(3), <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3), <i><a href="/docs/linux/man/3-usleep/">usleep</a></i>(3) </p>
<p> <i>The AWK Programming Language</i>, Alfred V. Aho, Brian W. Kernighan, Peter J. Weinberger, Addison-Wesley, 1988. ISBN 0-201-07981-X. </p>
<p> <i>GAWK: Effective AWK Programming</i>, Edition 5.1, shipped with the <i>gawk</i> source. The current version of this document is available online at <code><a rel="nofollow" href="https://www.gnu.org/software/gawk/manual">https://www.gnu.org/software/gawk/manual</a></code>. </p>
<p> The GNU <code>gettext</code> documentation, available online at <code><a rel="nofollow" href="https://www.gnu.org/software/gettext">https://www.gnu.org/software/gettext</a></code>.  </p>
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
<p> Brian Kernighan provided valuable assistance during testing and debugging. We thank him.  </p>
<h2>COPYING PERMISSIONS</h2>
<p> Copyright &#169; 1989, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2001, 2002, 2003, 2004, 2005, 2007, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this manual page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual page into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Foundation. </p>
