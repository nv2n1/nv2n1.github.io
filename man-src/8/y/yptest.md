---
title: "yptest(8)"
name: "yptest"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yptest/"
description: "yptest – test NIS configuration"
---

<p>yptest &#8211; test NIS configuration</p>
<h2>Synopsis</h2>
<p><code>yptest [-q</code>] [<code>-d </code><i>domain</i>] [<code>-h </code><i>host</i>] [<code>-m </code><i>map</i>] [<code>-u </code><i>user</i>] </p>
<h2>Description</h2>
<p><code>yptest</code> calls various NIS functions to check if the NIS configuration is correct and works as expected. </p>
<h2>Options</h2>
<dl>
<dt><code>-q</code></p>
<dd>Be quiet, don&#8217;t print messages</p>
<dt><code>-d</code><i> domainname</i></p>
<dd>Specify a domain other than the default domain as returned by <code><a href="/docs/linux/man/8-domainname/">domainname</a></code>(8). This option is not supported by all tests.</p>
<dt><code>-h</code><i> hostname</i></p>
<dd>Query ypserv on <i>hostname</i> instead of the currently used one. This option is not supported by all tests.</p>
<dt><code>-m</code><i> map</i></p>
<dd>Use the map <i>map</i> for the tests instead of <i>passwd.byname.</i> This option should be used if the default map does not exist.</p>
<dt><code>-u</code><i> user</i></p>
<dd>Use the account <i>user</i> instead of <i>nobody.</i> This option should be used if the <i>nobody</i> account does not exist in the map used for testing (<i>passwd.byname</i> or the one given with the <code>-m</code> option).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-domainname/">domainname</a></code>(8), <code><a href="/docs/linux/man/8-ypbind/">ypbind</a></code>(8), <code><a href="/docs/linux/man/8-ypcat/">ypcat</a></code>(8), <code><a href="/docs/linux/man/1-ypmatch/">ypmatch</a></code>(1), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-yppoll/">yppoll</a></code>(8), <code><a href="/docs/linux/man/1-ypwhich/">ypwhich</a></code>(1) </p>
<h2>Author</h2>
<p><code>yptest</code> is part of the <code>yp-tools</code> package, which was written by Thorsten Kukuk &lt;kukuk [at] linux-nis.org&gt;.</p>
