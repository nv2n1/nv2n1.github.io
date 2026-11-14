---
title: "sbcl(1)"
name: "sbcl"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sbcl/"
description: "SBCL — Steel Bank Common Lisp"
---

<h2 class="name">NAME</h2>
<p> SBCL &#8212; Steel Bank Common Lisp</p>
<h2>DESCRIPTION</h2>
<p> SBCL is an implementation of ANSI Common Lisp, featuring a high-performance native compiler, native threads on several platforms, a socket interface, a source-level debugger, a statistical profiler, and much more. </p>
<p> It is free software, mostly in the public domain, but with some subsystems under BSD-style licenses which allow modification and reuse as long as credit is given. It is provided &quot;as is&quot;, with no warranty of any kind. </p>
<p> For more information about license issues, see the COPYING file in the distribution. For more information about history, see the CREDITS file in the distribution. </p>
<h2>RUNNING SBCL</h2>
<p> To run SBCL, type &quot;sbcl&quot;. After startup messages a prompt (&quot;*&quot;) appears. Enter a Lisp expression, and SBCL will read and execute it, print any values returned, give you another prompt, and wait for your next input. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>$&nbsp;<wbr>sbcl<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230;[startup messages elided]&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>(+&nbsp;<wbr>1 2 3) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>6<br />
&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>(exit) </p>
<p> Most people like to run SBCL as a subprocess under Emacs. The Emacs &quot;Slime&quot; mode provides many convenient features, like command line editing, tab completion, and various kinds of coupling between Common Lisp source files and the interactive SBCL subprocess. </p>
<p> For information on creating &quot;standalone executables&quot; using SBCL, see SB-EXT:SAVE-LISP-AND-DIE in the User Manual. </p>
<h2>COMMAND LINE SYNTAX</h2>
<p> For ordinary interactive use, no command line arguments should be necessary. </p>
<p> In order to understand the SBCL command line syntax, it is helpful to understand that the system is composed of two parts: a runtime environment, and the Common Lisp system it supports. Some command line arguments are processed during the initialization of the runtime, and some during the initialization of the Lisp system &#8212; any remaining command line arguments are passed on to user code. </p>
<p> The overall command line syntax is:</p>
<dl>
<dt>
<dd> <code>sbcl [runtime options] &#8211;end-runtime-options [toplevel options] &#8211;end-toplevel-options [user options]</code></dl>
<p> Both &#8211;end-runtime-options and &#8211;end-toplevel-options are optional, and may be omitted. They are intended for use in situations where any command line options are under user control (<i>e.g.</i> in batch files): by using them you can prevent options intended for your program being accidentally processed by SBCL. </p>
<p> Supported runtime options are</p>
<dl>
<dt><code>&#8211;core &lt;corefilename&gt;</code></p>
<dd> Use the specified Lisp core file instead of the default. (See the FILES section for the standard core, or the system documentation for SB-EXT:SAVE-LISP-AND-DIE for information about how to create a custom core.) Note that if the Lisp core file is a user-created core file, it may run a nonstandard toplevel which does not recognize the standard toplevel options.</p>
<dt><code>&#8211;dynamic-space-size &lt;megabytes&gt;</code></p>
<dd> Size of the dynamic space reserved on startup in megabytes. Default value is platform dependent.</p>
<dt><code>&#8211;control-stack-size &lt;megabytes&gt;</code></p>
<dd> Size of control stack reserved for each thread in megabytes. Default value is 2.</p>
<dt><code>&#8211;noinform</code></p>
<dd> Suppress the printing of any banner or other informational message at startup. (This makes it easier to write Lisp programs which work cleanly in Unix pipelines. See also the &quot;&#8211;noprint&quot; and &quot;&#8211;disable-debugger&quot; options.)</p>
<dt><code>&#8211;disable-ldb</code></p>
<dd> Disable the low-level debugger. Only effective if SBCL is compiled with LDB.</p>
<dt><code>&#8211;lose-on-corruption</code></p>
<dd> There are some dangerous low level errors (for instance, control stack exhausted, memory fault) that (or whose handlers) can corrupt the image. By default SBCL prints a warning, then tries to continue and handle the error in Lisp, but this will not always work and SBCL may malfunction or even hang. With this option, upon encountering such an error SBCL will invoke ldb (if present and enabled) or else exit.</p>
<dt><code>&#8211;script &lt;filename&gt;</code></p>
<dd> As a runtime option equivalent to &#8211;noinform &#8211;disable-ldb &#8211;lose-on-corruption &#8211;end-runtime-options &#8211;script &lt;filename&gt;. See the description of &#8211;script as a toplevel option below.</p>
<dt><code>&#8211;merge-core-pages</code></p>
<dd> When platform support is present, provide hints to the operating system that identical pages may be shared between processes until they are written to. This can be useful to reduce the memory usage on systems with multiple SBCL processes started from similar but differently-named core files, or from compressed cores. Without platform support, do nothing.</p>
<dt><code>&#8211;no-merge-core-pages</code></p>
<dd> Ensures that no sharing hint is provided to the operating system.</p>
<dt><code>&#8211;default-merge-core-pages</code></p>
<dd> Reverts the sharing hint policy to the default: only compressed cores trigger hinting. Uncompressed cores are mapped directly from the core file, which is usually enough to ensure sharing.</p>
<dt><code>&#8211;help</code></p>
<dd> Print some basic information about SBCL, then exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print SBCL&#8217;s version information, then exit.</dl>
<p> In the future, runtime options may be added to control behavior such as lazy allocation of memory. </p>
<p> Runtime options, including any &#8211;end-runtime-options option, are stripped out of the command line before the Lisp toplevel logic gets a chance to see it. </p>
<p> The toplevel options supported by the standard SBCL core are</p>
<dl>
<dt><code>&#8211;sysinit &lt;filename&gt;</code></p>
<dd> Load filename instead of the default system-wide initialization file. (See the FILES section.)</p>
<dt><code>&#8211;no-sysinit</code></p>
<dd> Do not load a system-wide initialization file. If this option is given, the &#8211;sysinit option is ignored.</p>
<dt><code>&#8211;userinit &lt;filename&gt;</code></p>
<dd> Load filename instead of the default user initialization file. (See the FILES section.)</p>
<dt><code>&#8211;no-userinit</code></p>
<dd> Do not load a user initialization file. If this option is given, the &#8211;userinit option is ignored.</p>
<dt><code>&#8211;eval &lt;command&gt;</code></p>
<dd> After executing any initialization file, but before starting the read-eval-print loop on standard input, read and evaluate the command given. More than one &#8211;eval option can be used, and all will be read and executed, in the order they appear on the command line.</p>
<dt><code>&#8211;load &lt;filename&gt;</code></p>
<dd> This is equivalent to &#8211;eval &#8216;(load &quot;&lt;filename&gt;&quot;)&#8217;. The special syntax is intended to reduce quoting headaches when invoking SBCL from shell scripts.</p>
<dt><code>&#8211;noprint</code></p>
<dd> When ordinarily the toplevel &quot;read-eval-print loop&quot; would be executed, execute a &quot;read-eval loop&quot; instead, <i>i.e.</i> don&#8217;t print a prompt and don&#8217;t echo results. Combined with the &#8211;noinform runtime option, this makes it easier to write Lisp &quot;scripts&quot; which work cleanly in Unix pipelines.</p>
<dt><code>&#8211;disable-debugger</code></p>
<dd> By default when SBCL encounters an error, it enters the builtin debugger, allowing interactive diagnosis and possible intercession. This option disables the debugger, causing errors to print a backtrace and exit with status 1 instead &#8212; which is a mode of operation better suited for batch processing. See the User Manual on SB-EXT:DISABLE-DEBUGGER for details.</p>
<dt><code>&#8211;quit</code></p>
<dd> At the end of toplevel option processing, exit SBCL with a successful code of zero. Note that the effect of this option is delayed until after toplevel options following this one.</p>
<dt><code>&#8211;non-interactive</code></p>
<dd> This option disables the read-eval-print loop for both exceptional and non-exceptional reasons. It is short for &#8211;disable-debugger and &#8211;quit in combination and is useful for batch uses where the special option processing implied by &#8211;script is not desired.</p>
<dt><code>&#8211;script &lt;filename&gt;</code></p>
<dd> Implies &#8211;no-sysinit &#8211;no-userinit &#8211;disable-debugger &#8211;end-toplevel-options. </p>
<p> Causes the system to load the specified file and exit immediately afterwards, instead of entering the read-eval-print loop. If the file begins with a shebang line, it is ignored.</dl>
<p> Regardless of the order in which toplevel options appear on the command line, the order of actions is: </p>
<dl>
<dt>step].</p>
<dd> Debugger is disabled, if requested.</p>
<dt>step].</p>
<dd> Any system initialization file is loaded, unless prohibited.</p>
<dt>step].</p>
<dd> Any user initialization file is loaded, unless prohibited.</p>
<dt>step].</p>
<dd> &#8211;eval and &#8211;load options are processed in the order given.</dl>
<p> Finally, either the read-eval-print loop is entered or the file specified with &#8211;script option is loaded. </p>
<p> When running in the read-eval-print loop the system exits on end of file. Similarly, the system exits immediately after processing the file specified with &#8211;script. </p>
<p> Note that when running SBCL with the &#8211;core option, using a core file created by a user call to the SB-EXT:SAVE-LISP-AND-DIE, the toplevel options may be under the control of user code passed as arguments to SB-EXT:SAVE-LISP-AND-DIE. For this purpose, the &#8211;end-toplevel-options option itself can be considered a toplevel option, <i>i.e.</i> the user core, at its option, may not support it. </p>
<p> In the standard SBCL startup sequence (<i>i.e.</i> with no user core involved) toplevel options and any &#8211;end-toplevel-options option are stripped out of the command line argument list before user code gets a chance to see it. </p>
<h2>OVERVIEW</h2>
<p> SBCL is derived from the CMU CL. (The name is intended to acknowledge the connection: steel and banking are the industries where Carnegie and Mellon made the big bucks.) </p>
<p> SBCL compiles by default: even functions entered in the read-eval-print loop are compiled to native code, unless the evaluator has been explicitly turned on. (Even today, some 40 years after the MacLisp compiler, people will tell you that Lisp is an interpreted language. Ignore them.) </p>
<p> SBCL aims for but has not completely achieved compliance with the ANSI standard for Common Lisp. More information about this is available in the BUGS section below. </p>
<p> SBCL also includes various non-ANSI extensions, described more fully in the User Manual. Some of these are in the base system and others are &quot;contrib&quot; modules loaded on request using REQUIRE. For example, to load the SB-BSD-SOCKETS module that provides TCP/IP connectivity,<br />
*&nbsp;<wbr>(require&nbsp;<wbr>&#8216;asdf)<br />
*&nbsp;<wbr>(require&nbsp;<wbr>&#8216;sb-bsd-sockets) </p>
<p> For more information, see the User Manual. </p>
<h2>THE COMPILER</h2>
<p> SBCL inherits from CMU CL the &quot;Python&quot; native code compiler. (Though we often avoid that name in order to avoid confusion with the scripting language also called Python.) This compiler is very clever about understanding the type system of Common Lisp and using it to optimize code, and about producing notes to let the user know when the compiler doesn&#8217;t have enough type information to produce efficient code. It also tries (almost always successfully) to follow the unusual but very useful principle that &quot;declarations are assertions&quot;, <i>i.e.</i> type declarations should be checked at runtime unless the user explicitly tells the system that speed is more important than safety. </p>
<p> The compiled code uses garbage collection to automatically manage memory. The garbage collector implementation varies considerably from CPU to CPU. In particular, on some CPUs the GC is nearly exact, while on others it&#8217;s more conservative, and on some CPUs the GC is generational, while on others simpler stop and copy strategies are used. </p>
<p> For more information about the compiler, see the user manual. </p>
<h2>SYSTEM REQUIREMENTS</h2>
<p> SBCL currently runs on X86 (Linux, FreeBSD, OpenBSD, and NetBSD), X86-64 (Linux), Alpha (Linux, Tru64), PPC (Linux, Darwin/MacOS X), SPARC (Linux and Solaris 2.x), and MIPS (Linux). For information on other ongoing and possible ports, see the sbcl-devel mailing list, and/or the web site. </p>
<p> SBCL requires on the order of 16Mb RAM to run on X86 systems, though all but the smallest programs would be happier with 32Mb or more. </p>
<h2>KNOWN BUGS</h2>
<p> This section attempts to list the most serious and long-standing bugs. For more detailed and current information on bugs, see the BUGS file in the distribution. </p>
<p> It is possible to get in deep trouble by exhausting heap memory. The SBCL system overcommits memory at startup, so, on typical Unix-alikes like Linux and FreeBSD, this means that if the SBCL system turns out to use more virtual memory than the system has available for it, other processes tend to be killed randomly (!). </p>
<p> The compiler&#8217;s handling of function return values unnecessarily violates the &quot;declarations are assertions&quot; principle that it otherwise adheres to. Using PROCLAIM or DECLAIM to specify the return type of a function causes the compiler to believe you without checking. Thus compiling a file containing<br />
&nbsp;<wbr>&nbsp;<wbr>(DECLAIM&nbsp;<wbr>(FTYPE&nbsp;<wbr>(FUNCTION&nbsp;<wbr>(T)&nbsp;<wbr>NULL)&nbsp;<wbr>SOMETIMES))<br />
&nbsp;<wbr>&nbsp;<wbr>(DEFUN SOMETIMES&nbsp;<wbr>(X)&nbsp;<wbr>(ODDP X))<br />
&nbsp;<wbr>&nbsp;<wbr>(DEFUN FOO&nbsp;<wbr>(X)&nbsp;<wbr>(IF&nbsp;<wbr>(SOMETIMES X)&nbsp;<wbr>&#8216;THIS-TIME&nbsp;<wbr>&#8216;NOT-THIS-TIME))<br />
 then running (FOO 1) gives NOT-THIS-TIME, because the compiler relied on the truth of the DECLAIM without checking it. </p>
<p> Some things are implemented very inefficiently.</p>
<dl>
<dt>&#8212;</p>
<dd> Multidimensional arrays are inefficient, especially multidimensional arrays of floating point numbers.</p>
<dt>&#8212;</p>
<dd> SBCL, like most (maybe all?) implementations of Common Lisp on stock hardware, has trouble passing floating point numbers around efficiently, because a floating point number, plus a few extra bits to identify its type, is larger than a machine word. (Thus, they get &quot;boxed&quot; in heap-allocated storage, causing GC overhead.) Within a single compilation unit, or when doing built-in operations like SQRT and AREF, or some special operations like structure slot accesses, this is avoidable: see the user manual for some efficiency hints. But for general function calls across the boundaries of compilation units, passing the result of a floating point calculation as a function argument (or returning a floating point result as a function value) is a fundamentally slow operation.</dl>
<h2>REPORTING BUGS</h2>
<p> To report a bug, please send mail to the mailing lists sbcl-help or sbcl-devel. You can find the complete mailing list addresses on the web pages at &lt;<a rel="nofollow" href="http://sbcl.sourceforge.net/">http://sbcl.sourceforge.net/</a>&gt;; note that as a spam reduction measure you must subscribe to the lists before you can post. (You may also find fancy SourceForge bug-tracking machinery there, but don&#8217;t be fooled. As of 2002-07-25 anyway, we don&#8217;t actively monitor that machinery, and it exists only because we haven&#8217;t been able to figure out how to turn it off.) </p>
<p> As with any software bug report, it&#8217;s most helpful if you can provide enough information to reproduce the symptoms reliably, and if you say clearly what the symptoms are. For example, &quot;There seems to be something wrong with TAN of very small negative arguments. When I execute (TAN LEAST-NEGATIVE-SINGLE-FLOAT) interactively on sbcl-1.2.3 on my Linux 4.5 X86 box, I get an UNBOUND-VARIABLE error.&quot; </p>
<h2>DIFFERENCES FROM CMU CL</h2>
<p> SBCL can be built from scratch using a plain vanilla ANSI Common Lisp system and a C compiler, and all of its properties are specified by the version of the source code that it was created from. This clean bootstrappability was the immediate motivation for forking off of the CMU CL development tree. A variety of implementation differences are motivated by this design goal. </p>
<p> Maintenance work in SBCL since the fork has diverged somewhat from the maintenance work in CMU CL. Many but not all bug fixes and improvements have been shared between the two projects, and sometimes the two projects disagree about what would be an improvement. </p>
<p> Most extensions supported by CMU CL have been unbundled from SBCL, including Motif support, the Hemlock editor, search paths, the WIRE protocol, various user-level macros and functions (<i>e.g.</i> LETF, ITERATE, MEMQ, REQUIRED-ARGUMENT), and many others. </p>
<p> (Why doesn&#8217;t SBCL support more extensions natively? Why drop all those nice extensions from CMU CL when the code already exists? This is a frequently asked question on the mailing list. There are two principal reasons. First, it&#8217;s a design philosophy issue: arguably SBCL has done its job by supplying a stable FFI, and the right design decision is to move functionality derived from that, like socket support, into separate libraries. Some of these are distributed with SBCL as &quot;contrib&quot; modules, others are distributed as separate software packages by separate maintainers. Second, it&#8217;s a practical decision &#8211; focusing on a smaller number of things will, we hope, let us do a better job on them.) </p>
<h2>SUPPORT</h2>
<p> Various information about SBCL is available at &lt;<a rel="nofollow" href="http://www.sbcl.org/">http://www.sbcl.org/</a>&gt;. The mailing lists there are the recommended place to look for support. </p>
<h2>AUTHORS</h2>
<p> Dozens of people have made substantial contributions to SBCL and its subsystems, and to the CMU CL system on which it was based, over the years. See the CREDITS file in the distribution for more information. </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SBCL_HOME</code></p>
<dd> This variable controls where files like &quot;sbclrc&quot;, &quot;sbcl.core&quot;, and the add-on &quot;contrib&quot; systems are searched for. If it is not set, then sbcl sets it from a compile-time default location which is usually <code>/usr/local/lib/sbcl/</code> but may have been changed <i>e.g.</i> by a third-party packager. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>sbcl</i></p>
<dd> executable program containing some low-level runtime support and a loader, used to read sbcl.core</p>
<dt><i>sbcl.core</i></p>
<dd> dumped memory image containing most of SBCL, to be loaded by the `sbcl&#8217; executable. Looked for in <code>$SBCL_HOME</code>, unless overridden by the &#8211;core option.</p>
<dt><i>sbclrc</i></p>
<dd> optional system-wide startup script, looked for in <code>$SBCL_HOME</code> then <code>/etc</code>, unless overridden by the &#8211;sysinit command line option.</p>
<dt><i>.sbclrc</i></p>
<dd> optional per-user customizable startup script (in user&#8217;s home directory, or as specified by &#8211;userinit) </p>
</dl>
<h2>SEE ALSO</h2>
<p> Full SBCL documentation is maintained as a Texinfo manual. If is has been installed, the command</p>
<dl>
<dt>
<dd> <code>info sbcl</code></dl>
<p> should give you access to the complete manual. Depending on your installation it may also be available in HTML and PDF formats in <i>e.g.</i></p>
<dl>
<dt>
<dd> <code>/usr/local/share/doc/sbcl/</code></dl>
<p> See the SBCL homepage</p>
<dl>
<dt>
<dd> &lt;<a rel="nofollow" href="http://www.sbcl.org/">http://www.sbcl.org/</a>&gt;</dl>
<p> for more information, including directions on how to subscribe to the sbcl-devel and sbcl-help mailing-lists. </p>
<h2>Index</h2>
