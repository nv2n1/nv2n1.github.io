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
<dt>-d</dt>
<dd>Enable printing of debugging informations. </dd>
<dt>nas-type</dt>
<dd>Type of port/NAS. Can be one of: </dd>
<dl>
<dd>
</dd><dl>
<dt>&bull;</dt>
<dd>ascend</dd>
<dt>&bull;</dt>
<dd>bay</dd>
<dt>&bull;</dt>
<dd>cisco</dd>
<dt>&bull;</dt>
<dd>cisco_l2tp</dd>
<dt>&bull;</dt>
<dd>computone</dd>
<dt>&bull;</dt>
<dd>cvx</dd>
<dt>&bull;</dt>
<dd>digitro</dd>
<dt>&bull;</dt>
<dd>dot1x</dd>
<dt>&bull;</dt>
<dd>livingston</dd>
<dt>&bull;</dt>
<dd>max40xx</dd>
<dt>&bull;</dt>
<dd>mikrotik</dd>
<dt>&bull;</dt>
<dd>mikrotik_snmp</dd>
<dt>&bull;</dt>
<dd>multitech</dd>
<dt>&bull;</dt>
<dd>netserver</dd>
<dt>&bull;</dt>
<dd>other</dd>
<dt>&bull;</dt>
<dd>pathras</dd>
<dt>&bull;</dt>
<dd>patton</dd>
<dt>&bull;</dt>
<dd>portslave</dd>
<dt>&bull;</dt>
<dd>pr3000</dd>
<dt>&bull;</dt>
<dd>pr4000</dd>
<dt>&bull;</dt>
<dd>redback</dd>
<dt>&bull;</dt>
<dd>tc</dd>
<dt>&bull;</dt>
<dd>usrhiper</dd>
<dt>&bull;</dt>
<dd>versanet</dd></dl>
<p> The &quot;other&quot; type cause <code>checkrad</code> to skip any check and always returns 1.</dl>
<dt>nas-ip</dt>
<dd>IP address of the NAS to check. </dd>
<dt>nas-port</dt>
<dd>The NAS port to check (may be ignored by some nas-type). </dd>
<dt>login</dt>
<dd>The login name to check. </dd>
<dt>session-id</dt>
<dd>Session to check. (actually ignored by all nas-type) </dd>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-radiusd/">radiusd</a>(8) </p>
<h2>Author</h2>
<p>Written by Miquel van Smoorenburg, miquels [at] cistron.nl. </p>
<p> This manual page was written by Marco Nenciarini &lt;mnencia [at] debian.org&gt; for the Debian project (but may be used by others).</p>
