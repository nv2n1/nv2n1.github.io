---
title: "tc-netem(8)"
name: "tc-netem"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-netem/"
description: "NetEm – Network Emulator"
---

<p>NetEm &#8211; Network Emulator</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; dev</code> <i>DEVICE</i> ] <code>add netem</code> <i>OPTIONS</i> <i>OPTIONS</i> := [ <i>LIMIT</i> ] [ <i>DELAY</i> ] [ <i>LOSS</i> ] [ <i>CORRUPT</i> ] [ <i>DUPLICATION</i> ] [ <i>REORDERING</i> ] [ <i>RATE</i> ] [ <i>SLOT</i> ] <i>LIMIT</i> := <code>limit</code> <i>packets</i> <i>DELAY</i> := <code>delay</code> <i>TIME</i> [ <i>JITTER</i> [ <i>CORRELATION</i> ]]] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[ <code>distribution</code> { uniform<code> | </code>normal<code> | </code>pareto<code> | </code>paretonormal<code> } ]</code> <i>LOSS</i> := <code>loss</code> { <code>random</code> <i>PERCENT</i> [ <i>CORRELATION</i> ] |<br />
 <code>state</code> <i>p13</i> [ <i>p31</i> [ <i>p32</i> [ <i>p23</i> [ <i>p14</i>]]]] |<br />
 <code>gemodel</code> <i>p</i> [ <i>r</i> [ <i>1-h</i> [ <i>1-k</i> ]]] } [ <code>ecn</code> ] <i>CORRUPT</i> := <code>corrupt</code> <i>PERCENT</i> [ <i>CORRELATION</i> ]] <i>DUPLICATION</i> := <code>duplicate</code> <i>PERCENT</i> [ <i>CORRELATION</i> ]] <i>REORDERING</i> := <code>reorder</code> <i>PERCENT</i> [ <i>CORRELATION</i> ] [ <code>gap</code> <i>DISTANCE</i> ] <i>RATE</i> := <code>rate</code> <i>RATE</i> [ <i>PACKETOVERHEAD</i> [ <i>CELLSIZE</i> [ <i>CELLOVERHEAD</i> ]]]] <i>SLOT</i> := <code>slot</code> { <i>MIN_DELAY</i> [ <i>MAX_DELAY</i> ] |<br />
 <code>distribution</code> { uniform<code> | </code>normal<code> | </code>pareto<code> | </code>paretonormal<code> | </code> <i>FILE</i> } <i>DELAY</i> <i>JITTER</i> }<br />
 [ <code>packets</code> <i>PACKETS</i> ] [ <code>bytes</code> <i>BYTES</i> ] </p>
