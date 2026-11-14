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
<p>opashowallports [-C] [-f <i>hostfile</i>] [-F <i>chassisfile</i>] [-h &#8216;<i>hosts</i>&#8216;]<br />
 [-H &#8216;<i>chassis</i>&#8216;] [-S]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text.</p>
<dt>-C</p>
<dd>Performs operation against chassis. Default = host.</p>
<dt>-f <i>hostfile</i></p>
<dd>File with list of hosts in cluster. Default is /etc/sysconfig/opa/hosts file.</p>
<dt>-F <i>chassisfile</i></p>
<dd>File with list of chassis in cluster. Default is /etc/sysconfig/opa/chassis file.</p>
<dt>-h <i>hosts</i></p>
<dd>List of hosts for which to show ports.</p>
<dt>-H <i>chassis</i></p>
<dd>List of chassis for which to show ports.</p>
<dt>-S</p>
<dd>Securely prompts for password for admin on chassis.</dl>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>HOSTS</code></p>
<dd>List of hosts, used if -h option not supplied. </p>
<dt><code>CHASSIS</code></p>
<dd>List of chassis, used if -C is used and -H and -F options not supplied. </p>
<dt><code>HOSTS_FILE</code></p>
<dd>File containing list of hosts, used in absence of -f and -h. </p>
<dt><code>CHASSIS_FILE</code></p>
<dd>File containing list of chassis, used in absence of -F and -H. </p>
<dt><code>FF_CHASSIS_LOGIN_METHOD</code></p>
<dd>How to log into chassis. Can be Telnet or SSH. </p>
<dt><code>FF_CHASSIS_ADMIN_PASSWORD</code></p>
<dd>Password for admin on all chassis. Used in absence of -S option. </p>
</dl>
<h2>Example</h2>
<p>opashowallports<br />
 opashowallports -h &#8216;elrond arwen&#8217;<br />
 HOSTS=&#8217;elrond arwen&#8217; opashowallports<br />
 opashowallports -C<br />
 opashowallports -H &#8216;chassis1 chassis2&#8242;<br />
 CHASSIS=&#8217;chassis1 chasssi2&#8217; opashowallports</p>
<h2>Notes</h2>
<p>When performing opashowallports against hosts, internally SSH is used. The command opashowallports requires that password-less SSH be set up between the host running the Intel(R) Omni-Path Fabric Suite FastFabric Toolset and the hosts opashowallports is operating against. The opasetupssh FastFabric tool can aid in setting up password-less SSH. When performing operations against chassis, Intel recommends that you set up SSH keys (see <i>opasetupssh</i> ). If SSH keys are not set up, Intel recommends that you use the -S option, to avoid keeping the password in configuration files. When performing opashowallports against externally-managed switches, a node with Intel(R) Omni-Path Fabric Suite FastFabric Toolset installed is required. Typically, this is the node from which opashowallports is being run. </p>
