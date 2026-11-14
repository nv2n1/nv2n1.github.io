---
title: "snmptest(1)"
name: "snmptest"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmptest/"
description: "snmptest – communicates with a network entity using SNMP requests"
---

<h2>NAME</h2>
<p> snmptest &#8211; communicates with a network entity using SNMP requests</p>
<h2>SYNOPSIS</h2>
<p> <code>snmptest</code> [COMMON OPTIONS] AGENT</p>
<h2>DESCRIPTION</h2>
<p> <code>snmptest</code> is a flexible SNMP application that can monitor and manage information on a network entity. </p>
<p> After invoking the program, a command line interpreter proceeds to accept commands. This intepreter enables the user to send different types of SNMP requests to target agents. </p>
<p> AGENT identifies a target SNMP agent, which is instrumented to monitor the given objects. At its simplest, the AGENT specification will consist of a hostname or an IPv4 address. In this situation, the command will attempt communication with the agent, using UDP/IPv4 to port 161 of the given target host. See <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1) for a full list of the possible formats for AGENT. </p>
<p> Once snmptest is invoked, the command line intepreter will prompt with: </p>
<p> <code>Variable:</code> </p>
<p> At this point you can enter one or more variable names, one per line. A blank line ends the parameter input and will send the request (variables entered) in a single packet, to the remote entity. Each variable name is given in the format specified in <i><a href="/docs/linux/man/5-variables/">variables</a>(5)</i>. For example: </p>
<p> snmptest -c public -v 1 zeus<br />
 <code>Variable:</code> system.sysDescr.0<br />
 <code>Variable:</code> </p>
<p> will return some information about the request and reply packets, as well as the information: </p>
<p> requestid 0x5992478A errstat 0x0 errindex 0x0<br />
 system.sysDescr.0 = STRING: &quot;Unix 4.3BSD&quot; </p>
<p> The errstatus value shows the error status code for the call. The possible values for errstat are in the header file snmp.h. The errindex value identifies the variable that has the given error. Index values are assigned to all the variables entered at the &quot;Variable&quot;: prompt. The first value is assigned an index of 1. </p>
<p> Upon startup, the program defaults to sending a GET request packet. The type of request can be changed by typing one of the following commands at the &quot;Variable:&quot; prompt: </p>
<pre>
$G - send a GET request
$N - send a GETNEXT request
$S - send a SET request
$B - send a GETBULK request
     Note: GETBULK is not available in SNMPv1
