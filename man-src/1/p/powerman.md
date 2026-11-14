---
title: "powerman(1)"
name: "powerman"
section: "1"
letter: "p"
url: "/docs/linux/man/1-powerman/"
description: "powerman – power on/off nodes"
---

<h2>NAME</h2>
<p> powerman &#8211; power on/off nodes</p>
<h2>SYNOPSIS</h2>
<p> <code>pm</code> <i>[-options] -action [targets] [-action [targets] &#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>powerman</code> provides power management in a data center or compute cluster environment. It performs operations such as power on, power off, and power cycle via remote power controller (RPC) devices. Target hostnames are mapped to plugs on RPC devices in <i><a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a>(5).</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-1, &#8211;on targets</i></p>
<dd> Power ON targets.</p>
<dt><i>-0, &#8211;off targets</i></p>
<dd> Power OFF targets.</p>
<dt><i>-c, &#8211;cycle targets</i></p>
<dd> Power cycle targets.</p>
<dt><i>-r, &#8211;reset targets</i></p>
<dd> Assert hardware reset for targets (if implemented by RPC).</p>
<dt><i>-f, &#8211;flash targets</i></p>
<dd> Turn beacon ON for targets (if implemented by RPC).</p>
<dt><i>-u, &#8211;unflash targets</i></p>
<dd> Turn beacon OFF for targets (if implemented by RPC).</p>
<dt><i>-l, &#8211;list</i></p>
<dd> List available targets. If possible, output will be compressed into a host range (see TARGET SPECIFICATION below).</p>
<dt><i>-q, &#8211;query-all</i></p>
<dd> Query plug status of all targets. Status is not cached; each time this option is used, powermand queries the appropriate RPC&#8217;s. Targets connected to RPC&#8217;s that could not be contacted (e.g. due to network failure) are reported as status &quot;unknown&quot;. If possible, output will be compressed into host ranges.</p>
<dt><i>-Q, &#8211;query targets</i></p>
<dd> Query plug status of specific targets.</p>
<dt><i>-n, &#8211;soft-all</i></p>
<dd> Query soft power status of all targets (if implemented by RPC). In this context, a node in the OFF state could be ON at the plug but operating in standby power mode.</p>
<dt><i>-N, &#8211;soft targets</i></p>
<dd> Query soft power status of specific targets (if implemented by RPC).</p>
<dt><i>-b, &#8211;beacon-all</i></p>
<dd> Query beacon status of all targets (if implemented by RPC).</p>
<dt><i>-B, &#8211;beacon targets</i></p>
<dd> Query beacon status of specific targets (if implemented by RPC).</p>
<dt><i>-t, &#8211;temp-all</i></p>
<dd> Query node temperature of all targets (if implemented by RPC). Temperature information is not interpreted by powerman and is reported as received from the RPC on one line per target, prefixed by target name.</p>
<dt><i>-P, &#8211;temp targets</i></p>
<dd> Query node temperature of specific targets (if implemented by RPC).</p>
<dt><i>-L, &#8211;license</i></p>
<dd> Show powerman license information.</p>
<dt><i>-h, &#8211;server-host host[:port]</i></p>
<dd> Connect to a powerman daemon on non-default host and optionally port.</p>
<dt><i>-V, &#8211;version</i></p>
<dd> Display the powerman version number and exit.</p>
<dt><i>-D, &#8211;device</i></p>
<dd> Displays RPC status information. If targets are specified, only RPC&#8217;s matching the target list are displayed.</p>
<dt><i>-T, &#8211;telemetry</i></p>
<dd> Causes RPC telemetry information to be displayed as commands are processed. Useful for debugging device scripts.</p>
<dt><i>-x, &#8211;exprange</i></p>
<dd> Expand host ranges in query responses.</p>
<dt><i>-g, &#8211;genders</i></p>
<dd> If configured with the <a href="/docs/linux/man/3-genders/">genders</a>(3) package, this option tells powerman that targets are genders attributes that map to node names rather than the node names themselves.</dl>
<h2>TARGET SPECIFICATION</h2>
<p> <code>powerman</code> target hostnames may be specified as comma separated or space separated hostnames or host ranges. Host ranges are of the general form: prefix[n-m,l-k,&#8230;], where n &lt; m and l &lt; k, etc., This form should not be confused with regular expression character classes (also denoted by &#8220;[]&#8221;). For example, foo[19] does not represent foo1 or foo9, but rather represents a degenerate range: foo19. </p>
<p> This range syntax is meant only as a convenience on clusters with a prefixNN naming convention and specification of ranges should not be considered necessary &#8212; the list foo1,foo9 could be specified as such, or by the range foo[1,9]. </p>
<p> Some examples of powerman targets follows: </p>
<p> Power on hosts bar,baz,foo01,foo02,&#8230;,foo05<br />
&nbsp;<wbr>powerman &#8211;on bar baz foo[01-05] </p>
<p> Power on hosts bar,foo7,foo9,foo10<br />
&nbsp;<wbr>powerman &#8211;on bar,foo[7,9-10] </p>
<p> Power on foo0,foo4,foo5<br />
&nbsp;<wbr>powerman &#8211;on foo[0,4-5] </p>
<p> As a reminder to the reader, some shells will interpret brackets ([ and ]) for pattern matching. Depending on your shell, it may be necessary to enclose ranged lists within quotes. For example, in tcsh, the last example above should be executed as: </p>
<pre>
    powerman --on &quot;foo[0,4-5]&quot;
</pre>
<h2>FILES</h2>
<p> /usr/bin/powerman<br />
 /usr/bin/pm </p>
<h2>ORIGIN</h2>
<p> PowerMan was originally developed by Andrew Uselton on LLNL&#8217;s Linux clusters. This software is open source and distributed under the terms of the GNU GPL. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-powerman/">powerman</a></code>(1), <code><a href="/docs/linux/man/8-powermand/">powermand</a></code>(8), <code><a href="/docs/linux/man/8-httppower/">httppower</a></code>(8), <code><a href="/docs/linux/man/8-plmpower/">plmpower</a></code>(8), <code><a href="/docs/linux/man/8-vpcd/">vpcd</a></code>(8), <code><a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a></code>(5), <code><a href="/docs/linux/man/5-powerman-dev/">powerman.dev</a></code>(5). </p>
<p> <code><a rel="nofollow" href="http://code.google.com/p/powerman">http://code.google.com/p/powerman</a></code> </p>
<h2>Index</h2>
