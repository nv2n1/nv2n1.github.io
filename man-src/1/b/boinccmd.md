---
title: "boinccmd(1)"
name: "boinccmd"
section: "1"
letter: "b"
url: "/docs/linux/man/1-boinccmd/"
description: "boinccmd – The command line interface to the BOINC client."
---

<h2>NAME</h2>
<p> boinccmd &#8211; The command line interface to the BOINC client.</p>
<h2>SYNOPSIS</h2>
<p> <code>boinccmd</code> [<code>&#8211;host</code> <i>hostname</i>[:<i>port</i>]] [<code>&#8211;passwd</code> <i>passwd</i>] {<i>command</i>} <code>boinccmd</code> [<code>-hV</code>] </p>
<p> Notice that the order of the options is important. The <code>&#8211;host</code> and <code>&#8211;passwd</code> options must precede any command.</p>
<h2>DESCRIPTION</h2>
<p> The BOINC command tool (<code>boinccmd</code>) provides a command line interface to control a running BOINC client (<code><a href="/docs/linux/man/1-boinc/">boinc</a></code>(1)). It communicates with a running client using port 31416 over TCP/IP. It can only connect to one client at a time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;host</code> <i>hostname</i>[:<i>port</i>]</p>
<dd> Connect to the host <i>hostname</i>. The default host is localhost.</p>
<dt><code>&#8211;passwd</code> <i>passwd</i></p>
<dd> Use <i>passwd</i> as password for RPC authentication. If the current working directory contains a file <i>gui_rpc_auth.cfg</i>, <code>boinccmd</code> will read the password from this file.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show a help message and all commands.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Show the version of the program.</dl>
<h2>COMMANDS</h2>
<h3>ACCOUNT QUERY AND ATTACH</h3>
<dl>
<dt><code>&#8211;lookup_account</code> <i>URL</i> <i>email</i> <i>passwd</i></p>
<dd> Look up account and print account key.</p>
<dt><code>&#8211;create_account</code> <i>URL</i> <i>email</i> <i>passwd</i> <i>name</i></p>
<dd> Create account with the given email address, password, and user name.</p>
<dt><code>&#8211;project_attach</code> <i>URL</i> <i>account_key</i></p>
<dd> Attach to an account using the project URL and authenticator (send via email after <code>&#8211;create_account</code> was succesfull).</p>
<dt><code>&#8211;join_acct_mgr</code> <i>URL</i> <i>name</i> <i>passwd</i></p>
<dd> Attach to an account manager (or do RPC if already attached). The account has to be created via the account manager website.</p>
<dt><code>&#8211;quit_acct_mgr</code></p>
<dd> Detach from the current account manager.</dl>
<h3>STATE QUERIES</h3>
<dl>
<dt><code>&#8211;get_state</code></p>
<dd> Show complete client state.</p>
<dt><code>&#8211;get_cc_status</code></p>
<dd> Show only current CPU, GPU and network modes.</p>
<dt><code>&#8211;get_tasks</code></p>
<dd> Show all tasks of the client (in progress, waiting and completed only). Tasks that where reported to the project server are not shown here.</p>
<dt><code>&#8211;get_simple_gui_info</code></p>
<dd> Show status of projects and active tasks.</p>
<dt><code>&#8211;get_file_transfers</code></p>
<dd> Show all current file transfers.</p>
<dt><code>&#8211;get_project_status</code></p>
<dd> Show status of all projects.</p>
<dt><code>&#8211;get_disk_usage</code></p>
<dd> Show disk usage of all projects.</p>
<dt><code>&#8211;get_proxy_settings</code></p>
<dd> Get proxy settings.</p>
<dt><code>&#8211;get_messages</code> <i>seqno</i></p>
<dd> Show messages with sequence numbers beyond <i>seqno</i>.</p>
<dt><code>&#8211;get_message_count</code></p>
<dd> Show largest message sequence number.</p>
<dt><code>&#8211;get_notices</code> <i>seqno</i></p>
<dd> Show project notices with sequence numbers beyond <i>seqno</i>.</p>
<dt><code>&#8211;get_host_info</code></p>
<dd> Show system information about the host where the BOINC client is running.</p>
<dt><code>&#8211;get_daily_xfer_history</code></p>
<dd> Show network traffic history of the BOINC client.</dl>
<h3>CONTROL OPERATIONS</h3>
<dl>
<dt><code>&#8211;task</code> <i>URL</i> <i>task_name</i> {suspend | resume | abort}</p>
<dd> Do operation on a task.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>suspend</code></p>
<dd> Temporarily stop work on task.</p>
<dt><code>resume</code></p>
<dd> Allow work on task.</p>
<dt><code>abort</code></p>
<dd> Permanently stop work on task.</dl>
</dl>
<dt><code>&#8211;project</code> <i>URL</i> {reset | detach | update | suspend | resume | nomorework | allowmorework | detach_when_done | dont_detach_when_done}</p>
<dd> Do operation on a project, identified by its master URL.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>reset</code></p>
<dd> Delete current tasks, applications and other files from this project, request new tasks.</p>
<dt><code>detach</code></p>
<dd> Delete current tasks applications and other files from this project, don&#8217;t request any new tasks.</p>
<dt><code>update</code></p>
<dd> Contact project scheduling server.</p>
<dt><code>suspend</code></p>
<dd> Stop all tasks for project.</p>
<dt><code>resume</code></p>
<dd> Resume tasks for project.</p>
<dt><code>nomorework</code></p>
<dd> Finish all downloaded tasks but don&#8217;t get more.</p>
<dt><code>allowmorework</code></p>
<dd> Undo <code>nomorework</code>.</p>
<dt><code>detach_when_done</code></p>
<dd> Detach project after all tasks are finished.</p>
<dt><code>dont_detach_when_done</code></p>
<dd> Undo <code>detach_when_done</code>.</dl>
</dl>
<dt><code>&#8211;file_transfer</code> <i>URL</i> <i>filename</i> {retry | abort}</p>
<dd> Do operation on a file transfer.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>retry</code></p>
<dd> Retry file transfer.</p>
<dt><code>abort</code></p>
<dd> Permanently abort file transfer.</dl>
</dl>
<dt><code>&#8211;set_run_mode</code> {always | auto | never} [<i>duration</i>]</p>
<dd> Set run mode (applies to CPU and GPU).</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>always</code></p>
<dd> Do work always.</p>
<dt><code>auto</code></p>
<dd> Do work only when allowed by preferences.</p>
<dt><code>never</code></p>
<dd> Don&#8217;t do work.</dl>
</dl>
<p> If <i>duration</i> is zero or absent, this mode is permanent. Otherwise, after <i>duration</i> seconds elapse, revert to last permanent mode.</p>
<dt><code>&#8211;set_network_mode</code> {always | auto | never} [<i>duration</i>]</p>
<dd> Set network mode. Like <code>&#8211;set_run_mode</code> but applies to network transfers only.</p>
<dt><code>&#8211;set_gpu_mode</code> {always | auto | never} [<i>duration</i>]</p>
<dd> Set GPU mode. Like <code>&#8211;set_run_mode</code> but applies to GPU processing only.</p>
<dt><code>&#8211;set_proxy_settings</code> <i>http_server_name</i> <i>http_server_port</i> <i>http_user_name</i> <i>http_user_passwd</i> <i>socks_server_name</i> <i>socks_server_port</i> <i>socks5_user_name</i> <i>socks5_user_passwd</i> <i>noproxy_hosts</i></p>
<dd> Set proxy settings. All fields are mandatory.</p>
<dt><code>&#8211;run_benchmarks</code></p>
<dd> Run CPU benchmarks.</p>
<dt><code>&#8211;read_global_prefs_override</code></p>
<dd> Tell the client to read the <i>global_prefs_override.xml</i> file and incorporate any global preferences indicated there.</p>
<dt><code>&#8211;quit</code></p>
<dd> Tell the client to quit.</p>
<dt><code>&#8211;read_cc_config</code></p>
<dd> Tell the client to reread the configuration file (<i>cc_config.xml</i>).</p>
<dt><code>&#8211;get_project_config</code> <i>URL</i></p>
<dd> Fetch configuration of project located at <i>URL</i>.</p>
<dt><code>&#8211;network_available</code></p>
<dd> Tell the client to retry deferred network communication.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-boinc/">boinc</a></code>(1), <code><a href="/docs/linux/man/1-boincmgr/">boincmgr</a></code>(1) </p>
<p> &lt;<a rel="nofollow" href="http://boinc.berkeley.edu/wiki/Boinccmd_tool">http://boinc.berkeley.edu/wiki/Boinccmd_tool</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007-2008 University of California. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<h2>Index</h2>
