---
title: "hcidump(8)"
name: "hcidump"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hcidump/"
description: "hcidump – Parse HCI data"
---

<p>hcidump &#8211; Parse HCI data</p>
<h2>Synopsis</h2>
<p><code>hcidump [-h]</code><br />
 <code>hcidump [option [option&#8230;]] [filter]</code> </p>
<h2>Description</h2>
<p><code>hcidump</code> reads raw HCI data coming from and going to a Bluetooth device (which can be specified with the option <code>-i</code>, default is the first available one) and prints to screen commands, events and data in a human-readable form. Optionally, the dump can be written to a file rather than parsed, and the dump file can be parsed in a subsequent moment.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Prints usage info and exits</p>
<dt><code>-i</code><i> &lt;hciX&gt;</i></p>
<dd>Data is read from <i>hciX</i>, which must be the name of an installed Bluetooth device. If not specified, and if <code>-r</code> option is not set, data is read from the first available Bluetooth device.</p>
<dt><code>-l</code><i> &lt;len&gt;</i>, &#8211;snap-len=<i>&lt;len&gt;</i></p>
<dd>Sets max length of processed packets to <i>len</i>.</p>
<dt><code>-p</code><i> &lt;psm&gt;</i>, &#8211;psm=<i>&lt;psm&gt;</i></p>
<dd>Sets default Protocol Service Multiplexer to <i>psm</i>.</p>
<dt><code>-m</code><i> &lt;compid&gt;</i>, &#8211;manufacturer=<i>&lt;compid&gt;</i></p>
<dd>Sets default company id for manufacturer to <i>compid</i>.</p>
<dt><code>-w</code><i> &lt;file&gt;</i>, &#8211;save-dump=<i>&lt;file&gt;</i></p>
<dd>Parse output is not printed to screen, instead data read from device is saved in file <i>file</i>. The saved dump file can be subsequently parsed with option <code>-r</code>.</p>
<dt><code>-r</code><i> &lt;file&gt;</i>, &#8211;read-dump=<i>&lt;file&gt;</i></p>
<dd>Data is not read from a Bluetooth device, but from file <i>file</i>. <i>file</i> is created with option <code>-w</code>.</p>
<dt><code>-s</code><i> &lt;host&gt;</i>, &#8211;send-dump=<i>&lt;host&gt;</i></p>
<dd>Parse output is not printed to screen, instead data read from device is sent to host <i>host</i>.</p>
<dt><code>-n</code><i> &lt;host&gt;</i>, &#8211;recv-dump=<i>&lt;host&gt;</i></p>
<dd>Data is not read from a Bluetooth device, but from host <i>host</i>.</p>
<dt><code>-d</code><i> &lt;host&gt;</i>, &#8211;wait-dump=<i>&lt;host&gt;</i></p>
<dd>Data is read from a Bluetooth device, but then send to <i>host</i> for processing. No data is read if no host is connected.</p>
<dt><code>-t</code>, <code>&#8211;timestamp</code></p>
<dd>Prepend a time stamp to every packet.</p>
<dt><code>-a</code>, <code>&#8211;ascii</code></p>
<dd>For every packet, not only is the packet type displayed, but also all data in ASCII.</p>
<dt><code>-x</code>, <code>&#8211;hex</code></p>
<dd>For every packet, not only is the packet type displayed, but also all data in hex.</p>
<dt><code>-X</code>, <code>&#8211;ext</code></p>
<dd>For every packet, not only is the packet type displayed, but also all data in hex and ASCII.</p>
<dt><code>-R</code>, <code>&#8211;raw</code></p>
<dd>For every packet, only the raw data is displayed.</p>
<dt><code>-C</code>, <code>&#8211;cmtp=</code>&lt;psm&gt;</p>
<dd>Sets the PSM value for the CAPI Message Transport Protocol.</p>
<dt><code>-H</code>, <code>&#8211;hcrp=</code>&lt;psm&gt;</p>
<dd>Sets the PSM value for the Hardcopy Control Channel.</p>
<dt><code>-O</code>, <code>&#8211;obex=</code>&lt;channel&gt;</p>
<dd>Sets the RFCOMM channel value for the Object Exchange Protocol.</p>
<dt><code>-P</code>, <code>&#8211;ppp=</code>&lt;channel&gt;</p>
<dd>Sets the RFCOMM channel value for the Point-to-Point Protocol.</p>
<dt><code>-D</code>, <code>&#8211;pppdump=</code>&lt;file&gt;</p>
<dd>Extract PPP traffic with pppdump format.</p>
<dt><code>-A</code>, <code>&#8211;audio=</code>&lt;file&gt;</p>
<dd>Extract SCO audio data.</p>
<dt><code>-B</code>, <code>&#8211;btsnoop</code></p>
<dd>Use the BTSnoop file format.</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Enables a more verbose decoding of every packet.</p>
<dt><code>-Y</code>, <code>&#8211;novendor</code></p>
<dd>Don&#8217;t display any vendor commands or events and don&#8217;t show any pin code or link key in plain text.</p>
<dt><code>-N</code>, <code>&#8211;noappend</code></p>
<dd>No appending to existing files. Always create new files.</p>
<dt><code>-4</code>, <code>&#8211;ipv4</code></p>
<dd>Use IPv4 when sending information over the network</p>
<dt><code>-6</code>, <code>&#8211;ipv6</code></p>
<dd>Use IPv6 when sending information over the network</dl>
<h2>Filters</h2>
<p><code>filter</code> is a space-separated list of packet categories: available categories are <i>lmp</i>, <i>hci</i>, <i>sco</i>, <i>l2cap</i>, <i>rfcomm</i>, <i>sdp</i>, <i>bnep</i>, <i>cmtp</i>, <i>hidp</i>, <i>hcrp</i>, <i>avdtp</i>, <i>avctp</i>, <i>obex</i>, <i>capi</i> and <i>ppp</i>. If filters are used, only packets belonging to the specified categories are dumped. By default, all packets are dumped.</p>
<h2>Authors</h2>
<p>Written by Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt; and Marcel Holtmann &lt;marcel [at] holtmann.org&gt; </p>
<p> man page by Fabrizio Gennari &lt;fabrizio.gennari [at] philips.com&gt;</p>
