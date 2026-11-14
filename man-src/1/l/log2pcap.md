---
title: "log2pcap(1)"
name: "log2pcap"
section: "1"
letter: "l"
url: "/docs/linux/man/1-log2pcap/"
description: "log2pcap – Extract network traces from Samba log files"
---

<h2 class="name">NAME</h2>
<p> log2pcap &#8211; Extract network traces from Samba log files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>log2pcap [-h] [-q] [logfile] [pcap_file]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> log2pcap reads in a samba log file and generates a pcap file (readable by most sniffers, such as ethereal or tcpdump) based on the packet dumps in the log file. </p>
<p> The log file must have a <i>log level</i> of at least <code>5</code> to get the SMB header/parameters right, <code>10</code> to get the first 512 data bytes of the packet and <code>50</code> to get the whole packet.</p>
<h2>OPTIONS</h2>
<p> -h</p>
<dl>
<dt>
<dd> If this parameter is specified the output file will be a hex dump, in a format that is readable by the text2pcap utility.</dl>
<p> -q</p>
<dl>
<dt>
<dd> Be quiet. No warning messages about missing or incomplete data will be given.</dl>
<p> logfile</p>
<dl>
<dt>
<dd> Samba log file. log2pcap will try to read the log from stdin if the log file is not specified.</dl>
<p> pcap_file</p>
<dl>
<dt>
<dd> Name of the output file to write the pcap (or hexdump) data to. If this argument is not specified, output data will be written to stdout.</dl>
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<h2>EXAMPLES</h2>
<p> Extract all network traffic from all samba log files: </p>
<dl>
<dt>
<dd>
<pre>
                        $ log2pcap &lt; /var/log/* &gt; trace.pcap
        
</pre>
</dl>
<p> Convert to pcap using text2pcap: </p>
<dl>
<dt>
<dd>
<pre>
        $ log2pcap -h samba.log | text2pcap -T 139,139 - trace.pcap
        
</pre>
</dl>
<h2>VERSION</h2>
<p> This man page is correct for version 3 of the Samba suite.</p>
<h2>BUGS</h2>
<p> Only SMB data is extracted from the samba logs, no LDAP, NetBIOS lookup or other data. </p>
<p> The generated TCP and IP headers don&#8217;t contain a valid checksum.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-text2pcap/">text2pcap</a></code>(1), <code><a href="/docs/linux/man/1-ethereal/">ethereal</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> This manpage was written by Jelmer Vernooij. </p>
<h2>Index</h2>
