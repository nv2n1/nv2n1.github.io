---
title: "collectd-snmp(5)"
name: "collectd-snmp"
section: "5"
letter: "c"
url: "/docs/linux/man/5-collectd-snmp/"
description: "collectd-snmp – Documentation of collectd’s \"snmp plugin\""
---

<p>collectd-snmp &#8211; Documentation of collectd&#8217;s &quot;snmp plugin&quot;</p>
<h2>Synopsis</h2>
<pre> LoadPlugin snmp
 # ...
 &lt;Plugin snmp&gt;
 &lt;Data &quot;powerplus_voltge_input&quot;&gt;
 Type &quot;voltage&quot;
 Table false
 Instance &quot;input_line1&quot;
 Scale 0.1
 Values &quot;SNMPv2-SMI::enterprises.6050.5.4.1.1.2.1&quot;
 &lt;/Data&gt;
 &lt;Data &quot;hr_users&quot;&gt;
 Type &quot;users&quot;
 Table false
 Instance &quot;&quot;
 Shift -1
 Values &quot;HOST-RESOURCES-MIB::hrSystemNumUsers.0&quot;
 &lt;/Data&gt;
 &lt;Data &quot;std_traffic&quot;&gt;
 Type &quot;if_octets&quot;
 Table true
 Instance &quot;IF-MIB::ifDescr&quot;
 Values &quot;IF-MIB::ifInOctets&quot; &quot;IF-MIB::ifOutOctets&quot;
 &lt;/Data&gt;
 &lt;Host &quot;some.switch.mydomain.org&quot;&gt;
 Address &quot;192.168.0.2&quot;
 Version 1
 Community &quot;community_string&quot;
 Collect &quot;std_traffic&quot;
 Interval 120
 &lt;/Host&gt;
 &lt;Host &quot;some.server.mydomain.org&quot;&gt;
 Address &quot;192.168.0.42&quot;
 Version 2
 Community &quot;another_string&quot;
 Collect &quot;std_traffic&quot; &quot;hr_users&quot;
 &lt;/Host&gt;
 &lt;Host &quot;secure.router.mydomain.org&quot;&gt;
 Address &quot;192.168.0.7&quot;
 Version 3
 SecurityLevel &quot;authPriv&quot;
 Username &quot;cosmo&quot;
 AuthProtocol &quot;SHA&quot;
 AuthPassphrase &quot;setec_astronomy&quot;
 PrivacyProtocol &quot;AES&quot;
 PrivacyPassphrase &quot;too_many_secrets&quot;
 Collect &quot;std_traffic&quot;
 &lt;/Host&gt;
 &lt;Host &quot;some.ups.mydomain.org&quot;&gt;
 Address &quot;192.168.0.3&quot;
 Version 1
 Community &quot;more_communities&quot;
 Collect &quot;powerplus_voltge_input&quot;
 Interval 300
 &lt;/Host&gt;
 &lt;/Plugin&gt;</pre>
