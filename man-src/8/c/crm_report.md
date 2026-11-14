---
title: "crm_report(8)"
name: "crm_report"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_report/"
description: "crm_report – Part of the Pacemaker cluster resource manager"
---

<p>crm_report &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_report</code> <i>&#8211;from date-time </i>[<i>&#8211;to date-time</i>] [<i>additional options</i>] [<i>dest</i>]</p>
<h2>Description</h2>
<p>crm_report &#8211; Create a tarball containing everything needed when reporting cluster problems</p>
<h2>Options</h2>
<dl>
<dt><code>-V</code></p>
<dd>increase verbosity</p>
<dt><code>-v</code>,&#8211;version</p>
<dd>software version</p>
<dt><code>&#8211;features</code></p>
<dd>software features</p>
<dt><code>-f</code>, <code>&#8211;from</code> time</p>
<dd>time prior to problems beginning: &quot;YYYY-M-D H:M:S&quot; (do not forget the quotes)</p>
<dt><code>-t</code>, <code>&#8211;to</code> time</p>
<dd>time at which all problems were resolved: &quot;YYYY-M-D H:M:S&quot; (default: &#8216;now&#8217;)</p>
<dt><code>-T</code>, <code>&#8211;cts</code> test</p>
<dd>CTS test or set of tests to extract</p>
<dt><code>&#8211;cts-log</code></p>
<dd>CTS master logfile</p>
<dt><code>-n</code>, <code>&#8211;nodes</code> nodes</p>
<dd>node names for this cluster only needed if the cluster is not active on the current machine accepts both <code>-n</code> &quot;a b&quot; and <code>-n</code> a <code>-n</code> b</p>
<dt><code>-l</code>, <code>&#8211;logfile</code> file</p>
<dd>log file to collect, normally this will be determined automatically</p>
<dt><code>-p</code> patt</p>
<dd>additional regular expression to match variables to be removed (default: &quot;passw.*&quot;)</p>
<dt><code>-L</code> patt</p>
<dd>additional regular expression to match in log files for analysis (default: CRIT: ERROR:)</p>
<dt><code>-M</code></p>
<dd>collect only the logs specified by <code>-l</code></p>
<dt><code>-S</code>, <code>&#8211;single-node</code></p>
<dd>single node operation; don&#8217;t try to start report collectors on other nodes</p>
<dt><code>-c</code>, <code>&#8211;cluster</code> type</p>
<dd>force the cluster type (corosync,openais,heartbeat,logmaster)</p>
<dt><code>-A</code>, <code>&#8211;openais</code></p>
<dd>force the cluster type to be OpenAIS</p>
<dt><code>-C</code>, <code>&#8211;corosync</code></p>
<dd>force the cluster type to be CoroSync</p>
<dt><code>-H</code>, <code>&#8211;heartbeat</code></p>
<dd>force the cluster type to be Heartbeat</p>
<dt><code>-u</code>, <code>&#8211;user</code> user</p>
<dd>ssh username for cluster nodes (default: root)</p>
<dt><code>-D</code>, <code>&#8211;depth</code></p>
<dd>search depth to use when attempting to locate files</p>
<dt><code>-e</code>, <code>&#8211;rsh</code></p>
<dd>specify the remote shell to use (default: ssh <code>-T</code>)</p>
<dt><code>&#8211;sos-mode</code></p>
<dd>use defaults suitable for being called by sosreport tool (behavior subject to change and not useful to end users)</p>
<dt><code>&#8211;dest</code></p>
<dd>a custom destination directory/file</p>
<dt>dest</p>
<dd>a custom destination directory/file</dl>
<p> crm_report works best when run from a cluster node on a running cluster, but can be run from a stopped cluster node or a Pacemaker Remote node. </p>
<p> If neither <code>&#8211;nodes</code> nor <code>&#8211;single-node</code> is given, crm_report will guess the node list, but may have trouble detecting Pacemaker Remote nodes. Unless <code>&#8211;single-node</code> is given, the node names (whether specified by <code>&#8211;nodes</code> or detected automatically) must be resolvable and reachable via ssh.</p>
<h2>Examples</h2>
<dl>
<dd>crm_report -f &quot;2011-12-14 13:05:00&quot; unexplained-apache-failure crm_report -f 2011-12-14 -t 2011-12-15 something-that-took-multiple-days crm_report -f 13:05:00 -t 13:12:00 brief-outage </p>
