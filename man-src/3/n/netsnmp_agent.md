---
title: "netsnmp_agent(3)"
name: "netsnmp_agent"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_agent/"
description: "The Net-SNMP agent – The snmp agent responds to SNMP queries from management stations."
---

<p>The Net-SNMP agent &#8211; The snmp agent responds to SNMP queries from management stations.</p>
<h3>Modules</h3>
<p><code>Net-SNMP Agent handler and extensibility API</code><br />
 <i>The basic theory goes something like this: In the past, with the original mib module api (which derived from the original CMU SNMP code) the underlying mib modules were passed very little information (only the truly most basic information about a request). </i> </p>
<p> <code>Maintain a registry of MIB subtrees, together with related information regarding mibmodule, sessions, etc</code> </p>
<p> <code>Trap generation routines for mib modules to use</code> </p>
<p> <code>net-snmp agent related processing</code></p>
<h2>Detailed Description</h2>
<p>The snmp agent responds to SNMP queries from management stations.</p>
