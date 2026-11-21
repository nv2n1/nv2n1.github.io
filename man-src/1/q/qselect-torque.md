---
title: "qselect-torque(1)"
name: "qselect-torque"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qselect-torque/"
description: "qselect – select pbs batch jobs"
---

<h2 class="name">NAME</h2>
<p> qselect &#8211; select pbs batch jobs </p>
<h2>SYNOPSIS</h2>
<p> qselect [-a [op]date_time] [-A account_string] [-e] [-c [op]interval] [-h hold_list] [-l resource_list] [-N name] [-p [op]priority] [-q destination] [-r rerun] [-s states] [-u user_list]</p>
<h2>DESCRIPTION</h2>
<p> The <code>qselect</code> command provides a method to list the job identifier of those jobs which meet a list of selection criteria. Jobs are selected from those owned by a single server. </p>
<p> When qselect successfully completes, it will have written to standard output a list of zero or more jobs which meet the criteria specified by the options. Each option acts as a filter restricting the number of jobs which might be listed. With no options, the qselect command will list all jobs at the server which the user is authorized to list (query status of). The -u option may be used to limit the selection to jobs owned by this user or other specified users.</p>
<h2>OPTIONS</h2>
<p> When an option is specified with a optional <i> component to the option argument, then specifies a relation between the value of a certain job attribute and the value component of the option argument. If an is allowable on an option, then the description of the option letter will indicate the is allowable. The only acceptable strings for the component, and the relation the string indicates, are shown in the following list:</p>
<dl>
<dl>
<dt>.eq.</dt>
<dd> the value represented by the attribute of the job is equal to the value represented by the option argument.</dd>
<dt>.ne.</dt>
<dd> the value represented by the attribute of the job is not equal to the value represented by the option argument.</dd>
<dt>.ge.</dt>
<dd> the value represented by the attribute of the job is greater than or equal to the value represented by the option argument.</dd>
<dt>.gt.</dt>
<dd> the value represented by the attribute of the job is greater than the value represented by the option argument.</dd>
<dt>.le.</dt>
<dd> the value represented by the attribute of the job is less than or equal to the value represented by the option argument.</dd>
<dt>.lt.</dt>
<dd> the value represented by the attribute of the job is less than the value represented by the option argument.</dd></dl>
</dl>
<dl>
<dt>-a [op]date_time</dt>
<dd> Restricts selection to a specific time, or a range of times.</dd>
<dt>
</dt><dd> The qselect command selects only jobs for which the value of the </i><font SIZE="-1"><i> attribute is related to the argument by the optional operator. The argument is in the form of the date_time operand of the </i><code><a href="/docs/linux/man/1-touch/">touch</a></code>(1) command: <code><br />
 where the MM is the two digits for the month, DD is the day of the month, hh is the hour, mm is the minute, and the optional SS is the seconds. CC is the century and YY the year.</dd>
<dt>
</dt><dd> If </code><i> is not specified, jobs will be selected for which the </i></font><font SIZE="-2"><i> and values are equal. If is specified, jobs will be selected according to the following definitions:</dd>
<dl>
<dl>
<dt>.eq.</dt>
<dd> </i></font><font SIZE="-3"><i> attribute is equal to the argument.</dd>
<dt>.ne.</dt>
<dd> </i></font><font SIZE="-4"><i> attribute is not equal to the argument.</dd>
<dt>.ge.</dt>
<dd> </i></font><font SIZE="-5"><i> attribute is greater than (after) or equal to the argument.</dd>
<dt>.gt.</dt>
<dd> </i></font><font SIZE="-6"><i> attribute is greater than (after) the argument.</dd>
<dt>.le.</dt>
<dd> </i></font><font SIZE="-7"><i> attribute is less than (before) or equal to the argument.</dd>
<dt>.lt.</dt>
<dd> </i></font><font SIZE="-8"><i> attribute is less than (before) the argument.</dd></dl>
</dl>
<dt>-e</dt>
<dd> Restricts selection to jobs in execution queues.</dd>
<dt>-A account_string</dt>
<dd> Restricts selection to jobs whose </i></font><font SIZE="-9"><i> attribute matches the specified</dd>
<dt>-c [op]interval</dt>
<dd> Restricts selection to jobs whose interval attribute matches the specified relationship.</dd>
<dt>
</dt><dd> The values of the attribute are defined to have the following ordered relationship:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>n&nbsp;<wbr>&gt;&nbsp;<wbr> s&nbsp;<wbr>&gt;&nbsp;<wbr>c=minutes&nbsp;<wbr>&gt;&nbsp;<wbr>c&nbsp;<wbr>&gt;&nbsp;<wbr>u<br />
 If the optional is not specified, jobs will be selected whose attribute is equal to the argument. If is specified, jobs will be selected according to:</dd>
<dl>
<dl>
<dt>.eq.</dt>
<dd> attribute of the job is equal to the argument.</dd>
<dt>.ne.</dt>
<dd> attribute of the job is not equal to the argument.</dd>
<dt>.ge.</dt>
<dd> attribute of the job is greater than or equal to the argument.</dd>
<dt>.gt.</dt>
<dd> attribute of the job is greater than the argument.</dd>
<dt>.le.</dt>
<dd> attribute of the job is less than or equal to the argument.</dd>
<dt>.lt.</dt>
<dd> attribute of the job is less than the argument.</dd></dl>
</dl>
<dt>
</dt><dd> For an interval value of &quot;u&quot;, only &quot;.eq.&quot; and &quot;.ne.&quot; are valid.</dd>
<dt>-h hold_list</dt>
<dd> Restricts the selection of jobs to those with a specific set of hold types. Only those jobs will be selected whose attribute exactly match the value of the argument.</dd>
<dl>
<dt>
</dt><dd>
<p> The argument is a string consisting of one or more occurrences the single letter </i><code> or one or more of the letters or in any combination. If letters are duplicated, they are treated as if they occurred once. The letters represent the hold types: </code></font></p>
<pre>
  <code>n</code> - none
  <code>u</code> - user
  <code>o</code> - other
  <code>s</code> - system
