---
title: "condor_config_val(1)"
name: "condor_config_val"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_config_val/"
description: "condor_config_val Query or set a given HTCondor configuration variable"
---

<h2>Name</h2>
<p> <i>condor_config_val</i> Query or set a given HTCondor configuration variable </p>
<h2>Synopsis</h2>
<p> <i>condor_config_val</i> <i>&lt;help option&gt;</i> </p>
<p> <i>condor_config_val</i> [ <code>&lt;location options&gt;</code> ] <i>&lt;edit option&gt;</i> </p>
<p> <i>condor_config_val</i> [ <code>&lt;location options&gt;</code> ] [ <code>&lt;view options&gt;</code> ] <i>vars</i> </p>
<h2>Description</h2>
<p> <i>condor_config_val</i> can be used to quickly see what the current HTCondor configuration is on any given machine. Given a space separated set of configuration variables with the <i>vars</i> argument, <i>condor_config_val</i> will report what each of these variables is currently set to. If a given variable is not defined, <i>condor_config_val</i> will halt on that variable, and report that it is not defined. By default, <i>condor_config_val</i> looks in the local machine&#8217;s configuration files in order to evaluate the variables. Variables and values may instead be queried from a daemon specified using a <code>location option</code> . </p>
<p> <i>Raw</i> output of <i>condor_config_val</i> displays the string used to define the configuration variable. This is what is on the right hand side of the equals sign ( = ) in a configuration file for a variable. The default output is an <i>expanded</i> one. Expanded output recursively replaces any macros within the raw definition of a variable with the macro&#8217;s raw definition. </p>
<p> Each daemon remembers settings made by a successful invocation of <i>condor_config_val</i> . The configuration <i>file</i> is not modified. </p>
<p> <i>condor_config_val</i> can be used to persistently set or unset configuration variables for a specific daemon on a given machine using a <i>-set</i> or <i>-unset</i> <code>edit option</code> . Persistent settings remain when the daemon is restarted. Configuration variables for a specific daemon on a given machine may be set or unset for the time period that the daemon continues to run using a <i>-rset</i> or <i>-runset</i> <code>edit option</code> . These runtime settings will override persistent settings until the daemon is restarted. Any changes made will not take effect until <i>condor_reconfig</i> is invoked. </p>
<p> In general, modifying a host&#8217;s configuration with <i>condor_config_val</i> requires the CONFIG access level, which is disabled on all hosts by default. Administrators have more fine-grained control over which access levels can modify which settings. See section on page for more details on security settings. Further, security considerations require proper settings of configuration variables SETTABLE_ATTRS_&lt;PERMISSION-LEVEL&gt; (see ), ENABLE_PERSISTENT_CONFIG (see ), and HOSTALLOW&#8230; (see ) in order to use <i>condor_config_val</i> to change any configuration variable. </p>
<p> It is generally wise to test a new configuration on a single machine to ensure that no syntax or other errors in the configuration have been made before the reconfiguration of many machines. Having bad syntax or invalid configuration settings is a fatal error for HTCondor daemons, and they will exit. It is far better to discover such a problem on a single machine than to cause all the HTCondor daemons in the pool to exit. <i>condor_config_val</i> can help with this type of testing. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> (help option) Print usage information and exit.</p>
<dt>
<dd></dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> (help option) Print the HTCondor version information and exit.</p>
<dt>
<dd></dl>
<p> <code>-set </code> <i>var = value</i></p>
<dl>
<dt>
<dd> (edit option) Sets one or more persistent configuration file variables. The new value remains if the daemon is restarted. One or more variables can be set; the syntax requires double quote marks to identify the pairing of variable name to value, and to permit spaces.</p>
<dt>
<dd></dl>
<p> <code>-unset </code> <i>var</i></p>
<dl>
<dt>
<dd> (edit option) Each of the persistent configuration variables listed reverts to its previous value.</p>
<dt>
<dd></dl>
<p> <code>-rset </code> <i>var = value</i></p>
<dl>
<dt>
<dd> (edit option) Sets one or more configuration file variables. The new value remains as long as the daemon continues running. One or more variables can be set; the syntax requires double quote marks to identify the pairing of variable name to value, and to permit spaces.</p>
<dt>
<dd></dl>
<p> <code>-runset </code> <i>var</i></p>
<dl>
<dt>
<dd> (edit option) Each of the configuration variables listed reverts to its previous value as long as the daemon continues running.</p>
<dt>
<dd></dl>
<p> <code>-dump</code></p>
<dl>
<dt>
<dd> (view option) Display the raw value of all <i>vars</i> listed. If no <i>vars</i> are listed, then print all configuration variables and their values. The <code>-expand</code> , <code>-default</code> , and <code>-evaluate</code> options take precedence over this <code>-dump</code> option, such that the output will not be raw.</p>
<dt>
<dd></dl>
<p> <code>-default</code></p>
<dl>
<dt>
<dd> (view option) Default values are displayed.</p>
<dt>
<dd></dl>
<p> <code>-expand</code></p>
<dl>
<dt>
<dd> (view option) Expanded values are displayed. This is the default.</p>
<dt>
<dd></dl>
<p> <code>-raw</code></p>
<dl>
<dt>
<dd> (view option) Raw values are displayed.</p>
<dt>
<dd></dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> (view option) Display configuration file name and line number where the variable is set, along with the raw, expanded, and default values of the variable.</p>
<dt>
<dd></dl>
<p> <code>-debug[:&lt;opts&gt;]</code></p>
<dl>
<dt>
<dd> (view option) Send output to stderr , overriding a set value of TOOL_DEBUG .</p>
<dt>
<dd></dl>
<p> <code>-evaluate</code></p>
<dl>
<dt>
<dd> (view option) Applied only when a <code>location option</code> specifies a daemon. The value of the requested parameter will be evaluated with respect to the ClassAd of that daemon.</p>
<dt>
<dd></dl>
<p> <code>-used</code></p>
<dl>
<dt>
<dd> (view option) Applied only when a <code>location option</code> specifies a daemon. Modifies which variables are displayed to only those used by the specified daemon.</p>
<dt>
<dd></dl>
<p> <code>-unused</code></p>
<dl>
<dt>
<dd> (view option) Applied only when a <code>location option</code> specifies a daemon. Modifies which variables are displayed to only those <i>not</i> used by the specified daemon.</p>
<dt>
<dd></dl>
<p> <code>-config</code></p>
<dl>
<dt>
<dd> (view option) Applied only when the configuration is read from files (the default), and <i>not</i> when applied to a specific daemon. Display the current configuration file that set the variable.</p>
<dt>
<dd></dl>
<p> <code>-writeconfig[:upgrade] </code> <i>filename</i></p>
<dl>
<dt>
<dd> (view option) For the configuration read from files (the default), write to file <i>filename</i> all configuration variables. Values that are the same as internal, compile-time defaults will be preceded by the comment character. If the <code>:upgrade </code> <i>o</i> ption is specified, then values that are the same as the internal, compile-time defaults are omitted. Variables are in the same order as the they were read from the original configuration files.</p>
<dt>
<dd></dl>
<p> <code>-mixedcase</code></p>
<dl>
<dt>
<dd> (view option) Applied only when the configuration is read from files (the default), and <i>not</i> when applied to a specific daemon. Print variable names with the same letter case used in the variable&#8217;s definition.</p>
<dt>
<dd></dl>
<p> <code>-local-name </code> <i>&lt;name&gt;</i></p>
<dl>
<dt>
<dd> (view option) Applied only when the configuration is read from files (the default), and <i>not</i> when applied to a specific daemon. Inspect the values of attributes that use local names, which is useful to distinguish which daemon when there is more than one of the particular daemon running.</p>
<dt>
<dd></dl>
<p> <code>-subsystem </code> <i>&lt;daemon&gt;</i></p>
<dl>
<dt>
<dd> (view option) Applied only when the configuration is read from files (the default), and <i>not</i> when applied to a specific daemon. Specifies the subsystem or daemon name to query, with a default value of the TOOL subsystem.</p>
<dt>
<dd></dl>
<p> <code>-address </code> <i>&lt;ip:port&gt;</i></p>
<dl>
<dt>
<dd> (location option) Connect to the given IP address and port number.</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> (location option) Use the given central manager and an optional port number to find daemons.</p>
<dt>
<dd></dl>
<p> <code>-name </code> <i>&lt;machine_name&gt;</i></p>
<dl>
<dt>
<dd> (location option) Query the specified machine&#8217;s <i>condor_master</i> daemon for its configuration. Does not function together with any of the options: <code>-dump</code> , <code>-config</code> , or <code>-verbose</code> .</p>
<dt>
<dd></dl>
<p> <code>-master | -schedd | -startd | -collector | -negotiator</code></p>
<dl>
<dt>
<dd> (location option) The specific daemon to query.</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_config_val</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Examples</h2>
<p> Here is a set of examples to show a sequence of operations using <i>condor_config_val</i> . To request the <i>condor_schedd</i> daemon on host perdita to display the value of the MAX_JOBS_RUNNING configuration variable: </p>
<p>%&nbsp;<wbr>condor_config_val -name perdita -schedd MAX_JOBS_RUNNING </p>
<p>500 </p>
<p> To request the <i>condor_schedd</i> daemon on host perdita to set the value of the MAX_JOBS_RUNNING configuration variable to the value 10. </p>
<p>%&nbsp;<wbr>condor_config_val -name perdita -schedd -set&nbsp;<wbr>&quot;MAX_JOBS_RUNNING&nbsp;<wbr>=&nbsp;<wbr>10&quot; </p>
<p>Successfully set configuration&nbsp;<wbr>&quot;MAX_JOBS_RUNNING&nbsp;<wbr>=&nbsp;<wbr>10&quot;&nbsp;<wbr>on&nbsp;<wbr> </p>
<p>schedd perdita.cs.wisc.edu&nbsp;<wbr>&lt;128.105.73.32:52067&gt;. </p>
<p> A command that will implement the change just set in the previous example. </p>
<p>%&nbsp;<wbr>condor_reconfig -schedd perdita </p>
<p>Sent&nbsp;<wbr>&quot;Reconfig&quot;&nbsp;<wbr>command to schedd perdita.cs.wisc.edu </p>
<p> A re-check of the configuration variable reflects the change implemented: </p>
<p>%&nbsp;<wbr>condor_config_val -name perdita -schedd MAX_JOBS_RUNNING </p>
<p>10 </p>
<p> To set the configuration variable MAX_JOBS_RUNNING back to what it was before the command to set it to 10: </p>
<p>%&nbsp;<wbr>condor_config_val -name perdita -schedd -unset MAX_JOBS_RUNNING </p>
<p>Successfully unset configuration&nbsp;<wbr>&quot;MAX_JOBS_RUNNING&quot;&nbsp;<wbr>on&nbsp;<wbr> </p>
<p>schedd perdita.cs.wisc.edu&nbsp;<wbr>&lt;128.105.73.32:52067&gt;. </p>
<p> A command that will implement the change just set in the previous example. </p>
<p>%&nbsp;<wbr>condor_reconfig -schedd perdita </p>
<p>Sent&nbsp;<wbr>&quot;Reconfig&quot;&nbsp;<wbr>command to schedd perdita.cs.wisc.edu </p>
<p> A re-check of the configuration variable reflects that variable has gone back to is value before initial set of the variable: </p>
<p>%&nbsp;<wbr>condor_config_val -name perdita -schedd MAX_JOBS_RUNNING </p>
<p>500 </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
