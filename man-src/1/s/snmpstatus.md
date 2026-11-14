---
title: "snmpstatus(1)"
name: "snmpstatus"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpstatus/"
description: "snmpstatus – retrieves a fixed set of management information from a network entity"
---

<h2>NAME</h2>
<p> snmpstatus &#8211; retrieves a fixed set of management information from a network entity</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpstatus</code> [COMMON OPTIONS] [-Cf] AGENT</p>
<h2>DESCRIPTION</h2>
<p> <code>snmpstatus</code> is an SNMP application that retrieves several important statistics from a network entity. </p>
<p> AGENT identifies a target SNMP agent, which is instrumented to monitor the given objects. At its simplest, the AGENT specification will consist of a hostname or an IPv4 address. n this situation, the command will attempt communication with the agent, using UDP/IPv4 to port 161 of the given target host. </p>
<p> See the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page for a full list of the possible formats for AGENT. </p>
<p> The information returned is:</p>
<dl>
<dt>
<dd> The IP address of the entity.<br />
 A textual description of the entity (sysDescr.0)<br />
 The uptime of the entity&#8217;s SNMP agent (sysUpTime.0)<br />
 The sum of received packets on all interfaces (ifInUCastPkts.* + ifInNUCastPkts.*)<br />
 The sum of transmitted packets on all interfaces (ifOutUCastPkts.* + ifOutNUCastPkts.*)<br />
 The number of IP input packets (ipInReceives.0)<br />
 The number of IP output packets (ipOutRequests.0)</dl>
<p> For example: </p>
<p> snmpstatus -c public -v 1 netdev-kbox.cc.cmu.edu </p>
<p> will produce output similar to the following: </p>
<p> [128.2.56.220]=&gt;[Kinetics FastPath2] Up: 1 day, 4:43:31<br />
 Interfaces: 1, Recv/Trans packets: 262874/39867 | IP: 31603/15805 </p>
<p> <code>snmpstatus</code> also checks the operational status of all interfaces (ifOperStatus.*), and if it finds any that are not running, it will report in a manner similar to this: </p>
<p> 2 interfaces are down! </p>
<p> If the network entity has an error processing the request packet, an error packet will be returned and a message will be shown, helping to pinpoint in what way the request was malformed. <code>snmpstatus</code> will attempt to reform its request to eliminate the malformed variable (unless the <code>-Cf</code> option is given, see below), but this variable will then be missing from the displayed data. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>COMMON OPTIONS</code></p>
<dd> Please see <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for a list of possible values for COMMON OPTIONS as well as their descriptions.</p>
<dt><code>-Cf</code></p>
<dd> By default, snmpstatus will try to fix errors returned by the agent and retry a request. In this situation, the command will display the data that it can. If the -Cf option is specified, then snmpstatus will not try to fix errors, and the error will cause the command to terminate.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/1-snmpget/">snmpget</a>(1) </p>
<h2>Index</h2>
