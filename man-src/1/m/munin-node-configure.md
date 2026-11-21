---

title: "munin-node-configure(1)"
name: "munin-node-configure"
section: "1"
letter: "m"
url: "/docs/linux/man/1-munin-node-configure/"
description: "munin-node-configure – View and modify which plugins are enabled."
---

<pre>
  munin-node-configure [options]
</pre>
<p> <code>munin-node-configure</code> reports which plugins are enabled on the current node, and suggest changes to this list. </p>
<p> By default this program shows which plugins are activated on the system. </p>
<p> If you specify <tt>&quot;--suggest&quot;</tt>, it will present a table of plugins that will probably work (according to the plugins&#8217; autoconf command). </p>
<p> If you specify <tt>&quot;--snmp&quot;</tt>, followed by a list of hosts, it will present a table of <font SIZE="-1">SNMP</font> plugins that they support. </p>
<p> If you additionally specify <tt>&quot;--shell&quot;</tt>, shell commands to install those same plugins will be printed. These can be reviewed or piped directly into a shell to install the plugins.</p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Show this help page.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version information.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Print debug information on the operations of <tt>&quot;munin-node-configure&quot;</tt>. This can be very verbose. </dd>
<p> All debugging output is printed to <font SIZE="-1">STDOUT,</font> and each line is prefixed with &#8216;#&#8217;. Only errors are printed to <font SIZE="-1">STDERR.</font></p>
<dt><code>&#8211;pidebug</code></dt>
<dd> Plugin debug. Sets the environment variable <font SIZE="-1">MUNIN_DEBUG</font> to 1 so that plugins may enable debugging.</dd>
<dt><code>&#8211;config &lt;file&gt;</code></dt>
<dd> Override configuration file [/etc/munin/munin-node.conf]</dd>
<dt><code>&#8211;servicedir &lt;dir&gt;</code></dt>
<dd> Override plugin directory [/etc/munin/plugins/]</dd>
<dt><code>&#8211;sconfdir &lt;dir&gt;</code></dt>
<dd> Override plugin configuration directory [/etc/munin/plugin-conf.d/]</dd>
<dt><code>&#8211;libdir &lt;dir&gt;</code></dt>
<dd> Override plugin library [/usr/share/munin/plugins/]</dd>
<dt><code>&#8211;exitnoterror</code></dt>
<dd> Do not consider plugins that exit non-zero exit-value as error.</dd>
<dt><code>&#8211;suggest</code></dt>
<dd> Suggest plugins that might be added or removed, instead of those that are currently enabled.</dd></dl>
<h3><font SIZE="-1">OUTPUT OPTIONS</font></h3>
<p> By default, <tt>&quot;munin-node-configure&quot;</tt> will print out a table summarising the results.</p>
<dl>
<dt><code>&#8211;shell</code></dt>
<dd> Instead of a table, print shell commands to install the new plugin suggestions. </dd>
<p> This implies <tt>&quot;--suggest&quot;</tt>, unless <tt>&quot;--snmp&quot;</tt> was also enabled. By default, it will not attempt to remove any plugins.</p>
<dt><code>&#8211;remove-also</code></dt>
<dd> When <tt>&quot;--shell&quot;</tt> is enabled, also provide commands to remove plugins that are no longer applicable from the service directory.</dd></dl>
<h3><font SIZE="-1">PLUGIN SELECTION OPTIONS</font></h3>
<dl>
<dt><code>&#8211;families &lt;family,&#8230;&gt;</code></dt>
<dd> Override the list of families that will be used (auto, manual, contrib, snmpauto). Multiple families can be specified as a comma-separated list, by repeating the <tt>&quot;--families&quot;</tt> option, or as a combination of the two. </dd>
<p> When listing installed plugins, the default families are &#8216;auto&#8217;, &#8216;manual&#8217; and &#8216;contrib&#8217;. Only &#8216;auto&#8217; plugins are checked for suggestions. <font SIZE="-1">SNMP</font> probing is only performed on &#8216;snmpauto&#8217; plugins.</p>
<dt><code>&#8211;newer &lt;version&gt;</code></dt>
<dd> Only consider plugins added to the Munin core since &lt;version&gt;. This option is useful when upgrading, since it can prevent plugins that have been manually removed from being reinstalled. This only applies to plugins in the &#8216;auto&#8217; family.</dd></dl>
<h3><font SIZE="-1">SNMP</font> Options</h3>
<dl>
<dt><code>&#8211;snmp &lt;host|cidr,&#8230;&gt;</code></dt>
<dd> Probe the <font SIZE="-1">SNMP</font> agents on the host or <font SIZE="-1">CIDR</font> network (e.g. &#8220;192.168.1.0/24&#8221;), to see what plugins they support. This may take some time, especially if the many hosts are specified. </dd>
<p> This option can be specified multiple times, or as a comma-separated list, to include more than one host/CIDR.</p>
<dt><code>&#8211;snmpversion &lt;ver&gt;</code></dt>
<dd> The <font SIZE="-1">SNMP</font> version (1, 2c or 3) to use. [&#8216;2c&#8217;]</dd>
<dt><code>&#8211;snmpport &lt;port&gt;</code></dt>
<dd> The <font SIZE="-1">SNMP</font> port to use [161]</dd>
<dt><font SIZE="-1"><code>SNMP</code></font><code> 1/2c authentication</code></dt>
<dd> <font SIZE="-1">SNMP</font> versions 1 and 2c use a &#8220;community string&#8221; for authentication. This is a shared password, sent in plaintext over the network.</dd>
<dt><code>&#8211;snmpcommunity &lt;string&gt;</code></dt>
<dd> The community string for version 1 and 2c agents. [&#8216;public&#8217;] (If this works your device is probably very insecure and needs a security checkup).</dd>
<dt><font SIZE="-1"><code>SNMP 3</code></font><code> authentication</code></dt>
<dd> <font SIZE="-1">SNMP</font> v3 has three security levels. Lowest is <tt>&quot;noAuthNoPriv&quot;</tt>, which provides neither authentication nor encryption. If a username and <tt>&quot;authpassword&quot;</tt> are given it goes up to <tt>&quot;authNoPriv&quot;</tt>, and the connection is authenticated. If <tt>&quot;privpassword&quot;</tt> is also given the security level becomes <tt>&quot;authPriv&quot;</tt>, and the connection is authenticated and encrypted. </dd>
<p> <code>Note</code>: Encryption can slow down slow or heavily loaded network devices. For most uses <tt>&quot;authNoPriv&quot;</tt> will be secure enough &#8212; the password is sent over the network encrypted in any case. </p>
<p> ContextEngineIDs are not (yet) supported. </p>
<p> For further reading on <font SIZE="-1">SNMP</font> v3 security models please consult <font SIZE="-1">RFC3414</font> and the documentation for Net::SNMP.</p>
<dt><code>&#8211;snmpusername &lt;name&gt;</code></dt>
<dd> Username. There is no default.</dd>
<dt><code>&#8211;snmpauthpassword &lt;password&gt;</code></dt>
<dd> Authentication password. Optional when encryption is also enabled, in which case defaults to the privacy password (<tt>&quot;--snmpprivpassword&quot;</tt>).</dd>
<dt><code>&#8211;snmpauthprotocol &lt;protocol&gt;</code></dt>
<dd> Authentication protocol. One of &#8216;md5&#8217; or &#8216;sha&#8217; (<font SIZE="-1">HMAC-MD5-96, RFC1321</font> and <font SIZE="-1">SHA-1/HMAC-SHA-96, NIST FIPS PIB 180, RFC2264</font>). [&#8216;md5&#8217;]</dd>
<dt><code>&#8211;snmpprivpassword &lt;password&gt;</code></dt>
<dd> Privacy password to enable encryption. There is no default. An empty (&#8221;) password is considered as no password and will not enable encryption. </dd>
<p> Privacy requires a privprotocol as well as an authprotocol and a authpassword, but all of these are defaulted (to &#8216;des&#8217;, &#8216;md5&#8217;, and the privpassword value, respectively) and may therefore be left unspecified.</p>
<dt><code>&#8211;snmpprivprotocol &lt;protocol&gt;</code></dt>
<dd> If the privpassword is set this setting controls what kind of encryption is used to achieve privacy in the session. Only the very weak &#8216;des&#8217; encryption method is supported officially. [&#8216;des&#8217;] </dd>
<p> munin-node-configure also supports &#8216;3des&#8217; (<font SIZE="-1">CBC-3DES-EDE,</font> aka Triple-DES, <font SIZE="-1">NIST FIPS 46-3</font>) as specified in <font SIZE="-1">IETF</font> draft-reeder-snmpv3-usm-3desede. Whether or not this works with any particular device, we do not know.</dl>
<h2>FILES</h2>
<pre>
    /etc/munin/munin-node.conf
    /etc/munin/plugin-conf.d/*
    /etc/munin/plugins/*
    /usr/share/munin/plugins/plugins.history
    /usr/share/munin/plugins/*
</pre>
<h2>VERSION</h2>
<p> This is munin-node-configure (munin-node) v2.0.29. </p>
<p> <tt>$Id</tt>$</p>
<h2>AUTHORS</h2>
<p> Jimmy Olsen, Nicolai Langfeldt, Matthew Boyle</p>
<h2>BUGS</h2>
<p> Please see &lt;<a rel="nofollow" href="http://munin-monitoring.org/report/1">http://munin-monitoring.org/report/1</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003-2006 Jimmy Olsen, Nicolai Langfeldt. </p>
<p> Copyright (C) 2009-2010 Matthew Boyle </p>
<p> This is free software; see the source for copying conditions. There is <font SIZE="-1">NO</font> warranty; not even for <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> </p>
<p> This program is released under the <font SIZE="-1">GNU</font> General Public License </p>
