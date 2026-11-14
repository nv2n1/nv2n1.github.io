---
title: "condor_advertise(1)"
name: "condor_advertise"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_advertise/"
description: "condor_advertise Send a ClassAd to the condor_collector daemon"
---

<h2>Name</h2>
<p> <i>condor_advertise</i> Send a ClassAd to the <i>condor_collector</i> daemon </p>
<h2>Synopsis</h2>
<p> <i>condor_advertise</i> [ <code>-help -version</code> ] </p>
<p> <i>condor_advertise</i> [ <code>-pool </code> <i>centralmanagerhostname[:portname]</i> ] [ <code>-debug</code> ] [ <code>-tcp</code> ] [ <code>-multiple</code> ] <i>update-command</i> [ <i>classad-filename</i> ] </p>
<h2>Description</h2>
<p> <i>condor_advertise</i> sends one or more ClassAds to the <i>condor_collector</i> daemon on the central manager machine. The required argument <i>update-command</i> says what daemon type&#8217;s ClassAd is to be updated. The optional argument <i>classad-filename</i> is the file from which the ClassAd(s) should be read. If <i>classad-filename</i> is omitted or is the dash character (&#8216;-&#8216;), then the ClassAd(s) are read from standard input. </p>
<p> When <code>-multiple</code> is specified, multiple ClassAds may be published. Publishing many ClassAds in a single invocation of <i>condor_advertise</i> is more efficient than invoking <i>condor_advertise</i> once per ClassAd. The ClassAds are expected to be separated by one or more blank lines. When <code>-multiple</code> is not specified, blank lines are ignored (for backward compatibility). It is best not to rely on blank lines being ignored, as this may change in the future. </p>
<p> The <i>update-command</i> may be one of the following strings: </p>
<p> <code>UPDATE_STARTD_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_SCHEDD_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_MASTER_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_GATEWAY_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_CKPT_SRVR_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_NEGOTIATOR_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_HAD_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_AD_GENERIC</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_SUBMITTOR_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_COLLECTOR_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_LICENSE_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UPDATE_STORAGE_AD</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>condor_advertise</i> can also be used to invalidate and delete ClassAds currently held by the <i>condor_collector</i> daemon. In this case the <i>update-command</i> will be one of the following strings: </p>
<p> <code>INVALIDATE_STARTD_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_SCHEDD_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_MASTER_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_GATEWAY_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_CKPT_SRVR_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_NEGOTIATOR_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_HAD_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_ADS_GENERIC</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_SUBMITTOR_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_COLLECTOR_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_LICENSE_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>INVALIDATE_STORAGE_ADS</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> For any of these INVALIDATE commands, the ClassAd in the required file consists of three entries. The file contents will be similar to: </p>
<p> MyType = &quot;Query&quot;<br />
 TargetType = &quot;Machine&quot;<br />
 Requirements = Name == &quot;condor.example.com&quot; </p>
<p> The definition for MyType is always Query . TargetType is set to the MyType of the ad to be deleted. This MyType is DaemonMaster for the <i>condor_master</i> ClassAd, Machine for the <i>condor_startd</i> ClassAd, Scheduler for the <i>condor_schedd</i> ClassAd, and Negotiator for the <i>condor_negotiator</i> ClassAd. Requirements is an expression evaluated within the context of ads of TargetType . When Requirements evaluates to True , the matching ad is invalidated. A full example is given below. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Display usage information</p>
<dt>
<dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Display version information</p>
<dt>
<dd></dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Print debugging information as the command executes.</p>
<dt>
<dd></dl>
<p> <code>-multiple</code></p>
<dl>
<dt>
<dd> Send more than one ClassAd, where the boundary between ClassAds is one or more blank lines.</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portname]</i></p>
<dl>
<dt>
<dd> Specify a pool by giving the central manager&#8217;s host name and an optional port number. The default is the COLLECTOR_HOST specified in the configuration file.</p>
<dt>
<dd></dl>
<p> <code>-tcp</code></p>
<dl>
<dt>
<dd> Use TCP for communication. Without this option, UDP is used.</p>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<p> The job and machine ClassAds are regularly updated. Therefore, the result of <i>condor_advertise</i> is likely to be overwritten in a very short time. It is unlikely that either HTCondor users (those who submit jobs) or administrators will ever have a use for this command. If it is desired to update or set a ClassAd attribute, the <i>condor_config_val</i> command is the proper command to use. </p>
<p> Attributes are defined in Appendix A of the HTCondor manual. </p>
<p> For those administrators who do need <i>condor_advertise</i> , the following attributes may be included: </p>
<p> <code>DaemonStartTime </code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UpdateSequenceNumber </code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> If both of the above are included, the <i>condor_collector</i> will automatically include the following attributes: </p>
<p> <code>UpdatesTotal </code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UpdatesLost </code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UpdatesSequenced </code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>UpdatesHistory </code></p>
<dl>
<dt>
<dd> Affected by COLLECTOR_DAEMON_HISTORY_SIZE .</p>
<dt>
<dd></dl>
<h2>Examples</h2>
<p> Assume that a machine called condor.example.com is turned off, yet its <i>condor_startd</i> ClassAd does not expire for another 20 minutes. To avoid this machine being matched, an administrator chooses to delete the machine&#8217;s <i>condor_startd</i> ClassAd. Create a file (called remove_file in this example) with the three required attributes: </p>
<p> MyType = &quot;Query&quot;<br />
 TargetType = &quot;Machine&quot;<br />
 Requirements = Name == &quot;condor.example.com&quot; </p>
<p> This file is used with the command: </p>
<p> % condor_advertise INVALIDATE_STARTD_ADS remove_file </p>
<h2>Exit Status</h2>
<p> <i>condor_advertise</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. Success means that all ClassAds were successfully sent to all <i>condor_collector</i> daemons. When there are multiple ClassAds or multiple <i>condor_collector</i> daemons, it is possible that some but not all publications succeed; in this case, the exit status is 1, indicating failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
