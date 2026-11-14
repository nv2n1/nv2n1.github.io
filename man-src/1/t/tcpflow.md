---
title: "tcpflow(1)"
name: "tcpflow"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tcpflow/"
description: "tcpflow – TCP flow recorder"
---

<h2>NAME</h2>
<p> tcpflow &#8211; TCP flow recorder</p>
<h2>SYNOPSIS</h2>
<p> <code>tcpflow</code> [<code>-aBcCDhpsvVZ</code>] [<code>-b</code><i>&nbsp;<wbr>max_bytes</i>] [<code>-d</code><i>&nbsp;<wbr>debug_level</i>] [<code>-[eE]</code><i>&nbsp;<wbr>scanner</i>] [<code>-f</code><i>&nbsp;<wbr>max_fds</i>] [<code>-F[ctTXMkmg]</code>] [<code>-i</code><i>&nbsp;<wbr>iface</i>] [<code>-L</code><i>&nbsp;<wbr>semlock</i>] [<code>-m</code><i>&nbsp;<wbr>min_bytes</i>] [<code>-o</code><i>&nbsp;<wbr>outdir</i>] [<code>-r</code><i>&nbsp;<wbr>file1.pcap</i>] [<code>-R</code><i>&nbsp;<wbr>file0.pcap</i>] [<code>-S</code><i>name=value</i>] [<code>-T[filename template]</code>] [<code>-w</code><i>file</i>] [<code>-x scanner</code>] [<code>-X</code><i>&nbsp;<wbr>file.xml</i>] [<code>expression</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>tcpflow</code> is a program that captures data transmitted as part of TCP connections (flows), and stores the data in a way that is convenient for protocol analysis or debugging. Rather than showing packet-by-packet information, tcpflow reconstructs the actual data streams and stores each flow in a separate file for later analysis. tcpflow understands TCP sequence numbers and will correctly reconstruct data streams regardless of retransmissions or out-of-order delivery. tcpflow provides control over filenames for automatic binning of connections by protocol, IP adress or connection number, and has a sophisticated plug-in system for decompressing compressed HTTP connections, undoing MIME encoding, or calling user-provided programs for post-processing. </p>
<p> By default tcpflow stores all captured data in files that have names of the form: </p>
<pre>
<code>192.168.101.102.02345-010.011.012.013.45103</code>
</pre>
<p> ,&#8230;where the contents of the above file would be data transmitted from host 192.168.101.102 port 2345, to host 10.11.12.13 port 45103. </p>
<p> If you want to simply process a few hundred thousand packets and see what you have, try this: </p>
<pre>
<code>tcpflow -a -o outdir -Fk -r packets.pcap</code>
</pre>
<p> This will cause tcpflow to perform (-a) all processing, store the output in a directory called <code>outdir,</code> bin the output in directories of 1000 connections each, and read its input from the file <code>packets.pcap</code>. More sophisticiated processing is possible, of course.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Enable all processing. Same as <code>-e all.</code></p>
<dt><code>-B</code></p>
<dd> Force binary output even when printing to console with <code>-C </code> or <code>-c.</code></p>
<dt><code>-b </code><i>max_bytes</i></p>
<dd> Specifies the maximum size of a captured flow. Any bytes beyond <i>max_bytes</i> from the first byte captured will be discarded. The default is to store an unlimited number of bytes per flow. <code>Note:</code> previous versions of <code>tcpflow</code> could only store a maximum of 4GiB per flow, but version 1.4 and above can really store an unlimited amount of bytes. Good thing that modern disks are so big, eh?</p>
<dt><code>-c</code></p>
<dd> Console print. Print the contents of packets to stdout as they are received, without storing any captured data to files (implies</p>
<dt><code>-C</code></p>
<dd> Console print without the packet source and destination details being printed. Print the contents of packets to stdout as they are received, without storing any captured data to files (implies <code>-e</code> When outputting to the console each flow will be output in different colors (blue for client to server flows, red for server to client flows, green for undecided flows). <code>-s</code> ).</p>
<dt><code>-D</code></p>
<dd> Console output should be in hex.</p>
<dt><code>-d</code></p>
<dd> Debug level. Set the level of debugging messages printed to stderr to <i>debug_level</i>. Higher numbers produce more messages. <code>-d 0</code> causes completely silent operation. <code>-d 1</code> , the default, produces minimal status messages. <code>-d 10</code> produces verbose output equivalent to <code>-v .</code> Numbers higher than 10 can produce a large amount of debugging information useful only to developers.</p>
<dt><code>-E name</code></p>
<dd> Disable all scanners and then enable scanner <code>name</code></p>
<dt><code>-e name</code></p>
<dd> Enable scanner <code>name.</code></p>
<dt><code>-e all</code></p>
<dd> Enables all scanners. Same as <code>-a</code></p>
<dt><code>-e http</code></p>
<dd> Perform HTTP post-processing (&quot;After&quot; processing). If the output file is </p>
<pre>
<code>208.111.153.175.00080-192.168.001.064.37314,</code>
</pre>
<p> Then the post-processing will create the files: </p>
<pre>
<code>208.111.153.175.00080-192.168.001.064.37314-HTTP</code>
<code>208.111.153.175.00080-192.168.001.064.37314-HTTPBODY</code>
</pre>
<p> If the HTTPBODY was compressed with GZIP, you may get a third file as well: </p>
<pre>
<code>208.111.153.175.00080-192.168.001.064.37314-HTTPBODY-GZIP</code>
</pre>
<p> Additional information about these streams, such as their MD5 hash value, is also written to the DFXML file</p>
<dt><code>-F[format]</code></p>
<dd> Specifies format for output filenames. Format specifiers: <code>c</code> appends the connection counter to ALL filenames. <code>t</code> prepends each filename with a Unix timestamp. <code>T</code> prepends each filename with an ISO-8601 timestamp. <code>X</code> Do not output any files (other than the <code>report.xml </code> report files).</p>
<dt><code>-FM</code></p>
<dd> Include MD5 of each flow in the DFXML output.</p>
<dt><code>-FX</code></p>
<dd> Suppresses file output entirely (DFXML file is still produced).</p>
<dt><code>-Fk</code></p>
<dd> bin output in 1K directories</p>
<dt><code>-Fm</code></p>
<dd> bin output in 1M directories (2 levels)</p>
<dt><code>-Fg</code></p>
<dd> bin output in 1G directories (3 levels) <code>-T[format]</code> Specifies an arbitrary template for filenames. <code>%A</code> expands to source IP address. <code>%a</code> expands to source IP port. <code>%B</code> expands to destination IP address. <code>%a</code> expands to destination IP port. <code>%T</code> expands to timestamp in ISO8601 format. <code>%t</code> expands to timestamp in Unix time_t format. <code>%V</code> expands to &quot;&#8211;&quot; if a VLAN is present. <code>%v</code> expands to the VLAN number if a VLAN is present. <code>%C</code> expands to &quot;c&quot; if the connection count&gt;0. <code>%c</code> expands to the connection count if the connection count&gt;0. <code>%#</code> always expands to the connection count. <code>%%</code> prints a &quot;%&quot;.</p>
<dt><code>-f</code><i>max_fds</i></p>
<dd> Max file descriptors used. Limit the number of file descriptors used by tcpflow to <i>max_fds</i>. Higher numbers use more system resources, but usually perform better. If the underlying operating system supports the <code>setrlimit()</code> system call, the OS will be asked to enforce the requested limit. The default is for tcpflow to use the maximum number of file descriptors allowed by the OS. The <code>-v</code> option will report how many file descriptors tcpflow is using.</p>
<dt><code>-h</code></p>
<dd> Help. Print usage information and exit.</p>
<dt><code>-hh</code></p>
<dd> More help. Print more usage information and exit.</p>
<dt><code>-i </code><i>iface</i></p>
<dd> Interface name. Capture packets from the network interface named <i>iface</i>. If no interface is specified with <code>-i</code> , a reasonable default will be used by libpcap automatically.</p>
<dt><code>-L </code><i>semlock_name</i></p>
<dd> Specifies that <i>semlock_name</i> should be used as a Unix semaphore to prevent two different copies of tcpflow running in two different processes but outputing to the same standard output from printing on top of each other. This is an application of Unix named semaphores; bet you have never seen one before.</p>
<dt><code>-l</code></p>
<dd> Treat the following arguments as filenames with an assumed <code>-r</code> command before each one. This allows you to read a lot of files at once with shell globbing. For example, to process all of the pcap files in the current directory, use this: </p>
<pre>
<code>tcpflow -o out -a -l *.pcap</code>
</pre>
<dt><code>-J</code></p>
<dd> Output flow information to console in multiple colors. <code>NOTE: This option was changed from tcpflow 1.3.</code></p>
<dt><code>-m </code><i>min_size</i></p>
<dd> Forces a new connection output file when there is a skip in the TCP session of <i>min_size</i> bytes or more.</p>
<dt><code>-o </code><i>outdir</i></p>
<dd> Specifies the output directory where the transcript files will be written.</p>
<dt><code>-P</code></p>
<dd> No purge. Normally tcpflow removes connections from the hash table after the connection is closed with a FIN. This conserves memory but takes additional CPU time. Selecting this option causes the std::tr1:unordered_map to grow without bounds, as tcpflow did prior to version 1.1. That makes tcpflow run faster if there are less than 10 million connections, but can lead to out-of-memory errors.</p>
<dt><code>-p</code></p>
<dd> No promiscuous mode. Normally, tcpflow attempts to put the network interface into promiscuous mode before capturing packets. The <code>-p</code> option tells tcpflow <i>not</i> to put the interface into promiscuous mode. Note that it might already be in promiscuous mode for some other reason.</p>
<dt><code>-q</code></p>
<dd> Quiet mode &#8212; don&#8217;t print warnings. Currently the only warning that <code>tcpflow</code> prints is a warning when more than 10,000 files are created that the user should have provided the <code>-Fk</code>, <code>-Fm</code>, or <code>-Fg</code> options. We might have other warnings in the future.</p>
<dt><code>-r</code></p>
<dd> Read from file. Read packets from <i>file</i>, which was created using the <code>-w</code> option of <i><a href="/docs/linux/man/1-tcpdump/">tcpdump</a></i>(1). This option may be repeated any number of times. Standard input is used if <i>file</i> is &quot;-&quot;. Note that for this option to be useful, tcpdump&#8217;s <code>-s</code> option should be used to set the snaplen to the MTU of the interface (e.g., 1500) while capturing packets.</p>
<dt><code>-R</code></p>
<dd> Read from a file, but only to complete TCP flows. This option is used when <i>tcpflow</i> is used to process a series of files that are captured over time. For each time period <i>n,</i> file <i>filen.pcap</i> should be processed with <code>R -r </code><i>filen.pcap</i>, while <i>file(n-1).pcap</i> should be processed with <i>R -R file(n-1).pcap.</i></p>
<dt><code>-S</code><i>name</i><code>=</code><i>value</i></p>
<dd> Sets a <i>name</i> parameter to be equal to <i>value</i> for a plug-in. Use <code>-hh</code> to find out all of the settable parameters.</p>
<dt><code>-s</code></p>
<dd> Strip non-printables. Convert all non-printable characters to the &quot;.&quot; character before printing packets to the console or storing them to a file.</p>
<dt><code>-V</code></p>
<dd> Print the version number and exit.</p>
<dt><code>-v</code></p>
<dd> Verbose operation. Verbosely describe tcpflow&#8217;s operation. Equivalent to <code> -d 10</code>.</p>
<dt><code>-w </code><i>filename.pcap</i></p>
<dd> Write packets that were not processed to <i>filename.pcap</i>. Typically this will be UDP packets.</p>
<dt><code>-X </code><i>filename.xml</i></p>
<dd> Write a DFXML report file to <i>filename.xml</i>. The file contains a record of every tcp connection, how the tcpflow program was compiled, and the computer on which tcpflow was run.</p>
<dt><code>-Z</code></p>
<dd> Don&#8217;t decompress gzip-compressed streams.</dl>
<h2>EXAMPLES</h2>
<p> To record all packets arriving at or departing from <i>sundown</i> and extract all of the HTTP attachments:</p>
<dl>
<dt>
<dd>
<pre>
<code>tcpflow -e scan_http -o outdir host sundown</code>
</pre>
</dl>
<p> To record traffic between <i>helios</i> and either <i>hot</i> or <i>ace</i> and bin the results into 1000 files per directory and calculate the MD5 of each flow:</p>
<dl>
<dt>
<dd>
<pre>
<code>tcpflow -X report.xml -e scan_md5 -o outdir -Fk host helios and \( hot or ace \)</code>
</pre>
</dl>
<h2>BUGS</h2>
<p> Please send bug reports to simsong [at] acm.org. </p>
<p> tcpflow currently does not understand IP fragments. Flows containing IP fragments will not be recorded correctly.</p>
<h2>AUTHORS</h2>
<p> Originally by Jeremy Elson &lt;jelson [at] circlemud.org&gt;. Substantially modified and maintained by Simson L. Garfinkel &lt;simsong [at] acm.org&gt;. Network visualization code by Michael Shick &lt;mike [at] shick.in&gt; </p>
<p> The current version of this software is available at</p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="http://www.digitalcorpora.org/downloads/tcpflow/">http://www.digitalcorpora.org/downloads/tcpflow/</a></i> </p>
</dl>
<p> An announcement mailing list for this program is at:</p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="http://groups.google.com/group/tcpflow-users">http://groups.google.com/group/tcpflow-users</a></i></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tcpdump/">tcpdump</a>(1), <a href="//www.systutorials.com/docs/linux/man/4P-nit/">nit</a>(4P), <a href="/docs/linux/man/4-bpf/">bpf</a>(4), <a href="/docs/linux/man/3-pcap/">pcap</a>(3), <a href="/docs/linux/man/5-pcap-savefile/">pcap-savefile</a>(5), <a href="/docs/linux/man/7-pcap-filter/">pcap-filter</a>(7) </p>
<h2>Index</h2>
