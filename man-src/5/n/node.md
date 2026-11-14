---
title: "node(5)"
name: "node"
section: "5"
letter: "n"
url: "/docs/linux/man/5-node/"
description: "node.perms – LinuxNode permissions file."
---

<p>node.perms &#8211; LinuxNode permissions file.</p>
<h2>Description</h2>
<p><code>Node.perms</code> file is read at program startup with the knowledge of users username (call), connection type (AX.25, NET/ROM, ROSE, TCP/IP), peers IP address (for TCP/IP) and port name (for AX.25). The first entry matching this information is taken and user is asked for password and given permissions according to it. </p>
<p> The lines within <code>node.perms</code> must either be a comment line, which starts with a # in the first column, or a permission entry in the following format, each field being delimited by white space: </p>
<dl>
<dd>username type portname password permissions</dl>
<p> The field descriptions are: </p>
<dl>
<dt><code>username</code></p>
<dd>This is matched against users username (call) without SSID. An asterisk (*) matches any username.</p>
<dt><code>type</code></p>
<dd>This is matched against the type of the connection to user. Possible values for this field are:</p>
<dl>
<dd>
<dl>
<dt><code>*</code></p>
<dd>matches any type of connection.</p>
<dt><code>ax25</code></p>
<dd>matches users coming in with AX.25.</p>
<dt><code>netrom</code></p>
<dd>matches users coming in with NET/ROM.</p>
<dt><code>rose</code></p>
<dd>matches users coming in with ROSE.</p>
<dt><code>local</code></p>
<dd>matches TCP/IP connections where users host is in &quot;local&quot; network as defined in <a href="/docs/linux/man/5-node-conf/">node.conf</a>(5).</p>
<dt><code>ampr</code></p>
<dd>matches TCP/IP connections where users host is in amprnet (44.0.0.0/8).</p>
<dt><code>inet</code></p>
<dd>matches TCP/IP connections where users host is neither in &quot;local&quot; network nor in amprnet.</p>
<dt><code>host</code></p>
<dd>matches users starting LinuxNode from shell.</dl>
</dl>
<dt><code>portname</code></p>
<dd>If user is coming in with AX.25 this field is matched against the local port name the user is coming in via. An asterisk (*) matches any port name.</p>
<dt><code>password</code></p>
<dd>If the previous tree fields match and this field is not a single asterisk (*) the user is asked for a password. The password is then matched against this field.</p>
<dt><code>permissions</code></p>
<dd>This field represents a a bitmask of operations the user is permitted to do. It is a sum of the values listed here:</p>
<dl>
<dd>
<dl>
<dt><code>1</code></p>
<dd>permits logging in even if no other permissions are given.</p>
<dt><code>2</code></p>
<dd>permits outgoing AX.25 connects.</p>
<dt><code>4</code></p>
<dd>permits outgoing NET/ROM connects.</p>
<dt><code>8</code></p>
<dd>permits telneting to hosts in the &quot;local&quot; network as defined in <a href="/docs/linux/man/5-node-conf/">node.conf</a>(5).</p>
<dt><code>16</code></p>
<dd>permits telneting to hosts in amprnet.</p>
<dt><code>32</code></p>
<dd>permits telneting to hosts neither in the &quot;local&quot; network nor in amprnet.</p>
<dt><code>64</code></p>
<dd>permits using hidden ports in outgoing AX.25 connections. (See HiddenPorts command in <a href="/docs/linux/man/5-node-conf/">node.conf</a>(5).)</p>
<dt><code>128</code></p>
<dd>permits outgoing ROSE connects.</p>
<dt><code>256</code></p>
<dd>The no-escape flag. Disables the escape mechanism for this user.</dl>
</dl>
</dl>
<h2>Files</h2>
<p>/etc/ax25/node.perms</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-node/">node</a></code>(8), <code><a href="/docs/linux/man/5-node-conf/">node.conf</a></code>(5), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4). </p>
