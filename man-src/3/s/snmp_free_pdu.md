---
title: "snmp_free_pdu(3)"
name: "snmp_free_pdu"
section: "3"
letter: "s"
url: "/docs/linux/man/3-snmp_free_pdu/"
description: "snmp_pdu_create, snmp_clone_pdu, snmp_fix_pdu, snmp_free_pdu – netsnmp_pdu_api functions"
---

<p>snmp_pdu_create, snmp_clone_pdu, snmp_fix_pdu, snmp_free_pdu &#8211; netsnmp_pdu_api functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/pdu_api.h&gt;</code></pre>
<p> <code>netsnmp_pdu *snmp_pdu_create( int</code><i>type</i><code>);</code> <code>netsnmp_pdu *snmp_clone_pdu( netsnmp_pdu*</code><i>pdu</i><code>);</code> <code>netsnmp_pdu *snmp_fix_pdu( netsnmp_pdu*</code><i>pdu</i><code>, int </code><i>idx</i><code>);</code> <code>netsnmp_pdu *snmp_free_pdu( netsnmp_pdu*</code><i>pdu</i><code>);</code> </p>
<h2>Description</h2>
<p>These functions deal with SNMP request structures. </p>
<p> <code>snmp_pdu_create</code> </p>
<p> <code>snmp_clone_pdu</code> </p>
<p> <code>snmp_fix_pdu</code> </p>
<p> <code>snmp_free_pdu</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-varbind_api/">varbind_api</a></code>(3) <code><a href="/docs/linux/man/3-session_api/">session_api</a></code>(3) </p>
