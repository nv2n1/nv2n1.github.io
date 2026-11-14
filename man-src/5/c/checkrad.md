---
title: "checkrad(5)"
name: "checkrad"
section: "5"
letter: "c"
url: "/docs/linux/man/5-checkrad/"
description: "checkrad — See if a user is (still) logged in on a certain port."
---

<p>checkrad &#8212; See if a user is (still) logged in on a certain port.</p>
<h2>Synopsis</h2>
<p><code>checkrad</code> [<code>-d</code>] <i>nas-type nas-ip nas-port login session-id</i></p>
<h2>Description</h2>
<p><code>Checkrad</code> is used by the radius server to check if its idea of a user logged in on a certain port/NAS is correct if a double login is detected. Returns: 0 = no duplicate, 1 = duplicate, &gt;1 = error. </p>
<h2>Options</h2>
<dl>
<dt>-d</p>
<dd>Enable printing of debugging informations. </p>
<dt>nas-type</p>
<dd>Type of port/NAS. Can be one of: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>ascend</p>
<dt>&bull;</p>
<dd>bay</p>
<dt>&bull;</p>
<dd>cisco</p>
<dt>&bull;</p>
<dd>cisco_l2tp</p>
<dt>&bull;</p>
<dd>computone</p>
<dt>&bull;</p>
<dd>cvx</p>
<dt>&bull;</p>
<dd>digitro</p>
<dt>&bull;</p>
<dd>dot1x</p>
<dt>&bull;</p>
<dd>livingston</p>
<dt>&bull;</p>
<dd>max40xx</p>
<dt>&bull;</p>
<dd>mikrotik</p>
<dt>&bull;</p>
<dd>mikrotik_snmp</p>
<dt>&bull;</p>
<dd>multitech</p>
<dt>&bull;</p>
<dd>netserver</p>
<dt>&bull;</p>
<dd>other</p>
<dt>&bull;</p>
<dd>pathras</p>
<dt>&bull;</p>
<dd>patton</p>
<dt>&bull;</p>
<dd>portslave</p>
<dt>&bull;</p>
<dd>pr3000</p>
<dt>&bull;</p>
<dd>pr4000</p>
<dt>&bull;</p>
<dd>redback</p>
<dt>&bull;</p>
<dd>tc</p>
<dt>&bull;</p>
<dd>usrhiper</p>
<dt>&bull;</p>
<dd>versanet</dl>
<p> The &quot;other&quot; type cause <code>checkrad</code> to skip any check and always returns 1.</dl>
<dt>nas-ip</p>
<dd>IP address of the NAS to check. </p>
<dt>nas-port</p>
<dd>The NAS port to check (may be ignored by some nas-type). </p>
<dt>login</p>
<dd>The login name to check. </p>
<dt>session-id</p>
<dd>Session to check. (actually ignored by all nas-type) </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-radiusd/">radiusd</a>(8) </p>
<h2>Author</h2>
<p>Written by Miquel van Smoorenburg, miquels [at] cistron.nl. </p>
<p> This manual page was written by Marco Nenciarini &lt;mnencia [at] debian.org&gt; for the Debian project (but may be used by others).</p>
