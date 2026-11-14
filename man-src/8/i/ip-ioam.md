---
title: "ip-ioam(8)"
name: "ip-ioam"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-ioam/"
description: "ip-ioam – IPv6 In-situ OAM (IOAM)"
---

<p>ip-ioam &#8211; IPv6 In-situ OAM (IOAM)</p>
<h2>Synopsis</h2>
<pre><code>ip ioam

{ COMMAND |

    help }
</code></pre>
<p> <code>ip ioam namespace show</code><br />
 <code>ip ioam namespace add</code> <i>ID</i> <code> [ </code> <code>data</code> <i>DATA32</i> <code>]</code> <code> [ </code> <code>wide</code> <i>DATA64</i> <code>]</code><br />
 <code>ip ioam namespace del</code> <i>ID</i><br />
 <code>ip ioam schema show</code><br />
 <code>ip ioam schema add</code> <i>ID DATA</i><br />
 <code>ip ioam schema del</code> <i>ID</i> </p>
<pre><code>ip ioam namespace set

ID

schema

{ ID |

    none }
</code></pre>
<h2>Description</h2>
<p>The <code>ip ioam</code> command is used to configure IPv6 In-situ OAM (IOAM6) internal parameters, namely IOAM namespaces and schemas. Those parameters also include the mapping between an IOAM namespace and an IOAM schema. </p>
<h2>Examples</h2>
<h3>Configure an IOAM namespace (ID = 1) with both data (32 bits) and wide data (64 bits)</h3>
<pre># ip ioam namespace add 1 data 0xdeadbeef wide 0xcafec0caf00dc0de</pre>
<h3>Link an existing IOAM schema (ID = 7) to an existing IOAM namespace (ID = 1)</h3>
<pre># ip ioam namespace set 1 schema 7</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip-route/">ip-route</a></code>(8)</p>
<h2>Author</h2>
<p>Justin Iurman &lt;justin.iurman [at] uliege.be&gt;</p>
