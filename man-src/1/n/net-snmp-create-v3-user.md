---
title: "net-snmp-create-v3-user(1)"
name: "net-snmp-create-v3-user"
section: "1"
letter: "n"
url: "/docs/linux/man/1-net-snmp-create-v3-user/"
description: "net-snmp-create-v3-user – create a SNMPv3 user in net-snmp configuration file"
---

<h2>NAME</h2>
<p> net-snmp-create-v3-user &#8211; create a SNMPv3 user in net-snmp configuration file</p>
<h2>SYNOPSIS</h2>
<p> <code>net-snmp-create-v3-user [-ro] [-a authpass] [-x privpass] [-X DES|AES]</code> <code>[username]</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>net-snmp-create-v3-user</i> shell script is designed to create a new user in net-snmp configuration file (/var/net-snmp/snmpd.conf by default). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> displays the net-snmp version number</p>
<dt><code>-ro</code></p>
<dd> create an user with read-only permissions</p>
<dt><code>-a authpass</code></p>
<dd> specify authentication password</p>
<dt><code>-x privpass</code></p>
<dd> specify encryption password</p>
<dt><code>-X DES|AES</code></p>
<dd> specify encryption algorithm </p>
</dl>
<h2>Index</h2>
