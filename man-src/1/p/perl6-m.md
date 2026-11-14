---
title: "perl6-m(1)"
name: "perl6-m"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl6-m/"
---

<h2 class="name">NAME</h2>
 

 perl6 - Rakudo Perl 6 Compiler 

<h2>SYNOPSIS</h2>

 <pre><code>
perl6[switches][--][programfile][arguments]
</code></pre>

<h2>DESCRIPTION</h2>

 With no arguments, enters a <font SIZE="-1">REPL.</font> With a <tt>&quot;[programfile]&quot;</tt> or the <tt>&quot;-e&quot;</tt> option, compiles the given program and by default also executes the compiled code. 

 
  -c                   check syntax only (runs BEGIN and CHECK blocks)
  --doc                extract documentation and print it as text
  -e program           one line of program, strict is enabled by default
  -h, --help           display this help text
  -n                   run program once for each line of input
  -p                   same as -n, but also print $_ at the end of lines
  -I path              adds the path to the module search path
  -M module            loads the module prior to running the program
  --target=[stage]     specify compilation stage to emit
  --optimize=[level]   use the given level of optimization (0..3)
  --encoding=[mode]    specify string encoding mode
  -o, --output=[name]  specify name of output file
  -v, --version        display version information
  --stagestats         display time spent in the compilation stages
  --ll-exception       display a low level backtrace on errors
  --profile            write profile information as HTML file (MoarVM)
  --profile-filename   provide a different filename (also allows .json)
  --doc=[module]       Use Pod::To::[module] to render inline documentation.
 

 Note that only boolean single-letter options may be bundled. 

 The supported values for <tt>&quot;--target&quot;</tt> are: 

 <pre><code>
Target Backend Description == == == == == == = == == == == == =
                                                                  parse all a representation of the parse tree
                                                                      ast all an abstract syntax
                                                                      tree(before optimizations)
                                                                          optimize all an abstract syntax
                                                                          tree(after optimizations)
                                                                              mbc MoarVM MoarVM byte code
                                                                                  jar JVM JVM archive
</code></pre> 

 For <tt>&quot;--profile-filename&quot;</tt>, specifying a name ending in <tt>&quot;.json&quot;</tt> will write a raw <font SIZE="-1">JSON</font> profile dump. The default if this is omitted is <tt>&quot;profile-</tt>[timestamp]<tt>.html&quot;</tt>.

<h2>ENVIRONMENT VARIABLES</h2>

 Rakudo's behavior can be tweaked by a (growing) number of environment variables; this section attempts to document all those currently in use.

<h3>Module Loading</h3>

<dl>
<dt>&quot;RAKUDOLIB&quot;, &quot;PERL6LIB&quot; (<i>Str</i>; <i>src/core/Inc.pm</i>)
<dd> Appends a comma-delimited list of paths to <tt>@INC</tt>. <tt>&quot;RAKUDOLIB&quot;</tt> is evaluated first.
<dt>&quot;RAKUDO_MODULE_DEBUG&quot; (<i>Bool</i>; <i>src/Perl6/ModuleLoader.pm</i>)
<dd> Causes the module loader to print debugging information to standard error.</dl>

<h3>Error Message Verbosity and Strictness</h3>

<dl>
<dt>&quot;RAKUDO_NO_DEPRECATIONS&quot; (<i>Bool</i>; <i>src/core/Deprecations.pm</i>)
<dd> If true, suppresses deprecation warnings triggered by the <tt>&quot;is DEPRECATED&quot;</tt> trait.
<dt>&quot;RAKUDO_DEPRECATIONS_FATAL&quot; (<i>Bool</i>; <i>src/core/Deprecations.pm</i>)
<dd> If true, deprecation warnings become thrown exceptions.
<dt>&quot;RAKUDO_VERBOSE_STACKFRAME&quot; (<i>UInt</i>; <i>src/core/Backtrace.pm</i>)
<dd> Displays source code in stack frames surrounded by the specified number of lines of context.
<dt>&quot;RAKUDO_BACKTRACE_SETTING&quot; (<i>Bool</i>; <i>src/core/Backtrace.pm</i>)
<dd> Controls whether .setting files are included in backtraces.</dl>

<h3>Affecting Precompilation</h3>

<dl>
<dt>&quot;RAKUDO_PREFIX&quot; (<i>Str</i>; <i>src/core/CompUnit/RepositoryRegistry.pm</i>)
<dd> When this is set, Rakudo will look for the standard repositories (perl, vendor, site) in the specified directory. This is intended as an escape hatch for build-time bootstrapping issues, where Rakudo may be built as an unprivileged user without write access to the runtime paths in <font SIZE="-1">NQP</font>'s config.
<dt>&quot;RAKUDO_PRECOMP_DIST&quot; (<i>src/core/CompUnit/PrecompilationRepository.pm</i>)
<dd>
<dt>&quot;RAKUDO_PRECOMP_LOADING&quot; (<i>src/core/CompUnit/PrecompilationRepository.pm</i>)
<dd>
<dt>&quot;RAKUDO_PRECOMP_WITH&quot; (<i>src/core/CompUnit/PrecompilationRepository.pm</i>)
<dd> These are internal variables for passing serialized state to precompilation jobs in child processes. Please do not set them manually.</dl>

<h3>Other</h3>

<dl>
<dt>&quot;RAKUDO_ERROR_COLOR&quot; (<i>Bool</i>; <i>src/core/Exception.pm</i>)
<dd> Controls whether to emit <font SIZE="-1">ANSI</font> codes for error highlighting. Defaults to true if unset, except on Win32.
<dt>&quot;RAKUDO_MAX_THREADS&quot; (<i>UInt</i>; <i>src/core/ThreadPoolScheduler.pm</i>)
<dd> Override the default maximum number of threads used by a thread pool.
<dt>&quot;TMPDIR&quot;, &quot;TEMP&quot;, &quot;TMP&quot; (<i>Str</i>; <i>src/core/IO/Spec/</i>)
<dd> The <tt>&quot;IO::Spec::Unix.tmpdir&quot;</tt> method will return <tt>$TMPDIR</tt> if it points to a directory with full access permissions for the current user, with a fallback default of <tt>'/tmp'</tt>. 

 <tt>&quot;IO::Spec::Cygwin&quot;</tt> and <tt>&quot;IO::Spec::Win32&quot;</tt> use more Win32-appropriate lists which also include the <tt>&quot;%TEMP%&quot;</tt> and <tt>&quot;%TMP%&quot;</tt> environment variables.
<dt>&quot;PATH&quot;, &quot;Path&quot; (<i>Str</i>; <i>src/core/IO/Spec/</i>)
<dd> The <tt>&quot;IO::Spec::Unix.path&quot;</tt> method splits <tt>$PATH</tt> as a shell would; i.e. as a colon-separated list. <tt>&quot;IO::Spec::Cygwin&quot;</tt> inherits this from <tt>&quot;IO::Spec::Unix&quot;</tt>. 

 <tt>&quot;IO::Spec::Win32.path&quot;</tt> will read the first defined of either <tt>&quot;%PATH%&quot;</tt> or <tt>&quot;%Path%&quot;</tt> as a semicolon-delimited list.</dl>

<h2>AUTHORS</h2>

 Written by the Rakudo contributors, see the <font SIZE="-1">CREDITS</font> file. 

 This manual page was written by Reini Urban, Moritz Lenz and the Rakudo contributors. 

<h2>Index</h2>


