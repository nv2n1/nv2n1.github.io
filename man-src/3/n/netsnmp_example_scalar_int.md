---
title: "netsnmp_example_scalar_int(3)"
name: "netsnmp_example_scalar_int"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_example_scalar_int/"
---

example_scalar_int: instantiates a few example scalars. - This example merely creates some scalar registrations that allows some simple variables to be accessed via SNMP. More...

<h3>Functions</h3>

<pre><code>void init_scalar_int (void)</code></pre>

<h2>Detailed Description</h2>

This example merely creates some scalar registrations that allows some simple variables to be accessed via SNMP. 

 In a more realistic example, it is likely that these variables would also be manipulated in other ways outside of SNMP gets/sets. 

 If this module is compiled into an agent, you should be able to issue snmp commands that look something like (authentication information not shown in these commands): 

 snmpget localhost netSnmpExampleInteger.0 netSnmpExampleScalars = 42 

 snmpset localhost netSnmpExampleInteger.0 = 1234 netSnmpExampleScalars = 1234 

 snmpget localhost netSnmpExampleInteger.0 netSnmpExampleScalars = 1234
