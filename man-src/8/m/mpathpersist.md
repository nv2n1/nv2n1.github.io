---
title: "mpathpersist(8)"
name: "mpathpersist"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mpathpersist/"
description: "mpathpersist"
---

<p>mpathpersist</p>
<h2>Synopsis</h2>
<p><code>mpathpersist</code> [<i>OPTIONS</i>] [<i>DEVICE</i>]</p>
<h2>Description</h2>
<dl>
<dd>Options:</p>
<dt><code>&#8211;verbose</code>|-v level</p>
<dd>verbosity level</p>
<dt>0</p>
<dd>Critical and error messages</p>
<dt>1</p>
<dd>Warning messages</p>
<dt>2</p>
<dd>Informational messages</p>
<dt>3</p>
<dd>Informational messages with trace enabled</p>
<dt><code>&#8211;clear</code>|-C</p>
<dd>PR Out: Clear</p>
<dt><code>&#8211;device</code>=<i>DEVICE</i>|-d DEVICE</p>
<dd>query or change DEVICE</p>
<dt><code>&#8211;help</code>|-h</p>
<dd>output this usage message</p>
<dt><code>&#8211;hex</code>|-H</p>
<dd>output response in hex</p>
<dt><code>&#8211;in</code>|-i</p>
<dd>request PR In command</p>
<dt><code>&#8211;out</code>|-o</p>
<dd>request PR Out command</p>
<dt><code>&#8211;param-aptpl</code>|-Z</p>
<dd>PR Out parameter &#8216;APTPL&#8217;</p>
<dt><code>&#8211;read-keys</code>|-k</p>
<dd>PR In: Read Keys</p>
<dt><code>&#8211;param-sark</code>=<i>SARK</i>|-S SARK</p>
<dd>PR Out parameter service action reservation key (SARK is in hex)</p>
<dt><code>&#8211;preempt</code>|-P</p>
<dd>PR Out: Preempt</p>
<dt><code>&#8211;preempt-abort</code>|-A</p>
<dd>PR Out: Preempt and Abort</p>
<dt><code>&#8211;prout-type</code>=<i>TYPE</i>|-T TYPE</p>
<dd>PR Out command type</p>
<dt><code>&#8211;read-status</code>|-s</p>
<dd>PR In: Read Full Status</p>
<dt><code>&#8211;read-keys</code>|-k</p>
<dd>PR In: Read Keys</p>
<dt><code>&#8211;read-reservation</code>|-r</p>
<dd>PR In: Read Reservation</p>
<dt><code>&#8211;register</code>|-G</p>
<dd>PR Out: Register</p>
<dt><code>&#8211;register-ignore</code>|-I</p>
<dd>PR Out: Register and Ignore</p>
<dt><code>&#8211;release</code>|-L</p>
<dd>PR Out: Release</p>
<dt><code>&#8211;report-capabilities</code>|-c</p>
<dd>PR In: Report Capabilities</p>
<dt><code>&#8211;reserve</code>|-R</p>
<dd>PR Out: Reserve</p>
<dt><code>&#8211;transport-id</code>=<i>TIDS</i>|-X TIDS</p>
<dd>TransportIDs can be mentioned in several forms</p>
<dd>Examples:</p>
<dd>mpathpersist <code>&#8211;out</code> <code>&#8211;register</code> <code>&#8211;param-sark</code>=<i>123abc</i> <code>&#8211;prout-type</code>=<i>5</i> /dev/mapper/mpath9 mpathpersist <code>-i</code> <code>-k</code> /dev/mapper/mpath9</dl>
