---
title: "condor_stats(1)"
name: "condor_stats"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_stats/"
description: "condor_stats Display historical information about the HTCondor pool"
---

<h2>Name</h2>
<p> <i>condor_stats</i> Display historical information about the HTCondor pool </p>
<h2>Synopsis</h2>
<p> <i>condor_stats</i> [ <code>-f </code> <i>filename</i> ] [ <code>-orgformat</code> ] [ <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i> ] [ <code>time-range</code> ] <i>query-type</i> </p>
<h2>Description</h2>
<p> <i>condor_stats</i> displays historic information about an HTCondor pool. Based on the type of information requested, a query is sent to the <i>condor_collector</i> daemon, and the information received is displayed using the standard output. If the <code>-f</code> option is used, the information will be written to a file instead of to standard output. The <code>-pool</code> option can be used to get information from other pools, instead of from the local (default) pool. The <i>condor_stats</i> tool is used to query resource information (single or by platform), submitter and user information, and checkpoint server information. If a time range is not specified, the default query provides information for the previous 24 hours. Otherwise, information can be retrieved for other time ranges such as the last specified number of hours, last week, last month, or a specified date range. </p>
<p> The information is displayed in columns separated by tabs. The first column always represents the time, as a percentage of the range of the query. Thus the first entry will have a value close to 0.0, while the last will be close to 100.0. If the <code>-orgformat</code> option is used, the time is displayed as number of seconds since the Unix epoch. The information in the remainder of the columns depends on the query type. </p>
<p> Note that logging of pool history must be enabled in the <i>condor_collector</i> daemon, otherwise no information will be available. </p>
<p> One query type is required. If multiple queries are specified, only the last one takes effect. </p>
<h2>Time Range Options</h2>
<p> <code>-lastday</code></p>
<dl>
<dt>
<dd> Get information for the last day.</p>
<dt>
<dd></dl>
<p> <code>-lastweek</code></p>
<dl>
<dt>
<dd> Get information for the last week.</p>
<dt>
<dd></dl>
<p> <code>-lastmonth</code></p>
<dl>
<dt>
<dd> Get information for the last month.</p>
<dt>
<dd></dl>
<p> <code>-lasthours </code> <i>n</i></p>
<dl>
<dt>
<dd> Get information for the n last hours.</p>
<dt>
<dd></dl>
<p> <code>-from </code> <i>m d y</i></p>
<dl>
<dt>
<dd> Get information for the time since the beginning of the specified date. A start date prior to the Unix epoch causes <i>condor_stats</i> to print its usage information and quit.</p>
<dt>
<dd></dl>
<p> <code>-to </code> <i>m d y</i></p>
<dl>
<dt>
<dd> Get information for the time up to the beginning of the specified date, instead of up to now. A finish date in the future causes <i>condor_stats</i> to print its usage information and quit.</p>
<dt>
<dd></dl>
<h2>Query Type Arguments</h2>
<p> The query types that do not list all of a category require further specification as given by an argument. </p>
<p> <code>-resourcequery </code> <i>hostname</i></p>
<dl>
<dt>
<dd> A single resource query provides information about a single machine. The information also includes the keyboard idle time (in seconds), the load average, and the machine state.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-resourcelist</code></p>
<dl>
<dt>
<dd> A query of a single list of resources to provide a list of all the machines for which the <i>condor_collector</i> daemon has historic information within the query&#8217;s time range.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-resgroupquery </code> <i>arch/opsys | &#8220;Total&#8221;</i></p>
<dl>
<dt>
<dd> A query of a specified group to provide information about a group of machines based on their platform (operating system and architecture). The architecture is defined by the machine ClassAd Arch , and the operating system is defined by the machine ClassAd OpSys . The string &#8220;Total&#8221; ask for information about all platforms.</p>
<dt>
<dd> The columns displayed are the number of machines that are unclaimed, matched, claimed, preempting, owner, shutdown, delete, backfill, and drained state.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-resgrouplist</code></p>
<dl>
<dt>
<dd> Queries for a list of all the group names for which the <i>condor_collector</i> has historic information within the query&#8217;s time range.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-userquery </code> <i>email_address/submit_machine</i></p>
<dl>
<dt>
<dd> Query for a specific submitter on a specific machine. The information displayed includes the number of running jobs and the number of idle jobs. An example argument appears as</dl>
<p>&nbsp;<wbr>-userquery jondoe [at] sample.com/onemachine.sample.com</p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-userlist</code></p>
<dl>
<dt>
<dd> Queries for the list of all submitters for which the <i>condor_collector</i> daemon has historic information within the query&#8217;s time range.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-usergroupquery </code> <i>email_address | &#8220;Total&#8221;</i></p>
<dl>
<dt>
<dd> Query for all jobs submitted by the specific user, regardless of the machine they were submitted from, or all jobs. The information displayed includes the number of running jobs and the number of idle jobs.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-usergrouplist</code></p>
<dl>
<dt>
<dd> Queries for the list of all users for which the <i>condor_collector</i> has historic information within the query&#8217;s time range.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-ckptquery </code> <i>hostname</i></p>
<dl>
<dt>
<dd> Query about a checkpoint server given its host name. The information displayed includes the number of MiB received, MiB sent, average receive bandwidth (in KiB/sec), and average send bandwidth (in KiB/sec).</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-ckptlist</code></p>
<dl>
<dt>
<dd> Query for the entire list of checkpoint servers for which the <i>condor_collector</i> has historic information in the query&#8217;s time range.</p>
<dt>
<dd></dl>
<h2>Options</h2>
<p> <code>-f </code> <i>filename</i></p>
<dl>
<dt>
<dd> Write the information to a file instead of the standard output.</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> Contact the specified central manager instead of the local one.</p>
<dt>
<dd></dl>
<p> <code>-orgformat</code></p>
<dl>
<dt>
<dd> Display the information in an alternate format for timing, which presents timestamps since the Unix epoch. This argument only affects the display of <i>resoursequery</i> , <i>resgroupquery</i> , <i>userquery</i> , <i>usergroupquery</i> , and <i>ckptquery</i> .</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_stats</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
