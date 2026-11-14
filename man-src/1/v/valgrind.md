---
title: "valgrind(1)"
name: "valgrind"
section: "1"
letter: "v"
url: "/docs/linux/man/1-valgrind/"
description: "valgrind – a suite of tools for debugging and profiling programs"
---

<h2 class="name">NAME</h2>
<p> valgrind &#8211; a suite of tools for debugging and profiling programs </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>valgrind</code> [<i>valgrind-options</i>] [<code>your-program</code>] [<i>your-program-options</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Valgrind</code></p>
<dd>is a flexible program for debugging and profiling Linux executables. It consists of a core, which provides a synthetic CPU in software, and a series of debugging and profiling tools. The architecture is modular, so that new tools can be created easily and without disturbing the existing structure. </p>
<p> Some of the options described below work with all Valgrind tools, and some only work with a few or one. The section MEMCHECK OPTIONS and those below it describe tool-specific options. </p>
<p> This manual page covers only basic usage and options. For more comprehensive information, please see the HTML documentation on your system: $INSTALL/share/doc/valgrind/html/index.html, or online: <a rel="nofollow" href="http://www.valgrind.org/docs/manual/index.html.">http://www.valgrind.org/docs/manual/index.html.</a></p>
<h2>TOOL SELECTION OPTIONS</h2>
<p> The single most important option. </p>
<p> <code>&#8211;tool=&lt;toolname&gt; [default: memcheck] </code></p>
<dl>
<dt>
<dd> Run the Valgrind tool called <i>toolname</i>, e.g. memcheck, cachegrind, callgrind, helgrind, drd, massif, dhat, lackey, none, exp-sgcheck, exp-bbv, etc.</dl>
<h2>BASIC OPTIONS</h2>
<p> These options work with all tools. </p>
<p> <code>-h &#8211;help</code></p>
<dl>
<dt>
<dd> Show help for all options, both for the core and for the selected tool. If the option is repeated it is equivalent to giving <code>&#8211;help-debug</code>.</dl>
<p> <code>&#8211;help-debug</code></p>
<dl>
<dt>
<dd> Same as <code>&#8211;help</code>, but also lists debugging options which usually are only of use to Valgrind&#8217;s developers.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show the version number of the Valgrind core. Tools can have their own version numbers. There is a scheme in place to ensure that tools only execute when the core version is one they are known to work with. This was done to minimise the chances of strange problems arising from tool-vs-core version incompatibilities.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Run silently, and only print error messages. Useful if you are running regression tests or have some other automated test machinery.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Be more verbose. Gives extra information on various aspects of your program, such as: the shared objects loaded, the suppressions used, the progress of the instrumentation and execution engines, and warnings about unusual behaviour. Repeating the option increases the verbosity level.</dl>
<p> <code>&#8211;trace-children=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, Valgrind will trace into sub-processes initiated via the <i>exec</i> system call. This is necessary for multi-process programs. </p>
<p> Note that Valgrind does trace into the child of a <i>fork</i> (it would be difficult not to, since <i>fork</i> makes an identical copy of a process), so this option is arguably badly named. However, most children of <i>fork</i> calls immediately call <i>exec</i> anyway.</dl>
<p> <code>&#8211;trace-children-skip=patt1,patt2,&#8230; </code></p>
<dl>
<dt>
<dd> This option only has an effect when <code>&#8211;trace-children=yes</code> is specified. It allows for some children to be skipped. The option takes a comma separated list of patterns for the names of child executables that Valgrind should not trace into. Patterns may include the metacharacters ? and *, which have the usual meaning. </p>
<p> This can be useful for pruning uninteresting branches from a tree of processes being run on Valgrind. But you should be careful when using it. When Valgrind skips tracing into an executable, it doesn&#8217;t just skip tracing that executable, it also skips tracing any of that executable&#8217;s child processes. In other words, the flag doesn&#8217;t merely cause tracing to stop at the specified executables &#8212; it skips tracing of entire process subtrees rooted at any of the specified executables.</dl>
<p> <code>&#8211;trace-children-skip-by-arg=patt1,patt2,&#8230; </code></p>
<dl>
<dt>
<dd> This is the same as <code>&#8211;trace-children-skip</code>, with one difference: the decision as to whether to trace into a child process is made by examining the arguments to the child process, rather than the name of its executable.</dl>
<p> <code>&#8211;child-silent-after-fork=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, Valgrind will not show any debugging or logging output for the child process resulting from a <i>fork</i> call. This can make the output less confusing (although more misleading) when dealing with processes that create children. It is particularly useful in conjunction with <i>&#8211;trace-children=</i>. Use of this option is also strongly recommended if you are requesting XML output (<i>&#8211;xml=yes</i>), since otherwise the XML from child and parent may become mixed up, which usually makes it useless.</dl>
<p> <code>&#8211;vgdb=&lt;no|yes|full&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> Valgrind will provide &quot;gdbserver&quot; functionality when <code>&#8211;vgdb=yes</code> or <code>&#8211;vgdb=full</code> is specified. This allows an external GNU GDB debugger to control and debug your program when it runs on Valgrind. <code>&#8211;vgdb=full</code> incurs significant performance overheads, but provides more precise breakpoints and watchpoints. See Debugging your program using Valgrind&#8217;s gdbserver and GDB for a detailed description. </p>
<p> If the embedded gdbserver is enabled but no gdb is currently being used, the vgdb command line utility can send &quot;monitor commands&quot; to Valgrind from a shell. The Valgrind core provides a set of Valgrind monitor commands. A tool can optionally provide tool specific monitor commands, which are documented in the tool specific chapter.</dl>
<p> <code>&#8211;vgdb-error=&lt;number&gt; [default: 999999999] </code></p>
<dl>
<dt>
<dd> Use this option when the Valgrind gdbserver is enabled with <code>&#8211;vgdb=yes</code> or <code>&#8211;vgdb=full</code>. Tools that report errors will wait for &quot;number&quot; errors to be reported before freezing the program and waiting for you to connect with GDB. It follows that a value of zero will cause the gdbserver to be started before your program is executed. This is typically used to insert GDB breakpoints before execution, and also works with tools that do not report errors, such as Massif.</dl>
<p> <code>&#8211;vgdb-stop-at=&lt;set&gt; [default: none] </code></p>
<dl>
<dt>
<dd> Use this option when the Valgrind gdbserver is enabled with <code>&#8211;vgdb=yes</code> or <code>&#8211;vgdb=full</code>. The Valgrind gdbserver will be invoked for each error after <code>&#8211;vgdb-error</code> have been reported. You can additionally ask the Valgrind gdbserver to be invoked for other events, specified in one of the following ways: </p>
<dl>
<dt>
<dd> &bull; a comma separated list of one or more of <code>startup exit valgrindabexit</code>. </p>
<p> The values <code>startup</code> <code>exit</code> <code>valgrindabexit</code> respectively indicate to invoke gdbserver before your program is executed, after the last instruction of your program, on Valgrind abnormal exit (e.g. internal error, out of memory, &#8230;). </p>
<p> Note: <code>startup</code> and <code>&#8211;vgdb-error=0</code> will both cause Valgrind gdbserver to be invoked before your program is executed. The <code>&#8211;vgdb-error=0</code> will in addition cause your program to stop on all subsequent errors.</dl>
<dl>
<dt>
<dd> &bull; <code>all</code> to specify the complete set. It is equivalent to <code>&#8211;vgdb-stop-at=startup,exit,valgrindabexit</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>none</code> for the empty set.</dl>
</dl>
<p> <code>&#8211;track-fds=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, Valgrind will print out a list of open file descriptors on exit or on request, via the gdbserver monitor command <i>v.info open_fds</i>. Along with each file descriptor is printed a stack backtrace of where the file was opened and any details relating to the file descriptor such as the file name or socket details.</dl>
<p> <code>&#8211;time-stamp=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, each message is preceded with an indication of the elapsed wallclock time since startup, expressed as days, hours, minutes, seconds and milliseconds.</dl>
<p> <code>&#8211;log-fd=&lt;number&gt; [default: 2, stderr] </code></p>
<dl>
<dt>
<dd> Specifies that Valgrind should send all of its messages to the specified file descriptor. The default, 2, is the standard error channel (stderr). Note that this may interfere with the client&#8217;s own use of stderr, as Valgrind&#8217;s output will be interleaved with any output that the client sends to stderr.</dl>
<p> <code>&#8211;log-file=&lt;filename&gt; </code></p>
<dl>
<dt>
<dd> Specifies that Valgrind should send all of its messages to the specified file. If the file name is empty, it causes an abort. There are three special format specifiers that can be used in the file name. </p>
<p> <code>%p</code> is replaced with the current process ID. This is very useful for program that invoke multiple processes. WARNING: If you use <code>&#8211;trace-children=yes</code> and your program invokes multiple processes OR your program forks without calling exec afterwards, and you don&#8217;t use this specifier (or the <code>%q</code> specifier below), the Valgrind output from all those processes will go into one file, possibly jumbled up, and possibly incomplete. Note: If the program forks and calls exec afterwards, Valgrind output of the child from the period between fork and exec will be lost. Fortunately this gap is really tiny for most programs; and modern programs use posix_spawn anyway. </p>
<p> <code>%n</code> is replaced with a file sequence number unique for this process. This is useful for processes that produces several files from the same filename template. </p>
<p> <code>%q{FOO}</code> is replaced with the contents of the environment variable <i>FOO</i>. If the <code>{FOO}</code> part is malformed, it causes an abort. This specifier is rarely needed, but very useful in certain circumstances (eg. when running MPI programs). The idea is that you specify a variable which will be set differently for each process in the job, for example BPROC_RANK or whatever is applicable in your MPI setup. If the named environment variable is not set, it causes an abort. Note that in some shells, the <code>{</code> and <code>}</code> characters may need to be escaped with a backslash. </p>
<p> <code>%%</code> is replaced with <code>%</code>. </p>
<p> If an <code>%</code> is followed by any other character, it causes an abort. </p>
<p> If the file name specifies a relative file name, it is put in the program&#8217;s initial working directory: this is the current directory when the program started its execution after the fork or after the exec. If it specifies an absolute file name (ie. starts with &#8216;/&#8217;) then it is put there.</dl>
<p> <code>&#8211;log-socket=&lt;ip-address:port-number&gt; </code></p>
<dl>
<dt>
<dd> Specifies that Valgrind should send all of its messages to the specified port at the specified IP address. The port may be omitted, in which case port 1500 is used. If a connection cannot be made to the specified socket, Valgrind falls back to writing output to the standard error (stderr). This option is intended to be used in conjunction with the valgrind-listener program. For further details, see the commentary in the manual.</dl>
<h2>ERROR-RELATED OPTIONS</h2>
<p> These options are used by all tools that can report errors, e.g. Memcheck, but not Cachegrind. </p>
<p> <code>&#8211;xml=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, the important parts of the output (e.g. tool error messages) will be in XML format rather than plain text. Furthermore, the XML output will be sent to a different output channel than the plain text output. Therefore, you also must use one of <code>&#8211;xml-fd</code>, <code>&#8211;xml-file</code> or <code>&#8211;xml-socket</code> to specify where the XML is to be sent. </p>
<p> Less important messages will still be printed in plain text, but because the XML output and plain text output are sent to different output channels (the destination of the plain text output is still controlled by <code>&#8211;log-fd</code>, <code>&#8211;log-file</code> and <code>&#8211;log-socket</code>) this should not cause problems. </p>
<p> This option is aimed at making life easier for tools that consume Valgrind&#8217;s output as input, such as GUI front ends. Currently this option works with Memcheck, Helgrind, DRD and SGcheck. The output format is specified in the file docs/internals/xml-output-protocol4.txt in the source tree for Valgrind 3.5.0 or later. </p>
<p> The recommended options for a GUI to pass, when requesting XML output, are: <code>&#8211;xml=yes</code> to enable XML output, <code>&#8211;xml-file</code> to send the XML output to a (presumably GUI-selected) file, <code>&#8211;log-file</code> to send the plain text output to a second GUI-selected file, <code>&#8211;child-silent-after-fork=yes</code>, and <code>-q</code> to restrict the plain text output to critical error messages created by Valgrind itself. For example, failure to read a specified suppressions file counts as a critical error message. In this way, for a successful run the text output file will be empty. But if it isn&#8217;t empty, then it will contain important information which the GUI user should be made aware of.</dl>
<p> <code>&#8211;xml-fd=&lt;number&gt; [default: -1, disabled] </code></p>
<dl>
<dt>
<dd> Specifies that Valgrind should send its XML output to the specified file descriptor. It must be used in conjunction with <code>&#8211;xml=yes</code>.</dl>
<p> <code>&#8211;xml-file=&lt;filename&gt; </code></p>
<dl>
<dt>
<dd> Specifies that Valgrind should send its XML output to the specified file. It must be used in conjunction with <code>&#8211;xml=yes</code>. Any <code>%p</code> or <code>%q</code> sequences appearing in the filename are expanded in exactly the same way as they are for <code>&#8211;log-file</code>. See the description of &#8211;log-file for details.</dl>
<p> <code>&#8211;xml-socket=&lt;ip-address:port-number&gt; </code></p>
<dl>
<dt>
<dd> Specifies that Valgrind should send its XML output the specified port at the specified IP address. It must be used in conjunction with <code>&#8211;xml=yes</code>. The form of the argument is the same as that used by <code>&#8211;log-socket</code>. See the description of <code>&#8211;log-socket</code> for further details.</dl>
<p> <code>&#8211;xml-user-comment=&lt;string&gt; </code></p>
<dl>
<dt>
<dd> Embeds an extra user comment string at the start of the XML output. Only works when <code>&#8211;xml=yes</code> is specified; ignored otherwise.</dl>
<p> <code>&#8211;demangle=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> Enable/disable automatic demangling (decoding) of C++ names. Enabled by default. When enabled, Valgrind will attempt to translate encoded C++ names back to something approaching the original. The demangler handles symbols mangled by g++ versions 2.X, 3.X and 4.X. </p>
<p> An important fact about demangling is that function names mentioned in suppressions files should be in their mangled form. Valgrind does not demangle function names when searching for applicable suppressions, because to do otherwise would make suppression file contents dependent on the state of Valgrind&#8217;s demangling machinery, and also slow down suppression matching.</dl>
<p> <code>&#8211;num-callers=&lt;number&gt; [default: 12] </code></p>
<dl>
<dt>
<dd> Specifies the maximum number of entries shown in stack traces that identify program locations. Note that errors are commoned up using only the top four function locations (the place in the current function, and that of its three immediate callers). So this doesn&#8217;t affect the total number of errors reported. </p>
<p> The maximum value for this is 500. Note that higher settings will make Valgrind run a bit more slowly and take a bit more memory, but can be useful when working with programs with deeply-nested call chains.</dl>
<p> <code>&#8211;unw-stack-scan-thresh=&lt;number&gt; [default: 0] </code>, <code>&#8211;unw-stack-scan-frames=&lt;number&gt; [default: 5] </code></p>
<dl>
<dt>
<dd> Stack-scanning support is available only on ARM targets. </p>
<p> These flags enable and control stack unwinding by stack scanning. When the normal stack unwinding mechanisms &#8212; usage of Dwarf CFI records, and frame-pointer following &#8212; fail, stack scanning may be able to recover a stack trace. </p>
<p> Note that stack scanning is an imprecise, heuristic mechanism that may give very misleading results, or none at all. It should be used only in emergencies, when normal unwinding fails, and it is important to nevertheless have stack traces. </p>
<p> Stack scanning is a simple technique: the unwinder reads words from the stack, and tries to guess which of them might be return addresses, by checking to see if they point just after ARM or Thumb call instructions. If so, the word is added to the backtrace. </p>
<p> The main danger occurs when a function call returns, leaving its return address exposed, and a new function is called, but the new function does not overwrite the old address. The result of this is that the backtrace may contain entries for functions which have already returned, and so be very confusing. </p>
<p> A second limitation of this implementation is that it will scan only the page (4KB, normally) containing the starting stack pointer. If the stack frames are large, this may result in only a few (or not even any) being present in the trace. Also, if you are unlucky and have an initial stack pointer near the end of its containing page, the scan may miss all interesting frames. </p>
<p> By default stack scanning is disabled. The normal use case is to ask for it when a stack trace would otherwise be very short. So, to enable it, use &#8211;unw-stack-scan-thresh=number. This requests Valgrind to try using stack scanning to &quot;extend&quot; stack traces which contain fewer than number frames. </p>
<p> If stack scanning does take place, it will only generate at most the number of frames specified by &#8211;unw-stack-scan-frames. Typically, stack scanning generates so many garbage entries that this value is set to a low value (5) by default. In no case will a stack trace larger than the value specified by &#8211;num-callers be created.</dl>
<p> <code>&#8211;error-limit=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> When enabled, Valgrind stops reporting errors after 10,000,000 in total, or 1,000 different ones, have been seen. This is to stop the error tracking machinery from becoming a huge performance overhead in programs with many errors.</dl>
<p> <code>&#8211;error-exitcode=&lt;number&gt; [default: 0] </code></p>
<dl>
<dt>
<dd> Specifies an alternative exit code to return if Valgrind reported any errors in the run. When set to the default value (zero), the return value from Valgrind will always be the return value of the process being simulated. When set to a nonzero value, that value is returned instead, if Valgrind detects any errors. This is useful for using Valgrind as part of an automated test suite, since it makes it easy to detect test cases for which Valgrind has reported errors, just by inspecting return codes.</dl>
<p> <code>&#8211;exit-on-first-error=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> If this option is enabled, Valgrind exits on the first error. A nonzero exit value must be defined using &#8211;error-exitcode option. Useful if you are running regression tests or have some other automated test machinery.</dl>
<p> <code>&#8211;error-markers=&lt;begin&gt;,&lt;end&gt; [default: none]</code></p>
<dl>
<dt>
<dd> When errors are output as plain text (i.e. XML not used), <code>&#8211;error-markers</code> instructs to output a line containing the <code>begin</code> (<code>end</code>) string before (after) each error. </p>
<p> Such marker lines facilitate searching for errors and/or extracting errors in an output file that contain valgrind errors mixed with the program output. </p>
<p> Note that empty markers are accepted. So, only using a begin (or an end) marker is possible.</dl>
<p> <code>&#8211;show-error-list=no|yes [default: no]</code></p>
<dl>
<dt>
<dd> If this option is enabled, for tools that report errors, valgrind will show the list of detected errors and the list of used suppressions at exit. </p>
<p> Note that at verbosity 2 and above, valgrind automatically shows the list of detected errors and the list of used suppressions at exit, unless <code>&#8211;show-error-list=no</code> is selected.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Specifying <code>-s</code> is equivalent to <code>&#8211;show-error-list=yes</code>.</dl>
<p> <code>&#8211;sigill-diagnostics=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> Enable/disable printing of illegal instruction diagnostics. Enabled by default, but defaults to disabled when <code>&#8211;quiet</code> is given. The default can always be explicitly overridden by giving this option. </p>
<p> When enabled, a warning message will be printed, along with some diagnostics, whenever an instruction is encountered that Valgrind cannot decode or translate, before the program is given a SIGILL signal. Often an illegal instruction indicates a bug in the program or missing support for the particular instruction in Valgrind. But some programs do deliberately try to execute an instruction that might be missing and trap the SIGILL signal to detect processor features. Using this flag makes it possible to avoid the diagnostic output that you would otherwise get in such cases.</dl>
<p> <code>&#8211;keep-debuginfo=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, keep (&quot;archive&quot;) symbols and all other debuginfo for unloaded code. This allows saved stack traces to include file/line info for code that has been dlclose&#8217;d (or similar). Be careful with this, since it can lead to unbounded memory use for programs which repeatedly load and unload shared objects. </p>
<p> Some tools and some functionalities have only limited support for archived debug info. Memcheck fully supports it. Generally, tools that report errors can use archived debug info to show the error stack traces. The known limitations are: Helgrind&#8217;s past access stack trace of a race condition is does not use archived debug info. Massif (and more generally the xtree Massif output format) does not make use of archived debug info. Only Memcheck has been (somewhat) tested with <code>&#8211;keep-debuginfo=yes</code>, so other tools may have unknown limitations.</dl>
<p> <code>&#8211;show-below-main=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> By default, stack traces for errors do not show any functions that appear beneath <code>main</code> because most of the time it&#8217;s uninteresting C library stuff and/or gobbledygook. Alternatively, if <code>main</code> is not present in the stack trace, stack traces will not show any functions below <code>main</code>-like functions such as glibc&#8217;s <code>__libc_start_main</code>. Furthermore, if <code>main</code>-like functions are present in the trace, they are normalised as <code>(below main)</code>, in order to make the output more deterministic. </p>
<p> If this option is enabled, all stack trace entries will be shown and <code>main</code>-like functions will not be normalised.</dl>
<p> <code>&#8211;fullpath-after=&lt;string&gt; [default: don&#8217;t show source paths] </code></p>
<dl>
<dt>
<dd> By default Valgrind only shows the filenames in stack traces, but not full paths to source files. When using Valgrind in large projects where the sources reside in multiple different directories, this can be inconvenient. <code>&#8211;fullpath-after</code> provides a flexible solution to this problem. When this option is present, the path to each source file is shown, with the following all-important caveat: if <code>string</code> is found in the path, then the path up to and including <code>string</code> is omitted, else the path is shown unmodified. Note that <code>string</code> is not required to be a prefix of the path. </p>
<p> For example, consider a file named /home/janedoe/blah/src/foo/bar/xyzzy.c. Specifying <code>&#8211;fullpath-after=/home/janedoe/blah/src/</code> will cause Valgrind to show the name as foo/bar/xyzzy.c. </p>
<p> Because the string is not required to be a prefix, <code>&#8211;fullpath-after=src/</code> will produce the same output. This is useful when the path contains arbitrary machine-generated characters. For example, the path /my/build/dir/C32A1B47/blah/src/foo/xyzzy can be pruned to foo/xyzzy using <code>&#8211;fullpath-after=/blah/src/</code>. </p>
<p> If you simply want to see the full path, just specify an empty string: <code>&#8211;fullpath-after=</code>. This isn&#8217;t a special case, merely a logical consequence of the above rules. </p>
<p> Finally, you can use <code>&#8211;fullpath-after</code> multiple times. Any appearance of it causes Valgrind to switch to producing full paths and applying the above filtering rule. Each produced path is compared against all the <code>&#8211;fullpath-after</code>-specified strings, in the order specified. The first string to match causes the path to be truncated as described above. If none match, the full path is shown. This facilitates chopping off prefixes when the sources are drawn from a number of unrelated directories.</dl>
<p> <code>&#8211;extra-debuginfo-path=&lt;path&gt; [default: undefined and unused] </code></p>
<dl>
<dt>
<dd> By default Valgrind searches in several well-known paths for debug objects, such as /usr/lib/debug/. </p>
<p> However, there may be scenarios where you may wish to put debug objects at an arbitrary location, such as external storage when running Valgrind on a mobile device with limited local storage. Another example might be a situation where you do not have permission to install debug object packages on the system where you are running Valgrind. </p>
<p> In these scenarios, you may provide an absolute path as an extra, final place for Valgrind to search for debug objects by specifying <code>&#8211;extra-debuginfo-path=/path/to/debug/objects</code>. The given path will be prepended to the absolute path name of the searched-for object. For example, if Valgrind is looking for the debuginfo for /w/x/y/zz.so and <code>&#8211;extra-debuginfo-path=/a/b/c</code> is specified, it will look for a debug object at /a/b/c/w/x/y/zz.so. </p>
<p> This flag should only be specified once. If it is specified multiple times, only the last instance is honoured.</dl>
<p> <code>&#8211;debuginfo-server=ipaddr:port [default: undefined and unused]</code></p>
<dl>
<dt>
<dd> This is a new, experimental, feature introduced in version 3.9.0. </p>
<p> In some scenarios it may be convenient to read debuginfo from objects stored on a different machine. With this flag, Valgrind will query a debuginfo server running on ipaddr and listening on port port, if it cannot find the debuginfo object in the local filesystem. </p>
<p> The debuginfo server must accept TCP connections on port port. The debuginfo server is contained in the source file auxprogs/valgrind-di-server.c. It will only serve from the directory it is started in. port defaults to 1500 in both client and server if not specified. </p>
<p> If Valgrind looks for the debuginfo for /w/x/y/zz.so by using the debuginfo server, it will strip the pathname components and merely request zz.so on the server. That in turn will look only in its current working directory for a matching debuginfo object. </p>
<p> The debuginfo data is transmitted in small fragments (8 KB) as requested by Valgrind. Each block is compressed using LZO to reduce transmission time. The implementation has been tuned for best performance over a single-stage 802.11g (WiFi) network link. </p>
<p> Note that checks for matching primary vs debug objects, using GNU debuglink CRC scheme, are performed even when using the debuginfo server. To disable such checking, you need to also specify &#8211;allow-mismatched-debuginfo=yes. </p>
<p> By default the Valgrind build system will build valgrind-di-server for the target platform, which is almost certainly not what you want. So far we have been unable to find out how to get automake/autoconf to build it for the build platform. If you want to use it, you will have to recompile it by hand using the command shown at the top of auxprogs/valgrind-di-server.c.</dl>
<p> <code>&#8211;allow-mismatched-debuginfo=no|yes [no] </code></p>
<dl>
<dt>
<dd> When reading debuginfo from separate debuginfo objects, Valgrind will by default check that the main and debuginfo objects match, using the GNU debuglink mechanism. This guarantees that it does not read debuginfo from out of date debuginfo objects, and also ensures that Valgrind can&#8217;t crash as a result of mismatches. </p>
<p> This check can be overridden using &#8211;allow-mismatched-debuginfo=yes. This may be useful when the debuginfo and main objects have not been split in the proper way. Be careful when using this, though: it disables all consistency checking, and Valgrind has been observed to crash when the main and debuginfo objects don&#8217;t match.</dl>
<p> <code>&#8211;suppressions=&lt;filename&gt; [default: $PREFIX/lib/valgrind/default.supp] </code></p>
<dl>
<dt>
<dd> Specifies an extra file from which to read descriptions of errors to suppress. You may use up to 100 extra suppression files.</dl>
<p> <code>&#8211;gen-suppressions=&lt;yes|no|all&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When set to <i>yes</i>, Valgrind will pause after every error shown and print the line: </p>
<dl>
<dt>
<dd>
<pre><code>
-- --Print suppression ? -- -[Return / N / n / Y / y / C / c]-- --
</code></pre>
</dl>
<p> Pressing <i>Ret</i>, or <i>N Ret</i> or <i>n Ret</i>, causes Valgrind continue execution without printing a suppression for this error. </p>
<p> Pressing <i>Y Ret</i> or <i>y Ret</i> causes Valgrind to write a suppression for this error. You can then cut and paste it into a suppression file if you don&#8217;t want to hear about the error in the future. </p>
<p> When set to <i>all</i>, Valgrind will print a suppression for every reported error, without querying the user. </p>
<p> This option is particularly useful with C++ programs, as it prints out the suppressions with mangled names, as required. </p>
<p> Note that the suppressions printed are as specific as possible. You may want to common up similar ones, by adding wildcards to function names, and by using frame-level wildcards. The wildcarding facilities are powerful yet flexible, and with a bit of careful editing, you may be able to suppress a whole family of related errors with only a few suppressions. </p>
<p> Sometimes two different errors are suppressed by the same suppression, in which case Valgrind will output the suppression more than once, but you only need to have one copy in your suppression file (but having more than one won&#8217;t cause problems). Also, the suppression name is given as &lt;insert a suppression name here&gt;; the name doesn&#8217;t really matter, it&#8217;s only used with the <code>-v</code> option which prints out all used suppression records.</dl>
<p> <code>&#8211;input-fd=&lt;number&gt; [default: 0, stdin] </code></p>
<dl>
<dt>
<dd> When using <code>&#8211;gen-suppressions=yes</code>, Valgrind will stop so as to read keyboard input from you when each error occurs. By default it reads from the standard input (stdin), which is problematic for programs which close stdin. This option allows you to specify an alternative file descriptor from which to read input.</dl>
<p> <code>&#8211;dsymutil=no|yes [yes] </code></p>
<dl>
<dt>
<dd> This option is only relevant when running Valgrind on Mac OS X. </p>
<p> Mac OS X uses a deferred debug information (debuginfo) linking scheme. When object files containing debuginfo are linked into a .dylib or an executable, the debuginfo is not copied into the final file. Instead, the debuginfo must be linked manually by running dsymutil, a system-provided utility, on the executable or .dylib. The resulting combined debuginfo is placed in a directory alongside the executable or .dylib, but with the extension .dSYM. </p>
<p> With <code>&#8211;dsymutil=no</code>, Valgrind will detect cases where the .dSYM directory is either missing, or is present but does not appear to match the associated executable or .dylib, most likely because it is out of date. In these cases, Valgrind will print a warning message but take no further action. </p>
<p> With <code>&#8211;dsymutil=yes</code>, Valgrind will, in such cases, automatically run dsymutil as necessary to bring the debuginfo up to date. For all practical purposes, if you always use <code>&#8211;dsymutil=yes</code>, then there is never any need to run dsymutil manually or as part of your applications&#8217;s build system, since Valgrind will run it as necessary. </p>
<p> Valgrind will not attempt to run dsymutil on any executable or library in /usr/, /bin/, /sbin/, /opt/, /sw/, /System/, /Library/ or /Applications/ since dsymutil will always fail in such situations. It fails both because the debuginfo for such pre-installed system components is not available anywhere, and also because it would require write privileges in those directories. </p>
<p> Be careful when using <code>&#8211;dsymutil=yes</code>, since it will cause pre-existing .dSYM directories to be silently deleted and re-created. Also note that dsymutil is quite slow, sometimes excessively so.</dl>
<p> <code>&#8211;max-stackframe=&lt;number&gt; [default: 2000000] </code></p>
<dl>
<dt>
<dd> The maximum size of a stack frame. If the stack pointer moves by more than this amount then Valgrind will assume that the program is switching to a different stack. </p>
<p> You may need to use this option if your program has large stack-allocated arrays. Valgrind keeps track of your program&#8217;s stack pointer. If it changes by more than the threshold amount, Valgrind assumes your program is switching to a different stack, and Memcheck behaves differently than it would for a stack pointer change smaller than the threshold. Usually this heuristic works well. However, if your program allocates large structures on the stack, this heuristic will be fooled, and Memcheck will subsequently report large numbers of invalid stack accesses. This option allows you to change the threshold to a different value. </p>
<p> You should only consider use of this option if Valgrind&#8217;s debug output directs you to do so. In that case it will tell you the new threshold you should specify. </p>
<p> In general, allocating large structures on the stack is a bad idea, because you can easily run out of stack space, especially on systems with limited memory or which expect to support large numbers of threads each with a small stack, and also because the error checking performed by Memcheck is more effective for heap-allocated data than for stack-allocated data. If you have to use this option, you may wish to consider rewriting your code to allocate on the heap rather than on the stack.</dl>
<p> <code>&#8211;main-stacksize=&lt;number&gt; [default: use current &#8216;ulimit&#8217; value] </code></p>
<dl>
<dt>
<dd> Specifies the size of the main thread&#8217;s stack. </p>
<p> To simplify its memory management, Valgrind reserves all required space for the main thread&#8217;s stack at startup. That means it needs to know the required stack size at startup. </p>
<p> By default, Valgrind uses the current &quot;ulimit&quot; value for the stack size, or 16 MB, whichever is lower. In many cases this gives a stack size in the range 8 to 16 MB, which almost never overflows for most applications. </p>
<p> If you need a larger total stack size, use <code>&#8211;main-stacksize</code> to specify it. Only set it as high as you need, since reserving far more space than you need (that is, hundreds of megabytes more than you need) constrains Valgrind&#8217;s memory allocators and may reduce the total amount of memory that Valgrind can use. This is only really of significance on 32-bit machines. </p>
<p> On Linux, you may request a stack of size up to 2GB. Valgrind will stop with a diagnostic message if the stack cannot be allocated. </p>
<p> <code>&#8211;main-stacksize</code> only affects the stack size for the program&#8217;s initial thread. It has no bearing on the size of thread stacks, as Valgrind does not allocate those. </p>
<p> You may need to use both <code>&#8211;main-stacksize</code> and <code>&#8211;max-stackframe</code> together. It is important to understand that <code>&#8211;main-stacksize</code> sets the maximum total stack size, whilst <code>&#8211;max-stackframe</code> specifies the largest size of any one stack frame. You will have to work out the <code>&#8211;main-stacksize</code> value for yourself (usually, if your applications segfaults). But Valgrind will tell you the needed <code>&#8211;max-stackframe</code> size, if necessary. </p>
<p> As discussed further in the description of <code>&#8211;max-stackframe</code>, a requirement for a large stack is a sign of potential portability problems. You are best advised to place all large data in heap-allocated memory.</dl>
<p> <code>&#8211;max-threads=&lt;number&gt; [default: 500] </code></p>
<dl>
<dt>
<dd> By default, Valgrind can handle to up to 500 threads. Occasionally, that number is too small. Use this option to provide a different limit. E.g. &#8211;max-threads=3000.</dl>
<h2>MALLOC()-RELATED OPTIONS</h2>
<p> For tools that use their own version of malloc (e.g. Memcheck, Massif, Helgrind, DRD), the following options apply. </p>
<p> <code>&#8211;alignment=&lt;number&gt; [default: 8 or 16, depending on the platform] </code></p>
<dl>
<dt>
<dd> By default Valgrind&#8217;s <code>malloc</code>, <code>realloc</code>, etc, return a block whose starting address is 8-byte aligned or 16-byte aligned (the value depends on the platform and matches the platform default). This option allows you to specify a different alignment. The supplied value must be greater than or equal to the default, less than or equal to 4096, and must be a power of two.</dl>
<p> <code>&#8211;redzone-size=&lt;number&gt; [default: depends on the tool] </code></p>
<dl>
<dt>
<dd> Valgrind&#8217;s <code>malloc, realloc,</code> etc, add padding blocks before and after each heap block allocated by the program being run. Such padding blocks are called redzones. The default value for the redzone size depends on the tool. For example, Memcheck adds and protects a minimum of 16 bytes before and after each block allocated by the client. This allows it to detect block underruns or overruns of up to 16 bytes. </p>
<p> Increasing the redzone size makes it possible to detect overruns of larger distances, but increases the amount of memory used by Valgrind. Decreasing the redzone size will reduce the memory needed by Valgrind but also reduces the chances of detecting over/underruns, so is not recommended.</dl>
<p> <code>&#8211;xtree-memory=none|allocs|full [none] </code></p>
<dl>
<dt>
<dd> Tools replacing Valgrind&#8217;s <code>malloc, realloc,</code> etc, can optionally produce an execution tree detailing which piece of code is responsible for heap memory usage. See ??? for a detailed explanation about execution trees. </p>
<p> When set to <i>none</i>, no memory execution tree is produced. </p>
<p> When set to <i>allocs</i>, the memory execution tree gives the current number of allocated bytes and the current number of allocated blocks. </p>
<p> When set to <i>full</i>, the memory execution tree gives 6 different measurements : the current number of allocated bytes and blocks (same values as for <i>allocs</i>), the total number of allocated bytes and blocks, the total number of freed bytes and blocks. </p>
<p> Note that the overhead in cpu and memory to produce an xtree depends on the tool. The overhead in cpu is small for the value <i>allocs</i>, as the information needed to produce this report is maintained in any case by the tool. For massif and helgrind, specifying <i>full</i> implies to capture a stack trace for each free operation, while normally these tools only capture an allocation stack trace. For Memcheck, the cpu overhead for the value <i>full</i> is small, as this can only be used in combination with <code>&#8211;keep-stacktraces=alloc-and-free</code> or <code>&#8211;keep-stacktraces=alloc-then-free</code>, which already records a stack trace for each free operation. The memory overhead varies between 5 and 10 words per unique stacktrace in the xtree, plus the memory needed to record the stack trace for the free operations, if needed specifically for the xtree.</dl>
<p> <code>&#8211;xtree-memory-file=&lt;filename&gt; [default: xtmemory.kcg.%p] </code></p>
<dl>
<dt>
<dd> Specifies that Valgrind should produce the xtree memory report in the specified file. Any <code>%p</code> or <code>%q</code> sequences appearing in the filename are expanded in exactly the same way as they are for <code>&#8211;log-file</code>. See the description of &#8211;log-file for details. </p>
<p> If the filename contains the extension <code>.ms</code>, then the produced file format will be a massif output file format. If the filename contains the extension <code>.kcg</code> or no extension is provided or recognised, then the produced file format will be a callgrind output format. </p>
<p> See ??? for a detailed explanation about execution trees formats.</dl>
<h2>UNCOMMON OPTIONS</h2>
<p> These options apply to all tools, as they affect certain obscure workings of the Valgrind core. Most people won&#8217;t need to use them. </p>
<p> <code>&#8211;smc-check=&lt;none|stack|all|all-non-file&gt; [default: all-non-file for x86/amd64/s390x, stack for other archs] </code></p>
<dl>
<dt>
<dd> This option controls Valgrind&#8217;s detection of self-modifying code. If no checking is done, when a program executes some code, then overwrites it with new code, and executes the new code, Valgrind will continue to execute the translations it made for the old code. This will likely lead to incorrect behaviour and/or crashes. </p>
<p> For &quot;modern&quot; architectures &#8212; anything that&#8217;s not x86, amd64 or s390x &#8212; the default is <i>stack</i>. This is because a correct program must take explicit action to reestablish D-I cache coherence following code modification. Valgrind observes and honours such actions, with the result that self-modifying code is transparently handled with zero extra cost. </p>
<p> For x86, amd64 and s390x, the program is not required to notify the hardware of required D-I coherence syncing. Hence the default is <i>all-non-file</i>, which covers the normal case of generating code into an anonymous (non-file-backed) mmap&#8217;d area. </p>
<p> The meanings of the four available settings are as follows. No detection (<i>none</i>), detect self-modifying code on the stack (which is used by GCC to implement nested functions) (<i>stack</i>), detect self-modifying code everywhere (<i>all</i>), and detect self-modifying code everywhere except in file-backed mappings (<i>all-non-file</i>). </p>
<p> Running with <i>all</i> will slow Valgrind down noticeably. Running with <i>none</i> will rarely speed things up, since very little code gets dynamically generated in most programs. The <code>VALGRIND_DISCARD_TRANSLATIONS</code> client request is an alternative to <code>&#8211;smc-check=all</code> and <code>&#8211;smc-check=all-non-file</code> that requires more programmer effort but allows Valgrind to run your program faster, by telling it precisely when translations need to be re-made. </p>
<p> <code>&#8211;smc-check=all-non-file</code> provides a cheaper but more limited version of <code>&#8211;smc-check=all</code>. It adds checks to any translations that do not originate from file-backed memory mappings. Typical applications that generate code, for example JITs in web browsers, generate code into anonymous mmaped areas, whereas the &quot;fixed&quot; code of the browser always lives in file-backed mappings. <code>&#8211;smc-check=all-non-file</code> takes advantage of this observation, limiting the overhead of checking to code which is likely to be JIT generated.</dl>
<p> <code>&#8211;read-inline-info=&lt;yes|no&gt; [default: see below] </code></p>
<dl>
<dt>
<dd> When enabled, Valgrind will read information about inlined function calls from DWARF3 debug info. This slows Valgrind startup and makes it use more memory (typically for each inlined piece of code, 6 words and space for the function name), but it results in more descriptive stacktraces. Currently, this functionality is enabled by default only for Linux, Android and Solaris targets and only for the tools Memcheck, Massif, Helgrind and DRD. Here is an example of some stacktraces with <code>&#8211;read-inline-info=no</code>: </p>
<dl>
<dt>
<dd>
== 15380 == Conditional jump or move depends on uninitialised value(s) == 15380 == at 0x80484EA : main(inlinfo.c : 6) == 15380 == == 15380 == Conditional jump or move depends on uninitialised value(s) == 15380 == at 0x8048550 : fun_noninline(inlinfo.c : 6) == 15380 == by 0x804850E : main(inlinfo.c : 34) == 15380 == == 15380 == Conditional jump or move depends on uninitialised value(s) == 15380 == at 0x8048520 : main(inlinfo.c : 6)
</dl>
<p> And here are the same errors with <code>&#8211;read-inline-info=yes</code>: </p>
<dl>
<dt>
<dd>
== 15377 == Conditional jump or move depends on uninitialised value(s) == 15377 == at 0x80484EA : fun_d(inlinfo.c : 6) == 15377 == by 0x80484EA : fun_c(inlinfo.c : 14) == 15377 == by 0x80484EA : fun_b(inlinfo.c : 20) == 15377 == by 0x80484EA : fun_a(inlinfo.c : 26) == 15377 == by 0x80484EA : main(inlinfo.c : 33) == 15377 == == 15377 == Conditional jump or move depends on uninitialised value(s) == 15377 == at 0x8048550 : fun_d(inlinfo.c : 6) == 15377 == by 0x8048550 : fun_noninline(inlinfo.c : 41) == 15377 == by 0x804850E : main(inlinfo.c : 34) == 15377 == == 15377 == Conditional jump or move depends on uninitialised value(s) == 15377 == at 0x8048520 : fun_d(inlinfo.c : 6) == 15377 == by 0x8048520 : main(inlinfo.c : 35)
</dl>
</dl>
<p> <code>&#8211;read-var-info=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, Valgrind will read information about variable types and locations from DWARF3 debug info. This slows Valgrind startup significantly and makes it use significantly more memory, but for the tools that can take advantage of it (Memcheck, Helgrind, DRD) it can result in more precise error messages. For example, here are some standard errors issued by Memcheck: </p>
<dl>
<dt>
<dd>
== 15363 == Uninitialised byte(s)<br />
found during client check request == 15363 == at 0x80484A9 : croak(varinfo1.c : 28) == 15363 == by 0x8048544 : main(varinfo1.c : 55) == 15363 == Address 0x80497f7 is 7 bytes inside data symbol &#8220;global_i2&#8221; == 15363 ==<br />
                                                                                                               == 15363 == Uninitialised byte(s)<br />
found during client check request == 15363 == at 0x80484A9 : croak(varinfo1.c : 28) == 15363 == by 0x8048550 : main(varinfo1.c : 56) == 15363 == Address 0xbea0d0cc is on thread 1&#8217;s stack<br />
                                                                                                               == 15363 == in frame #1,<br />
    created by main(varinfo1.c : 45)
</dl>
<p> And here are the same errors with <code>&#8211;read-var-info=yes</code>: </p>
<dl>
<dt>
<dd>
<pre><code>
== 15370 == Uninitialised byte(s)
found during client check request == 15370 == at 0x80484A9 : croak(varinfo1.c : 28) == 15370 == by 0x8048544 : main(varinfo1.c : 55) == 15370 == Location 0x80497f7 is 0 bytes inside global_i2[7],
    == 15370 == a global variable declared at varinfo1.c : 41 == 15370 ==
        == 15370 == Uninitialised byte(s)
found during client check request == 15370 == at 0x80484A9 : croak(varinfo1.c : 28) == 15370 == by 0x8048550 : main(varinfo1.c : 56) == 15370 == Location 0xbeb4a0cc is 0 bytes inside local var "local" == 15370 == declared at varinfo1.c : 46, in frame #1 of thread 1
</code></pre>
</dl>
</dl>
<p> <code>&#8211;vgdb-poll=&lt;number&gt; [default: 5000] </code></p>
<dl>
<dt>
<dd> As part of its main loop, the Valgrind scheduler will poll to check if some activity (such as an external command or some input from a gdb) has to be handled by gdbserver. This activity poll will be done after having run the given number of basic blocks (or slightly more than the given number of basic blocks). This poll is quite cheap so the default value is set relatively low. You might further decrease this value if vgdb cannot use ptrace system call to interrupt Valgrind if all threads are (most of the time) blocked in a system call.</dl>
<p> <code>&#8211;vgdb-shadow-registers=no|yes [default: no] </code></p>
<dl>
<dt>
<dd> When activated, gdbserver will expose the Valgrind shadow registers to GDB. With this, the value of the Valgrind shadow registers can be examined or changed using GDB. Exposing shadow registers only works with GDB version 7.1 or later.</dl>
<p> <code>&#8211;vgdb-prefix=&lt;prefix&gt; [default: /tmp/vgdb-pipe] </code></p>
<dl>
<dt>
<dd> To communicate with gdb/vgdb, the Valgrind gdbserver creates 3 files (2 named FIFOs and a mmap shared memory file). The prefix option controls the directory and prefix for the creation of these files.</dl>
<p> <code>&#8211;run-libc-freeres=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> This option is only relevant when running Valgrind on Linux. </p>
<p> The GNU C library (<code>libc.so</code>), which is used by all programs, may allocate memory for its own uses. Usually it doesn&#8217;t bother to free that memory when the program ends&#8212;there would be no point, since the Linux kernel reclaims all process resources when a process exits anyway, so it would just slow things down. </p>
<p> The glibc authors realised that this behaviour causes leak checkers, such as Valgrind, to falsely report leaks in glibc, when a leak check is done at exit. In order to avoid this, they provided a routine called <code>__libc_freeres</code> specifically to make glibc release all memory it has allocated. Memcheck therefore tries to run <code>__libc_freeres</code> at exit. </p>
<p> Unfortunately, in some very old versions of glibc, <code>__libc_freeres</code> is sufficiently buggy to cause segmentation faults. This was particularly noticeable on Red Hat 7.1. So this option is provided in order to inhibit the run of <code>__libc_freeres</code>. If your program seems to run fine on Valgrind, but segfaults at exit, you may find that <code>&#8211;run-libc-freeres=no</code> fixes that, although at the cost of possibly falsely reporting space leaks in libc.so.</dl>
<p> <code>&#8211;run-cxx-freeres=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> This option is only relevant when running Valgrind on Linux or Solaris C++ programs. </p>
<p> The GNU Standard C++ library (<code>libstdc++.so</code>), which is used by all C++ programs compiled with g++, may allocate memory for its own uses. Usually it doesn&#8217;t bother to free that memory when the program ends&#8212;there would be no point, since the kernel reclaims all process resources when a process exits anyway, so it would just slow things down. </p>
<p> The gcc authors realised that this behaviour causes leak checkers, such as Valgrind, to falsely report leaks in libstdc++, when a leak check is done at exit. In order to avoid this, they provided a routine called <code>__gnu_cxx::__freeres</code> specifically to make libstdc++ release all memory it has allocated. Memcheck therefore tries to run <code>__gnu_cxx::__freeres</code> at exit. </p>
<p> For the sake of flexibility and unforeseen problems with <code>__gnu_cxx::__freeres</code>, option <code>&#8211;run-cxx-freeres=no</code> exists, although at the cost of possibly falsely reporting space leaks in libstdc++.so.</dl>
<p> <code>&#8211;sim-hints=hint1,hint2,&#8230; </code></p>
<dl>
<dt>
<dd> Pass miscellaneous hints to Valgrind which slightly modify the simulated behaviour in nonstandard or dangerous ways, possibly to help the simulation of strange features. By default no hints are enabled. Use with caution! Currently known hints are: </p>
<dl>
<dt>
<dd> &bull; <code>lax-ioctls: </code> Be very lax about ioctl handling; the only assumption is that the size is correct. Doesn&#8217;t require the full buffer to be initialised when writing. Without this, using some device drivers with a large number of strange ioctl commands becomes very tiresome.</dl>
<dl>
<dt>
<dd> &bull; <code>fuse-compatible: </code> Enable special handling for certain system calls that may block in a FUSE file-system. This may be necessary when running Valgrind on a multi-threaded program that uses one thread to manage a FUSE file-system and another thread to access that file-system.</dl>
<dl>
<dt>
<dd> &bull; <code>enable-outer: </code> Enable some special magic needed when the program being run is itself Valgrind.</dl>
<dl>
<dt>
<dd> &bull; <code>no-inner-prefix: </code> Disable printing a prefix <code>&gt;</code> in front of each stdout or stderr output line in an inner Valgrind being run by an outer Valgrind. This is useful when running Valgrind regression tests in an outer/inner setup. Note that the prefix <code>&gt;</code> will always be printed in front of the inner debug logging lines.</dl>
<dl>
<dt>
<dd> &bull; <code>no-nptl-pthread-stackcache: </code> This hint is only relevant when running Valgrind on Linux; it is ignored on Solaris and Mac OS X. </p>
<p> The GNU glibc pthread library (<code>libpthread.so</code>), which is used by pthread programs, maintains a cache of pthread stacks. When a pthread terminates, the memory used for the pthread stack and some thread local storage related data structure are not always directly released. This memory is kept in a cache (up to a certain size), and is re-used if a new thread is started. </p>
<p> This cache causes the helgrind tool to report some false positive race condition errors on this cached memory, as helgrind does not understand the internal glibc cache synchronisation primitives. So, when using helgrind, disabling the cache helps to avoid false positive race conditions, in particular when using thread local storage variables (e.g. variables using the <code>__thread</code> qualifier). </p>
<p> When using the memcheck tool, disabling the cache ensures the memory used by glibc to handle __thread variables is directly released when a thread terminates. </p>
<p> Note: Valgrind disables the cache using some internal knowledge of the glibc stack cache implementation and by examining the debug information of the pthread library. This technique is thus somewhat fragile and might not work for all glibc versions. This has been successfully tested with various glibc versions (e.g. 2.11, 2.16, 2.18) on various platforms.</dl>
<dl>
<dt>
<dd> &bull; <code>lax-doors: </code> (Solaris only) Be very lax about door syscall handling over unrecognised door file descriptors. Does not require that full buffer is initialised when writing. Without this, programs using libdoor(3LIB) functionality with completely proprietary semantics may report large number of false positives.</dl>
<dl>
<dt>
<dd> &bull; <code>fallback-llsc: </code>(MIPS and ARM64 only): Enables an alternative implementation of Load-Linked (LL) and Store-Conditional (SC) instructions. The standard implementation gives more correct behaviour, but can cause indefinite looping on certain processor implementations that are intolerant of extra memory references between LL and SC. So far this is known only to happen on Cavium 3 cores. You should not need to use this flag, since the relevant cores are detected at startup and the alternative implementation is automatically enabled if necessary. There is no equivalent anti-flag: you cannot force-disable the alternative implementation, if it is automatically enabled. The underlying problem exists because the &quot;standard&quot; implementation of LL and SC is done by copying through LL and SC instructions into the instrumented code. However, tools may insert extra instrumentation memory references in between the LL and SC instructions. These memory references are not present in the original uninstrumented code, and their presence in the instrumented code can cause the SC instructions to persistently fail, leading to indefinite looping in LL-SC blocks. The alternative implementation gives correct behaviour of LL and SC instructions between threads in a process, up to and including the ABA scenario. It also gives correct behaviour between a Valgrinded thread and a non-Valgrinded thread running in a different process, that communicate via shared memory, but only up to and including correct CAS behaviour &#8212; in this case the ABA scenario may not be correctly handled.</dl>
</dl>
<p> <code>&#8211;fair-sched=&lt;no|yes|try&gt; [default: no] </code></p>
<dl>
<dt>
<dd> The <code>&#8211;fair-sched</code> option controls the locking mechanism used by Valgrind to serialise thread execution. The locking mechanism controls the way the threads are scheduled, and different settings give different trade-offs between fairness and performance. For more details about the Valgrind thread serialisation scheme and its impact on performance and thread scheduling, see Scheduling and Multi-Thread Performance. </p>
<dl>
<dt>
<dd> &bull; The value <code>&#8211;fair-sched=yes</code> activates a fair scheduler. In short, if multiple threads are ready to run, the threads will be scheduled in a round robin fashion. This mechanism is not available on all platforms or Linux versions. If not available, using <code>&#8211;fair-sched=yes</code> will cause Valgrind to terminate with an error. </p>
<p> You may find this setting improves overall responsiveness if you are running an interactive multithreaded program, for example a web browser, on Valgrind.</dl>
<dl>
<dt>
<dd> &bull; The value <code>&#8211;fair-sched=try</code> activates fair scheduling if available on the platform. Otherwise, it will automatically fall back to <code>&#8211;fair-sched=no</code>.</dl>
<dl>
<dt>
<dd> &bull; The value <code>&#8211;fair-sched=no</code> activates a scheduler which does not guarantee fairness between threads ready to run, but which in general gives the highest performance.</dl>
</dl>
<p> <code>&#8211;kernel-variant=variant1,variant2,&#8230;</code></p>
<dl>
<dt>
<dd> Handle system calls and ioctls arising from minor variants of the default kernel for this platform. This is useful for running on hacked kernels or with kernel modules which support nonstandard ioctls, for example. Use with caution. If you don&#8217;t understand what this option does then you almost certainly don&#8217;t need it. Currently known variants are: </p>
<dl>
<dt>
<dd> &bull; <code>bproc</code>: support the <code>sys_broc</code> system call on x86. This is for running on BProc, which is a minor variant of standard Linux which is sometimes used for building clusters.</dl>
<dl>
<dt>
<dd> &bull; <code>android-no-hw-tls</code>: some versions of the Android emulator for ARM do not provide a hardware TLS (thread-local state) register, and Valgrind crashes at startup. Use this variant to select software support for TLS.</dl>
<dl>
<dt>
<dd> &bull; <code>android-gpu-sgx5xx</code>: use this to support handling of proprietary ioctls for the PowerVR SGX 5XX series of GPUs on Android devices. Failure to select this does not cause stability problems, but may cause Memcheck to report false errors after the program performs GPU-specific ioctls.</dl>
<dl>
<dt>
<dd> &bull; <code>android-gpu-adreno3xx</code>: similarly, use this to support handling of proprietary ioctls for the Qualcomm Adreno 3XX series of GPUs on Android devices.</dl>
</dl>
<p> <code>&#8211;merge-recursive-frames=&lt;number&gt; [default: 0] </code></p>
<dl>
<dt>
<dd> Some recursive algorithms, for example balanced binary tree implementations, create many different stack traces, each containing cycles of calls. A cycle is defined as two identical program counter values separated by zero or more other program counter values. Valgrind may then use a lot of memory to store all these stack traces. This is a poor use of memory considering that such stack traces contain repeated uninteresting recursive calls instead of more interesting information such as the function that has initiated the recursive call. </p>
<p> The option <code>&#8211;merge-recursive-frames=&lt;number&gt;</code> instructs Valgrind to detect and merge recursive call cycles having a size of up to <code>&lt;number&gt;</code> frames. When such a cycle is detected, Valgrind records the cycle in the stack trace as a unique program counter. </p>
<p> The value 0 (the default) causes no recursive call merging. A value of 1 will cause stack traces of simple recursive algorithms (for example, a factorial implementation) to be collapsed. A value of 2 will usually be needed to collapse stack traces produced by recursive algorithms such as binary trees, quick sort, etc. Higher values might be needed for more complex recursive algorithms. </p>
<p> Note: recursive calls are detected by analysis of program counter values. They are not detected by looking at function names.</dl>
<p> <code>&#8211;num-transtab-sectors=&lt;number&gt; [default: 6 for Android platforms, 16 for all others] </code></p>
<dl>
<dt>
<dd> Valgrind translates and instruments your program&#8217;s machine code in small fragments (basic blocks). The translations are stored in a translation cache that is divided into a number of sections (sectors). If the cache is full, the sector containing the oldest translations is emptied and reused. If these old translations are needed again, Valgrind must re-translate and re-instrument the corresponding machine code, which is expensive. If the &quot;executed instructions&quot; working set of a program is big, increasing the number of sectors may improve performance by reducing the number of re-translations needed. Sectors are allocated on demand. Once allocated, a sector can never be freed, and occupies considerable space, depending on the tool and the value of <code>&#8211;avg-transtab-entry-size</code> (about 40 MB per sector for Memcheck). Use the option <code>&#8211;stats=yes</code> to obtain precise information about the memory used by a sector and the allocation and recycling of sectors.</dl>
<p> <code>&#8211;avg-transtab-entry-size=&lt;number&gt; [default: 0, meaning use tool provided default] </code></p>
<dl>
<dt>
<dd> Average size of translated basic block. This average size is used to dimension the size of a sector. Each tool provides a default value to be used. If this default value is too small, the translation sectors will become full too quickly. If this default value is too big, a significant part of the translation sector memory will be unused. Note that the average size of a basic block translation depends on the tool, and might depend on tool options. For example, the memcheck option <code>&#8211;track-origins=yes</code> increases the size of the basic block translations. Use <code>&#8211;avg-transtab-entry-size</code> to tune the size of the sectors, either to gain memory or to avoid too many retranslations.</dl>
<p> <code>&#8211;aspace-minaddr=&lt;address&gt; [default: depends on the platform] </code></p>
<dl>
<dt>
<dd> To avoid potential conflicts with some system libraries, Valgrind does not use the address space below <code>&#8211;aspace-minaddr</code> value, keeping it reserved in case a library specifically requests memory in this region. So, some &quot;pessimistic&quot; value is guessed by Valgrind depending on the platform. On linux, by default, Valgrind avoids using the first 64MB even if typically there is no conflict in this complete zone. You can use the option <code>&#8211;aspace-minaddr</code> to have your memory hungry application benefitting from more of this lower memory. On the other hand, if you encounter a conflict, increasing aspace-minaddr value might solve it. Conflicts will typically manifest themselves with mmap failures in the low range of the address space. The provided address must be page aligned and must be equal or bigger to 0x1000 (4KB). To find the default value on your platform, do something such as valgrind -d -d date 2&gt;&amp;1 | grep -i minaddr. Values lower than 0x10000 (64KB) are known to create problems on some distributions.</dl>
<p> <code>&#8211;valgrind-stacksize=&lt;number&gt; [default: 1MB] </code></p>
<dl>
<dt>
<dd> For each thread, Valgrind needs its own &#8216;private&#8217; stack. The default size for these stacks is largely dimensioned, and so should be sufficient in most cases. In case the size is too small, Valgrind will segfault. Before segfaulting, a warning might be produced by Valgrind when approaching the limit. </p>
<p> Use the option <code>&#8211;valgrind-stacksize</code> if such an (unlikely) warning is produced, or Valgrind dies due to a segmentation violation. Such segmentation violations have been seen when demangling huge C++ symbols. </p>
<p> If your application uses many threads and needs a lot of memory, you can gain some memory by reducing the size of these Valgrind stacks using the option <code>&#8211;valgrind-stacksize</code>.</dl>
<p> <code>&#8211;show-emwarns=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, Valgrind will emit warnings about its CPU emulation in certain cases. These are usually not interesting.</dl>
<p> <code>&#8211;require-text-symbol=:sonamepatt:fnnamepatt</code></p>
<dl>
<dt>
<dd> When a shared object whose soname matches <i>sonamepatt</i> is loaded into the process, examine all the text symbols it exports. If none of those match <i>fnnamepatt</i>, print an error message and abandon the run. This makes it possible to ensure that the run does not continue unless a given shared object contains a particular function name. </p>
<p> Both <i>sonamepatt</i> and <i>fnnamepatt</i> can be written using the usual <i>?</i> and <i>*</i> wildcards. For example: <i>&quot;:*libc.so*:foo?bar&quot;</i>. You may use characters other than a colon to separate the two patterns. It is only important that the first character and the separator character are the same. For example, the above example could also be written <i>&quot;Q*libc.so*Qfoo?bar&quot;</i>. Multiple <i> &#8211;require-text-symbol</i> flags are allowed, in which case shared objects that are loaded into the process will be checked against all of them. </p>
<p> The purpose of this is to support reliable usage of marked-up libraries. For example, suppose we have a version of GCC&#8217;s <i>libgomp.so</i> which has been marked up with annotations to support Helgrind. It is only too easy and confusing to load the wrong, un-annotated <i>libgomp.so</i> into the application. So the idea is: add a text symbol in the marked-up library, for example <i>annotated_for_helgrind_3_6</i>, and then give the flag <i>&#8211;require-text-symbol=:*libgomp*so*:annotated_for_helgrind_3_6</i> so that when <i>libgomp.so</i> is loaded, Valgrind scans its symbol table, and if the symbol isn&#8217;t present the run is aborted, rather than continuing silently with the un-marked-up library. Note that you should put the entire flag in quotes to stop shells expanding up the <i>*</i> and <i>?</i> wildcards.</dl>
<p> <code>&#8211;soname-synonyms=syn1=pattern1,syn2=pattern2,&#8230;</code></p>
<dl>
<dt>
<dd> When a shared library is loaded, Valgrind checks for functions in the library that must be replaced or wrapped. For example, Memcheck replaces some string and memory functions (strchr, strlen, strcpy, memchr, memcpy, memmove, etc.) with its own versions. Such replacements are normally done only in shared libraries whose soname matches a predefined soname pattern (e.g. <i>libc.so*</i> on linux). By default, no replacement is done for a statically linked binary or for alternative libraries, except for the allocation functions (malloc, free, calloc, memalign, realloc, operator new, operator delete, etc.) Such allocation functions are intercepted by default in any shared library or in the executable if they are exported as global symbols. This means that if a replacement allocation library such as tcmalloc is found, its functions are also intercepted by default. In some cases, the replacements allow <code>&#8211;soname-synonyms</code> to specify one additional synonym pattern, giving flexibility in the replacement. Or to prevent interception of all public allocation symbols. </p>
<p> Currently, this flexibility is only allowed for the malloc related functions, using the synonym <i>somalloc</i>. This synonym is usable for all tools doing standard replacement of malloc related functions (e.g. memcheck, helgrind, drd, massif, dhat, exp-sgcheck). </p>
<dl>
<dt>
<dd> &bull; Alternate malloc library: to replace the malloc related functions in a specific alternate library with soname <i>mymalloclib.so</i> (and not in any others), give the option <code>&#8211;soname-synonyms=somalloc=mymalloclib.so</code>. A pattern can be used to match multiple libraries sonames. For example, <code>&#8211;soname-synonyms=somalloc=*tcmalloc*</code> will match the soname of all variants of the tcmalloc library (native, debug, profiled, &#8230; tcmalloc variants). </p>
<p> Note: the soname of a elf shared library can be retrieved using the readelf utility.</dl>
<dl>
<dt>
<dd> &bull; Replacements in a statically linked library are done by using the <i>NONE</i> pattern. For example, if you link with <i>libtcmalloc.a</i>, and only want to intercept the malloc related functions in the executable (and standard libraries) themselves, but not any other shared libraries, you can give the option <code>&#8211;soname-synonyms=somalloc=NONE</code>. Note that a NONE pattern will match the main executable and any shared library having no soname.</dl>
<dl>
<dt>
<dd> &bull; To run a &quot;default&quot; Firefox build for Linux, in which JEMalloc is linked in to the main executable, use <code>&#8211;soname-synonyms=somalloc=NONE</code>.</dl>
<dl>
<dt>
<dd> &bull; To only intercept allocation symbols in the default system libraries, but not in any other shared library or the executable defining public malloc or operator new related functions use a non-existing library name like <code>&#8211;soname-synonyms=somalloc=nouserintercepts</code> (where <i>nouserintercepts</i> can be any non-existing library name).</dl>
<dl>
<dt>
<dd> &bull; Shared library of the dynamic (runtime) linker is excluded from searching for global public symbols, such as those for the malloc related functions (identified by <i>somalloc</i> synonym).</dl>
</dl>
<p> <code>&#8211;progress-interval=&lt;number&gt; [default: 0, meaning &#8216;disabled&#8217;] </code></p>
<dl>
<dt>
<dd> This is an enhancement to Valgrind&#8217;s debugging output. It is unlikely to be of interest to end users. </p>
<p> When <i>number</i> is set to a non-zero value, Valgrind will print a one-line progress summary every <i>number</i> seconds. Valid settings for <i>number</i> are between 0 and 3600 inclusive. Here&#8217;s some example output with <i>number</i> set to 10: </p>
<dl>
<dt>
<dd>
<pre>
PROGRESS: U 110s, W 113s, 97.3% CPU, EvC 414.79M, TIn 616.7k, TOut 0.5k, #thr 67
PROGRESS: U 120s, W 124s, 96.8% CPU, EvC 505.27M, TIn 636.6k, TOut 3.0k, #thr 64
PROGRESS: U 130s, W 134s, 97.0% CPU, EvC 574.90M, TIn 657.5k, TOut 3.0k, #thr 63
</pre>
</dl>
<p> Each line shows: </p>
<dl>
<dt>
<dd> &bull; <i>U</i>: total user time.RE </p>
<dl>
<dt>
<dd> &bull; <i>W</i>: total wallclock time.RE </p>
<dl>
<dt>
<dd> &bull; <i>CPU</i>: overall average cpu use.RE </p>
<dl>
<dt>
<dd> &bull; <i>EvC</i>: number of event checks. An event<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;check is a backwards branch in the simulated program, so this is a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;measure of forward progress of the program.RE </p>
<dl>
<dt>
<dd> &bull; <i>TIn</i>: number of code blocks instrumented<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;by the JIT.RE </p>
<dl>
<dt>
<dd> &bull; <i>TOut</i>: number of instrumented code<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks that have been thrown away.RE </p>
<dl>
<dt>
<dd> &bull; <i>#thr</i>: number of threads in the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;program.RE </p>
<p> From the progress of these, it is possible to observe: </p>
<dl>
<dt>
<dd> &bull; when the program is compute bound (<i>TIn</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rises slowly,&nbsp;<i>EvC</i>&nbsp;rises rapidly).RE </p>
<dl>
<dt>
<dd> &bull; when the program is in a spinloop<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(<i>TIn</i>/<i>TOut</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fixed,&nbsp;<i>EvC</i>&nbsp;rises rapidly).RE </p>
<dl>
<dt>
<dd> &bull; when the program is JIT-bound (<i>TIn</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;rises rapidly).RE </p>
<dl>
<dt>
<dd> &bull; when the program is rapidly discarding code<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(<i>TOut</i>&nbsp;rises rapidly).RE </p>
<dl>
<dt>
<dd> &bull; when the program is about to achieve some expected state<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(<i>EvC</i>&nbsp;arrives at some value you<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;expect).RE </p>
<dl>
<dt>
<dd> &bull;<br />
&nbsp;when the program is idling&nbsp;(<i>U</i>&nbsp;rises<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;more slowly than&nbsp;<i>W</i>).RE </p>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>DEBUGGING VALGRIND OPTIONS</h2>
<p> There are also some options for debugging Valgrind itself. You shouldn&#8217;t need to use them in the normal run of things. If you wish to see the list, use the <code>&#8211;help-debug</code> option.</p>
<h2>MEMCHECK OPTIONS</h2>
<p> <code>&#8211;leak-check=&lt;no|summary|yes|full&gt; [default: summary] </code></p>
<dl>
<dt>
<dd> When enabled, search for memory leaks when the client program finishes. If set to <i>summary</i>, it says how many leaks occurred. If set to <i>full</i> or <i>yes</i>, each individual leak will be shown in detail and/or counted as an error, as specified by the options <code>&#8211;show-leak-kinds</code> and <code>&#8211;errors-for-leak-kinds</code>.</dl>
<p> <code>&#8211;leak-resolution=&lt;low|med|high&gt; [default: high] </code></p>
<dl>
<dt>
<dd> When doing leak checking, determines how willing Memcheck is to consider different backtraces to be the same for the purposes of merging multiple leaks into a single leak report. When set to <i>low</i>, only the first two entries need match. When <i>med</i>, four entries have to match. When <i>high</i>, all entries need to match. </p>
<p> For hardcore leak debugging, you probably want to use <code>&#8211;leak-resolution=high</code> together with <code>&#8211;num-callers=40</code> or some such large number. </p>
<p> Note that the <code>&#8211;leak-resolution</code> setting does not affect Memcheck&#8217;s ability to find leaks. It only changes how the results are presented.</dl>
<p> <code>&#8211;show-leak-kinds=&lt;set&gt; [default: definite,possible] </code></p>
<dl>
<dt>
<dd> Specifies the leak kinds to show in a <i>full</i> leak search, in one of the following ways: </p>
<dl>
<dt>
<dd> &bull; a comma separated list of one or more of <code>definite indirect possible reachable</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>all</code> to specify the complete set (all leak kinds). It is equivalent to <code>&#8211;show-leak-kinds=definite,indirect,possible,reachable</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>none</code> for the empty set.</dl>
</dl>
<p> <code>&#8211;errors-for-leak-kinds=&lt;set&gt; [default: definite,possible] </code></p>
<dl>
<dt>
<dd> Specifies the leak kinds to count as errors in a <i>full</i> leak search. The <code>&lt;set&gt;</code> is specified similarly to <code>&#8211;show-leak-kinds</code></dl>
<p> <code>&#8211;leak-check-heuristics=&lt;set&gt; [default: all] </code></p>
<dl>
<dt>
<dd> Specifies the set of leak check heuristics to be used during leak searches. The heuristics control which interior pointers to a block cause it to be considered as reachable. The heuristic set is specified in one of the following ways: </p>
<dl>
<dt>
<dd> &bull; a comma separated list of one or more of <code>stdstring length64 newarray multipleinheritance</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>all</code> to activate the complete set of heuristics. It is equivalent to <code>&#8211;leak-check-heuristics=stdstring,length64,newarray,multipleinheritance</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>none</code> for the empty set.</dl>
<p> Note that these heuristics are dependent on the layout of the objects produced by the C++ compiler. They have been tested with some gcc versions (e.g. 4.4 and 4.7). They might not work properly with other C++ compilers.</dl>
<p> <code>&#8211;show-reachable=&lt;yes|no&gt; </code>, <code>&#8211;show-possibly-lost=&lt;yes|no&gt; </code></p>
<dl>
<dt>
<dd> These options provide an alternative way to specify the leak kinds to show: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;show-reachable=no &#8211;show-possibly-lost=yes</code> is equivalent to <code>&#8211;show-leak-kinds=definite,possible</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;show-reachable=no &#8211;show-possibly-lost=no</code> is equivalent to <code>&#8211;show-leak-kinds=definite</code>.</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;show-reachable=yes</code> is equivalent to <code>&#8211;show-leak-kinds=all</code>.</dl>
<p> Note that <code>&#8211;show-possibly-lost=no</code> has no effect if <code>&#8211;show-reachable=yes</code> is specified.</dl>
<p> <code>&#8211;xtree-leak=&lt;no|yes&gt; [no] </code></p>
<dl>
<dt>
<dd> If set to yes, the results for the leak search done at exit will be output in a &#8216;Callgrind Format&#8217; execution tree file. Note that this automatically sets the options <code>&#8211;leak-check=full</code> and <code>&#8211;show-leak-kinds=all</code>, to allow xtree visualisation tools such as kcachegrind to select what kind to leak to visualise. The produced file will contain the following events: </p>
<dl>
<dt>
<dd> &bull; <code>RB</code> : Reachable Bytes</dl>
<dl>
<dt>
<dd> &bull; <code>PB</code> : Possibly lost Bytes</dl>
<dl>
<dt>
<dd> &bull; <code>IB</code> : Indirectly lost Bytes</dl>
<dl>
<dt>
<dd> &bull; <code>DB</code> : Definitely lost Bytes (direct plus indirect)</dl>
<dl>
<dt>
<dd> &bull; <code>DIB</code> : Definitely Indirectly lost Bytes (subset of DB)</dl>
<dl>
<dt>
<dd> &bull; <code>RBk</code> : reachable Blocks</dl>
<dl>
<dt>
<dd> &bull; <code>PBk</code> : Possibly lost Blocks</dl>
<dl>
<dt>
<dd> &bull; <code>IBk</code> : Indirectly lost Blocks</dl>
<dl>
<dt>
<dd> &bull; <code>DBk</code> : Definitely lost Blocks</dl>
<p> The increase or decrease for all events above will also be output in the file to provide the delta (increase or decrease) between 2 successive leak searches. For example, <code>iRB</code> is the increase of the <code>RB</code> event, <code>dPBk</code> is the decrease of <code>PBk</code> event. The values for the increase and decrease events will be zero for the first leak search done. </p>
<p> See ??? for a detailed explanation about execution trees.</dl>
<p> <code>&#8211;xtree-leak-file=&lt;filename&gt; [default: xtleak.kcg.%p] </code></p>
<dl>
<dt>
<dd> Specifies that Valgrind should produce the xtree leak report in the specified file. Any <code>%p</code>, <code>%q</code> or <code>%n</code> sequences appearing in the filename are expanded in exactly the same way as they are for <code>&#8211;log-file</code>. See the description of &#8211;log-file for details. </p>
<p> See ??? for a detailed explanation about execution trees formats.</dl>
<p> <code>&#8211;undef-value-errors=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> Controls whether Memcheck reports uses of undefined value errors. Set this to <i>no</i> if you don&#8217;t want to see undefined value errors. It also has the side effect of speeding up Memcheck somewhat. AddrCheck (removed in Valgrind 3.1.0) functioned like Memcheck with <code>&#8211;undef-value-errors=no</code>.</dl>
<p> <code>&#8211;track-origins=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> Controls whether Memcheck tracks the origin of uninitialised values. By default, it does not, which means that although it can tell you that an uninitialised value is being used in a dangerous way, it cannot tell you where the uninitialised value came from. This often makes it difficult to track down the root problem. </p>
<p> When set to <i>yes</i>, Memcheck keeps track of the origins of all uninitialised values. Then, when an uninitialised value error is reported, Memcheck will try to show the origin of the value. An origin can be one of the following four places: a heap block, a stack allocation, a client request, or miscellaneous other sources (eg, a call to <i>brk</i>). </p>
<p> For uninitialised values originating from a heap block, Memcheck shows where the block was allocated. For uninitialised values originating from a stack allocation, Memcheck can tell you which function allocated the value, but no more than that &#8212; typically it shows you the source location of the opening brace of the function. So you should carefully check that all of the function&#8217;s local variables are initialised properly. </p>
<p> Performance overhead: origin tracking is expensive. It halves Memcheck&#8217;s speed and increases memory use by a minimum of 100MB, and possibly more. Nevertheless it can drastically reduce the effort required to identify the root cause of uninitialised value errors, and so is often a programmer productivity win, despite running more slowly. </p>
<p> Accuracy: Memcheck tracks origins quite accurately. To avoid very large space and time overheads, some approximations are made. It is possible, although unlikely, that Memcheck will report an incorrect origin, or not be able to identify any origin. </p>
<p> Note that the combination <code>&#8211;track-origins=yes</code> and <code>&#8211;undef-value-errors=no</code> is nonsensical. Memcheck checks for and rejects this combination at startup.</dl>
<p> <code>&#8211;partial-loads-ok=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> Controls how Memcheck handles 32-, 64-, 128- and 256-bit naturally aligned loads from addresses for which some bytes are addressable and others are not. When <i>yes</i>, such loads do not produce an address error. Instead, loaded bytes originating from illegal addresses are marked as uninitialised, and those corresponding to legal addresses are handled in the normal way. </p>
<p> When <i>no</i>, loads from partially invalid addresses are treated the same as loads from completely invalid addresses: an illegal-address error is issued, and the resulting bytes are marked as initialised. </p>
<p> Note that code that behaves in this way is in violation of the ISO C/C++ standards, and should be considered broken. If at all possible, such code should be fixed.</dl>
<p> <code>&#8211;expensive-definedness-checks=&lt;no|auto|yes&gt; [default: auto] </code></p>
<dl>
<dt>
<dd> Controls whether Memcheck should employ more precise but also more expensive (time consuming) instrumentation when checking the definedness of certain values. In particular, this affects the instrumentation of integer adds, subtracts and equality comparisons. </p>
<p> Selecting <code>&#8211;expensive-definedness-checks=yes</code> causes Memcheck to use the most accurate analysis possible. This minimises false error rates but can cause up to 30% performance degradation. </p>
<p> Selecting <code>&#8211;expensive-definedness-checks=no</code> causes Memcheck to use the cheapest instrumentation possible. This maximises performance but will normally give an unusably high false error rate. </p>
<p> The default setting, <code>&#8211;expensive-definedness-checks=auto</code>, is strongly recommended. This causes Memcheck to use the minimum of expensive instrumentation needed to achieve the same false error rate as <code>&#8211;expensive-definedness-checks=yes</code>. It also enables an instrumentation-time analysis pass which aims to further reduce the costs of accurate instrumentation. Overall, the performance loss is generally around 5% relative to <code>&#8211;expensive-definedness-checks=no</code>, although this is strongly workload dependent. Note that the exact instrumentation settings in this mode are architecture dependent.</dl>
<p> <code>&#8211;keep-stacktraces=alloc|free|alloc-and-free|alloc-then-free|none [default: alloc-and-free] </code></p>
<dl>
<dt>
<dd> Controls which stack trace(s) to keep for malloc&#8217;d and/or free&#8217;d blocks. </p>
<p> With <i>alloc-then-free</i>, a stack trace is recorded at allocation time, and is associated with the block. When the block is freed, a second stack trace is recorded, and this replaces the allocation stack trace. As a result, any &quot;use after free&quot; errors relating to this block can only show a stack trace for where the block was freed. </p>
<p> With <i>alloc-and-free</i>, both allocation and the deallocation stack traces for the block are stored. Hence a &quot;use after free&quot; error will show both, which may make the error easier to diagnose. Compared to <i>alloc-then-free</i>, this setting slightly increases Valgrind&#8217;s memory use as the block contains two references instead of one. </p>
<p> With <i>alloc</i>, only the allocation stack trace is recorded (and reported). With <i>free</i>, only the deallocation stack trace is recorded (and reported). These values somewhat decrease Valgrind&#8217;s memory and cpu usage. They can be useful depending on the error types you are searching for and the level of detail you need to analyse them. For example, if you are only interested in memory leak errors, it is sufficient to record the allocation stack traces. </p>
<p> With <i>none</i>, no stack traces are recorded for malloc and free operations. If your program allocates a lot of blocks and/or allocates/frees from many different stack traces, this can significantly decrease cpu and/or memory required. Of course, few details will be reported for errors related to heap blocks. </p>
<p> Note that once a stack trace is recorded, Valgrind keeps the stack trace in memory even if it is not referenced by any block. Some programs (for example, recursive algorithms) can generate a huge number of stack traces. If Valgrind uses too much memory in such circumstances, you can reduce the memory required with the options <i>&#8211;keep-stacktraces</i> and/or by using a smaller value for the option <i>&#8211;num-callers</i>. </p>
<p> If you want to use &#8211;xtree-memory=full memory profiling (see ??? ), then you cannot specify <i>&#8211;keep-stacktraces=free</i> or <i>&#8211;keep-stacktraces=none</i>.</dl>
<p> <code>&#8211;freelist-vol=&lt;number&gt; [default: 20000000] </code></p>
<dl>
<dt>
<dd> When the client program releases memory using <code>free</code> (in C) or delete (C++), that memory is not immediately made available for re-allocation. Instead, it is marked inaccessible and placed in a queue of freed blocks. The purpose is to defer as long as possible the point at which freed-up memory comes back into circulation. This increases the chance that Memcheck will be able to detect invalid accesses to blocks for some significant period of time after they have been freed. </p>
<p> This option specifies the maximum total size, in bytes, of the blocks in the queue. The default value is twenty million bytes. Increasing this increases the total amount of memory used by Memcheck but may detect invalid uses of freed blocks which would otherwise go undetected.</dl>
<p> <code>&#8211;freelist-big-blocks=&lt;number&gt; [default: 1000000] </code></p>
<dl>
<dt>
<dd> When making blocks from the queue of freed blocks available for re-allocation, Memcheck will in priority re-circulate the blocks with a size greater or equal to <code>&#8211;freelist-big-blocks</code>. This ensures that freeing big blocks (in particular freeing blocks bigger than <code>&#8211;freelist-vol</code>) does not immediately lead to a re-circulation of all (or a lot of) the small blocks in the free list. In other words, this option increases the likelihood to discover dangling pointers for the &quot;small&quot; blocks, even when big blocks are freed. </p>
<p> Setting a value of 0 means that all the blocks are re-circulated in a FIFO order.</dl>
<p> <code>&#8211;workaround-gcc296-bugs=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, assume that reads and writes some small distance below the stack pointer are due to bugs in GCC 2.96, and does not report them. The &quot;small distance&quot; is 256 bytes by default. Note that GCC 2.96 is the default compiler on some ancient Linux distributions (RedHat 7.X) and so you may need to use this option. Do not use it if you do not have to, as it can cause real errors to be overlooked. A better alternative is to use a more recent GCC in which this bug is fixed. </p>
<p> You may also need to use this option when working with GCC 3.X or 4.X on 32-bit PowerPC Linux. This is because GCC generates code which occasionally accesses below the stack pointer, particularly for floating-point to/from integer conversions. This is in violation of the 32-bit PowerPC ELF specification, which makes no provision for locations below the stack pointer to be accessible. </p>
<p> This option is deprecated as of version 3.12 and may be removed from future versions. You should instead use <code>&#8211;ignore-range-below-sp</code> to specify the exact range of offsets below the stack pointer that should be ignored. A suitable equivalent is <code>&#8211;ignore-range-below-sp=1024-1</code>.</dl>
<p> <code>&#8211;ignore-range-below-sp=&lt;number&gt;-&lt;number&gt; </code></p>
<dl>
<dt>
<dd> This is a more general replacement for the deprecated <code>&#8211;workaround-gcc296-bugs</code> option. When specified, it causes Memcheck not to report errors for accesses at the specified offsets below the stack pointer. The two offsets must be positive decimal numbers and &#8212; somewhat counterintuitively &#8212; the first one must be larger, in order to imply a non-wraparound address range to ignore. For example, to ignore 4 byte accesses at 8192 bytes below the stack pointer, use <code>&#8211;ignore-range-below-sp=8192-8189</code>. Only one range may be specified.</dl>
<p> <code>&#8211;show-mismatched-frees=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> When enabled, Memcheck checks that heap blocks are deallocated using a function that matches the allocating function. That is, it expects <i>free</i> to be used to deallocate blocks allocated by <i>malloc</i>, <i>delete</i> for blocks allocated by <i>new</i>, and <i>delete[]</i> for blocks allocated by <i>new[]</i>. If a mismatch is detected, an error is reported. This is in general important because in some environments, freeing with a non-matching function can cause crashes. </p>
<p> There is however a scenario where such mismatches cannot be avoided. That is when the user provides implementations of <i>new</i>/<i>new[]</i> that call <i>malloc</i> and of <i>delete</i>/<i>delete[]</i> that call <i>free</i>, and these functions are asymmetrically inlined. For example, imagine that <i>delete[]</i> is inlined but <i>new[]</i> is not. The result is that Memcheck &quot;sees&quot; all <i>delete[]</i> calls as direct calls to <i>free</i>, even when the program source contains no mismatched calls. </p>
<p> This causes a lot of confusing and irrelevant error reports. <i>&#8211;show-mismatched-frees=no</i> disables these checks. It is not generally advisable to disable them, though, because you may miss real errors as a result.</dl>
<p> <code>&#8211;ignore-ranges=0xPP-0xQQ[,0xRR-0xSS] </code></p>
<dl>
<dt>
<dd> Any ranges listed in this option (and multiple ranges can be specified, separated by commas) will be ignored by Memcheck&#8217;s addressability checking.</dl>
<p> <code>&#8211;malloc-fill=&lt;hexnumber&gt; </code></p>
<dl>
<dt>
<dd> Fills blocks allocated by malloc, new, etc, but not by calloc, with the specified byte. This can be useful when trying to shake out obscure memory corruption problems. The allocated area is still regarded by Memcheck as undefined &#8212; this option only affects its contents. Note that <code>&#8211;malloc-fill</code> does not affect a block of memory when it is used as argument to client requests VALGRIND_MEMPOOL_ALLOC or VALGRIND_MALLOCLIKE_BLOCK.</dl>
<p> <code>&#8211;free-fill=&lt;hexnumber&gt; </code></p>
<dl>
<dt>
<dd> Fills blocks freed by free, delete, etc, with the specified byte value. This can be useful when trying to shake out obscure memory corruption problems. The freed area is still regarded by Memcheck as not valid for access &#8212; this option only affects its contents. Note that <code>&#8211;free-fill</code> does not affect a block of memory when it is used as argument to client requests VALGRIND_MEMPOOL_FREE or VALGRIND_FREELIKE_BLOCK.</dl>
<h2>CACHEGRIND OPTIONS</h2>
<p> <code>&#8211;I1=&lt;size&gt;,&lt;associativity&gt;,&lt;line size&gt; </code></p>
<dl>
<dt>
<dd> Specify the size, associativity and line size of the level 1 instruction cache.</dl>
<p> <code>&#8211;D1=&lt;size&gt;,&lt;associativity&gt;,&lt;line size&gt; </code></p>
<dl>
<dt>
<dd> Specify the size, associativity and line size of the level 1 data cache.</dl>
<p> <code>&#8211;LL=&lt;size&gt;,&lt;associativity&gt;,&lt;line size&gt; </code></p>
<dl>
<dt>
<dd> Specify the size, associativity and line size of the last-level cache.</dl>
<p> <code>&#8211;cache-sim=no|yes [yes] </code></p>
<dl>
<dt>
<dd> Enables or disables collection of cache access and miss counts.</dl>
<p> <code>&#8211;branch-sim=no|yes [no] </code></p>
<dl>
<dt>
<dd> Enables or disables collection of branch instruction and misprediction counts. By default this is disabled as it slows Cachegrind down by approximately 25%. Note that you cannot specify <code>&#8211;cache-sim=no</code> and <code>&#8211;branch-sim=no</code> together, as that would leave Cachegrind with no information to collect.</dl>
<p> <code>&#8211;cachegrind-out-file=&lt;file&gt; </code></p>
<dl>
<dt>
<dd> Write the profile data to file rather than to the default output file, cachegrind.out.&lt;pid&gt;. The <code>%p</code> and <code>%q</code> format specifiers can be used to embed the process ID and/or the contents of an environment variable in the name, as is the case for the core option <code>&#8211;log-file</code>.</dl>
<h2>CALLGRIND OPTIONS</h2>
<p> <code>&#8211;callgrind-out-file=&lt;file&gt; </code></p>
<dl>
<dt>
<dd> Write the profile data to file rather than to the default output file, callgrind.out.&lt;pid&gt;. The <code>%p</code> and <code>%q</code> format specifiers can be used to embed the process ID and/or the contents of an environment variable in the name, as is the case for the core option <code>&#8211;log-file</code>. When multiple dumps are made, the file name is modified further; see below.</dl>
<p> <code>&#8211;dump-line=&lt;no|yes&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> This specifies that event counting should be performed at source line granularity. This allows source annotation for sources which are compiled with debug information (<code>-g</code>).</dl>
<p> <code>&#8211;dump-instr=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
<dd> This specifies that event counting should be performed at per-instruction granularity. This allows for assembly code annotation. Currently the results can only be displayed by KCachegrind.</dl>
<p> <code>&#8211;compress-strings=&lt;no|yes&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> This option influences the output format of the profile data. It specifies whether strings (file and function names) should be identified by numbers. This shrinks the file, but makes it more difficult for humans to read (which is not recommended in any case).</dl>
<p> <code>&#8211;compress-pos=&lt;no|yes&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> This option influences the output format of the profile data. It specifies whether numerical positions are always specified as absolute values or are allowed to be relative to previous numbers. This shrinks the file size.</dl>
<p> <code>&#8211;combine-dumps=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, when multiple profile data parts are to be generated these parts are appended to the same output file. Not recommended.</dl>
<p> <code>&#8211;dump-every-bb=&lt;count&gt; [default: 0, never] </code></p>
<dl>
<dt>
<dd> Dump profile data every <code>count</code> basic blocks. Whether a dump is needed is only checked when Valgrind&#8217;s internal scheduler is run. Therefore, the minimum setting useful is about 100000. The count is a 64-bit value to make long dump periods possible.</dl>
<p> <code>&#8211;dump-before=&lt;function&gt; </code></p>
<dl>
<dt>
<dd> Dump when entering <code>function</code>.</dl>
<p> <code>&#8211;zero-before=&lt;function&gt; </code></p>
<dl>
<dt>
<dd> Zero all costs when entering <code>function</code>.</dl>
<p> <code>&#8211;dump-after=&lt;function&gt; </code></p>
<dl>
<dt>
<dd> Dump when leaving <code>function</code>.</dl>
<p> <code>&#8211;instr-atstart=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> Specify if you want Callgrind to start simulation and profiling from the beginning of the program. When set to no, Callgrind will not be able to collect any information, including calls, but it will have at most a slowdown of around 4, which is the minimum Valgrind overhead. Instrumentation can be interactively enabled via callgrind_control -i on. </p>
<p> Note that the resulting call graph will most probably not contain <code>main</code>, but will contain all the functions executed after instrumentation was enabled. Instrumentation can also be programmatically enabled/disabled. See the Callgrind include file callgrind.h for the macro you have to use in your source code. </p>
<p> For cache simulation, results will be less accurate when switching on instrumentation later in the program run, as the simulator starts with an empty cache at that moment. Switch on event collection later to cope with this error.</dl>
<p> <code>&#8211;collect-atstart=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> Specify whether event collection is enabled at beginning of the profile run. </p>
<p> To only look at parts of your program, you have two possibilities: </p>
<dl>
<dt>
<dd> 1. Zero event counters before entering the program part you want to profile, and dump the event counters to a file after leaving that program part.</dl>
<dl>
<dt>
<dd> 2. Switch on/off collection state as needed to only see event counters happening while inside of the program part you want to profile.</dl>
<p> The second option can be used if the program part you want to profile is called many times. Option 1, i.e. creating a lot of dumps is not practical here. </p>
<p> Collection state can be toggled at entry and exit of a given function with the option <code>&#8211;toggle-collect</code>. If you use this option, collection state should be disabled at the beginning. Note that the specification of <code>&#8211;toggle-collect</code> implicitly sets <code>&#8211;collect-state=no</code>. </p>
<p> Collection state can be toggled also by inserting the client request CALLGRIND_TOGGLE_COLLECT ; at the needed code positions.</dl>
<p> <code>&#8211;toggle-collect=&lt;function&gt; </code></p>
<dl>
<dt>
<dd> Toggle collection on entry/exit of <code>function</code>.</dl>
<p> <code>&#8211;collect-jumps=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
<dd> This specifies whether information for (conditional) jumps should be collected. As above, callgrind_annotate currently is not able to show you the data. You have to use KCachegrind to get jump arrows in the annotated code.</dl>
<p> <code>&#8211;collect-systime=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
<dd> This specifies whether information for system call times should be collected.</dl>
<p> <code>&#8211;collect-bus=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
<dd> This specifies whether the number of global bus events executed should be collected. The event type &quot;Ge&quot; is used for these events.</dl>
<p> <code>&#8211;cache-sim=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> Specify if you want to do full cache simulation. By default, only instruction read accesses will be counted (&quot;Ir&quot;). With cache simulation, further event counters are enabled: Cache misses on instruction reads (&quot;I1mr&quot;/&quot;ILmr&quot;), data read accesses (&quot;Dr&quot;) and related cache misses (&quot;D1mr&quot;/&quot;DLmr&quot;), data write accesses (&quot;Dw&quot;) and related cache misses (&quot;D1mw&quot;/&quot;DLmw&quot;). For more information, see Cachegrind: a cache and branch-prediction profiler.</dl>
<p> <code>&#8211;branch-sim=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> Specify if you want to do branch prediction simulation. Further event counters are enabled: Number of executed conditional branches and related predictor misses (&quot;Bc&quot;/&quot;Bcm&quot;), executed indirect jumps and related misses of the jump address predictor (&quot;Bi&quot;/&quot;Bim&quot;).</dl>
<h2>HELGRIND OPTIONS</h2>
<p> <code>&#8211;free-is-write=no|yes [default: no] </code></p>
<dl>
<dt>
<dd> When enabled (not the default), Helgrind treats freeing of heap memory as if the memory was written immediately before the free. This exposes races where memory is referenced by one thread, and freed by another, but there is no observable synchronisation event to ensure that the reference happens before the free. </p>
<p> This functionality is new in Valgrind 3.7.0, and is regarded as experimental. It is not enabled by default because its interaction with custom memory allocators is not well understood at present. User feedback is welcomed.</dl>
<p> <code>&#8211;track-lockorders=no|yes [default: yes] </code></p>
<dl>
<dt>
<dd> When enabled (the default), Helgrind performs lock order consistency checking. For some buggy programs, the large number of lock order errors reported can become annoying, particularly if you&#8217;re only interested in race errors. You may therefore find it helpful to disable lock order checking.</dl>
<p> <code>&#8211;history-level=none|approx|full [default: full] </code></p>
<dl>
<dt>
<dd> <code>&#8211;history-level=full</code> (the default) causes Helgrind collects enough information about &quot;old&quot; accesses that it can produce two stack traces in a race report &#8212; both the stack trace for the current access, and the trace for the older, conflicting access. To limit memory usage, &quot;old&quot; accesses stack traces are limited to a maximum of 8 entries, even if <code>&#8211;num-callers</code> value is bigger. </p>
<p> Collecting such information is expensive in both speed and memory, particularly for programs that do many inter-thread synchronisation events (locks, unlocks, etc). Without such information, it is more difficult to track down the root causes of races. Nonetheless, you may not need it in situations where you just want to check for the presence or absence of races, for example, when doing regression testing of a previously race-free program. </p>
<p> <code>&#8211;history-level=none</code> is the opposite extreme. It causes Helgrind not to collect any information about previous accesses. This can be dramatically faster than <code>&#8211;history-level=full</code>. </p>
<p> <code>&#8211;history-level=approx</code> provides a compromise between these two extremes. It causes Helgrind to show a full trace for the later access, and approximate information regarding the earlier access. This approximate information consists of two stacks, and the earlier access is guaranteed to have occurred somewhere between program points denoted by the two stacks. This is not as useful as showing the exact stack for the previous access (as <code>&#8211;history-level=full</code> does), but it is better than nothing, and it is almost as fast as <code>&#8211;history-level=none</code>.</dl>
<p> <code>&#8211;delta-stacktrace=no|yes [default: yes on linux amd64/x86] </code></p>
<dl>
<dt>
<dd> This flag only has any effect at <code>&#8211;history-level=full</code>. </p>
<p> <code>&#8211;delta-stacktrace</code> configures the way Helgrind captures the stacktraces for the option <code>&#8211;history-level=full</code>. Such a stacktrace is typically needed each time a new piece of memory is read or written in a basic block of instructions. </p>
<p> <code>&#8211;delta-stacktrace=no</code> causes Helgrind to compute a full history stacktrace from the unwind info each time a stacktrace is needed. </p>
<p> <code>&#8211;delta-stacktrace=yes</code> indicates to Helgrind to derive a new stacktrace from the previous stacktrace, as long as there was no call instruction, no return instruction, or any other instruction changing the call stack since the previous stacktrace was captured. If no such instruction was executed, the new stacktrace can be derived from the previous stacktrace by just changing the top frame to the current program counter. This option can speed up Helgrind by 25% when using <code>&#8211;history-level=full</code>. </p>
<p> The following aspects have to be considered when using <code>&#8211;delta-stacktrace=yes</code> : </p>
<dl>
<dt>
<dd> &bull; In some cases (for example in a function prologue), the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;valgrind unwinder might not properly unwind the stack, due to some<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;limitations and/or due to wrong unwind info. When using<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;delta-stacktrace=yes, the wrong stack trace captured in the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function prologue will be kept till the next call or return.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.RE </p>
<dl>
<dt>
<dd> &bull; On the other hand, &#8211;delta-stacktrace=yes sometimes helps to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtain a correct stacktrace, for example when the unwind info allows<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a correct stacktrace to be done in the beginning of the sequence,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;but not later on in the instruction sequence..RE </p>
<dl>
<dt>
<dd> &bull; Determining which instructions are changing the callstack is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;partially based on platform dependent heuristics, which have to be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tuned/validated specifically for the platform. Also, unwinding in a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function prologue must be good enough to allow using<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;delta-stacktrace=yes. Currently, the option &#8211;delta-stacktrace=yes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;has been reasonably validated only on linux x86 32 bits and linux<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;amd64 64 bits. For more details about how to validate<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;delta-stacktrace=yes, see debug option &#8211;hg-sanity-flags and the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function check_cached_rcec_ok in libhb_core.c..RE </p>
</dl>
<p> <code>&#8211;conflict-cache-size=N [default: 1000000] </code></p>
<dl>
<dt>
<dd> This flag only has any effect at <code>&#8211;history-level=full</code>. </p>
<p> Information about &quot;old&quot; conflicting accesses is stored in a cache of limited size, with LRU-style management. This is necessary because it isn&#8217;t practical to store a stack trace for every single memory access made by the program. Historical information on not recently accessed locations is periodically discarded, to free up space in the cache. </p>
<p> This option controls the size of the cache, in terms of the number of different memory addresses for which conflicting access information is stored. If you find that Helgrind is showing race errors with only one stack instead of the expected two stacks, try increasing this value. </p>
<p> The minimum value is 10,000 and the maximum is 30,000,000 (thirty times the default value). Increasing the value by 1 increases Helgrind&#8217;s memory requirement by very roughly 100 bytes, so the maximum value will easily eat up three extra gigabytes or so of memory.</dl>
<p> <code>&#8211;check-stack-refs=no|yes [default: yes] </code></p>
<dl>
<dt>
<dd> By default Helgrind checks all data memory accesses made by your program. This flag enables you to skip checking for accesses to thread stacks (local variables). This can improve performance, but comes at the cost of missing races on stack-allocated data.</dl>
<p> <code>&#8211;ignore-thread-creation=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Controls whether all activities during thread creation should be ignored. By default enabled only on Solaris. Solaris provides higher throughput, parallelism and scalability than other operating systems, at the cost of more fine-grained locking activity. This means for example that when a thread is created under glibc, just one big lock is used for all thread setup. Solaris libc uses several fine-grained locks and the creator thread resumes its activities as soon as possible, leaving for example stack and TLS setup sequence to the created thread. This situation confuses Helgrind as it assumes there is some false ordering in place between creator and created thread; and therefore many types of race conditions in the application would not be reported. To prevent such false ordering, this command line option is set to yes by default on Solaris. All activity (loads, stores, client requests) is therefore ignored during: </p>
<dl>
<dt>
<dd> &bull; pthread_create() call in the creator thread</dl>
<dl>
<dt>
<dd> &bull; thread creation phase (stack and TLS setup) in the created thread</dl>
<p> Also new memory allocated during thread creation is untracked, that is race reporting is suppressed there. DRD does the same thing implicitly. This is necessary because Solaris libc caches many objects and reuses them for different threads and that confuses Helgrind.</dl>
</dl>
</dl>
</dl>
<h2>DRD OPTIONS</h2>
<p> <code>&#8211;check-stack-var=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Controls whether DRD detects data races on stack variables. Verifying stack variables is disabled by default because most programs do not share stack variables over threads.</dl>
<p> <code>&#8211;exclusive-threshold=&lt;n&gt; [default: off]</code></p>
<dl>
<dt>
<dd> Print an error message if any mutex or writer lock has been held longer than the time specified in milliseconds. This option enables the detection of lock contention.</dl>
<p> <code>&#8211;join-list-vol=&lt;n&gt; [default: 10]</code></p>
<dl>
<dt>
<dd> Data races that occur between a statement at the end of one thread and another thread can be missed if memory access information is discarded immediately after a thread has been joined. This option allows one to specify for how many joined threads memory access information should be retained.</dl>
<p> <code> &#8211;first-race-only=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> Whether to report only the first data race that has been detected on a memory location or all data races that have been detected on a memory location.</dl>
<p> <code> &#8211;free-is-write=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> Whether to report races between accessing memory and freeing memory. Enabling this option may cause DRD to run slightly slower. Notes: </p>
<dl>
<dt>
<dd> &bull; Don&#8217;t enable this option when using custom memory allocators that use the VG_USERREQ__MALLOCLIKE_BLOCK and VG_USERREQ__FREELIKE_BLOCK because that would result in false positives.</dl>
<dl>
<dt>
<dd> &bull; Don&#8217;t enable this option when using reference-counted objects because that will result in false positives, even when that code has been annotated properly with ANNOTATE_HAPPENS_BEFORE and ANNOTATE_HAPPENS_AFTER. See e.g. the output of the following command for an example: valgrind &#8211;tool=drd &#8211;free-is-write=yes drd/tests/annotate_smart_pointer.</dl>
</dl>
<p> <code> &#8211;report-signal-unlocked=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> Whether to report calls to <code>pthread_cond_signal</code> and <code>pthread_cond_broadcast</code> where the mutex associated with the signal through <code>pthread_cond_wait</code> or <code>pthread_cond_timed_wait</code>is not locked at the time the signal is sent. Sending a signal without holding a lock on the associated mutex is a common programming error which can cause subtle race conditions and unpredictable behavior. There exist some uncommon synchronization patterns however where it is safe to send a signal without holding a lock on the associated mutex.</dl>
<p> <code>&#8211;segment-merging=&lt;yes|no&gt; [default: yes]</code></p>
<dl>
<dt>
<dd> Controls segment merging. Segment merging is an algorithm to limit memory usage of the data race detection algorithm. Disabling segment merging may improve the accuracy of the so-called &#8216;other segments&#8217; displayed in race reports but can also trigger an out of memory error.</dl>
<p> <code>&#8211;segment-merging-interval=&lt;n&gt; [default: 10]</code></p>
<dl>
<dt>
<dd> Perform segment merging only after the specified number of new segments have been created. This is an advanced configuration option that allows one to choose whether to minimize DRD&#8217;s memory usage by choosing a low value or to let DRD run faster by choosing a slightly higher value. The optimal value for this parameter depends on the program being analyzed. The default value works well for most programs.</dl>
<p> <code>&#8211;shared-threshold=&lt;n&gt; [default: off]</code></p>
<dl>
<dt>
<dd> Print an error message if a reader lock has been held longer than the specified time (in milliseconds). This option enables the detection of lock contention.</dl>
<p> <code>&#8211;show-confl-seg=&lt;yes|no&gt; [default: yes]</code></p>
<dl>
<dt>
<dd> Show conflicting segments in race reports. Since this information can help to find the cause of a data race, this option is enabled by default. Disabling this option makes the output of DRD more compact.</dl>
<p> <code>&#8211;show-stack-usage=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Print stack usage at thread exit time. When a program creates a large number of threads it becomes important to limit the amount of virtual memory allocated for thread stacks. This option makes it possible to observe how much stack memory has been used by each thread of the client program. Note: the DRD tool itself allocates some temporary data on the client thread stack. The space necessary for this temporary data must be allocated by the client program when it allocates stack memory, but is not included in stack usage reported by DRD.</dl>
<p> <code>&#8211;ignore-thread-creation=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Controls whether all activities during thread creation should be ignored. By default enabled only on Solaris. Solaris provides higher throughput, parallelism and scalability than other operating systems, at the cost of more fine-grained locking activity. This means for example that when a thread is created under glibc, just one big lock is used for all thread setup. Solaris libc uses several fine-grained locks and the creator thread resumes its activities as soon as possible, leaving for example stack and TLS setup sequence to the created thread. This situation confuses DRD as it assumes there is some false ordering in place between creator and created thread; and therefore many types of race conditions in the application would not be reported. To prevent such false ordering, this command line option is set to yes by default on Solaris. All activity (loads, stores, client requests) is therefore ignored during: </p>
<dl>
<dt>
<dd> &bull; pthread_create() call in the creator thread</dl>
<dl>
<dt>
<dd> &bull; thread creation phase (stack and TLS setup) in the created thread</dl>
</dl>
<p> <code>&#8211;trace-addr=&lt;address&gt; [default: none]</code></p>
<dl>
<dt>
<dd> Trace all load and store activity for the specified address. This option may be specified more than once.</dl>
<p> <code>&#8211;ptrace-addr=&lt;address&gt; [default: none]</code></p>
<dl>
<dt>
<dd> Trace all load and store activity for the specified address and keep doing that even after the memory at that address has been freed and reallocated.</dl>
<p> <code>&#8211;trace-alloc=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Trace all memory allocations and deallocations. May produce a huge amount of output.</dl>
<p> <code>&#8211;trace-barrier=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Trace all barrier activity.</dl>
<p> <code>&#8211;trace-cond=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Trace all condition variable activity.</dl>
<p> <code>&#8211;trace-fork-join=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Trace all thread creation and all thread termination events.</dl>
<p> <code>&#8211;trace-hb=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Trace execution of the ANNOTATE_HAPPENS_BEFORE(), ANNOTATE_HAPPENS_AFTER() and ANNOTATE_HAPPENS_DONE() client requests.</dl>
<p> <code>&#8211;trace-mutex=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Trace all mutex activity.</dl>
<p> <code>&#8211;trace-rwlock=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Trace all reader-writer lock activity.</dl>
<p> <code>&#8211;trace-semaphore=&lt;yes|no&gt; [default: no]</code></p>
<dl>
<dt>
<dd> Trace all semaphore activity.</dl>
<h2>MASSIF OPTIONS</h2>
<p> <code>&#8211;heap=&lt;yes|no&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> Specifies whether heap profiling should be done.</dl>
<p> <code>&#8211;heap-admin=&lt;size&gt; [default: 8] </code></p>
<dl>
<dt>
<dd> If heap profiling is enabled, gives the number of administrative bytes per block to use. This should be an estimate of the average, since it may vary. For example, the allocator used by glibc on Linux requires somewhere between 4 to 15 bytes per block, depending on various factors. That allocator also requires admin space for freed blocks, but Massif cannot account for this.</dl>
<p> <code>&#8211;stacks=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> Specifies whether stack profiling should be done. This option slows Massif down greatly, and so is off by default. Note that Massif assumes that the main stack has size zero at start-up. This is not true, but doing otherwise accurately is difficult. Furthermore, starting at zero better indicates the size of the part of the main stack that a user program actually has control over.</dl>
<p> <code>&#8211;pages-as-heap=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
<dd> Tells Massif to profile memory at the page level rather than at the malloc&#8217;d block level. See above for details.</dl>
<p> <code>&#8211;depth=&lt;number&gt; [default: 30] </code></p>
<dl>
<dt>
<dd> Maximum depth of the allocation trees recorded for detailed snapshots. Increasing it will make Massif run somewhat more slowly, use more memory, and produce bigger output files.</dl>
<p> <code>&#8211;alloc-fn=&lt;name&gt; </code></p>
<dl>
<dt>
<dd> Functions specified with this option will be treated as though they were a heap allocation function such as <code>malloc</code>. This is useful for functions that are wrappers to <code>malloc</code> or <code>new</code>, which can fill up the allocation trees with uninteresting information. This option can be specified multiple times on the command line, to name multiple functions. </p>
<p> Note that the named function will only be treated this way if it is the top entry in a stack trace, or just below another function treated this way. For example, if you have a function <code>malloc1</code> that wraps <code>malloc</code>, and <code>malloc2</code> that wraps <code>malloc1</code>, just specifying <code>&#8211;alloc-fn=malloc2</code> will have no effect. You need to specify <code>&#8211;alloc-fn=malloc1</code> as well. This is a little inconvenient, but the reason is that checking for allocation functions is slow, and it saves a lot of time if Massif can stop looking through the stack trace entries as soon as it finds one that doesn&#8217;t match rather than having to continue through all the entries. </p>
<p> Note that C++ names are demangled. Note also that overloaded C++ names must be written in full. Single quotes may be necessary to prevent the shell from breaking them up. For example: </p>
<dl>
<dt>
<dd>
<pre>
--alloc-fn='operator new(unsigned, std::nothrow_t const&amp;)'
</pre>
</dl>
</dl>
<p> <code>&#8211;ignore-fn=&lt;name&gt; </code></p>
<dl>
<dt>
<dd> Any direct heap allocation (i.e. a call to <code>malloc</code>, <code>new</code>, etc, or a call to a function named by an <code>&#8211;alloc-fn</code> option) that occurs in a function specified by this option will be ignored. This is mostly useful for testing purposes. This option can be specified multiple times on the command line, to name multiple functions. </p>
<p> Any <code>realloc</code> of an ignored block will also be ignored, even if the <code>realloc</code> call does not occur in an ignored function. This avoids the possibility of negative heap sizes if ignored blocks are shrunk with <code>realloc</code>. </p>
<p> The rules for writing C++ function names are the same as for <code>&#8211;alloc-fn</code> above.</dl>
<p> <code>&#8211;threshold=&lt;m.n&gt; [default: 1.0] </code></p>
<dl>
<dt>
<dd> The significance threshold for heap allocations, as a percentage of total memory size. Allocation tree entries that account for less than this will be aggregated. Note that this should be specified in tandem with ms_print&#8217;s option of the same name.</dl>
<p> <code>&#8211;peak-inaccuracy=&lt;m.n&gt; [default: 1.0] </code></p>
<dl>
<dt>
<dd> Massif does not necessarily record the actual global memory allocation peak; by default it records a peak only when the global memory allocation size exceeds the previous peak by at least 1.0%. This is because there can be many local allocation peaks along the way, and doing a detailed snapshot for every one would be expensive and wasteful, as all but one of them will be later discarded. This inaccuracy can be changed (even to 0.0%) via this option, but Massif will run drastically slower as the number approaches zero.</dl>
<p> <code>&#8211;time-unit=&lt;i|ms|B&gt; [default: i] </code></p>
<dl>
<dt>
<dd> The time unit used for the profiling. There are three possibilities: instructions executed (i), which is good for most cases; real (wallclock) time (ms, i.e. milliseconds), which is sometimes useful; and bytes allocated/deallocated on the heap and/or stack (B), which is useful for very short-run programs, and for testing purposes, because it is the most reproducible across different machines.</dl>
<p> <code>&#8211;detailed-freq=&lt;n&gt; [default: 10] </code></p>
<dl>
<dt>
<dd> Frequency of detailed snapshots. With <code>&#8211;detailed-freq=1</code>, every snapshot is detailed.</dl>
<p> <code>&#8211;max-snapshots=&lt;n&gt; [default: 100] </code></p>
<dl>
<dt>
<dd> The maximum number of snapshots recorded. If set to N, for all programs except very short-running ones, the final number of snapshots will be between N/2 and N.</dl>
<p> <code>&#8211;massif-out-file=&lt;file&gt; [default: massif.out.%p] </code></p>
<dl>
<dt>
<dd> Write the profile data to file rather than to the default output file, massif.out.&lt;pid&gt;. The <code>%p</code> and <code>%q</code> format specifiers can be used to embed the process ID and/or the contents of an environment variable in the name, as is the case for the core option <code>&#8211;log-file</code>.</dl>
<h2>SGCHECK OPTIONS</h2>
<p> There are no SGCheck-specific command-line options at present.</p>
<h2>BBV OPTIONS</h2>
<p> <code>&#8211;bb-out-file=&lt;name&gt; [default: bb.out.%p] </code></p>
<dl>
<dt>
<dd> This option selects the name of the basic block vector file. The <code>%p</code> and <code>%q</code> format specifiers can be used to embed the process ID and/or the contents of an environment variable in the name, as is the case for the core option <code>&#8211;log-file</code>.</dl>
<p> <code>&#8211;pc-out-file=&lt;name&gt; [default: pc.out.%p] </code></p>
<dl>
<dt>
<dd> This option selects the name of the PC file. This file holds program counter addresses and function name info for the various basic blocks. This can be used in conjunction with the basic block vector file to fast-forward via function names instead of just instruction counts. The <code>%p</code> and <code>%q</code> format specifiers can be used to embed the process ID and/or the contents of an environment variable in the name, as is the case for the core option <code>&#8211;log-file</code>.</dl>
<p> <code>&#8211;interval-size=&lt;number&gt; [default: 100000000] </code></p>
<dl>
<dt>
<dd> This option selects the size of the interval to use. The default is 100 million instructions, which is a commonly used value. Other sizes can be used; smaller intervals can help programs with finer-grained phases. However smaller interval size can lead to accuracy issues due to warm-up effects (When fast-forwarding the various architectural features will be un-initialized, and it will take some number of instructions before they &quot;warm up&quot; to the state a full simulation would be at without the fast-forwarding. Large interval sizes tend to mitigate this.)</dl>
<p> <code>&#8211;instr-count-only [default: no] </code></p>
<dl>
<dt>
<dd> This option tells the tool to only display instruction count totals, and to not generate the actual basic block vector file. This is useful for debugging, and for gathering instruction count info without generating the large basic block vector files.</dl>
<h2>LACKEY OPTIONS</h2>
<p> <code>&#8211;basic-counts=&lt;no|yes&gt; [default: yes] </code></p>
<dl>
<dt>
<dd> When enabled, Lackey prints the following statistics and information about the execution of the client program: </p>
<dl>
<dt>
<dd> 1. The number of calls to the function specified by the <code>&#8211;fnname</code> option (the default is main). If the program has had its symbols stripped, the count will always be zero.</dl>
<dl>
<dt>
<dd> 2. The number of conditional branches encountered and the number and proportion of those taken.</dl>
<dl>
<dt>
<dd> 3. The number of superblocks entered and completed by the program. Note that due to optimisations done by the JIT, this is not at all an accurate value.</dl>
<dl>
<dt>
<dd> 4. The number of guest (x86, amd64, ppc, etc.) instructions and IR statements executed. IR is Valgrind&#8217;s RISC-like intermediate representation via which all instrumentation is done.</dl>
<dl>
<dt>
<dd> 5. Ratios between some of these counts.</dl>
<dl>
<dt>
<dd> 6. The exit code of the client program.</dl>
</dl>
<p> <code>&#8211;detailed-counts=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, Lackey prints a table containing counts of loads, stores and ALU operations, differentiated by their IR types. The IR types are identified by their IR name (&quot;I1&quot;, &quot;I8&quot;, &#8230; &quot;I128&quot;, &quot;F32&quot;, &quot;F64&quot;, and &quot;V128&quot;).</dl>
<p> <code>&#8211;trace-mem=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, Lackey prints the size and address of almost every memory access made by the program. See the comments at the top of the file lackey/lk_main.c for details about the output format, how it works, and inaccuracies in the address trace. Note that this option produces immense amounts of output.</dl>
<p> <code>&#8211;trace-superblocks=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, Lackey prints out the address of every superblock (a single entry, multiple exit, linear chunk of code) executed by the program. This is primarily of interest to Valgrind developers. See the comments at the top of the file lackey/lk_main.c for details about the output format. Note that this option produces large amounts of output.</dl>
<p> <code>&#8211;fnname=&lt;name&gt; [default: main] </code></p>
<dl>
<dt>
<dd> Changes the function for which calls are counted when <code>&#8211;basic-counts=yes</code> is specified.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-cg_annotate/">cg_annotate</a>(1), <a href="/docs/linux/man/1-callgrind_annotate/">callgrind_annotate</a>(1), <a href="/docs/linux/man/1-callgrind_control/">callgrind_control</a>(1), <a href="/docs/linux/man/1-ms_print/">ms_print</a>(1), $INSTALL/share/doc/valgrind/html/index.html or <a rel="nofollow" href="http://www.valgrind.org/docs/manual/index.html,">http://www.valgrind.org/docs/manual/index.html,</a> m[blue]<code>Debugging your program using Valgrind&#8217;s gdbserver and GDB</code>m[]<font SIZE="-2">[1]</font> m[blue]<code>vgdb</code>m[]<font SIZE="-2">[2]</font>, m[blue]<code>Valgrind monitor commands</code>m[]<font SIZE="-2">[3]</font>, m[blue]<code>The Commentary</code>m[]<font SIZE="-2">[4]</font>, m[blue]<code>Scheduling and Multi-Thread Performance</code>m[]<font SIZE="-2">[5]</font>, m[blue]<code>Cachegrind: a cache and branch-prediction profiler</code>m[]<font SIZE="-2">[6]</font>.</p>
<h2>AUTHOR</h2>
<p> See the AUTHORS file in the valgrind distribution for a comprehensive list of authors. </p>
<p> This manpage was written by Andres Roldan &lt;aroldan [at] debian.org&gt; and the Valgrind developers.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Debugging your program using Valgrind&#8217;s gdbserver and GDB</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.gdbserver">http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.gdbserver</a></dl>
<dt> 2.</p>
<dd> vgdb</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.vgdb">http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.vgdb</a></dl>
<dt> 3.</p>
<dd> Valgrind monitor commands</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.valgrind-monitor-commands">http://www.valgrind.org/docs/manual/manual-core-adv.html#manual-core-adv.valgrind-monitor-commands</a></dl>
<dt> 4.</p>
<dd> The Commentary</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.valgrind.org/docs/manual/manual-core.html#manual-core.comment">http://www.valgrind.org/docs/manual/manual-core.html#manual-core.comment</a></dl>
<dt> 5.</p>
<dd> Scheduling and Multi-Thread Performance</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.valgrind.org/docs/manual/manual-core.html#manual-core.pthreads_perf_sched">http://www.valgrind.org/docs/manual/manual-core.html#manual-core.pthreads_perf_sched</a></dl>
<dt> 6.</p>
<dd> Cachegrind: a cache and branch-prediction profiler</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.valgrind.org/docs/manual/cg-manual.html">http://www.valgrind.org/docs/manual/cg-manual.html</a></dl>
</dl>
<h2>Index</h2>
