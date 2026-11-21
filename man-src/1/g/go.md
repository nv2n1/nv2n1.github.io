---
title: "go(1)"
name: "go"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go/"
description: "go – tool for managing Go source code"
---

<h2>SYNOPSIS</h2>
<p> <code>go</code> command [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> The Go distribution includes a command, named <code>go</code>, that automates the downloading, building, installation, and testing of Go packages and commands.</p>
<h2>COMMANDS</h2>
<p> Each command is documented in its own manpage. For example, the <code>build</code> command is documented in <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1). The commands are:</p>
<dl>
<dt><code>bug</code></dt>
<dd> start a bug report</dd>
<dt><code>build</code></dt>
<dd> compile packages and dependencies</dd>
<dt><code>clean</code></dt>
<dd> remove object files and cached files</dd>
<dt><code>doc</code></dt>
<dd> show documentation for package or symbol</dd>
<dt><code>env</code></dt>
<dd> print Go environment information</dd>
<dt><code>fix</code></dt>
<dd> update packages to use new APIs</dd>
<dt><code>fmt</code></dt>
<dd> gofmt (reformat) package sources</dd>
<dt><code>generate</code></dt>
<dd> generate Go files by processing source</dd>
<dt><code>get</code></dt>
<dd> add dependencies to current module and install them</dd>
<dt><code>install</code></dt>
<dd> compile and install packages and dependencies</dd>
<dt><code>list</code></dt>
<dd> list packages or modules</dd>
<dt><code>mod</code></dt>
<dd> module maintenance</dd>
<dt><code>run</code></dt>
<dd> compile and run Go program</dd>
<dt><code>test</code></dt>
<dd> test packages</dd>
<dt><code>tool</code></dt>
<dd> run specified go tool</dd>
<dt><code>version</code></dt>
<dd> print Go version</dd>
<dt><code>vet</code></dt>
<dd> report likely mistakes in packages</dd></dl>
<p> Use &quot;go help &lt;command&gt;&quot; for more information about a command.</p>
<h2>ADDITIONAL HELP TOPICS</h2>
<dl>
<dt><code>buildconstraint</code></dt>
<dd> build constraints</dd>
<dt><code>buildmode</code></dt>
<dd> build modes</dd>
<dt><code>c</code></dt>
<dd> calling between Go and C</dd>
<dt><code>cache</code></dt>
<dd> build and test caching</dd>
<dt><code>environment</code></dt>
<dd> environment variables</dd>
<dt><code>filetype</code></dt>
<dd> file types</dd>
<dt><code>go.mod</code></dt>
<dd> the go.mod file</dd>
<dt><code>gopath</code></dt>
<dd> GOPATH environment variable</dd>
<dt><code>gopath-get</code></dt>
<dd> legacy GOPATH go get</dd>
<dt><code>goproxy</code></dt>
<dd> module proxy protocol</dd>
<dt><code>importpath</code></dt>
<dd> import path syntax</dd>
<dt><code>modules</code></dt>
<dd> modules, module versions, and more</dd>
<dt><code>module-get</code></dt>
<dd> module-aware go get</dd>
<dt><code>module-auth</code></dt>
<dd> module authentication using go.sum</dd>
<dt><code>packages</code></dt>
<dd> package lists and patterns</dd>
<dt><code>private</code></dt>
<dd> configuration for downloading non-public code</dd>
<dt><code>testflag</code></dt>
<dd> testing flags</dd>
<dt><code>testfunc</code></dt>
<dd> testing functions</dd>
<dt><code>vcs</code></dt>
<dd> controlling version control with GOVCS</dd></dl>
<p> Use &quot;go help &lt;topic&gt;&quot; for more information about that topic.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1), <code><a href="/docs/linux/man/1-go-clean/">go-clean</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help&#8217; for the Debian project (and may be used by others). </p>
