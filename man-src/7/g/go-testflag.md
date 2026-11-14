---
title: "go-testflag(7)"
name: "go-testflag"
section: "7"
letter: "g"
url: "/docs/linux/man/7-go-testflag/"
description: "go – tool for managing Go source code"
---

<p>go &#8211; tool for managing Go source code</p>
<h2>Description</h2>
<p>The &#8216;go test&#8217; command takes both flags that apply to &#8216;go test&#8217; itself and flags that apply to the resulting test binary. </p>
<p> Several of the flags control profiling and write an execution profile suitable for &quot;go tool pprof&quot;; run &quot;go tool pprof -h&quot; for more information. The &#8211;alloc_space, &#8211;alloc_objects, and &#8211;show_bytes options of pprof control how the information is presented. </p>
<p> The following flags are recognized by the &#8216;go test&#8217; command and control the execution of any test:</p>
<dl>
<dt><code>-bench</code><i> regexp</i></p>
<dd>Run only those benchmarks matching a regular expression. By default, no benchmarks are run. To run all benchmarks, use &#8216;-bench .&#8217; or &#8216;-bench=.&#8217;. The regular expression is split by unbracketed slash (/) characters into a sequence of regular expressions, and each part of a benchmark&#8217;s identifier must match the corresponding element in the sequence, if any. Possible parents of matches are run with b.N=1 to identify sub-benchmarks. For example, given -bench=X/Y, top-level benchmarks matching X are run with b.N=1 to find any sub-benchmarks matching Y, which are then run in full.</p>
<dt><code>-benchtime</code><i> t</i></p>
<dd>Run enough iterations of each benchmark to take <i>t</i>, specified as a time.Duration (for example, -benchtime 1h30s).<br />
 The default is 1 second (1s).<br />
 The special syntax <i>N</i>x means to run the benchmark <i>N</i> times (for example, -benchtime 100x).</p>
<dt><code>-count</code><i> n</i></p>
<dd>Run each test and benchmark <i>n</i> times (default 1).<br />
 If -cpu is set, run n times for each GOMAXPROCS value.<br />
 Examples are always run once.</p>
<dt><code>-cover</code></p>
<dd>Enable coverage analysis.<br />
 Note that because coverage works by annotating the source code before compilation, compilation and test failures with coverage enabled may report line numbers that don&#8217;t correspond to the original sources.</p>
<dt><code>-covermode</code> set,count,atomic</p>
<dd>Set the mode for coverage analysis for the package[s] being tested. The default is &quot;set&quot; unless -race is enabled, in which case it is &quot;atomic&quot;.<br />
 The values:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;set: bool: does this statement run?<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count: int: how many times does this statement run?<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;atomic: int: count, but correct in multithreaded tests;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;significantly more expensive.<br />
 Sets -cover.</p>
<dt><code>-coverpkg </code><i>pattern1</i><code>,</code><i>pattern2</i><code>,</code><i>pattern3</i></p>
<dd>Apply coverage analysis in each test to packages matching the patterns. The default is for each test to analyze only the package being tested.<br />
 See &#8216;go help packages&#8217; for a description of package patterns.<br />
 Sets -cover.</p>
<dt><code>-cpu </code><i>1</i><code>,</code><i>2</i><code>,</code><i>4</i></p>
<dd>Specify a list of GOMAXPROCS values for which the tests or benchmarks should be executed. The default is the current value of GOMAXPROCS.</p>
<dt><code>-failfast</code></p>
<dd>Do not start new tests after the first test failure.</p>
<dt><code>-list</code><i> regexp</i></p>
<dd>List tests, benchmarks, or examples matching the regular expression. No tests, benchmarks or examples will be run. This will only list top-level tests. No subtest or subbenchmarks will be shown.</p>
<dt><code>-parallel</code><i> n</i></p>
<dd>Allow parallel execution of test functions that call t.Parallel. The value of this flag is the maximum number of tests to run simultaneously; by default, it is set to the value of GOMAXPROCS. Note that -parallel only applies within a single test binary. The &#8216;go test&#8217; command may run tests for different packages in parallel as well, according to the setting of the -p flag (see &#8216;go help build&#8217;).</p>
<dt><code>-run</code><i> regexp</i></p>
<dd>Run only those tests and examples matching the regular expression. For tests, the regular expression is split by unbracketed slash (/) characters into a sequence of regular expressions, and each part of a test&#8217;s identifier must match the corresponding element in the sequence, if any. Note that possible parents of matches are run too, so that -run=X/Y matches and runs and reports the result of all tests matching X, even those without sub-tests matching Y, because it must run them to look for those sub-tests.</p>
<dt><code>-short</code></p>
<dd>Tell long-running tests to shorten their run time. It is off by default but set during all.bash so that installing the Go tree can run a sanity check but not spend time running exhaustive tests.</p>
<dt><code>-shuffle </code>off,on,N</p>
<dd>Randomize the execution order of tests and benchmarks. It is off by default. If -shuffle is set to on, then it will seed the randomizer using the system clock. If -shuffle is set to an integer N, then N will be used as the seed value. In both cases, the seed will be reported for reproducibility.</p>
<dt><code>-timeout</code><i> d</i></p>
<dd>If a test binary runs longer than duration <i>d</i>, panic.<br />
 If <i>d</i> is 0, the timeout is disabled.<br />
 The default is 10 minutes (10m).</p>
