---
title: "vhostmd(8)"
name: "vhostmd"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vhostmd/"
description: "vhostmd – A metrics gathering daemon."
---

<p>vhostmd &#8211; A metrics gathering daemon.</p>
<h2>Synopsis</h2>
<p><code>vhostmd</code> [ <i>OPTION</i> ]</p>
<h2>Description</h2>
<p><code>vhostmd</code> provides a &quot;metrics communication channel&quot; between a host and its hosted virtual machines, allowing limited introspection of host resource usage from within virtual machines. This functionality may be useful in hosting environments, giving virtual machine administrators a limited view of host resource consumption &#8211; potentially explaining a performance degradation within the virtual machine. </p>
<p> vhostmd will periodically write metrics to a disk. The metrics to write, how often, and where to write them are all adjustable via the /etc/vhostmd/vhostmd.conf configuration file. The disk can then be surfaced read-only to virtual machines using tools provided by the host&#8217;s virtualization platform.</p>
<h2>Options</h2>
<dl>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Verbose messages</p>
<dt><code>-d, &#8211;no-daemonize</code></p>
<dd>Process will not daemonize</p>
<dt><code>-c, &#8211;connect &lt;uri&gt;</code></p>
<dd>Set the libvirt URI. If unspecified then we connect to the default libvirt hypervisor. It is recommended that you specify this since libvirt&#8217;s method for choosing the default hypervisor can give unexpected results.</p>
<dt><code>-u, &#8211;user &lt;user&gt;</code></p>
<dd>Drop root privileges and run as the named non-root user.</p>
<dt><code>-p, &#8211;pid-file &lt;file&gt;</code></p>
<dd>Specify an alternate path for vhostmd to record its process-id in. Normally /var/run/vhostmd.pid</p>
<dt><code>-f, &#8211;config &lt;file&gt;</code></p>
<dd>Specify a different configuration file. Normally /etc/vhostmd/vhostmd.conf</dl>
<h2>Config File</h2>
<p>At startup, vhostmd reads <i>/etc/vhostmd/vhostmd.conf,</i> if it exists.<br />
&nbsp;<wbr>(See the&nbsp;<wbr> <code>-f</code> option.) </p>
<p> The default configuration file (listed below) defines a 256Kbyte metrics disk in /dev/shm/vhostmd0, updated every 5 seconds. It also includes a few examples of user-defined metrics, which provide a (currently simplistic) mechanism for extending metrics gathered by vhostmd. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;vhostmd&gt;<br />
&nbsp;<wbr>&lt;globals&gt;<br />
&lt;disk&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;host-metrics-disk&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;path&gt;/dev/shm/vhostmd0&lt;/path&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;size unit=&quot;k&quot;&gt;256&lt;/size&gt;<br />
&lt;/disk&gt;<br />
&lt;update_period&gt;5&lt;/update_period&gt;<br />
&lt;path&gt;/usr/bin:/usr/sbin:/usr/share/vhostmd/scripts&lt;/path&gt;<br />
&nbsp;<wbr>&lt;/globals&gt;<br />
&nbsp;<wbr>&lt;metrics&gt;<br />
&lt;metric type=&quot;string&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;HostName&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;virsh hostname | tr -d&nbsp;<wbr>&#8216;[:space:]'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;string&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;VirtualizationVendor&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;/bin/rpm -q &#8211;info xen | grep Vendor: |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>awk&nbsp;<wbr>&#8216;{print substr($0, index($0,$5))&nbsp;<wbr>}'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;uint32&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalPhyCPUs&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;xm info | gawk&nbsp;<wbr>&#8216;/^nr_cpus/&nbsp;<wbr>{print&nbsp;<wbr>$3}'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;uint32&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;NumCPUs&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;xm info | gawk&nbsp;<wbr>&#8216;/^nr_cpus/&nbsp;<wbr>{print&nbsp;<wbr>$3}'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;uint64&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalPhyMem&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;xm info | gawk&nbsp;<wbr>&#8216;/^total_memory/&nbsp;<wbr>{print&nbsp;<wbr>$3}'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;uint64&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;UsedMem&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;xentop -b -i 1 | gawk&nbsp;<wbr>&#8216;/Domain-0/&nbsp;<wbr>{print&nbsp;<wbr>$5}'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;uint64&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;FreeMem&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;xm info | gawk&nbsp;<wbr>&#8216;/^max_free_memory/&nbsp;<wbr>{print&nbsp;<wbr>$3}'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;uint64&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;PagedInMemory&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;vmstat -s | gawk&nbsp;<wbr>&#8216;/pages paged in/&nbsp;<wbr>{print&nbsp;<wbr>$1}'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;uint64&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;PagedOutMemory&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;vmstat -s | gawk&nbsp;<wbr>&#8216;/pages paged out/&nbsp;<wbr>{print&nbsp;<wbr>$1}'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;group&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;PageRates&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;pagerate.pl&lt;/action&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;variable name=&quot;PageInRate&quot;&nbsp;<wbr>type=&quot;uint64&quot;/&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;variable name=&quot;PageFaultRate&quot;&nbsp;<wbr>type=&quot;uint64&quot;/&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;real64&quot;&nbsp;<wbr>context=&quot;host&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalCPUTime&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;virsh dominfo 0 | sed&nbsp;<wbr>&#8216;s/:&nbsp;<wbr>*/:/&#8217;&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gawk -F:&nbsp;<wbr>&#8216;/CPU time/&nbsp;<wbr>{print&nbsp;<wbr>$2;}'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;real64&quot;&nbsp;<wbr>context=&quot;vm&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalCPUTime&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;virsh dominfo NAME | sed&nbsp;<wbr>&#8216;s/:&nbsp;<wbr>*/:/&#8217;&nbsp;<wbr>|<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>gawk -F:&nbsp;<wbr>&#8216;/CPU time/&nbsp;<wbr>{print&nbsp;<wbr>$2;}'&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&quot;xml&quot;&nbsp;<wbr>context=&quot;vm&quot;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;my-metric&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;action&gt;xml-metrics-test.sh&lt;/action&gt;<br />
&lt;/metric&gt;<br />
&nbsp;<wbr>&lt;/metrics&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;/vhostmd&gt; </p>
<p> A valid configuration file must contain the root element &lt;vhostmd&gt;. The &lt;globals&gt; element contains configuration global to vhostmd, such as the metrics disk path and the metrics refresh interval. The &lt;metrics&gt; element is a container for all of the &lt;metric&gt; elements. A metric element is used to define a metric, giving it a name and an action that produces the metric value. </p>
<p> The supplied vhostmd configuration file provides a useful set of default metrics to be collected. This can be extended or modified by editing /etc/vhostmd/vhostmd.conf and changing existing metric definitions or adding new metric definitions under the metrics container. </p>
<p> Defined metrics begin with the &lt;metric&gt; element, which contains two attributes: type and context. The type attribute is used to describe the metric&#8217;s value type. Supported types are int32, uint32, int64, uint64, real32, real64, string, group, and xml. group is used when an action returns more than one metric value. xml is the most flexible type and specifies that the metric&#8217;s action returns valid metric XML. The context attribute is used to indicate whether this is a host or vm metric. Supported contexts are host and vm. </p>
<p> Currently, the metric element contains 3 elements: name, action, and variable. The name element defines the metric&#8217;s name. The action element describes a command or pipeline of commands used to gather the metric. </p>
<p> Any &lt;action&gt; element can contain the magic token CONNECT which is replaced with the string &quot;&#8211;connect &#8216;uri&#8217;&quot; where uri is the libvirt connection URI (specified on the command line to vhostmd as the -c option). If it wasn&#8217;t specified, then the token CONNECT is substituted with the empty string. This allows you to write virsh commands like this: </p>
<p>&nbsp;<wbr>virsh -r CONNECT command &#8230; </p>
<p> For metrics of vm context, the tokens NAME, VMID, and UUID may be used where these attributes of a VM are normally provided in a command. When the metric is sampled, these tokens will be substituted with the actual name, ID, or UUID of the vm currently being sampled by vhostmd. </p>
<p> If the metric type is xml, action is expected to return valid metric XML as defined below in &quot;XML Format of Content&quot;.</p>
<h2>Metrics Disk Format</h2>
<p>Currently, the disk format is quite simple: a raw, file-backed disk containing a header, immediately followed by metric content. </p>
<p> The header contains the following, all in network-byte order </p>
<p>&nbsp;<wbr>&#8211; 4 byte signature,&nbsp;<wbr>&#8216;mvbd&#8217;<br />
&nbsp;<wbr>&#8211; 4 byte busy flag<br />
&nbsp;<wbr>&#8211; 4 byte content checksum<br />
&nbsp;<wbr>&#8211; 4 byte content length </p>
<p> The busy flag permits simple reader/writer synchronization. The busy flag can be checked for clear, content read into a buffer, and the busy flag checked again for clear to ensure stable content.</p>
<h2>XML Format of Content</h2>
<p>The content is an XML document containing default and user-defined metrics. The format is quite similar to the metrics definitions found in the vhostmd configuration file. A notable addition, as illustrated below, is the value element containing the metric&#8217;s current value. </p>
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
&lt;metric type=&#8217;real64&#8242;&nbsp;<wbr>context=&#8217;vm&#8217;&nbsp;<wbr>id=&#8217;0&#8242;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>uuid=&#8217;00000000-0000-0000-0000-000000000000&#8242;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalCPUTime&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;847.700000&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&lt;metric type=&#8217;real64&#8242;&nbsp;<wbr>context=&#8217;vm&#8217;&nbsp;<wbr>id=&#8217;2&#8242;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>uuid=&#8217;6be3fdb8-bef5-6fec-b1b7-e61bbceab708&#8242;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;TotalCPUTime&lt;/name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;value&gt;69.400000&lt;/value&gt;<br />
&lt;/metric&gt;<br />
&nbsp;<wbr>&lt;/metrics&gt;</p>
<h2>Files</h2>
<p><i>/etc/vhostmd/vhostmd.conf</i> </p>
<p> <i>/etc/vhostmd/vhostmd.dtd</i> </p>
<p> <i>/etc/vhostmd/metric.dtd</i> </p>
<p> <i>/var/run/vhostmd.pid</i></p>
<h2>See Also</h2>
<h2>Authors</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>Pat Campbell&nbsp;<wbr>&lt;plc [at] novell.com&gt;.<br />
&nbsp;<wbr>&nbsp;<wbr>Jim Fehlig&nbsp;<wbr>&lt;jfehlig [at] novell.com&gt;.</p>
