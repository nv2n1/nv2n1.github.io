---
title: "go-vet(1)"
name: "go-vet"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-vet/"
description: "go-vet – report likely mistakes in packages"
---

<h2 class="name">NAME</h2>
<p> go-vet &#8211; report likely mistakes in packages </p>
<h2>SYNOPSIS</h2>
<p> <code>go vet</code> [<code>-n</code>] [<code>-x</code>] [<code>-vettool</code> <i>prog</i>] [<i>build flags</i>] [<i>vet flags</i>] [<i>packages</i>]</p>
<h2>DESCRIPTION</h2>
<p> Vet runs the Go vet command on the packages named by the import paths. </p>
<p> For more about vet and its flags, see &#8216;go doc cmd/vet&#8217;.<br />
 For more about specifying packages, see <code><a href="/docs/linux/man/7-go-packages/">go-packages</a></code>(7).<br />
 For a list of checkers and their flags, see &#8216;go tool vet help&#8217;.<br />
 For details of a specific checker such as &#8216;printf&#8217;, see &#8216;go tool vet help printf&#8217;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code></p>
<dd> The -n flag prints commands that would be executed.</p>
<dt><code>-x</code></p>
<dd> The -x flag prints commands as they are executed.</p>
<dt><code>-vettool=</code><i>prog</i></p>
<dd> The -vettool=prog flag selects a different analysis tool with alternative or additional checks.<br />
 For example, the &#8216;shadow&#8217; analyzer can be built and run using these commands: </p>
<pre>
  go install golang.org/x/tools/go/analysis/passes/shadow/cmd/shadow
  go vet -vettool=$(which shadow)
</pre>
</dl>
<p> The build flags supported by go vet are those that control package resolution and execution, such as -n, -x, -v, -tags, and -toolexec. For more about these flags, see &#8216;go help build&#8217;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-go-fmt/">go-fmt</a></code>(1), <code><a href="/docs/linux/man/1-go-fix/">go-fix</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help vet&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
