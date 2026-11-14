---
title: "git-ls-remote(1)"
name: "git-ls-remote"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-ls-remote/"
description: "git-ls-remote – List references in a remote repository"
---

<h2 class="name">NAME</h2>
<p> git-ls-remote &#8211; List references in a remote repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
git ls - remote[--heads][--tags][--refs][--upload - pack = &lt;exec&gt;]
               [-q | --quiet][--exit - code][--get - url][--sort = &lt;key&gt;]
               [--symref][&lt;repository&gt;[&lt;refs&gt;...]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Displays references available in a remote repository along with the associated commit IDs.</p>
<h2>OPTIONS</h2>
<p> -h, &#8211;heads, -t, &#8211;tags</p>
<dl>
<dt>
<dd> Limit to only refs/heads and refs/tags, respectively. These options are <i>not</i> mutually exclusive; when given both, references stored in refs/heads and refs/tags are displayed. Note that <code>git ls-remote -h</code> used without anything else on the command line gives help, consistent with other git subcommands.</dl>
<p> &#8211;refs</p>
<dl>
<dt>
<dd> Do not show peeled tags or pseudorefs like <code>HEAD</code> in the output.</dl>
<p> -q, &#8211;quiet</p>
<dl>
<dt>
<dd> Do not print remote URL to stderr.</dl>
<p> &#8211;upload-pack=&lt;exec&gt;</p>
<dl>
<dt>
<dd> Specify the full path of <i>git-upload-pack</i> on the remote host. This allows listing references from repositories accessed via SSH and where the SSH daemon does not use the PATH configured by the user.</dl>
<p> &#8211;exit-code</p>
<dl>
<dt>
<dd> Exit with status &quot;2&quot; when no matching refs are found in the remote repository. Usually the command exits with status &quot;0&quot; to indicate it successfully talked with the remote repository, whether it found any matching refs.</dl>
<p> &#8211;get-url</p>
<dl>
<dt>
<dd> Expand the URL of the given remote repository taking into account any &quot;url.&lt;base&gt;.insteadOf&quot; config setting (See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)) and exit without talking to the remote.</dl>
<p> &#8211;symref</p>
<dl>
<dt>
<dd> In addition to the object pointed by it, show the underlying ref pointed by it when showing a symbolic ref. Currently, upload-pack only shows the symref HEAD, so it will be the only one shown by ls-remote.</dl>
<p> &#8211;sort=&lt;key&gt;</p>
<dl>
<dt>
<dd> Sort based on the key given. Prefix <code>&#8211;</code> to sort in descending order of the value. Supports &quot;version:refname&quot; or &quot;v:refname&quot; (tag names are treated as versions). The &quot;version:refname&quot; sort order can also be affected by the &quot;versionsort.suffix&quot; configuration variable. See <code><a href="/docs/linux/man/1-git-for-each-ref/">git-for-each-ref</a></code>(1) for more sort options, but be aware keys like <code>committerdate</code> that require access to the objects themselves will not work for refs whose objects have not yet been fetched from the remote, and will give a <code>missing object</code> error.</dl>
<p> -o &lt;option&gt;, &#8211;server-option=&lt;option&gt;</p>
<dl>
<dt>
<dd> Transmit the given string to the server when communicating using protocol version 2. The given string must not contain a NUL or LF character. When multiple <code>&#8211;server-option=&lt;option&gt;</code> are given, they are all sent to the other side in the order listed on the command line.</dl>
<p> &lt;repository&gt;</p>
<dl>
<dt>
<dd> The &quot;remote&quot; repository to query. This parameter can be either a URL or the name of a remote (see the GIT URLS and REMOTES sections of <code><a href="/docs/linux/man/1-git-fetch/">git-fetch</a></code>(1)).</dl>
<p> &lt;refs&gt;&#8230;</p>
<dl>
<dt>
<dd> When unspecified, all references, after filtering done with &#8211;heads and &#8211;tags, are shown. When &lt;refs&gt;&#8230; are specified, only references matching the given patterns are displayed.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ git ls-remote --tags ./.
d6602ec5194c87b0fc87103ca4d67251c76f233a        refs/tags/v0.99
f25a265a342aed6041ab0cc484224d9ca54b6f41        refs/tags/v0.99.1
7ceca275d047c90c0c7d5afb13ab97efdf51bd6e        refs/tags/v0.99.3
c5db5456ae3b0873fc659c19fafdde22313cc441        refs/tags/v0.99.2
0918385dbd9656cab0d1d81ba7453d49bbc16250        refs/tags/junio-gpg-pub
$ git ls-remote <a rel="nofollow" href="http://www.kernel.org/pub/scm/git/git.git">http://www.kernel.org/pub/scm/git/git.git</a> master seen rc
5fe978a5381f1fbad26a80e682ddd2a401966740        refs/heads/master
c781a84b5204fb294c9ccc79f8b3baceeb32c061        refs/heads/seen
$ git remote add korg <a rel="nofollow" href="http://www.kernel.org/pub/scm/git/git.git">http://www.kernel.org/pub/scm/git/git.git</a>
$ git ls-remote --tags korg v\*
d6602ec5194c87b0fc87103ca4d67251c76f233a        refs/tags/v0.99
f25a265a342aed6041ab0cc484224d9ca54b6f41        refs/tags/v0.99.1
c5db5456ae3b0873fc659c19fafdde22313cc441        refs/tags/v0.99.2
7ceca275d047c90c0c7d5afb13ab97efdf51bd6e        refs/tags/v0.99.3
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-check-ref-format/">git-check-ref-format</a></code>(1).</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
