---
title: "go-mod(1)"
name: "go-mod"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-mod/"
description: "go-mod – module maintenance"
---

<h2 class="name">NAME</h2>
<p> go-mod &#8211; module maintenance </p>
<h2>SYNOPSIS</h2>
<p> <code>go mod</code> <i>command</i> [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> Go mod provides access to operations on modules. </p>
<p> Note that support for modules is built into all the go commands, not just &#8216;go mod&#8217;. For example, day-to-day adding, removing, upgrading, and downgrading of dependencies should be done using &#8216;go get&#8217;. See &#8216;go help modules&#8217; for an overview of module functionality.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>download</code></p>
<dd> download modules to local cache</p>
<dt><code>edit</code></p>
<dd> edit go.mod from tools or scripts</p>
<dt><code>graph</code></p>
<dd> print module requirement graph</p>
<dt><code>init</code></p>
<dd> initialize new module in current directory</p>
<dt><code>tidy</code></p>
<dd> add missing and remove unused modules</p>
<dt><code>vendor</code></p>
<dd> make vendored copy of dependencies</p>
<dt><code>verify</code></p>
<dd> verify dependencies have expected content</p>
<dt><code>why</code></p>
<dd> explain why packages or modules are needed</dl>
<p> Use &quot;go help mod &lt;command&gt;&quot; for more information about a command.</p>
<h2>AUTHOR</h2>
<p> This manual page and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help mod&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
