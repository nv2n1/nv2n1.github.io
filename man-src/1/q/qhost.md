---
title: "qhost(1)"
name: "qhost"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qhost/"
description: "qhost – show the status of xxQS_NAMExx hosts, queues, jobs"
---

<h2 class="name">NAME</h2>
<p> qhost &#8211; show the status of xxQS_NAMExx hosts, queues, jobs </p>
<h2>SYNTAX</h2>
<p> <code>qhost</code> [<code>-F</code> [<i>resource_name</i><code>,</code>&#8230;]] [<code>-help</code>] [<code>-h</code> <i>host_list</i>] [<code>-j</code>] [<code>-l</code> <i>resource</i>[<code>=</code><i>val</i>]<code>,</code>&#8230;] [<code>-ncb</code>] [<code>-u</code> <i>user</i><code>,</code>&#8230;] [<code>-xml</code>]</p>
<h2>DESCRIPTION</h2>
<p> <i>qhost</i> shows the current status of the available xxQS_NAMExx hosts, queues and the jobs associated with the queues. Selection options allow you to get information about specific hosts, queues, jobs or users. If multiple selections are done a host is only displayed if all selection criteria for a host are met. Without any options <i>qhost</i> will display a list of all hosts without queue or job information. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F</code> [<i>resource_name</i><code>,</code>&#8230;]</p>
<dd> <i>qhost</i> will present a detailed listing of the current resource availability per host with respect to all resources (if the option argument is omitted) or with respect to those resources contained in the resource_name list. Please refer to the description of the <code>Full Format</code> in section <code>OUTPUT FORMATS</code> below for further detail.</p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-h </code><i>host_list</i></p>
<dd> Prints a list of all hosts contained in host_list.</p>
<dt><code>-j</code></p>
<dd> Prints all jobs running on the queues hosted by the shown hosts. This switch calls <code>-q</code> implicitly.</p>
<dt><code>-l </code><i>resource</i>[<code>=</code><i>value</i>]<code>,</code>&#8230;</p>
<dd> Defines the resources to be granted by the hosts which should be included in the host list output. Matching is performed on hosts based on non-mutable resource availability information only. That means load values are always ignored except the so-called static load values listed in Also consumable utilization is ignored. If there are multiple -l resource requests they will be concatenated by a logical AND: a host needs to match all resources to be displayed.</p>
<dt><code>-ncb</code></p>
<dd> This command line switch can be used in order to get 6.2u5 compatible output with other command line switches. In that case the output of the corresponding command will suppress information concerning the execution host topology. Note that this option will be removed in the next major version.</p>
<dt><code>-q</code></p>
<dd> Show information about the queues instances hosted by the displayed hosts.</p>
<dt><code>-u </code><i>user</i><code>,</code>&#8230;</p>
<dd> Display information only on those jobs and queues being associated with the users from the given user list.</p>
<dt><code>-xml</code></p>
<dd> This option can be used with all other options and changes the output to XML. The used schemas are referenced in the XML output. The output is printed to stdout. </p>
<p> If the <code>-xml</code> parameter is combined with <code>-ncb</code> then the XML output will contain 6.2u5 compatible output.
</dl>
<h2>OUTPUT FORMATS</h2>
<p> Depending on the presence or absence of the <code>-q</code> or <code>-F</code> and <code>-j</code> option three output formats need to be differentiated.</p>
<h3><code>Default Format (without -q, -F and -j)</code></h3>
<p> For each host one line is printed. The output consists of consisting of</p>
<dl>
<dt>&bull;</p>
<dd> the Hostname</p>
<dt>&bull;</p>
<dd> the Architecture.</p>
<dt>&bull;</p>
<dd> the Number of processors.</p>
<dt>&bull;</p>
<dd> the Load.</p>
<dt>&bull;</p>
<dd> the Total Memory.</p>
<dt>&bull;</p>
<dd> the Used Memory.</p>
<dt>&bull;</p>
<dd> the Total Swapspace.</p>
<dt>&bull;</p>
<dd> the Used Swapspace.</dl>
<p> More details can be found in </p>
<p> If the <code>-q</code> option is supplied, each host status line also contains extra lines for every queue hosted by the host consisting of,</p>
<dl>
<dt>&bull;</p>
<dd> the queue name,</p>
<dt>&bull;</p>
<dd> the queue type &#8211; one of B(atch), I(nteractive), or a combination thereof,</p>
<dt>&bull;</p>
<dd> the number of reserved (by advance reservation, not resource reservation), used and, available (according to the queue&#8217;s <code>slots</code> parameter) job slots,</p>
<dt>&bull;</p>
<dd> the state of the queue &#8211; one of u(nknown), a(larm), A(larm), C(alendar suspended), s(uspended), S(ubordinate), d(isabled), D(isabled), E(rror), (c)configuration ambiguous, (o)rphaned, (P)reempted, or some combinations thereof. See section &quot;Full Format&quot; in for explanation of the status flags.</dl>
<p> If the <code>-F</code> option was used, resource availability information is printed following the host status line. For each resource (as selected in an option argument to <code>-F</code> or for all resources if the option argument was omitted) a single line is displayed with the following format:</p>
<dl>
<dt>&bull;</p>
<dd> a one letter specifier indicating whether the current resource availability value was dominated by either<br />
 `<code>g</code>&#8216; &#8211; a cluster global,<br />
 `<code>h</code>&#8216; &#8211; a host total or</p>
<dt>&bull;</p>
<dd> a second one letter specifier indicating the source for the current resource availability value, being one of<br />
 `<code>l</code>&#8216; &#8211; a load value reported for the resource,<br />
 `<code>L</code>&#8216; &#8211; a load value for the resource after administrator defined load scaling has been applied,<br />
 `<code>c</code>&#8216; &#8211; availability derived from the consumable resources facility (see<br />
 `<code>f</code>&#8216; &#8211; a fixed availability definition derived from a non-consumable complex attribute or a fixed resource limit.</p>
<dt>&bull;</p>
<dd> after a colon the name of the resource on which information is displayed.</p>
<dt>&bull;</p>
<dd> after an equal sign the current resource availability value.</dl>
<p> The displayed availability values and the sources from which they derive are always the minimum values of all possible combinations. Hence, for example, a line of the form &quot;qf:h_vmem=4G&quot; indicates that a queue currently has a maximum availability in virtual memory of 4 Gigabyte, where this value is a fixed value (e.g. a resource limit in the queue configuration) and it is queue dominated, i.e. the host in total may have more virtual memory available than this, but the queue doesn&#8217;t allow for more. Contrarily a line &quot;hl:h_vmem=4G&quot; would also indicate an upper bound of 4 Gigabyte virtual memory availability, but the limit would be derived from a load value currently reported for the host. So while the queue might allow for jobs with higher virtual memory requirements, the host on which this particular queue resides currently only has 4 Gigabyte available. </p>
<p> After the queue status line (in case of <code>-j</code>) a single line is printed for each job running currently in this queue. Each job status line contains</p>
<dl>
<dt>&bull;</p>
<dd> the job ID,</p>
<dt>&bull;</p>
<dd> the job name,</p>
<dt>&bull;</p>
<dd> the job owner name,</p>
<dt>&bull;</p>
<dd> the status of the job &#8211; one of t(ransfering), r(unning), R(estarted), s(uspended), S(uspended) or T(hreshold) (see the <code>Reduced Format</code> section for detailed information),</p>
<dt>&bull;</p>
<dd> the start date and time and the function of the job (MASTER or SLAVE &#8211; only meaningful in case of a parallel job) and</p>
<dt>&bull;</p>
<dd> the priority of the jobs.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qhost </i> uses (in the order of precedence): </p>
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
<dt><a href="#lbAH">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAI">FILES</a></p>
<dd>
<dt><a href="#lbAJ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAK">COPYRIGHT</a></p>
<dd></dl>
