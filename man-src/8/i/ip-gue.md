---
title: "ip-gue(8)"
name: "ip-gue"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-gue/"
description: "ip-fou – Foo-over-UDP receive port configuration"
---

<p>ip-fou &#8211; Foo-over-UDP receive port configuration </p>
<p> ip-gue &#8211; Generic UDP Encapsulation receive port configuration</p>
<h2>Synopsis</h2>
<pre><code>ip

[ OPTIONS ]

fou

{ COMMAND |

    help }</code></pre>
<p> <code>ip fou add</code> <code>port</code> <i>PORT</i> { <code>gue</code> | <code>ipproto</code> <i>PROTO</i> } [ <code>local</code> <i>IFADDR</i> ] [ <code>peer</code> <i>IFADDR</i> ] [ <code>peer_port</code> <i>PORT</i> ] [ <code>dev</code> <i>IFNAME</i> ] </p>
<p> <code>ip fou del</code> <code>port</code> <i>PORT</i> [ <code>local</code> <i>IFADDR</i> ] [ <code>peer</code> <i>IFADDR</i> ] [ <code>peer_port</code> <i>PORT</i> ] [ <code>dev</code> <i>IFNAME</i> ] </p>
<p> <code>ip fou show</code></p>
<h2>Description</h2>
<p>The <code>ip fou</code> commands are used to create and delete receive ports for Foo-over-UDP (FOU) as well as Generic UDP Encapsulation (GUE). </p>
<p> Foo-over-UDP allows encapsulating packets of an IP protocol directly over UDP. The receiver infers the protocol of a packet received on a FOU UDP port to be the protocol configured for the port. </p>
<p> Generic UDP Encapsulation (GUE) encapsulates packets of an IP protocol within UDP and an encapsulation header. The encapsulation header contains the IP protocol number for the encapsulated packet. </p>
<p> When creating a FOU or GUE receive port, the port number is specified in <i>PORT</i> argument. If FOU is used, the IP protocol number associated with the port is specified in <i>PROTO</i> argument. You can bind a port to a local address/interface, by specifying the address in the local <i>IFADDR</i> argument or the device in the <i>IFNAME</i> argument. If you would like to connect the port, you can specify the peer address in the peer <i>IFADDR</i> argument and peer port in the peer_port <i>PORT</i> argument. </p>
<p> A FOU or GUE receive port is deleted by specifying <i>PORT</i> in the delete command, as well as local address/interface or peer address/port (if set).</p>
<h2>Examples</h2>
<h3>Configure a FOU receive port for GRE bound to 7777</h3>
<pre># ip fou add port 7777 ipproto 47</pre>
<h3>Configure a FOU receive port for IPIP bound to 8888</h3>
<pre># ip fou add port 8888 ipproto 4</pre>
<h3>Configure a GUE receive port bound to 9999</h3>
<pre># ip fou add port 9999 gue</pre>
<h3>Delete the GUE receive port bound to 9999</h3>
<pre># ip fou del port 9999</pre>
<h3>Configure a FOU receive port for GRE bound to 1.2.3.4:7777</h3>
<pre># ip fou add port 7777 ipproto 47 local 1.2.3.4</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8)</p>
<h2>Author</h2>
<p>Tom Herbert &lt;therbert [at] google.com&gt;</p>
