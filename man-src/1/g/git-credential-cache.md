---
title: "git-credential-cache(1)"
name: "git-credential-cache"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-credential-cache/"
description: "git-credential-cache – Helper to temporarily store passwords in memory"
---

<h2 class="name">NAME</h2>
<p> git-credential-cache &#8211; Helper to temporarily store passwords in memory </p>
<h2>SYNOPSIS</h2>
<pre>
git config credential.helper 'cache [&lt;options&gt;]'
</pre>
<h2>DESCRIPTION</h2>
<p> This command caches credentials in memory for use by future Git programs. The stored credentials never touch the disk, and are forgotten after a configurable timeout. The cache is accessible over a Unix domain socket, restricted to the current user by filesystem permissions. </p>
<p> You probably don&#8217;t want to invoke this command directly; it is meant to be used as a credential helper by other parts of Git. See <code><a href="/docs/linux/man/7-gitcredentials/">gitcredentials</a></code>(7) or <code>EXAMPLES</code> below.</p>
<h2>OPTIONS</h2>
<p> &#8211;timeout &lt;seconds&gt;</p>
<dl>
<dt>
<dd> Number of seconds to cache credentials (default: 900).</dl>
<p> &#8211;socket &lt;path&gt;</p>
<dl>
<dt>
<dd> Use <code>&lt;path&gt;</code> to contact a running cache daemon (or start a new cache daemon if one is not started). Defaults to <code>$XDG_CACHE_HOME/git/credential/socket</code> unless <code>~/.git-credential-cache/</code> exists in which case <code>~/.git-credential-cache/socket</code> is used instead. If your home directory is on a network-mounted filesystem, you may need to change this to a local filesystem. You must specify an absolute path.</dl>
<h2>CONTROLLING THE DAEMON</h2>
<p> If you would like the daemon to exit early, forgetting all cached credentials before their timeout, you can issue an <code>exit</code> action: </p>
<dl>
<dt>
<dd>
<pre>
git credential-cache exit
</pre>
</dl>
<h2>EXAMPLES</h2>
<p> The point of this helper is to reduce the number of times you must type your username or password. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
$ git config credential.helper cache
$ git push http://example.com/repo.git
Username: &lt;type your username&gt;
Password: &lt;type your password&gt;
[work for 5 more minutes]
$ git push http://example.com/repo.git
[your credentials are used automatically]
</code></pre>
</dl>
<p> You can provide options via the credential.helper configuration variable (this example drops the cache time to 5 minutes): </p>
<dl>
<dt>
<dd>
<pre>
$ git config credential.helper 'cache --timeout=300'
</pre>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
