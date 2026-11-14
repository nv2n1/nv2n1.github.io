---
title: "qhold-ge(1)"
name: "qhold-ge"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qhold-ge/"
description: "qhold – hold back Grid Engine jobs from execution"
---

<h2>NAME</h2>
<p> qhold &#8211; hold back Grid Engine jobs from execution</p>
<h2>SYNTAX</h2>
<p> <code>qhold</code> [ <code>-h</code> {<code>u</code>|<code>o</code>|<code>s</code>},&#8230; ] [ <code>-help</code> ] [ <code>job/task_id_list</code> ] </p>
<p> <code>qhold</code> [ <code>-h</code> {<code>u</code>|<code>o</code>|<code>s</code>},&#8230; ] [ <code>-help</code> ] <code>-u user_list </code></p>
<h2>DESCRIPTION</h2>
<p> <i>Qhold</i> provides a means for a user/operator/manager to place so called <i>holds</i> on one or more jobs pending to be scheduled for execution. As long as any type of hold is assigned to a job, the job is not eligible for scheduling. </p>
<p> Holds can be removed with the or the command. </p>
<p> There are three different types of holds:</p>
<dl>
<dt><code>user</code></p>
<dd> User holds can be assigned and removed by managers, operators and the owner of the jobs.</p>
<dt><code>operator</code></p>
<dd> Operator holds can be assigned and removed by managers and operators.</p>
<dt><code>system</code></p>
<dd> System holds can be assigned and removed by managers only.</dl>
<p> If no hold type is specified with the <code>-h</code> option (see below) the user hold is assumed by default. </p>
<p> An alternate way to assign holds to jobs is the or the command (see the <i>-h</i> option).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> {<code>u</code>|<code>o</code>|<code>s</code>},&#8230;</p>
<dd> Assign a u(ser), o(perator) or s(system) hold or a combination thereof to one or more jobs.</p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-u username,&#8230;</code></p>
<dd> Changes are only made on those jobs which were submitted by users specified in the list of usernames. Managers are allowed to use the <code>qhold -u &quot;*&quot;</code> command to set a hold for all jobs of all users. </p>
<p> If a user uses the <code>-u</code> switch, the user may specify an additional <i>job/task_id_list</i>.</p>
<dt><code>job/task_id_list</code></p>
<dd> Specified by the following form: </p>
<p>&nbsp;<wbr><i>job_id[.task_range][,job_id[.task_range],&#8230;]</i> </p>
<p> If present, the <i>task_range</i> restricts the effect of the <i>qhold</i> operation to the array job task range specified as suffix to the job id (see the <code>-t</code> option to for further details on array jobs). </p>
<p> The task range specifier has the form n[-m[:s]]. The range may be a single number, a simple range of the form n-m or a range with a step size. </p>
<p> Instead of <i>job/task_id_list</i> it is possible to use the keyword &#8216;all&#8217; to modify the hold state for all jobs of the current user.</dl>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><code>GE_ROOT</code></p>
<dd> Specifies the location of the Grid Engine standard configuration files.</p>
<dt><code>GE_CELL</code></p>
<dd> If set, specifies the default Grid Engine cell. To address a Grid Engine cell <i>qhold</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable GE_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>GE_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>GE_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</dl>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
