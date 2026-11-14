---
title: "go(1)"
name: "go"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go/"
description: "go – tool for managing Go source code"
---

<h2 class="name">NAME</h2>
<p> go &#8211; tool for managing Go source code </p>
<h2>SYNOPSIS</h2>
<p> <code>go</code> command [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> The Go distribution includes a command, named <code>go</code>, that automates the downloading, building, installation, and testing of Go packages and commands.</p>
<h2>COMMANDS</h2>
<p> Each command is documented in its own manpage. For example, the <code>build</code> command is documented in <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1). The commands are:</p>
<dl>
<dt><code>bug</code></p>
<dd> start a bug report</p>
<dt><code>build</code></p>
<dd> compile packages and dependencies</p>
<dt><code>clean</code></p>
<dd> remove object files and cached files</p>
<dt><code>doc</code></p>
<dd> show documentation for package or symbol</p>
<dt><code>env</code></p>
<dd> print Go environment information</p>
<dt><code>fix</code></p>
<dd> update packages to use new APIs</p>
<dt><code>fmt</code></p>
<dd> gofmt (reformat) package sources</p>
<dt><code>generate</code></p>
<dd> generate Go files by processing source</p>
<dt><code>get</code></p>
<dd> add dependencies to current module and install them</p>
<dt><code>install</code></p>
<dd> compile and install packages and dependencies</p>
<dt><code>list</code></p>
<dd> list packages or modules</p>
<dt><code>mod</code></p>
<dd> module maintenance</p>
<dt><code>run</code></p>
<dd> compile and run Go program</p>
<dt><code>test</code></p>
<dd> test packages</p>
<dt><code>tool</code></p>
<dd> run specified go tool</p>
<dt><code>version</code></p>
<dd> print Go version</p>
<dt><code>vet</code></p>
<dd> report likely mistakes in packages</dl>
<p> Use &quot;go help &lt;command&gt;&quot; for more information about a command.</p>
<h2>ADDITIONAL HELP TOPICS</h2>
<dl>
<dt><code>buildconstraint</code></p>
<dd> build constraints</p>
<dt><code>buildmode</code></p>
<dd> build modes</p>
<dt><code>c</code></p>
<dd> calling between Go and C</p>
<dt><code>cache</code></p>
<dd> build and test caching</p>
<dt><code>environment</code></p>
<dd> environment variables</p>
<dt><code>filetype</code></p>
<dd> file types</p>
<dt><code>go.mod</code></p>
<dd> the go.mod file</p>
<dt><code>gopath</code></p>
<dd> GOPATH environment variable</p>
<dt><code>gopath-get</code></p>
<dd> legacy GOPATH go get</p>
<dt><code>goproxy</code></p>
<dd> module proxy protocol</p>
<dt><code>importpath</code></p>
<dd> import path syntax</p>
<dt><code>modules</code></p>
<dd> modules, module versions, and more</p>
<dt><code>module-get</code></p>
<dd> module-aware go get</p>
<dt><code>module-auth</code></p>
<dd> module authentication using go.sum</p>
<dt><code>packages</code></p>
<dd> package lists and patterns</p>
<dt><code>private</code></p>
<dd> configuration for downloading non-public code</p>
<dt><code>testflag</code></p>
<dd> testing flags</p>
<dt><code>testfunc</code></p>
<dd> testing functions</p>
<dt><code>vcs</code></p>
<dd> controlling version control with GOVCS</dl>
<p> Use &quot;go help &lt;topic&gt;&quot; for more information about that topic.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1), <code><a href="/docs/linux/man/1-go-clean/">go-clean</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
