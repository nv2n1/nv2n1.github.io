---
title: "ypset(8)"
name: "ypset"
section: "8"
letter: "y"
url: "/docs/linux/man/8-ypset/"
description: "ypset – bind ypbind to a particular NIS server"
---

<p>ypset &#8211; bind ypbind to a particular NIS server</p>
<h2>Synopsis</h2>
<p><code>ypset</code> [ <code>-d</code><i> domain</i> ] [ <code>-h</code><i> hostname</i> ] <i>server</i> </p>
<h2>Description</h2>
<p>In order to run <code>ypset</code>, <code>ypbind</code> must be initiated with the <code>-ypset</code> or <code>-ypsetme</code> options. See <code><a href="/docs/linux/man/8-ypbind/">ypbind</a></code>(8). <code>ypset</code> tells <code>ypbind</code> to get NIS services for the specified <i>domain</i> from the <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8) process running on <i>server.</i> In cases where several hosts on the local net are supplying NIS services, it is possible for <code>ypbind</code> to rebind to another host even while you attempt to find out if the <code>ypset</code> operation succeeded. For example, you can type:</p>
<dl>
<dd>
<dt><code>example% ypset host1</p>
<dd>
<dt>example% ypwhich</p>
<dd>
<dt>host2</p>
<dd></dl>
<p> which can be confusing. This is a function of the NIS subsystem&#8217;s attempt to know always a running NIS server, and occurs when host1 does not respond to ypbind because it is not running ypserv (or is overloaded), and host2, running ypserv, gets the binding. </code><i>Server</i> indicates the NIS server to bind to, and must be specified as a name or an IP address. This will work only if the node has a current valid binding for the domain in question, and <code>ypbind</code> has been set to allow use of <code>ypset</code>. In most cases, <i>server</i> should be specified as an IP address. </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code><i> domain</i></p>
<dd>Specify a domain other than the default domain as returned by <code><a href="/docs/linux/man/8-domainname/">domainname</a></code>(8).</p>
<dt><code>-h</code><i> hostname</i></p>
<dd>Set the NIS binding on host <i>hostname</i><br />
&nbsp;<wbr>instead of the local machine.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-domainname/">domainname</a></code>(8), <code><a href="/docs/linux/man/8-ypbind/">ypbind</a></code>(8), <code><a href="/docs/linux/man/8-ypcat/">ypcat</a></code>(8), <code><a href="/docs/linux/man/1-ypmatch/">ypmatch</a></code>(1), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-yppoll/">yppoll</a></code>(8), <code><a href="/docs/linux/man/1-ypwhich/">ypwhich</a></code>(1) </p>
<h2>Author</h2>
<p><code>ypset</code> is part of the <code>yp-tools</code> package, which was written by Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;.</p>
