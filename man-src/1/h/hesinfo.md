---
title: "hesinfo(1)"
name: "hesinfo"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hesinfo/"
description: "hesinfo – find out what is stored in the Hesiod database"
---

<h2>NAME</h2>
<p> hesinfo &#8211; find out what is stored in the Hesiod database</p>
<h2>SYNOPSIS</h2>
<pre>
hesinfo <i>[-bl]</i> <i>HesiodName</i> <i>HesiodNameType</i>
</pre>
<h2>DESCRIPTION</h2>
<p> <i>hesinfo</i> takes two arguments, a name to be resolved and a string, known as a HesiodNameType. It then prints the information returned by the Hesiod nameserver. </p>
<p> The value returned by <code>hesinfo</code> is of the type <i>HesiodNameType.</i> </p>
<p> <i>hesinfo</i> understands the following options:</p>
<dl>
<dt><code>-l</code></dt>
<dd> Selects long format.</dd>
<dt><code>-b</code></dt>
<dd> Prints the fully-qualified string passed to the nameserver. </dd>
</dl>
<h3>VALID Hesiod_Names</h3>
<p> The following types of identifiers may be used in the <i>HesiodName</i> argument to <code>hesinfo.</code> These values will be resolved by accessing the <code>hesiod</code> database. </p>
<dl>
<dt><code>&lt;username&gt;</code></dt>
<dd> the 8-character-or-less string used to identify users or classes (e.g. joeuser, root, 1.00, etc). Used with the <i>Hesiod_Name_Types</i> <code>passwd,</code> <code>pobox,</code> and <code>filsys.</code> </dd>
<dt><code>&lt;uid&gt;</code></dt>
<dd> the id number assigned to a user. </dd>
<dt><code>&lt;groupid&gt;</code></dt>
<dd> the id number assigned to a group. </dd>
<dt><code>&lt;groupname&gt;</code></dt>
<dd> a name identifying a unique group. </dd>
<dt><code>&lt;file-system-name&gt;</code></dt>
<dd> the name of an athena file system. </dd>
<dt><code>&lt;rvd server&gt;:&lt;pack&gt;</code></dt>
<dd> the name of an rvd&#8217;s server and pack seperated by a colon. </dd>
<dt><code>&lt;nfs server&gt;:&lt;partition&gt;</code></dt>
<dd> the name of an nfs server and its partition seperated by a colon. </dd>
<dt><code>&lt;workstation-name&gt;</code></dt>
<dd> the machine name of an Athena workstation (e.g. E40-343-3). </dd>
<dt><code>&lt;service-name&gt;</code></dt>
<dd> name of an Athena service (e.g. Zephyr). </dd>
<dt><code>&lt;service-type&gt;</code></dt>
<dd> name of Unix service (valid entries are defined in /etc/services). </dd>
<dt><code>&lt;printer-name&gt;</code></dt>
<dd> name of a printer. </dd>
<dt><code>&lt;printer-cluster-name&gt;</code></dt>
<dd> name of an Athena print cluster. </dd>
<dt><code>&lt;foo&gt;</code></dt>
<dd> some <code>hesinfo</code> calls (e.g. <code>prclusterlist</code> ) do not require a specific <i>HesiodName</i> argument. However, you must include a dummy string (e.g. &#8216;foo&#8217;) for <code>hesinfo</code><br />
&nbsp;<wbr>to work properly. </dd>
</dl>
<h3>VALID Hesiod_Name_Types</h3>
<p> The following symbols are valid substitutions for the <i>HesiodNameType</i> argument to <code>hesinfo.</code> </p>
<dl>
<dt><code>&nbsp;<wbr>passwd</code></dt>
<dd> returns string suitable for inclusion in <i>/etc/passwd,</i> searching with <code>&lt;username&gt;.</code> </dd>
<dt><code>&nbsp;<wbr>pobox</code></dt>
<dd> returns information on the pobox assigned to the user specified by <i>HesiodName,</i> searching with <code>&lt;username&gt;.</code> </dd>
<dt><code>&nbsp;<wbr>uid </code></dt>
<dd> returns string suitable for inclusion in <i>/etc/passwd,</i> searching with <code>&lt;uid&gt;.</code> </dd>
<dt><code>&nbsp;<wbr>gid </code></dt>
<dd> returns string suitable for inclusion in <i>/etc/group,</i> searching with <code>&lt;groupid&gt;.</code> </dd>
<dt><code>&nbsp;<wbr>group</code></dt>
<dd> returns string suitable for inclusion in <i>/etc/group,</i> searching with <code>&lt;groupname&gt;.</code> </dd>
<dt><code>&nbsp;<wbr>grplist</code></dt>
<dd> returns subgroups included in superset defined by <code>&lt;groupname&gt;.</code> </dd>
<dt><code>&nbsp;<wbr>filsys</code></dt>
<dd> returns file system type, export point, server, mount mode, and import point for the following valid <i>HesiodNames</i> (see above) <code>&#8211; &lt;file system name&gt;, &lt;username&gt;, &lt;rvd server&gt;:&lt;pack&gt;, </code> <code>and &lt;nfs server&gt;:&lt;partition&gt;</code> </dd>
<dt><code>&nbsp;<wbr>cluster</code></dt>
<dd> returns information about the local cluster the workstation, specified by <code>&lt;workstation name&gt;.</code> Included is information about the local file and print servers. This information is accesses by <code>clusterinfo </code> at boot time. </dd>
<dt><code>&nbsp;<wbr>sloc</code></dt>
<dd> returns network name of service host for <code>&lt;service-name&gt;.</code> </dd>
<dt><code>&nbsp;<wbr>service</code></dt>
<dd> returns Internet protocol type and protocol service port for <code>&lt;service-type&gt;.</code> </dd>
<dt><code>&nbsp;<wbr>pcap</code></dt>
<dd> returns a valid entry for /etc/printcap for <code>&lt;printer-name&gt;.</code> </dd>
<dt><code>&nbsp;<wbr>prcluserlist</code></dt>
<dd> returns a list of print clusters. </dd>
<dt><code>&nbsp;<wbr>prcluster</code></dt>
<dd> returns a list of printers in a cluster specified by <code>&lt;printer-cluster-name&gt;.</code> </dd>
</dl>
<h2>FILES</h2>
<p> /etc/athena/hesiod.conf</p>
<h2>SEE ALSO</h2>
<p> `Hesiod &#8211; Project Athena Technical Plan &#8212; Name Service&#8217;, <a href="/docs/linux/man/8-named/">named</a>(8), <a href="/docs/linux/man/3-hesiod/">hesiod</a>(3)</p>
<h2>AUTHOR</h2>
<p> Steve Dyer, IBM/Project Athena<br />
 Copyright 1987, 1988, 1996 by the Massachusetts Institute of Technology. </p>
