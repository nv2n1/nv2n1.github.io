---

title: "scan-build(1)"
name: "scan-build"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scan-build/"
description: "scan-build – Clang static analyzer"
---

<p> <code>scan-build</code> &#8211; Clang static analyzer </p>
<h2>SYNOPSIS</h2>
<p> [-<code>ohkvV</code> ] [-<code>analyze-headers</code> ] [-<code>enable-checker </code>[<i>checker_name</i> ] ] [-<code>disable-checker </code>[<i>checker_name</i> ] ] [-<code>-help</code> ] [-<code>-help-checkers</code> ] [-<code>-html-title </code>[<i>=title</i> ] ] [-<code>-keep-going</code> ] [-<code>plist</code> ] [-<code>plist-html</code> ] [-<code>-status-bugs</code> ] [-<code>-use-c++ </code>[<i>=compiler_path</i> ] ] [-<code>-use-cc </code>[<i>=compiler_path</i> ] ] [-<code>-view</code> ] [-<code>constraints </code>[<i>model</i> ] ] [-<code>maxloop </code><i>N</i> ] [-<code>no-failure-reports</code> ] [-<code>stats</code> ] [-<code>store </code>[<i>model</i> ] ] <i>build_command</i> [build_options]</p>
<h2>DESCRIPTION</h2>
<p> is a Perl script that invokes the Clang static analyzer. Options used by or by the analyzer appear first, followed by the <i>build_command</i> and any <i>build_options</i> normally used to build the target system. </p>
<p> The static analyzer employs a long list of checking algorithms, see Sx CHECKERS . Output can be written in standard <code>.plist</code> and/or HTML format. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>-analyze-headers</code></dt>
<dd> Also analyze functions in #included files.</dd>
<dt><code>-enable-checker </code><i>checker_name , &#8211;</i><code>disable-checker </code><i>checker_name</i></dt>
<dd> Enable/disable <i>checker_name</i> See Sx CHECKERS .</dd>
<dt><code>-h , &#8211;help</code></dt>
<dd> Display this message.</dd>
<dt><code>&#8211;help-checkers</code></dt>
<dd> List default checkers, see Sx CHECKERS .</dd>
<dt><code>&#8211;html-title </code>[= <i>title</i> ]</dt>
<dd> Specify the title used on generated HTML pages. A default title is generated if <i>title</i> is not specified.</dd>
<dt><code>-k , &#8211;keep-going</code></dt>
<dd> Add a &#8220;keep on going&#8221; option to <i>build_command</i> Currently supports make and xcodebuild. This is a convenience option; one can specify this behavior directly using build options.</dd>
<dt><code>-o</code></dt>
<dd> Target directory for HTML report files. Subdirectories will be created as needed to represent separate invocations of the analyzer. If this option is not specified, a directory is created in /tmp (TMPDIR on Mac OS X) to store the reports.</dd>
<dt><code>-plist</code></dt>
<dd> Output the results as a set of <code>.plist</code> files. (By default the output of is a set of HTML files.)</dd>
<dt><code>-plist-html</code></dt>
<dd> Output the results as a set of HTML and .plist files</dd>
<dt><code>&#8211;status-bugs</code></dt>
<dd> Set exit status to 1 if it found potential bugs and 0 otherwise. By default the exit status of is that returned by <i>build_command</i></dd>
<dt><code>&#8211;use-c++ </code>[= <i>compiler_path</i> ]</dt>
<dd> Guess the default compiler for your C++ and Objective-C++ code. Use this option to specify an alternate compiler.</dd>
<dt><code>&#8211;use-cc </code>[= <i>compiler_path</i> ]</dt>
<dd> Guess the default compiler for your C and Objective-C code. Use this option to specify an alternate compiler.</dd>
<dt><code>-v</code></dt>
<dd> Verbose output from and the analyzer. A second and third <i>v</i> increases verbosity.</dd>
<dt><code>-V , &#8211;view</code></dt>
<dd> View analysis results in a web browser when the build completes.</dd>
<dt><code>-constraints </code>[<i>model</i> ]</dt>
<dd> Specify the contraint engine used by the analyzer. By default the `range&#8217; model is used. Specifying `basic&#8217; uses a simpler, less powerful constraint model used by checker-0.160 and earlier.</dd>
<dt><code>-maxloop </code><i>N</i></dt>
<dd> Specifiy the number of times a block can be visited before giving up. Default is 4. Increase for more comprehensive coverage at a cost of speed.</dd>
<dt><code>-no-failure-reports</code></dt>
<dd> Do not create a `failures&#8217; subdirectory that includes analyzer crash reports and preprocessed source files.</dd>
<dt><code>-stats</code></dt>
<dd> Generates visitation statistics for the project being analyzed.</dd>
<dt><code>-store </code>[<i>model</i> ]</dt>
<dd> Specify the store model used by the analyzer. By default, the `region&#8217; store model is used. `region&#8217; specifies a field- sensitive store model. Users can also specify `basic&#8217; which is far less precise but can more quickly analyze code. `basic&#8217; was the default store model for checker-0.221 and earlier.</dd></dl>
<h2>EXIT STATUS</h2>
<p> returns the value returned by <i>build_command</i> unless &#8211;<code>-status-bugs</code> or &#8211;<code>-keep-going</code> is used.</p>
<h2>CHECKERS</h2>
<p> The checkers listed below may be enabled/disabled using the &#8211;<code>enable-checker</code> and &#8211;<code>disable-checker</code> options. A default group of checkers is run unless explicitly disabled. Exactly which checkers constitute the default group is a function of the operating system in use; they are listed with &#8211;<code>-help-checkers</code></p>
<dl>
<dt><code>core.AdjustedReturnValue</code></dt>
<dd> Check to see if the return value of a function call is different than the caller expects (e.g., from calls through function pointers).</dd>
<dt><code>core.AttributeNonNull</code></dt>
<dd> Check for null pointers passed as arguments to a function whose arguments are marked with the `nonnull&#8217; attribute.</dd>
<dt><code>core.CallAndMessage</code></dt>
<dd> Check for logical errors for function calls and Objective-C message expressions (e.g., uninitialized arguments, null function pointers).</dd>
<dt><code>core.DivideZero</code></dt>
<dd> Check for division by zero.</dd>
<dt><code>core.NullDereference</code></dt>
<dd> Check for dereferences of null pointers.</dd>
<dt><code>core.StackAddressEscape</code></dt>
<dd> Check that addresses to stack memory do not escape the function.</dd>
<dt><code>core.UndefinedBinaryOperatorResult</code></dt>
<dd> Check for undefined results of binary operators.</dd>
<dt><code>core.VLASize</code></dt>
<dd> Check for declarations of VLA of undefined or zero size.</dd>
<dt><code>core.builtin.BuiltinFunctions</code></dt>
<dd> Evaluate compiler builtin functions, e.g. Fn alloca .</dd>
<dt><code>core.builtin.NoReturnFunctions</code></dt>
<dd> Evaluate `panic&#8217; functions that are known to not return to the caller.</dd>
<dt><code>core.uninitialized.ArraySubscript</code></dt>
<dd> Check for uninitialized values used as array subscripts.</dd>
<dt><code>core.uninitialized.Assign</code></dt>
<dd> Check for assigning uninitialized values.</dd>
<dt><code>core.uninitialized.Branch</code></dt>
<dd> Check for uninitialized values used as branch conditions.</dd>
<dt><code>core.uninitialized.CapturedBlockVariable</code></dt>
<dd> Check for blocks that capture uninitialized values.</dd>
<dt><code>core.uninitialized.UndefReturn</code></dt>
<dd> Check for uninitialized values being returned to the caller.</dd>
<dt><code>deadcode.DeadStores</code></dt>
<dd> Check for values stored to variables that are never read afterwards.</dd>
<dt><code>debug.DumpCFG</code></dt>
<dd> Display Control-Flow Graphs.</dd>
<dt><code>debug.DumpCallGraph</code></dt>
<dd> Display Call Graph.</dd>
<dt><code>debug.DumpDominators</code></dt>
<dd> Print the dominance tree for a given Control-Flow Graph.</dd>
<dt><code>debug.DumpLiveVars</code></dt>
<dd> Print results of live variable analysis.</dd>
<dt><code>debug.Stats</code></dt>
<dd> Emit warnings with analyzer statistics.</dd>
<dt><code>debug.TaintTest</code></dt>
<dd> Mark tainted symbols as such.</dd>
<dt><code>debug.ViewCFG</code></dt>
<dd> View Control-Flow Graphs using <code>GraphViz</code></dd>
<dt><code>debug.ViewCallGraph</code></dt>
<dd> View Call Graph using <code>GraphViz</code></dd>
<dt><code>llvm.Conventions</code></dt>
<dd> Check code for LLVM codebase conventions.</dd>
<dt><code>osx.API</code></dt>
<dd> Check for proper uses of various Mac OS X APIs.</dd>
<dt><code>osx.AtomicCAS</code></dt>
<dd> Evaluate calls to Vt OSAtomic functions.</dd>
<dt><code>osx.SecKeychainAPI</code></dt>
<dd> Check for proper uses of Secure Keychain APIs.</dd>
<dt><code>osx.cocoa.AtSync</code></dt>
<dd> Check for null pointers used as mutexes for @synchronized.</dd>
<dt><code>osx.cocoa.ClassRelease</code></dt>
<dd> Check for sending `retain&#8217; , `release,&#8217; or `autorelease&#8217; directly to a Class.</dd>
<dt><code>osx.cocoa.IncompatibleMethodTypes</code></dt>
<dd> Warn about Objective-C method signatures with type incompatibilities.</dd>
<dt><code>osx.cocoa.NSAutoreleasePool</code></dt>
<dd> Warn for suboptimal uses of Vt NSAutoreleasePool in Objective-C GC mode.</dd>
<dt><code>osx.cocoa.NSError</code></dt>
<dd> Check usage of NSError** parameters.</dd>
<dt><code>osx.cocoa.NilArg</code></dt>
<dd> Check for prohibited nil arguments to Objective-C method calls.</dd>
<dt><code>osx.cocoa.RetainCount</code></dt>
<dd> Check for leaks and improper reference count management.</dd>
<dt><code>osx.cocoa.SelfInit</code></dt>
<dd> Check that `self&#8217; is properly initialized inside an initializer method.</dd>
<dt><code>osx.cocoa.UnusedIvars</code></dt>
<dd> Warn about private ivars that are never used.</dd>
<dt><code>osx.cocoa.VariadicMethodTypes</code></dt>
<dd> Check for passing non-Objective-C types to variadic methods that expect only Objective-C types.</dd>
<dt><code>osx.coreFoundation.CFError</code></dt>
<dd> Check usage of CFErrorRef* parameters.</dd>
<dt><code>osx.coreFoundation.CFNumber</code></dt>
<dd> Check for proper uses of Fn CFNumberCreate .</dd>
<dt><code>osx.coreFoundation.CFRetainRelease</code></dt>
<dd> Check for null arguments to Fn CFRetain , Fn CFRelease , and Fn CFMakeCollectable .</dd>
<dt><code>osx.coreFoundation.containers.OutOfBounds</code></dt>
<dd> Checks for index out-of-bounds when using the Vt CFArray API.</dd>
<dt><code>osx.coreFoundation.containers.PointerSizedValues</code></dt>
<dd> Warns if Vt CFArray , Vt CFDictionary , or Vt CFSet are created with non-pointer-size values.</dd>
<dt><code>security.FloatLoopCounter</code></dt>
<dd> Warn on using a floating point value as a loop counter (CERT: FLP30-C, FLP30-CPP).</dd>
<dt><code>security.insecureAPI.UncheckedReturn</code></dt>
<dd> Warn on uses of functions whose return values must be always checked.</dd>
<dt><code>security.insecureAPI.getpw</code></dt>
<dd> Warn on uses of Fn getpw .</dd>
<dt><code>security.insecureAPI.gets</code></dt>
<dd> Warn on uses of Fn gets .</dd>
<dt><code>security.insecureAPI.mkstemp</code></dt>
<dd> Warn when Fn mkstemp is passed fewer than 6 X&#8217;s in the format string.</dd>
<dt><code>security.insecureAPI.mktemp</code></dt>
<dd> Warn on uses of Fn mktemp .</dd>
<dt><code>security.insecureAPI.rand</code></dt>
<dd> Warn on uses of Fn rand , Fn random , and related functions.</dd>
<dt><code>security.insecureAPI.strcpy</code></dt>
<dd> Warn on uses of Fn strcpy and Fn strcat .</dd>
<dt><code>security.insecureAPI.vfork</code></dt>
<dd> Warn on uses of Fn vfork .</dd>
<dt><code>unix.API</code></dt>
<dd> Check calls to various UNIX/Posix functions.</dd>
<dt><code>unix.Malloc</code></dt>
<dd> Check for memory leaks, double free, and use-after-free.</dd>
<dt><code>unix.cstring.BadSizeArg</code></dt>
<dd> Check the size argument passed into C string functions for common erroneous patterns.</dd>
<dt><code>unix.cstring.NullArg</code></dt>
<dd> Check for null pointers being passed as arguments to C string functions.</dd></dl>
<h2>EXAMPLE</h2>
<p> <code>scan-build -o /tmp/myhtmldir make -j4</code> </p>
<p> The above example causes analysis reports to be deposited into a subdirectory of /tmp/myhtmldir and to run <code>make</code> with the &#8211;<code>j4</code> option. A different subdirectory is created each time analyzes a project. The analyzer should support most parallel builds, but not distributed builds.</p>
<h2>AUTHORS</h2>
<p> was written by An Ted Kremenek . Documentation contributed by An James K. Lowden Aq jklowden [at] schemamania.org . </p>
