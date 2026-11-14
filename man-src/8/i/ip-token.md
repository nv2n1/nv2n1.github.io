---
title: "ip-token(8)"
name: "ip-token"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-token/"
description: "ip-token – tokenized interface identifier support"
---

<p>ip-token &#8211; tokenized interface identifier support</p>
<h2>Synopsis</h2>
<pre><code>ip token

{ COMMAND |

    help }
</code></pre>
<p> <code>ip token set</code> <i>TOKEN</i> <code>dev</code> <i>DEV</i><br />
 <code>ip token del dev</code> <i>DEV</i><br />
 <code>ip token get</code> [ <code>dev</code> <i>DEV</i> ]<br />
 <code>ip token</code> [ <code>list</code> ] </p>
<h2>Description</h2>
<p>IPv6 tokenized interface identifier support is used for assigning well-known host-part addresses to nodes whilst still obtaining a global network prefix from Router advertisements. The primary target for tokenized identifiers are server platforms where addresses are usually manually configured, rather than using DHCPv6 or SLAAC. By using tokenized identifiers, hosts can still determine their network prefix by use of SLAAC, but more readily be automatically renumbered should their network prefix change [1]. Tokenized IPv6 Identifiers are described in the draft [1]: &lt;draft-chown-6man-tokenised-ipv6-identifiers-02&gt;.</p>
<h3>ip token set &#8211; set an interface token</h3>
<p>set the interface token to the kernel.</p>
<dl>
<dt><i>TOKEN</i></p>
<dd>the interface identifier token address.</p>
<dt><code>dev</code><i> DEV</i></p>
<dd>the networking interface.</dl>
<h3>ip token del &#8211; delete an interface token</h3>
<p>delete the interface token from the kernel.</p>
<dl>
<dt><code>dev</code><i> DEV</i></p>
<dd>the networking interface.</dl>
<h3>ip token get &#8211; get the interface token from the kernel</h3>
<p>show a tokenized interface identifier of a particular networking device. <code>Arguments:</code> coincide with the arguments of <code>ip token set</code> but the <i>TOKEN</i> must be left out.</p>
<h3>ip token list &#8211; list all interface tokens</h3>
<p>list all tokenized interface identifiers for the networking interfaces from the kernel. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Manpage by Daniel Borkmann</p>
