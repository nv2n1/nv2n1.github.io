---
title: "gitcredentials(7)"
name: "gitcredentials"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gitcredentials/"
description: "gitcredentials – Providing usernames and passwords to Git"
---

<p>gitcredentials &#8211; Providing usernames and passwords to Git</p>
<h2>Synopsis</h2>
<pre>git config credential.<a rel="nofollow" href="https://example.com.username">https://example.com.username</a> myusername
git config credential.helper &quot;$helper $options&quot;</pre>
<h2>Description</h2>
<p>Git will sometimes need credentials from the user in order to perform operations; for example, it may need to ask for a username and password in order to access a remote repository over HTTP. This manual describes the mechanisms Git uses to request these credentials, as well as some features to avoid inputting these credentials repeatedly.</p>
<h2>Requesting Credentials</h2>
<p>Without any credential helpers defined, Git will try the following strategies to ask the user for usernames and passwords: </p>
<dl>
<dd>1. If the <code>GIT_ASKPASS</code> environment variable is set, the program specified by the variable is invoked. A suitable prompt is provided to the program on the command line, and the user&#8217;s input is read from its standard output.</dl>
<dl>
<dd>2. Otherwise, if the <code>core.askPass</code> configuration variable is set, its value is used as above.</dl>
<dl>
<dd>3. Otherwise, if the <code>SSH_ASKPASS</code> environment variable is set, its value is used as above.</dl>
<dl>
<dd>4. Otherwise, the user is prompted on the terminal.</dl>
<h2>Avoiding Repetition</h2>
<p>It can be cumbersome to input the same credentials over and over. Git provides two methods to reduce this annoyance: </p>
<dl>
<dd>1. Static configuration of usernames for a given authentication context.</dl>
<dl>
<dd>2. Credential helpers to cache or store passwords, or to interact with a system password wallet or keychain.</dl>
<p> The first is simple and appropriate if you do not have secure storage available for a password. It is generally configured by adding this to your config: </p>
<dl>
<dd>
<pre>[credential &quot;<a rel="nofollow" href="https://example.com">https://example.com</a>&quot;]
 username = me</pre>
</dl>
<p> Credential helpers, on the other hand, are external programs from which Git can request both usernames and passwords; they typically interface with secure storage provided by the OS or other programs. </p>
<p> To use a helper, you must first select one to use. Git currently includes the following helpers: </p>
<p> cache</p>
<dl>
<dd>Cache credentials in memory for a short period of time. See <code><a href="/docs/linux/man/1-git-credential-cache/">git-credential-cache</a></code>(1) for details.</dl>
<p> store</p>
<dl>
<dd>Store credentials indefinitely on disk. See <code><a href="/docs/linux/man/1-git-credential-store/">git-credential-store</a></code>(1) for details.</dl>
<p> You may also have third-party helpers installed; search for <code>credential-*</code> in the output of <code>git help -a</code>, and consult the documentation of individual helpers. Once you have selected a helper, you can tell Git to use it by putting its name into the credential.helper variable. </p>
<dl>
<dd>1. Find a helper. </p>
<dl>
<dd>
<pre>$ git help -a | grep credential-
credential-foo</pre>
</dl>
</dl>
<dl>
<dd>2. Read its description. </p>
<dl>
<dd>
<pre>$ git help credential-foo</pre>
</dl>
</dl>
<dl>
<dd>3. Tell Git to use it. </p>
<dl>
<dd>
<pre>$ git config --global credential.helper foo</pre>
</dl>
</dl>
<h2>Credential Contexts</h2>
<p>Git considers each credential to have a context defined by a URL. This context is used to look up context-specific configuration, and is passed to any helpers, which may use it as an index into secure storage. </p>
<p> For instance, imagine we are accessing <code><a rel="nofollow" href="https://example.com/foo.git">https://example.com/foo.git</a></code>. When Git looks into a config file to see if a section matches this context, it will consider the two a match if the context is a more-specific subset of the pattern in the config file. For example, if you have this in your config file: </p>
<dl>
<dd>
<pre>[credential &quot;<a rel="nofollow" href="https://example.com">https://example.com</a>&quot;]
 username = foo</pre>
</dl>
<p> then we will match: both protocols are the same, both hosts are the same, and the &quot;pattern&quot; URL does not care about the path component at all. However, this context would not match: </p>
<dl>
<dd>
<pre>[credential &quot;<a rel="nofollow" href="https://kernel.org">https://kernel.org</a>&quot;]
 username = foo</pre>
</dl>
<p> because the hostnames differ. Nor would it match <code>foo.example.com</code>; Git compares hostnames exactly, without considering whether two hosts are part of the same domain. Likewise, a config entry for <code><a rel="nofollow" href="http://example.com">http://example.com</a></code> would not match: Git compares the protocols exactly. However, you may use wildcards in the domain name and other pattern matching techniques as with the <code>http.&lt;url&gt;.*</code> options. </p>
<p> If the &quot;pattern&quot; URL does include a path component, then this too must match exactly: the context <code><a rel="nofollow" href="https://example.com/bar/baz.git">https://example.com/bar/baz.git</a></code> will match a config entry for <code><a rel="nofollow" href="https://example.com/bar/baz.git">https://example.com/bar/baz.git</a></code> (in addition to matching the config entry for <code><a rel="nofollow" href="https://example.com">https://example.com</a></code>) but will not match a config entry for <code><a rel="nofollow" href="https://example.com/bar">https://example.com/bar</a></code>.</p>
<h2>Configuration Options</h2>
<p>Options for a credential context can be configured either in <code>credential.*</code> (which applies to all credentials), or <code>credential.&lt;url&gt;.*</code>, where &lt;url&gt; matches the context as described above. </p>
<p> The following options are available in either location: </p>
<p> helper</p>
<dl>
<dd>The name of an external credential helper, and any associated options. If the helper name is not an absolute path, then the string <code>git credential-</code> is prepended. The resulting string is executed by the shell (so, for example, setting this to <code>foo &#8211;option=bar</code> will execute <code>git credential-foo &#8211;option=bar</code> via the shell. See the manual of specific helpers for examples of their use. </p>
<p> If there are multiple instances of the <code>credential.helper</code> configuration variable, each helper will be tried in turn, and may provide a username, password, or nothing. Once Git has acquired both a username and a password, no more helpers will be tried. </p>
<p> If <code>credential.helper</code> is configured to the empty string, this resets the helper list to empty (so you may override a helper set by a lower-priority config file by configuring the empty-string helper, followed by whatever set of helpers you would like).</dl>
<p> username</p>
<dl>
<dd>A default username, if one is not provided in the URL.</dl>
<p> useHttpPath</p>
<dl>
<dd>By default, Git does not consider the &quot;path&quot; component of an http URL to be worth matching via external helpers. This means that a credential stored for <code><a rel="nofollow" href="https://example.com/foo.git">https://example.com/foo.git</a></code> will also be used for <code><a rel="nofollow" href="https://example.com/bar.git">https://example.com/bar.git</a></code>. If you do want to distinguish these cases, set this option to <code>true</code>.</dl>
<h2>Custom Helpers</h2>
<p>You can write your own custom helpers to interface with any system in which you keep credentials. </p>
<p> Credential helpers are programs executed by Git to fetch or save credentials from and to long-term storage (where &quot;long-term&quot; is simply longer than a single Git process; e.g., credentials may be stored in-memory for a few minutes, or indefinitely on disk). </p>
<p> Each helper is specified by a single string in the configuration variable <code>credential.helper</code> (and others, see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)). The string is transformed by Git into a command to be executed using these rules: </p>
<dl>
<dd>1. If the helper string begins with &quot;!&quot;, it is considered a shell snippet, and everything after the &quot;!&quot; becomes the command.</dl>
<dl>
<dd>2. Otherwise, if the helper string begins with an absolute path, the verbatim helper string becomes the command.</dl>
<dl>
<dd>3. Otherwise, the string &quot;git credential-&quot; is prepended to the helper string, and the result becomes the command.</dl>
<p> The resulting command then has an &quot;operation&quot; argument appended to it (see below for details), and the result is executed by the shell. </p>
<p> Here are some example specifications: </p>
<dl>
<dd>
<pre># run &quot;git credential-foo&quot;
[credential]
 helper = foo
# same as above, but pass an argument to the helper
[credential]
 helper = &quot;foo --bar=baz&quot;
# the arguments are parsed by the shell, so use shell
# quoting if necessary
[credential]
 helper = &quot;foo --bar='whitespace arg'&quot;
# you can also use an absolute path, which will not use the git wrapper
[credential]
 helper = &quot;/path/to/my/helper --with-arguments&quot;
# or you can specify your own shell snippet
[credential &quot;<a rel="nofollow" href="https://example.com">https://example.com</a>&quot;]
 username = your_user
 helper = &quot;!f() { test \&quot;$1\&quot; = get &amp;&amp; echo \&quot;password=$(cat $HOME/.secret)\&quot;; }; f&quot;</pre>
</dl>
<p> Generally speaking, rule (3) above is the simplest for users to specify. Authors of credential helpers should make an effort to assist their users by naming their program &quot;git-credential-$NAME&quot;, and putting it in the <code>$PATH</code> or <code>$GIT_EXEC_PATH</code> during installation, which will allow a user to enable it with <code>git config credential.helper $NAME</code>. </p>
<p> When a helper is executed, it will have one &quot;operation&quot; argument appended to its command line, which is one of: </p>
<p> <code>get</code></p>
<dl>
<dd>Return a matching credential, if any exists.</dl>
<p> <code>store</code></p>
<dl>
<dd>Store the credential, if applicable to the helper.</dl>
<p> <code>erase</code></p>
<dl>
<dd>Remove a matching credential, if any, from the helper&#8217;s storage.</dl>
<p> The details of the credential will be provided on the helper&#8217;s stdin stream. The exact format is the same as the input/output format of the <code>git credential</code> plumbing command (see the section <code>INPUT/OUTPUT FORMAT</code> in <code><a href="/docs/linux/man/1-git-credential/">git-credential</a></code>(1) for a detailed specification). </p>
<p> For a <code>get</code> operation, the helper should produce a list of attributes on stdout in the same format (see <code><a href="/docs/linux/man/1-git-credential/">git-credential</a></code>(1) for common attributes). A helper is free to produce a subset, or even no values at all if it has nothing useful to provide. Any provided attributes will overwrite those already known about by Git&#8217;s credential subsystem. </p>
<p> While it is possible to override all attributes, well behaving helpers should refrain from doing so for any attribute other than username and password. </p>
<p> If a helper outputs a <code>quit</code> attribute with a value of <code>true</code> or <code>1</code>, no further helpers will be consulted, nor will the user be prompted (if no credential has been provided, the operation will then fail). </p>
<p> Similarly, no more helpers will be consulted once both username and password had been provided. </p>
<p> For a <code>store</code> or <code>erase</code> operation, the helper&#8217;s output is ignored. </p>
<p> If a helper fails to perform the requested operation or needs to notify the user of a potential issue, it may write to stderr. </p>
<p> If it does not support the requested operation (e.g., a read-only store), it should silently ignore the request. </p>
<p> If a helper receives any other operation, it should silently ignore the request. This leaves room for future operations to be added (older helpers will just ignore the new requests).</p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
