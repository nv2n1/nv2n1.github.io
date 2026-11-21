---

title: "opapacketcapture(1)"
name: "opapacketcapture"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opapacketcapture/"
description: "opapacketcapture"
---

<p> opapacketcapture </p>
<p> Starts capturing packet data. </p>
<p> To stop capture and trigger dump, use SIGINT or SIGUSR1. Program dumps packets to file and exits. </p>
<p> <code>NOTE:</code> Using opapacketcapture with large amounts of traffic can cause performance issues on the given host. Intel recommends you use opapacketcapture on hosts with lower packet rates and bandwidth. </p>
<h2>Syntax</h2>
<p> opapacketcapture [-o <i>outfile</i>] [-d <i>devfile</i>] [-f <i>filterfile</i>] [-t <i>triggerfile</i>] [-l <i>triggerlag</i>][-a <i>alarm</i>] [-p <i>packets</i>] [-s <i>maxblocks</i>] [-v] [-h]</p>
<h2>Options</h2>
<dl>
<dt>-h/&#8211;help</dt>
<dd> Produces full help text. </dd>
<dt>-o <i>outfile</i></dt>
<dd> Output file for captured packets. Default = packetDump.pcap </dd>
<dt>-d <i>devfile</i></dt>
<dd> Device file for capturing packets. Default = /dev/hfi1_diagpkt0 </dd>
<dt>-f <i>filterfile</i></dt>
<dd> File used for filtering. If absent, no filtering is done. </dd>
<dt>-t <i>triggerfile</i></dt>
<dd> File used for triggering a stop capture. If absent, normal triggering is performed. </dd>
<dt>-l <i>triggerlag</i></dt>
<dd> Number of packets to collect after trigger condition is met, before dumping data and exiting. Default = 10. </dd>
<dt>-a <i>alarm</i></dt>
<dd> Number of seconds for alarm trigger to dump capture and exit. </dd>
<dt>-p <i>packets</i></dt>
<dd> Number of packets for alarm trigger to dump capture and exit. </dd>
<dt>-s <i>maxblocks</i></dt>
<dd> Number of blocks to allocate for ring buffer. Value is in Millions. Default = 2 which corresponds to 128 MiB because 1 block = 64 Bytes. </dd>
<dt>-v</dt>
<dd> Produces verbose output. </dd>
</dl>
<h2>Example</h2>
<p> # opapacketcapture<br />
 opapacketcapture: Capturing packets using 128 MiB buffer<br />
 ^C<br />
 opapacketcapture: Triggered<br />
 Number of packets stored is 100 </p>
<p> In the example above, opapacketcapture operates until <code>CTRL+C</code> is entered. </p>
