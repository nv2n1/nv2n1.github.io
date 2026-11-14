---
title: "types-db(5)"
name: "types-db"
section: "5"
letter: "t"
url: "/docs/linux/man/5-types-db/"
description: "types.db – Data-set specifications for the system statistics collection daemon collectd"
---

<p>types.db &#8211; Data-set specifications for the system statistics collection daemon collectd</p>
<h2>Synopsis</h2>
<pre> bitrate value:GAUGE:0:4294967295
 counter value:COUNTER:U:U
 if_octets rx:COUNTER:0:4294967295, tx:COUNTER:0:4294967295</pre>
<h2>Description</h2>
<p>The types.db file contains one line for each data-set specification. Each line consists of two fields delimited by spaces and/or horizontal tabs. The first field defines the name of the data-set, while the second field defines a list of data-source specifications, delimited by spaces and, optionally, a comma (&#8220;,&#8221;) right after each list-entry. </p>
<p> The format of the data-source specification has been inspired by RRDtool&#8217;s data-source specification. Each data-source is defined by a quadruple made up of the data-source name, type, minimal and maximal values, delimited by colons (&#8220;:&#8221;): <i>ds-name</i>:<i>ds-type</i>:<i>min</i>:<i>max</i>. <i>ds-type</i> may be either <font SIZE="-1"><code>ABSOLUTE</code></font>, <font SIZE="-1"><code>COUNTER</code></font>, <font SIZE="-1"><code>DERIVE</code></font>, or <font SIZE="-1"><code>GAUGE</code></font>. <i>min</i> and <i>max</i> define the range of valid values for data stored for this data-source. If <code>U</code> is specified for either the min or max value, it will be set to unknown, meaning that no range checks will happen. See <i><a href="/docs/linux/man/1-rrdcreate/">rrdcreate</a></i>(1) for more details.</p>
<h2>Files</h2>
<p>The location of the types.db file is defined by the <code>TypesDB</code> configuration option (see <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5)). It defaults to collectd&#8217;s shared data directory, i. e. <i>prefix/share/collectd/</i>.</p>
<h2>Custom Types</h2>
<p>If you want to specify custom types, you should do so by specifying a custom file in addition to the default one (see <font SIZE="-1">FILES</font>) above. You can do that by having multiple <code>TypesDB</code> statements in your configuration file or by specifying more than one file in one line. </p>
<p> For example: </p>
<pre> TypesDB &quot;/opt/collectd/share/collectd/types.db&quot;
 TypesDB &quot;/opt/collectd/etc/types.db.custom&quot;</pre>
<p><code>Note</code>: Make sure to make this file available on all systems if you&#8217;re sending values over the network.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/1-rrdcreate/">rrdcreate</a></i>(1)</p>
<h2>Author</h2>
<p><code>collectd</code> has been written by Florian Forster &lt;octo at collectd.org&gt;. </p>
<p> This manpage has been written by Sebastian Harl &lt;sh at tokkee.org&gt;.</p>
