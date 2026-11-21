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
<p> <code>pscp</code> is a command-line client for the SSH-based SCP (secure copy) and SFTP (secure file transfer protocol) protocols.</p>
<h2>OPTIONS</h2>
<p> The command-line options supported by <i>pscp</i> are:</p>
<dl>
<dt><code>-V</code></dt>
<dd> Show version information and exit.</dd>
<dt><code>-pgpfp</code></dt>
<dd> Display the fingerprints of the PuTTY PGP Master Keys and exit, to aid in verifying new files released by the PuTTY team.</dd>
<dt><code>-ls</code></dt>
<dd> Remote directory listing.</dd>
<dt><code>-p</code></dt>
<dd> Preserve file attributes.</dd>
<dt><code>-q</code></dt>
<dd> Quiet, don&#8217;t show statistics.</dd>
<dt><code>-r</code></dt>
<dd> Copy directories recursively.</dd>
<dt><code>-unsafe</code></dt>
<dd> Allow server-side wildcards (DANGEROUS).</dd>
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
<dd> Private key file for authentication.</dd>
<dt><code>-scp</code></dt>
<dd> Force use of SCP protocol.</dd>
<dt><code>-sftp</code></dt>
<dd> Force use of SFTP protocol.</dd></dl>
<h2>MORE INFORMATION</h2>
<p> For more information on <code>pscp</code> it&#8217;s probably best to go and look at the manual on the PuTTY web page: </p>
<p> <code><a rel="nofollow" href="http://www.chiark.greenend.org.uk/~sgtatham/putty/">http://www.chiark.greenend.org.uk/~sgtatham/putty/</a></code></p>
<h2>BUGS</h2>
<p> This man page isn&#8217;t terribly complete. See the above web link for better documentation. </p>
