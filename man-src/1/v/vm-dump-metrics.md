---
title: "vm-dump-metrics(1)"
name: "vm-dump-metrics"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vm-dump-metrics/"
description: "vm-dump-metrics – Dump VM metrics."
---

<h2>NAME</h2>
<p> vm-dump-metrics &#8211; Dump VM metrics.</p>
<h2>SYNOPSIS</h2>
<p> <code>vm-dump-metrics</code> [ <i>OPTION</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>vm-dump-metrics</code> reads virtualization hosts provided metrics decription and dumps output</p>
<h2>OPTIONS</h2>
<p> <code>-f, &#8211;dest &lt;file&gt;</code> Specify a dump file to be used instead of &lt;stdout&gt; </p>
<h2>XML Format of Content</h2>
<p> The content is an XML document containing host provided. The format is quite simple and is illustrated below. </p>
<p>&nbsp;<wbr>&lt;metrics&gt;<br />
&lt;metric type=&#8217;real64&#8242;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalCPUTime&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;846.600000&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;uint64&#8242;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;PageInRate&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;0.000000&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;uint64&#8242;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;PageFaultRate&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;0.000000&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;uint64&#8242;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;PagedOutMemory&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;6885044&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;uint64&#8242;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;PagedInMemory&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;2367980&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;uint64&#8242;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;FreeMem&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;829&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;uint64&#8242;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;UsedMem&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;1369088&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;uint64&#8242;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalPhyMem&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;1919&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;uint32&#8242;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;NumCPUs&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;2&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;uint32&#8242;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalPhyCPUs&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;2&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;string&#8217;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;VirtualizationVendor&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;SUSE LINUX Products GmbH&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;string&#8217;&nbsp;<wbr>context=&#8217;host&#8217;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;HostName&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;laptop&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;real64&#8242;&nbsp;<wbr>context=&#8217;vm&#8217;&nbsp;<wbr>id=&#8217;0&#8242;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>uuid=&#8217;00000000-0000-0000-0000-000000000000&#8242;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalCPUTime&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;847.700000&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;real64&#8242;&nbsp;<wbr>context=&#8217;vm&#8217;&nbsp;<wbr>id=&#8217;2&#8242;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>uuid=&#8217;6be3fdb8-bef5-6fec-b1b7-e61bbceab708&#8242;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalCPUTime&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;69.400000&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&nbsp;<wbr>&lt;/metrics&gt; </p>
<h2>FILES</h2>
<p> <i>/usr/sbin/vm-dump-metrics</i> </p>
<h2>SEE ALSO</h2>
<h2>AUTHORS</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>Pat Campbell&nbsp;<wbr>&lt;plc [at] novell.com&gt;.<br />
&nbsp;<wbr>&nbsp;<wbr>Jim Fehlig&nbsp;<wbr>&lt;jfehlig [at] novell.com&gt;. </p>
<h2>Index</h2>
