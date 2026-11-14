---
title: "condor_updates_stats(1)"
name: "condor_updates_stats"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_updates_stats/"
description: "condor_updates_stats Display output from condor_status"
---

<h2>Name</h2>
<p> <i>condor_updates_stats</i> Display output from <i>condor_status</i> </p>
<h2>Synopsis</h2>
<p> <i>condor_updates_stats</i> [ &#8212; <code>help</code><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> <code>h</code> ] [ &#8212; <code>version</code> ] </p>
<p> <i>condor_updates_stats</i> [ &#8212; <code>long</code><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> <code>l</code> ] [ &#8212; <code>history=&lt;min&gt;-&lt;max&gt;</code> ] [ &#8212; <code>interval=&lt;seconds&gt;</code> ] [ &#8212; <code>notime</code> ] [ &#8212; <code>time</code> ] [ &#8212; <code>summary</code><br />
&nbsp;<wbr>&#8211;&nbsp;<wbr> <code>s</code> ] </p>
<h2>Description</h2>
<p> <i>condor_updates_stats</i> parses the output from <i>condor_status</i> , and it displays the information relating to update statistics in a useful format. The statistics are displayed with the most recent update first; the most recent update is numbered with the smallest value. </p>
<p> The number of historic points that represent updates is configurable on a per-source basis by configuration variable COLLECTOR_DAEMON_HISTORY_SIZE . </p>
<h2>Options</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display usage information and exit.</p>
<dt>
<dd></dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Same as <code>&#8211;help</code> .</p>
<dt>
<dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display HTCondor version information and exit.</p>
<dt>
<dd></dl>
<p> <code>&#8211;long</code></p>
<dl>
<dt>
<dd> All update statistics are displayed. Without this option, the statistics are condensed.</p>
<dt>
<dd></dl>
<p> <code>-l</code></p>
<dl>
<dt>
<dd> Same as <code>&#8211;long</code> .</p>
<dt>
<dd></dl>
<p> <code>&#8211;history=&lt;min&gt;-&lt;max&gt;</code></p>
<dl>
<dt>
<dd> Sets the range of update numbers that are printed. By default, the entire history is displayed. To limit the range, the minimum and/or maximum number may be specified. If a minimum is not specified, values from 0 to the maximum are displayed. If the maximum is not specified, all values after the minimum are displayed. When both minimum and maximum are specified, the range to be displayed includes the endpoints as well as all values in between. If no sign is given, command-line parsing fails, and usage information is displayed. If an sign is given, with no minimum or maximum values, the default of the entire history is displayed.</p>
<dt>
<dd></dl>
<p> <code>&#8211;interval=&lt;seconds&gt;</code></p>
<dl>
<dt>
<dd> The assumed update interval, in seconds. Assumed times for the the updates are displayed, making the use of the <code>&#8211;time</code> option together with the <code>&#8211;interval</code> option redundant.</p>
<dt>
<dd></dl>
<p> <code>&#8211;notime</code></p>
<dl>
<dt>
<dd> Do not display assumed times for the the updates. If more than one of the options <code>&#8211;notime</code> and <code>&#8211;time</code> are provided, the final one within the command line parsed determines the display.</p>
<dt>
<dd></dl>
<p> <code>&#8211;time</code></p>
<dl>
<dt>
<dd> Display assumed times for the the updates. If more than one of the options <code>&#8211;notime</code> and <code>&#8211;time</code> are provided, the final one within the command line parsed determines the display.</p>
<dt>
<dd></dl>
<p> <code>&#8211;summary</code></p>
<dl>
<dt>
<dd> Display only summary information, not the entire history for each machine.</p>
<dt>
<dd></dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Same as <code>&#8211;summary</code> .</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_updates_stats</i> will exit with a status value of 0 (zero) upon success, and it will exit with a nonzero value upon failure. </p>
<h2>Examples</h2>
<p> Assuming the default of 128 updates kept, and assuming that the update interval is 5 minutes, <i>condor_updates_stats</i> displays: </p>
<p> $ condor_status -l host1 | condor_updates_stats &#8211;interval=300<br />
 (Reading from stdin)<br />
 *** Name/Machine = &#8216;HOST1.cs.wisc.edu&#8217; MyType = &#8216;Machine&#8217; *** </p>
<p>&nbsp;<wbr>Type: Main </p>
<p>Stats: Total=2277, Seq=2276, Lost=3&nbsp;<wbr>(0.13%) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>@&nbsp;<wbr>Mon Feb 16 12:55:38 2004: Ok </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8230; </p>
<p>&nbsp;<wbr>28&nbsp;<wbr>@&nbsp;<wbr>Mon Feb 16 10:35:38 2004: Missed </p>
<p>&nbsp;<wbr>29&nbsp;<wbr>@&nbsp;<wbr>Mon Feb 16 10:30:38 2004: Ok </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8230; </p>
<p>127&nbsp;<wbr>@&nbsp;<wbr>Mon Feb 16 02:20:38 2004: Ok </p>
<p> Within this display, update numbered 27, which occurs later in time than the missed update numbered 28, is Ok. Each change in state, in reverse time order, displays in this condensed version. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
