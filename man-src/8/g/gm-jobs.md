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
<dt><code>-h, &#8211;help</code></dt>
<dd>Show help for available options</dd>
<dt><code>-l, &#8211;longlist</code></dt>
<dd>display more information about each job</dd>
<dt><code>-c, &#8211;conffile=file</code></dt>
<dd>use specified configuration file</dd>
<dt><code>-d, &#8211;controldir=dir</code></dt>
<dd>read information from specified control directory</dd>
<dt><code>-s, &#8211;showshares</code></dt>
<dd>print summary of jobs in each transfer share. Shows for input (preparing) and output (finishing) files the number of files being copied and the number queued per transfer share</dd>
<dt><code>-J, &#8211;notshowjobs</code></dt>
<dd>do not print list of jobs (printed by default)</dd>
<dt><code>-S, &#8211;notshowstates</code></dt>
<dd>do not print number of jobs in each state (printed by default)</dd>
<dt><code>-w, &#8211;showservice</code></dt>
<dd>print state of the service</dd>
<dt><code>-f, &#8211;filteruser=dn</code></dt>
<dd>show only jobs of user(s) with specified subject name(s)</dd>
<dt><code>-k, &#8211;killjob=id</code></dt>
<dd>request to cancel job(s) with specified ID(s)</dd>
<dt><code>-K, &#8211;killuser=dn</code></dt>
<dd>request to cancel jobs belonging to user(s) with specified subject name(s)</dd>
<dt><code>-r, &#8211;remjob=id</code></dt>
<dd>request to clean job(s) with specified ID(s)</dd>
<dt><code>-R, &#8211;remuser=dn</code></dt>
<dd>request to clean jobs belonging to user(s) with specified subject name(s)</dd>
<dt><code>-j, &#8211;filterjob=id</code></dt>
<dd>show only jobs with specified ID(s)</dd>
<dt><code>-e, &#8211;listdelegs</code></dt>
<dd>print list of available delegation IDs</dd>
<dt><code>-E, &#8211;showdeleg=id</code></dt>
<dd>print delegation token of specified ID(s) </dd>
</dl>
<h2>Author</h2>
<p>Aleksandr Konstantinov &lt;aleksandr dot konstantinov at fys dot uio dot no&gt;</p>
