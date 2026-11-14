---
title: "tc-cbq-details(8)"
name: "tc-cbq-details"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-cbq-details/"
description: "CBQ – Class Based Queueing"
---

<p>CBQ &#8211; Class Based Queueing</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; dev</code> dev <code>( parent</code> classid <code>| root) [ handle</code> major: <code>] cbq avpkt</code> bytes <code>bandwidth</code> rate <code>[ cell</code> bytes <code>] [ ewma</code> log <code>] [ mpu</code> bytes <code>]</code> <code>tc class &#8230; dev</code> dev <code>parent</code> major:[minor] <code>[ classid</code> major:minor <code>] cbq allot</code> bytes <code>[ bandwidth</code> rate <code>] [ rate</code> rate <code>] prio</code> priority <code>[ weight</code> weight <code>] [ minburst</code> packets <code>] [ maxburst</code> packets <code>] [ ewma</code> log <code>] [ cell</code> bytes <code>] avpkt</code> bytes <code>[ mpu</code> bytes <code>] [ bounded isolated ] [ split</code> handle <code>&amp; defmap</code> defmap <code>] [ estimator</code> interval timeconstant <code>]</code> </p>
<h2>Description</h2>
<p>Class Based Queueing is a classful qdisc that implements a rich linksharing hierarchy of classes. It contains shaping elements as well as prioritizing capabilities. Shaping is performed using link idle time calculations based on the timing of dequeue events and underlying link bandwidth. </p>
<h2>Shaping Algorithm</h2>
<p>Shaping is done using link idle time calculations, and actions taken if these calculations deviate from set limits. </p>
<p> When shaping a 10mbit/s connection to 1mbit/s, the link will be idle 90% of the time. If it isn&#8217;t, it needs to be throttled so that it IS idle 90% of the time. </p>
<p> From the kernel&#8217;s perspective, this is hard to measure, so CBQ instead derives the idle time from the number of microseconds (in fact, jiffies) that elapse between requests from the device driver for more data. Combined with the knowledge of packet sizes, this is used to approximate how full or empty the link is. </p>
<p> This is rather circumspect and doesn&#8217;t always arrive at proper results. For example, what is the actual link speed of an interface that is not really able to transmit the full 100mbit/s of data, perhaps because of a badly implemented driver? A PCMCIA network card will also never achieve 100mbit/s because of the way the bus is designed &#8211; again, how do we calculate the idle time? </p>
<p> The physical link bandwidth may be ill defined in case of not-quite-real network devices like PPP over Ethernet or PPTP over TCP/IP. The effective bandwidth in that case is probably determined by the efficiency of pipes to userspace &#8211; which not defined. </p>
<p> During operations, the effective idletime is measured using an exponential weighted moving average (EWMA), which considers recent packets to be exponentially more important than past ones. The Unix loadaverage is calculated in the same way. </p>
<p> The calculated idle time is subtracted from the EWMA measured one, the resulting number is called &#8216;avgidle&#8217;. A perfectly loaded link has an avgidle of zero: packets arrive exactly at the calculated interval. </p>
<p> An overloaded link has a negative avgidle and if it gets too negative, CBQ throttles and is then &#8216;overlimit&#8217;. </p>
<p> Conversely, an idle link might amass a huge avgidle, which would then allow infinite bandwidths after a few hours of silence. To prevent this, avgidle is capped at <code>maxidle.</code> </p>
<p> If overlimit, in theory, the CBQ could throttle itself for exactly the amount of time that was calculated to pass between packets, and then pass one packet, and throttle again. Due to timer resolution constraints, this may not be feasible, see the <code>minburst</code> parameter below.</p>
<h2>Classification</h2>
<p>Within the one CBQ instance many classes may exist. Each of these classes contains another qdisc, by default <code><a href="/docs/linux/man/8-tc-pfifo/">tc-pfifo</a></code>(8). </p>
<p> When enqueueing a packet, CBQ starts at the root and uses various methods to determine which class should receive the data. If a verdict is reached, this process is repeated for the recipient class which might have further means of classifying traffic to its children, if any. </p>
<p> CBQ has the following methods available to classify a packet to any child classes.</p>
<dl>
<dt>(i)</p>
<dd><code>skb-&gt;priority class encoding.</code> Can be set from userspace by an application with the <code>SO_PRIORITY</code> setsockopt. The <code>skb-&gt;priority class encoding</code> only applies if the skb-&gt;priority holds a major:minor handle of an existing class within this qdisc.</p>
<dt>(ii)</p>
<dd>tc filters attached to the class.</p>
<dt>(iii)</p>
<dd>The defmap of a class, as set with the <code>split &amp; defmap</code> parameters. The defmap may contain instructions for each possible Linux packet priority. </p>
</dl>
<p> Each class also has a <code>level.</code> Leaf nodes, attached to the bottom of the class hierarchy, have a level of 0.</p>
<h2>Classification Algorithm</h2>
<p>Classification is a loop, which terminates when a leaf class is found. At any point the loop may jump to the fallback algorithm. </p>
<p> The loop consists of the following steps:</p>
<dl>
<dt>(i)</p>
<dd>If the packet is generated locally and has a valid classid encoded within its <code>skb-&gt;priority,</code> choose it and terminate. </p>
<dt>(ii)</p>
<dd>Consult the tc filters, if any, attached to this child. If these return a class which is not a leaf class, restart loop from the class returned. If it is a leaf, choose it and terminate.</p>
<dt>(iii)</p>
<dd>If the tc filters did not return a class, but did return a classid, try to find a class with that id within this qdisc. Check if the found class is of a lower <code>level</code> than the current class. If so, and the returned class is not a leaf node, restart the loop at the found class. If it is a leaf node, terminate. If we found an upward reference to a higher level, enter the fallback algorithm.</p>
<dt>(iv)</p>
<dd>If the tc filters did not return a class, nor a valid reference to one, consider the minor number of the reference to be the priority. Retrieve a class from the defmap of this class for the priority. If this did not contain a class, consult the defmap of this class for the <code>BEST_EFFORT</code> class. If this is an upward reference, or no <code>BEST_EFFORT</code> class was defined, enter the fallback algorithm. If a valid class was found, and it is not a leaf node, restart the loop at this class. If it is a leaf, choose it and terminate. If neither the priority distilled from the classid, nor the <code>BEST_EFFORT</code> priority yielded a class, enter the fallback algorithm.</dl>
<p> The fallback algorithm resides outside of the loop and is as follows.</p>
<dl>
<dt>(i)</p>
<dd>Consult the defmap of the class at which the jump to fallback occurred. If the defmap contains a class for the <code>priority</code> of the class (which is related to the TOS field), choose this class and terminate.</p>
<dt>(ii)</p>
<dd>Consult the map for a class for the <code>BEST_EFFORT</code> priority. If found, choose it, and terminate.</p>
<dt>(iii)</p>
<dd>Choose the class at which break out to the fallback algorithm occurred. Terminate.</dl>
<p> The packet is enqueued to the class which was chosen when either algorithm terminated. It is therefore possible for a packet to be enqueued *not* at a leaf node, but in the middle of the hierarchy.</p>
<h2>Link Sharing Algorithm</h2>
<p>When dequeuing for sending to the network device, CBQ decides which of its classes will be allowed to send. It does so with a Weighted Round Robin process in which each class with packets gets a chance to send in turn. The WRR process starts by asking the highest priority classes (lowest numerically &#8211; highest semantically) for packets, and will continue to do so until they have no more data to offer, in which case the process repeats for lower priorities. </p>
<p> <code>CERTAINTY ENDS HERE, ANK PLEASE HELP</code> </p>
<p> Each class is not allowed to send at length though &#8211; they can only dequeue a configurable amount of data during each round. </p>
<p> If a class is about to go overlimit, and it is not <code>bounded</code> it will try to borrow avgidle from siblings that are not <code>isolated.</code> This process is repeated from the bottom upwards. If a class is unable to borrow enough avgidle to send a packet, it is throttled and not asked for a packet for enough time for the avgidle to increase above zero. </p>
<p> <code>I REALLY NEED HELP FIGURING THIS OUT. REST OF DOCUMENT IS PRETTY CERTAIN</code> <code>AGAIN.</code></p>
<h2>Qdisc</h2>
<p>The root qdisc of a CBQ class tree has the following parameters: </p>
<dl>
<dt>parent major:minor | root</p>
<dd>This mandatory parameter determines the place of the CBQ instance, either at the <code>root</code> of an interface or within an existing class.</p>
<dt>handle major:</p>
<dd>Like all other qdiscs, the CBQ can be assigned a handle. Should consist only of a major number, followed by a colon. Optional.</p>
<dt>avpkt bytes</p>
<dd>For calculations, the average packet size must be known. It is silently capped at a minimum of 2/3 of the interface MTU. Mandatory.</p>
<dt>bandwidth rate</p>
<dd>To determine the idle time, CBQ must know the bandwidth of your underlying physical interface, or parent qdisc. This is a vital parameter, more about it later. Mandatory.</p>
<dt>cell</p>
<dd>The cell size determines he granularity of packet transmission time calculations. Has a sensible default.</p>
<dt>mpu</p>
<dd>A zero sized packet may still take time to transmit. This value is the lower cap for packet transmission time calculations &#8211; packets smaller than this value are still deemed to have this size. Defaults to zero.</p>
<dt>ewma log</p>
<dd>When CBQ needs to measure the average idle time, it does so using an Exponentially Weighted Moving Average which smooths out measurements into a moving average. The EWMA LOG determines how much smoothing occurs. Defaults to 5. Lower values imply greater sensitivity. Must be between 0 and 31.</dl>
<p> A CBQ qdisc does not shape out of its own accord. It only needs to know certain parameters about the underlying link. Actual shaping is done in classes.</p>
<h2>Classes</h2>
<p>Classes have a host of parameters to configure their operation. </p>
<dl>
<dt>parent major:minor</p>
<dd>Place of this class within the hierarchy. If attached directly to a qdisc and not to another class, minor can be omitted. Mandatory.</p>
<dt>classid major:minor</p>
<dd>Like qdiscs, classes can be named. The major number must be equal to the major number of the qdisc to which it belongs. Optional, but needed if this class is going to have children.</p>
<dt>weight weight</p>
<dd>When dequeuing to the interface, classes are tried for traffic in a round-robin fashion. Classes with a higher configured qdisc will generally have more traffic to offer during each round, so it makes sense to allow it to dequeue more traffic. All weights under a class are normalized, so only the ratios matter. Defaults to the configured rate, unless the priority of this class is maximal, in which case it is set to 1.</p>
<dt>allot bytes</p>
<dd>Allot specifies how many bytes a qdisc can dequeue during each round of the process. This parameter is weighted using the renormalized class weight described above. </p>
<dt>priority priority</p>
<dd>In the round-robin process, classes with the lowest priority field are tried for packets first. Mandatory. </p>
<dt>rate rate</p>
<dd>Maximum rate this class and all its children combined can send at. Mandatory. </p>
<dt>bandwidth rate</p>
<dd>This is different from the bandwidth specified when creating a CBQ disc. Only used to determine maxidle and offtime, which are only calculated when specifying maxburst or minburst. Mandatory if specifying maxburst or minburst. </p>
<dt>maxburst</p>
<dd>This number of packets is used to calculate maxidle so that when avgidle is at maxidle, this number of average packets can be burst before avgidle drops to 0. Set it higher to be more tolerant of bursts. You can&#8217;t set maxidle directly, only via this parameter. </p>
<dt>minburst</p>
<dd>As mentioned before, CBQ needs to throttle in case of overlimit. The ideal solution is to do so for exactly the calculated idle time, and pass 1 packet. However, Unix kernels generally have a hard time scheduling events shorter than 10ms, so it is better to throttle for a longer period, and then pass minburst packets in one go, and then sleep minburst times longer. </p>
<p> The time to wait is called the offtime. Higher values of minburst lead to more accurate shaping in the long term, but to bigger bursts at millisecond timescales. </p>
<dt>minidle</p>
<dd>If avgidle is below 0, we are overlimits and need to wait until avgidle will be big enough to send one packet. To prevent a sudden burst from shutting down the link for a prolonged period of time, avgidle is reset to minidle if it gets too low. </p>
<p> Minidle is specified in negative microseconds, so 10 means that avgidle is capped at -10us. </p>
<dt>bounded</p>
<dd>Signifies that this class will not borrow bandwidth from its siblings.</p>
<dt>isolated</p>
<dd>Means that this class will not borrow bandwidth to its siblings </p>
<dt>split major:minor &amp; defmap bitmap[/bitmap]</p>
<dd>If consulting filters attached to a class did not give a verdict, CBQ can also classify based on the packet&#8217;s priority. There are 16 priorities available, numbered from 0 to 15. </p>
<p> The defmap specifies which priorities this class wants to receive, specified as a bitmap. The Least Significant Bit corresponds to priority zero. The <code>split</code> parameter tells CBQ at which class the decision must be made, which should be a (grand)parent of the class you are adding. </p>
<p> As an example, &#8216;tc class add &#8230; classid 10:1 cbq .. split 10:0 defmap c0&#8217; configures class 10:0 to send packets with priorities 6 and 7 to 10:1. </p>
<p> The complimentary configuration would then be: &#8216;tc class add &#8230; classid 10:2 cbq &#8230; split 10:0 defmap 3f&#8217; Which would send all packets 0, 1, 2, 3, 4 and 5 to 10:1.</p>
<dt>estimator interval timeconstant</p>
<dd>CBQ can measure how much bandwidth each class is using, which tc filters can use to classify packets with. In order to determine the bandwidth it uses a very simple estimator that measures once every <code>interval</code> microseconds how much traffic has passed. This again is a EWMA, for which the time constant can be specified, also in microseconds. The <code>time constant</code> corresponds to the sluggishness of the measurement or, conversely, to the sensitivity of the average to short bursts. Higher values mean less sensitivity. </p>
</dl>
<h2>Sources</h2>
<dl>
<dt>o</p>
<dd>Sally Floyd and Van Jacobson, &quot;Link-sharing and Resource Management Models for Packet Networks&quot;, IEEE/ACM Transactions on Networking, Vol.3, No.4, 1995 </p>
<dt>o</p>
<dd>Sally Floyd, &quot;Notes on CBQ and Guarantee Service&quot;, 1995 </p>
<dt>o</p>
<dd>Sally Floyd, &quot;Notes on Class-Based Queueing: Setting Parameters&quot;, 1996 </p>
<dt>o</p>
<dd>Sally Floyd and Michael Speer, &quot;Experimental Results for Class-Based Queueing&quot;, 1998, not published. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) </p>
<h2>Author</h2>
<p>Alexey N. Kuznetsov, &lt;kuznet [at] ms2.inr.ac.ru&gt;. This manpage maintained by bert hubert &lt;ahu [at] ds9a.nl&gt;</p>
