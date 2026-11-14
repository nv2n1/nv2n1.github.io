---
title: "ip-tunnel(8)"
name: "ip-tunnel"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-tunnel/"
description: "ip-tunnel – tunnel configuration"
---

<p>ip-tunnel &#8211; tunnel configuration</p>
<h2>Synopsis</h2>
<p><code>ip tunnel help</code><br />
 <code>ip </code> [ <i>OPTIONS</i> ] <code>tunnel</code> { <code>add</code> | <code>change</code> | <code>del</code> | <code>show</code> | <code>prl</code> | <code>6rd</code> } [ <i>NAME</i> ]<br />
 [ <code>mode</code> <i>MODE</i> ] [ <code>remote</code> <i>ADDR</i> ] [ <code>local</code> <i>ADDR</i> ]<br />
 [ [<code>i</code>|<code>o</code>]<code>seq</code> ] [ [<code>i</code>|<code>o</code>]<code>key</code> <i>KEY</i> ] [ [<code>i</code>|<code>o</code>]<code>csum</code> ] ]<br />
 [ <code>encaplimit</code> <i>ELIM</i> ] [ <code>ttl</code>|<code>hoplimit</code> <i>TTL</i> ]<br />
 [ <code>tos</code> <i>TOS</i> ] [ <code>flowlabel</code> <i>FLOWLABEL</i> ]<br />
 [ <code>prl-default</code> <i>ADDR</i> ] [ <code>prl-nodefault</code> <i>ADDR</i> ] [ <code>prl-delete</code> <i>ADDR</i> ]<br />
 [ <code>6rd-prefix</code> <i>ADDR</i> ] [ <code>6rd-relay_prefix</code> <i>ADDR</i> ] [ <code>6rd-reset</code> ]<br />
 [ [<code>no</code>]<code>pmtudisc</code> ] [ [<code>no</code>]<code>ignore-df</code> ] [ [<code>no</code>]<code>allow-localremote</code> ]<br />
 [ <code>dev</code> <i>PHYS_DEV</i> ] </p>
<pre><code>MODE :=

{ ipip | gre | sit | isatap | vti | ip6ip6 | ipip6 | ip6gre | vti6 | any }
ADDR := { IP_ADDRESS |

    any }
TOS := { STRING | 00..ff |

    inherit |

    inherit/STRING

    |

    inherit/00..ff

}
ELIM := {

    none |

    0..255 }
TTL := { 1..255 |

    inherit }
KEY := { DOTTED_QUAD | NUMBER }
</code></pre>
<h2>Description</h2>
<p><code>tunnel</code> objects are tunnels, encapsulating packets in IP packets and then sending them over the IP infrastructure. The encapsulating (or outer) address family is specified by the <code>-f</code> option. The default is IPv4.</p>
<dl>
<dt><code>ip tunnel add</code></p>
<dd>add a new tunnel</p>
<dt><code>ip tunnel change</code></p>
<dd>change an existing tunnel</p>
<dt><code>ip tunnel delete</code></p>
<dd>destroy a tunnel</p>
<dl>
<dd>
<dl>
<dt><code>name</code><i> NAME </i><code>(default)</code></p>
<dd>select the tunnel device name.</p>
<dt><code>mode</code><i> MODE</i></p>
<dd>set the tunnel mode. Available modes depend on the encapsulating address family.<br />
 Modes for IPv4 encapsulation available: <code>ipip</code>, <code>sit</code>, <code>isatap</code>, <code>vti</code>, and <code>gre</code>.<br />
 Modes for IPv6 encapsulation available: <code>ip6ip6</code>, <code>ipip6</code>, <code>ip6gre</code>, <code>vti6</code>, and <code>any</code>.</p>
