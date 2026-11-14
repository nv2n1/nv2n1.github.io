---
title: "mosh-client(1)"
name: "mosh-client"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mosh-client/"
description: "mosh-client – client-side helper for mosh"
---

<h2 class="name">NAME</h2>
<p> mosh-client &#8211; client-side helper for mosh </p>
<h2>SYNOPSIS</h2>
<p> MOSH_KEY=KEY <code>mosh-client </code> IP PORT<br />
 <code>mosh-client </code> -c </p>
<h2>DESCRIPTION</h2>
<p> <code>mosh-client</code> is a helper program for the <code><a href="/docs/linux/man/1-mosh/">mosh</a></code>(1) remote terminal application. </p>
<p> <code>mosh</code> itself is a setup script that establishes an SSH connection, runs the server-side helper <code>mosh-server</code>, and collects the server&#8217;s port number and session key. </p>
<p> <code>mosh</code> then executes <code>mosh-client</code> with the server&#8217;s IP address, port, and session key. <code>mosh-client</code> runs for the lifetime of the connection. </p>
<p> The 22-byte base64 session key given by <code>mosh-server</code> is supplied in the MOSH_KEY environment variable. This represents a 128-bit AES key that protects the integrity and confidentiality of the session. </p>
<p> For constructing new setup wrappers for remote execution facilities other than SSH, it may be necessary to invoke <code>mosh-client</code> directly. </p>
<p> With the -c option, <code>mosh-client</code> instead prints the number of colors of the terminal given by the TERM environment variable. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>MOSH_KEY</code></p>
<dd> This variable must be set, and must contain a Base64-encoded cryptographic key from <code><a href="/docs/linux/man/1-mosh-server/">mosh-server</a></code>(1). </p>
<dt><code>MOSH_ESCAPE_KEY</code></p>
<dd> See <code><a href="/docs/linux/man/1-mosh/">mosh</a></code>(1). </p>
<dt><code>MOSH_PREDICTION_DISPLAY</code></p>
<dd> Controls local echo as described in <code><a href="/docs/linux/man/1-mosh/">mosh</a></code>(1). </p>
<dt><code>MOSH_TITLE_NOPREFIX</code></p>
<dd> See <code><a href="/docs/linux/man/1-mosh/">mosh</a></code>(1). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mosh/">mosh</a></code>(1), <code><a href="/docs/linux/man/1-mosh-server/">mosh-server</a></code>(1). </p>
<p> Project home page: <i><a rel="nofollow" href="http://mosh.mit.edu">http://mosh.mit.edu</a></i> </p>
<h2>AUTHOR</h2>
<p> mosh was written by Keith Winstein &lt;mosh-devel [at] mit.edu&gt;.</p>
<h2>BUGS</h2>
<p> Please report bugs to <i>mosh-devel [at] mit.edu</i>. Users may also subscribe to the <i>mosh-users [at] mit.edu</i> mailing list, at<br />
 <i><a rel="nofollow" href="http://mailman.mit.edu/mailman/listinfo/mosh-users">http://mailman.mit.edu/mailman/listinfo/mosh-users</a></i> </p>
<h2>Index</h2>
