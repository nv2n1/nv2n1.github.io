---
title: "smokeping_probes_dismanping(3)"
name: "smokeping_probes_dismanping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_dismanping/"
description: "Smokeping::probes::DismanPing – DISMAN-PING-MIB Probe for SmokePing"
---

<p>Smokeping::probes::DismanPing &#8211; DISMAN-PING-MIB Probe for SmokePing </p>
<h2>Synopsis</h2>
<pre> *** Probes ***
 +DismanPing
 offset = 50%
 pings = 15
 step = 300
 # The following variables can be overridden in each target section
 ownerindex = smokeping
 packetsize = 56
 pinghost = pinger [at] router.example.com # mandatory
 pingsrc = 192.0.2.9
 # [...]
 *** Targets ***
 probe = DismanPing # if this should be the default probe
 # [...]
 + mytarget
 # probe = DismanPing # if the default probe is something else
 host = my.host
 ownerindex = smokeping
 packetsize = 56
 pinghost = pinger [at] router.example.com # mandatory
 pingsrc = 192.0.2.9</pre>
<h2>Description</h2>
<p>Uses the DISMAN-PING-MIB to cause a remote system to send probes.</p>
<h2>Variables</h2>
<p>Supported probe-specific variables:</p>
<dl COMPACT>
<dt>offset</p>
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as &#8216;random&#8217;, and the offset from the &#8216;General&#8217; section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 50%</p>
<dt>pings</p>
<dd>How many pings should be sent to each target. Note that the maximum value for DismanPing <font SIZE="-1">MIP</font> is 15, which is less than the SmokePing default, so this class has its own default value. If your Database section specifies a value less than 15, you must also set it for this probe. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. </p>
<p> Example value: 15 </p>
<p> Default value: 15</p>
<dt>step</p>
<dd>Duration of the base interval that this probe should use, if different from the one specified in the &#8216;Database&#8217; section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 300</dl>
<p> Supported target-specific variables:</p>
<dl COMPACT>
<dt>ownerindex</p>
<dd>The <font SIZE="-1">SNMP</font> OwnerIndex to use when setting up the test. When using <font SIZE="-1">VACM,</font> can map to a Security Name or Group Name of the entity running the test. </p>
<p> By default this will be set to </p>
<p> Example value: smokeping</p>
<dt>packetsize</p>
<dd>The packetsize parameter lets you configure the packet size for the pings sent. The minimum is 8, the maximum 65507. Use the same number as with fping if you want the same packet sizes being used on the network. </p>
<p> Default value: 56</p>
<dt>pinghost</p>
<dd>The (mandatory) pinghost parameter specifies the remote system which will execute the pings, as well as the <font SIZE="-1">SNMP</font> community string on the device. </p>
<p> Example value: pinger [at] router.example.com </p>
<p> This setting is mandatory.</p>
<dt>pingsrc</p>
<dd>The (optional) pingsrc parameter specifies the source address to be used for pings. If specified, this parameter must identify an <font SIZE="-1">IP</font> address assigned to pinghost. </p>
<p> Example value: 192.0.2.9</dl>
<h2>Authors</h2>
<p>Bill Fenner &lt;fenner [at] research.att.com&gt;, Tobi Oetiker &lt;tobi [at] oetiker.ch&gt;</p>
<h2>Notes</h2>
<h3><font SIZE="-1">MENU NAMES</font></h3>
<p>This probe uses the menu name of a test as part of the unique index. If the menu name is longer than 32 characters, the last 32 characters are used for the index. Collisions are *<code>not</code>* detected and simply cause one test&#8217;s results to be used for all colliding names.</p>
<h3><font SIZE="-1">CONFIGURATION</font></h3>
<p>This probe requires read/write access to the pingCtlTable. It also requires read-only access to the pingResultsTable and the pingHistoryTable. The DISMAN-PING-MIB is structured such that it is possible to restrict by pingCtlOwnerIndex. This probe uses a pingCtlOwnerIndex of &#8220;<font SIZE="-1">SP</font> on hostname&#8221; as ownerindex by default; use <code>ownerindex</code> to configure this if needed.</p>
<h3><font SIZE="-1">SAMPLE JUNOS CONFIGURATION</font></h3>
<p>This configuration permits the community &#8220;pinger&#8221; read-write access to the full DISMAN-PING-MIB, but only when sourced from the manager at <code>192.0.2.134</code>. </p>
<pre> snmp {
 view pingMIB {
 oid .1.3.6.1.2.1.80 include;
 }
 community pinger {
 view pingMIB; 
 authorization read-write;
 clients {
 192.0.2.134/32;
 }
 }
 }</pre>
<h3><font SIZE="-1">SAMPLE CONFIGURATIONS NOTE</font></h3>
<p>This configuration allows the &#8220;pinger&#8221; community full access to the DISMAN-PING-MIB. There is information in the description of <code>pingCtlOwnerIndex</code> in <font SIZE="-1">RFC 4560 </font>(&lt;<a rel="nofollow" href="http://tools.ietf.org/html/rfc4560">http://tools.ietf.org/html/rfc4560</a>&gt;) about using the vacmViewTreeFamilyTable to further restrict access. The author has not tried this method.</p>
