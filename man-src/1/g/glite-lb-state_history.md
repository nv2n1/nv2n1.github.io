---
title: "glite-lb-state_history(1)"
name: "glite-lb-state_history"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-lb-state_history/"
description: "glite-lb-state_history – utility to show job state changes stored in Logging and Bookkeeping"
---

<h2 class="name">NAME</h2>
<p> glite-lb-state_history &#8211; utility to show job state changes stored in Logging and Bookkeeping </p>
<h2>SYNOPSIS</h2>
<p> <code>glite-lb-state_history</code> [<code>-f</code> <i>FIELDS</i>] <i>JOBID</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>glite-lb-state_history</code> shows the job state changes from the events stored in Logging and Bookkeeping. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code> <i>FIELDS</i></p>
<dd> Job status fields to show in the history listing. </p>
<p> Basic information always shown:<br />
&nbsp;<wbr>&nbsp;<wbr><code>event name</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>jobid</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>job status</code> </p>
<p> Fields shown by default:<br />
&nbsp;<wbr>&nbsp;<wbr><code>network_server</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>jdl:VirtualOrganisation</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>destination</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>done_code</code><br />
&nbsp;<wbr>&nbsp;<wbr><code>reason</code> </p>
</dl>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>AUTHORS</h2>
<p> L&amp;B Product Team, CESNET. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-glite-lb-mon/">glite-lb-mon</a></code>(1), <code><a href="/docs/linux/man/1-glite-lb-statistics/">glite-lb-statistics</a></code>(1) </p>
<h2>Index</h2>