<dt><code>remote</code><i> ADDRESS</i></p>
<dd>set the remote endpoint of the tunnel.</p>
<dt><code>local</code><i> ADDRESS</i></p>
<dd>set the fixed local address for tunneled packets. It must be an address on another interface of this host.</p>
<dt><code>ttl</code><i> N</i></p>
<dd>
<dt><code>hoplimit</code><i> N</i></p>
<dd>set a fixed TTL (IPv4) or hoplimit (IPv6) <i>N</i> on tunneled packets. <i>N</i> is a number in the range 1&#8211;255. 0 is a special value meaning that packets inherit the TTL value. The default value for IPv4 tunnels is: <code>inherit</code>. The default value for IPv6 tunnels is: <code>64</code>.</p>
<dt><code>tos</code><i> T</i></p>
<dd>
<dt><code>dsfield</code><i> T</i></p>
<dd>
<dt><code>tclass</code><i> T</i></p>
<dd>set the type of service (IPv4) or traffic class (IPv6) field on tunneled packets, which can be specified as either a two-digit hex value (e.g. c0) or a predefined string (e.g. internet). The value <code>inherit</code> causes the field to be copied from the original IP header. The values <code>inherit/</code><i>STRING</i> or <code>inherit/</code><i>00</i><code>..</code><i>ff</i> will set the field to <i>STRING</i> or <i>00</i>..<i>ff</i> when tunneling non-IP packets. The default value is 00.</p>
<dt><code>dev</code><i> NAME</i></p>
<dd>bind the tunnel to the device <i>NAME</i> so that tunneled packets will only be routed via this device and will not be able to escape to another device when the route to endpoint changes.</p>
<dt><code>nopmtudisc</code></p>
<dd>disable Path MTU Discovery on this tunnel. It is enabled by default. Note that a fixed ttl is incompatible with this option: tunneling with a fixed ttl always makes pmtu discovery.</p>
<dt><code>ignore-df</code></p>
<dd>enable IPv4 DF suppression on this tunnel. Normally datagrams that exceed the MTU will be fragmented; the presence of the DF flag inhibits this, resulting instead in an ICMP Unreachable (Fragmentation Required) message. Enabling this attribute causes the DF flag to be ignored.</p>
<dt><code>key</code><i> K</i></p>
<dd>
<dt><code>ikey</code><i> K</i></p>
<dd>
<dt><code>okey</code><i> K</i></p>
<dd>(<code> only GRE tunnels </code>) use keyed GRE with key <i>K</i>. <i>K</i> is either a number or an IP address-like dotted quad. The <code>key</code> parameter sets the key to use in both directions. The <code>ikey</code> and <code>okey</code> parameters set different keys for input and output.</p>
<dt><code>csum</code>, <code>icsum</code>, <code>ocsum</code></p>
<dd>(<code> only GRE tunnels </code>) generate/require checksums for tunneled packets. The <code>ocsum</code> flag calculates checksums for outgoing packets. The <code>icsum</code> flag requires that all input packets have the correct checksum. The <code>csum</code> flag is equivalent to the combination <code>icsum ocsum</code>.</p>
<dt><code>seq</code>, <code>iseq</code>, <code>oseq</code></p>
<dd>(<code> only GRE tunnels </code>) serialize packets. The <code>oseq</code> flag enables sequencing of outgoing packets. The <code>iseq</code> flag requires that all input packets are serialized. The <code>seq</code> flag is equivalent to the combination <code>iseq oseq</code>. <code>It doesn&#8217;t work. Don&#8217;t use it.</code></p>
<dt><code>encaplimit</code><i> ELIM</i></p>
<dd>(<code> only IPv6 tunnels </code>) set a fixed encapsulation limit. Default is 4.</p>
<dt><code>flowlabel</code><i> FLOWLABEL</i></p>
<dd>(<code> only IPv6 tunnels </code>) set a fixed flowlabel.</p>
<dt><code>allow-localremote</code></p>
<dd>(<code> only IPv6 tunnels </code>) allow remote endpoint on the local host.</dl>
</dl>
<dt><code>ip tunnel prl</code></p>
<dd>potential router list (ISATAP only)</p>
<dl>
<dd>
<dl>
<dt><code>dev</code><i> NAME</i></p>
<dd>mandatory device name.</p>
<dt><code>prl-default</code><i> ADDR</i></p>
<dd>
<dt><code>prl-nodefault</code><i> ADDR</i></p>
<dd>
<dt><code>prl-delete</code><i> ADDR</i></p>
<dd>Add or delete <code>ADDR</code> as a potential router or default router.</dl>
</dl>
<dt><code>ip tunnel show</code></p>
<dd>list tunnels This command has no arguments. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;</p>
