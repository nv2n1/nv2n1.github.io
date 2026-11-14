---
title: "go-remote(7)"
name: "go-remote"
section: "7"
letter: "g"
url: "/docs/linux/man/7-go-remote/"
description: "go – tool for managing Go source code"
---

<p>go &#8211; tool for managing Go source code</p>
<h2>Description</h2>
<p>An import path (see <code><a href="/docs/linux/man/1-go-importpath/">go-importpath</a></code>(1)) denotes a package stored in the local file system. Certain import paths also describe how to obtain the source code for the package using a revision control system. A few common code hosting sites have special syntax:</p>
<dl>
<dt><code>BitBucket (Mercurial)</code></p>
<dd>
<pre>import &quot;bitbucket.org/user/project&quot;
import &quot;bitbucket.org/user/project/sub/directory&quot;</pre>
<dt><code>GitHub (Git)</code></p>
<dd>
<pre>import &quot;github.com/user/project&quot;
import &quot;github.com/user/project/sub/directory&quot;</pre>
<dt><code>Google Code Project Hosting (Git, Mercurial, Subversion)</code></p>
<dd>
<pre>import &quot;code.google.com/p/project&quot;
import &quot;code.google.com/p/project/sub/directory&quot;</pre>
<pre>import &quot;code.google.com/p/project.subrepository&quot;
import &quot;code.google.com/p/project.subrepository/sub/directory&quot;</pre>
<dt><code>Launchpad (Bazaar)</code></p>
<dd>
<pre>import &quot;launchpad.net/project&quot;
import &quot;launchpad.net/project/series&quot;
import &quot;launchpad.net/project/series/sub/directory&quot;</pre>
<pre>import &quot;launchpad.net/~user/project/branch&quot;
import &quot;launchpad.net/~user/project/branch/sub/directory&quot;</pre>
<p> For code hosted on other servers, import paths may either be qualified with the version control type, or the go tool can dynamically fetch the import path over https/http and discover where the code resides from a &lt;meta&gt; tag in the HTML. To declare the code location, an import path of the form </p>
<pre> repository.vcs/path</pre>
<p>specifies the given repository, with or without the .vcs suffix, using the named version control system, and then the path inside that repository. The supported version control systems are:</p>
<dl>
<dt><code>Bazaar</code></p>
<dd>&nbsp;.bzr</p>
<dt><code>Git</code></p>
<dd>&nbsp;.git</p>
<dt><code>Mercurial</code></p>
<dd>&nbsp;.hg</p>
<dt><code>Subversion</code></p>
<dd>&nbsp;.svn  For example, </p>
<pre> import &quot;example.org/user/foo.hg&quot;</pre>
<p>denotes the root directory of the Mercurial repository at example.org/user/foo or foo.hg, and </p>
<pre> import &quot;example.org/repo.git/foo/bar&quot;</pre>
<p>denotes the foo/bar directory of the Git repository at example.com/repo or repo.git. When a version control system supports multiple protocols, each is tried in turn when downloading. For example, a Git download tries <a href="git://,">git://,</a> then <a rel="nofollow" href="https://,">https://,</a> then <a rel="nofollow" href="http://.">http://.</a> If the import path is not a known code hosting site and also lacks a version control qualifier, the go tool attempts to fetch the import over https/http and looks for a &lt;meta&gt; tag in the document&#8217;s HTML &lt;head&gt;. The meta tag has the form: </p>
<pre><code>&lt;meta name=&quot;go-import&quot; content=&quot;import-prefix vcs repo-root&quot;&gt;</code></pre>
<p> The import-prefix is the import path corresponding to the repository root. It must be a prefix or an exact match of the package being fetched with &quot;go get&quot;. If it&#8217;s not an exact match, another http request is made at the prefix to verify the &lt;meta&gt; tags match. The vcs is one of &quot;git&quot;, &quot;hg&quot;, &quot;svn&quot;, etc, The repo-root is the root of the version control system containing a scheme and not containing a .vcs qualifier. For example, </p>
<pre> import &quot;example.org/pkg/foo&quot;</pre>
<p>will result in the following request(s): </p>
<pre> <a rel="nofollow" href="https://example.org/pkg/foo?go-get=1">https://example.org/pkg/foo?go-get=1</a> (preferred)
 <a rel="nofollow" href="http://example.org/pkg/foo?go-get=1">http://example.org/pkg/foo?go-get=1</a> (fallback)</pre>
<p>If that page contains the meta tag </p>
<pre> &lt;meta name=&quot;go-import&quot; content=&quot;example.org git <a rel="nofollow" href="https://code.org/r/p/exproj">https://code.org/r/p/exproj</a>&quot;&gt;</pre>
<p>the go tool will verify that <a rel="nofollow" href="https://example.org/?go-get=1">https://example.org/?go-get=1</a> contains the same meta tag and then git clone <a rel="nofollow" href="https://code.org/r/p/exproj">https://code.org/r/p/exproj</a> into GOPATH/src/example.org. New downloaded packages are written to the first directory listed in the GOPATH environment variable (see <code><a href="/docs/linux/man/1-go-path/">go-path</a></code>(1)). The go command attempts to download the version of the package appropriate for the Go release being used. See <code><a href="/docs/linux/man/1-go-install/">go-install</a></code>(1) for more.</p>
<h2>Author</h2>
<p>This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt;, for the Debian project (and may be used by others).</p>
