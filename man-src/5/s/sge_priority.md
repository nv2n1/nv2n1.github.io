---
title: "sge_priority(5)"
name: "sge_priority"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_priority/"
description: "sge_priority – xxQS_NAMExx job priorities"
---

<p>sge_priority &#8211; xxQS_NAMExx job priorities</p>
<h2>Description</h2>
<p>xxQS_NAMExx provides a means for controlling job dispatch and run-time priorities. The dispatch priority indicates the relative importance of pending jobs and determines the order in which xxQS_NAMExx initially considers dispatching jobs to queue instances, if the relevant resources are available. (The actual running order may be influenced may be influenced by other factors, such as reservations.) The run-time priority determines the CPU allocation that the operating system assigns to jobs.</p>
<h3>Jobs Dispatch Priority</h3>
<p>A job&#8217;s dispatch priority (display in the &quot;reduced&quot; output format of is affected by a number of factors:</p>
<dl>
<dt>&bull;</p>
<dd>the identity of the submitting user;</p>
<dt>&bull;</p>
<dd>the project under which the job is submitted (or alternatively, the default project of the submitting user);</p>
<dt>&bull;</p>
<dd>any resources requested by the job;</p>
<dt>&bull;</p>
<dd>the job&#8217;s submit time;</p>
<dt>&bull;</p>
<dd>the job&#8217;s initiation deadline time (if specified);</p>
<dt>&bull;</p>
<dd>the <code>-p</code> priority specified for the job (also known as the POSIX priority &quot;<i>pprio</i>&quot;).</dl>
<p> The effect of each of these is governed by the overall policy setup, which is split into three top-level contributions. Each of these is configured through the parameters <code>weight_priority</code>, <code>weight_ticket</code> and <code>weight_urgency</code>. These three parameters control to what degree POSIX priority, ticket policy, and urgency policy are in effect. To facilitate interpretation, the raw priorities (&quot;<i>tckts</i>&quot;/&quot;<i>urg</i>&quot;/&quot;<i>ppri</i>&quot;) are normalized (&quot;<i>ntckts</i>&quot;/&quot;<i>nurg</i>&quot;/&quot;<i>npprior</i>&quot;) before they are used to calculate job priorities (&quot;<i>prio</i>&quot;). Normalization maps each raw urgency/ticket/priority value into a range between 0 and 1. </p>
<pre> <i>npprior</i> = normalized(<i>ppri</i>)
 <i>nurg</i> = normalized(<i>urg</i>)
 <i>ntckts</i> = normalized(<i>tckts</i>)
 <i>prio</i> = <i>weight_priority</i> * <i>npprio</i> +
 <i>weight_urgency</i> * <i>nurg</i> +
 <i>weight_ticket</i> * <i>ntckts</i></pre>
<p>The higher a job&#8217;s priority value, the earlier it gets dispatched. The urgency policy defines an urgency value for each job. The urgency value </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>urg</i>&nbsp;=&nbsp;<wbr>&nbsp;<i>rrcontr</i>&nbsp;+&nbsp;<i>wtcontr</i>&nbsp;+&nbsp;<i>dlcontr</i><br />
 consists of the resource requirement contribution (<i>rrcontr</i>), the waiting time contribution (<i>wtcontr</i>) and the deadline contribution (<i>dlcontr</i>). The resource requirement contribution adds up all resource requirements of a job into a single numeric value. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>rrcontr</i>&nbsp;=&nbsp;Sum over all(<i>hrr</i>)<br />
 with an <i>hrr</i> for each hard resource request. Depending on the resource type, two different methods are used to determine the value to be used for <i>hrr</i> here. For numeric type resource requests, the <i>hrr</i> represents how much of a resource a job requests (on a per-slot basis for PE jobs) and how &quot;important&quot; this resource is considered in comparison to other resources. This is expressed by the formula: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>hrr</i>&nbsp;=&nbsp;<i>rurg</i>&nbsp;*&nbsp;<i>assumed_slot_allocation</i>&nbsp;*&nbsp;<i>request</i><br />
 where the resource&#8217;s urgency value (<i>rurg</i>) is as specified under <code>urgency</code> in the job&#8217;s <i>assumed_slot_allocation</i> represents the number of slots supposedly assigned to the job, and the per-slot request is that which was specified using the <code>-l</code> option. For string-type requests the formula is simply </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>hrr</i>&nbsp;=&nbsp;<i>rurg</i><br />
 and directly assigns the resource urgency value as specified under <code>urgency</code> in The waiting time contribution represents a weighted waiting time of the jobs </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Fiwtcontr&nbsp;=&nbsp;<i>waiting_time</i>&nbsp;*&nbsp;<i>weight_waiting_time</i><br />
 with the waiting time in seconds and the <i>weight_waiting_time</i> value as specified in The deadline contribution has an increasing effect as jobs approach their deadline initiation time (see the <code>-dl</code> option in It is defined as the quotient of the <code>weight_deadline</code> value from and the (steadily decreasing) free time in seconds until deadline initiation time </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Fidlcontr&nbsp;=&nbsp;<i>weight_deadline</i>&nbsp;/&nbsp;<i>free_time</i><br />
 or is set to 0 for non-deadline jobs. After the deadline passes, the value is static and equal to <code>weight_deadline</code>. The <code>-urg</code> option displays urgency information for jobs. The ticket policy unites functional, override and share tree policies in the ticket value (<i>tckts</i>), defined as the sum of the specific ticket values (<i>ftckt</i>/<i>otckt</i>/<i>stckt</i>) for each sub-policy (functional, override, share): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Fitckts&nbsp;=&nbsp;<i>ftckt</i>&nbsp;+&nbsp;<i>otckt</i>&nbsp;+&nbsp;<i>stckt</i> The ticket policies provide a broad range of means for influencing both job dispatch and runtime priorities on a per job, per user, per project, and per department basis. The <code>-ext</code> option displays ticket information for jobs.</p>
<h3>Job Run-Time Priority</h3>
<p>The run-time priority can be dynamically adjusted in order to meet the goals set with the ticket policy when execution hosts are over-subscribed. Dynamic run-time priority adjustment can be turned on globally using <code>reprioritize</code> in and <code>reprioritize_interval</code> in If no dynamic run-time priority adjustment is done at a host level, the <code>priority</code> specification in is in effect. Note that urgency and POSIX priorities do <code>not</code> affect runtime priority. </p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
