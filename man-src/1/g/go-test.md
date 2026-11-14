---
title: "go-test(1)"
name: "go-test"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-test/"
description: "go-test – test packages"
---

<h2 class="name">NAME</h2>
<p> go-test &#8211; test packages </p>
<h2>SYNOPSIS</h2>
<p> <code>go test</code> [<i>build/test flags</i>] [<i>packages</i>] [<i>build/test flags &amp; test binary flags</i>]</p>
<h2>DESCRIPTION</h2>
<p> &quot;Go test&quot; automates testing the packages named by the import paths. It prints a summary of the test results in the format: </p>
<pre>
      ok   archive/tar   0.011s
      FAIL archive/zip   0.022s
      ok   compress/gzip 0.033s
      ...
</pre>
<p> followed by detailed output for each failed package. </p>
<p> &quot;Go test&quot; recompiles each package along with any files with names matching the file pattern &quot;*_test.go&quot;. These additional files can contain test functions, benchmark functions, and example functions. See &#8216;go help testfunc&#8217; for more.<br />
 Each listed package causes the execution of a separate test binary. Files whose names begin with &quot;_&quot; (including &quot;_test.go&quot;) or &quot;.&quot; are ignored. </p>
<p> Test files that declare a package with the suffix &quot;_test&quot; will be compiled as a separate package, and then linked and run with the main test binary. </p>
<p> The go tool will ignore a directory named &quot;testdata&quot;, making it available to hold ancillary data needed by the tests. </p>
<p> As part of building a test binary, go test runs go vet on the package and its test source files to identify significant problems. If go vet finds any problems, go test reports those and does not run the test binary. Only a high-confidence subset of the default go vet checks are used. That subset is: &#8216;atomic&#8217;, &#8216;bool&#8217;, &#8216;buildtags&#8217;, &#8216;errorsas&#8217;, &#8216;ifaceassert&#8217;, &#8216;nilfunc&#8217;, &#8216;printf&#8217;, and &#8216;stringintconv&#8217;. You can see the documentation for these and other vet tests via &quot;go doc cmd/vet&quot;. To disable the running of go vet, use the -vet=off flag. </p>
<p> All test output and summary lines are printed to the go command&#8217;s standard output, even if the test printed them to its own standard error. (The go command&#8217;s standard error is reserved for printing errors building the tests.) </p>
<p> Go test runs in two different modes: </p>
<p> The first, called local directory mode, occurs when go test is invoked with no package arguments (for example, &#8216;go test&#8217; or &#8216;go test -v&#8217;). In this mode, go test compiles the package sources and tests found in the current directory and then runs the resulting test binary. In this mode, caching (discussed below) is disabled. After the package test finishes, go test prints a summary line showing the test status (&#8216;ok&#8217; or &#8216;FAIL&#8217;), package name, and elapsed time. </p>
<p> The second, called package list mode, occurs when go test is invoked with explicit package arguments (for example &#8216;go test math&#8217;, &#8216;go test ./&#8230;&#8217;, and even &#8216;go test .&#8217;). In this mode, go test compiles and tests each of the packages listed on the command line. If a package test passes, go test prints only the final &#8216;ok&#8217; summary line. If a package test fails, go test prints the full test output. If invoked with the -bench or -v flag, go test prints the full output even for passing package tests, in order to display the requested benchmark results or verbose logging. After the package tests for all of the listed packages finish, and their output is printed, go test prints a final &#8216;FAIL&#8217; status if any package test has failed. </p>
<p> In package list mode only, go test caches successful package test results to avoid unnecessary repeated running of tests. When the result of a test can be recovered from the cache, go test will redisplay the previous output instead of running the test binary again. When this happens, go test prints &#8216;(cached)&#8217; in place of the elapsed time in the summary line. </p>
<p> The rule for a match in the cache is that the run involves the same test binary and the flags on the command line come entirely from a restricted set of &#8216;cacheable&#8217; test flags, defined as -benchtime, -cpu, -list, -parallel, -run, -short, and -v. If a run of go test has any test or non-test flags outside this set, the result is not cached. To disable test caching, use any test flag or argument other than the cacheable flags. The idiomatic way to disable test caching explicitly is to use -count=1. Tests that open files within the package&#8217;s source root (usually $GOPATH) or that consult environment variables only match future runs in which the files and environment variables are unchanged. A cached test result is treated as executing in no time at all, so a successful package test result will be cached and reused regardless of -timeout setting.</p>
<h2>OPTIONS</h2>
<p> In addition to the build flags, the flags handled by &#8216;go test&#8217; itself are:</p>
<dl>
<dt><code>-args</code></p>
<dd> Pass the remainder of the command line (everything after -args) to the test binary, uninterpreted and unchanged. Because this flag consumes the remainder of the command line, the package list (if present) must appear before this flag.</p>
<dt><code>-c</code></p>
<dd> Compile the test binary to pkg.test but do not run it (where pkg is the last element of the package&#8217;s import path). The file name can be changed with the -o flag.</p>
<dt><code>-exec </code><i>xprog</i></p>
<dd> Run the test binary using xprog. The behavior is the same as in &#8216;go run&#8217;. See &#8216;go help run&#8217; for details.</p>
<dt><code>-i</code></p>
<dd> Install packages that are dependencies of the test. Do not run the test.</p>
<dt><code>-json</code></p>
<dd> Convert test output to JSON suitable for automated processing. See &#8216;go doc test2json&#8217; for the encoding details.</p>
<dt><code>-o </code><i>file</i></p>
<dd> Compile the test binary to the named file. The test still runs (unless -c or -i is specified).</dl>
<p> The test binary also accepts flags that control execution of the test; these flags are also accessible by &#8216;go test&#8217;. See <code><a href="/docs/linux/man/7-go-testflag/">go-testflag</a></code>(7) for details. </p>
<p> For more about build flags, see <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1). </p>
<p> For more about specifying packages, see <code><a href="/docs/linux/man/7-go-packages/">go-packages</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1), <code><a href="/docs/linux/man/1-go-vet/">go-vet</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help test&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
