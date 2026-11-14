---
title: "boinc(1)"
name: "boinc"
section: "1"
letter: "b"
url: "/docs/linux/man/1-boinc/"
description: "boinc – The BOINC client program."
---

<h2>NAME</h2>
<p> boinc &#8211; The BOINC client program.</p>
<h2>SYNOPSIS</h2>
<p> <code>boinc</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> The BOINC &quot;client&quot;, <code>boinc</code>, is the heart of BOINC. It controls which project applications are run on your computer, downloading &quot;Tasks&quot; and uploading the resulting files from completed tasks. <code>boinc</code> is usually run in the background, ideally as a daemon. It can then be controlled either by a graphical tool called the BOINC Manager, <code><a href="/docs/linux/man/1-boincmgr/">boincmgr</a></code>(1), or a command-line tool called <code><a href="/docs/linux/man/1-boinccmd/">boinccmd</a></code>(1), by means of Remote Procedure Calls (RPCs) over port 31416. </p>
<p> The BOINC client can be controlled by command-line options, configuration files, and environment variables. Standard usage is simply to start the client running in the background.</p>
<h2>OPTIONS</h2>
<p> These command-line options for <code>boinc</code> can be used to control how BOINC is started. Once the client has started, you should use a separate program, (<code><a href="/docs/linux/man/1-boincmgr/">boincmgr</a></code>(1) or <code><a href="/docs/linux/man/1-boinccmd/">boinccmd</a></code>(1)) which communicates with it by means of Remote Procedure Calls (RPCs).</p>
<h3>GENERAL OPTIONS</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version info.</p>
<dt><code>&#8211;run_cpu_benchmarks</code></p>
<dd> Run the CPU benchmarks.</p>
<dt><code>&#8211;check_all_logins</code></p>
<dd> For idle detection, check remote logins too.</p>
<dt><code>&#8211;daemon</code></p>
<dd> Run as daemon. Will redirect stderr and stdout to syslog.</p>
<dt><code>&#8211;dir </code><i>path</i></p>
<dd> Use given dir as the client working directory.</p>
<dt><code>&#8211;no_gpus</code></p>
<dd> Don&#8217;t check for GPUs.</p>
<dt><code>&#8211;no_info_fetch</code></p>
<dd> Don&#8217;t fetch project list or client version info from boinc.berkeley.edu.</p>
<dt><code>&#8211;skip_cpu_benchmarks</code></p>
<dd> Don&#8217;t run CPU benchmarks.</p>
<dt><code>&#8211;start_delay </code><i>X</i></p>
<dd> Delay starting apps for X secs.</dl>
<h3>PROJECT OPTIONS</h3>
<dl>
<dt><code>&#8211;attach_project </code><i>URL</i><i>key</i></p>
<dd> Attach to a project using URL and authenticator.</p>
<dt><code>&#8211;show_projects</code></p>
<dd> Show attached projects.</p>
<dt><code>&#8211;detach_project </code><i>URL</i></p>
<dd> Detach from project specified by URL.</p>
<dt><code>&#8211;reset_project </code><i>URL</i></p>
<dd> Reset (clear) the projectspecified by URL.</p>
<dt><code>&#8211;update_prefs </code><i>URL</i></p>
<dd> Contact the project specified by URL to update preferences</dl>
<h3>COMMUNICATION OPTIONS</h3>
<dl>
<dt><code>&#8211;allow_remote_gui_rpc</code></p>
<dd> Allow RPC connections from remote hosts.</p>
<dt><code>&#8211;gui_rpc_port </code><i>port</i></p>
<dd> Port for RPCs.</p>
<dt><code>&#8211;no_gui_rpc</code></p>
<dd> Omits creation of a socket as required for the remote control of the client. Consequently the client cannot be controlled by external tools like GUIs (<code>boincmgr</code> etc.) or the console command tool (<code>boinccmd</code>).</dl>
<h3>DEBUGGING OPTIONS</h3>
<dl>
<dt><code>&#8211;abort_jobs_on_exit</code></p>
<dd> When client exits, abort and report tasks.</p>
<dt><code>&#8211;allow_multiple_clients</code></p>
<dd> Allow more than one client instance per host.</p>
<dt><code>&#8211;exit_after_app_start </code><i>N</i></p>
<dd> Exit N seconds after an app starts. Useful to look at the files in the slot directory.</p>
<dt><code>&#8211;exit_after_finish</code></p>
<dd> Exit right after finishing a task. Useful to look at the files in the slot directory.</p>
<dt><code>&#8211;exit_before_start</code></p>
<dd> Exit right before starting a task. Useful to look at the files in the slot directory.</p>
<dt><code>&#8211;exit_before_upload</code></p>
<dd> Exit right before starting an upload.</p>
<dt><code>&#8211;exit_when_idle</code></p>
<dd> Exit when there are no more tasks to work on.</p>
<dt><code>&#8211;fetch_minimal_work</code></p>
<dd> Fetch only 1 task per device.</p>
<dt><code>&#8211;file_xfer_giveup_period </code><i>N</i></p>
<dd> Give up on file transfers after N sec.</p>
<dt><code>&#8211;master_fetch_interval </code><i>N</i></p>
<dd> Limiting the period of project master file dowload retries.</p>
<dt><code>&#8211;master_fetch_period </code><i>N</i></p>
<dd> Reload a project&#8217;s master file after N RPC failures.</p>
<dt><code>&#8211;master_fetch_retry_cap </code><i>N</i></p>
<dd> Exponential backoff limit for downloading project master files.</p>
<dt><code>&#8211;no_priority_change</code></p>
<dd> Run applications at same priority as client.</p>
<dt><code>&#8211;pers_giveup </code><i>N</i></p>
<dd> Giveup time for persistent file transfer errors.</p>
<dt><code>&#8211;pers_retry_delay_max </code><i>N</i></p>
<dd> Maximum time (sec) for file transfer exponential backoff.</p>
<dt><code>&#8211;pers_retry_delay_min </code><i>N</i></p>
<dd> Minimum time (sec) for file transfer exponential backoff.</p>
<dt><code>&#8211;redirectio</code></p>
<dd> Redirect stdout and stderr to log files (<i>stdoutdae.txt</i> and <i>stderrdae.txt</i>).</p>
<dt><code>&#8211;retry_cap </code><i>N</i></p>
<dd> Limit the maximum exponential backoff time.</p>
<dt><code>&#8211;sched_retry_delay_max </code><i>N</i></p>
<dd> Maximum time (sec) for project RPC exponential backoff.</p>
<dt><code>&#8211;sched_retry_delay_min </code><i>N</i></p>
<dd> Minimum time (sec) for project RPC exponential backoff.</p>
<dt><code>&#8211;unsigned_apps_ok</code></p>
<dd> Allow unsigned apps (for testing).</dl>
<h2>ACCESS CONTROL FOR GUI RPC</h2>
<p> By default the client accepts GUI RPC connections only from programs on the same host, which means that any user on this host can control the client.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-boinccmd/">boinccmd</a></code>(1), <code><a href="/docs/linux/man/1-boincmgr/">boincmgr</a></code>(1) </p>
<p> &lt;<a rel="nofollow" href="http://boinc.berkeley.edu/wiki/Client_configuration#Command-line_options">http://boinc.berkeley.edu/wiki/Client_configuration#Command-line_options</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007-2013 University of California. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<h2>Index</h2>
