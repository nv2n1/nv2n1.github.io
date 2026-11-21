---
title: "suricata(1)"
name: "suricata"
section: "1"
letter: "s"
url: "/docs/linux/man/1-suricata/"
description: "suricata – Suricata"
---

<h2>NAME</h2>
<p> suricata &#8211; Suricata</p>
<h2>SYNOPSIS</h2>
<p> <code>suricata</code> [OPTIONS] [BPF FILTER]</p>
<h2>DESCRIPTION</h2>
<p> Suricata is a high performance Network IDS, IPS and Network Security Monitoring engine. Open Source and owned by a community run non-profit foundation, the Open Information Security Foundation (OISF).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Display a brief usage overview.</dd>
<dt><code>-V</code></dt>
<dd> Displays the version of Suricata.</dd>
<dt><code>-c &lt;path&gt;</code></dt>
<dd> Path to configuration file.</dd>
<dt><code>-T</code></dt>
<dd> Test configuration.</dd>
<dt><code>-v</code></dt>
<dd> The -v option enables more verbosity of Suricata&#8217;s output. Supply multiple times for more verbosity.</dd>
<dt><code>-r &lt;path&gt;</code></dt>
<dd> Run in pcap offline mode reading files from pcap file.</dd>
<dt><code>-i &lt;interface&gt;</code></dt>
<dd> After the -i option you can enter the interface card you would like to use to sniff packets from. This option will try to use the best capture method available.</dd>
<dt><code>&#8211;pcap[=&lt;device&gt;]</code></dt>
<dd> Run in PCAP mode. If no device is provided the interfaces provided in the <i>pcap</i> section of the configuration file will be used.</dd>
<dt><code>&#8211;af-packet[=&lt;device&gt;]</code></dt>
<dd> Enable capture of packet using AF_PACKET on Linux. If no device is supplied, the list of devices from the af-packet section in the yaml is used.</dd>
<dt><code>-q &lt;queue id&gt;</code></dt>
<dd> Run inline of the NFQUEUE queue ID provided. May be provided multiple times.</dd>
<dt><code>-s &lt;filename.rules&gt;</code></dt>
<dd> With the -s option you can set a file with signatures, which will be loaded together with the rules set in the yaml.</dd>
<dt><code>-S &lt;filename.rules&gt;</code></dt>
<dd> With the -S option you can set a file with signatures, which will be loaded exclusively, regardless of the rules set in the yaml.</dd>
<dt><code>-l &lt;directory&gt;</code></dt>
<dd> With the -l option you can set the default log directory. If you already have the default-log-dir set in yaml, it will not be used by Suricata if you use the -l option. It will use the log dir that is set with the -l option. If you do not set a directory with the -l option, Suricata will use the directory that is set in yaml.</dd>
<dt><code>-D</code></dt>
<dd> Normally if you run Suricata on your console, it keeps your console occupied. You can not use it for other purposes, and when you close the window, Suricata stops running. If you run Suricata as deamon (using the -D option), it runs at the background and you will be able to use the console for other tasks without disturbing the engine running.</dd>
<dt><code>&#8211;runmode &lt;runmode&gt;</code></dt>
<dd> With the <i>&#8211;runmode</i> option you can set the runmode that you would like to use. This command line option can override the yaml runmode option. </dd>
<p> Runmodes are: <i>workers</i>, <i>autofp</i> and <i>single</i>. </p>
<p> For more information about runmodes see <code>Runmodes</code> in the user guide.</p>
<dt><code>-F &lt;bpf filter file&gt;</code></dt>
<dd> Use BPF filter from file.</dd>
<dt><code>-k [all|none]</code></dt>
<dd> Force (all) the checksum check or disable (none) all checksum checks.</dd>
<dt><code>&#8211;user=&lt;user&gt;</code></dt>
<dd> Set the process user after initialization. Overrides the user provided in the <i>run-as</i> section of the configuration file.</dd>
<dt><code>&#8211;group=&lt;group&gt;</code></dt>
<dd> Set the process group to group after initialization. Overrides the group provided in the <i>run-as</i> section of the configuration file.</dd>
<dt><code>&#8211;pidfile &lt;file&gt;</code></dt>
<dd> Write the process ID to file. Overrides the <i>pid-file</i> option in the configuration file and forces the file to be written when not running as a daemon.</dd>
<dt><code>&#8211;init-errors-fatal</code></dt>
<dd> Exit with a failure when errors are encountered loading signatures.</dd>
<dt><code>&#8211;disable-detection</code></dt>
<dd> Disable the detection engine.</dd>
<dt><code>&#8211;dump-config</code></dt>
<dd> Dump the configuration loaded from the configuration file to the terminal and exit.</dd>
<dt><code>&#8211;build-info</code></dt>
<dd> Display the build information the Suricata was built with.</dd>
<dt><code>&#8211;list-app-layer-protos</code></dt>
<dd> List all supported application layer protocols.</dd>
<dt><code>&#8211;list-keywords=[all|csv|&lt;kword&gt;]</code></dt>
<dd> List all supported rule keywords.</dd>
<dt><code>&#8211;list-runmodes</code></dt>
<dd> List all supported run modes.</dd>
<dt><code>&#8211;set &lt;key&gt;=&lt;value&gt;</code></dt>
<dd> Set a configuration value. Useful for overriding basic configuration parameters in the configuration. For example, to change the default log directory: </dd>
<pre>
--set default-log-dir=/var/tmp
</pre>
<dt><code>&#8211;engine-analysis</code></dt>
<dd> Print reports on analysis of different sections in the engine and exit. Please have a look at the conf parameter engine-analysis on what reports can be printed</dd>
<dt><code>&#8211;unix-socket=&lt;file&gt;</code></dt>
<dd> Use file as the Suricata unix control socket. Overrides the <i>filename</i> provided in the <i>unix-command</i> section of the configuration file.</dd>
<dt><code>&#8211;pcap-buffer-size=&lt;size&gt;</code></dt>
<dd> Set the size of the PCAP buffer (0 &#8211; 2147483647).</dd>
<dt><code>&#8211;netmap[=&lt;device&gt;]</code></dt>
<dd> Enable capture of packet using NETMAP on FreeBSD or Linux. If no device is supplied, the list of devices from the netmap section in the yaml is used.</dd>
<dt><code>&#8211;pfring[=&lt;device&gt;]</code></dt>
<dd> Enable PF_RING packet capture. If no device provided, the devices in the Suricata configuration will be used.</dd>
<dt><code>&#8211;pfring-cluster-id &lt;id&gt;</code></dt>
<dd> Set the PF_RING cluster ID.</dd>
<dt><code>&#8211;pfring-cluster-type &lt;type&gt;</code></dt>
<dd> Set the PF_RING cluster type (cluster_round_robin, cluster_flow).</dd>
<dt><code>-d &lt;divert-port&gt;</code></dt>
<dd> Run inline using IPFW divert mode.</dd>
<dt><code>&#8211;dag &lt;device&gt;</code></dt>
<dd> Enable packet capture off a DAG card. If capturing off a specific stream the stream can be select using a device name like &quot;dag0:4&quot;. This option may be provided multiple times read off multiple devices and/or streams.</dd>
<dt><code>&#8211;napatech</code></dt>
<dd> Enable packet capture using the Napatech Streams API.</dd>
<dt><code>&#8211;mpipe</code></dt>
<dd> Enable packet capture using the TileGX mpipe interface.</dd>
<dt><code>&#8211;erf-in=&lt;file&gt;</code></dt>
<dd> Run in offline mode reading the specific ERF file (Endace extensible record format).</dd>
<dt><code>&#8211;simulate-ips</code></dt>
<dd> Simulate IPS mode when running in a non-IPS mode.</dd></dl>
<h2>OPTIONS FOR DEVELOPERS</h2>
<dl>
<dt><code>-u</code></dt>
<dd> Run the unit tests and exit. Requires that Suricata be compiled with <i>&#8211;enable-unittests</i>.</dd>
<dt><code>-U, &#8211;unittest-filter=REGEX</code></dt>
<dd> With the -U option you can select which of the unit tests you want to run. This option uses REGEX. Example of use: suricata -u -U http</dd>
<dt><code>&#8211;list-unittests</code></dt>
<dd> List all unit tests.</dd>
<dt><code>&#8211;fatal-unittests</code></dt>
<dd> Enables fatal failure on a unit test error. Suricata will exit instead of continuuing more tests.</dd>
<dt><code>&#8211;unittests-coverage</code></dt>
<dd> Display unit test coverage report.</dd></dl>
<h2>SIGNALS</h2>
<p> Suricata will respond to the following signals:</p>
<dl>
<dt><code>SIGUSR2</code></dt>
<dd> Causes Suricata to perform a live rule reload.</dd>
<dt><code>SIGHUP</code></dt>
<dd> Causes Suricata to close and re-open all log files. This can be used to re-open log files after they may have been moved away by log rotation utilities.</dd></dl>
<h2>FILES AND DIRECTORIES</h2>
<dl>
<dt><code>/usr/local/etc/suricata/suricata.yaml</code></dt>
<dd> Default location of the Suricata configuration file.</dd>
<dt><code>/usr/local/var/log/suricata</code></dt>
<dd> Default Suricata log directory.</dd></dl>
<h2>BUGS</h2>
<p> Please visit Suricata&#8217;s support page for information about submitting bugs or feature requests.</p>
<h2>NOTES</h2>
<dl>
<dt>&bull;</dt>
<dd> Suricata Home Page <i><a rel="nofollow" href="https://suricata-ids.org/">https://suricata-ids.org/</a></i></dd>
<dt>&bull;</dt>
<dd> Suricata Support Page <i><a rel="nofollow" href="https://suricata-ids.org/support/">https://suricata-ids.org/support/</a></i></dd></dl>
<h2>COPYRIGHT</h2>
<p> 2016, OISF </p>
