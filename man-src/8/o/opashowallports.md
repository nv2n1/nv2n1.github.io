---
title: "opashowallports(8)"
name: "opashowallports"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opashowallports/"
description: "opashowallports (Switch and Host) Displays basic port state and statistics for all host nodes, chassis, or externally-managed switches. NOTE: opareport and opareports are more powerful Intel(R) Omn..."
---

<p>opashowallports <code>(Switch and Host)</code> Displays basic port state and statistics for all host nodes, chassis, or externally-managed switches. <code>NOTE:</code> opareport and opareports are more powerful Intel(R) Omni-Path Fabric Suite FastFabric commands. For general fabric analysis, use opareport or opareports with options such as -o errors and -o slowlinks to perform an efficient analysis of link speeds and errors. </p>
<h2>Syntax</h2>
<p>opashowallports [-C] [-f <i>hostfile</i>] [-F <i>chassisfile</i>] [-h &#8216;<i>hosts</i>&#8216;]<br/>
 [-H &#8216;<i>chassis</i>&#8216;] [-S]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd>Produces full help text.</dd>
<dt>-C</dt>
<dd>Performs operation against chassis. Default = host.</dd>
<dt>-f <i>hostfile</i></dt>
<dd>File with list of hosts in cluster. Default is /etc/sysconfig/opa/hosts file.</dd>
<dt>-F <i>chassisfile</i></dt>
<dd>File with list of chassis in cluster. Default is /etc/sysconfig/opa/chassis file.</dd>
<dt>-h <i>hosts</i></dt>
<dd>List of hosts for which to show ports.</dd>
<dt>-H <i>chassis</i></dt>
<dd>List of chassis for which to show ports.</dd>
<dt>-S</dt>
<dd>Securely prompts for password for admin on chassis.</dd></dl>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS</code></dt>
<dd>List of hosts, used if -h option not supplied. </dd>
<dt><code>CHASSIS</code></dt>
<dd>List of chassis, used if -C is used and -H and -F options not supplied. </dd>
<dt><code>HOSTS_FILE</code></dt>
<dd>File containing list of hosts, used in absence of -f and -h. </dd>
<dt><code>CHASSIS_FILE</code></dt>
<dd>File containing list of chassis, used in absence of -F and -H. </dd>
<dt><code>FF_CHASSIS_LOGIN_METHOD</code></dt>
<dd>How to log into chassis. Can be Telnet or SSH. </dd>
<dt><code>FF_CHASSIS_ADMIN_PASSWORD</code></dt>
<dd>Password for admin on all chassis. Used in absence of -S option. </dd>
</dl>
<h2>Example</h2>
<p>opashowallports<br/>
 opashowallports -h &#8216;elrond arwen&#8217;<br/>
 HOSTS=&#8217;elrond arwen&#8217; opashowallports<br/>
 opashowallports -C<br/>
 opashowallports -H &#8216;chassis1 chassis2&#8242;<br/>
 CHASSIS=&#8217;chassis1 chasssi2&#8217; opashowallports</p>
<h2>Notes</h2>
<p>When performing opashowallports against hosts, internally SSH is used. The command opashowallports requires that password-less SSH be set up between the host running the Intel(R) Omni-Path Fabric Suite FastFabric Toolset and the hosts opashowallports is operating against. The opasetupssh FastFabric tool can aid in setting up password-less SSH. When performing operations against chassis, Intel recommends that you set up SSH keys (see <i>opasetupssh</i> ). If SSH keys are not set up, Intel recommends that you use the -S option, to avoid keeping the password in configuration files. When performing opashowallports against externally-managed switches, a node with Intel(R) Omni-Path Fabric Suite FastFabric Toolset installed is required. Typically, this is the node from which opashowallports is being run. </p>