<dt><code>-v</code></p>
<dd>Verbose output: log all tests as they are run. Also print all text from Log and Logf calls even if the test succeeds.</p>
<dt><code>-vet</code><i> list</i></p>
<dd>Configure the invocation of &quot;go vet&quot; during &quot;go test&quot; to use the comma-separated list of vet checks.<br />
 If list is empty, &quot;go test&quot; runs &quot;go vet&quot; with a curated list of checks believed to be always worth addressing.<br />
 If list is &quot;off&quot;, &quot;go test&quot; does not run &quot;go vet&quot; at all.</dl>
<p> The following flags are also recognized by &#8216;go test&#8217; and can be used to profile the tests during execution:</p>
<dl>
<dt><code>-benchmem</code></p>
<dd>Print memory allocation statistics for benchmarks.</p>
<dt><code>-blockprofile </code>block.out</p>
<dd>Write a goroutine blocking profile to the specified file when all tests are complete.<br />
 Writes test binary as -c would.</p>
<dt><code>-blockprofilerate</code><i> n</i></p>
<dd>Control the detail provided in goroutine blocking profiles by calling runtime.SetBlockProfileRate with <i>n</i>.<br />
 See &#8216;go doc runtime.SetBlockProfileRate&#8217;.<br />
 The profiler aims to sample, on average, one blocking event every n nanoseconds the program spends blocked. By default, if -test.blockprofile is set without this flag, all blocking events are recorded, equivalent to -test.blockprofilerate=1.</p>
<dt><code>-coverprofile </code>cover.out</p>
<dd>Write a coverage profile to the file after all tests have passed.<br />
 Sets -cover.</p>
<dt><code>-cpuprofile </code>cpu.out</p>
<dd>Write a CPU profile to the specified file before exiting.<br />
 Writes test binary as -c would.</p>
<dt><code>-memprofile </code>mem.out</p>
<dd>Write an allocation profile to the file after all tests have passed.<br />
 Writes test binary as -c would.</p>
<dt><code>-memprofilerate</code><i> n</i></p>
<dd>Enable more precise (and expensive) memory allocation profiles by setting runtime.MemProfileRate. See &#8216;go doc runtime.MemProfileRate&#8217;. To profile all memory allocations, use -test.memprofilerate=1.</p>
<dt><code>-mutexprofile </code>mutex.out</p>
<dd>Write a mutex contention profile to the specified file when all tests are complete.<br />
 Writes test binary as -c would.</p>
<dt><code>-mutexprofilefraction</code><i> n</i></p>
<dd>Sample 1 in <i>n</i> stack traces of goroutines holding a contended mutex.</p>
<dt><code>-outputdir </code><i>directory</i></p>
<dd>Place output files from profiling in the specified directory, by default the directory in which &quot;go test&quot; is running.</p>
<dt><code>-trace </code>trace.out</p>
<dd>Write an execution trace to the specified file before exiting.</dl>
<p> Each of these flags is also recognized with an optional &#8216;test.&#8217; prefix, as in -test.v. When invoking the generated test binary (the result of &#8216;go test -c&#8217;) directly, however, the prefix is mandatory. </p>
<p> The &#8216;go test&#8217; command rewrites or removes recognized flags, as appropriate, both before and after the optional package list, before invoking the test binary. </p>
<p> For instance, the command </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>go test -v -myflag testdata -cpuprofile=prof.out -x</p>
<p> will compile the test binary and then run it as </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>pkg.test -test.v -myflag testdata -test.cpuprofile=prof.out</p>
<p> (The -x flag is removed because it applies only to the go command&#8217;s execution, not to the test itself.) </p>
<p> The test flags that generate profiles (other than for coverage) also leave the test binary in pkg.test for use when analyzing the profiles. </p>
<p> When &#8216;go test&#8217; runs a test binary, it does so from within the corresponding package&#8217;s source code directory. Depending on the test, it may be necessary to do the same when invoking a generated test binary directly. </p>
<p> The command-line package list, if present, must appear before any flag not known to the go test command. Continuing the example above, the package list would have to appear before -myflag, but could appear on either side of -v. </p>
<p> When &#8216;go test&#8217; runs in package list mode, &#8216;go test&#8217; caches successful package test results to avoid unnecessary repeated running of tests. To disable test caching, use any test flag or argument other than the cacheable flags. The idiomatic way to disable test caching explicitly is to use -count=1. </p>
<p> To keep an argument for a test binary from being interpreted as a known flag or a package name, use -args (see &#8216;go help test&#8217;) which passes the remainder of the command line through to the test binary uninterpreted and unaltered. </p>
<p> For instance, the command </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>go test -v -args -x -v</p>
<p> will compile the test binary and then run it as </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>pkg.test -test.v -x -v</p>
<p> Similarly, </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>go test -args math</p>
<p> will compile the test binary and then run it as </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>pkg.test math</p>
<p> In the first example, the -x and the second -v are passed through to the test binary unchanged and with no effect on the go command itself. In the second example, the argument math is passed through to the test binary, instead of being interpreted as the package list.</p>
<h2>Author</h2>
<p>This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help testflag&#8217; for the Debian project (and may be used by others).</p>
