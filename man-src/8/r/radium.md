---
title: "radium(8)"
name: "radium"
section: "8"
letter: "r"
url: "/docs/linux/man/8-radium/"
description: "radium – argus record multiplexor"
---

<p>radium &#8211; argus record multiplexor</p>
<h2>Synopsis</h2>
<p><code>radium</code> [ <code>options</code> ] [ <code>raoptions</code> ]</p>
<h2>Description</h2>
<p> <code>Radium</code> is a real-time Argus Record multiplexor that processes Argus records and Netflow records and outputs them to any number of client programs and files. <code>Radium</code> is a combination of the features of ra.1 and argus.8, supporting access for upto 128 client programs to argus records originating from remote data sources and/or local managed argus data files. Using <code>radium</code> you can construct complex distribution networks for collecting and processing argus data, and providing a single point of access to archived argus data. Designed to run as a daemon, <code>radium</code> generally reads argus records directly from a remote argus, and writes the transaction status information to a log file or open socket connected to an <code>argus</code> client (such as <code><a href="/docs/linux/man/1-ra/">ra</a>(1)</code>). <code>Radium</code> provides the same data access controls as argus.8, including remote filtering, source address based access control, indivual oriented strong authentication and confidentiality protection for the distributed data, using <code>SASL</code> and <code>tcp_wrapper</code> technology. Please refer to the INSTALL and README files for each distribution for a complete description. <code>Radium</code> is normally configured from a system <code>/etc/radium.conf</code> configuration file, or from a configuration file either in the <code>$RADIUMHOME</code> directory, or specified on the command line.</p>
<h2>Radium Specific Options</h2>
<p>Radium, like all ra based clients, supports a number of <code>ra options</code> including remote data access, reading from multiple files and filtering of input argus records through a terminating filter expression. <code><a href="/docs/linux/man/8-radium/">radium</a>(8)</code> specific options are:</p>
<h2>Options</h2>
<dl>
<dt><code>-B &lt;addr&gt;</code></p>
<dd>Specify the bind interface address for remote access. Acceptable values are IP version 4 addresses. The default is to bind to INADDR_ANY address.</p>
<dt><code>-d</code></p>
<dd>Run radium as a daemon. This will cause radium to do the things that Unix daemons do and return, if there were no errors, with radium running as a detached process.</p>
<dt><code>-e &lt;value&gt;</code></p>
<dd>Specify the source identifier for this <code>radium</code>. Acceptable values are numbers, hostnames or ip address.</p>
<dt><code>-f &lt;radium.conf&gt;</code></p>
<dd>Use <i>radium.conf</i> as a source of configuration information. Options set in this file override any other specification, and so this is the last word on option values. This file is read after the system /etc/radium.conf file is processed. See <i>radium.conf.5</i> for the configuration file format.</p>
<dt><code>-O</code></p>
<dd>Turn off Berkeley Packet Filter optimizer. No reason to do this unless you think the optimizer generates bad code.</p>
<dt><code>-p</code></p>
<dd>Override the persistent connection facility. <code>Radium</code> provides a fault tolerant feature for its remote argus data access facility. If the remote argus data source closes, <code>radium</code> will maintain its client connections, and attempt to reestablish its connection with remote source. This option overrides this behavior, causing <code>radium</code> to terminate if any of its remote sources closes.</p>
<dt><code>-P &lt;portnum&gt;</code></p>
<dd>Specifies the <code>&lt;portnum&gt;</code> for remote client connection. The default is to not support remote access. Setting the value to zero (0) will forceably turn off the facility.</p>
<dt><code>-S</code></p>
<dd>&lt;host[:port][//full/path/to/argus.data.file]&gt; Attach to a specific remote <i>host</i> to receive argus records. Append an optional port specifier to attach to a port value other than the default 561. Without the optional full pathname, <code>radium </code> will continuously transmit a stream of real-time flow records as they are received. With the optional filename, <code>radium</code> will open the argus datafile specified, and stream the contents, closing the connection with the file EOF. </p>
<dt><code>-T threshold[smh] (secs)</code></p>
<dd>Indicate that <i>radium</i> should correct the timestamps of received <i>argus</i> records, if they are out of sync by threshold secconds. Threshold can be specified with the extensions s, m, or h for seconds, minutes or hours. <code>-X</code> Clear existing radium configuration. This removes any initialization done prior to encountering this flag. Allows you to eliminate the effects of the <i>/etc/radium.conf</i> file, or any radium.conf files that may have been loaded. </p>
</dl>
<h2>Signals</h2>
<p><code>Radium</code> catches a number of <code><a href="/docs/linux/man/3-signal/">signal</a>(3)</code> events. The three signals <code>SIGHUP</code>, <code>SIGINT</code>, and <code>SIGTERM</code> cause <code>radium</code> to exit, writing TIMEDOUT status records for all currently active transactions. The signal <code>SIGUSR1</code> will turn on <code>debug</code> reporting, and subsequent <code>SIGUSR1</code> signals, will increment the <code>debug-level</code>. The signal <code>SIGUSR2</code> will cause <code>radium</code> to turn off all <code>debug</code> reporting.</p>
<h2>Environment</h2>
<pre>$RADIUMHOME - Radium Root directory
$RADIUMPATH - Radium.conf search path (/etc:$RADIUMHOME:$HOME)</pre>
<h2>Files</h2>
<pre>/etc/radium.conf - radium daemon configuration file 
/var/run/radium.#.#.pid - PID file </pre>
<h2>Examples</h2>
<p>Run <code>radium</code> as a daemon, reading records from a remote host, using port 561, and writing all its transaction status reports to <i>output-file</i>. This is a typical mode.</p>
<dl>
<dd>
<pre><code>radium -S remotehost:561 -d -e `hostname` -w </code><i>output-file</i></pre>
</dl>
<p> Collect records from multiple argi, using port 561 on one and port 430 on the other, and make all of these records available to other programs on port 562.</p>
<dl>
<dd>
<pre><code>radium -S host1:561 -S host2:430 -de `hostname` -P 562
</code></pre>
</dl>
<p> Collect records from multiple Cisco Netflow sources, using the default port, and make the resulting argus records available on port 562.</p>
<dl>
<dd>
<pre><code>radium -C -S host1 -S host2 -de `hostname` -P 562
</code></pre>
</dl>
<p> Radium supports both input filtering and output filtering, and radium supports multiple output streams, each with their own independant filters. If you are interested in distributing IP traffic only (input filter) and want to separate traffic into differing files based on traffic type, this simple example separates ICMP traffic from other traffic.</p>
<dl>
<dd>
<pre><code>radium -w </code><i>file1</i> &quot;icmp&quot; -w <i>file2</i> &quot;not icmp&quot; - ip</pre>
</dl>
<p> Audit the network activity that is flowing between the two gateway routers, whose ethernet addresses are 00:08:03:2D:42:01 and 00:00:0C:18:29:F1. Make records available to other programs through port 430/tcp.</p>
<dl>
<dd>
<pre><code>radium -S source -P 430 - ether host (0:8:3:2d:42:1 and 0:0:c:18:29:f1)</code> &amp;</pre>
</dl>
<p> Process argus records from a remote source only between 9am and 5pm every day and provide access to this stream on port 562.</p>
<dl>
<dd>
<pre><code>radium -S remotehost -t 9-17 -P 562
</code></pre>
<h2>Copyright</h2>
<p>Copyright (c) 2000-2016 QoSient, LLC All rights reserved.</p>
<h2>Authors</h2>
<pre>Carter Bullard (carter [at] qosient.com)</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-radium-conf/">radium.conf</a></code>(5), <code><a href="/docs/linux/man/8-argus/">argus</a></code>(8), <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5), <code><a href="/docs/linux/man/5-hosts_options/">hosts_options</a></code>(5), <code><a href="/docs/linux/man/8-tcpd/">tcpd</a></code>(8), <code><a href="/docs/linux/man/1-tcpdump/">tcpdump</a></code>(1) </p>
