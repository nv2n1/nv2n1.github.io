---
title: "snmpd-internal(5)"
name: "snmpd-internal"
section: "5"
letter: "s"
url: "/docs/linux/man/5-snmpd-internal/"
---

snmpd.internal - internal configuration of the Net-SNMP agent

<h2>Description</h2>

The <i><a HREF="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> man page defines the syntax and behaviour of the main configuration directives that can be used to control the operation of the Net-SNMP agent, and the management information it provides. 

 However there are several other configuration directives (many of which, though not all, start with a leading underscore) that are recognised by the agent. These are typically used to retain configuration across agent restarts, and are not intended for direct user access. This man page list these directives, giving a brief indication of where they are used. For full details - see the relevant source files. If you can't follow that source, you probably shouldn't be fiddling with these directives!

<h2>Agent Behaviour</h2>

<dl><dt>quit
<dd></dl>

<h2>Access Control</h2>

<h3>VACM Configuration</h3>

<dl><dt>vacmView / vacmGroup / vacmAccess
<dd>These directives are used to retain dynamically configured access control settings.</dl>

<h2>System Information</h2>

<h3>System Group</h3>

<dl><dt>setSerialNo
<dd>This directive is used to implement the advisory lock object snmpSetSerialNo.
<dt>psyslocation / psyscontact / psysname
<dd>These directives are used to retain dynamically configured system settings. They will be overridden by the corresponding <i>sysLocation</i>, <i>sysContact</i> and <i>sysName</i> directives.</dl>

<h2>Active Monitoring</h2>

<h3>Notification Handling</h3>

<dl><dt>pauthtrapenable
<dd>This directive is used to retain the dynamically configured setting of whether the agent should generate authenticationFailure traps. It will be overridden by the corresponding <i>authtrapenable</i> directive.
<dt>snmpNotify*Table
<dd><dt>targetAddr / targetParams
<dd>These directives are used to retain dynamically configured notification destination settings.</dl>

<h3>DisMan Event MIB</h3>

<dl><dt>_mteE*Table, _mteOTable, _mteT*Table
<dd>These directives are used to retain dynamically configured event, object and monitor trigger settings.
<dt>mteObjectsTable / mteTriggerTable
<dd>These directives are for compatibility with the previous <i>disman/event-mib</i> implementation.</dl>

<h3>DisMan Schedule MIB</h3>

<dl><dt>_schedTable
<dd>This directive is used to retain dynamically configured scheduled events.</dl>

<h2>Extending Agent Functionality</h2>

<h3>Arbitrary Extension Commands</h3>

<dl><dt>extend-sh
<dd><dt>exec2 / sh2 / execFix2
<dd>These directives were defined by analogy with equivalent directives in the previous <i>ucd-snmp/extensible</i> implementation. They are deprecated, and should not be used.</dl>

<h2>Files</h2>

/etc/snmp/snmpd.conf

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-snmpconf/">snmpconf</a>(1), <a HREF="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5), <a HREF="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5), <a HREF="/docs/linux/man/5-snmp_config/">snmp_config</a>(5), <a HREF="/docs/linux/man/8-snmpd/">snmpd</a>(8), EXAMPLE.conf, <a HREF="/docs/linux/man/3-netsnmp_config_api/">netsnmp_config_api</a>(3). 
