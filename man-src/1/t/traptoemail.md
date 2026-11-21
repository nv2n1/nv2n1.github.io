---
title: "traptoemail(1)"
name: "traptoemail"
section: "1"
letter: "t"
url: "/docs/linux/man/1-traptoemail/"
description: "traptoemail – snmptrapd handler script to convert snmp traps into emails"
---

<h2>NAME</h2>
<p> traptoemail &#8211; snmptrapd handler script to convert snmp traps into emails</p>
<h2>SYNOPSIS</h2>
<p> <code>traptoemail</code> [<i>-f FROM</i>] [<i>-s SMTPSERVER</i>] ADDRESSES</p>
<h2>DESCRIPTION</h2>
<p> converts snmp traps into email messages.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f FROM</code></dt>
<dd> sender address, defaults to &quot;root&quot;</dd>
<dt><code>-s SMTPSERVER</code></dt>
<dd> SMTP server, defaults to &quot;localhost&quot;</dd>
<dt><code>ADDRESSES</code></dt>
<dd> recipient addresses </dd>
</dl>
