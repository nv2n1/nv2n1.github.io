---
title: "pmcd_wait(1)"
name: "pmcd_wait"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmcd_wait/"
description: "pmcd_wait – wait for PMCD to accept client connections"
---

<h2>NAME</h2>
<p> <code>pmcd_wait</code> &#8211; wait for PMCD to accept client connections</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmcd_wait</code> [<code>-h</code> <i>host</i>] [<code>-t</code> <i>interval</i>] [<code>-v</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmcd_wait</code> waits for the Performance Metrics Collector Daemon (PMCD) to be running and accepting client connections. </p>
<p> Unless directed to another host by the <code>-h</code> option, <code>pmcd_wait</code> will try to contact <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on the local host. </p>
<p> <code>pmcd_wait</code> will timeout and abandon the attempt to connect to <code>pmcd</code> after 60 seconds. This default timeout interval may be changed using the <code>-t</code> option, where the <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) and in the simplest form may be an unsigned integer (the implied units in this case are seconds). </p>
<p> On successful connection to <code>pmcd</code> an exit status of zero is returned. </p>
<p> If an error or timeout occurs, then a non-zero exit status is returned as described below. </p>
<p> The other options are as follows:</p>
<dl>
<dt><code>-v</code></p>
<dd> This option turns the verbose mode on. With the verbose mode off (which is the default), no output will be generated. With verbose mode on, error messages will be output on <i>stderr</i>.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> Error messages will be output to <i>stderr</i> only if the verbose mode is on. </p>
<p> The following exit status codes are returned:</p>
<dl>
<dt><code>0</code></p>
<dd> <code>pmcd_wait</code> was able to successfully connect to <code>pmcd</code> within the timeout period.</p>
<dt><code>1</code></p>
<dd> A usage error occurred, use <code>-v</code> for more details.</p>
<dt><code>2</code></p>
<dd> No connection was made in the timeout interval. This will happen if <code>pmcd</code> is running but takes too long to complete the client connection, or if <code>pmcd</code> is not running and all connection attempts in the timeout interval failed with the error ECONNREFUSED.</p>
<dt><code>3</code></p>
<dd> A U<font SIZE="-2">NIX</font> error occurred, use <code>-v</code> for more details.</p>
<dt><code>4</code></p>
<dd> A PCP error occurred, use <code>-v</code> for more details. </p>
</dl>
<h2>Index</h2>
