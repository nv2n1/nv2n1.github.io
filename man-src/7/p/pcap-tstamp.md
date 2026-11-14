---
title: "pcap-tstamp(7)"
name: "pcap-tstamp"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pcap-tstamp/"
description: "pcap-tstamp – packet time stamps in libpcap"
---

<p>pcap-tstamp &#8211; packet time stamps in libpcap</p>
<h2>Description</h2>
<p>When capturing traffic, each packet is given a time stamp representing, for incoming packets, the arrival time of the packet and, for outgoing packets, the transmission time of the packet. This time is an approximation of the arrival or transmission time. If it is supplied by the operating system running on the host on which the capture is being done, there are several reasons why it might not precisely represent the arrival or transmission time:</p>
<dl>
<dd>if the time stamp is applied to the packet when the networking stack receives the packet, the networking stack might not see the packet until an interrupt is delivered for the packet or a timer event causes the networking device driver to poll for packets, and the time stamp might not be applied until the packet has had some processing done by other code in the networking stack, so there might be a significant delay between the time when the last bit of the packet is received by the capture device and when the networking stack time-stamps the packet;</p>
<dd>the timer used to generate the time stamps might have low resolution, for example, it might be a timer updated once per host operating system timer tick, with the host operating system timer ticking once every few milliseconds;</p>
<dd>a high-resolution timer might use a counter that runs at a rate dependent on the processor clock speed, and that clock speed might be adjusted upwards or downwards over time and the timer might not be able to compensate for all those adjustments;</p>
<dd>the host operating system&#8217;s clock might be adjusted over time to match a time standard to which the host is being synchronized, which might be done by temporarily slowing down or speeding up the clock or by making a single adjustment;</p>
<dd>different CPU cores on a multi-core or multi-processor system might be running at different speeds, or might not have time counters all synchronized, so packets time-stamped by different cores might not have consistent time stamps.</dl>
<p> In addition, packets time-stamped by different cores might be time-stamped in one order and added to the queue of packets for libpcap to read in another order, so time stamps might not be monotonically increasing. </p>
<p> Some capture devices on some platforms can provide time stamps for packets; those time stamps are usually high-resolution time stamps, and are usually applied to the packet when the first or last bit of the packet arrives, and are thus more accurate than time stamps provided by the host operating system. Those time stamps might not, however, be synchronized with the host operating system&#8217;s clock, so that, for example, the time stamp of a packet might not correspond to the time stamp of an event on the host triggered by the arrival of that packet. </p>
<p> Depending on the capture device and the software on the host, libpcap might allow different types of time stamp to be used. The <code><a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap_list_tstamp_types/">pcap_list_tstamp_types</a></code>(3PCAP) routine provides, for a packet capture handle created by <code><a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap_create/">pcap_create</a></code>(3PCAP) but not yet activated by <code><a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap_activate/">pcap_activate</a></code>(3PCAP), a list of time stamp types supported by the capture device for that handle. The list might be empty, in which case no choice of time stamp type is offered for that capture device. If the list is not empty, the <code><a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap_set_tstamp_type/">pcap_set_tstamp_type</a></code>(3PCAP) routine can be used after a <code>pcap_create()</code> call and before a <code>pcap_activate()</code> call to specify the type of time stamp to be used on the device. The time stamp types are listed here; the first value is the #define to use in code, the second value is the value returned by <code>pcap_tstamp_type_val_to_name()</code> and accepted by <code>pcap_tstamp_name_to_val()</code>.</p>
<dl>
<dd>
<dl>
<dt><code>PCAP_TSTAMP_HOST</code> &#8211; <code>host</code></p>
<dd>Time stamp provided by the host on which the capture is being done. The precision of this time stamp is unspecified; it might or might not be synchronized with the host operating system&#8217;s clock.</p>
<dt><code>PCAP_TSTAMP_HOST_LOWPREC</code> &#8211; <code>host_lowprec</code></p>
<dd>Time stamp provided by the host on which the capture is being done. This is a low-precision time stamp, synchronized with the host operating system&#8217;s clock.</p>
<dt><code>PCAP_TSTAMP_HOST_HIPREC</code> &#8211; <code>host_hiprec</code></p>
<dd>Time stamp provided by the host on which the capture is being done. This is a high-precision time stamp; it might or might not be synchronized with the host operating system&#8217;s clock. It might be more expensive to fetch than <code>PCAP_TSTAMP_HOST_LOWPREC</code>.</p>
<dt><code>PCAP_TSTAMP_ADAPTER</code> &#8211; <code>adapter</code></p>
<dd>Time stamp provided by the network adapter on which the capture is being done. This is a high-precision time stamp, synchronized with the host operating system&#8217;s clock.</p>
<dt><code>PCAP_TSTAMP_ADAPTER_UNSYNCED</code> &#8211; <code>adapter_unsynced</code></p>
<dd>Time stamp provided by the network adapter on which the capture is being done. This is a high-precision time stamp; it is not synchronized with the host operating system&#8217;s clock.</dl>
</dl>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap_set_tstamp_type/">pcap_set_tstamp_type</a>(3PCAP), <a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap_list_tstamp_types/">pcap_list_tstamp_types</a>(3PCAP), <a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap_tstamp_type_val_to_name/">pcap_tstamp_type_val_to_name</a>(3PCAP), <a href="//www.systutorials.com/docs/linux/man/3PCAP-pcap_tstamp_name_to_val/">pcap_tstamp_name_to_val</a>(3PCAP) </p>
