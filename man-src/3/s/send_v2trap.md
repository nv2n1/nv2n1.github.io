---
title: "send_v2trap(3)"
name: "send_v2trap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-send_v2trap/"
description: "send_easy_trap, send_trap_vars, send_v2trap – send TRAPs or INFORMs from a Net-SNMP MIB module"
---

<p>send_easy_trap, send_trap_vars, send_v2trap &#8211; send TRAPs or INFORMs from a Net-SNMP MIB module</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/agent/agent_trap.h&gt;
void send_easy_trap(int trap, int specific);
void send_trap_vars(int trap, int specific, struct variable_list *vars);
void send_v2trap(struct variable_list *vars);</code></pre>
<h2>Description</h2>
<p>These three routines may be used to send traps from a MIB module within the Net-SNMP agent (including an AgentX subagent). </p>
<p> <code>send_easy_trap()</code> sends an SNMPv1 trap (or the SNMPv2 equivalent) to the list of configured trap destinations (or &quot;sinks&quot;), using the provided values for the generic trap type, and specific trap value. </p>
<p> <code>send_trap_vars()</code> is similar, but appends the supplied list of variable bindings to the traps that are sent. </p>
<p> <code>send_v2trap()</code> uses the supplied list of variable bindings to form an SNMPv2 trap, which is sent to SNMPv2-capable sinks on the configured list. An equivalent INFORM is sent to the configuredq list of inform sinks. Sinks that can only handle SNMPv1 traps are skipped. </p>
<p> The various &quot;send_trap()&quot; calls allow you to specify traps in different formats. And the various &quot;trapsink&quot; directives allow you to specify destinations to receive different formats. But *all* traps are sent to *all* destinations, regardless of how they were specified. </p>
<pre>I.e. it's
 ___ trapsink
 /
 send_easy_trap ___ [ Trap ] ____ trap2sink
 ___ [ Generator ]
 send_v2trap / [ ] ----- informsink
 ____
 trapsess
*Not*
 send_easy_trap -------------------&gt; trapsink
 send_v2trap -------------------&gt; trap2sink
 ???? -------------------&gt; informsink
 ???? -------------------&gt; trapsess</pre>
<h2>Warnings</h2>
<p>These routines are used to send the traps immediately they are called. Invoking them at the appropriate time is left to the MIB module programmer.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a></code>(5), <code><a href="/docs/linux/man/8-snmptrapd/">snmptrapd</a></code>(8) </p>
