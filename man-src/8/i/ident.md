---
title: "ident(8)"
name: "ident"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ident/"
description: "ident – nnrpd ident resolver"
---

<p>ident &#8211; nnrpd ident resolver</p>
<h2>Synopsis</h2>
<p><code>ident</code> [<code>-p</code> <i>port</i>] [<code>-t</code>]</p>
<h2>Description</h2>
<p>This program attempts to resolve usernames for <code>nnrpd</code> by using the ident protocol to query the remote host. It contacts the remote host using either IPv4 or IPv6 depending on which protocol was used for the incoming <font SIZE="-1">NNTP</font> connection.</p>
<h2>Options</h2>
<dl>
<dt><code>-p</code> <i>port</i></p>
<dd>If this option is given, attempt to contact identd on the specified remote port (which can be a numeric or symbolic specification). Non-numeric values will be looked up using <i><a href="/docs/linux/man/3-getservbyname/">getservbyname</a></i>(3). The default value is the result of <tt>&quot;getservbyname(&quot;ident&quot;)&quot;</tt> if available, or port 113 otherwise.</p>
<dt><code>-t</code></p>
<dd>If this option is given, the identity returned will never have a domain part. That is, if the remote server returns a result containing an <tt>&quot;@&quot;</tt> character, <code>ident</code> truncates the response at the <tt>&quot;@&quot;</tt>. This is useful to allow the <i>default-domain</i> parameter in <i>reaers.conf</i> to override the domain supplied by the remote host (particularly if the supplied domain part is an unqualified local machine name rather than a full domain name).</dl>
<h2>Example</h2>
<p>The following <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) fragment tells nnrpd to trust ident information for hosts on a local network, but to replace the domain returned from the ident query: </p>
<pre> auth LAN {
 hosts: &quot;192.168/16&quot;
 res: &quot;ident -t&quot;
 default-domain: &quot;internal.example.com&quot;
 }
 access LAN {
 users: &quot;*@internal.example.com&quot;
 newsgroups: example.*
 }</pre>
<p>Access is granted to the example.* groups for all users on the local network whose machines respond to ident queries.</p>
<h2>History</h2>
<p>This documentation was written by Jeffrey M. Vinocur &lt;jeff [at] litech.org&gt;. </p>
<p> <tt>$Id:</tt> ident.pod 8200 2008-11-30 13:31:30Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) </p>
