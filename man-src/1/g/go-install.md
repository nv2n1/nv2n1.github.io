---
title: "go-install(1)"
name: "go-install"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-install/"
description: "go – tool for managing Go source code"
---

<h2 class="name">NAME</h2>
<p> go &#8211; tool for managing Go source code </p>
<h2>SYNOPSIS</h2>
<p> <code>go install</code> [<i>build flags</i>] [<i>packages</i>]</p>
<h2>DESCRIPTION</h2>
<p> Install compiles and installs the packages named by the import paths. </p>
<p> Executables are installed in the directory named by the GOBIN environment variable, which defaults to $GOPATH/bin or $HOME/go/bin if the GOPATH environment variable is not set. Executables in $GOROOT are installed in $GOROOT/bin or $GOTOOLDIR instead of $GOBIN. </p>
<p> If the arguments have version suffixes (like @latest or @v1.0.0), &quot;go install&quot; builds packages in module-aware mode, ignoring the go.mod file in the current directory or any parent directory, if there is one. This is useful for installing executables without affecting the dependencies of the main module. To eliminate ambiguity about which module versions are used in the build, the arguments must satisfy the following constraints:</p>
<dl>
<dt>&bull;</p>
<dd> Arguments must be package paths or package patterns (with &quot;&#8230;&quot; wildcards). They must not be standard packages (like fmt), meta-patterns (std, cmd, all), or relative or absolute file paths.</p>
<dt>&bull;</p>
<dd> All arguments must have the same version suffix. Different queries are not allowed, even if they refer to the same version.</p>
<dt>&bull;</p>
<dd> All arguments must refer to packages in the same module at the same version.</p>
<dt>&bull;</p>
<dd> No module is considered the &quot;main&quot; module. If the module containing packages named on the command line has a go.mod file, it must not contain directives (replace and exclude) that would cause it to be interpreted differently than if it were the main module. The module must not require a higher version of itself.</p>
<dt>&bull;</p>
<dd> Package path arguments must refer to main packages. Pattern arguments will only match main packages.</dl>
<p> If the arguments don&#8217;t have version suffixes, &quot;go install&quot; may run in module-aware mode or GOPATH mode, depending on the GO111MODULE environment variable and the presence of a go.mod file. See &#8216;go help modules&#8217; for details. If module-aware mode is enabled, &quot;go install&quot; runs in the context of the main module. </p>
<p> When module-aware mode is disabled, other packages are installed in the directory $GOPATH/pkg/$GOOS_$GOARCH. When module-aware mode is enabled, other packages are built and cached but not installed. </p>
<p> The -i flag installs the dependencies of the named packages as well.<br />
 The -i flag is deprecated. Compiled packages are cached automatically. </p>
<p> For more about the build flags, see <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1).<br />
 For more about specifying packages, see <code><a href="/docs/linux/man/7-go-packages/">go-packages</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1), <code><a href="/docs/linux/man/1-go-get/">go-get</a></code>(1), <code><a href="/docs/linux/man/1-go-clean/">go-clean</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help install&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
