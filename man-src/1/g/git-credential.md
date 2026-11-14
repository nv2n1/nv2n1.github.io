---
title: "git-credential(1)"
name: "git-credential"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-credential/"
description: "git-credential – Retrieve and store user credentials"
---

<h2 class="name">NAME</h2>
<p> git-credential &#8211; Retrieve and store user credentials </p>
<h2>SYNOPSIS</h2>
<pre>
git credential &lt;fill|approve|reject&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> Git has an internal interface for storing and retrieving credentials from system-specific helpers, as well as prompting the user for usernames and passwords. The git-credential command exposes this interface to scripts which may want to retrieve, store, or prompt for credentials in the same manner as Git. The design of this scriptable interface models the internal C API; see credential.h for more background on the concepts. </p>
<p> git-credential takes an &quot;action&quot; option on the command-line (one of <code>fill</code>, <code>approve</code>, or <code>reject</code>) and reads a credential description on stdin (see INPUT/OUTPUT FORMAT). </p>
<p> If the action is <code>fill</code>, git-credential will attempt to add &quot;username&quot; and &quot;password&quot; attributes to the description by reading config files, by contacting any configured credential helpers, or by prompting the user. The username and password attributes of the credential description are then printed to stdout together with the attributes already provided. </p>
<p> If the action is <code>approve</code>, git-credential will send the description to any configured credential helpers, which may store the credential for later use. </p>
<p> If the action is <code>reject</code>, git-credential will send the description to any configured credential helpers, which may erase any stored credential matching the description. </p>
<p> If the action is <code>approve</code> or <code>reject</code>, no output should be emitted.</p>
<h2>TYPICAL USE OF GIT CREDENTIAL</h2>
<p> An application using git-credential will typically use <code>git credential</code> following these steps: </p>
<dl>
<dt>
<dd> 1. Generate a credential description based on the context. </p>
<p> For example, if we want a password for <code><a rel="nofollow" href="https://example.com/foo.git">https://example.com/foo.git</a></code>, we might generate the following credential description (don&#8217;t forget the blank line at the end; it tells <code>git credential</code> that the application finished feeding all the information it has): </p>
<dl>
<dt>
<dd>
<pre>
protocol=https
host=example.com
path=foo.git
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 2. Ask git-credential to give us a username and password for this description. This is done by running <code>git credential fill</code>, feeding the description from step (1) to its standard input. The complete credential description (including the credential per se, i.e. the login and password) will be produced on standard output, like: </p>
<dl>
<dt>
<dd>
<pre>
protocol=https
host=example.com
username=bob
password=secr3t
</pre>
</dl>
<p> In most cases, this means the attributes given in the input will be repeated in the output, but Git may also modify the credential description, for example by removing the <code>path</code> attribute when the protocol is HTTP(s) and <code>credential.useHttpPath</code> is false. </p>
<p> If the <code>git credential</code> knew about the password, this step may not have involved the user actually typing this password (the user may have typed a password to unlock the keychain instead, or no user interaction was done if the keychain was already unlocked) before it returned <code>password=secr3t</code>.</dl>
<dl>
<dt>
<dd> 3. Use the credential (e.g., access the URL with the username and password from step (2)), and see if it&#8217;s accepted.</dl>
<dl>
<dt>
<dd> 4. Report on the success or failure of the password. If the credential allowed the operation to complete successfully, then it can be marked with an &quot;approve&quot; action to tell <code>git credential</code> to reuse it in its next invocation. If the credential was rejected during the operation, use the &quot;reject&quot; action so that <code>git credential</code> will ask for a new password in its next invocation. In either case, <code>git credential</code> should be fed with the credential description obtained from step (2) (which also contain the ones provided in step (1)).</dl>
<h2>INPUT/OUTPUT FORMAT</h2>
<p> <code>git credential</code> reads and/or writes (depending on the action used) credential information in its standard input/output. This information can correspond either to keys for which <code>git credential</code> will obtain the login information (e.g. host, protocol, path), or to the actual credential data to be obtained (username/password). </p>
<p> The credential is split into a set of named attributes, with one attribute per line. Each attribute is specified by a key-value pair, separated by an <code>=</code> (equals) sign, followed by a newline. </p>
<p> The key may contain any bytes except <code>=</code>, newline, or NUL. The value may contain any bytes except newline or NUL. </p>
<p> In both cases, all bytes are treated as-is (i.e., there is no quoting, and one cannot transmit a value with newline or NUL in it). The list of attributes is terminated by a blank line or end-of-file. </p>
<p> Git understands the following attributes: </p>
<p> <code>protocol</code></p>
<dl>
<dt>
<dd> The protocol over which the credential will be used (e.g., <code>https</code>).</dl>
<p> <code>host</code></p>
<dl>
<dt>
<dd> The remote hostname for a network credential. This includes the port number if one was specified (e.g., &quot;example.com:8088&quot;).</dl>
<p> <code>path</code></p>
<dl>
<dt>
<dd> The path with which the credential will be used. E.g., for accessing a remote https repository, this will be the repository&#8217;s path on the server.</dl>
<p> <code>username</code></p>
<dl>
<dt>
<dd> The credential&#8217;s username, if we already have one (e.g., from a URL, the configuration, the user, or from a previously run helper).</dl>
<p> <code>password</code></p>
<dl>
<dt>
<dd> The credential&#8217;s password, if we are asking it to be stored.</dl>
<p> <code>url</code></p>
<dl>
<dt>
<dd> When this special attribute is read by <code>git credential</code>, the value is parsed as a URL and treated as if its constituent parts were read (e.g., <code>url=<a rel="nofollow" href="https://example.com">https://example.com</a></code> would behave as if <code>protocol=https</code> and <code>host=example.com</code> had been provided). This can help callers avoid parsing URLs themselves. </p>
<p> Note that specifying a protocol is mandatory and if the URL doesn&#8217;t specify a hostname (e.g., &quot;<a href="cert:///path/to/file">cert:///path/to/file</a>&quot;) the credential will contain a hostname attribute whose value is an empty string. </p>
<p> Components which are missing from the URL (e.g., there is no username in the example above) will be left unset.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
