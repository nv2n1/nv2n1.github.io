---
title: "go-run(1)"
name: "go-run"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-run/"
description: "go-run – compile and run Go program"
---

<h2 class="name">NAME</h2>
<p> go-run &#8211; compile and run Go program </p>
<h2>SYNOPSIS</h2>
<p> <code>go run</code> [<i>build flags</i>] [<code>-exec</code> <i>xprog</i>] <i>package</i> [<i>arguments&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> Run compiles and runs the named main Go package.<br />
 Typically the package is specified as a list of .go source files from a single directory, but it may also be an import path, file system path, or pattern matching a single known package, as in &#8216;go run .&#8217; or &#8216;go run my/cmd&#8217;. </p>
<p> If the package argument has a version suffix (like @latest or @v1.0.0), &quot;go run&quot; builds the program in module-aware mode, ignoring the go.mod file in the current directory or any parent directory, if there is one. This is useful for running programs without affecting the dependencies of the main module. </p>
<p> By default, &#8216;go run&#8217; runs the compiled binary directly: &#8216;a.out arguments&#8230;&#8217;.<br />
 If the -exec flag is given, &#8216;go run&#8217; invokes the binary using xprog: </p>
<pre>
        'xprog a.out arguments...'.
</pre>
<p> If the -exec flag is not given, GOOS or GOARCH is different from the system default, and a program named go_$GOOS_$GOARCH_exec can be found on the current search path, &#8216;go run&#8217; invokes the binary using that program, for example &#8216;go_js_wasm_exec a.out arguments&#8230;&#8217;. This allows execution of cross-compiled programs when a simulator or other execution method is available. </p>
<p> The exit status of Run is not the exit status of the compiled binary. </p>
<p> For more about build flags, see &#8216;go help build&#8217;.<br />
 For more about specifying packages, see &#8216;go help packages&#8217;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help run&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
