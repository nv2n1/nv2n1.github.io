---
title: "go-gopath-get(1)"
name: "go-gopath-get"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-gopath-get/"
description: "go-get – legacy GOPATH go get"
---

<h2 class="name">NAME</h2>
<p> go-get &#8211; legacy GOPATH go get </p>
<h2>SYNOPSIS</h2>
<p> The &#8216;go get&#8217; command changes behavior depending on whether the go command is running in module-aware mode or legacy GOPATH mode. This help text, accessible as &#8216;go help gopath-get&#8217; even in module-aware mode, describes &#8216;go get&#8217; as it operates in legacy GOPATH mode. </p>
<p> <code>go get</code> [-d] [-f] [-t] [-u] [-v] [-fix] [<i>build flags</i>] [<i>packages</i>]</p>
<h2>DESCRIPTION</h2>
<p> Get downloads the packages named by the import paths, along with their dependencies. It then installs the named packages, like &#8216;go install&#8217;.</p>
<dl>
<dt><code>-d</code></p>
<dd> The -d flag instructs get to stop after downloading the packages; that is, it instructs get not to install the packages.</p>
<dt><code>-f</code></p>
<dd> The -f flag, valid only when -u is set, forces get -u not to verify that each package has been checked out from the source control repository implied by its import path. This can be useful if the source is a local fork of the original.</p>
<dt><code>-fix</code></p>
<dd> The -fix flag instructs get to run the fix tool on the downloaded packages before resolving dependencies or building the code.</p>
<dt><code>-t</code></p>
<dd> The -t flag instructs get to also download the packages required to build the tests for the specified packages.</p>
<dt><code>-u</code></p>
<dd> The -u flag instructs get to use the network to update the named packages and their dependencies. By default, get uses the network to check out missing packages but does not use it to look for updates to existing packages.</p>
<dt><code>-v</code></p>
<dd> The -v flag enables verbose progress and debug output.</dl>
<p> Get also accepts build flags to control the installation. See <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1). </p>
<p> When checking out a new package, get creates the target directory GOPATH/src/&lt;import-path&gt;. If the GOPATH contains multiple entries, get uses the first one. For more details see: &#8216;go help gopath&#8217;. </p>
<p> When checking out or updating a package, get looks for a branch or tag that matches the locally installed version of Go. The most important rule is that if the local installation is running version &quot;go1&quot;, get searches for a branch or tag named &quot;go1&quot;. If no such version exists it retrieves the default branch of the package. </p>
<p> When go get checks out or updates a Git repository, it also updates any git submodules referenced by the repository. </p>
<p> Get never checks out or updates code stored in vendor directories. </p>
<p> For more about specifying packages, see <code><a href="/docs/linux/man/7-go-packages/">go-packages</a></code>(7). </p>
<p> For more about how &#8216;go get&#8217; finds source code to download, see <code><a href="/docs/linux/man/7-go-remote/">go-remote</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1), <code><a href="/docs/linux/man/1-go-install/">go-install</a></code>(1), <code><a href="/docs/linux/man/1-go-clean/">go-clean</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help gopath-get&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
