---
title: "ssh-keyscan(1)"
name: "ssh-keyscan"
section: "1"
letter: "s"
url: "/docs/linux/man/1-ssh-keyscan/"
description: "ssh-keyscan – gather SSH public keys from servers"
---

<h2 class="name">NAME</h2>
<p> <code>ssh-keyscan</code> &#8211; gather SSH public keys from servers </p>
<h2>SYNOPSIS</h2>
<p> <code>ssh-keyscan</code> [-<code>46cDHv </code>[-<code>f </code><i>file</i> ] ] [-<code>p </code><i>port</i> ] [-<code>T </code><i>timeout</i> ] [-<code>t </code><i>type</i> ] [<i>host | addrlist namelist</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>ssh-keyscan</code> is a utility for gathering the public SSH host keys of a number of hosts. It was designed to aid in building and verifying ssh_known_hosts files, the format of which is documented in <a href="/docs/linux/man/8-sshd/">sshd</a>(8). <code>ssh-keyscan</code> provides a minimal interface suitable for use by shell and perl scripts. </p>
<p> <code>ssh-keyscan</code> uses non-blocking socket I/O to contact as many hosts as possible in parallel, so it is very efficient. The keys from a domain of 1,000 hosts can be collected in tens of seconds, even when some of those hosts are down or do not run <a href="/docs/linux/man/8-sshd/">sshd</a>(8). For scanning, one does not need login access to the machines that are being scanned, nor does the scanning process involve any encryption. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-4</code></p>
<dd> Force <code>ssh-keyscan</code> to use IPv4 addresses only.</p>
<dt><code>-6</code></p>
<dd> Force <code>ssh-keyscan</code> to use IPv6 addresses only.</p>
<dt><code>-c</code></p>
<dd> Request certificates from target hosts instead of plain keys.</p>
<dt><code>-D</code></p>
<dd> Print keys found as SSHFP DNS records. The default is to print keys in a format usable as a <a href="/docs/linux/man/1-ssh/">ssh</a>(1) known_hosts file.</p>
<dt><code>-f </code><i>file</i></p>
<dd> Read hosts or &#8220;addrlist namelist&#8221; pairs from <i>file</i> one per line. If `-&#8216; is supplied instead of a filename, <code>ssh-keyscan</code> will read from the standard input. Input is expected in the format: </p>
<pre>
1.2.3.4,1.2.4.4 name.my.domain,name,n.my.domain,n,1.2.3.4,1.2.4.4
</pre>
<dt><code>-H</code></p>
<dd> Hash all hostnames and addresses in the output. Hashed names may be used normally by <a href="/docs/linux/man/1-ssh/">ssh</a>(1) and <a href="/docs/linux/man/8-sshd/">sshd</a>(8), but they do not reveal identifying information should the file&#8217;s contents be disclosed.</p>
<dt><code>-p </code><i>port</i></p>
<dd> Connect to <i>port</i> on the remote host.</p>
<dt><code>-T </code><i>timeout</i></p>
<dd> Set the timeout for connection attempts. If <i>timeout</i> seconds have elapsed since a connection was initiated to a host or since the last time anything was read from that host, the connection is closed and the host in question considered unavailable. The default is 5 seconds.</p>
<dt><code>-t </code><i>type</i></p>
<dd> Specify the type of the key to fetch from the scanned hosts. The possible values are &#8220;dsa&#8221; &#8220;ecdsa&#8221; &#8220;ed25519&#8221; or &#8220;rsa&#8221; Multiple values may be specified by separating them with commas. The default is to fetch &#8220;rsa&#8221; &#8220;ecdsa&#8221; and &#8220;ed25519&#8221; keys.</p>
<dt><code>-v</code></p>
<dd> Verbose mode: print debugging messages about progress.</dl>
<p> If an ssh_known_hosts file is constructed using <code>ssh-keyscan</code> without verifying the keys, users will be vulnerable to <i>man in the middle</i> attacks. On the other hand, if the security model allows such a risk, <code>ssh-keyscan</code> can help in the detection of tampered keyfiles or man in the middle attacks which have begun after the ssh_known_hosts file was created.</p>
<h2>FILES</h2>
<p> /etc/ssh/ssh_known_hosts</p>
<h2>EXAMPLES</h2>
<p> Print the RSA host key for machine <i>hostname</i> </p>
<blockquote><p><tt>$ ssh-keyscan -t rsa hostname</tt></p></blockquote>
<p> Find all hosts from the file ssh_hosts which have new or different keys from those in the sorted file ssh_known_hosts </p>
<blockquote>
<pre>
$ ssh-keyscan -t rsa,dsa,ecdsa,ed25519 -f ssh_hosts | \
        sort -u - ssh_known_hosts | diff ssh_known_hosts -
</pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ssh/">ssh</a>(1), <a href="/docs/linux/man/8-sshd/">sshd</a>(8)</p>
<dl>
<dt>
<dd> 2006 <i>RFC 4255</i> <i>Using DNS to Securely Publish Secure Shell (SSH) Key Fingerprints</i></dl>
<h2>AUTHORS</h2>
<p> An -nosplit An David Mazieres Aq Mt dm [at] lcs.mit.edu wrote the initial version, and An Wayne Davison Aq Mt wayned [at] users.sourceforge.net added support for protocol version 2. </p>
<h2>Index</h2>
