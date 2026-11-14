---
title: "git-credential-store(1)"
name: "git-credential-store"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-credential-store/"
description: "git-credential-store – Helper to store credentials on disk"
---

<h2 class="name">NAME</h2>
<p> git-credential-store &#8211; Helper to store credentials on disk </p>
<h2>SYNOPSIS</h2>
<pre>
git config credential.helper 'store [&lt;options&gt;]'
</pre>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> Using this helper will store your passwords unencrypted on disk, protected only by filesystem permissions. If this is not an acceptable security tradeoff, try <code><a href="/docs/linux/man/1-git-credential-cache/">git-credential-cache</a></code>(1), or find a helper that integrates with secure storage provided by your operating system. </p>
</dl>
<p> This command stores credentials indefinitely on disk for use by future Git programs. </p>
<p> You probably don&#8217;t want to invoke this command directly; it is meant to be used as a credential helper by other parts of git. See <code><a href="/docs/linux/man/7-gitcredentials/">gitcredentials</a></code>(7) or <code>EXAMPLES</code> below.</p>
<h2>OPTIONS</h2>
<p> &#8211;file=&lt;path&gt;</p>
<dl>
<dt>
<dd> Use <code>&lt;path&gt;</code> to lookup and store credentials. The file will have its filesystem permissions set to prevent other users on the system from reading it, but will not be encrypted or otherwise protected. If not specified, credentials will be searched for from <code>~/.git-credentials</code> and <code>$XDG_CONFIG_HOME/git/credentials</code>, and credentials will be written to <code>~/.git-credentials</code> if it exists, or <code>$XDG_CONFIG_HOME/git/credentials</code> if it exists and the former does not. See also the section called &#8220;FILES&#8221;.</dl>
<h2>FILES</h2>
<p> If not set explicitly with <code>&#8211;file</code>, there are two files where git-credential-store will search for credentials in order of precedence: </p>
<p> ~/.git-credentials</p>
<dl>
<dt>
<dd> User-specific credentials file.</dl>
<p> $XDG_CONFIG_HOME/git/credentials</p>
<dl>
<dt>
<dd> Second user-specific credentials file. If <i>$XDG_CONFIG_HOME</i> is not set or empty, <code>$HOME/.config/git/credentials</code> will be used. Any credentials stored in this file will not be used if <code>~/.git-credentials</code> has a matching credential as well. It is a good idea not to create this file if you sometimes use older versions of Git that do not support it.</dl>
<p> For credential lookups, the files are read in the order given above, with the first matching credential found taking precedence over credentials found in files further down the list. </p>
<p> Credential storage will by default write to the first existing file in the list. If none of these files exist, <code>~/.git-credentials</code> will be created and written to. </p>
<p> When erasing credentials, matching credentials will be erased from all files.</p>
<h2>EXAMPLES</h2>
<p> The point of this helper is to reduce the number of times you must type your username or password. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
$ git config credential.helper store
    $ git push http : // example.com/repo.git
                      Username : &lt;type your username&gt;
                                     Password : &lt;type your password&gt;[several days later] $ git push http : // example.com/repo.git
                                                                                                           [your credentials are used automatically]
</code></pre>
</dl>
<h2>STORAGE FORMAT</h2>
<p> The <code>.git-credentials</code> file is stored in plaintext. Each credential is stored on its own line as a URL like: </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="https://user:pass@example.com">https://user:pass@example.com</a>
</pre>
</dl>
<p> No other kinds of lines (e.g. empty lines or comment lines) are allowed in the file, even though some may be silently ignored. Do not view or edit the file with editors. </p>
<p> When Git needs authentication for a particular URL context, credential-store will consider that context a pattern to match against each entry in the credentials file. If the protocol, hostname, and username (if we already have one) match, then the password is returned to Git. See the discussion of configuration in <code><a href="/docs/linux/man/7-gitcredentials/">gitcredentials</a></code>(7) for more information.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
