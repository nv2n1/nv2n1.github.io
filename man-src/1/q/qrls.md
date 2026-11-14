---
title: "qrls(1)"
name: "qrls"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qrls/"
description: "qrls – release xxQS_NAMExx jobs from previous hold states"
---

<h2 class="name">NAME</h2>
<p> qrls &#8211; release xxQS_NAMExx jobs from previous hold states </p>
<h2>SYNTAX</h2>
<p> <code>qrls</code> [ <code>-h</code> {<code>u</code>|<code>o</code>|<code>s</code>},&#8230; ] [ <code>-help</code> ] [ <code>job/task_id_list</code> ] </p>
<p> <code>qrls</code> [ <code>-h</code> {<code>u</code>|<code>o</code>|<code>s</code>},&#8230; ] [ <code>-help</code> ] <code>-u user_list</code></p>
<h2>DESCRIPTION</h2>
<p> <i>Qrls</i> provides a means for a user/operator/manager to release so called <i>holds</i> from one or more jobs pending to be scheduled for execution. As long as any type of hold is assigned to a job, the job is not eligible for scheduling. </p>
<p> Holds can be assigned to jobs with the or the command. </p>
<p> There are three different types of holds:</p>
<dl>
<dt><code>user</code></p>
<dd> User holds can be assigned and removed by managers, operators and the owner of the jobs.</p>
<dt><code>operator</code></p>
<dd> Operator holds can be assigned and removed by managers and operators.</p>
<dt><code>system</code></p>
<dd> System holds can be assigned and removed by managers only.</dl>
<p> If no hold type is specified with the <code>-h</code> option (see below) the user hold is assumed by default. </p>
<p> An alternate way to release holds is the command (see the <i>-h</i> option).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> {<code>u</code>|<code>o</code>|<code>s</code>},&#8230;</p>
<dd> Releases a u(ser), o(perator) or s(system) hold or a combination thereof from one or more jobs.</p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-u username,&#8230;</code></p>
<dd> Modifies the hold state of those jobs which were submitted by users specified in the list of usernames. Managers are allowed to use the <code>qrls -u &quot;*&quot;</code> command to modify the hold state for jobs of all users. </p>
<p> If a user uses the <code>-u</code> switch, the user may specify an additional <i>job/task_id_list</i>.</p>
<dt><code>job/task_id_list</code></p>
<dd> Specified by the following form: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>job_id[.task_range][,job_id[.task_range],&#8230;]</i> </p>
<p> If present, the <i>task_range</i> restricts the effect of the operation to the array job task range specified as suffix to the job id (see the <code>-t</code> option to for further details on array jobs). </p>
<p> The task range specifier has the form n[-m[:s]]. The range may be a single number, a simple range of the form n-m or a range with a step size. </p>
<p> Instead of <i>job/task_id_list</i> it is possible to use the keyword &#8216;all&#8217; to modify all jobs of the current user.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qrls</i> uses (in the order of precedence): </p>
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
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
