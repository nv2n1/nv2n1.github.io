---
title: "nqs2pbs(1)"
name: "nqs2pbs"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nqs2pbs/"
---

<h2 class="name">NAME</h2>
 

 nqs2pbs - convert NQS job scripts to PBS 

<h2>SYNOPSIS</h2>

 nqs2pbs nqs_script [pbs_script]

<h2>DESCRIPTION</h2>

 This utility converts a existing NQS job script to work with PBS and NQS. The existing script is copied and PBS directives, <i>#PBS ,</i> are inserted prior to each NQS directive <i>#QSUB </i> or <i>#@$ ,</i> in the original script. 

 Certain NQS date specification and options are not supported by PBS. A warning message will be displayed indicating the problem and the line of the script on which it occurred. 

 If any unrecognizable NQS directives are encountered, an error message is displayed. The new PBS script will be deleted if any errors occur.

<h2>OPERANDS</h2>

<dl>
<dt>nqs_script
<dd> Specifies the file name of the NQS script to convert. This file is not changed.
<dt>pbs_script
<dd> If specified, it is the name of the new PBS script. If not specified, the new file name is <i>nqs_script.new .</i></dl>
 

<h2>NOTES</h2>

 Converting NQS date specifications to the PBS form may result in a warning message and an incompleted converted date. PBS does not support date specifications of &quot;today&quot;, &quot;tomorrow&quot;, or the name of the days of the week such as &quot;Monday&quot;. If any of these are encountered in a script, the PBS specification will contain only the time portion of the NQS specification, i.e. #PBS -a hhmm[.ss]. It is suggested that you specify the execution time on the qsub command line rather than in the script. 

 Note that PBS will interpret a time specification without a date in the following way:
<dl>
<dt>-
<dd> If the time specified has not yet been reached, the job will become eligible to run at that time today.
<dt>-
<dd> If the specified time has already passed when the job is submitted, the job will become eligible to run at that time tomorrow.</dl>
 

 PBS does not support time zone identifiers. All times are taken as local time.

<h2>SEE ALSO</h2>

 <a HREF="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B) 

<h2>Index</h2>


