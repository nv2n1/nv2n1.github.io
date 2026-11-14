---
title: "radclient(1)"
name: "radclient"
section: "1"
letter: "r"
url: "/docs/linux/man/1-radclient/"
description: "radclient – send packets to a RADIUS server, show reply"
---

<h2>NAME</h2>
<p> radclient &#8211; send packets to a RADIUS server, show reply</p>
<h2>SYNOPSIS</h2>
<p> <code>radclient</code> [<code>-4</code>] [<code>-6</code>] [<code>-c</code> <i>count</i>] [<code>-d</code> <i>raddb_directory</i>] [<code>-D</code> <i>dictionary_directory</i>] [<code>-f</code> <i>file</i>] [<code>-F</code>] [<code>-h</code>] [<code>-i</code> <i>id</i>] [<code>-n</code> <i>num_requests_per_second</i>] [<code>-p</code> <i>num_requests_in_parallel</i>] [<code>-q</code>] [<code>-r</code> <i>num_retries</i>] [<code>-s</code>] [<code>-S</code> <i>shared_secret_file</i>] [<code>-t</code> <i>timeout</i>] [<code>-v</code>] [<code>-x</code>] <i>server {acct|auth|status|disconnect|auto} secret</i></p>
<h2>DESCRIPTION</h2>
<p> <code>radclient</code> is a radius client program. It can send arbitrary radius packets to a radius server, then shows the reply. It can be used to test changes you made in the configuration of the radius server, or it can be used to monitor if a radius server is up. </p>
<p> <code>radclient</code> reads radius attribute/value pairs from it standard input, or from a file specified on the command line. It then encodes these attribute/value pairs using the dictionary, and sends them to the remote server. </p>
<p> The <i>User-Password</i> and <i>CHAP-Password</i> attributes are automatically encrypted before the packet is sent to the server. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-4</p>
<dd> Use IPv4 (default)</p>
<dt>-6</p>
<dd> Use IPv6</p>
<dt>-c&nbsp;<wbr><i>count</i></p>
<dd> Send each packet <i>count</i> times.</p>
<dt>-d&nbsp;<wbr><i>raddb_directory</i></p>
<dd> The directory that contains the user dictionary file. Defaults to <i>/etc/raddb</i>.</p>
<dt>-D&nbsp;<wbr><i>dictionary_directory</i></p>
<dd> The directory that contains the main dictionary file. Defaults to <i>/usr/share/freeradius</i>.</p>
<dt>-f&nbsp;<wbr><i>file[:file]</i></p>
<dd> File to read the attribute/value pairs from. If this is not specified, they are read from stdin. This option can be specified multiple times, in which case packets are sent in order by file, and within each file, by first packet to last packet. A blank line separates logical packets within a file. If a pair of files separated by a colon is specified, the second file will be used to filter the responses to requests from the first. The number of requests and filters must be the same. A summary of filter results will be displayed if -s is passed.</p>
<dt>-F</p>
<dd> Print the file name, packet number and reply code.</p>
<dt>-h</p>
<dd> Print usage help information.</p>
<dt>-i&nbsp;<wbr><i>id</i></p>
<dd> Use <i>id</i> as the RADIUS request Id.</p>
<dt>-n&nbsp;<wbr><i>num_requests_per_second</i></p>
<dd> Try to send <i>num_requests_per_second</i>, evenly spaced. This option allows you to slow down the rate at which radclient sends requests. When not using -n, the default is to send packets as quickly as possible, with no inter-packet delays. </p>
<p> Due to limitations in radclient, this option does not accurately send the requested number of packets per second.</p>
<dt>-p&nbsp;<wbr><i>num_requests_in_parallel</i></p>
<dd> Send <i>num_requests_in_parallel</i>, without waiting for a response for each one. By default, radclient sends the first request it has read, waits for the response, and once the response is received, sends the second request in its list. This option allows you to send many requests at simultaneously. Once <i>num_requests_in_parallel</i> are sent, radclient waits for all of the responses to arrive (or for the requests to time out), before sending any more packets. </p>
<p> This option permits you to discover the maximum load accepted by a RADIUS server.</p>
<dt>-P&nbsp;<wbr><i>proto</i></p>
<dd> Use <i>proto</i> transport protocol (&quot;tcp&quot; or &quot;udp&quot;). Only available if FreeRADIUS is compiled with TCP transport support.</p>
<dt>-q</p>
<dd> Go to quiet mode, and do not print out anything.</p>
<dt>-r&nbsp;<wbr><i>num_retries</i></p>
<dd> Try to send each packet <i>num_retries</i> times, before giving up on it. The default is 10.</p>
<dt>-s</p>
<dd> Print out some summaries of packets sent and received.</p>
<dt>-S&nbsp;<wbr><i>shared_secret_file</i></p>
<dd> Rather than reading the shared secret from the command-line (where it can be seen by others on the local system), read it instead from <i>shared_secret_file</i>.</p>
<dt>-t&nbsp;<wbr><i>timeout</i></p>
<dd> Wait <i>timeout</i> seconds before deciding that the NAS has not responded to a request, and re-sending the packet. The default timeout is 3.</p>
<dt>-v</p>
<dd> Print out version information.</p>
<dt>-x</p>
<dd> Print out debugging information.</p>
<dt>server[:port]</p>
<dd> The hostname or IP address of the remote server. Optionally a UDP port can be specified. If no UDP port is specified, it is looked up in <i>/etc/services</i>. The service name looked for is <code>radacct</code> for accounting packets, and <code>radius</code> for all other requests. If a service is not found in <i>/etc/services</i>, 1813 and 1812 are used respectively. </p>
<p> The RADIUS attributes read by <i>radclient</i> can contain the special attribute <code>Packet-Dst-IP-Address</code>. If this attribute exists, then that IP address is where the packet is sent, and the <code>server</code> specified on the command-line is ignored. </p>
<p> If the RADIUS attribute list always contains the <code>Packet-Dst-IP-Address</code> attribute, then the <code>server</code> parameter can be given as <code>&#8211;</code>. </p>
<p> The RADIUS attributes read by <i>radclient</i> can contain the special attribute <code>Packet-Dst-Port</code>. If this attribute exists, then that UDP port is where the packet is sent, and the <code>:port</code> specified on the command-line is ignored. </p>
<dt>acct | auth | status | disconnect | auto</p>
<dd> Use <code>auth</code> to send an authentication packet (Access-Request), <code>acct</code> to send an accounting packet (Accounting-Request), <code>status</code> to send an status packet (Status-Server), or <code>disconnect</code> to send a disconnection request. Instead of these values, you can also use a decimal code here. For example, code 12 is also <code>Status-Server</code>. </p>
<p> The RADIUS attributes read by <i>radclient</i> can contain the special attribute <code>Packet-Type</code>. If this attribute exists, then that type of packet is sent, and the <i>type</i> specified on the command-line is ignored. </p>
<p> If the RADIUS attribute list always contains the <code>Packet-Type</code> attribute, then the <code>type</code> parameter can be given as <code>auto</code>. </p>
<dt>secret</p>
<dd> The shared secret for this client. It needs to be defined on the radius server side too, for the IP address you are sending the radius packets from. </p>
</dl>
<h2>EXAMPLE</h2>
<p> A sample session that queries the remote server for <i>Status-Server</i> (not all servers support this, but FreeRADIUS has configurable support for it).</p>
<dl>
<dt>
<dd>
<pre>
$ echo &quot;Message-Authenticator = 0x00&quot; | radclient 192.0.2.42 status s3cr3t
Sending request to server 192.0.2.42, port 1812.
radrecv: Packet from host 192.0.2.42 code=2, id=140, length=54
    Reply-Message = &quot;FreeRADIUS up 21 days, 02:05&quot;
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-radiusd/">radiusd</a>(8),</p>
<h2>AUTHORS</h2>
<p> Miquel van Smoorenburg, miquels [at] cistron.nl. Alan DeKok &lt;aland [at] freeradius.org&gt; </p>
<h2>Index</h2>
