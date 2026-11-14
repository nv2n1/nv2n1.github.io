---
title: "go-version(1)"
name: "go-version"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-version/"
description: "go-version – print the build information for Go executables"
---

<h2 class="name">NAME</h2>
<p> go-version &#8211; print the build information for Go executables </p>
<h2>SYNOPSIS</h2>
<p> <code>go version</code> [<code>-m</code>] [<code>-v</code>] [<i>file &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> Go version reports the Go version used to build each of the named executable files. </p>
<p> If no files are named on the command line, go version prints its own version information. </p>
<p> If a directory is named, go version walks that directory, recursively, looking for recognized Go binaries and reporting their versions. By default, go version does not report unrecognized files found during a directory scan. The -v flag causes it to report unrecognized files. </p>
<p> The -m flag causes go version to print each executable&#8217;s embedded module version information, when available. In the output, the module information consists of multiple lines following the version line, each indented by a leading tab character.</p>
<h2>SEE ALSO</h2>
<p> go doc runtime/debug.BuildInfo.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help version&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
