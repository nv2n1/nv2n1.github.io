---
title: "docker-logout(1)"
name: "docker-logout"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-logout/"
description: "docker-logout – Log out from a Docker registry"
---

<h2 class="name">NAME</h2>
<p> docker-logout &#8211; Log out from a Docker registry </p>
<h2>SYNOPSIS</h2>
<p> <code>docker logout [SERVER]</code> </p>
<h2>DESCRIPTION</h2>
<p> Log out of a Docker Registry located on the specified SERVER. You can specify a URL or a hostname for the SERVER value. If you do not specify a SERVER, the command attempts to log you out of Docker&#8217;s public registry located at <a rel="nofollow" href="https://registry-1.docker.io/">https://registry-1.docker.io/</a> by default. </p>
<h2>EXAMPLES</h2>
<h2>Log out from a registry on your localhost</h2>
<dl>
<dt>
<dd>
<pre>
# docker logout localhost:8080
</pre>
</dl>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/1-docker-login/">docker-login</a>(1)</code> to log in to a Docker registry server. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for logout</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker/">docker</a>(1)</code> </p>
<h2>Index</h2>
