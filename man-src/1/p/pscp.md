---
title: "pscp(1)"
name: "pscp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pscp/"
description: "pscp – command-line SCP (secure copy) / SFTP client"
---

<h2>NAME</h2>
<p> <code>pscp</code> &#8211; command-line SCP (secure copy) / SFTP client</p>
<h2>SYNOPSIS</h2>
<pre><code>
pscp &amp;nbsp;
[options] &amp; nbsp;
[user @] host : source &amp;nbsp;
target
    pscp &amp;nbsp;
[options] &amp; nbsp;
source &amp;nbsp;
[source...] &amp; nbsp;
[user @] host : target
                    pscp &amp;nbsp;
[options] &amp; nbsp;
- ls &amp;nbsp;
[user @] host : filespec
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>pscp</code> is a command-line client for the SSH-based SCP (secure copy) and SFTP (secure file transfer protocol) protocols.</p>
<h2>OPTIONS</h2>
<p> The command-line options supported by <i>pscp</i> are:</p>
<dl>
<dt><code>-V</code></p>
<dd> Show version information and exit.</p>
<dt><code>-pgpfp</code></p>
<dd> Display the fingerprints of the PuTTY PGP Master Keys and exit, to aid in verifying new files released by the PuTTY team.</p>
<dt><code>-ls</code></p>
<dd> Remote directory listing.</p>
<dt><code>-p</code></p>
<dd> Preserve file attributes.</p>
<dt><code>-q</code></p>
<dd> Quiet, don&#8217;t show statistics.</p>
<dt><code>-r</code></p>
<dd> Copy directories recursively.</p>
<dt><code>-unsafe</code></p>
<dd> Allow server-side wildcards (DANGEROUS).</p>
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
<dd> Private key file for authentication.</p>
<dt><code>-scp</code></p>
<dd> Force use of SCP protocol.</p>
<dt><code>-sftp</code></p>
<dd> Force use of SFTP protocol.</dl>
<h2>MORE INFORMATION</h2>
<p> For more information on <code>pscp</code> it&#8217;s probably best to go and look at the manual on the PuTTY web page: </p>
<p> <code><a rel="nofollow" href="http://www.chiark.greenend.org.uk/~sgtatham/putty/">http://www.chiark.greenend.org.uk/~sgtatham/putty/</a></code></p>
<h2>BUGS</h2>
<p> This man page isn&#8217;t terribly complete. See the above web link for better documentation. </p>
<h2>Index</h2>
