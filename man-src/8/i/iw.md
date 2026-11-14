---
title: "iw(8)"
name: "iw"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iw/"
description: "iw – show / manipulate wireless devices and their configuration"
---

<p>iw &#8211; show / manipulate wireless devices and their configuration</p>
<h2>Synopsis</h2>
<pre><code>iw

[ OPTIONS ] {

    help [

    command ]

    |

    OBJECT COMMAND }

OBJECT := {

    dev | phy | reg }

OPTIONS := { --version | --debug }
</code></pre>
<h2>Options</h2>
<dl>
<dt><code> &#8211;version</code></p>
<dd>print version information and exit. </p>
<dt><code> &#8211;debug</code></p>
<dd>enable netlink message debugging. </p>
</dl>
<h2>Iw &#8211; Command Syntax</h2>
<h3><i>OBJECT</i></h3>
<dl>
<dt><code>dev &lt;interface name&gt;</code></p>
<dd>&#8211; network interface. </p>
<dt><code>phy &lt;phy name&gt;</code></p>
<dd>&#8211; wireless hardware device (by name).</p>
<dt><code>phy#&lt;phy index&gt;</code></p>
<dd>&#8211; wireless hardware device (by index). </p>
<dt><code>reg</code></p>
<dd>&#8211; regulatory agent. </p>
</dl>
<h3><i>COMMAND</i></h3>
<p>Specifies the action to perform on the object. The set of possible actions depends on the object type. <code>iw help</code> will print all supported commands, while <code>iw help command</code> will print the help for all matching commands.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-crda/">crda</a></code>(8), <code><a href="/docs/linux/man/8-regdbdump/">regdbdump</a></code>(8), <code><a href="/docs/linux/man/5-regulatory-bin/">regulatory.bin</a></code>(5) <code><a rel="nofollow" href="http://wireless.kernel.org/en/users/Documentation/iw">http://wireless.kernel.org/en/users/Documentation/iw</a></code> </p>
