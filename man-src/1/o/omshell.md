---
title: "omshell(1)"
name: "omshell"
section: "1"
letter: "o"
url: "/docs/linux/man/1-omshell/"
description: "omshell – OMAPI Command Shell"
---

<h2>NAME</h2>
<p> omshell &#8211; OMAPI Command Shell</p>
<h2>SYNOPSIS</h2>
<p> <code>omshell</code></p>
<h2>DESCRIPTION</h2>
<p> The OMAPI Command Shell, omshell, provides an interactive way to connect to, query, and possibly change, the ISC DHCP Server&#8217;s state via OMAPI, the Object Management API. By using OMAPI and omshell, you do not have to stop, make changes, and then restart the DHCP server, but can make the changes while the server is running. Omshell provides a way of accessing OMAPI. </p>
<p> OMAPI is simply a communications mechanism that allows you to manipulate objects. In order to actually <i>use</i> omshell, you <i>must</i> understand what objects are available and how to use them. Documentation for OMAPI objects can be found in the documentation for the server that provides them &#8211; for example, in the <code><a href="/docs/linux/man/1-dhcpd/">dhcpd</a>(1)</code> manual page and the <code><a href="/docs/linux/man/1-dhclient/">dhclient</a>(1)</code> manual page.</p>
<h2>CONTRIBUTIONS</h2>
<p> This software is free software. At various times its development has been underwritten by various organizations, including the ISC and Vixie Enterprises. The development of 3.0 has been funded almost entirely by Nominum, Inc. </p>
<p> At this point development is being shepherded by Ted Lemon, and hosted by the ISC, but the future of this project depends on you. If you have features you want, please consider implementing them.</p>
<h2>LOCAL AND REMOTE OBJECTS</h2>
<p> Throughout this document, there are references to local and remote objects. Local objects are ones created in omshell with the <code>new</code> command. Remote objects are ones on the server: leases, hosts, and groups that the DHCP server knows about. Local and remote objects are associated together to enable viewing and modification of object attributes. Also, new remote objects can be created to match local objects.</p>
<h2>OPENING A CONNECTION</h2>
<p> omshell is started from the command line. Once omshell is started, there are several commands that can be issued: </p>
<p> <code>server </code><i>address</i></p>
<dl>
<dt>
<dd> where address is the IP address of the DHCP server to connect to. If this is not specified, the default server is 127.0.0.1 (localhost).</dl>
<p> <code>port </code><i>number</i></p>
<dl>
<dt>
<dd> where number is the port that OMAPI listens on. By default, this is 7911.</dl>
<p> <code>key </code><i>name secret</i></p>
<dl>
<dt>
<dd> This specifies the TSIG key to use to authenticate the OMAPI transactions. <i>name</i> is the name of a key defined in <i>dhcpd.conf</i> with the <code>omapi-key</code> statement. The <i>secret</i> is the secret key generated from <code>dnssec-keygen</code> or another key generation program.</dl>
<p> <code>connect</code></p>
<dl>
<dt>
<dd> This starts the OMAPI connection to the server as specified by the <i>server</i> statement.</dl>
<h2>CREATING LOCAL OBJECTS</h2>
<p> Any object defined in OMAPI can be created, queried, and/or modified. The object types available to OMAPI are defined in <code><a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8)</code> and <code><a href="/docs/linux/man/8-dhclient/">dhclient</a>(8)</code>. When using omshell, objects are first defined locally, manipulated as desired, and then associated with an object on the server. Only one object can be manipulated at a time. To create a local object, use </p>
<p> <code>new </code><i>object-type</i></p>
<dl>
<dt>
<dd> <i>object-type</i> is one of group, host, or lease.</dl>
<p> At this point, you now have an object that you can set properties on. For example, if a new lease object was created with <i>new lease</i>, any of a lease&#8217;s attributes can be set as follows: </p>
<p> <code>set </code><i>attribute-name = value</i></p>
<dl>
<dt>
<dd> <code>Attribute</code> names are defined in <code><a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8)</code> and <code><a href="/docs/linux/man/8-dhclient/">dhclient</a>(8)</code>. Values should be quoted if they are strings. So, to set a lease&#8217;s IP address, you would do the following: <code> set ip-address = 192.168.4.50</code></dl>
<h2>ASSOCIATING LOCAL AND REMOTE OBJECTS</h2>
<p> At this point, you can query the server for information about this lease, by </p>
<p> <code>open</code> </p>
<p> Now, the local lease object you created and set the IP address for is associated with the corresponding lease object on the DHCP server. All of the lease attributes from the DHCP server are now also the attributes on the local object, and will be shown in omshell.</p>
<h2>VIEWING A REMOTE OBJECT</h2>
<p> To query a lease of address 192.168.4.50, and find out its attributes, after connecting to the server, take the following steps: </p>
<p> <code>new lease</code> </p>
<p> This creates a new local lease object. </p>
<p> <code>set ip-address = 192.168.4.50</code> </p>
<p> This sets the <i>local</i> object&#8217;s IP address to be 192.168.4.50 </p>
<p> <code>open</code> </p>
<p> Now, if a lease with that IP address exists, you will see all the information the DHCP server has about that particular lease. Any data that isn&#8217;t readily printable text will show up in colon-separated hexadecimal values. In this example, output back from the server for the entire transaction might look like this: </p>
<pre>
&gt; new &quot;lease&quot;
obj: lease
&gt; set ip-address = 192.168.4.50
obj: lease
ip-address = c0:a8:04:32
&gt; open
obj: lease
ip-address = c0:a8:04:32
state = 00:00:00:02
dhcp-client-identifier = 01:00:10:a4:b2:36:2c
client-hostname = &quot;wendelina&quot;
subnet = 00:00:00:06
pool = 00:00:00:07
hardware-address = 00:10:a4:b2:36:2c
hardware-type = 00:00:00:01
ends = dc:d9:0d:3b
starts = 5c:9f:04:3b
tstp = 00:00:00:00
tsfp = 00:00:00:00
cltt = 00:00:00:00
</pre>
<p> As you can see here, the IP address is represented in hexadecimal, as are the starting and ending times of the lease.</p>
<h2>MODIFYING A REMOTE OBJECT</h2>
<p> Attributes of remote objects are updated by using the <code>set</code> command as before, and then issuing an <code>update</code> command. The <code>set</code> command sets the attributes on the current local object, and the <code>update</code> command pushes those changes out to the server. </p>
<p> Continuing with the previous example, if a <code>set client-hostname = &quot;something-else&quot;</code> was issued, followed by an <code>update</code> command, the output would look about like this: </p>
<pre>
&gt; set client-hostname = &quot;something-else&quot;
obj: lease
ip-address = c0:a8:04:32
state = 00:00:00:02
dhcp-client-identifier = 01:00:10:a4:b2:36:2c
client-hostname = &quot;something-else&quot;
subnet = 00:00:00:06
pool = 00:00:00:07
hardware-address = 00:10:a4:b2:36:2c
hardware-type = 00:00:00:01
ends = dc:d9:0d:3b
starts = 5c:9f:04:3b
tstp = 00:00:00:00
tsfp = 00:00:00:00
cltt = 00:00:00:00
&gt; update
obj: lease
ip-address = c0:a8:04:32
state = 00:00:00:02
dhcp-client-identifier = 01:00:10:a4:b2:36:2c
client-hostname = &quot;something-else&quot;
subnet = 00:00:00:06
pool = 00:00:00:07
hardware-address = 00:10:a4:b2:36:2c
hardware-type = 00:00:00:01
ends = dc:d9:0d:3b
starts = 5c:9f:04:3b
tstp = 00:00:00:00
tsfp = 00:00:00:00
cltt = 00:00:00:00
</pre>
<h2>NEW REMOTE OBJECTS</h2>
<p> New remote objects are created much in the same way that existing server objects are modified. Create a local object using <code>new</code>, set the attributes as you&#8217;d wish them to be, and then create the remote object with the same properties by using </p>
<p> <code>create</code> </p>
<p> Now a new object exists on the DHCP server which matches the properties that you gave your local object. Objects created via OMAPI are saved into the dhcpd.leases file. </p>
<p> For example, if a new host with the IP address of 192.168.4.40 needs to be created it would be done as follows: </p>
<pre>
&gt; new host
obj: host
&gt; set name = &quot;some-host&quot;
obj: host
name = &quot;some-host&quot;
&gt; set hardware-address = 00:80:c7:84:b1:94
obj: host
name = &quot;some-host&quot;
hardware-address = 00:80:c7:84:b1:94
&gt; set hardware-type = 1
obj: host
name = &quot;some-host&quot;
hardware-address = 00:80:c7:84:b1:94
hardware-type = 1
&gt; set ip-address = 192.168.4.40
obj: host
name = &quot;some-host&quot;
hardware-address = 00:80:c7:84:b1:94
hardware-type = 1
ip-address = c0:a8:04:28
&gt; create
obj: host
name = &quot;some-host&quot;
hardware-address = 00:80:c7:84:b1:94
hardware-type = 00:00:00:01
ip-address = c0:a8:04:28
&gt; 
</pre>
<p> Your dhcpd.leases file would then have an entry like this in it: </p>
<pre><code>
host some - host
{
    dynamic;
    hardware ethernet 00 : 80 : c7 : 84 : b1 : 94;
    fixed - address 192.168.4.40;
}
</code></pre>
<p> The <i>dynamic;</i> line is to denote that this host entry did not come from dhcpd.conf, but was created dynamically via OMAPI.</p>
<h2>RESETTING ATTRIBUTES</h2>
<p> If you want to remove an attribute from an object, you can do this with the <code>unset</code> command. Once you have unset an attribute, you must use the <code>update</code> command to update the remote object. So, if the host &quot;some-host&quot; from the previous example will not have a static IP address anymore, the commands in omshell would look like this: </p>
<pre>
obj: host
name = &quot;some-host&quot;
hardware-address = 00:80:c7:84:b1:94
hardware-type = 00:00:00:01
ip-address = c0:a8:04:28
&gt; unset ip-address
obj: host
name = &quot;some-host&quot;
hardware-address = 00:80:c7:84:b1:94
hardware-type = 00:00:00:01
ip-address = &lt;null&gt;
&gt; 
</pre>
<h2>REFRESHING OBJECTS</h2>
<p> A local object may be refreshed with the current remote object properties using the <code>refresh</code> command. This is useful for object that change periodically, like leases, to see if they have been updated. This isn&#8217;t particularly useful for hosts.</p>
<h2>DELETING OBJECTS</h2>
<p> Any remote object that can be created can also be destroyed. This is done by creating a new local object, setting attributes, associating the local and remote object using <code>open</code>, and then using the <code>remove</code> command. If the host &quot;some-host&quot; from before was created in error, this could be corrected as follows: </p>
<pre>
obj: host
name = &quot;some-host&quot;
hardware-address = 00:80:c7:84:b1:94
hardware-type = 00:00:00:01
ip-address = c0:a8:04:28
&gt; remove
obj: &lt;null&gt;
&gt; 
</pre>
<h2>HELP</h2>
<p> The <code>help</code> command will print out all of the commands available in omshell, with some syntax pointers.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-dhcpctl/">dhcpctl</a>(3), <a href="/docs/linux/man/3-omapi/">omapi</a>(3), <a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8), <a href="/docs/linux/man/8-dhclient/">dhclient</a>(8), <a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5), <a href="/docs/linux/man/5-dhclient-conf/">dhclient.conf</a>(5).</p>
<h2>AUTHOR</h2>
<p> <code>omshell</code> was written by Ted Lemon of Nominum, Inc. Information about Nominum can be found at <code><a rel="nofollow" href="http://www.nominum.com.">http://www.nominum.com.</a></code> This preliminary documentation was written by Wendy Verschoor of Nominum, Inc., while she was testing omshell. </p>
<h2>Index</h2>
