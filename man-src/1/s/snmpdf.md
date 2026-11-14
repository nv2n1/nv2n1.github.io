---
title: "snmpdf(1)"
name: "snmpdf"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpdf/"
description: "snmpdf – display disk space usage on a network entity via SNMP"
---

<h2>NAME</h2>
<p> snmpdf &#8211; display disk space usage on a network entity via SNMP</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpdf</code> [COMMON OPTIONS] [-Cu] AGENT</p>
<h2>DESCRIPTION</h2>
<p> <code>snmpdf</code> is simply a networked version of the typical df command. It checks the disk space on the remote machine by examining the HOST-RESOURCES-MIB&#8217;s hrStorageTable or the UCD-SNMP-MIB&#8217;s dskTable. By default, the hrStorageTable is preferred as it typically contains more information. However, the -Cu argument can be passed to snmpdf to force the usage of the dskTable. </p>
<p> AGENT identifies a target SNMP agent, which is instrumented to monitor the gievn objects. At its simplest, the AGENT specification will consist of a hostname or an IPv4 address. In this situation, the command will attempt communication with the agent, using UDP/IPv4 to port 161 of the given target host. See the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page for a full list of the possible formats for AGENT. </p>
<p> See the <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> manual page on setting up the dskTable using the <i>disk</i> directive in the snmpd.conf file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>COMMON OPTIONS</code></p>
<dd> Please see <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for a list of possible values for COMMON OPTIONS as well as their descriptions.</p>
<dt><code>-Cu</code></p>
<dd> Forces the command to use dskTable in mib UCD-SNMP-MIB instead of the default to determine the storage information. Generally, the default use of hrStorageTable in mib HOST-RESOURCES-MIB is preferred because it typically contains more information.</dl>
<h2>EXAMPLES</h2>
<p> % snmpdf -v 2c -c public localhost </p>
<pre>
Description       size (kB)         Used    Available Used%
/                   7524587      2186910      5337677   29%
/proc                     0            0            0    0%
/etc/mnttab               0            0            0    0%
/var/run            1223088           32      1223056    0%
/tmp                1289904        66848      1223056    5%
/cache               124330         2416       121914    1%
/vol                      0            0            0    0%
Real Memory          524288       447456        76832   85%
Swap Space          1420296       195192      1225104   13%
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5), <a href="/docs/linux/man/5-snmp-conf/">snmp.conf</a>(5) </p>
<h2>Index</h2>
