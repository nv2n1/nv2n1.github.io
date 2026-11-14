---
title: "randpkt(1)"
name: "randpkt"
section: "1"
letter: "r"
url: "/docs/linux/man/1-randpkt/"
description: "randpkt – Random Packet Generator"
---

<h2 class="name">NAME</h2>
<p> randpkt &#8211; Random Packet Generator </p>
<h2>SYNOPSIS</h2>
<p> <code>randpkt</code> [&nbsp;<wbr><code>-b</code>&nbsp;<wbr>&lt;maxbytes&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-c</code>&nbsp;<wbr>&lt;count&gt;&nbsp;<wbr>] [&nbsp;<wbr><code>-t</code>&nbsp;<wbr>&lt;type&gt;&nbsp;<wbr>] &lt;filename&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>randpkt</code> is a small utility that creates a <code>pcap</code> trace file full of random packets. </p>
<p> By creating many randomized packets of a certain type, you can test packet sniffers to see how well they handle malformed packets. The sniffer can never trust the data that it sees in the packet because you can always sniff a very bad packet that conforms to no standard. <code>randpkt</code> produces <i>very bad</i> packets. </p>
<p> When creating packets of a certain type, <code>randpkt</code> uses a sample packet that is stored internally to <code>randpkt</code>. It uses this as the starting point for your random packets, and then adds extra random bytes to the end of this sample packet. </p>
<p> For example, if you choose to create random <font SIZE="-1">ARP</font> packets, <code>randpkt</code> will create a packet which contains a predetermined Ethernet <font SIZE="-1">II</font> header, with the Type field set to <font SIZE="-1">ARP.</font> After the Ethernet <font SIZE="-1">II</font> header, it will put a random number of bytes with random values.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-b &lt;maxbytes&gt;</p>
<dd> Default 5000. </p>
<p> Defines the maximum number of bytes added to the sample packet. If you choose a <code>maxbytes</code> value that is less than the size of the sample packet, then your packets would contain only the sample packet&#8230; not much variance there! <code>randpkt</code> exits on that condition.</p>
<dt>-c &lt;count&gt;</p>
<dd> Default 1000. </p>
<p> Defines the number of packets to generate.</p>
<dt>-t &lt;type&gt;</p>
<dd> Default Ethernet <font SIZE="-1">II</font> frame. </p>
<p> Defines the type of packet to generate: </p>
<pre>
        arp             Address Resolution Protocol
        bgp             Border Gateway Protocol
        bvlc            BACnet Virtual Link Control
        dns             Domain Name Service
        eth             Ethernet
        fddi            Fiber Distributed Data Interface
        giop            General Inter-ORB Protocol
        icmp            Internet Control Message Protocol
        ip              Internet Protocol
        llc             Logical Link Control
        m2m             WiMAX M2M Encapsulation Protocol
        megaco          MEGACO
        nbns            NetBIOS-over-TCP Name Service
        ncp2222         NetWare Core Protocol
        sctp            Stream Control Transmission Protocol
        syslog          Syslog message
        tds             TDS NetLib
        tcp             Transmission Control Protocol
        tr              Token-Ring
        udp             User Datagram Protocol
        usb             Universal Serial Bus
        usb-linux       Universal Serial Bus with Linux specific header
</pre>
</dl>
<h2>EXAMPLES</h2>
<p> To see a description of the randpkt options use: </p>
<pre>
    randpkt
</pre>
<p> To generate a capture file with 1000 <font SIZE="-1">DNS</font> packets use: </p>
<pre>
    randpkt -b 500 -t dns rand_dns.pcap
</pre>
<p> To generate a small capture file with just a single <font SIZE="-1">LLC</font> frame use: </p>
<pre>
    randpkt -b 100 -c 1 -t llc single_llc.pcap
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-pcap/">pcap</a></i>(3), <i><a href="/docs/linux/man/1-editcap/">editcap</a></i>(1) </p>
<h2>Index</h2>
