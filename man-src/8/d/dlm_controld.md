---
title: "dlm_controld(8)"
name: "dlm_controld"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dlm_controld/"
description: "dlm_controld – dlm cluster control daemon"
---

<p>dlm_controld &#8211; dlm cluster control daemon</p>
<h2>Synopsis</h2>
<p><code>dlm_controld</code> [OPTIONS] </p>
<h2>Description</h2>
<p>The kernel dlm requires a user daemon to manage lockspace membership. dlm_controld manages lockspace membership using corosync cpg groups, and translates membership changes into dlm kernel recovery events. dlm_controld also manages posix locks for cluster file systems using the dlm. </p>
<h2>Options</h2>
<p>Command line options override a corresponding setting in <code><a href="/docs/linux/man/5-dlm-conf/">dlm.conf</a></code>(5).<br />
 For default settings, see dlm_controld -h. </p>
<p> <code>&#8211;daemon_debug | -D</code><br />
&nbsp;<wbr>&nbsp;<wbr>enable debugging to stderr and don&#8217;t fork </p>
<p> <code>&#8211;foreground</code><br />
&nbsp;<wbr>&nbsp;<wbr>don&#8217;t fork </p>
<p> <code>&#8211;log_debug | -K</code><br />
&nbsp;<wbr>&nbsp;<wbr>enable kernel dlm debugging messages </p>
<p> <code>&#8211;protocol | -r</code> <i>str</i><br />
&nbsp;<wbr>&nbsp;<wbr>dlm kernel lowcomms protocol: tcp, sctp, detect </p>
<p> <code>&#8211;debug_logfile | -L</code><br />
&nbsp;<wbr>&nbsp;<wbr>write debugging to log file </p>
<p> <code>&#8211;enable_plock | -p</code> 0|1<br />
&nbsp;<wbr>&nbsp;<wbr>enable/disable posix lock support for cluster fs </p>
<p> <code>&#8211;plock_debug | -P</code><br />
&nbsp;<wbr>&nbsp;<wbr>enable plock debugging </p>
<p> <code>&#8211;plock_rate_limit | -l</code> <i>int</i><br />
&nbsp;<wbr>&nbsp;<wbr>limit rate of plock operations&nbsp;<wbr>(0 for none) </p>
<p> <code>&#8211;plock_ownership | -o</code> 0|1<br />
&nbsp;<wbr>&nbsp;<wbr>enable/disable plock ownership </p>
<p> <code>&#8211;drop_resources_time | -t</code> <i>int</i><br />
&nbsp;<wbr>&nbsp;<wbr>plock ownership drop resources time&nbsp;<wbr>(milliseconds) </p>
<p> <code>&#8211;drop_resources_count | -c</code> <i>int</i><br />
&nbsp;<wbr>&nbsp;<wbr>plock ownership drop resources count </p>
<p> <code>&#8211;drop_resources_age | -a</code> <i>int</i><br />
&nbsp;<wbr>&nbsp;<wbr>plock ownership drop resources age&nbsp;<wbr>(milliseconds) </p>
<p> <code>&#8211;post_join_delay | -j</code> <i>int</i><br />
&nbsp;<wbr>&nbsp;<wbr>seconds to delay fencing after cluster join </p>
<p> <code>&#8211;enable_fencing | -f</code> 0|1<br />
&nbsp;<wbr>&nbsp;<wbr>enable/disable fencing </p>
<p> <code>&#8211;enable_concurrent_fencing</code> 0|1<br />
&nbsp;<wbr>&nbsp;<wbr>enable/disable concurrent fencing </p>
<p> <code>&#8211;enable_startup_fencing | -s</code> 0|1<br />
&nbsp;<wbr>&nbsp;<wbr>enable/disable startup fencing </p>
<p> <code>&#8211;enable_quorum_fencing | -q</code> 0|1<br />
&nbsp;<wbr>&nbsp;<wbr>enable/disable quorum requirement for fencing </p>
<p> <code>&#8211;enable_quorum_lockspace</code> 0|1<br />
&nbsp;<wbr>&nbsp;<wbr>enable/disable quorum requirement for lockspace operations </p>
<p> <code>&#8211;fence_all</code> <i>str</i><br />
&nbsp;<wbr>&nbsp;<wbr>fence all nodes with this agent </p>
<p> <code>&#8211;unfence_all</code><br />
&nbsp;<wbr>&nbsp;<wbr>enable unfencing self with fence_all agent </p>
<p> <code>&#8211;help | -h</code><br />
&nbsp;<wbr>&nbsp;<wbr>print this help, then exit </p>
<p> <code>&#8211;version | -V</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print program version information, then exit</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dlm_tool/">dlm_tool</a></code>(8), <code><a href="/docs/linux/man/5-dlm-conf/">dlm.conf</a></code>(5) </p>
