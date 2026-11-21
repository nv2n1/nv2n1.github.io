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
<p> <code>net-snmp-create-v3-user [-ro] [-a authpass] [-x privpass] [-X DES|AES]</code> <code>[username]</code></p>
<p> The <i>net-snmp-create-v3-user</i> shell script is designed to create a new user in net-snmp configuration file (/var/net-snmp/snmpd.conf by default). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> displays the net-snmp version number</dd>
<dt><code>-ro</code></dt>
<dd> create an user with read-only permissions</dd>
<dt><code>-a authpass</code></dt>
<dd> specify authentication password</dd>
<dt><code>-x privpass</code></dt>
<dd> specify encryption password</dd>
<dt><code>-X DES|AES</code></dt>
<dd> specify encryption algorithm </dd>
</dl>
