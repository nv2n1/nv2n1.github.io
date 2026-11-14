---
title: "gm-jobs(8)"
name: "gm-jobs"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gm-jobs/"
description: "gm-jobs – displays information and manages current jobs handled by ARC middleware"
---

<p>gm-jobs &#8211; displays information and manages current jobs handled by ARC middleware </p>
<h2>Description</h2>
<p><code>gm-jobs</code> displays information related to jobs handled by locally running ARC middleware service A-REX. Different kind of information may be selected by using various options. This utility also can perform simple management operations &#8211; currently cancel processing of specific jobs and remove them. Default behavior is to print minimal information about all jobs currently handled by A-REX and some statistics. </p>
<h2>Synopsis</h2>
<p>gm-jobs [OPTION&#8230;] </p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Show help for available options</p>
<dt><code>-l, &#8211;longlist</code></p>
<dd>display more information about each job</p>
<dt><code>-c, &#8211;conffile=file</code></p>
<dd>use specified configuration file</p>
<dt><code>-d, &#8211;controldir=dir</code></p>
<dd>read information from specified control directory</p>
<dt><code>-s, &#8211;showshares</code></p>
<dd>print summary of jobs in each transfer share. Shows for input (preparing) and output (finishing) files the number of files being copied and the number queued per transfer share</p>
<dt><code>-J, &#8211;notshowjobs</code></p>
<dd>do not print list of jobs (printed by default)</p>
<dt><code>-S, &#8211;notshowstates</code></p>
<dd>do not print number of jobs in each state (printed by default)</p>
<dt><code>-w, &#8211;showservice</code></p>
<dd>print state of the service</p>
<dt><code>-f, &#8211;filteruser=dn</code></p>
<dd>show only jobs of user(s) with specified subject name(s)</p>
<dt><code>-k, &#8211;killjob=id</code></p>
<dd>request to cancel job(s) with specified ID(s)</p>
<dt><code>-K, &#8211;killuser=dn</code></p>
<dd>request to cancel jobs belonging to user(s) with specified subject name(s)</p>
<dt><code>-r, &#8211;remjob=id</code></p>
<dd>request to clean job(s) with specified ID(s)</p>
<dt><code>-R, &#8211;remuser=dn</code></p>
<dd>request to clean jobs belonging to user(s) with specified subject name(s)</p>
<dt><code>-j, &#8211;filterjob=id</code></p>
<dd>show only jobs with specified ID(s)</p>
<dt><code>-e, &#8211;listdelegs</code></p>
<dd>print list of available delegation IDs</p>
<dt><code>-E, &#8211;showdeleg=id</code></p>
<dd>print delegation token of specified ID(s) </p>
</dl>
<h2>Author</h2>
<p>Aleksandr Konstantinov &lt;aleksandr dot konstantinov at fys dot uio dot no&gt;</p>
