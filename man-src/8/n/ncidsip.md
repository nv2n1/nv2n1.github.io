---
title: "ncidsip(8)"
name: "ncidsip"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ncidsip/"
description: "ncidsip – Inject CID info by snooping SIP invites"
---

<p><code>ncidsip</code> &#8211; Inject CID info by snooping SIP invites</p>
<h2>Synopsis</h2>
<p><code>ncidsip</code> [options] </p>
<p> <i>Options:</i> </p>
<pre>[-D | --debug]
[-d &lt;filename&gt; | --dumpfile &lt;filename&gt;]
[-i &lt;interface&gt; | --interface &lt;interface&gt;]
[-h | --help]
[-l | --list]
[-n &lt;host[:port]&gt; | --ncid &lt;host[:port]&gt;]
[-s &lt;[host][:port]&gt; | --sip &lt;[host][:port]&gt;]
[-p &lt;filename&gt; | --pidfile &lt;filename&gt;]
[-t | --test]
[-u | --usage]
[-V | --version]
[-v | --verbose]</pre>
<h2>Description</h2>
<p>Snoops SIP Invites via libpcap and injects the caller id information found to the NCID server specified. Uses Net::Pcap to interface with the libpcap library and snoops only udp traffic on the specified SIP host and port. </p>
<p> The configuration file for <i>ncidsip</i> is /etc/ncid/ncidsip.conf.</p>
<h2>Options</h2>
<dl>
<dt><code>-s &lt;[host][:port]&gt; | &#8211;sip=&lt;[host][:port]&gt;</code></p>
<dd>Specifies the hostname of the SIP devie to snoop. You may also specify the UDP port by suffixing the hostname with :&lt;port&gt;, or if no hostname is wanted, just :&lt;port&gt;. If you do not specify a host, it defaults to the network interface. If you do not specify a port, it defaults to &lt;5061&gt; (Vonage default). Other Vonage ports are 5060 and 10000. The new Vonage default appears to be &lt;10000&gt;.</p>
<dt><code>-n &lt;host[:port]&gt; | &#8211;ncid=&lt;host[:port]&gt;</code></p>
<dd>Specifies the NCID server to connect to. Port may be specified by suffixing the hostname with :&lt;port&gt;. By default it will connect to port 3333 on &quot;localhost&quot;.</p>
<dt><code>-i &lt;interface&gt; | &#8211;interface=&lt;interface&gt;</code></p>
<dd>Specifies the network interface to snoop on. If this is not specified then libpcap will pick a network interface. This will generally be the first ethernet interface found.</p>
<dt><code>-p &lt;filename&gt; | &#8211;pidfile=&lt;filename&gt;</code></p>
<dd>Specifies the pidfile name to write. Set to <i>/var/run/ncidsip.pid</i><code> in a rc or init script when used as a service. The program will still run if it does not have permission to write a pidfile. There is no default, if pidfile is not set, no pid file will be used.</p>
<dt>-h | &#8211;help</code></p>
<dd>Prints this help</p>
<dt><code>-D | &#8211;debug</code></p>
<dd>Display the payload of all packets that matched the libpcap filter.</p>
<dt><code>-d &lt;filename&gt; | &#8211;dumpfile &lt;filename&gt;</code></p>
<dd>Read packets from a libpcap capture file instead of the network. Mostly only useful for development purposes.</p>
<dt><code>-u | &#8211;usage</code></p>
<dd>Prints this help</p>
<dt><code>-V | &#8211;version</code></p>
<dd>Displays the version</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd>Displays status. Use this option to run interactive.</p>
<dt><code>-l | &#8211;listdevs</code></p>
<dd>Returns a list of all network device names that can be used.</p>
<dt><code>-t | &#8211;test</code></p>
<dd>Test for SIP packets. This option is used to check if SIP packets exist without starting the NCID server. It will display the Caller ID line generated when a call comes in, and a CANCEL line if cancel was generated.</dl>
<h2>Files</h2>
<p>/etc/ncid/ncidsip.conf</p>
<h2>Cid Message Format</h2>
<pre>CID: ###DATEmmddhhss...LINEidentifier...NMBRnumber...NAMEwords+++</pre>
<h3>Example</h3>
<pre>CID: ###DATE05311233...LINE1122...NMBR13215551212...NAMEBig John+++</pre>
<h2>Examples</h2>
<pre># run ncidsip as root and view status:
ncidsip -v
# run ncidsip as root and list all network device names:
ncidsip --listdevs
# run ncidsip as root and view SIP packets:
ncidsip --debug
# run sip from the init file at boot:
ncidsip</pre>
<h2>See Also</h2>
<p>ncidsip.conf.5, sip2ncid.8, ncidd.8 </p>
