---
title: "psftp(1)"
name: "psftp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-psftp/"
description: "psftp – interactive SFTP (secure file transfer protocol) client"
---

<h2>NAME</h2>
<p> <code>psftp</code> &#8211; interactive SFTP (secure file transfer protocol) client</p>
<h2>SYNOPSIS</h2>
<pre><code>
psftp &amp;nbsp;
[options] &amp; nbsp;
[user @] host
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>psftp</code> is an interactive text-based client for the SSH-based SFTP (secure file transfer) protocol.</p>
<h2>OPTIONS</h2>
<p> The command-line options supported by <code>psftp</code> are:</p>
<dl>
<dt><code>-V</code></p>
<dd> Show version information and exit.</p>
<dt><code>-pgpfp</code></p>
<dd> Display the fingerprints of the PuTTY PGP Master Keys and exit, to aid in verifying new files released by the PuTTY team.</p>
<dt><code>-b</code> <i>batchfile</i></p>
<dd> Use specified batchfile.</p>
<dt><code>-bc</code></p>
<dd> Output batchfile commands.</p>
<dt><code>-be</code></p>
<dd> Don&#8217;t stop batchfile processing on errors.</p>
<dt><code>-v</code></p>
<dd> Show verbose messages.</p>
<dt><code>-load</code> <i>session</i></p>
<dd> Load settings from saved session.</p>
<dt><code>-P</code> <i>port</i></p>
<dd> Connect to port <i>port</i>.</p>
<dt><code>-l</code> <i>user</i></p>
<dd> Set remote username to <i>user</i>.</p>
<dt><code>-batch</code></p>
<dd> Disable interactive prompts.</p>
<dt><code>-pw</code> <i>password</i></p>
<dd> Set remote password to <i>password</i>. <i>CAUTION:</i> this will likely make the password visible to other users of the local machine (via commands such as `<code>w</code>&#8216;).</p>
<dt><code>-1</code></p>
<dd> Force use of SSH protocol version 1.</p>
<dt><code>-2</code></p>
<dd> Force use of SSH protocol version 2.</p>
<dt><code>-C</code></p>
<dd> Enable SSH compression.</p>
<dt><code>-i</code> <i>path</i></p>
<dd> Private key file for authentication.</dl>
<h2>COMMANDS</h2>
<p> For a list of commands available inside <code>psftp</code>, type <code>help</code> at the <code>psftp&gt;</code> prompt.</p>
<h2>MORE INFORMATION</h2>
<p> For more information on <code>psftp</code> it&#8217;s probably best to go and look at the manual on the PuTTY web page: </p>
<p> <code><a rel="nofollow" href="http://www.chiark.greenend.org.uk/~sgtatham/putty/">http://www.chiark.greenend.org.uk/~sgtatham/putty/</a></code></p>
<h2>BUGS</h2>
<p> This man page isn&#8217;t terribly complete. See the above web link for better documentation. </p>
<h2>Index</h2>
