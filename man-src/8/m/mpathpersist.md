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
<dd>Options:</dd>
<dt><code>&#8211;verbose</code>|-v level</dt>
<dd>verbosity level</dd>
<dt>0</dt>
<dd>Critical and error messages</dd>
<dt>1</dt>
<dd>Warning messages</dd>
<dt>2</dt>
<dd>Informational messages</dd>
<dt>3</dt>
<dd>Informational messages with trace enabled</dd>
<dt><code>&#8211;clear</code>|-C</dt>
<dd>PR Out: Clear</dd>
<dt><code>&#8211;device</code>=<i>DEVICE</i>|-d DEVICE</dt>
<dd>query or change DEVICE</dd>
<dt><code>&#8211;help</code>|-h</dt>
<dd>output this usage message</dd>
<dt><code>&#8211;hex</code>|-H</dt>
<dd>output response in hex</dd>
<dt><code>&#8211;in</code>|-i</dt>
<dd>request PR In command</dd>
<dt><code>&#8211;out</code>|-o</dt>
<dd>request PR Out command</dd>
<dt><code>&#8211;param-aptpl</code>|-Z</dt>
<dd>PR Out parameter &#8216;APTPL&#8217;</dd>
<dt><code>&#8211;read-keys</code>|-k</dt>
<dd>PR In: Read Keys</dd>
<dt><code>&#8211;param-sark</code>=<i>SARK</i>|-S SARK</dt>
<dd>PR Out parameter service action reservation key (SARK is in hex)</dd>
<dt><code>&#8211;preempt</code>|-P</dt>
<dd>PR Out: Preempt</dd>
<dt><code>&#8211;preempt-abort</code>|-A</dt>
<dd>PR Out: Preempt and Abort</dd>
<dt><code>&#8211;prout-type</code>=<i>TYPE</i>|-T TYPE</dt>
<dd>PR Out command type</dd>
<dt><code>&#8211;read-status</code>|-s</dt>
<dd>PR In: Read Full Status</dd>
<dt><code>&#8211;read-keys</code>|-k</dt>
<dd>PR In: Read Keys</dd>
<dt><code>&#8211;read-reservation</code>|-r</dt>
<dd>PR In: Read Reservation</dd>
<dt><code>&#8211;register</code>|-G</dt>
<dd>PR Out: Register</dd>
<dt><code>&#8211;register-ignore</code>|-I</dt>
<dd>PR Out: Register and Ignore</dd>
<dt><code>&#8211;release</code>|-L</dt>
<dd>PR Out: Release</dd>
<dt><code>&#8211;report-capabilities</code>|-c</dt>
<dd>PR In: Report Capabilities</dd>
<dt><code>&#8211;reserve</code>|-R</dt>
<dd>PR Out: Reserve</dd>
<dt><code>&#8211;transport-id</code>=<i>TIDS</i>|-X TIDS</dt>
<dd>TransportIDs can be mentioned in several forms</dd>
<dd>Examples:</dd>
<dd>mpathpersist <code>&#8211;out</code> <code>&#8211;register</code> <code>&#8211;param-sark</code>=<i>123abc</i> <code>&#8211;prout-type</code>=<i>5</i> /dev/mapper/mpath9 mpathpersist <code>-i</code> <code>-k</code> /dev/mapper/mpath9</dd></dl>
