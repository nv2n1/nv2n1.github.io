---
title: "wavelan(4)"
name: "wavelan"
section: "4"
letter: "w"
url: "/docs/linux/man/4-wavelan/"
description: "wavelan – AT&T GIS WaveLAN ISA device driver"
---

<p>wavelan &#8211; AT&amp;T GIS WaveLAN ISA device driver</p>
<h2>Synopsis</h2>
<p><code>insmod wavelan_cs.o [io=</code><i>B,B..</i><code>] [ irq=</code><i>I,I..</i><code>] [name=</code><i>N,N..</i><code>]</code></p>
<h2>Description</h2>
<p><i>This driver is obsolete:</i> it was removed from the kernel in version 2.6.35. </p>
<p> <code>wavelan</code> is the low-level device driver for the NCR / AT&amp;T / Lucent <code>WaveLAN ISA</code> and Digital (DEC) <code>RoamAbout DS</code> wireless ethernet adapter. This driver is available as a module or might be compiled in the kernel. This driver supports multiple cards in both forms (up to 4) and allocates the next available ethernet device (eth0..eth#) for each card found, unless a device name is explicitly specified (see below). This device name will be reported in the kernel log file with the MAC address, NWID and frequency used by the card.</p>
<h3>Parameters</h3>
<p>This section applies to the module form (parameters passed on the <code><a href="/docs/linux/man/8-insmod/">insmod</a></code>(8) command line). If the driver is included in the kernel, use the <i>ether=IRQ,IO,NAME</i> syntax on the kernel command line.</p>
<dl>
<dt><code>io</code></p>
<dd>Specify the list of base addresses where to search for wavelan cards (setting by dip switch on the card). If you don&#8217;t specify any io address, the driver will scan 0x390 and 0x3E0 addresses, which might conflict with other hardware&#8230;</p>
<dt><code>irq</code></p>
<dd>Set the list of IRQs that each wavelan card should use (the value is saved in permanent storage for future use).</p>
<dt><code>name</code></p>
<dd>Set the list of names to be used for each wavelan card device (name used by <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8)).</dl>
<h3>Wireless extensions</h3>
<p>Use <code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8) to manipulate wireless extensions.</p>
<h3>NWID (or domain)</h3>
<p>Set the network ID [<i>0</i> to <i>FFFF</i>] or disable it [<i>off</i>]. As the NWID is stored in the card Permanent Storage Area, it will be reused at any further invocation of the driver.</p>
<h3>Frequency &amp; channels</h3>
<p>For the 2.4 GHz 2.00 Hardware, you are able to set the frequency by specifying one of the 10 defined channels (<i>2.412,</i> <i>2.422, 2.425, 2.4305, 2.432, 2.442, 2.452, 2.460, 2.462</i> or <i>2.484</i>) or directly as a numeric value. The frequency is changed immediately and permanently. Frequency availability depends on the regulations&#8230;</p>
<h3>Statistics spy</h3>
<p>Set a list of MAC addresses in the driver (up to 8) and get the last quality of link for each of those (see <code><a href="/docs/linux/man/8-iwspy/">iwspy</a></code>(8)).</p>
<h3>/proc/net/wireless</h3>
<p><i>status</i> is the status reported by the modem. <i>Link quality</i> reports the quality of the modulation on the air (direct sequence spread spectrum) [max = 16]. <i>Level</i> and <i>Noise</i> refer to the signal level and noise level [max = 64]. The <i>crypt discarded packet</i> and <i>misc discarded packet</i> counters are not implemented.</p>
<h3>Private ioctl</h3>
<p>You may use <code><a href="/docs/linux/man/8-iwpriv/">iwpriv</a></code>(8) to manipulate private ioctls.</p>
<h3>Quality and level threshold</h3>
<p>Enables you to define the quality and level threshold used by the modem (packet below that level are discarded).</p>
<h3>Histogram</h3>
<p>This functionality makes it possible to set a number of signal level intervals and to count the number of packets received in each of those defined intervals. This distribution might be used to calculate the mean value and standard deviation of the signal level.</p>
<h3>Specific notes</h3>
<p>This driver fails to detect some <code>non-NCR/AT&amp;T/Lucent</code> Wavelan cards. If this happens for you, you must look in the source code on how to add your card to the detection routine. </p>
<p> Some of the mentioned features are optional. You may enable to disable them by changing flags in the driver header and recompile.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-wavelan_cs/">wavelan_cs</a></code>(4), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/8-insmod/">insmod</a></code>(8), <code><a href="/docs/linux/man/8-iwconfig/">iwconfig</a></code>(8), <code><a href="/docs/linux/man/8-iwpriv/">iwpriv</a></code>(8), <code><a href="/docs/linux/man/8-iwspy/">iwspy</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
