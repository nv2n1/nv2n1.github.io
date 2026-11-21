---
title: "go-mod(1)"
name: "go-mod"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-mod/"
description: "go-mod – module maintenance"
---

<h2>SYNOPSIS</h2>
<p> <code>go mod</code> <i>command</i> [<i>arguments</i>]</p>
<h2>DESCRIPTION</h2>
<p> Go mod provides access to operations on modules. </p>
<p> Note that support for modules is built into all the go commands, not just &#8216;go mod&#8217;. For example, day-to-day adding, removing, upgrading, and downgrading of dependencies should be done using &#8216;go get&#8217;. See &#8216;go help modules&#8217; for an overview of module functionality.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>download</code></dt>
<dd> download modules to local cache</dd>
<dt><code>edit</code></dt>
<dd> edit go.mod from tools or scripts</dd>
<dt><code>graph</code></dt>
<dd> print module requirement graph</dd>
<dt><code>init</code></dt>
<dd> initialize new module in current directory</dd>
<dt><code>tidy</code></dt>
<dd> add missing and remove unused modules</dd>
<dt><code>vendor</code></dt>
<dd> make vendored copy of dependencies</dd>
<dt><code>verify</code></dt>
<dd> verify dependencies have expected content</dd>
<dt><code>why</code></dt>
<dd> explain why packages or modules are needed</dd></dl>
<p> Use &quot;go help mod &lt;command&gt;&quot; for more information about a command.</p>
<h2>AUTHOR</h2>
<p> This manual page and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help mod&#8217; for the Debian project (and may be used by others). </p>
