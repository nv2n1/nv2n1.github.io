---
title: "qperf(1)"
name: "qperf"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qperf/"
description: "qperf – Measure RDMA and IP performance"
---

<h2>NAME</h2>
<p> qperf &#8211; Measure RDMA and IP performance</p>
<h2>SYNOPSIS</h2>
<p> <code>qperf</code><br />
 <code>qperf</code> <i>SERVERNODE</i> [<i>OPTIONS</i>] <i>TESTS</i> </p>
<h2>DESCRIPTION</h2>
<p> qperf measures bandwidth and latency between two nodes. It can work over TCP/IP as well as the RDMA transports. On one of the nodes, qperf is typically run with no arguments designating it the server node. One may then run qperf on a client node to obtain measurements such as bandwidth, latency and cpu utilization. </p>
<p> In its most basic form, qperf is run on one node in server mode by invoking it with no arguments. On the other node, it is run with two arguments: the name of the server node followed by the name of the test. A list of tests can be found in the section, TESTS. A variety of options may also be specified. </p>
<p> One can get more detailed information on qperf by using the &#8211;help option. Below are examples of using the &#8211;help option: </p>
<p>&nbsp;<wbr>qperf &#8211;help examples&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Some examples of using qperf<br />
&nbsp;<wbr>qperf &#8211;help opts&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Summary of options<br />
&nbsp;<wbr>qperf &#8211;help options&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Description of options<br />
&nbsp;<wbr>qperf &#8211;help tests&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Short summary and description of tests<br />
&nbsp;<wbr>qperf &#8211;help TESTNAME&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>More information on test TESTNAME</p>
<h2>EXAMPLES</h2>
<p> In these examples, we first run qperf on a node called myserver in server mode by invoking it with no arguments. In all the subsequent examples, we run qperf on another node and connect to the server which we assume has a hostname of myserver.</p>
<dl>
<dt>To run a TCP bandwidth and latency test:</p>
<dd> qperf myserver tcp_bw tcp_lat</p>
<dt>To run a UDP latency test and then cause the server to terminate:</p>
<dd> qperf myserver udp_lat quit</p>
<dt>To measure the RDMA UD latency and bandwidth:</p>
<dd> qperf myserver ud_lat ud_bw</p>
<dt>To measure RDMA UC bi-directional bandwidth:</p>
<dd> qperf myserver rc_bi_bw</p>
<dt>To get a range of TCP latencies with a message size from 1 to 64K</p>
<dd> qperf myserver -oo msg_size:1:64K:*2 -vu tcp_lat</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ar</code>, <code>&#8211;access_recv</code> <i>OnOff</i></p>
<dd> If OnOff is non-zero, data is accessed once received. Otherwise, data is ignored. By default, OnOff is 0. This can help to mimic some applications.</p>
<dt><code>-ar1</code></p>
<dd> Cause received data to be accessed.</p>
<dt><code>-ap</code>, <code>&#8211;alt_port</code> <i>Port</i></p>
<dd> Set alternate path port. This enables automatic path failover.</p>
<dt><code>-lap</code>, <code>&#8211;loc_alt_port</code> <i>Port</i></p>
<dd> Set local alternate path port. This enables automatic path failover.</p>
<dt><code>-rap</code>, <code>&#8211;rem_alt_port</code> <i>Port</i></p>
<dd> Set remote alternate path port. This enables automatic path failover.</p>
<dt><code>-ca</code>, <code>&#8211;cpu_affinity</code> <i>PN</i></p>
<dd> Set cpu affinity to PN. CPUs are numbered sequentially from 0. If PN is &quot;any&quot;, any cpu is allowed otherwise the cpu is limited to the one specified.</p>
<dt><code>-lca</code>, <code>&#8211;loc_cpu_affinity</code> <i>PN</i></p>
<dd> Set local processor affinity to PN.</p>
<dt><code>-rca</code>, <code>&#8211;rem_cpu_affinity</code> <i>PN</i></p>
<dd> Set remote processor affinity to PN.</p>
<dt><code>-f</code>, <code>&#8211;flip</code> <i>OnOff</i></p>
<dd> If non-zero, cause sender and receiver to play opposite roles.</p>
<dt><code>-f1</code></p>
<dd> Cause sender and receiver to play opposite roles.</p>
<dt><code>-h</code>, <code>&#8211;help</code> <i>Topic</i></p>
<dd> Print out information about Topic. To see the list of topics, type qperf &#8211;help</p>
<dt><code>-H</code>, <code>&#8211;host</code> <i>Host</i></p>
<dd> Run test between the current node and the qperf running on node Host. This can also be specified as the first non-option argument.</p>
<dt><code>-i</code>, <code>&#8211;id</code> <i>Device:Port</i></p>
<dd> Use RDMA Device and Port.</p>
<dt><code>-li</code>, <code>&#8211;loc_id</code> <i>Device:Port</i></p>
<dd> Use local RDMA Device and Port.</p>
<dt><code>-ri</code>, <code>&#8211;rem_id</code> <i>Device:Port</i></p>
<dd> Use remote RDMA Device and Port.</p>
<dt><code>-lp</code>, <code>&#8211;listen_port</code> <i>Port</i></p>
<dd> Set the port we listen on to ListenPort. This must be set to the same port on both the server and client machines. The default value is 19765.</p>
<dt><code>-oo</code>, <code>&#8211;loop</code> <i>Var:Init:Last:Incr</i></p>
<dd> Run a test multiple times sequencing through a series of values. Var is the loop variable; Init is the initial value; Last is the value it must not exceed and Incr is the increment. It is useful to set the &#8211;verbose_used (-vu) option in conjunction with this option.</p>
<dt><code>-m</code>, <code>&#8211;msg_size</code> <i>Size</i></p>
<dd> Set the message size to Size. The default value varies by test. It is assumed that the value is specified in bytes however, a trailing kib or K, mib or M, or gib or G indicates that the size is being specified in kibibytes, mebibytes or gibibytes respectively while a trailing kb or k, mb or m, or gb or g indicates kilobytes, megabytes or gigabytes respectively.</p>
<dt><code>-mt</code>, <code>&#8211;mtu_size</code> <i>Size</i></p>
<dd> Set the MTU size. Only relevant to the RDMA UC/RC tests. Units are specified in the same manner as the &#8211;msg_size option.</p>
<dt><code>-n</code>, <code>&#8211;no_msgs</code> <i>N</i></p>
<dd> Set test duration by number of messages sent instead of time.</p>
<dt><code>-cp</code>, <code>&#8211;cq_poll</code> <i>OnOff</i></p>
<dd> Turn polling mode on or off. This is only relevant to the RDMA tests and determines whether they poll or wait on the completion queues. If OnOff is 0, they wait; otherwise they poll.</p>
<dt><code>-lcp</code>, <code>&#8211;loc_cq_poll</code> <i>OnOff</i></p>
<dd> Locally turn polling mode on or off.</p>
<dt><code>-rcp</code>, <code>&#8211;rem_cq_poll</code> <i>OnOff</i></p>
<dd> Remotely turn polling mode on or off.</p>
<dt><code>-cp1</code></p>
<dd> Turn polling mode on.</p>
<dt><code>-lcp1</code></p>
<dd> Turn local polling mode on.</p>
<dt><code>-rcp1</code></p>
<dd> Turn remote polling mode on.</p>
<dt><code>-ip</code>, <code>&#8211;ip_port</code> <i>Port</i></p>
<dd> Use Port to run the socket tests. This is different from &#8211;listen_port which is used for synchronization. This is only relevant for the socket tests and refers to the TCP/UDP/RDS/SCTP port that the test is run on.</p>
<dt><code>-e</code>, <code>&#8211;precision</code> <i>Digits</i></p>
<dd> Set the number of significant digits that are used to report results.</p>
<dt><code>-nr</code>, <code>&#8211;rd_atomic</code> <i>Max</i></p>
<dd> Set the number of in-flight operations that can be handled for a RDMA read or atomic operation to Max. This is only relevant to the RDMA Read and Atomic tests.</p>
<dt><code>-lnr</code>, <code>&#8211;loc_rd_atomic</code> <i>Max</i></p>
<dd> Set local read/atomic count.</p>
<dt><code>-rnr</code>, <code>&#8211;rem_rd_atomic</code> <i>Max</i></p>
<dd> Set remote read/atomic count.</p>
<dt><code>-sl</code>, <code>&#8211;service_level</code> <i>SL</i></p>
<dd> Set RDMA service level to SL. This is only used by the RDMA tests. The service level must be between 0 and 15. The default service level is 0.</p>
<dt><code>-lsl</code>, <code>&#8211;loc_service_level</code> <i>SL</i></p>
<dd> Set local service level.</p>
<dt><code>-rsl</code>, <code>&#8211;rem_service_level</code> <i>SL</i></p>
<dd> Set remote service level.</p>
<dt><code>-sb</code>, <code>&#8211;sock_buf_size</code> <i>Size</i></p>
<dd> Set the socket buffer size. This is only relevant to the socket tests.</p>
<dt><code>-lsb</code>, <code>&#8211;loc_sock_buf_size</code> <i>Size</i></p>
<dd> Set local socket buffer size.</p>
<dt><code>-rsb</code>, <code>&#8211;rem_sock_buf_size</code> <i>Size</i></p>
<dd> Set remote socket buffer size.</p>
<dt><code>-sp</code>, <code>&#8211;src_path_bits</code> <i>N</i></p>
<dd> Set source path bits. If the LMC is not zero, this will cause the connection to use a LID with the low order LMC bits set to N.</p>
<dt><code>-lsp</code>, <code>&#8211;loc_src_path_bits</code> <i>N</i></p>
<dd> Set local source path bits.</p>
<dt><code>-rsp</code>, <code>&#8211;rem_src_path_bits</code> <i>N</i></p>
<dd> Set remote source path bits.</p>
<dt><code>-sr</code>, <code>&#8211;static_rate</code> <i>Rate</i></p>
<dd> Force InfiniBand static rate. Rate can be one of: 2.5, 5, 10, 20, 30, 40, 60, 80, 120, 1xSDR (2.5 Gbps), 1xDDR (5 Gbps), 1xQDR (10 Gbps), 4xSDR (2.5 Gbps), 4xDDR (5 Gbps), 4xQDR (10 Gbps), 8xSDR (2.5 Gbps), 8xDDR (5 Gbps), 8xQDR (10 Gbps).</p>
<dt><code>-lsr</code>, <code>&#8211;loc_static_rate</code></p>
<dd> Force local InfiniBand static rate</p>
<dt><code>-rsr</code>, <code>&#8211;rem_static_rate</code></p>
<dd> Force remote InfiniBand static rate</p>
<dt><code>-t</code>, <code>&#8211;time</code> <i>Time</i></p>
<dd> Set test duration to Time. Specified in seconds however a trailing m, h or d indicates that the time is specified in minutes, hours or days respectively.</p>
<dt><code>-to</code>, <code>&#8211;timeout</code> <i>Time</i></p>
<dd> Set timeout to Time. This is the timeout used for various things such as exchanging messages. The default is 5 seconds.</p>
<dt><code>-lto</code>, <code>&#8211;loc_timeout</code> <i>Time</i></p>
<dd> Set local timeout to Time. This may be used on the server to set the timeout when initially exchanging data with each client. However, as soon as we receive the client&#8217;s parameters, the client&#8217;s remote timeout will override this parameter.</p>
<dt><code>-rto</code>, <code>&#8211;rem_timeout</code> <i>Time</i></p>
<dd> Set remote timeout to Time.</p>
<dt><code>-un</code>, <code>&#8211;unify_nodes</code></p>
<dd> Unify the nodes. Describe them in terms of local and remote rather than send and receive.</p>
<dt><code>-uu</code>, <code>&#8211;unify_units</code></p>
<dd> Unify the units that results are shown in. Uses the lowest common denominator. Helpful for scripts.</p>
<dt><code>-ub</code>, <code>&#8211;use_bits_per_sec</code></p>
<dd> Use bits/sec rather than bytes/sec when displaying networking speed.</p>
<dt><code>-cm</code>, <code>&#8211;use_cm</code> <i>OnOff</i></p>
<dd> Use the RDMA Connection Manager (CM) if OnOff is non-zero. It is necessary to use the CM for iWARP devices. The default is to establish the connection without using the CM. This only works for the tests that use the RC transport.</p>
<dt><code>-cm1</code></p>
<dd> Use RDMA Connection Manager.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Provide more detailed output. Turns on -vc, -vs, -vt and -vu.</p>
<dt><code>-vc</code>, <code>&#8211;verbose_conf</code></p>
<dd> Provide information on configuration.</p>
<dt><code>-vs</code>, <code>&#8211;verbose_stat</code></p>
<dd> Provide information on statistics.</p>
<dt><code>-vt</code>, <code>&#8211;verbose_time</code></p>
<dd> Provide information on timing.</p>
<dt><code>-vu</code>, <code>&#8211;verbose_used</code></p>
<dd> Provide information on parameters used.</p>
<dt><code>-vv</code>, <code>&#8211;verbose_more</code></p>
<dd> Provide even more detailed output. Turns on -vvc, -vvs, -vvt and -vvu.</p>
<dt><code>-vvc</code>, <code>&#8211;verbose_more_conf</code></p>
<dd> Provide more information on configuration.</p>
<dt><code>-vvs</code>, <code>&#8211;verbose_more_stat</code></p>
<dd> Provide more information on statistics.</p>
<dt><code>-vvt</code>, <code>&#8211;verbose_more_time</code></p>
<dd> Provide more information on timing.</p>
<dt><code>-vvu</code>, <code>&#8211;verbose_more_used</code></p>
<dd> Provide more information on parameters used.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> The current version of qperf is printed.</p>
<dt><code>-ws</code>, <code>&#8211;wait_server</code> <i>Time</i></p>
<dd> If the server is not ready, continue to try connecting for Time seconds before giving up. The default is 5 seconds.</dl>
<h2>TESTS</h2>
<dl>
<dt><code>conf</code></p>
<dd> Show configuration</p>
<dt><code>quit</code></p>
<dd> Cause the server to quit</p>
<dt><code>rds_bw</code></p>
<dd> RDS streaming one way bandwidth</p>
<dt><code>rds_lat</code></p>
<dd> RDS one way latency</p>
<dt><code>sctp_bw</code></p>
<dd> SCTP streaming one way bandwidth</p>
<dt><code>sctp_lat</code></p>
<dd> SCTP one way latency</p>
<dt><code>tcp_bw</code></p>
<dd> TCP streaming one way bandwidth</p>
<dt><code>tcp_lat</code></p>
<dd> TCP one way latency</p>
<dt><code>udp_bw</code></p>
<dd> UDP streaming one way bandwidth</p>
<dt><code>udp_lat</code></p>
<dd> UDP one way latency</p>
<dt><code>rc_bi_bw</code></p>
<dd> RC streaming two way bandwidth</p>
<dt><code>rc_bw</code></p>
<dd> RC streaming one way bandwidth</p>
<dt><code>rc_lat</code></p>
<dd> RC one way latency</p>
<dt><code>uc_bi_bw</code></p>
<dd> UC streaming two way bandwidth</p>
<dt><code>uc_bw</code></p>
<dd> UC streaming one way bandwidth</p>
<dt><code>uc_lat</code></p>
<dd> UC one way latency</p>
<dt><code>ud_bi_bw</code></p>
<dd> UD streaming two way bandwidth</p>
<dt><code>ud_bw</code></p>
<dd> UD streaming one way bandwidth</p>
<dt><code>ud_lat</code></p>
<dd> UD one way latency</p>
<dt><code>xrc_bi_bw</code></p>
<dd> XRC streaming two way bandwidth</p>
<dt><code>xrc_bw</code></p>
<dd> XRC streaming one way bandwidth</p>
<dt><code>xrc_lat</code></p>
<dd> XRC one way latency</p>
<dt><code>rc_rdma_read_bw</code></p>
<dd> RC RDMA read streaming one way bandwidth</p>
<dt><code>rc_rdma_read_lat</code></p>
<dd> RC RDMA read one way latency</p>
<dt><code>rc_rdma_write_bw</code></p>
<dd> RC RDMA write streaming one way bandwidth</p>
<dt><code>rc_rdma_write_lat</code></p>
<dd> RC RDMA write one way latency</p>
<dt><code>rc_rdma_write_poll_lat</code></p>
<dd> RC RDMA write one way polling latency</p>
<dt><code>uc_rdma_write_bw</code></p>
<dd> UC RDMA write streaming one way bandwidth</p>
<dt><code>uc_rdma_write_lat</code></p>
<dd> UC RDMA write one way latency</p>
<dt><code>uc_rdma_write_poll_lat</code></p>
<dd> UC RDMA write one way polling latency</p>
<dt><code>rc_compare_swap_mr</code></p>
<dd> RC compare and swap messaging rate</p>
<dt><code>rc_fetch_add_mr</code></p>
<dd> RC fetch and add messaging rate</p>
<dt><code>ver_rc_compare_swap</code></p>
<dd> Verify RC compare and swap</p>
<dt><code>ver_rc_fetch_add</code></p>
<dd> Verify RC fetch and add</dl>
<h2>AUTHOR</h2>
<p> Written by Johann George.</p>
<h2>BUGS</h2>
<p> None of the RDMA tests are available if qperf is compiled without the RDMA libraries. None of the XRC tests are available if qperf is compiled without the XRC extensions. The -f option is not yet implemented in many of the tests. </p>
<h2>Index</h2>