</pre>
</dd></dl>
<dt>-l resource_list</dt>
<dd> Restricts selection of jobs to those with specified resource amounts.</dd>
<dl>
<dt>
</dt><dd>
<p> Only those jobs will be selected whose <i> </i><font SIZE="-1"><i> attribute matches the specified relation with each resource and value listed in the argument. The is in the following format:<br />
 resource_name</i><code>op</code>value[,resource_name<code>op</code>val,&#8230;]<br />
 The relation operator <i> must be present. </p>
<p> When comparing the values of resources, the following definitions for the operator apply:</p>
</dd><dl>
<dt>.eq.</dt>
<dd> the resource value in the </i></font><font SIZE="-2"><i> attribute of the job equals the value specified in</dd>
<dt>.ne.</dt>
<dd> the resource value in the </i></font><font SIZE="-3"><i> attribute of the job is not equal to the value specified in</dd>
<dt>.ge.</dt>
<dd> the resource value in the </i></font><font SIZE="-4"><i> attribute of the job is greater than or equal to the value specified in</dd>
<dt>.gt.</dt>
<dd> the resource value in the </i></font><font SIZE="-5"><i> attribute of the job is greater than the value specified in</dd>
<dt>.le.</dt>
<dd> the resource value in the </i></font><font SIZE="-6"><i> attribute of the job is less than or equal to the value specified in</dd>
<dt>.lt.</dt>
<dd> the resource value in the </i></font><font SIZE="-7"><i> attribute of the job is less than the value specified in</dd></dl>
</dl>
<dt>-N name</dt>
<dd> Restricts selection of jobs to those with a specific name.</dd>
<dt>-p [op]priority</dt>
<dd> Restricts selection of jobs to those with a priority that matches the specified relationship. If is not specified, jobs are selected for which the job </i></font><font SIZE="-8"><i> attribute is equal to the</dd>
<dl>
<dt>
</dt><dd>
<p> If the is specified, the relationship is defined as:</p>
</dd><dl>
<dt>.eq.</dt>
<dd> </i></font><font SIZE="-9"><i> attribute is equal to the value of the argument.</dd>
<dt>.ne.</dt>
<dd> attribute is not equal to the value of the argument.</dd>
<dt>.ge.</dt>
<dd> attribute is greater than or equal to the value of the argument.</dd>
<dt>.gt.</dt>
<dd> attribute is greater than the value of the argument.</dd>
<dt>.le.</dt>
<dd> attribute is less than or equal to the value of the argument.</dd>
<dt>.lt.</dt>
<dd> attribute is less than the value of the argument.</dd></dl>
</dl>
<dt>-q destination</dt>
<dd> Restricts selection to those jobs residing at the specified destination.</dd>
<dl>
<dt>
</dt><dd>
<p> The may be of one of the following three forms:<br />
 </i><code> </p>
<p> If the </code><i> option is not specified, jobs will be selected from the default server. </p>
<p> If the describes only a queue, only jobs in that queue on the default batch server will be selected. </p>
<p> If the describes only a server, then jobs in all queues on that server will be selected. </p>
<p> If the describes both a queue and a server, then only jobs in the named queue on the named server will be selected.</dd></dl>
<dt>-r rerun</dt>
<dd> Restricts selection of jobs to those with the specified attribute. The option argument must be a single character. The following two characters are supported by PBS: </i><code> and</dd>
<dt>-s states</dt>
<dd> Restricts job selection to those in the specified states.</dd>
<dl>
<dt>
</dt><dd>
<p> The </code><i> argument is a character string which consists of any combination of the characters: </i><code> and </p>
<p> The characters in the </code><i> argument have the following interpretation:</p>
</dd><dl>
<dt></i><code>E</code></dt>
<dd> the Exiting state.</dd>
<dt><code>H</code></dt>
<dd> the Held state.</dd>
<dt><code>Q</code></dt>
<dd> the Queued state.</dd>
<dt><code>R</code></dt>
<dd> the Running state.</dd>
<dt><code>T</code></dt>
<dd> the Transiting state.</dd>
<dt><code>W</code></dt>
<dd> the Waiting state.</dd></dl>
<p> Jobs will be selected which are in any of the specified states.</dl>
<dt>-u user_list</dt>
<dd> Restricts selection to jobs owned by the specified user names.</dd>
<dl>
<dt>
</dt><dd>
<p> This provides a means of limiting the selection to jobs owned by one or more users. </p>
<p> The syntax of the <i> is:<br />
 </i><code><br />
 Host names may be wild carded on the left end, e.g. &quot;*.nasa.gov&quot;. User_name without a &quot;@host&quot; is equivalent to &quot;user_name@*&quot;, that is at any host. Jobs will be selected which are owned by the listed users at the corresponding hosts.</dd></dl>
</dl>
<p> </code></font></p>
<h2>STANDARD OUTPUT</h2>
<p> The list of job identifiers of selected jobs is written to standard output. Each job identifier is separated by white space. Each job identifier is of the form:<br />
 <code><br />
 Where is the identifier assigned at submission time, see qsub</code>. <code> identifies the server which currently owns the job. </code></p>
<h2>STANDARD ERROR</h2>
<p> The qselect command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all options presented to the qselect command, the exit status will be a value of zero. </p>
<p> If the qselect command fails to process any option, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> qsub(1B), qstat(1B), pbs_selectjob(3B), pbs_selstat(3B), pbs_statjob(3B) </p>
