---
title: "sge_shadowd(8)"
name: "sge_shadowd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sge_shadowd/"
description: "xxqs_name_sxx_shadowd – xxQS_NAMExx shadow master daemon"
---

<p>xxqs_name_sxx_shadowd &#8211; xxQS_NAMExx shadow master daemon</p>
<h2>Synopsis</h2>
<p><code>xxqs_name_sxx_shadowd</code></p>
<h2>Description</h2>
<p><i>xxqs_name_sxx_shadowd</i> is a &quot;light weight&quot; process which can be run on so-called shadow master hosts in a xxQS_NAMExx cluster to detect failure of the current xxQS_NAMExx master daemon, and to start-up a new on the host on which the <i>xxqs_name_sxx_shadowd</i> runs. If multiple shadow daemons are active in a cluster, they run a protocol which ensures that only one of them will start-up a new master daemon. </p>
<p> The hosts suitable as shadow master hosts must have shared root read/write access to the directory <i>$xxQS_NAME_Sxx_ROOT/$xxQS_NAME_Sxx_CELL/common</i>, as well as to the master daemon spool directory (by default <i>$xxQS_NAME_Sxx_ROOT/$xxQS_NAME_Sxx_CELL/spool/qmaster</i>). The names of the shadow master hosts need to be contained in the file <i>$xxQS_NAME_Sxx_ROOT/$xQS_NAME_Sxx_CELL/common/shadow_masters</i>.</p>
<h2>Restrictions</h2>
<p><i>xxqs_name_sxx_shadowd</i> may only be started by root.</p>
<h2>Environment Variables</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd>Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd>If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>xxqs_name_sxx_shadowd</i> uses (in order of precedence): </p>
<dl>
<dd>
<dl>
<dd>The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd>If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd>If set, specifies the TCP port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</p>
<dt><code>xxQS_NAME_Sxx_DELAY_TIME</code></p>
<dd>This variable controls the time for which <i>xxqs_name_sxx_shadowd</i> pauses if a takeover bid fails. This value is used only when there are multiple <i>xxqs_name_sxx_shadowd</i> instances and they are contending to be the master. The default is 600 seconds.</p>
<dt><code>xxQS_NAME_Sxx_CHECK_INTERVAL</code></p>
<dd>This variable controls the interval between <i>xxqs_name_sxx_shadowd</i> checks of the heartbeat file (60 seconds by default).</p>
<dt><code>xxQS_NAME_Sxx_GET_ACTIVE_INTERVAL</code></p>
<dd>This variable controls the interval between attempts by a <i>xxqs_name_sxx_shadowd</i> instance to take over when the heartbeat file has not changed. The default is 240 seconds.</dl>
<h2>Files</h2>
<pre><i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common</i>
 Default configuration directory
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/shadow_masters</i>
 Shadow master hostname file.
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/spool/qmaster</i>
 Default master daemon spool directory
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/spool/qmaster/heartbeat</i>
 The heartbeat file.</pre>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