<h2>Description</h2>
<p>NetEm is an enhancement of the Linux traffic control facilities that allow to add delay, packet loss, duplication and more other characteristics to packets outgoing from a selected network interface. NetEm is built using the existing Quality Of Service (QOS) and Differentiated Services (diffserv) facilities in the Linux kernel. </p>
<h2>netem OPTIONS</h2>
<p>netem has the following options:</p>
<h3>limit packets</h3>
<p>maximum number of packets the qdisc may hold queued at a time.</p>
<h3>delay</h3>
<p>adds the chosen delay to the packets outgoing to chosen network interface. The optional parameters allows to introduce a delay variation and a correlation. Delay and jitter values are expressed in ms while correlation is percentage.</p>
<h3>distribution</h3>
<p>allow the user to choose the delay distribution. If not specified, the default distribution is Normal. Additional parameters allow to consider situations in which network has variable delays depending on traffic flows concurring on the same path, that causes several delay peaks and a tail.</p>
<h3>loss random</h3>
<p>adds an independent loss probability to the packets outgoing from the chosen network interface. It is also possible to add a correlation, but this option is now deprecated due to the noticed bad behavior.</p>
<h3>loss state</h3>
<p>adds packet losses according to the 4-state Markov using the transition probabilities as input parameters. The parameter p13 is mandatory and if used alone corresponds to the Bernoulli model. The optional parameters allows to extend the model to 2-state (p31), 3-state (p23 and p32) and 4-state (p14). State 1 corresponds to good reception, State 4 to independent losses, State 3 to burst losses and State 2 to good reception within a burst.</p>
<h3>loss gemodel</h3>
<p>adds packet losses according to the Gilbert-Elliot loss model or its special cases (Gilbert, Simple Gilbert and Bernoulli). To use the Bernoulli model, the only needed parameter is p while the others will be set to the default values r=1-p, 1-h=1 and 1-k=0. The parameters needed for the Simple Gilbert model are two (p and r), while three parameters (p, r, 1-h) are needed for the Gilbert model and four (p, r, 1-h and 1-k) are needed for the Gilbert-Elliot model. As known, p and r are the transition probabilities between the bad and the good states, 1-h is the loss probability in the bad state and 1-k is the loss probability in the good state.</p>
<h3>ecn</h3>
<p>can be used optionally to mark packets instead of dropping them. A loss model has to be used for this to be enabled.</p>
<h3>corrupt</h3>
<p>allows the emulation of random noise introducing an error in a random position for a chosen percent of packets. It is also possible to add a correlation through the proper parameter.</p>
<h3>duplicate</h3>
<p>using this option the chosen percent of packets is duplicated before queuing them. It is also possible to add a correlation through the proper parameter.</p>
<h3>reorder</h3>
<p>to use reordering, a delay option must be specified. There are two ways to use this option (assuming &#8216;delay 10ms&#8217; in the options list). </p>
<p> <code>reorder </code> <i>25% 50%</i> <code>gap</code> <i>5</i><br />
 in this first example, the first 4 (gap &#8211; 1) packets are delayed by 10ms and subsequent packets are sent immediately with a probability of 0.25 (with correlation of 50% ) or delayed with a probability of 0.75. After a packet is reordered, the process restarts i.e. the next 4 packets are delayed and subsequent packets are sent immediately or delayed based on reordering probability. To cause a repeatable pattern where every 5th packet is reordered reliably, a reorder probability of 100% can be used. </p>
<p> <code>reorder</code> <i>25% 50%</i><br />
 in this second example 25% of packets are sent immediately (with correlation of 50%) while the others are delayed by 10 ms.</p>
<h3>rate</h3>
<p>delay packets based on packet size and is a replacement for <i>TBF</i>. Rate can be specified in common units (e.g. 100kbit). Optional <i>PACKETOVERHEAD</i> (in bytes) specify an per packet overhead and can be negative. A positive value can be used to simulate additional link layer headers. A negative value can be used to artificial strip the Ethernet header (e.g. -14) and/or simulate a link layer header compression scheme. The third parameter &#8211; an unsigned value &#8211; specify the cellsize. Cellsize can be used to simulate link layer schemes. ATM for example has an payload cellsize of 48 bytes and 5 byte per cell header. If a packet is 50 byte then ATM must use two cells: 2 * 48 bytes payload including 2 * 5 byte header, thus consume 106 byte on the wire. The last optional value <i>CELLOVERHEAD</i> can be used to specify per cell overhead &#8211; for our ATM example 5. <i>CELLOVERHEAD</i> can be negative, but use negative values with caution. </p>
<p> Note that rate throttling is limited by several factors: the kernel clock granularity avoid a perfect shaping at a specific level. This will show up in an artificial packet compression (bursts). Another influence factor are network adapter buffers which can also add artificial delay.</p>
<h3>slot</h3>
<p>defer delivering accumulated packets to within a slot. Each available slot can be configured with a minimum delay to acquire, and an optional maximum delay. Alternatively it can be configured with the distribution similar to <code>distribution</code> for <code>delay</code> option. Slot delays can be specified in nanoseconds, microseconds, milliseconds or seconds (e.g. 800us). Values for the optional parameters <i>BYTES</i> will limit the number of bytes delivered per slot, and/or <i>PACKETS</i> will limit the number of packets delivered per slot. </p>
<p> These slot options can provide a crude approximation of bursty MACs such as DOCSIS, WiFi, and LTE. </p>
<p> Note that slotting is limited by several factors: the kernel clock granularity, as with a rate, and attempts to deliver many packets within a slot will be smeared by the timer resolution, and by the underlying native bandwidth also. </p>
<p> It is possible to combine slotting with a rate, in which case complex behaviors where either the rate, or the slot limits on bytes or packets per slot, govern the actual delivered rate.</p>
<h2>Limitations</h2>
<p>The main known limitation of Netem are related to timer granularity, since Linux is not a real-time operating system.</p>
<h2>Examples</h2>
<p>tc qdisc add dev eth0 root netem rate 5kbit 20 100 5</p>
<dl>
<dd>delay all outgoing packets on device eth0 with a rate of 5kbit, a per packet overhead of 20 byte, a cellsize of 100 byte and a per celloverhead of 5 byte:</dl>
<h2>Sources</h2>
<dl>
<dt> 1.</p>
<dd>Hemminger S. , &quot;Network Emulation with NetEm&quot;, Open Source Development Lab, April 2005 (<a rel="nofollow" href="http://devresources.linux-foundation.org/shemminger/netem/LCA2005_paper.pdf)">http://devresources.linux-foundation.org/shemminger/netem/LCA2005_paper.pdf)</a> </p>
<dt> 2.</p>
<dd>Netem page from Linux foundation, (<a rel="nofollow" href="https://wiki.linuxfoundation.org/networking/netem)">https://wiki.linuxfoundation.org/networking/netem)</a> </p>
<dt> 3.</p>
<dd>Salsano S., Ludovici F., Ordine A., &quot;Definition of a general and intuitive loss model for packet networks and its implementation in the Netem module in the Linux kernel&quot;, available at <a rel="nofollow" href="http://netgroup.uniroma2.it/NetemCLG">http://netgroup.uniroma2.it/NetemCLG</a> </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-tbf/">tc-tbf</a></code>(8) </p>
<h2>Author</h2>
<p>Netem was written by Stephen Hemminger at Linux foundation and is based on NISTnet. This manpage was created by Fabio Ludovici &lt;fabio.ludovici at yahoo dot it&gt; and Hagen Paul Pfeifer &lt;hagen [at] jauu.net&gt;</p>
