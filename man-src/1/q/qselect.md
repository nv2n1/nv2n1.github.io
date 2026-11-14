---
title: "qselect(1)"
name: "qselect"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qselect/"
description: "qselect – select queues."
---

<h2 class="name">NAME</h2>
<p> qselect &#8211; select queues. </p>
<h2>SYNTAX</h2>
<p> <code>qselect</code> [ <code>-help</code> ] [ <code>-l resource=val,&#8230;</code> ] [ <code>-pe pe_name,&#8230;</code> ] [ <code>-q wc_queue,&#8230;</code> ] [ <code>-s {r|p|s|z|hu|ho|hs|hj|ha|h}[+]</code> ] [ <code>-U user,&#8230;</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>qselect</i> prints a list of xxQS_NAMExx queue instance names corresponding to selection criteria specified in the arguments described below. The output is of limited use since it comprises queue instances rather than cluster queues or hosts.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-l resource</code>[<code>=value</code>],&#8230;</p>
<dd> Defines the resources to be granted by the queues which should be included in the queue list output. Matching is performed on queues based on non-mutable resource availability information only. That means load values are always ignored except the so-called static load values listed in Also consumable utilization is ignored. If there are multiple -l resource requests they will be concatenated by a logical AND: a queue needs to offer all resources to be displayed.</p>
<dt><code>-pe pe_name,&#8230;</code></p>
<dd> Includes queue instances in the output to which are attached at least one of the parallel environments listed in the comma-separated option argument.</p>
<dt><code>-q wc_queue,&#8230;</code></p>
<dd> Directly specifies the wildcard expression queue list to be included in the output. This option usually is only meaningful in conjunction with another <i>qselect</i> option to extract a subset of queue names from a list given by <code>-q</code>. Description of <i>wc_queue</i> can be found in</p>
<dt><code>-qs {a|c|d|o|s|u|A|C|D|E|S}</code></p>
<dd> This option allows filtering by queue instances in certain states (see</p>
<dt><code>-U user,&#8230;</code></p>
<dd> Includes the queues to which the specified users have access in the <i>qselect </i> output.</dl>
<h2>EXAMPLES</h2>
<pre><code>
== == == == == == == == == == == == == == == == == == == == == == == == == == =
                                                                                  % qselect - l arch = linux % qselect - l arch = linux - U andreas,
                                                                           shannon % qconf - mattr queue h_vmem = 1GB `qselect - l arch = linux` == == == == == == == == == == == == == == == == == == == == == == == == == == =
</code></pre>
<p> The first example prints the names of those queues residing on Linux machines. The second command in addition restricts the output to those queues with access permission for the users <i>andreas</i> and <i>shannon</i>. The third command changes the queue attribute <i>h_vmem</i> to 1 Gigabyte on queues residing on Linux machines (see the manual page for details on the <i>-mattr</i> option and the manual page on details of queue configuration entries).</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qselect</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</dl>
<h2>FILES</h2>
<pre>
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
                          xxQS_NAMExx master host file
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