$I - send an Inform request
$T - send an SNMPv2 Trap request
</pre>
<p> Other values that can be entered at the &quot;Variable:&quot; prompt are: </p>
<pre>
$D - toggle the dumping of each sent and received packet
$QP - toggle a quicker, less verbose output form
$Q - Quit the program
</pre>
<p> Request Types: </p>
<p> GET Request: </p>
<p> When in &quot;GET request&quot; mode ($G or default), the user can enter an OID at the &quot;Variable:&quot; prompt. The user can enter multiple OIDs, one per prompt. The user enters a blank line to send the GET request. </p>
<p> GETNEXT Request: </p>
<p> The &quot;GETNEXT request&quot; mode ($N) is simlar to the &quot;Get request&quot; mode, described above. </p>
<p> SET Request: </p>
<p> When in the &quot;SET request&quot; mode ($S), more information is requested by the prompt for each variable. The prompt: </p>
<pre>
Type [i|s|x|d|n|o|t|a]:
</pre>
<p> requests the type of the variable be entered. Depending on the type of value you want to set, you can type one of the following: </p>
<pre>
i - integer
u - unsigned integer
s - octet string in ASCII
x - octet string in hex bytes, separated by whitespace
d - octet string as decimal bytes, separated by whitespace
a - ip address in dotted IP notation
o - object identifier
n - null
t - timeticks
</pre>
<p> At this point a value will be prompted for: </p>
<p> Value: </p>
<p> If this is an integer value, just type the integer (in decimal). If it is a decimal string, type in white-space separated decimal numbers, one per byte of the string. Again type a blank line at the prompt for the variable name to send the packet. </p>
<p> GETBULK Request: </p>
<p> The &quot;GETBULK request&quot; mode ($B) is similar to the &quot;Set request&quot; mode. GETBULK, however, is not available in SNMPv1. </p>
<p> Inform Request: </p>
<p> The &quot;Inform request&quot; mode ($I) is similar to the &quot;Set request&quot; mode. This type of request, however, is not available in SNMPv1. Also, the _agent_ specified on the snmptest command should correspond to the target snmptrapd agent. </p>
<p> SNMPv2 Trap Request: </p>
<p> The &quot;SNMPv2 Trap Request&quot; mode ($T) is similar to the &quot;Set request&quot; mode. This type of request, however, is not available in SNMPv1. Also, the _agent_ specified on the snmptest command should correspond to the target snmptrapd agent.</p>
<h2>OPTIONS</h2>
<p> <code>snmptest</code> takes the common options described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page.</p>
<h2>EXAMPLES</h2>
<p> The following is an example of sending a GET request for two OIDs: </p>
<p> % snmptest -v 2c -c public testhost:9999 </p>
<pre>
Variable: system.sysDescr.0
Variable: system.sysContact.0
Variable:
Received Get Response from 128.2.56.220
requestid 0x7D9FCD63 errstat 0x0 errindex 0x0
SNMPv2-MIB::sysDescr.0 = STRING: SunOS testhost 5.9 Generic_112233-02 sun4u
SNMPv2-MIB::sysContact.0 = STRING: x1111
</pre>
<p> The following is an example of sending a GETNEXT request: </p>
<pre>
Variable: SNMPv2-MIB::sysORUpTime
Variable:
Received Get Response from 128.2.56.220
requestid 0x7D9FCD64 errstat 0x0 errindex 0x0
SNMPv2-MIB::sysORUpTime.1 = Timeticks: (6) 0:00:00.06
Variable:
</pre>
<p> The following is an example of sending a SET request: </p>
<pre>
Variable: $S
Request type is Set Request
Variable: system.sysLocation.0
Type [i|u|s|x|d|n|o|t|a]: s
Value: building 17
Variable:
Received Get Response from 128.2.56.220
requestid 0x7D9FCD65 errstat 0x0 errindex 0x0
SNMPv2-MIB::sysLocation.0 = STRING: building A
Variable:
</pre>
<p> The following is an example of sending a GETBULK request: </p>
<pre>
Variable: $B
Request type is Bulk Request
Enter a blank line to terminate the list of non-repeaters
and to begin the repeating variables
Variable:
Now input the repeating variables
Variable: system.sysContact.0
Variable: system.sysLocation.0
Variable:
What repeat count? 2
Received Get Response from 128.2.56.220
requestid 0x2EA7942A errstat 0x0 errindex 0x0
SNMPv2-MIB::sysName.0 = STRING: testhost
SNMPv2-MIB::sysORLastChange.0 = Timeticks: (58) 0:00:00.58
SNMPv2-MIB::sysLocation.0 = STRING: bldg A
SNMPv2-MIB::sysORID.1 = OID: IF-MIB::ifMIB
Variable:
</pre>
<p> The following is an example of sending an Inform request: </p>
<pre>
snmptest -v 2c -c public snmptrapd_host
Variable: $I
Request type is Inform Request
(Are you sending to the right port?)
Variable: system.sysContact.0
Type [i|u|sIx|d|n|o|t|a]: s
Value: x12345
Variable:
Inform Acknowledged
Variable:
</pre>
<p> The snmptrapd_host will show: </p>
<p> snmptrapd_host [&lt;ip address&gt;]: Trap SNMPv2-MIB::sysContact.0 = STRING: x12345 </p>
<p> The following is an example of sending an SNMPv2 Trap request: </p>
<pre>
snmptest -v 2c -c public snmptrapd_host
Variable: $T
Request type is SNMPv2 Trap Request
(Are you sending to the right port?)
Variable: system.sysLocation.0
Type [i|u|s|x|d|n|o|t|a]: s
Value: building a
Variable:
</pre>
<p> The snmptrapd_host will show: </p>
<pre>
snmptrapd_host [&lt;ip address&gt;]: Trap SNMPv2-MIB::sys.0 = STRING:
building a
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/1-snmpget/">snmpget</a>(1), <a href="/docs/linux/man/1-snmpset/">snmpset</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5) </p>
<h2>Index</h2>
