---
title: "go-get(1)"
name: "go-get"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-get/"
description: "go-get – add dependencies to current module and install them"
---

<h2 class="name">NAME</h2>
<p> go-get &#8211; add dependencies to current module and install them </p>
<h2>SYNOPSIS</h2>
<p> <code>go get</code> [-d] [-t] [-u] [-v] [<i>build flags</i>] [<i>packages</i>]</p>
<h2>DESCRIPTION</h2>
<p> Get resolves its command-line arguments to packages at specific module versions, updates go.mod to require those versions, downloads source code into the module cache, then builds and installs the named packages. </p>
<p> To add a dependency for a package or upgrade it to its latest version: </p>
<pre>
        go get example.com/pkg
</pre>
<p> To upgrade or downgrade a package to a specific version: </p>
<pre>
        go get example.com/pkg [at] v1.2.3
</pre>
<p> To remove a dependency on a module and downgrade modules that require it: </p>
<pre>
        go get example.com/mod [at] none
</pre>
<p> See <a rel="nofollow" href="https://golang.org/ref/mod#go-get">https://golang.org/ref/mod#go-get</a> for details. </p>
<p> The &#8216;go install&#8217; command may be used to build and install packages. When a version is specified, &#8216;go install&#8217; runs in module-aware mode and ignores the go.mod file in the current directory. For example: </p>
<pre><code>
go install example.com / pkg[at] v1 .2.3 go install example.com / pkg[at] latest
</code></pre>
<p> See &#8216;go help install&#8217; or <a rel="nofollow" href="https://golang.org/ref/mod#go-install">https://golang.org/ref/mod#go-install</a> for details. </p>
<p> In addition to build flags (listed in &#8216;go help build&#8217;) &#8216;go get&#8217; accepts the following flags.</p>
<dl>
<dt><code>-t</code></p>
<dd> The -t flag instructs get to consider modules needed to build tests of packages specified on the command line.</p>
<dt><code>-u</code></p>
<dd> The -u flag instructs get to update modules providing dependencies of packages named on the command line to use newer minor or patch releases when available.</p>
<dt><code>-u=</code><i>patch</i></p>
<dd> The -u=patch flag (not -u patch) also instructs get to update dependencies, but changes the default to select patch releases.</dl>
<p> When the -t and -u flags are used together, get will update test dependencies as well.</p>
<dl>
<dt><code>-d</code></p>
<dd> The -d flag instructs get not to build or install packages. get will only update go.mod and download source code needed to build packages.</dl>
<p> Building and installing packages with get is deprecated. In a future release, the -d flag will be enabled by default, and &#8216;go get&#8217; will be only be used to adjust dependencies of the current module. To install a package using dependencies from the current module, use &#8216;go install&#8217;. To install a package ignoring the current module, use &#8216;go install&#8217; with an @version suffix like &quot;@latest&quot; after each argument. </p>
<p> For more about modules, see <a rel="nofollow" href="https://golang.org/ref/mod.">https://golang.org/ref/mod.</a> </p>
<p> For more about specifying packages, see <code><a href="/docs/linux/man/7-go-packages/">go-packages</a></code>(7). </p>
<p> This text describes the behavior of get using modules to manage source code and dependencies. If instead the go command is running in GOPATH mode, the details of get&#8217;s flags and effects change, as does &#8216;go help get&#8217;. See &#8216;go help gopath-get&#8217; or <code><a href="/docs/linux/man/1-go-gopath-get/">go-gopath-get</a></code>(1).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1), <code><a href="/docs/linux/man/1-go-install/">go-install</a></code>(1), <code><a href="/docs/linux/man/1-go-clean/">go-clean</a></code>(1). <code><a href="/docs/linux/man/1-go-mod/">go-mod</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help get&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
