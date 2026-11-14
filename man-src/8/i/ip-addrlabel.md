---
title: "ip-addrlabel(8)"
name: "ip-addrlabel"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-addrlabel/"
description: "ip-addrlabel – protocol address label management"
---

<p>ip-addrlabel &#8211; protocol address label management</p>
<h2>Synopsis</h2>
<pre><code>ip addrlabel

{ COMMAND |

    help }</code></pre>
<p> <code>ip addrlabel</code> { <code>add</code> | <code>del</code> } <code>prefix</code> <code>PREFIX</code> [ <code>dev</code> <i>DEV</i> ] [ <code>label</code> <i>NUMBER</i> ] </p>
<pre><code>ip addrlabel { list | flush }
</code></pre>
<h2>Description</h2>
<p>IPv6 address labels are used for address selection; they are described in RFC 3484. Precedence is managed by userspace, and only the label itself is stored in the kernel.</p>
<h3>ip addrlabel add &#8211; add an address label</h3>
<p>add an address label entry to the kernel.</p>
<dl>
<dt><code>prefix</code><i> PREFIX</i></p>
<dd>
<dt><code>dev</code><i> DEV</i></p>
<dd>the outgoing interface.</p>
<dt><code>label</code><i> NUMBER</i></p>
<dd>the label for the prefix. 0xffffffff is reserved.</dl>
<h3>ip addrlabel del &#8211; delete an address label</h3>
<p>delete an address label entry from the kernel. <code>Arguments:</code> coincide with the arguments of <code>ip addrlabel add</code> but the label is not required.</p>
<h3>ip addrlabel list &#8211; list address labels</h3>
<p>list the current address label entries in the kernel.</p>
<h3>ip addrlabel flush &#8211; flush address labels</h3>
<p>flush all address labels in the kernel. This does not restore any default settings. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Manpage by Yoshifuji Hideaki / 吉藤英明</p>
