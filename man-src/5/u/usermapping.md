---
title: "usermapping(5)"
name: "usermapping"
section: "5"
letter: "u"
url: "/docs/linux/man/5-usermapping/"
description: "usermapping – user mapping entry file format"
---

<p>usermapping &#8211; user mapping entry file format</p>
<h2>Description</h2>
<p>A usermapping entry is used to define alias names for a cluster user. The user&#8217;s name known by the scheduling system is known as the cluster user. If the cluster user doesn&#8217;t match the user account name on an execution host, the usermapping feature can solve the problem. </p>
<p> Each line in the usermapping entry file specifies a user name and the host(s) where he has an account. </p>
<p> A list of currently configured user mapping entries can be displayed via the <code>-sumapl</code> option. The contents of each enlisted user mapping entry can be shown via the <code>-sumap</code> switch. The output follows the <i>usermapping</i> format description. New user entries can be created and existing can be modified via the <code>-aumap</code>, <code>-mumap</code> and <code>-dumap</code> options to</p>
<h2>Format</h2>
<p>A user mapping entry contains two parameters:</p>
<h3><code>cluster_user</code></h3>
<p>The cluster_user keyword defines the cluster user name. The rest of the textline after the keyword &quot;cluster_user&quot; will be taken as cluster user value.</p>
<h3><code>remote_user</code></h3>
<p>The user name on an execution host. Please note that the value for this attribute might be overwritten for a certain hostgroups or single host. Find an example below.</p>
<h2>Example</h2>
<p>This is a typical user mapping entry for a cluster user mapping: cluster_user peter remote_user peter,[@linux=pet1],[fangorn=peter1] The entry will map the user peter which is defined in the cluster system to the user peter on all hosts in the cluster except for all hosts which are referenced in the hostgroup @linux. For all these hosts the user will be mapped to pet1. For the host fangorn the remote user will be peter1. to obtain for more information about that. </p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
