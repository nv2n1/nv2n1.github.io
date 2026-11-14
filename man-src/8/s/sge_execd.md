---
title: "sge_execd(8)"
name: "sge_execd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sge_execd/"
description: "xxqs_name_sxx_execd, xxqs_name_sxx_loadsensor – xxQS_NAMExx job execution agent and load sensor interface"
---

<p>xxqs_name_sxx_execd, xxqs_name_sxx_loadsensor &#8211; xxQS_NAMExx job execution agent and load sensor interface</p>
<h2>Synopsis</h2>
<p><code>xxqs_name_sxx_execd</code> [ <code>-help</code> ]</p>
<h2>Description</h2>
<p><i>xxqs_name_sxx_execd</i> controls the xxQS_NAMExx queues local to the machine on which <i>xxqs_name_sxx_execd</i> is running and executes/controls the jobs sent from to be run on these queues via or the <code>shepherd_cmd</code> of</p>
<h2>Options</h2>
<h3><code>-help</code></h3>
<p>Prints a listing of all options.</p>
<h2>Load Sensors</h2>
<p>One of more <code>load sensor</code>s may be configured for <i>xxqs_name_sxx_execd</i> via the possibilities listed in the global host configuration, the execution-host-specific cluster configuration, the default <i>qloadsensor</i>, or <i>qidle</i> (when <code>USE_QIDLE</code> is set &#8211; see The executable path of the load sensor is invoked by <i>xxqs_name_sxx_execd</i> on a regular basis (governed by <code>load_report_time</code> in and delivers one or multiple load figures for the execution host (e.g. users currently logged in) or the complete cluster (e.g. free disk space on a network wide scratch file system). A load sensor may be a script or a binary executable. In either case its handling of the STDIN and STDOUT streams and its control flow must comply with the following rules. Load sensors are restarted if their modification time changes or they are killed. If they read a configuration file, for instance, killing will be necessary to pick up modifications to it unless the sensor will re-read a modified version.</p>
<h3>Load sensor interface</h3>
<p>The load sensor must be written as an infinite loop, waiting at a certain point for input from STDIN. If the string &quot;quit&quot; is read from STDIN, the load sensor should exit. When an end-of-line is read from STDIN, a load data retrieval cycle should start. The load sensor then performs whatever operation is necessary to compute the desired load figures. At the end of the cycle the load sensor writes the result to stdout. The format is as follows:</p>
<dl>
<dt>&bull;</p>
<dd>A load value report starts with a line containing only either the word &quot;start&quot; or the word &quot;begin&quot;.</p>
<dt>&bull;</p>
<dd>Individual load values are separated by newlines.</p>
<dt>&bull;</p>
<dd>Each load value report consists of three parts separated by colons (&quot;:&quot;) and containing no blanks.</p>
<dt>&bull;</p>
<dd>The first part of a load value information is either the name of the host for which load is reported or the special name &quot;global&quot;.</p>
<dt>&bull;</p>
<dd>The second part is the symbolic name of the load value as defined in the host or global complex list (see for details). This must be the full name of the complex, not the shortcut name. If a load value is reported for which no entry in the host or global complex list exists, the reported load value is not used.</p>
<dt>&bull;</p>
<dd>The third part is the measured load value.</p>
<dt>&bull;</p>
<dd>A load value report ends with a line with only the word &quot;end&quot;.</dl>
<p> NB. If the runtime of the language in which the sensor is written buffers the output (e.g. Perl), ensure it is flushed on each iteration.</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd>Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd>If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>xxqs_name_sxx_execd</i> uses (in the order of precedence): </p>
<dl>
<dd>
<dl>
<dd>The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd>If set, specifies that debug information should be written to stderr. In addition, the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd>If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</p>
<dt><code>xxQS_NAME_Sxx_EXECD_PORT</code></p>
<dd>If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_execd&quot; instead to define that port.</p>
<dt><code>SGE_ND</code></p>
<dd>If set, don&#8217;t daemonize the program (for debugging).</p>
<dt><code>SGE_ENABLE_COREDUMP</code></p>
<dd>If set, enable core dumps on Linux when the admin_user is not root. Linux normally disables core dumps when the daemon has changed uid or gid. Setting SGE_ENABLE_COREDUMP in xxqs_name_sxx_execd&#8217;s environment defeats that to enable core dumps for debugging if they are otherwise allowed. This is typically not a big hazard with xxQS_NAME_Sxx, since most information is exposed in the spool area anyhow. Dumps will appear in the qmaster spool directory, which need not be world-readable.<br />
 On Solaris, may be used to enable such dumps.</p>
<dt><code>SGE_EXECD_PIDFILE</code></p>
<dd>Path name of file to which to write the daemon process id at startup (default &quot;execd.pid&quot;). Note that this must be writable by the admin user (see</dl>
<h2>Restrictions</h2>
<p><i>xxqs_name_sxx_execd</i> usually is started from root on each machine in the xxQS_NAMExx pool. If started by a normal user, a spool directory must be used to which the user has read/write access. In this case only jobs being submitted by that same user are handled correctly by the system.</p>
<h2>Files</h2>
<pre><i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/configuration</i>
 xxQS_NAMExx global configuration
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/local_conf/&lt;host&gt;</i>
 xxQS_NAMExx host specific configuration
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/spool/&lt;host&gt;</i>
 Default execution host spool directory
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
 xxQS_NAMExx master host file
<i>&lt;xxqs_name_sxx_root&gt;/bin/&lt;arch&gt;/qloadsensor</i>
 Default load sensor
<i>&lt;xxqs_name_sxx_root&gt;/bin/&lt;arch&gt;/qidle</i>
 Idle load sensor per USE_QIDLE in execd_params
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/sgepasswd</i>
 Password information used on Microsoft Windows hosts. See</pre>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
