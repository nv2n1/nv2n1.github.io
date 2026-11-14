---
title: "axlisten(1)"
name: "axlisten"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axlisten/"
description: "axlisten – monitor AX.25 traffic"
---

<h2>NAME</h2>
<p> axlisten &#8211; monitor AX.25 traffic</p>
<h2>SYNOPSIS</h2>
<p> <code>axlisten [-8] [-a] [-c] [-h] [-i] [-p port] [-r] [-t] [-v]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Axlisten</code> uses SOCK_PACKET facilities to provide a network monitor of all AX.25 traffic heard by the system. Since KISS is implicitly promiscuous no special driver configurations are needed. </p>
<p> This version displays standard AX.25, PE1CHL extended AX.25, NET/ROM, Rose, ARP, IP, ICMP, TCP and UDP. It also displays IP, TCP, ICMP, TCP and UDP encapsulated within NET/ROM frames. The program also displays AX.25 and IP encapsulated within an IP frame, but see RFC1326 for reasons not to do so. </p>
<p> <code>Axlisten</code> makes an attempt at decoding some of the more common routing protocols. RSPF and RIP (both lqnormalrq and G8BPQs RIP98) are traced. JNOS style NET/ROM node polls are also displayed. </p>
<p> <code>Axlisten</code> can use colors to make the output more readable. The ncurses library is used to accomplish this. <code>Color support defaults to being disabled,</code> and the <code>-c</code> parameter is used to enable it.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-8</code></p>
<dd> Indicates that the terminal is capable of printing 8-bit characters. This parameter is required for the -i parameter to work.</p>
<dt><code>-a</code></p>
<dd> Allow for the monitoring of outgoing frames as well as incoming ones.</p>
<dt><code>-c</code></p>
<dd> Enable color support.</p>
<dt><code>-h</code></p>
<dd> Dump the data portion of the packet in both hexadecimal and ASCII. The default is to display data as ASCII only.</p>
<dt><code>-i</code></p>
<dd> Map IBM codepage 437 characters 128-158 to their ISO-Latin-1 equivalents. This is a hack for scandinavian users. This parameter is only valid when used with the -8 and -c parameters.</p>
<dt><code>-p port</code></p>
<dd> Monitor only those frames received on a particular port, by default all AX.25 devices are monitored.</p>
<dt><code>-r</code></p>
<dd> Dump the data portion in a &quot;readable&quot; fashion, which is more suitable for tracing plaintext AX.25 traffic. CR-LF conversion is done.</p>
<dt><code>-t</code></p>
<dd> Displays a timestamp with each packet received.</p>
<dt><code>-v</code></p>
<dd> Display the version.</dl>
<h2>FILES</h2>
<p> /etc/ax25/axports</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-axcall/">axcall</a></code>(1), <code><a href="/docs/linux/man/1-mheard/">mheard</a></code>(1), <code><a href="/docs/linux/man/1-beacon/">beacon</a></code>(1), <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <code><a href="/docs/linux/man/4-rose/">rose</a></code>(4), <code><a href="/docs/linux/man/8-kissattach/">kissattach</a></code>(8). </p>
<h2>BUGS</h2>
<p> <code>Axlisten</code> does not validate the checksums of frames that support them (ie IP), therefore corrupt frames will be displayed with bogus values. The MSS of a TCP frame that contains that option is not displayed.</p>
<h2>AUTHORS</h2>
<pre><code>
Alan Cox GW4PTS&lt;alan[at] cymru.net&gt;

    Jonathan Naylor G4KLX&lt;g4klx[at] g4klx.demon.co.uk&gt;

        Phil Karn KA9Q&lt;karn[at] qualcomm.com&gt;

            Heikki Hannikainen OH7LZB&lt;hessu[at] pspt.fi&gt;
</code></pre>
<h2>Index</h2>