<h2>Description</h2>
<p>The <tt>&quot;snmp plugin&quot;</tt> queries other hosts using <font SIZE="-1">SNMP,</font> the simple network management protocol, and translates the value it receives to collectd&#8217;s internal format and dispatches them. Depending on the write plugins you have loaded they may be written to disk or submitted to another instance or whatever you configured. </p>
<p> Because querying a host via <font SIZE="-1">SNMP</font> may produce a timeout multiple threads are used to query hosts in parallel. Depending on the number of hosts between one and ten threads are used.</p>
<h2>Configuration</h2>
<p>Since the aim of the <tt>&quot;snmp plugin&quot;</tt> is to provide a generic interface to <font SIZE="-1">SNMP,</font> it&#8217;s configuration is not trivial and may take some time. </p>
<p> Since the <tt>&quot;Net-SNMP&quot;</tt> library is used you can use all the environment variables that are interpreted by that package. See <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a></i>(1) for more details. </p>
<p> There are two types of blocks that can be contained in the <tt>&quot;&lt;Plugin snmp&gt;&quot;</tt> block: <code>Data</code> and <code>Host</code>:</p>
<h3>The <code>Data</code> block</h3>
<p>The <code>Data</code> block defines a list of values or a table of values that are to be queried. The following options can be set:</p>
<dl>
<dt><code>Type</code> <i>type</i></p>
<dd>collectd&#8217;s type that is to be used, e. g. &#8220;if_octets&#8221; for interface traffic or &#8220;users&#8221; for a user count. The types are read from the <code>TypesDB</code> (see <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5)), so you may want to check for which types are defined. See <i><a href="/docs/linux/man/5-types-db/">types.db</a></i>(5) for a description of the format of this file.</p>
<dt><code>Table</code> <i>true|false</i></p>
<dd>Define if this is a single list of values or a table of values. The difference is the following: </p>
<p> When <code>Table</code> is set to <code>false</code>, the OIDs given to <code>Values</code> (see below) are queried using the <tt>&quot;GET&quot;</tt> <font SIZE="-1">SNMP</font> command (see <i><a href="/docs/linux/man/1-snmpget/">snmpget</a></i>(1)) and transmitted to collectd. <code>One</code> value list is dispatched and, eventually, one file will be written. </p>
<p> When <code>Table</code> is set to <code>true</code>, the OIDs given to <code>Values</code> (see below) are queried using the <tt>&quot;GETNEXT&quot;</tt> <font SIZE="-1">SNMP</font> command until the subtree is left. After all the lists (think: all columns of the table) have been read <code>several</code> values sets will be dispatches and, eventually, several files will be written. If you configure a <code>Type</code> (see above) which needs more than one data source (for example <tt>&quot;if_octets&quot;</tt> which needs <tt>&quot;rx&quot;</tt> and <tt>&quot;tx&quot;</tt>) you will need to specify more than one (two, in the example case) OIDs with the <code>Values</code> option. This has nothing to do with the <code>Table</code> setting. </p>
<p> For example, if you want to query the number of users on a system, you can use <tt>&quot;HOST-RESOURCES-MIB::hrSystemNumUsers.0&quot;</tt>. This is one value and belongs to one value list, therefore <code>Table</code> must be set to <code>false</code>. Please note that, in this case, you have to include the sequence number (zero in this case) in the <font SIZE="-1">OID.</font> </p>
<p> Counter example: If you want to query the interface table provided by the <tt>&quot;IF-MIB&quot;</tt>, e. g. the bytes transmitted. There are potentially many interfaces, so you will want to set <code>Table</code> to <code>true</code>. Because the <tt>&quot;if_octets&quot;</tt> type needs two values, received and transmitted bytes, you need to specify two OIDs in the <code>Values</code> setting, in this case likely <tt>&quot;IF-MIB::ifHCInOctets&quot;</tt> and <tt>&quot;IF-MIB::ifHCOutOctets&quot;</tt>. But, this is because of the <code>Type</code> setting, not the <code>Table</code> setting. </p>
<p> Since the semantic of <code>Instance</code> and <code>Values</code> depends on this setting you need to set it before setting them. Doing vice verse will result in undefined behavior.</p>
<dt><code>Instance</code> <i>Instance</i></p>
<dd>Sets the type-instance of the values that are dispatched. The meaning of this setting depends on whether <code>Table</code> is set to <i>true</i> or <i>false</i>: </p>
<p> If <code>Table</code> is set to <i>true</i>, <i>Instance</i> is interpreted as an SNMP-prefix that will return a list of values. Those values are then used as the actual type-instance. An example would be the <tt>&quot;IF-MIB::ifDescr&quot;</tt> subtree. <i><a href="/docs/linux/man/5-variables/">variables</a></i>(5) from the <font SIZE="-1">SNMP</font> distribution describes the format of OIDs. </p>
<p> If <code>Table</code> is set to <i>true</i> and <code>Instance</code> is omitted, then &#8220;<font SIZE="-1">SUBID&#8221;</font> will be used as the instance. </p>
<p> If <code>Table</code> is set to <i>false</i> the actual string configured for <i>Instance</i> is copied into the value-list. In this case <i>Instance</i> may be empty, i. e. &quot;&quot;.</p>
<dt><code>InstancePrefix</code> <i>String</i></p>
<dd>If <code>Table</code> is set to <i>true</i>, you may feel the need to add something to the instance of the files. If set, <i>String</i> is prepended to the instance as determined by querying the agent. When <code>Table</code> is set to <i>false</i> this option has no effect. </p>
<p> The <tt>&quot;UPS-MIB&quot;</tt> is an example where you need this setting: It has voltages of the inlets, outlets and the battery of an <font SIZE="-1">UPS.</font> However, it doesn&#8217;t provide a descriptive column for these voltages. In this case having 1, 2, &#8230; as instances is not enough, because the inlet voltages and outlet voltages may both have the subids 1, 2, &#8230; You can use this setting to distinguish between the different voltages.</p>
<dt><code>Values</code> <i></i><font SIZE="-1"><i>OID</i></font><i></i> [<i></i><font SIZE="-1"><i>OID</i></font><i></i> &#8230;]</p>
<dd>Configures the values to be queried from the <font SIZE="-1">SNMP</font> host. The meaning slightly changes with the <code>Table</code> setting. <i><a href="/docs/linux/man/5-variables/">variables</a></i>(5) from the <font SIZE="-1">SNMP</font> distribution describes the format of OIDs. </p>
<p> If <code>Table</code> is set to <i>true</i>, each <i></i><font SIZE="-1"><i>OID</i></font><i></i> must be the prefix of all the values to query, e. g. <tt>&quot;IF-MIB::ifInOctets&quot;</tt> for all the counters of incoming traffic. This subtree is walked (using <tt>&quot;GETNEXT&quot;</tt>) until a value from outside the subtree is returned. </p>
<p> If <code>Table</code> is set to <i>false</i>, each <i></i><font SIZE="-1"><i>OID</i></font><i></i> must be the <font SIZE="-1">OID</font> of exactly one value, e. g. <tt>&quot;IF-MIB::ifInOctets.3&quot;</tt> for the third counter of incoming traffic.</p>
<dt><code>Scale</code> <i>Value</i></p>
<dd>The gauge-values returned by the SNMP-agent are multiplied by <i>Value</i>. This is useful when values are transferred as a fixed point real number. For example, thermometers may transfer <code>243</code> but actually mean <code>24.3</code>, so you can specify a scale value of <code>0.1</code> to correct this. The default value is, of course, <code>1.0</code>. </p>
<p> This value is not applied to counter-values.</p>
<dt><code>Shift</code> <i>Value</i></p>
<dd><i>Value</i> is added to gauge-values returned by the SNMP-agent after they have been multiplied by any <code>Scale</code> value. If, for example, a thermometer returns degrees Kelvin you could specify a shift of <code>273.15</code> here to store values in degrees Celsius. The default value is, of course, <code>0.0</code>. </p>
<p> This value is not applied to counter-values.</p>
<dt><code>Ignore</code> <i>Value</i> [, <i>Value</i> &#8230;]</p>
<dd>The ignore values allows one to ignore Instances based on their name and the patterns specified by the various values you&#8217;ve entered. The match is a glob-type shell matching.</p>
<dt><code>InvertMatch</code> <i>true|false(default)</i></p>
<dd>The invertmatch value should be use in combination of the Ignore option. It changes the behaviour of the Ignore option, from a blacklist behaviour when InvertMatch is set to false, to a whitelist when specified to true.</dl>
<h3>The Host block</h3>
<p>The <code>Host</code> block defines which hosts to query, which <font SIZE="-1">SNMP</font> community and version to use and which of the defined <code>Data</code> to query. </p>
<p> The argument passed to the <code>Host</code> block is used as the hostname in the data stored by collectd.</p>
<dl>
<dt><code>Address</code> <i>IP-Address</i>|<i>Hostname</i></p>
<dd>Set the address to connect to.</p>
<dt><code>Version</code> <code>1</code>|<code>2</code>|<code>3</code></p>
<dd>Set the <font SIZE="-1">SNMP</font> version to use. When giving <code>2</code> version <tt>&quot;2c&quot;</tt> is actually used.</p>
<dt><code>Community</code> <i>Community</i></p>
<dd>Pass <i>Community</i> to the host. (Ignored for SNMPv3).</p>
<dt><code>Username</code> <i>Username</i></p>
<dd>Sets the <i>Username</i> to use for SNMPv3 security.</p>
<dt><code>SecurityLevel</code> <i>authPriv</i>|<i>authNoPriv</i>|<i>noAuthNoPriv</i></p>
<dd>Selects the security level for SNMPv3 security.</p>
<dt><code>Context</code> <i>Context</i></p>
<dd>Sets the <i>Context</i> for SNMPv3 security.</p>
<dt><code>AuthProtocol</code> <i></i><font SIZE="-1"><i>MD5</i></font><i></i>|<i></i><font SIZE="-1"><i>SHA</i></font><i></i></p>
<dd>Selects the authentication protocol for SNMPv3 security.</p>
<dt><code>AuthPassphrase</code> <i>Passphrase</i></p>
<dd>Sets the authentication passphrase for SNMPv3 security.</p>
<dt><code>PrivacyProtocol</code> <i></i><font SIZE="-1"><i>AES</i></font><i></i>|<i></i><font SIZE="-1"><i>DES</i></font><i></i></p>
<dd>Selects the privacy (encryption) protocol for SNMPv3 security.</p>
<dt><code>PrivacyPassphrase</code> <i>Passphrase</i></p>
<dd>Sets the privacy (encryption) passphrase for SNMPv3 security.</p>
<dt><code>Collect</code> <i>Data</i> [<i>Data</i> &#8230;]</p>
<dd>Defines which values to collect. <i>Data</i> refers to one of the <code>Data</code> block above. Since the config file is read top-down you need to define the data before using it here.</p>
<dt><code>Interval</code> <i>Seconds</i></p>
<dd>Collect data from this host every <i>Seconds</i> seconds. This option is meant for devices with not much <font SIZE="-1">CPU</font> power, e. g. network equipment such as switches, embedded devices, rack monitoring systems and so on. Since the <code>Step</code> of generated <font SIZE="-1">RRD</font> files depends on this setting it&#8217;s wise to select a reasonable value once and never change it.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-collectd/">collectd</a></i>(1), <i><a href="/docs/linux/man/5-collectd-conf/">collectd.conf</a></i>(5), <i><a href="/docs/linux/man/1-snmpget/">snmpget</a></i>(1), <i><a href="/docs/linux/man/1-snmpgetnext/">snmpgetnext</a></i>(1), <i><a href="/docs/linux/man/5-variables/">variables</a></i>(5), <i><a href="/docs/linux/man/7-unix/">unix</a></i>(7)</p>
<h2>Authors</h2>
<p>Florian Forster &lt;octo [at] collectd.org&gt; Michael Pilat &lt;mike [at] mikepilat.com&gt;</p>
