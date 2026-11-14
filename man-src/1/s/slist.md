---
title: "slist(1)"
name: "slist"
section: "1"
letter: "s"
url: "/docs/linux/man/1-slist/"
description: "slist – Lists available NetWare Servers"
---

<h2>NAME</h2>
<p> slist &#8211; Lists available NetWare Servers</p>
<h2>SYNOPSIS</h2>
<p> <code>slist</code> [ <i>pattern</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>slist</code> lists all NetWare Servers available in your network. </p>
<p> If slist does not print to a tty, the decorative header line is not printed, so that you can count the servers on your network by doing </p>
<p> slist | wc -l </p>
<h2>OPTIONS</h2>
<p> <code>pattern</code></p>
<dl>
<dt>
<dd> <code>pattern</code> is used to list only servers whose names match the specified pattern. For a server to be listed, the pattern must match the full server name. You can use wildcards for the pattern, but you must protect these wildcards from any command line expansion by quoting. Case doesn&#8217;t matter.</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>slist &quot;I*&quot;</p>
<dd>
<dt>or</p>
<dd>
<dt>slist &quot;i*&quot;</p>
<dd> List all available Netware servers on your Network, that begin with an &quot;I&quot;. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-ncpmount/">ncpmount</a>(8), <a href="/docs/linux/man/8-ncpumount/">ncpumount</a>(8), <a href="/docs/linux/man/1-pqlist/">pqlist</a>(1), <a href="/docs/linux/man/1-nprint/">nprint</a>(1) </code> </p>
<h2>CREDITS</h2>
<p> slist was written by Volker Lendecke (lendecke [at] math.uni-goettingen.de) </p>
<h2>BUGS</h2>
<p> <code>slist</code> works only in <i>IPX</i> environment, as it uses <i>SAP</i> to find first server and then <i>Bindery</i> to get list of servers. </p>
<h2>Index</h2>
