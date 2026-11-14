---
title: "eurephiadm-lastlog(7)"
name: "eurephiadm-lastlog"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephiadm-lastlog/"
description: "eurephiadm lastlog – View the eurephia lastlog"
---

<p>eurephiadm lastlog &#8211; View the eurephia lastlog</p>
<h2>Synopsis</h2>
<p><code>eurephiadm lastlog</code> [\-v|\-\-verbose] [\-S|\-\-sortkeys &lt;sort keys&gt;] [&lt;FILTER arguments&gt;]</p>
<h2>Description</h2>
<p>This command will query the lastlog records, which contains information about all logins done with the eurephia-auth plug-in.</p>
<h2>Options</h2>
<dl>
<dt><code>-S</code> | <code>&#8211;sortkeys</code> &lt;sort key&gt;[,&lt;sort key&gt;[,&lt;sort key&gt;]&#8230;]</p>
<dd>Sorting order of the report. More sort keys can be given, separated by comma. The available sort keys are:</p>
<dd><code>uid</code> : User ID</p>
<dd><code>certid</code> : Certificate ID</p>
<dd><code>ip</code> : IP address where the client connects from</p>
<dd><code>vpnip</code> : Assigned IP address on the VPN client</p>
<dd><code>status</code> : eurephia connection status</p>
<dd><code>login</code> : When the client logged in</p>
<dd><code>logout</code> : When the client logged out</p>
<dd><code>username</code> : eurephia username</p>
<dd><code>macaddr</code> : MAC address of the TUN/TAP interface on the VPN client</p>
<dd><code>uicid</code> : User ID/Certificate ID link ID. Related to the IDs provided by <code>eurephiadm usercerts</code></p>
<dt><code>-v</code> | <code>&#8211;verbose</code></p>
<dd>View detailed lastlog</dl>
<h2>Filters</h2>
<p>The filters can help reducing the amount of data being reported. Multiple filters may be added, but they will only work as additional &quot;AND&quot; arguments in the query.</p>
<dl>
<dt><code>-c</code> | <code>&#8211;certid</code> &lt;Certificate ID&gt;</p>
<dd>Certificate ID</p>
<dt><code>-i</code> | <code>&#8211;uid</code> &lt;User ID&gt;</p>
<dd>Numeric user ID</p>
<dt><code>-u</code> | <code>&#8211;username</code> &lt;User name&gt;</p>
<dd>User name</p>
<dt><code>-I</code> | <code>&#8211;ip-addr</code> &lt;IP address&gt;</p>
<dd>IP address of remote host</p>
<dt><code>-s</code> | <code>&#8211;login</code> &lt;YYYY-MM-DD&gt;</p>
<dd>Login time</p>
<dt><code>-e</code> | <code>&#8211;logout</code> &lt;YYYY-MM-DD&gt;</p>
<dd>Logout time</p>
<dt><code>-m</code> | <code>&#8211;mac-addr</code> &lt;TUN/TAP MAC address&gt;</p>
<dd>MAC address of remote VPN interface of the client</p>
<dt><code>-a</code> | <code>&#8211;uicid</code> &lt;Access ID&gt;</p>
<dd>User ID/Certificate ID link ID. Related to the IDs provided by <code>eurephiadm usercerts</code></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm/">eurephiadm</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-certs/">eurephiadm-certs</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-users/">eurephiadm-users</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-usercerts/">eurephiadm-usercerts</a></code>(7)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
