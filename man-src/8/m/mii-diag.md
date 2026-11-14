---
title: "mii-diag(8)"
name: "mii-diag"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mii-diag/"
description: "mii-diag – Network adapter control and monitoring"
---

<p>mii-diag &#8211; Network adapter control and monitoring</p>
<h2>Synopsis</h2>
<p><code>mii-diag</code> [<i>options</i>]<i>&lt;interface&gt;</i></p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>mii-diag</code> network adapter control and monitoring command. Addition documentation is available from <a rel="nofollow" href="http://scyld.com/diag/index.html.">http://scyld.com/diag/index.html.</a> This <code>mii-diag</code> command configures, controls and monitors the transceiver management registers for network interfaces, and configures driver operational parameters. For transceiver control <code>mii-diag</code> uses the Media Independent Interface (MII) standard (thus the command name). It also has additional Linux-specific controls to communicate parameters such as message enable settings and buffer sizes to the underlying device driver. The MII standard defines registers that control and report network transceiver capabilities, link settings and errors. Examples are link speed, duplex, capabilities advertised to the link partner, status LED indications and link error counters. </p>
<h2>Options</h2>
<p>The <code>mii-diag</code> command supports both single character and long option names. Short options use a single dash (´-´) in front of the option character. For options without parameters, multiple options may be concatenated after a single dash. Long options are prefixed by two dashes (´&#8211;´), and may be abbreviated with a unique prefix. A long option may take a parameter of the form &#8211;arg=param or &#8211;arg param. </p>
<p> A summary of options is as follows. </p>
<dl>
<dt><code>-A, &#8211;advertise &lt;speed|setting&gt;</code></p>
<dd><code>-F, &#8211;fixed-speed &lt;speed|setting&gt;</code> </p>
<p> Speed is one of: 100baseT4, 100baseTx, 100baseTx-FD, 100baseTx-HD, 10baseT, 10baseT-FD, 10baseT-HD. For more precise control an explicit numeric register setting is also allowed. </p>
<dt><code>-a, &#8211;all-interfaces</code></p>
<dd>Show the status of all interfaces. This option is not recommended with any other option, especially ones that change settings. </p>
<dt><code>-s,&#8211;status</code></p>
<dd>Return exit status 2 if there is no link beat. </p>
<dt><code>-D</code></p>
<dd>Increase the debugging level. This may be used to understand the actions the command is taking. </p>
<dt><code>-g, &#8211;read-parameters</code></p>
<dd>Show driver-specific parameters. </p>
<dt><code>-G, &#8211;set-parameters value[,value&#8230;]</code></p>
<dd>Set driver-specific parameters. Set a adapter-specific parameters. Parameters are comma separated, with missing elements retaining the existing value. </p>
<dt><code>-v</code></p>
<dd>Increase the verbosity level. Additional &quot;-v&quot; options increase the level further. </p>
<dt><code>-V</code></p>
<dd>Show the program version information. </p>
<dt><code>-w, &#8211;watch</code></p>
<dd>Continuously monitor the transceiver and report changes. </p>
<dt><code>-?</code></p>
<dd>Emit usage information. </p>
</dl>
<h2>Description</h2>
<p>Calling the command with just the interface name produces extensive output describing the transceiver capabilities, configuration and current status. The &#8216;&#8211;monitor&#8217; option allows scripting link beat changes. This option is similar to &#8211;watch, but with lower overhead and simplified output. It polls the interface only once a second and the output format is a single line per link change with three fixed words<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;unknown|down||negotiating|up&gt;&nbsp;<wbr>&lt;STATUS&gt;&nbsp;<wbr>&lt;PARTNER-CAP&gt; Example output: mii-diag &#8211;monitor eth0<br />
down&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x7809 0x0000<br />
negotiating&nbsp;<wbr>&nbsp;<wbr>0x7829 0x45e1<br />
up&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x782d 0x45e1<br />
down&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x7809 0x0000 This may be used as<br />
&nbsp;<wbr>&nbsp;<wbr>mii-diag &#8211;monitor eth0 |<br />
&nbsp;<wbr>while read linkstatus bmsr linkpar;&nbsp;<wbr>do<br />
&nbsp;<wbr>&nbsp;<wbr>case&nbsp;<wbr>$linkstatus in<br />
&nbsp;<wbr>&nbsp;<wbr>up)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ifup eth0&nbsp;<wbr>;;<br />
&nbsp;<wbr>&nbsp;<wbr>down)&nbsp;<wbr>ifdown eth0&nbsp;<wbr>;;<br />
&nbsp;<wbr>&nbsp;<wbr>esac<br />
&nbsp;<wbr>done It may be useful to shorten the DHCP client daemon timeout if it does not receive an address by adding the following setting to /etc/sysconfig/network: DHCPCDARGS=&quot;-t 3&quot; </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ether-wake/">ether-wake</a></code>(8),<code><a href="/docs/linux/man/8-net-diag/">net-diag</a></code>(8),<code><a href="/docs/linux/man/8-mii-tool/">mii-tool</a></code>(8).<br />
 Addition documentation is available from <a rel="nofollow" href="http://scyld.com/diag/index.html.">http://scyld.com/diag/index.html.</a> </p>
<h2>Known Bugs</h2>
<p>The &#8211;all-interfaces option is quirky. There are very few settings that are usefully applied to all interfaces.</p>
<h2>Author</h2>
<p>The manual pages, diagnostic commands, and many of the underlying Linux network drivers were written by Donald Becker for the Scyld Beowulf() cluster system.</p>
