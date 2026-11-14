---
title: "ip-sr(8)"
name: "ip-sr"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-sr/"
description: "ip-sr – IPv6 Segment Routing management"
---

<p>ip-sr &#8211; IPv6 Segment Routing management</p>
<h2>Synopsis</h2>
<pre><code>ip sr

{ COMMAND |

    help }
</code></pre>
<p> <code>ip sr hmac show</code><br />
 <code>ip sr hmac set</code> <i>KEYID ALGO</i><br />
 <code>ip sr tunsrc show</code><br />
 <code>ip sr tunsrc set</code> <i>ADDRESS</i> </p>
<h2>Description</h2>
<p>The <code>ip sr</code> command is used to configure IPv6 Segment Routing (SRv6) internal parameters. Those parameters include the mapping between an HMAC key ID and its associated hashing algorithm and secret, and the IPv6 address to use as source for encapsulated packets. The <code>ip sr hmac set</code> command prompts for a passphrase that will be used as the HMAC secret for the corresponding key ID. A blank passphrase removes the mapping. The currently supported algorithms for <i>ALGO</i> are <code>sha1</code> and <code>sha256</code>. If the tunnel source is set to the address :: (which is the default), then an address of the egress interface will be selected. As this operation may hinder performances, it is recommended to set a non-default address. </p>
<h2>Examples</h2>
<h3>Configure an HMAC mapping for key ID 42 and hashing algorithm SHA-256</h3>
<pre># ip sr hmac set 42 sha256</pre>
<h3>Set the tunnel source address to 2001:db8::1</h3>
<pre># ip sr tunsrc set 2001:db8::1</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip-route/">ip-route</a></code>(8)</p>
<h2>Author</h2>
<p>David Lebrun &lt;david.lebrun [at] uclouvain.be&gt;</p>
