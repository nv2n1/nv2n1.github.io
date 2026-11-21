---
title: "clisp(1)"
name: "clisp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clisp/"
description: "clisp – ANSI Common Lisp compiler, interpreter and debugger."
---

<h2 class="name">NAME</h2>
<p> clisp &#8211; ANSI Common Lisp compiler, interpreter and debugger. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>clisp</code> [[<code>-h</code>] | [<code>&#8211;help</code>]] [<code>&#8211;version</code>] [<code>&#8211;license</code>] [<code>-help-image</code>] [<code>-B&nbsp;<wbr></code><i>lisp-lib-dir</i>] [<code>-K&nbsp;<wbr></code><i>linking-set</i>] [<code>-M&nbsp;<wbr></code><i>mem-file</i>] [<code>-m&nbsp;<wbr></code><i>memory-size</i>] [<code>-L&nbsp;<wbr></code><i>language</i>] [<code>-N&nbsp;<wbr></code><i>locale-dir</i>] [<code>-E</code><i>domain</i>&nbsp;<wbr><i>encoding</i>] [[<code>-q</code>] | [<code>&#8211;quiet</code>] | [<code>&#8211;silent</code>] | [<code>-v</code>] | [<code>&#8211;verbose</code>]] [<code>-on-error&nbsp;<wbr></code><i>action</i>] [<code>-repl</code>] [<code>-w</code>] [<code>-I</code>] [[<code>-ansi</code>] | [<code>-traditional</code>]] [<code>-modern</code>] [<code>-p&nbsp;<wbr></code><i>package</i>] [<code>-C</code>] [<code>-norc</code>] [<code>-lp&nbsp;<wbr></code><i>directory</i>&#8230;] [<code>-i&nbsp;<wbr></code><i>init-file</i>&#8230;] [<code>-c</code>&nbsp;<wbr>[<code>-l</code>]&nbsp;<wbr><i>lisp-file</i>&nbsp;<wbr>[<code>-o</code><code>&nbsp;<wbr></code><i>output-file</i>]&#8230;] [<code>-x&nbsp;<wbr></code><i>expressions</i>&#8230;] [<i>lisp-file</i>&nbsp;<wbr>[<i>argument</i>&#8230;]]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>Invokes the <i></i><code>Common Lisp</code>[1] interpreter and compiler. When called without arguments, executes the <i>read-eval-print loop</i>[2], in which expressions are in turn <i></i><code>READ</code>[3] from the standard input, <i></i><code>EVAL</code>[4]uated by the lisp interpreter, and their results are <i></i><code>PRINT</code>[5]ed to the standard output. Invoked with <code>-c</code>, compiles the specified lisp files to a platform-independent bytecode which can be executed more efficiently.</dd>
<h2>OPTIONS</h2>
<p> <code>-h</code><br />
 <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Displays a help message on how to invoke <i></i><code>CLISP</code>[6].</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Displays the <i></i><code>CLISP</code>[6] version number, as given by the function <i></i><code>LISP-IMPLEMENTATION-VERSION</code>[7], the value of the variable <i>*FEATURES*</i>, as well some other information.</dd></dl>
<p> <code>&#8211;license</code></p>
<dl>
<dt>
</dt><dd> Displays a summary of the licensing information, the <i>GNU</i>[8] <i>GPL</i>[9].</dd></dl>
<p> <code>-help-image</code></p>
<dl>
<dt>
</dt><dd> Displays information about the memory image being invoked: whether is it suitable for scripting as well as the <code>:DOCUMENTATION</code> supplied to <code>EXT:SAVEINITMEM</code>.</dd></dl>
<p> <code>-B</code> <i>lisp-lib-dir</i></p>
<dl>
<dt>
</dt><dd> Specifies the installation directory. This is the directory containing the linking sets and other data files. This option is normally not necessary, because the installation directory is already built-in into the <code>clisp</code> executable. Directory <i>lisp-lib-dir</i> can be changed dynamically using the <i>SYMBOL-MACRO</i>[10] <i>*LIB-DIRECTORY*</i>.</dd></dl>
<p> <code>-K</code> <i>linking-set</i></p>
<dl>
<dt>
</dt><dd> Specifies the linking set to be run. This is a directory (relative to the <i>lisp-lib-dir</i>) containing at least a main executable (runtime) and an initial memory image. Possible values are </dd>
<p> <code>base</code></p>
<dl>
<dt>
</dt><dd> the core <i></i><code>CLISP</code>[6]</dd></dl>
<p> <code>full</code></p>
<dl>
<dt>
</dt><dd> core plus all the modules with which this installation was built, see Section 32.2, lqExternal Modulesrq.</dd></dl>
<p> The default is <code>base</code>.</dl>
<p> <code>-M</code> <i>mem-file</i></p>
<dl>
<dt>
</dt><dd> Specifies the initial memory image. This must be a memory dump produced by the <code>EXT:SAVEINITMEM</code> function by this <code>clisp</code> runtime. It may have been compressed using <i>GNU</i>[8] <i></i><code>gzip</code>[11].</dd></dl>
<p> <code>-m</code> <i>memory-size</i></p>
<dl>
<dt>
</dt><dd> Sets the amount of memory <i></i><code>CLISP</code>[6] tries to grab on startup. The amount may be given as </dd>
<p> <i>n</i><br />
 <i>n</i><code>B</code></p>
