---
title: "kayac(1)"
name: "kayac"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kayac/"
description: "Kayac – Compiler for the kaya language"
---

<h2>NAME</h2>
<p> Kayac &#8211; Compiler for the kaya language</p>
<h2>SYNOPSIS</h2>
<p> <code>kayac</code> <i>FILE [-L DIRECTORY [-L &#8230;]] [-libdir DIRECTORY [-libdir &#8230;]] [-force] [-nochase] [-noprelude] [-nortchecks|-fastvm] [-noopts] [-repl] [-pic] [-xmldocs] [-static] [-profile] [-T] [-seedkey STRING] [-dumptac] [-dumpraw] [-dumptree] [-dumpsimpl] [-dumpeqns] [-dumpcg] [-dumpdeps] [-keepc] [-showgcc]</i> </p>
<p> <code>kayac</code> <i>[-version|-v|-help|-h|-?|-installdir]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>kayac</code> compiles modules, programs and web applications in the Kaya programming language. </p>
<p> kayac will automatically compile dependencies as necessary provided that, for a dependency Foo, the source file is called Foo.k and is in the current working directory.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code> | <code>-h</code> | <code>-help</code></p>
<dd> Show usage summary </p>
<dt><code>-v</code> | <code>-version</code></p>
<dd> Show version number </p>
<dt><code>-installdir</code></p>
<dd> Show the directory in which the libraries are installed </p>
<dt><code>-L </code><i>DIRECTORY</i> | <code>-libdir </code><i>DIRECTORY</i></p>
<dd> Add DIRECTORY to the library search path. </p>
<dt><code>-force</code></p>
<dd> Force compilation even if kayac thinks it isn&#8217;t needed. </p>
<dt><code>-q</code></p>
<dd> Quiet compilation; don&#8217;t report which module is being built. </p>
<dt><code>-nochase</code></p>
<dd> Don&#8217;t chase up and compile dependencies. Implies <code>-force</code> and <code>-q</code>. </p>
<dt><code>-deprfail</code></p>
<dd> Fail compilation if a deprecated function is called. </p>
<dt><code>-noprelude</code></p>
<dd> Don&#8217;t import the Prelude (probably only useful when compiling the standard library). Compiling anything other than modules with this option is unlikely to work well. </p>
<dt><code>-noenvlibs</code></p>
<dd> kayac will ignore the <code>KAYA_LIBRARY_PATH</code> environment variable when compiling, and will not import from the compiled-in library directories (probably only useful when compiling the standard library) </p>
<dt><code>-nortchecks</code></p>
<dd> Disables some run-time checking. This speeds up the final program, at the cost of making errors harder to track down (and possibly introducing additional subtle errors where an exception would previously have occurred). Only recommended for bug free programs&#8230; </p>
<dt><code>-fastvm</code></p>
<dd> Uses a version of the Kaya VM that is optimised for applications such as web applications with a short run-time (a few seconds or less) for which it is significantly faster than the normal VM. However, for longer-running applications memory usage can grow very rapidly. This option implies and takes precedence over <code>-nortchecks</code>. </p>
<dt><code>-noopts</code></p>
<dd> Disables compile-time optimisations. Probably only useful for debugging purposes. </p>
<dt><code>-repl</code></p>
<dd> Read-Eval-Print loop mode. In this mode you can interactively test the behaviour of functions without needing to build a separate testing program, in a top-level interpreter. See <code><a href="/docs/linux/man/1-kaya/">kaya</a>(1)</code> for more information. This option implies -pic. </p>
<dt><code>-pic</code></p>
<dd> Use the -fPIC option of the C compiler to make position-independent code suitable for shared libraries. This option has no effect on Windows, where all code is position-independent. </p>
<dt><code>-xmldocs</code></p>
<dd> Generate XML documentation. This can then be converted into HTML or Manpage format using the KayaDoc module and the <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> tool. </p>
<dt><code>-static</code></p>
<dd> Statically link executables so that they can be run on a wider range of systems at the cost of signficantly increased file size. This is generally only useful if you are making a pre-compiled binary distribution. You may get some warnings from the linker about potential problems and limitations when linking some libraries, or compilation may fail entirely if the static libraries are unavailable. </p>
<dt><code>-profile</code></p>
<dd> Turns on profiling in the output code. The program will then generate a gmon.out file when run, which can then be analysed with a program such as <code><a href="/docs/linux/man/1-gprof/">gprof</a>(1). This option also enables -static</code>, and to get a useful call graph report from gprof, your libgc library must have been compiled with profiling enabled. </p>
<dt><code>-T</code></p>
<dd> Turns on Taint mode. In this mode, all Strings received from external sources are considered &quot;tainted&quot; and cannot be used until processed by a de-tainting function. This is most useful in CGI applications for forcing data validation. </p>
<dt><code>-seedkey </code><i>STRING</i></p>
<dd> Use a string to seed the random number generator which makes a secret key. Useful for testing web apps. </p>
</dl>
<h2>DEBUGGING OPTIONS</h2>
<p> These options generate debugging information. </p>
<dl>
<dt><code>-dumptac</code></p>
<dd> Dump bytecode </p>
<dt><code>-dumpraw</code></p>
<dd> Dump the raw parse tree. </p>
<dt><code>-dumptree</code></p>
<dd> Dump the type checked parse tree. </p>
<dt><code>-dumpsimpl</code></p>
<dd> Dump the simplified, desugared and optimised code in a human readable (almost) form. </p>
<dt><code>-dumpeqns</code></p>
<dd> Dump the type equations used in type inference </p>
<dt><code>-dumpcg</code></p>
<dd> Dump the function call graph </p>
<dt><code>-dumpdeps</code></p>
<dd> Dump the module dependency graph </p>
<dt><code>-keepc</code></p>
<dd> Keep the generated C code </p>
<dt><code>-showgcc</code></p>
<dd> Print the command sent to gcc </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>KAYA_LIBRARY_PATH</code></p>
<dd> A list of extra paths to search for kaya libraries. Paths are separated by &#8216;:&#8217; on Posix systems, and &#8216;;&#8217; on Windows. </p>
</dl>
<h2>DOCUMENTATION</h2>
<p> Library documentation for Kaya can be found at &lt;<a rel="nofollow" href="http://kayalang.org/library">http://kayalang.org/library</a>&gt; or in the manual section <code>3kaya</code> </p>
<h2>OBTAINING</h2>
<p> The latest release of Kaya can be obtained from &lt;<a rel="nofollow" href="http://kayalang.org/download">http://kayalang.org/download</a>&gt;. You can receive announcements of new versions of Kaya by subscribing to the kaya-announce mailing list &lt;<a href="http://lists.kayalang.org/lists/listinfo/kaya-announce">http://lists.kayalang.org/lists/listinfo/kaya-announce</a>&gt; </p>
<p> Development versions can be obtained using <code><a href="/docs/linux/man/1-darcs/">darcs</a>(1)</code> from &lt;<a rel="nofollow" href="http://kayalang.org/darcs/">http://kayalang.org/darcs/</a>&gt; </p>
<h2>BUGS</h2>
<p> Please report bugs found to &lt;kaya [at] kayalang.org&gt; </p>
<h2>LICENSE</h2>
<p> <code>kayac</code> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License (version 2 or any later version) as published by the Free Software Foundation. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-darcs/">darcs</a>(1)</code> <code><a href="/docs/linux/man/1-gcc/">gcc</a>(1)</code> <code><a href="/docs/linux/man/1-gprof/">gprof</a>(1)</code> <code><a href="/docs/linux/man/1-rekey/">rekey</a>(1)</code> <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> </p>
<h2>Index</h2>
