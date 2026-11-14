---
title: "ftrace(1)"
name: "ftrace"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ftrace/"
description: "ftrace – trace system calls, function calls and signals"
---

<h2 class="name">NAME</h2>
<p> ftrace &#8211; trace system calls, function calls and signals </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ftrace</code> [-f] [-follow] [-dl] [-m] [-o=<i>FILE</i>] [-p=<i>PID</i>&#8230;] [-pc] [-sys=<i>SYSCALL</i>[,<i>SYSCALL</i>&#8230;]] [-sig=<i>SIG</i>[,<i>SIG</i>&#8230;]] [-sym=<i>RULE</i>[,<i>RULE</i>&#8230;]] [-addr=<i>RULE</i>[,<i>RULE</i>&#8230;]] [-stack] [&#8211;] <i>command</i>&nbsp;<wbr>[<i>arguments</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>ftrace</code></p>
<dd>starts given <i>command</i> and according to tracing script given via command-line arguments, it traces its system calls, symbol entry points in general, and possibly other events as well. It uses the Frysk framework to implement tracing. </p>
<p> The working set of events <code>ftrace</code> should trace is defined by the following arguments.</p>
<h3>Process Selection Options</h3>
<p> -p=<i>PID</i></p>
<dl>
<dt>
<dd> Attach to a process with given <i>PID</i>.</dl>
<p> -f, -follow</p>
<dl>
<dt>
<dd> Follow children: automatically attach to forks of traced process.</dl>
<h3>Symbol Tracing</h3>
<p> -dl</p>
<dl>
<dt>
<dd> Trace inside dynamic linker. When this option is not present, <code>ftrace</code> will function as if -#INTERP#* rule was present at the end of each tracing script.</dl>
<p> -sym=<i>SYMBOL</i>[,<i>SYMBOL</i>&#8230;]</p>
<dl>
<dt>
<dd> Trace calls through the symbol entry points. Ftrace displays a message each time a thread of execution hits entry point of one of the traced functions, and then when (if) the function returns. </p>
<p> If <i>SYMBOL</i> references PLT slot, calls done through that PLT slot are recorded. You then effectively trace calls done FROM given library or executable, and generally can&#8217;t say which library the call leads TO. </p>
<p> When tracing ordinary symbol, catch all calls that end up at this symbol. That includes the calls that don&#8217;t go through PLT and as such are not intended as inter-library calls, but rather intra-library calls. </p>
<p> See below for detailed description of <i>SYMBOL</i> rule syntax.</dl>
<h3>Other Traceable Events</h3>
<p> -sys=<i>SYSCALL</i>[,<i>SYSCALL</i>&#8230;]</p>
<dl>
<dt>
<dd> Trace system calls that match given <i>SYSCALL</i> ruleset. See below for description of <i>SYSCALL</i> syntax.</dl>
<p> -sig=<i>SIGNAL</i>[,<i>SIGNAL</i>&#8230;]</p>
<dl>
<dt>
<dd> Trace signals that match given <i>SIGNAL</i> ruleset. See below for description of <i>SIGNAL</i> syntax.</dl>
<p> -addr=<i>RULE</i>[,<i>RULE</i>&#8230;]</p>
<dl>
<dt>
<dd> Trace addresses given by <i>RULE</i>s. See below for description of address <i>RULE</i> syntax.</dl>
<h3>Other Options</h3>
<p> -m</p>
<dl>
<dt>
<dd> Print each file mapped to or unmapped from address space of the traced process.</dl>
<p> -pc</p>
<dl>
<dt>
<dd> Show the value of instruction pointer at each reported event.</dl>
<p> -stack</p>
<dl>
<dt>
<dd> Stack trace when traced symbol is hit. Note that this option also applies to traced system calls. If you need to cherry-pick which event should stack trace, use # operator described in sections below.</dl>
<h3>Stack Print Options</h3>
<p> <code>-number-of-frames </code><i>count</i></p>
<dl>
<dt>
<dd> Limit the back-trace to <i>count</i> frames. The default is to limit the back-trace to 10 frames. Specify 0 or &quot;all&quot; to print all frames.</dl>
<p> <code>-lite</code></p>
<dl>
<dt>
<dd> Perform a light-weight stack backtrace containing only minimal information. Equivalent to <code>-print &#8211;</code>.</dl>
<p> <code>-rich</code></p>
<dl>
<dt>
<dd> Perform a detailed stack back-trace that includes, where possible, inlined function calls, parameter names and values, and debug-names. Equivalent to <code>-print inline,params,debug-names</code>.</dl>
<p> <code>-print </code><i>print-option</i><code>,&#8230;</code></p>
<dl>
<dt>
<dd> Specify the level of detail to include in a stack back-trace. <i>print-option</i> can be any of: </p>
<p> debug-names: use debug information, such as DWARF, to determine the name of functions </p>
<p> paths: include the full path to source files and libraries </p>
<p> inline: include in-line function in back-trace </p>
<p> locals: to include local variables from each frame </p>
<p> params: include the function parameters </p>
<p> To negate a <i>print-option</i> prefix it with &quot;-&quot;.</dl>
<h3>Standard Frysk Options</h3>
<p> <code>-exe</code></p>
<dl>
<dt>
<dd> The full path of the executable to read.</dl>
<p> <code>-noexe</code></p>
<dl>
<dt>
<dd> Do not attempt to read the corresponding executable when loading a core file.</dl>
<p> <code>-sysroot </code><i>directory</i></p>
<dl>
<dt>
<dd> The system root directory under which all executables, libraries, and source are located.</dl>
<p> <code>-debug </code><i>class</i><code>=</code><i>level</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Set internal debug-tracing of the specified Java <i>class</i> to <i>level</i> (level can be NONE, INFO, WARNING, FINE, and FINEST). If the <i>level</i> is absent, FINE is assumed; if the <i>class</i> is absent, the global level is set.</dl>
<h2>SYMBOL RULE SYNTAX</h2>
<p> To decide which PLT slots or entry points should be traced, following process takes place. A set of symbols to trace (&quot;working set&quot;) is initially empty. Rules, if present, are then enumerated from left to right, and set is modified depending on the rules. Rules are delimited by a comma. Syntax of each rule is following: </p>
<p> [-]<i>pattern</i>[/<i>options</i>] </p>
<p> Without the optional &quot;-&quot; all symbols that match the <i>pattern</i> are added to the working set. With &quot;-&quot;, matching symbols are removed. </p>
<p> If &quot;/&quot; is present at the end of the rule, following letters are interpreted as rule flags. Currently only one flag is available, &quot;s&quot;. When present, it means ftrace should show a stack trace when it hits a symbol that matches this rule. </p>
<p> When a &quot;-&quot; rule has an &quot;/s&quot; flag, the call should still be traced, but stack trace shouldn&#8217;t be generated. </p>
<p> <i>pattern</i> defines which symbols or PLT slots from which libraries should be added or removed from working set. Syntax of pattern is as follows: </p>
<p> [#<i>soname</i>#][<i>filename.c</i>#][(<i>proc</i>|<i>line</i>)#][plt:]symbol[@<i>version</i>] </p>
<p> <i>soname</i> component is matched against a soname of a library in which we wish to trace the call. If the library has no associated soname (such as is usual in case of main executable), the match is done against the file name (without a path). Two special sonames are distinguished: &quot;MAIN&quot;, which always matches main executable; and &quot;INTERP&quot;, which always matches ELF interpreter (dynamic linker) of the main executable. If the component is missing, then the rule is applicable in all libraries and in main executable. </p>
<p> <i>filename.c</i> component is matched against the name of a file where the symbol is defined. NOTE: This is currently not implemented. </p>
<p> <i>proc</i> component is matched against the name of block surrounding the definition we wish to trace. If the block doesn&#8217;t have a name, you can instead refer to it with the <i>line</i> number that the block surrounds. NOTE: This is currently not implemented. </p>
<p> <i>symbol</i> component is matched against the name of symbol under consideration. If &quot;plt:&quot; prefix is present, the rule matches PLT entry associated with the symbol instead of the symbol itself. </p>
<p> <i>version</i> component is matched against version associated with symbol. If the symbol has no associated version, it is considered to be an empty string. (It is possible to request symbol without a version with the pattern &quot;foo@&quot;.) NOTE: This is currently not implemented. </p>
<p> All components are presented in glob syntax. See <a href="/docs/linux/man/7-glob/">glob</a>(7) manual page for more details. See below for examples.</p>
<h2>SYSCALL AND SIGNAL RULE SYNTAX</h2>
<p> Under the presence of the <code>-sys</code> (or <code>-sig</code>) option, ALL system calls (or signals) are ALWAYS traced. This is a limitation of the ptrace layer. The system call and signal rules however serve as a simple way of filtering out the output that you are not interested in. In following paragraphs, the word &quot;event&quot; will be used to mean &quot;signal or syscall, whatever applies&quot;. </p>
<p> The system call and signal rule syntax and semantics are the same as the symbol rule syntax: </p>
<p> [-]<i>pattern</i>[/<i>options</i>] </p>
<p> Event selection pattern syntax is then as follows: </p>
<p> [<i>event name</i>|<i>event number</i>] </p>
<p> When the pattern is empty, it matches all events known to frysk. When the pattern is simple number (e.g. &quot;12&quot;), then the pattern matches the event with the given number. Otherwise the pattern is considered to be case-insensitive glob, and matched against event names. Whole name has to match for event to be a part of working set. </p>
<p> Signal can be given both with and without leading &quot;sig&quot; (e.g. &quot;sigkill&quot; as well as &quot;kill&quot;).</p>
<h2>ADDRESS RULE SYNTAX</h2>
<p> The process of establishing a working set of addresses that should be traced is the same as for symbol rules, and the general syntax reflects that. Each rule looks like this: </p>
<p> [-]<i>pattern</i>[/<i>options</i>] </p>
<p> Each pattern then looks like this: </p>
<p> [#<i>soname</i>#][0x]<i>address</i> </p>
<p> Addresses are always given in hexadecimal notation, even if initial 0x is missing. </p>
<p> <i>soname</i> component is the same as in symbol tracing, i.e. it&#8217;s matched against a soname of a library in which we wish to trace the address. Same rules apply regarding INTERP and MAIN meta-sonames. Refer to the chapter &quot;SYMBOL RULE SYNTAX&quot; for detailed description. </p>
<p> Even though <i>soname</i> is optional, at least one soname has to be specified at the beginning of the <code>-addr</code> command. That&#8217;s because in general it makes no sense to want to trace the same address in ALL object files at once. The components that are soname-less are assumed to have a soname of the previous component that has soname. </p>
<p> For example, this will trace two addresses from the main binary, and stack trace one of them:</p>
<dl>
<dt> <code>ftrace -addr=#MAIN#0x08052780/s,08049314 &#8212; ls</code></dl>
<dd>If you need to trace the same address in several files, you can use the fact that the soname pattern is a glob. </p>
<p> The addresses are assumed to be copied from readelf or objdump. ftrace biases the value accordingly depending on where the module is actually mapped.</p>
<h2>EXAMPLES</h2>
<p> Trace all system calls:</p>
<dl>
<dt> <code>ftrace -sys= ls</code></dl>
<dd>Trace variants of stat system call and moreover a system call #3:</p>
<dl>
<dt> <code>ftrace -sys=&#8217;*stat*,3&#8242; ls</code></dl>
<dd>Various ways to tell ftrace that you want to stack trace on SIGUSR1:</p>
<dl>
<dt> <code>ftrace -sig=USR1/s,usr1/s,SIGUSR1/s,sigusr1/s,10/s ~/sig</code></dl>
<dd>Trace all library calls:</p>
<dl>
<dt> <code>ftrace -sym=plt:* ls</code></dl>
<dd>Trace all library calls to functions that contain substring &quot;write&quot; in their names:</p>
<dl>
<dt> <code>ftrace -sym=plt:*write* ls</code></dl>
<dd>Trace memory functions done from libraries, i.e. not from main executable:</p>
<dl>
<dt> <code>ftrace -sym=&#8217;plt:*alloc,plt:free,-#MAIN#plt:*&#8217; ls</code></dl>
<dd>Stack trace on everything, except for memory allocation functions (which should still be traced):</p>
<dl>
<dt> <code>ftrace -sym=&#8217;plt:*/s,-plt:*alloc/s,-plt:free/s&#8217; ls</code></dl>
<h2>SEE ALSO</h2>
<dd><a href="/docs/linux/man/7-frysk/">frysk</a>(7), <a href="/docs/linux/man/7-glob/">glob</a>(7)</p>
<h2>BUGS</h2>
<p> The option parser is greedy when looking for options so running ftrace on a program that uses options can be a problem, use &#8212; to split between ftrace and the program. So change from: </p>
<dl>
<dt>
<dd>
<pre>
~/prefix/bin/ftrace ~/prefix/lib64/frysk/funit --arch 32 frysk.proc.TestAbandon
</pre>
</dl>
<p> to </p>
<dl>
<dt>
<dd>
<pre>
~/prefix/bin/ftrace -- ~/prefix/lib64/frysk/funit --arch 32 frysk.proc.TestAbandon
</pre>
</dl>
<p> Report bugs to m[blue]<code><a rel="nofollow" href="http://sourceware.org/frysk">http://sourceware.org/frysk</a></code>m[] </p>
<h2>Index</h2>