<dl>
<dt>
</dt><dd> measured in bytes</dd></dl>
<p> <i>n</i><br />
 <i>n</i><code>W</code></p>
<dl>
<dt>
</dt><dd> measured in machine words (4&#215;<i>n</i> on 32-bit platforms, 8&#215;<i>n</i> on 64-bit platforms)</dd></dl>
<p> <i>n</i><code>K</code><br />
 <i>n</i><code>KB</code></p>
<dl>
<dt>
</dt><dd> measured in kilobytes</dd></dl>
<p> <i>n</i><code>KW</code></p>
<dl>
<dt>
</dt><dd> measured in kilowords</dd></dl>
<p> <i>n</i><code>M</code><br />
 <i>n</i><code>MB</code></p>
<dl>
<dt>
</dt><dd> measured in megabytes</dd></dl>
<p> <i>n</i><code>MW</code></p>
<dl>
<dt>
</dt><dd> measured in megawords</dd></dl>
<p> The default is 3 megabytes. The argument is constrained above 100 KB. </p>
<p> This version of <i></i><code>CLISP</code>[6] is not likely to actually use the entire <i>memory-size</i> since garbage-collection will periodically reduce the amount of used memory. It is therefore common to specify 10 MB even if only 2 MB are going to be used.</dl>
<p> <code>-L</code> <i>language</i></p>
<dl>
<dt>
</dt><dd> Specifies the language <i></i><code>CLISP</code>[6] uses to communicate with the user. This may be one of <code>english</code>, <code>german</code>, <code>french</code>, <code>spanish</code>, <code>dutch</code>, <code>russian</code>, <code>danish</code>. Other languages may be specified through the <i>environment variable</i>[12] <code>LANG</code>, provided the corresponding message catalog is installed. The language may be changed dynamically using the <i>SYMBOL-MACRO</i>[10] <i>CUSTOM:*CURRENT-LANGUAGE*</i>.</dd></dl>
<p> <code>-N</code> <i>locale-dir</i></p>
<dl>
<dt>
</dt><dd> Specifies the base directory of locale files. <i></i><code>CLISP</code>[6] will search its message catalogs in <i>locale-dir</i><i>/</i><i>language</i><i>/LC_MESSAGES/clisp.mo</i>. This directory may be changed dynamically using the <i>SYMBOL-MACRO</i>[10] <i>CUSTOM:*CURRENT-LANGUAGE*</i>.</dd></dl>
<p> <code>-E</code><i>domain</i><i>encoding</i></p>
<dl>
<dt>
</dt><dd> Specifies the encoding used for the given domain, overriding the default which depends on the <i>environment variable</i>[12]s <code>LC_ALL</code>, <code>LC_CTYPE</code>, <code>LANG</code>. <i>domain</i> can be </dd>
<p> <code>file</code></p>
<dl>
<dt>
</dt><dd> affecting <i>CUSTOM:*DEFAULT-FILE-ENCODING*</i></dd></dl>
<p> <code>pathname</code></p>
<dl>
<dt>
</dt><dd> affecting <i>CUSTOM:*PATHNAME-ENCODING*</i></dd></dl>
<p> <code>terminal</code></p>
<dl>
<dt>
</dt><dd> affecting <i>CUSTOM:*TERMINAL-ENCODING*</i></dd></dl>
<p> <code>foreign</code></p>
<dl>
<dt>
</dt><dd> affecting <i>CUSTOM:*FOREIGN-ENCODING*</i></dd></dl>
<p> <code>misc</code></p>
<dl>
<dt>
</dt><dd> affecting <i>CUSTOM:*MISC-ENCODING*</i></dd></dl>
<p> <i>blank</i></p>
<dl>
<dt>
</dt><dd> affecting all of the above.</dd></dl>
<p> Warning Note that the values of these <i>SYMBOL-MACRO</i>[10]s that have been saved in a memory image are ignored: these <i>SYMBOL-MACRO</i>[10]s are reset based on the OS environment <code>after</code> the memory image is loaded. You have to use the RC file, <i>CUSTOM:*INIT-HOOKS*</i> or init function to set them on startup, but it is best to set the aforementioned <i>environment variable</i>[12]s appropriately for consistency with other programs. See Section 31.1, lqCustomizing CLISP Process Initialization and Terminationrq.</dl>
<p> <code>-q</code><br />
 <code>&#8211;quiet</code><br />
 <code>&#8211;silent</code><br />
 <code>-v</code><br />
 <code>&#8211;verbose</code></p>
<dl>
<dt>
</dt><dd> Change verbosity level: by default, <i></i><code>CLISP</code>[6] displays a banner at startup and a good-bye message when quitting, and initializes <i>*LOAD-VERBOSE*</i>[13] and <i>*COMPILE-VERBOSE*</i>[14] to <i></i><code>T</code>[15], and <i>*LOAD-PRINT*</i>[13] and <i>*COMPILE-PRINT*</i>[14] to <i></i><code>NIL</code>[16], as per [ANSI CL standard]. The first <code>-q</code> removes the banner and the good-bye message, the second sets variables <i>*LOAD-VERBOSE*</i>[13], <i>*COMPILE-VERBOSE*</i>[14] and <i>CUSTOM:*SAVEINITMEM-VERBOSE*</i> to <i></i><code>NIL</code>[16]. The first <code>-v</code> sets variables <i>CUSTOM:*REPORT-ERROR-PRINT-BACKTRACE*</i>, <i>*LOAD-PRINT*</i>[13] and <i>*COMPILE-PRINT*</i>[14] to <i></i><code>T</code>[15], the second sets <i>CUSTOM:*LOAD-ECHO*</i> to <i></i><code>T</code>[15]. These settings affect the output produced by <code>-i</code> and <code>-c</code> options. Note that these settings persist into the <i>read-eval-print loop</i>[2]. Repeated <code>-q</code> and <code>-v</code> cancel each other, e.g., <code>-q -q -v -v -v</code> is equivalent to <code>-v</code>.</dd></dl>
<p> <code>-on-error</code> <i>action</i></p>
<dl>
<dt>
</dt><dd> Override (or force) the batch mode imposed by <code>-c</code>, <code>-x</code>, and <i>lisp-file</i>, depending on <i>action</i>:.PP appease</dd>
<dl>
<dt>
</dt><dd> <i>continuable</i>[17] <i>ERROR</i>[18]s are turned into <i>WARNING</i>[19]s (with <code>EXT:APPEASE-CERRORS</code>) other <i>ERROR</i>[18]s are handled in the default way</dd></dl>
<p> debug</p>
<dl>
<dt>
</dt><dd> <i>ERROR</i>[18]s <i></i><code>INVOKE-DEBUGGER</code>[20] (the normal <i>read-eval-print loop</i>[2] behavior)</dd></dl>
<p> abort</p>
<dl>
<dt>
</dt><dd> <i>continuable</i>[17] <i>ERROR</i>[18]s are appeased, other <i>ERROR</i>[18]s are <i></i><code>ABORT</code>[21]ed with <code>EXT:ABORT-ON-ERROR</code></dd></dl>
<p> exit</p>
<dl>
<dt>
</dt><dd> <i>continuable</i>[17] <i>ERROR</i>[18]s are appeased, other <i>ERROR</i>[18]s terminate <i></i><code>CLISP</code>[6] with <code>EXT:EXIT-ON-ERROR</code></dd></dl>
<p> See also <code>EXT:SET-GLOBAL-HANDLER</code>.</dl>
<p> <code>-repl</code></p>
<dl>
<dt>
</dt><dd> Start an interactive <i>read-eval-print loop</i>[2] after processing the <code>-c</code>, <code>-x</code>, and <i>lisp-file</i> options and on any <i>ERROR</i>[18] <i></i><code>SIGNAL</code>[22]ed during that processing.</dd></dl>
<p> <code>-w</code></p>
<dl>
<dt>
</dt><dd> Wait for a keypress after program termination.</dd></dl>
<p> <code>-I</code></p>
<dl>
<dt>
</dt><dd> Interact better with <i>Emacs</i>[23] (useful when running <i></i><code>CLISP</code>[6] under <i>Emacs</i>[23] using <i>SLIME</i>[24], <i>ILISP</i>[25] et al). With this option, <i></i><code>CLISP</code>[6] interacts in a way that <i>Emacs</i>[23] can deal with: </dd>
<dl>
<dt>
</dt><dd> *unnecessary prompts are not suppressed.</dd></dl>
<dl>
<dt>
</dt><dd> *The <i>GNU</i>[8] <i>readline</i>[26] library treats TAB (see TAB key) as a normal self-inserting character (see Q: A.4.6).</dd></dl>
</dl>
<p> <code>-ansi</code></p>
<dl>
<dt>
</dt><dd> Comply with the [ANSI CL standard] specification even where <i></i><code>CLISP</code>[6] has been traditionally different by setting the <i>SYMBOL-MACRO</i>[10] <i>CUSTOM:*ANSI*</i> to <i></i><code>T</code>[15].</dd></dl>
<p> <code>-traditional</code></p>
<dl>
<dt>
</dt><dd> Traditional: reverses the residual effects of <code>-ansi</code> in the saved memory image.</dd></dl>
<p> <code>-modern</code></p>
<dl>
<dt>
</dt><dd> Provides a modern view of symbols: at startup the <i>*PACKAGE*</i>[27] variable will be set to the lqCS-COMMON-LISP-USERrq package, and the <i>*PRINT-CASE*</i>[28] will be set to <code>:DOWNCASE</code>. This has the effect that symbol lookup is case-sensitive (except for keywords and old-style packages) and that keywords and uninterned symbols are printed with lower-case preferrence. See Section 11.5, lqPackage Case-Sensitivityrq.</dd></dl>
<p> <code>-p</code> <i>package</i></p>
<dl>
<dt>
</dt><dd> At startup the value of the variable <i>*PACKAGE*</i>[27] will be set to the package named <i>package</i>. The default is the value of <i>*PACKAGE*</i>[27] when the image was saved, normally <i>lqCOMMON-LISP-USERrq</i>[29].</dd></dl>
<p> <code>-C</code></p>
<dl>
<dt>
</dt><dd> Compile when loading: at startup the value of the variable <i>CUSTOM:*LOAD-COMPILING*</i> will be set to <i></i><code>T</code>[15]. Code being <i></i><code>LOAD</code>[30]ed will then be <i></i><code>COMPILE</code>[31]d on the fly. This results in slower loading, but faster execution.</dd></dl>
<p> <code>-norc</code></p>
<dl>
<dt>
</dt><dd> Normally <i></i><code>CLISP</code>[6] loads the user <i>lqrun controlrq (RC)</i>[32] file on startup (this happens <code>after</code> the <code>-C</code> option is processed). The file loaded is <i>.clisprc.lisp</i> or <i>.clisprc.fas</i> in the home directory <i></i><code>USER-HOMEDIR-PATHNAME</code>[33], whichever is newer. This option, <code>-norc</code>, prevents loading of the RC file.</dd></dl>
<p> <code>-lp</code> <i>directory</i></p>
<dl>
<dt>
</dt><dd> Specifies directories to be added to <i>CUSTOM:*LOAD-PATHS*</i> at startup. This is done <code>after</code> loading the RC file (so that it does not override the command-line option) but <code>before</code> loading the init-files specified by the <code>-i</code> options (so that the init-files will be searched for in the specified directories). Several <code>-lp</code> options can be given; all the specified directories will be added.</dd></dl>
<p> <code>-i</code> <i>init-file</i></p>
<dl>
<dt>
</dt><dd> Specifies initialization files to be <i></i><code>LOAD</code>[30]ed at startup. These should be lisp files (source or compiled). Several <code>-i</code> options can be given; all the specified files will be loaded in order.</dd></dl>
<p> <code>-c</code> <i>lisp-file</i></p>
<dl>
<dt>
</dt><dd> Compiles the specified <i>lisp-file</i>s to bytecode (<i>*.fas</i>). The compiled files can then be <i></i><code>LOAD</code>[30]ed instead of the sources to gain efficiency.</dd></dl>
<p> <code>-o</code> <i>outputfile</i></p>
<dl>
<dt>
</dt><dd> Specifies the output file or directory for the compilation of the last specified <i>lisp-file</i>.</dd></dl>
<p> <code>-l</code></p>
<dl>
<dt>
</dt><dd> Produce a bytecode <i></i><code>DISASSEMBLE</code>[34] listing (<i>*.lis</i>) of the files being compiled. Useful only for debugging. See Section 24.1, lqFunction COMPILE-FILErq for details.</dd></dl>
<p> <code>-x</code> <i>expressions</i></p>
<dl>
<dt>
</dt><dd> Executes a series of arbitrary expressions instead of a <i>read-eval-print loop</i>[2]. The values of the expressions will be output to <i>*STANDARD-OUTPUT*</i>[35]. Due to the argument processing done by the shell, the <i>expressions</i> must be enclosed in double quotes, and double quotes and backslashes must be escaped with backslashes.</dd></dl>
<p> <i>lisp-file</i> [ <i>argument</i> &#8230; ]</p>
<dl>
<dt>
</dt><dd> Loads and executes a <i>lisp-file</i>, as described in Script execution. There will be no <i>read-eval-print loop</i>[2]. Before <i>lisp-file</i> is loaded, the variable <i>EXT:*ARGS*</i> will be bound to a list of strings, representing the <i>argument</i>s. The first line of <i>lisp-file</i> may start with <code>#!</code>, thus permitting <i></i><code>CLISP</code>[6] to be used as a script interpreter. If <i>lisp-file</i> is <code>&#8211;</code>, the <i>*STANDARD-INPUT*</i>[35] is used instead of a file. </dd>
<p> This option is <i>disabled</i> if the memory image was created by <code>EXT:SAVEINITMEM</code> with <i></i><code>NIL</code>[16] <code>:SCRIPT</code> argument. In that case the <i>LIST</i>[36] <i>EXT:*ARGS*</i> starts with <i>lisp-file</i>. </p>
<p> This option must be the last one. </p>
<p> No RC file will be executed.</dl>
<p> As usual, <code>&#8212;</code> stops option processing and places all remaining command line arguments into <i>EXT:*ARGS*</i>.</p>
<h2>LANGUAGE REFERENCE</h2>
<p> The language implemented is <i>ANSI[38]</i>[37] <i></i><code>Common Lisp</code>[1]. The implementation mostly conforms to the ANSI Common Lisp standard, see Section 31.10, lqMaximum ANSI CL compliancerq. </p>
<p> [ANSI CL] ANSI CL standard1994. ANSI INCITS 226-1994 (R1999) <i>Information Technology &#8211; Programming Language &#8211; Common Lisp</i>[39] [formerly ANSI X3.226-1994 (R1999)].</p>
<h2>USAGE</h2>
<p> <code>help</code></p>
<dl>
<dt>
</dt><dd> get context-sensitive on-line help, see Chapter 25, Environment.</dd></dl>
<p> (<code>APROPOS</code> <i>name</i>)</p>
<dl>
<dt>
</dt><dd> list the <i>SYMBOL</i>[40]s matching <i>name</i>.</dd></dl>
<p> (<code>DESCRIBE</code> <i>symbol</i>)</p>
<dl>
<dt>
</dt><dd> describe the <i>symbol</i>.</dd></dl>
<p> (exit)<br />
 (quit)<br />
 (bye)</p>
<dl>
<dt>
</dt><dd> quit <i></i><code>CLISP</code>[6].</dd></dl>
<p> EOF (Control+D on <i></i><code>UNIX</code>[41])</p>
<dl>
<dt>
</dt><dd> leave the current level of the <i>read-eval-print loop</i>[2] (see also Section 1.1, lqSpecial Symbols rq).</dd></dl>
<p> arrow keys</p>
<dl>
<dt>
</dt><dd> for editing and viewing the input history, using the <i>GNU</i>[8] <i>readline</i>[26] library.</dd></dl>
<p> TAB key</p>
<dl>
<dt>
</dt><dd> Context sensitive: </dd>
<dl>
<dt>
</dt><dd> *If you are in the lqfunction positionrq (in the first symbol after an opening paren or in the first symbol after a <i>#&#8217;</i>[43]), the completion is limited to the symbols that name functions.</dd></dl>
<dl>
<dt>
</dt><dd> *If you are in the &quot;filename position&quot; (inside a string after <i>#P</i>[44]), the completion is done across file names, <i>bash</i>[45]-style.</dd></dl>
<dl>
<dt>
</dt><dd> *If you have not typed anything yet, you will get a help message, as if by the <code>help</code> command.</dd></dl>
<dl>
<dt>
</dt><dd> *If you have not started typing the next symbol (i.e., you are at a whitespace), the current function or macro is <code>DESCRIBE</code>d.</dd></dl>
<dl>
<dt>
</dt><dd> *Otherwise, the symbol you are currently typing is completed.</dd></dl>
<dl>
</dl>
</dl>
<h2>FILES</h2>
<p> <code>clisp</code></p>
<dl>
<dt>
</dt><dd> startup driver (a script or an executable)</dd></dl>
<p> <i>lisp.run</i><br />
 <i>lisp.exe</i></p>
<dl>
<dt>
</dt><dd> main executable (runtime)</dd></dl>
<p> <i>lispinit.mem</i></p>
<dl>
<dt>
</dt><dd> initial memory image</dd></dl>
<p> <i>config.lisp</i></p>
<dl>
<dt>
</dt><dd> site-dependent configuration (should have been customized before <i></i><code>CLISP</code>[6] was built); see Section 31.12, lqCustomizing CLISP behaviorrq</dd></dl>
<p> <i>*.lisp</i></p>
<dl>
<dt>
</dt><dd> lisp source</dd></dl>
<p> <i>*.fas</i></p>
<dl>
<dt>
</dt><dd> lisp code, compiled by <i></i><code>CLISP</code>[6]</dd></dl>
<p> <i>*.lib</i></p>
<dl>
<dt>
</dt><dd> lisp source library information, generated by <code>COMPILE-FILE</code>, see Section 24.3, lqFunction REQUIRErq.</dd></dl>
<p> <i>*.c</i></p>
<dl>
<dt>
</dt><dd> C code, compiled from lisp source by <i></i><code>CLISP</code>[6] (see Section 32.3, lqThe Foreign Function Call Facilityrq)</dd></dl>
<p> For the <i></i><code>CLISP</code>[6] source files, see Chapter 34, The source files of CLISP.</p>
<h2>ENVIRONMENT</h2>
<p> All <i>environment variable</i>[12]s that <i></i><code>CLISP</code>[6] uses are read at most once. </p>
<p> <code>CLISP_LANGUAGE</code></p>
<dl>
<dt>
</dt><dd> specifies the language <i></i><code>CLISP</code>[6] uses to communicate with the user. The legal values are identical to those of the <code>-L</code> option which can be used to override this <i>environment variable</i>[12].</dd></dl>
<p> <code>LC_CTYPE</code></p>
<dl>
<dt>
</dt><dd> specifies the locale which determines the character set in use. The value can be of the form <i>language</i> or <i>language</i><code>_</code><i>country</i> or <i>language</i><code>_</code><i>country</i><code>.</code><i>charset</i>, where <i>language</i> is a two-letter ISO 639 language code (lower case), <i>country</i> is a two-letter ISO 3166 country code (upper case). <i>charset</i> is an optional character set specification, and needs normally not be given because the character set can be inferred from the language and country. This <i>environment variable</i>[12] can be overridden with the <code>-Edomain encoding</code> option.</dd></dl>
<p> <code>LANG</code></p>
<dl>
<dt>
</dt><dd> specifies the language <i></i><code>CLISP</code>[6] uses to communicate with the user, unless it is already specified through the <i>environment variable</i>[12] <code>CLISP_LANGUAGE</code> or the <code>-L</code> option. It also specifies the locale determining the character set in use, unless already specified through the <i>environment variable</i>[12] <code>LC_CTYPE</code>. The value may begin with a two-letter ISO 639 language code, for example <code>en</code>, <code>de</code>, <code>fr</code>.</dd></dl>
<p> <code>HOME</code><br />
 <code>USER</code></p>
<dl>
<dt>
</dt><dd> used for determining the value of the function <i></i><code>USER-HOMEDIR-PATHNAME</code>[33].</dd></dl>
<p> <code>SHELL</code><br />
 <code>COMSPEC</code></p>
<dl>
<dt>
</dt><dd> is used to find the interactive command interpreter called by <code>EXT:SHELL</code>.</dd></dl>
<p> <code>TERM</code></p>
<dl>
<dt>
</dt><dd> determines the screen size recognized by the pretty printer.</dd></dl>
<p> <code>ORGANIZATION</code></p>
<dl>
<dt>
</dt><dd> for <i></i><code>SHORT-SITE-NAME</code>[46] and <i></i><code>LONG-SITE-NAME</code>[46] in <i>config.lisp</i>.</dd></dl>
<p> <code>CLHSROOT</code></p>
<dl>
<dt>
</dt><dd> for <code>CUSTOM:CLHS-ROOT</code> in <i>config.lisp</i>.</dd></dl>
<p> <code>IMPNOTES</code></p>
<dl>
<dt>
</dt><dd> for <code>CUSTOM:IMPNOTES-ROOT</code> in <i>config.lisp</i>.</dd></dl>
<p> <code>EDITOR</code></p>
<dl>
<dt>
</dt><dd> for <code>editor-name</code> in <i>config.lisp</i>.</dd></dl>
<p> <code>LOGICAL_HOST_</code><i>host</i><code>_FROM</code><br />
 <code>LOGICAL_HOST_</code><i>host</i><code>_TO</code><br />
 <code>LOGICAL_HOST_</code><i>host</i></p>
<dl>
<dt>
</dt><dd> for <i>CUSTOM:*LOAD-LOGICAL-PATHNAME-TRANSLATIONS-DATABASE*</i></dd></dl>
<h2>SEE ALSO</h2>
<dl>
<dt>
</dt><dd> CLISP impnotes</dd>
<dt>
</dt><dd> <i></i><code>CMU CL</code>[47] &#8211; <code>cmucl</code>(1)</dd>
<dt>
</dt><dd> <i>Emacs</i>[23] &#8211; <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1)</dd>
<dt>
</dt><dd> <i>XEmacs</i>[48] &#8211; <code><a href="/docs/linux/man/1-xemacs/">xemacs</a></code>(1)</dd></dl>
<h2>BUGS</h2>
<p> When you encounter a bug in <i></i><code>CLISP</code>[6] or in its documentation (this manual page or CLISP impnotes), please report it to the <i></i><code>CLISP</code>[6] <i>SourceForge bug tracker</i>[49]. </p>
<p> <i>Before</i> submitting a bug report, please take the following basic steps to make the report more useful: </p>
<dl>
<dt>
</dt><dd> 1.Please do a clean build (remove your build directory and build <i></i><code>CLISP</code>[6] with <code>./configure &#8211;cbc build</code> or at least do a <code>make distclean</code> before <code>make</code>).</dd></dl>
<dl>
<dt>
</dt><dd> 2.If you are reporting a lqhard crashrq (segmentation fault, bus error, core dump etc), please do <code>./configure </code><code>&#8211;with-debug</code><code> &#8211;cbc build-g ; cd build-g; gdb lisp.run</code>, then load the appropriate linking set by either <code>base</code> or <code>full</code> <i></i><code>gdb</code>[50] command, and report the backtrace (see also Q: A.1.1.10).</dd></dl>
<dl>
<dt>
</dt><dd> 3.If you are using pre-built binaries and experience a hard crash, the problem is likely to be in the incompatibilities between the platform on which the binary was built and yours; please try compiling the sources and report the problem if it persists.</dd></dl>
<p> When submitting a bug report, please specify the following information: </p>
<dl>
<dt>
</dt><dd> 1.What is your platform (<code>uname -a</code> on a <i></i><code>UNIX</code>[41] system)? Compiler version? <i>GNU</i>[8] <i>libc</i>[51] version (on <i>GNU</i>[8]/<i>Linux</i>[52])?</dd></dl>
<dl>
<dt>
</dt><dd> 2.Where did you get the sources or binaries? When? (Absolute dates, e.g., lq2006-01-17rq, are preferred over the relative ones, e.g., lq2 days agorq).</dd></dl>
<dl>
<dt>
</dt><dd> 3.How did you build <i></i><code>CLISP</code>[6]? (What command, options &amp;c.)</dd></dl>
<dl>
<dt>
</dt><dd> 4.What is the output of <code>clisp &#8211;version</code>?</dd></dl>
<dl>
<dt>
</dt><dd> 5.Please supply the full output (copy and paste) of all the error messages, as well as detailed instructions on how to reproduce them.</dd></dl>
<h2>PROJECTS</h2>
<dl>
<dt>
</dt><dd> *Enhance the compiler so that it can inline local functions.</dd></dl>
<dl>
<dt>
</dt><dd> *Add Multi-Threading capabilities, via OS threads.</dd></dl>
<dl>
<dt>
</dt><dd> *Embed <i></i><code>CLISP</code>[6] in <i>VIM</i>[53].</dd></dl>
<h2>AUTHORS</h2>
<p> <code>Bruno Haible</code> &lt;<i><a rel="nofollow" href="http://www.haible.de/bruno/">http://www.haible.de/bruno/</a></i>&gt; </p>
<dl>
<dt>
</dt><dd> The original author and long-time maintainer.</dd></dl>
<p> <code>Michael Stoll</code> &lt;<i><a rel="nofollow" href="http://www.faculty.iu-bremen.de/mstoll/">http://www.faculty.iu-bremen.de/mstoll/</a></i>&gt; </p>
<dl>
<dt>
</dt><dd> The original author.</dd></dl>
<p> <code>Sam Steingold</code> &lt;<i><a rel="nofollow" href="http://sds.podval.org/">http://sds.podval.org/</a></i>&gt; </p>
<dl>
<dt>
</dt><dd> Co-maintainer since 1998.</dd></dl>
<p> <code>Others</code> </p>
<dl>
<dt>
</dt><dd> See <i>COPYRIGHT</i> (file in the CLISP sources) for the list of other contributors and the license.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1992-2008 Bruno Haible<br />
 Copyright &#169; 1998-2008 Sam Steingold </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> <code>Common Lisp</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lisp.org">http://www.lisp.org</a></dd></dl>
<dt> 2.</dt>
<dd> read-eval-print loop</dd>
<dl>
<dt>
</dt><dd> sec_25-1-1</dd></dl>
<dt> 3.</dt>
<dd> <code>READ</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_readcm_re_g-whitespace.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_readcm_re_g-whitespace.html</a></dd></dl>
<dt> 4.</dt>
<dd> <code>EVAL</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_eval.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_eval.html</a></dd></dl>
<dt> 5.</dt>
<dd> <code>PRINT</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_writecm_p_rintcm_princ.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_writecm_p_rintcm_princ.html</a></dd></dl>
<dt> 6.</dt>
<dd> <code>CLISP</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://clisp.cons.org">http://clisp.cons.org</a></dd></dl>
<dt> 7.</dt>
<dd> <code>LISP-IMPLEMENTATION-VERSION</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_lisp-impl_tion-version.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_lisp-impl_tion-version.html</a></dd></dl>
<dt> 8.</dt>
<dd> GNU</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.gnu.org">http://www.gnu.org</a></dd></dl>
<dt> 9.</dt>
<dd> GPL</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.gnu.org/copyleft/gpl.html">http://www.gnu.org/copyleft/gpl.html</a></dd></dl>
<dt>10.</dt>
<dd> SYMBOL-MACRO</dd>
<dl>
<dt>
</dt><dd> mac_define-symbol-macro</dd></dl>
<dt>11.</dt>
<dd> <code>gzip</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.gzip.org/">http://www.gzip.org/</a></dd></dl>
<dt>12.</dt>
<dd> environment variable</dd>
<dl>
<dt>
</dt><dd> basedefs/xbd_chap08.html</dd></dl>
<dt>13.</dt>
<dd> <i>*LOAD-VERBOSE*</i></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/var_stload-pr_ad-verbosest.html">http://www.lispworks.com/documentation/HyperSpec/Body/var_stload-pr_ad-verbosest.html</a></dd></dl>
<dt>14.</dt>
<dd> <i>*COMPILE-VERBOSE*</i></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/var_stcompile_le-verbosest.html">http://www.lispworks.com/documentation/HyperSpec/Body/var_stcompile_le-verbosest.html</a></dd></dl>
<dt>15.</dt>
<dd> <code>T</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/convar_t.html">http://www.lispworks.com/documentation/HyperSpec/Body/convar_t.html</a></dd></dl>
<dt>16.</dt>
<dd> <code>NIL</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/convar_nil.html">http://www.lispworks.com/documentation/HyperSpec/Body/convar_nil.html</a></dd></dl>
<dt>17.</dt>
<dd> continuable</dd>
<dl>
<dt>
</dt><dd> clhs/glo</dd></dl>
<dt>18.</dt>
<dd> ERROR</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/contyp_error.html">http://www.lispworks.com/documentation/HyperSpec/Body/contyp_error.html</a></dd></dl>
<dt>19.</dt>
<dd> WARNING</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/contyp_warning.html">http://www.lispworks.com/documentation/HyperSpec/Body/contyp_warning.html</a></dd></dl>
<dt>20.</dt>
<dd> <code>INVOKE-DEBUGGER</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_invoke-debugger.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_invoke-debugger.html</a></dd></dl>
<dt>21.</dt>
<dd> <code>ABORT</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_abortcm_c_cm_use-value.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_abortcm_c_cm_use-value.html</a></dd></dl>
<dt>22.</dt>
<dd> <code>SIGNAL</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_signal.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_signal.html</a></dd></dl>
<dt>23.</dt>
<dd> Emacs</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.gnu.org/software/emacs/">http://www.gnu.org/software/emacs/</a></dd></dl>
<dt>24.</dt>
<dd> SLIME</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://common-lisp.net/project/slime/">http://common-lisp.net/project/slime/</a></dd></dl>
<dt>25.</dt>
<dd> ILISP</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://sourceforge.net/projects/ilisp/">http://sourceforge.net/projects/ilisp/</a></dd></dl>
<dt>26.</dt>
<dd> readline</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://tiswww.case.edu/php/chet/readline/readline.html">http://tiswww.case.edu/php/chet/readline/readline.html</a></dd></dl>
<dt>27.</dt>
<dd> <i>*PACKAGE*</i></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/var_stpackagest.html">http://www.lispworks.com/documentation/HyperSpec/Body/var_stpackagest.html</a></dd></dl>
<dt>28.</dt>
<dd> <i>*PRINT-CASE*</i></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/var_stprint-casest.html">http://www.lispworks.com/documentation/HyperSpec/Body/var_stprint-casest.html</a></dd></dl>
<dt>29.</dt>
<dd> lqCOMMON-LISP-USERrq</dd>
<dl>
<dt>
</dt><dd> sec_11-1-2-2</dd></dl>
<dt>30.</dt>
<dd> <code>LOAD</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_load.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_load.html</a></dd></dl>
<dt>31.</dt>
<dd> <code>COMPILE</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_compile.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_compile.html</a></dd></dl>
<dt>32.</dt>
<dd> lqrun<br />
&nbsp;<wbr>&nbsp;<wbr>controlrq&nbsp;<wbr>(RC)</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.faqs.org/docs/artu/ch10s03.html">http://www.faqs.org/docs/artu/ch10s03.html</a></dd></dl>
<dt>33.</dt>
<dd> <code>USER-HOMEDIR-PATHNAME</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_user-homedir-pathname.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_user-homedir-pathname.html</a></dd></dl>
<dt>34.</dt>
<dd> <code>DISASSEMBLE</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_disassemble.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_disassemble.html</a></dd></dl>
<dt>35.</dt>
<dd> <i>*STANDARD-OUTPUT*</i></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/var_stdebug-i_ace-outputst.html">http://www.lispworks.com/documentation/HyperSpec/Body/var_stdebug-i_ace-outputst.html</a></dd></dl>
<dt>36.</dt>
<dd> LIST</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/syscla_list.html">http://www.lispworks.com/documentation/HyperSpec/Body/syscla_list.html</a></dd></dl>
<dt>37.</dt>
<dd> ANSI</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.ansi.org/">http://www.ansi.org/</a></dd></dl>
<dt>38.</dt>
<dd> The American National Standards Institute</dd>
<dt>39.</dt>
<dd> Information Technology &#8211; Programming Language &#8211; Common Lisp</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://webstore.ansi.org/RecordDetail.aspx?sku=ANSI+INCITS+226-1994+(R1999)">http://webstore.ansi.org/RecordDetail.aspx?sku=ANSI+INCITS+226-1994+(R1999)</a></dd></dl>
<dt>40.</dt>
<dd> SYMBOL</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/syscla_symbol.html">http://www.lispworks.com/documentation/HyperSpec/Body/syscla_symbol.html</a></dd></dl>
<dt>41.</dt>
<dd> <code>UNIX</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.unix.org/online.html">http://www.unix.org/online.html</a></dd></dl>
<dt>42.</dt>
<dd> <i>Win32</i></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://winehq.org/">http://winehq.org/</a></dd></dl>
<dt>43.</dt>
<dd> #&#8217;</dd>
<dl>
<dt>
</dt><dd> sec_2-4-8-2</dd></dl>
<dt>44.</dt>
<dd> #P</dd>
<dl>
<dt>
</dt><dd> sec_2-4-8-14</dd></dl>
<dt>45.</dt>
<dd> bash</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.gnu.org/software/bash/">http://www.gnu.org/software/bash/</a></dd></dl>
<dt>46.</dt>
<dd> <code>SHORT-SITE-NAME</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.lispworks.com/documentation/HyperSpec/Body/fun_short-sit_ng-site-name.html">http://www.lispworks.com/documentation/HyperSpec/Body/fun_short-sit_ng-site-name.html</a></dd></dl>
<dt>47.</dt>
<dd> <code>CMU CL</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.cons.org/cmucl/">http://www.cons.org/cmucl/</a></dd></dl>
<dt>48.</dt>
<dd> XEmacs</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.xemacs.org">http://www.xemacs.org</a></dd></dl>
<dt>49.</dt>
<dd> SourceForge bug tracker</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://sourceforge.net/tracker/?func=add">http://sourceforge.net/tracker/?func=add</a>&amp;group_id=1355&amp;atid=101355</dd></dl>
<dt>50.</dt>
<dd> <code>gdb</code></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://sources.redhat.com/gdb/">http://sources.redhat.com/gdb/</a></dd></dl>
<dt>51.</dt>
<dd> libc</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.gnu.org/software/libc/">http://www.gnu.org/software/libc/</a></dd></dl>
<dt>52.</dt>
<dd> <i>Linux</i></dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.linux.org/">http://www.linux.org/</a></dd></dl>
<dt>53.</dt>
<dd> VIM</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.vim.org">http://www.vim.org</a></dd></dl>
</dl>
