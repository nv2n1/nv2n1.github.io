---
title: "go-fmt(1)"
name: "go-fmt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-fmt/"
description: "go-fmt – gofmt (reformat) package sources"
---

<h2 class="name">NAME</h2>
<p> go-fmt &#8211; gofmt (reformat) package sources </p>
<h2>SYNOPSIS</h2>
<p> <code>go fmt</code> [<code>-n</code>] [<code>-x</code>] [<i>packages</i>]</p>
<h2>DESCRIPTION</h2>
<p> Fmt runs the command &#8216;gofmt -l -w&#8217; on the packages named by the import paths. It prints the names of the files that are modified. </p>
<p> For more about gofmt, see &#8216;go doc cmd/gofmt&#8217;.<br />
 For more about specifying packages, see <code><a href="/docs/linux/man/7-go-packages/">go-packages</a></code>(7).</p>
<dl>
<dt><code>-n</code></p>
<dd> The -n flag prints commands that would be executed.</p>
<dt><code>-x</code></p>
<dd> The -x flag prints commands as they are executed.</p>
<dt><code>-mod</code></p>
<dd> The -mod flag&#8217;s value sets which module download mode to use: readonly or vendor. See &#8216;go help modules&#8217; for more.</dl>
<p> To run gofmt with specific options, run gofmt itself.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-go-fix/">go-fix</a></code>(1), <code><a href="/docs/linux/man/1-go-vet/">go-vet</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help fmt&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
