---
title: "scan-build(1)"
name: "scan-build"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scan-build/"
description: "scan-build – Clang static analyzer"
---

<h2 class="name">NAME</h2>
<p> <code>scan-build</code> &#8211; Clang static analyzer </p>
<h2>SYNOPSIS</h2>
<p> [-<code>ohkvV</code> ] [-<code>analyze-headers</code> ] [-<code>enable-checker </code>[<i>checker_name</i> ] ] [-<code>disable-checker </code>[<i>checker_name</i> ] ] [-<code>-help</code> ] [-<code>-help-checkers</code> ] [-<code>-html-title </code>[<i>=title</i> ] ] [-<code>-keep-going</code> ] [-<code>plist</code> ] [-<code>plist-html</code> ] [-<code>-status-bugs</code> ] [-<code>-use-c++ </code>[<i>=compiler_path</i> ] ] [-<code>-use-cc </code>[<i>=compiler_path</i> ] ] [-<code>-view</code> ] [-<code>constraints </code>[<i>model</i> ] ] [-<code>maxloop </code><i>N</i> ] [-<code>no-failure-reports</code> ] [-<code>stats</code> ] [-<code>store </code>[<i>model</i> ] ] <i>build_command</i> [build_options]</p>
<h2>DESCRIPTION</h2>
<p> is a Perl script that invokes the Clang static analyzer. Options used by or by the analyzer appear first, followed by the <i>build_command</i> and any <i>build_options</i> normally used to build the target system. </p>
<p> The static analyzer employs a long list of checking algorithms, see Sx CHECKERS . Output can be written in standard <code>.plist</code> and/or HTML format. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>-analyze-headers</code></p>
<dd> Also analyze functions in #included files.</p>
<dt><code>-enable-checker </code><i>checker_name , &#8211;</i><code>disable-checker </code><i>checker_name</i></p>
<dd> Enable/disable <i>checker_name</i> See Sx CHECKERS .</p>
<dt><code>-h , &#8211;help</code></p>
<dd> Display this message.</p>
<dt><code>&#8211;help-checkers</code></p>
<dd> List default checkers, see Sx CHECKERS .</p>
<dt><code>&#8211;html-title </code>[= <i>title</i> ]</p>
<dd> Specify the title used on generated HTML pages. A default title is generated if <i>title</i> is not specified.</p>
<dt><code>-k , &#8211;keep-going</code></p>
<dd> Add a &#8220;keep on going&#8221; option to <i>build_command</i> Currently supports make and xcodebuild. This is a convenience option; one can specify this behavior directly using build options.</p>
<dt><code>-o</code></p>
<dd> Target directory for HTML report files. Subdirectories will be created as needed to represent separate invocations of the analyzer. If this option is not specified, a directory is created in /tmp (TMPDIR on Mac OS X) to store the reports.</p>
<dt><code>-plist</code></p>
<dd> Output the results as a set of <code>.plist</code> files. (By default the output of is a set of HTML files.)</p>
<dt><code>-plist-html</code></p>
<dd> Output the results as a set of HTML and .plist files</p>
<dt><code>&#8211;status-bugs</code></p>
<dd> Set exit status to 1 if it found potential bugs and 0 otherwise. By default the exit status of is that returned by <i>build_command</i></p>
<dt><code>&#8211;use-c++ </code>[= <i>compiler_path</i> ]</p>
<dd> Guess the default compiler for your C++ and Objective-C++ code. Use this option to specify an alternate compiler.</p>
<dt><code>&#8211;use-cc </code>[= <i>compiler_path</i> ]</p>
<dd> Guess the default compiler for your C and Objective-C code. Use this option to specify an alternate compiler.</p>
<dt><code>-v</code></p>
<dd> Verbose output from and the analyzer. A second and third <i>v</i> increases verbosity.</p>
<dt><code>-V , &#8211;view</code></p>
<dd> View analysis results in a web browser when the build completes.</p>
<dt><code>-constraints </code>[<i>model</i> ]</p>
<dd> Specify the contraint engine used by the analyzer. By default the `range&#8217; model is used. Specifying `basic&#8217; uses a simpler, less powerful constraint model used by checker-0.160 and earlier.</p>
<dt><code>-maxloop </code><i>N</i></p>
<dd> Specifiy the number of times a block can be visited before giving up. Default is 4. Increase for more comprehensive coverage at a cost of speed.</p>
<dt><code>-no-failure-reports</code></p>
<dd> Do not create a `failures&#8217; subdirectory that includes analyzer crash reports and preprocessed source files.</p>
<dt><code>-stats</code></p>
<dd> Generates visitation statistics for the project being analyzed.</p>
<dt><code>-store </code>[<i>model</i> ]</p>
<dd> Specify the store model used by the analyzer. By default, the `region&#8217; store model is used. `region&#8217; specifies a field- sensitive store model. Users can also specify `basic&#8217; which is far less precise but can more quickly analyze code. `basic&#8217; was the default store model for checker-0.221 and earlier.</dl>
<h2>EXIT STATUS</h2>
<p> returns the value returned by <i>build_command</i> unless &#8211;<code>-status-bugs</code> or &#8211;<code>-keep-going</code> is used.</p>
<h2>CHECKERS</h2>
<p> The checkers listed below may be enabled/disabled using the &#8211;<code>enable-checker</code> and &#8211;<code>disable-checker</code> options. A default group of checkers is run unless explicitly disabled. Exactly which checkers constitute the default group is a function of the operating system in use; they are listed with &#8211;<code>-help-checkers</code></p>
<dl>
<dt><code>core.AdjustedReturnValue</code></p>
<dd> Check to see if the return value of a function call is different than the caller expects (e.g., from calls through function pointers).</p>
<dt><code>core.AttributeNonNull</code></p>
<dd> Check for null pointers passed as arguments to a function whose arguments are marked with the `nonnull&#8217; attribute.</p>
<dt><code>core.CallAndMessage</code></p>
<dd> Check for logical errors for function calls and Objective-C message expressions (e.g., uninitialized arguments, null function pointers).</p>
<dt><code>core.DivideZero</code></p>
<dd> Check for division by zero.</p>
<dt><code>core.NullDereference</code></p>
<dd> Check for dereferences of null pointers.</p>
<dt><code>core.StackAddressEscape</code></p>
<dd> Check that addresses to stack memory do not escape the function.</p>
<dt><code>core.UndefinedBinaryOperatorResult</code></p>
<dd> Check for undefined results of binary operators.</p>
<dt><code>core.VLASize</code></p>
<dd> Check for declarations of VLA of undefined or zero size.</p>
<dt><code>core.builtin.BuiltinFunctions</code></p>
<dd> Evaluate compiler builtin functions, e.g. Fn alloca .</p>
<dt><code>core.builtin.NoReturnFunctions</code></p>
<dd> Evaluate `panic&#8217; functions that are known to not return to the caller.</p>
<dt><code>core.uninitialized.ArraySubscript</code></p>
<dd> Check for uninitialized values used as array subscripts.</p>
<dt><code>core.uninitialized.Assign</code></p>
<dd> Check for assigning uninitialized values.</p>
<dt><code>core.uninitialized.Branch</code></p>
<dd> Check for uninitialized values used as branch conditions.</p>
<dt><code>core.uninitialized.CapturedBlockVariable</code></p>
<dd> Check for blocks that capture uninitialized values.</p>
<dt><code>core.uninitialized.UndefReturn</code></p>
<dd> Check for uninitialized values being returned to the caller.</p>
<dt><code>deadcode.DeadStores</code></p>
<dd> Check for values stored to variables that are never read afterwards.</p>
<dt><code>debug.DumpCFG</code></p>
<dd> Display Control-Flow Graphs.</p>
<dt><code>debug.DumpCallGraph</code></p>
<dd> Display Call Graph.</p>
<dt><code>debug.DumpDominators</code></p>
<dd> Print the dominance tree for a given Control-Flow Graph.</p>
<dt><code>debug.DumpLiveVars</code></p>
<dd> Print results of live variable analysis.</p>
<dt><code>debug.Stats</code></p>
<dd> Emit warnings with analyzer statistics.</p>
<dt><code>debug.TaintTest</code></p>
<dd> Mark tainted symbols as such.</p>
<dt><code>debug.ViewCFG</code></p>
<dd> View Control-Flow Graphs using <code>GraphViz</code></p>
<dt><code>debug.ViewCallGraph</code></p>
<dd> View Call Graph using <code>GraphViz</code></p>
<dt><code>llvm.Conventions</code></p>
<dd> Check code for LLVM codebase conventions.</p>
<dt><code>osx.API</code></p>
<dd> Check for proper uses of various Mac OS X APIs.</p>
<dt><code>osx.AtomicCAS</code></p>
<dd> Evaluate calls to Vt OSAtomic functions.</p>
<dt><code>osx.SecKeychainAPI</code></p>
<dd> Check for proper uses of Secure Keychain APIs.</p>
<dt><code>osx.cocoa.AtSync</code></p>
<dd> Check for null pointers used as mutexes for @synchronized.</p>
<dt><code>osx.cocoa.ClassRelease</code></p>
<dd> Check for sending `retain&#8217; , `release,&#8217; or `autorelease&#8217; directly to a Class.</p>
<dt><code>osx.cocoa.IncompatibleMethodTypes</code></p>
<dd> Warn about Objective-C method signatures with type incompatibilities.</p>
<dt><code>osx.cocoa.NSAutoreleasePool</code></p>
<dd> Warn for suboptimal uses of Vt NSAutoreleasePool in Objective-C GC mode.</p>
<dt><code>osx.cocoa.NSError</code></p>
<dd> Check usage of NSError** parameters.</p>
<dt><code>osx.cocoa.NilArg</code></p>
<dd> Check for prohibited nil arguments to Objective-C method calls.</p>
<dt><code>osx.cocoa.RetainCount</code></p>
<dd> Check for leaks and improper reference count management.</p>
<dt><code>osx.cocoa.SelfInit</code></p>
<dd> Check that `self&#8217; is properly initialized inside an initializer method.</p>
<dt><code>osx.cocoa.UnusedIvars</code></p>
<dd> Warn about private ivars that are never used.</p>
<dt><code>osx.cocoa.VariadicMethodTypes</code></p>
<dd> Check for passing non-Objective-C types to variadic methods that expect only Objective-C types.</p>
<dt><code>osx.coreFoundation.CFError</code></p>
<dd> Check usage of CFErrorRef* parameters.</p>
<dt><code>osx.coreFoundation.CFNumber</code></p>
<dd> Check for proper uses of Fn CFNumberCreate .</p>
<dt><code>osx.coreFoundation.CFRetainRelease</code></p>
<dd> Check for null arguments to Fn CFRetain , Fn CFRelease , and Fn CFMakeCollectable .</p>
<dt><code>osx.coreFoundation.containers.OutOfBounds</code></p>
<dd> Checks for index out-of-bounds when using the Vt CFArray API.</p>
<dt><code>osx.coreFoundation.containers.PointerSizedValues</code></p>
<dd> Warns if Vt CFArray , Vt CFDictionary , or Vt CFSet are created with non-pointer-size values.</p>
<dt><code>security.FloatLoopCounter</code></p>
<dd> Warn on using a floating point value as a loop counter (CERT: FLP30-C, FLP30-CPP).</p>
<dt><code>security.insecureAPI.UncheckedReturn</code></p>
<dd> Warn on uses of functions whose return values must be always checked.</p>
<dt><code>security.insecureAPI.getpw</code></p>
<dd> Warn on uses of Fn getpw .</p>
<dt><code>security.insecureAPI.gets</code></p>
<dd> Warn on uses of Fn gets .</p>
<dt><code>security.insecureAPI.mkstemp</code></p>
<dd> Warn when Fn mkstemp is passed fewer than 6 X&#8217;s in the format string.</p>
<dt><code>security.insecureAPI.mktemp</code></p>
<dd> Warn on uses of Fn mktemp .</p>
<dt><code>security.insecureAPI.rand</code></p>
<dd> Warn on uses of Fn rand , Fn random , and related functions.</p>
<dt><code>security.insecureAPI.strcpy</code></p>
<dd> Warn on uses of Fn strcpy and Fn strcat .</p>
<dt><code>security.insecureAPI.vfork</code></p>
<dd> Warn on uses of Fn vfork .</p>
<dt><code>unix.API</code></p>
<dd> Check calls to various UNIX/Posix functions.</p>
<dt><code>unix.Malloc</code></p>
<dd> Check for memory leaks, double free, and use-after-free.</p>
<dt><code>unix.cstring.BadSizeArg</code></p>
<dd> Check the size argument passed into C string functions for common erroneous patterns.</p>
<dt><code>unix.cstring.NullArg</code></p>
<dd> Check for null pointers being passed as arguments to C string functions.</dl>
<h2>EXAMPLE</h2>
<p> <code>scan-build -o /tmp/myhtmldir make -j4</code> </p>
<p> The above example causes analysis reports to be deposited into a subdirectory of /tmp/myhtmldir and to run <code>make</code> with the &#8211;<code>j4</code> option. A different subdirectory is created each time analyzes a project. The analyzer should support most parallel builds, but not distributed builds.</p>
<h2>AUTHORS</h2>
<p> was written by An Ted Kremenek . Documentation contributed by An James K. Lowden Aq jklowden [at] schemamania.org . </p>
<h2>Index</h2>
