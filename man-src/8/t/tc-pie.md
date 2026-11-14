---
title: "tc-pie(8)"
name: "tc-pie"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-pie/"
description: "PIE – Proportional Integral controller-Enhanced AQM algorithm"
---

<p>PIE &#8211; Proportional Integral controller-Enhanced AQM algorithm</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; pie</code> [ <code>limit</code> PACKETS ] [ <code>target</code> TIME ] [ <code>tupdate</code> TIME ] [ <code>alpha</code> int ] [ <code>beta</code> int ] [ <code>ecn</code> | <code>noecn</code> ] [ <code>bytemode</code> | <code>nobytemode</code> ] [ <code>dq_rate_estimator</code> | <code>no_dq_rate_estimator</code> ] </p>
<h2>Description</h2>
<p>Proportional Integral controller-Enhanced (PIE) is a control theoretic active queue management scheme. It is based on the proportional integral controller but aims to control delay. The main design goals are<br />
&nbsp;o Low latency control<br />
&nbsp;o High link utilization<br />
&nbsp;o Simple implementation<br />
&nbsp;o Guaranteed stability and fast responsiveness </p>
<h2>Algorithm</h2>
<p>PIE is designed to control delay effectively. First, an average dequeue rate is estimated based on the standing queue. The rate is used to calculate the current delay. Then, on a periodic basis, the delay is used to calculate the dropping probability. Finally, on arrival, a packet is dropped (or marked) based on this probability. </p>
<p> PIE makes adjustments to the probability based on the trend of the delay i.e. whether it is going up or down.The delay converges quickly to the target value specified. </p>
<p> alpha and beta are statically chosen parameters chosen to control the drop probability growth and are determined through control theoretic approaches. alpha determines how the deviation between the current and target latency changes probability. beta exerts additional adjustments depending on the latency trend. </p>
<p> The drop probability is used to mark packets in ecn mode. However, as in RED, beyond 10% packets are dropped based on this probability. The bytemode is used to drop packets proportional to the packet size. </p>
<p> Additional details can be found in the paper cited below.</p>
<h2>Parameters</h2>
<h3>limit</h3>
<p>limit on the queue size in packets. Incoming packets are dropped when this limit is reached. Default is 1000 packets.</p>
<h3>target</h3>
<p>is the expected queue delay. The default target delay is 15ms.</p>
<h3>tupdate</h3>
<p>is the frequency at which the system drop probability is calculated. The default is 15ms.</p>
<h3>alpha</h3>
<h3>beta</h3>
<p>alpha and beta are parameters chosen to control the drop probability. These should be in the range between 0 and 32.</p>
<h3>ecn | noecn</h3>
<p>is used to mark packets instead of dropping. <code>ecn</code> to turn on ecn mode, <code>noecn</code> to turn off ecn mode. By default, <code>ecn</code> is turned off.</p>
<h3>bytemode | nobytemode</h3>
<p>is used to scale drop probability proportional to packet size. <code>bytemode</code> to turn on bytemode, <code>nobytemode</code> to turn off bytemode. By default, <code>bytemode</code> is turned off.</p>
<h3>dq_rate_estimator | no_dq_rate_estimator</h3>
<p>is used to calculate delay using Little&#8217;s law. <code>dq_rate_estimator</code> to turn on dq_rate_estimator, <code>no_dq_rate_estimator</code> to turn off no_dq_rate_estimator. By default, <code>dq_rate_estimator</code> is turned off.</p>
<h2>Examples</h2>
<p>&nbsp;#&nbsp;tc qdisc add dev eth0 root pie<br />
&nbsp;#&nbsp;tc -s qdisc show<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;qdisc pie 8036: dev eth0 root refcnt 2 limit 1000p target 15.0ms tupdate 16.0ms alpha 2 beta 20<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sent 31216108 bytes 20800 pkt&nbsp;(dropped 80, overlimits 0 requeues 0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;backlog 16654b 11p requeues 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prob 0.006161 delay 15666us<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pkts_in 20811 overlimit 0 dropped 80 maxq 50 ecn_mark 0<br />
&nbsp;#&nbsp;tc qdisc add dev eth0 root pie dq_rate_estimator<br />
&nbsp;#&nbsp;tc -s qdisc show<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;qdisc pie 8036: dev eth0 root refcnt 2 limit 1000p target 15.0ms tupdate 16.0ms alpha 2 beta 20<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sent 63947420 bytes 42414 pkt&nbsp;(dropped 41, overlimits 0 requeues 0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;backlog 271006b 179p requeues 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prob 0.000092 delay 22200us avg_dq_rate 12145996<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pkts_in 41 overlimit 343 dropped 0 maxq 50 ecn_mark 0<br />
&nbsp;#&nbsp;tc qdisc add dev eth0 root pie limit 100 target 20ms tupdate 30ms ecn<br />
&nbsp;#&nbsp;tc -s qdisc show<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;qdisc pie 8036: dev eth0 root refcnt 2 limit 100p target 20.0ms tupdate 32.0ms alpha 2 beta 20 ecn<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sent 6591724 bytes 4442 pkt&nbsp;(dropped 27, overlimits 0 requeues 0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;backlog 18168b 12p requeues 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prob 0.008845 delay 11348us<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pkts_in 4454 overlimit 0 dropped 27 maxq 65 ecn_mark 0<br />
&nbsp;#&nbsp;tc qdisc add dev eth0 root pie limit 100 target 50ms tupdate 30ms bytemode<br />
&nbsp;#&nbsp;tc -s qdisc show<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;qdisc pie 8036: dev eth0 root refcnt 2 limit 100p target 50.0ms tupdate 32.0ms alpha 2 beta 20 bytemode<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sent 1616274 bytes 1137 pkt&nbsp;(dropped 0, overlimits 0 requeues 0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;backlog 13626b 9p requeues 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;prob 0.000000 delay 0us<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pkts_in 1146 overlimit 0 dropped 0 maxq 23 ecn_mark 0 </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-codel/">tc-codel</a></code>(8) <code><a href="/docs/linux/man/8-tc-red/">tc-red</a></code>(8) </p>
<h2>Sources</h2>
<p>&nbsp;o RFC 8033:&nbsp;<a rel="nofollow" href="https://tools.ietf.org/html/rfc8033">https://tools.ietf.org/html/rfc8033</a></p>
<h2>Authors</h2>
<p>PIE was implemented by Vijay Subramanian and Mythili Prabhu, also the authors of this man page. Please report bugs and corrections to the Linux networking development mailing list at &lt;netdev [at] vger.kernel.org&gt;.</p>
