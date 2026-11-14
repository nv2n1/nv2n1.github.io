---
title: "sip2ncid(8)"
name: "sip2ncid"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sip2ncid/"
description: "sip2ncid – Inject CID info by snooping SIP invites"
---

<p><code>sip2ncid</code> &#8211; Inject CID info by snooping SIP invites</p>
<h2>Synopsis</h2>
<p><code>sip2ncid</code> [options] </p>
<p> <i>Options:</i> </p>
<pre>[-C &lt;filename&gt; | --config &lt;filename&gt;]
[-D | --debug]
[-h | --help]
[-i &lt;interface&gt; | --interface &lt;interface&gt;]
[-l | --list]
[-L &lt;filename&gt; | --logfile &lt;filename&gt;]
[-n &lt;[host][:port]&gt; | --ncid &lt;[host][:port&gt;]
[-P &lt;filename&gt; | --pidfile &lt;filename&gt;]
[-r &lt;dumpfile&gt; | --readfile &lt;dumpfile&gt;]
[-s &lt;[host][:port]&gt; | --sip &lt;[host][:port]&gt;]
[-T | --testall]
[-t | --testudp]
[-u | --usage]
[-V | --version]
[-v &lt;1-9&gt; | --verbose &lt;1-9&gt;]
[-w &lt;dumpfile&gt; | --writefile &lt;dumpfile&gt;]</pre>
<h2>Description</h2>
<p>Snoops SIP Invites via libpcap and injects the caller id information found to the NCID server specified. Snoops only udp traffic on the specified SIP host and port. </p>
<p> If <i>/var/log/sip2ncid.log</i> exists, it is used as a log file. </p>
<p> If a pid file is given, usually <i>/var/run/sip2ncid.pid</i><code>, then a pid file used to store the process ID. </p>
<p> The configuration file for </code><i>sip2ncid</i> is /etc/ncid/sip2ncid.conf.</p>
<h2>Options</h2>
<dl>
<dt><code>-C &lt;filename&gt; | &#8211;config &lt;filename&gt;</code></p>
<dd>Configuration file.<br />
 Default: /etc/ncid/sip2ncid.conf</p>
<dt><code>-D | &#8211;debug</code></p>
<dd>Debug mode, <i>sip2ncid</i> stays attached to the terminal.</p>
<dt><code>-h | &#8211;help</code></p>
<dd>Prints this help</p>
<dt><code>-i &lt;interface&gt; | &#8211;interface=&lt;interface&gt;</code></p>
<dd>Specifies the network interface to snoop on. If this is not specified then libpcap will pick a network interface. This will generally be the first ethernet interface found.</p>
<dt><code>-l | &#8211;listdevs</code></p>
<dd>Returns a list of all network device names that can be used.</p>
<dt><code>-L &lt;filename&gt; | &#8211;logfile=&lt;filename&gt;</code></p>
<dd>Specifies the logfile name to use. The logfile must exist before it is used.<br />
 Default log filename: /var/log/sip2ncid.log</p>
<dt><code>-n &lt;[host][:port]&gt; | &#8211;ncid=&lt;[host][:port]&gt;</code></p>
<dd>Specifies the NCID server to connect to. Port may be specified by suffixing the hostname with &lt;:port&gt;, or if you only want to change the port, just &lt;:port&gt;. By default it will connect to port 3333 on &quot;127.0.0.1&quot;.</p>
<dt><code>-P &lt;filename&gt; | &#8211;pidfile=&lt;filename&gt;</code></p>
<dd>Specifies the pidfile name to write. Set to <i>/var/run/ncidd.pid</i><code> in a rc or init script when used as a service. The program will still run if it does not have permission to write a pidfile. There is no default. If pidfile is not set, no pid file will be used.</p>
<dt>-r &lt;dumpfile&gt; | &#8211;readfile &lt;dumpfile&gt;</code></p>
<dd>Read packets from a libpcap capture file instead of the network. This also sets the testudp option, verbose to level 3, and no filter is applied. Mostly only useful for development and debug purposes.</p>
<dt><code>-s &lt;[host][:port]&gt; | &#8211;sip=&lt;[host][:port]&gt;</code></p>
<dd>Specifies the hostname of the SIP devie to snoop. You may also specify the UDP port by suffixing the hostname with :&lt;port&gt;, or if no hostname is wanted, just &lt;:port&gt;. If you do not specify a host, it defaults to the network interface. If you do not specify a port, it defaults to &lt;5061&gt; (Vonage default). Other Vonage ports are 5060 and 10000. The new Vonage default appears to be &lt;10000&gt;.</p>
<dt><code>-T | &#8211;testall</code></p>
<dd>Test for all packets. This option is used to check for IP packets without starting the NCID server. It will display a packet count and the packet type. It will not send any CID data to NCID. It also sets the debug option.</p>
<dt><code>-t | &#8211;testudp</code></p>
<dd>Test for SIP packets. This option is used to check if SIP packets exist without starting the NCID server. It will display the Caller ID line generated when a call comes in, and a CANCEL line if cancel was generated. It will not send any CID data to NCID. It also sets the debug option. <code>-u | &#8211;usage</code> Prints this help</p>
<dt><code>-V | &#8211;version</code></p>
<dd>Displays the version</p>
<dt><code>-v &lt;1-9&gt; | &#8211;verbose &lt;1-9&gt;</code></p>
<dd>Verbose mode. Output information, used for the logfile and the -D option. Set higher number for more information.<br />
 Default: verbose = 1<br />
 Most Useful: verbose = 3 (displays payload of all packets that matched the libpcap filter.</p>
<dt><code>-w &lt;dumpfile&gt; | &#8211;writefile &lt;dumpfile&gt;</code></p>
<dd>Write packets to a libpcap capture file. This also sets the debug option, verbose to level 3, and no filter is applied. Mostly only useful for development and debug purposes.</dl>
<h2>Files</h2>
<p>/etc/ncid/sip2ncid.conf</p>
<h2>Messages Format</h2>
<pre>CID: ###DATE&lt;MMDDHHMM&gt;...LINE&lt;####&gt;...NMBR&lt;###########&gt;...NAME&lt;words&gt;+++
CIDINFO: ###CANCEL...NMBR&lt;###########&gt;...DATE&lt;MMDDHHMM+++
CIDINFO: ###BYE...NMBR&lt;###########&gt;...DATE&lt;MMDDHHMM&gt;+++</pre>
<h3>Example</h3>
<pre>CID: ###DATE05311233...LINE1122...NMBR13215551212...NAMEBig John+++</pre>
<h2>Examples</h2>
<pre># run sip2ncid as root and view status and SIP packets:
sip2ncid -Dv3
# run sip2ncid as root and list all network device names:
sip2ncid --listdevs
# run sip2ncid as root in test mode to look for SIP packets.
sip2ncid --testudp
# run sip2ncid as root in test mode to look for any packets.
sip2ncid --testall</pre>
<h2>Diagnostics</h2>
<pre> Return Code Meaning
 ----------- -------
 0 Successful
 -100 Usage
 -101 Invalid port number
 -104 Configuration file error
 -107 Invalid number
 -110 PID file already exists
 -? System error</pre>
<h2>See Also</h2>
<p>sip2ncid.conf.5 ncidd.8, ncidd.conf.5 ncidd.alias.5 </p>
