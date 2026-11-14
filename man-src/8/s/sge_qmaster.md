---
title: "sge_qmaster(8)"
name: "sge_qmaster"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sge_qmaster/"
description: "xxqs_name_sxx_qmaster – xxQS_NAMExx master control daemon"
---

<p>xxqs_name_sxx_qmaster &#8211; xxQS_NAMExx master control daemon</p>
<h2>Synopsis</h2>
<p><code>xxqs_name_sxx_qmaster</code> [ <code>-help</code> ]</p>
<h2>Description</h2>
<p><i>xxqs_name_sxx_qmaster</i> controls the overall xxQS_NAMExx behavior in a cluster.</p>
<h2>Options</h2>
<dl>
<dt><code>-help</code></p>
<dd>Prints a listing of all options.</dl>
<h2>Environment Variables</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd>Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd>If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>xxqs_name_sxx_qmaster</i> uses (in order of precedence): </p>
<dl>
<dd>
<dl>
<dd>The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd>If set, specifies that debug information should be written to stderr. In addition, the level of detail in which debug information is generated is defined by the defined value.</p>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd>If set, the qmaster will not daemonize.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd>If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</p>
<dt><code>xxQS_NAME_Sxx_EXECD_PORT</code></p>
<dd>If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_execd&quot; instead to define that port.</p>
<dt><code>xxQS_NAME_Sxx_TEST_DELAY_SCHEDULING</code></p>
<dd>If set, specifies a delay in (integral seconds) before a scheduling run, for test purposes.</p>
<dt><code>SGE_ND</code></p>
<dd>If set, don&#8217;t daemonize the program (for debugging).</p>
<dt><code>SGE_ENABLE_COREDUMP</code></p>
<dd>If set, enable core dumps on Linux when the admin_user is not root. Linux normally disables core dumps when the daemon has changed uid or gid. Setting SGE_ENABLE_COREDUMP in xxqs_name_sxx_qmaster&#8217;s environment defeats that to enable core dumps for debugging if they are otherwise allowed. This is typically not a big hazard with xxQS_NAME_Sxx, since most information is exposed in the spool area anyhow. Dumps will appear in the host spool directory.<br />
 On Solaris, may be used to enable such dumps.</p>
<dt><code>SGE_QMASTER_PIDFILE</code></p>
<dd>Path name of file to which to write the daemon process id at startup (default &quot;qmaster.pid&quot;). Note that this must be writable by the admin user (see</dl>
<h2>Restrictions</h2>
<p><i>xxqs_name_sxx_qmaster</i> is usually started from root on the master or shadow master machines of the cluster. If started by a normal user, a master spool directory must be used to which the user has read/write access. In this case only jobs being submitted by that same user are handled correctly by the system.</p>
<h2>Files</h2>
<pre><i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/configuration</i>
 xxQS_NAMExx global configuration
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/local_conf/&lt;host&gt;</i>
 xxQS_NAMExx host specific configuration
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/qmaster_args</i>
 <i>xxqs_name_sxx_qmaster</i> argument file
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/spool</i>
 Default master spool directory</pre>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
