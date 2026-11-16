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
<dt><code>-V</code></dt>
<dd> Show version information and exit.</dd>
<dt><code>-pgpfp</code></dt>
<dd> Display the fingerprints of the PuTTY PGP Master Keys and exit, to aid in verifying new files released by the PuTTY team.</dd>
<dt><code>-b</code> <i>batchfile</i></dt>
<dd> Use specified batchfile.</dd>
<dt><code>-bc</code></dt>
<dd> Output batchfile commands.</dd>
<dt><code>-be</code></dt>
<dd> Don&#8217;t stop batchfile processing on errors.</dd>
<dt><code>-v</code></dt>
<dd> Show verbose messages.</dd>
<dt><code>-load</code> <i>session</i></dt>
<dd> Load settings from saved session.</dd>
<dt><code>-P</code> <i>port</i></dt>
<dd> Connect to port <i>port</i>.</dd>
<dt><code>-l</code> <i>user</i></dt>
<dd> Set remote username to <i>user</i>.</dd>
<dt><code>-batch</code></dt>
<dd> Disable interactive prompts.</dd>
<dt><code>-pw</code> <i>password</i></dt>
<dd> Set remote password to <i>password</i>. <i>CAUTION:</i> this will likely make the password visible to other users of the local machine (via commands such as `<code>w</code>&#8216;).</dd>
<dt><code>-1</code></dt>
<dd> Force use of SSH protocol version 1.</dd>
<dt><code>-2</code></dt>
<dd> Force use of SSH protocol version 2.</dd>
<dt><code>-C</code></dt>
<dd> Enable SSH compression.</dd>
<dt><code>-i</code> <i>path</i></dt>
<dd> Private key file for authentication.</dd></dl>
<h2>COMMANDS</h2>
<p> For a list of commands available inside <code>psftp</code>, type <code>help</code> at the <code>psftp&gt;</code> prompt.</p>
<h2>MORE INFORMATION</h2>
<p> For more information on <code>psftp</code> it&#8217;s probably best to go and look at the manual on the PuTTY web page: </p>
<p> <code><a rel="nofollow" href="http://www.chiark.greenend.org.uk/~sgtatham/putty/">http://www.chiark.greenend.org.uk/~sgtatham/putty/</a></code></p>
<h2>BUGS</h2>
<p> This man page isn&#8217;t terribly complete. See the above web link for better documentation. </p>
<h2>Index</h2>
