---
title: "nuaclgen(8)"
name: "nuaclgen"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nuaclgen/"
description: "nuaclgen – NUFW acl generator"
---

<p>nuaclgen &#8211; NUFW acl generator</p>
<h2>Synopsis</h2>
<p><code>nuaclgen</code> [ <code>&#8211;Schema </code><i>eq|ineq</i> ] [ <code>&#8211;Aclname </code><i>ACLDN</i> ] [ <code>&#8211;saddr </code><i>NETWORK1</i> ] [ <code>&#8211;daddr </code><i>NETWORK2</i> ] [ <code>&#8211;proto </code><i>PROTONUMBER</i> ] [ <code>&#8211;sport </code><i>P1[:P2]</i> ] [ <code>&#8211;dport </code><i>P3[:P4]</i> ] [ <code>&#8211;OsName </code><i>OSNAME</i> ] [ <code>&#8211;OsVersion </code><i>OSVERSION</i> ] [ <code>&#8211;OsRelease </code><i>OSRELEASE</i> ] [ <code>&#8211;AppName </code><i>APPLICATION NAME</i> ] [ <code>&#8211;AppSig </code><i>APPLICATION SIGNATURE</i> ] [ <code>&#8211;Separator </code><i>SEPARATOR</i> ] [ <code>&#8211;jump </code><i>[ACCEPT|DROP]</i> ] [ <code>&#8211;groups </code><i>GROUPLIST</i> ] <code>nuaclgen</code> [ <code>&#8211;List</code> ] [ <code>&#8211;groups </code><i>Id Group</i> ] <code>nuaclgen</code> [ <code>&#8211;Delete </code><i>DN</i> ] <code>nuaclgen</code> [ <code>&#8211;help</code> ] </p>
<h2>Description</h2>
<p>This manual page documents the <code>nuaclgen</code> command. </p>
<p> nuaclgen is an Access control list generator for the ldap backend of Nuauth, the authentication server of the NUFW package. </p>
<p> Original packaging and informations and help can be found from <a rel="nofollow" href="http://www.nufw.org/">http://www.nufw.org/</a></p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;Schema </code><i>eq|ineq</i></p>
<dd>Use equality schema or not (Equality schema requires dport be specified, and is the default.</p>
<dt><code>&#8211;AclName </code><i>Acl DN</i></p>
<dd>Add an acl in the ldap tree with dn <i>Acl DN</i></p>
<dt><code>&#8211;saddr </code><i>Network</i></p>
<dd>Specify source network for the acl, with network of the form : aaa.bbb.ccc.ddd[/ee]. Default value : 0.0.0.0/0</p>
<dt><code>&#8211;daddr </code><i>Network</i></p>
<dd>Specify destination network for the acl, with network of the form : aaa.bbb.ccc.ddd[/ee]. Default value : 0.0.0.0/0</p>
<dt><code>&#8211;proto </code><i>Protocol number</i></p>
<dd>Specify protocol type for the acl</p>
<dt><code>&#8211;sport </code><i>Source port</i></p>
<dd>Specify source port(s) for the Acl. NNNN:MMMM can be used to specify a port range.</p>
<dt><code>&#8211;dport </code><i>Destination port</i></p>
<dd>Specify destination port(s) for the Acl. NNNN:MMMM can be used to specify a port range.</p>
<dt><code>&#8211;jump </code><i>Decision</i></p>
<dd>Specify decision for the Acl. Has to be ACCEPT or DROP.</p>
<dt><code>&#8211;groups </code><i>Groups list</i></p>
<dd>Specify the user group(s) on which Acl apply. Must be of the form : Group1[,Group2[,&#8230;]]</p>
<dt><code>&#8211;List &#8211;group </code><i>Group ID</i></p>
<dd>List Acls for the <i>Group ID</i> group</p>
<dt><code>&#8211;Delete </code><i>Dn</i></p>
<dd>Deletes the Acl stored in the provided Dn</p>
<dt><code>&#8211;help </code></p>
<dd>Displays a brief resume of available options and quits</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nufw/">nufw</a>(8) </p>
<p> <a href="/docs/linux/man/8-nuauth/">nuauth</a>(8)</p>
<h2>Author</h2>
<p>Nuauth was designed and coded by Eric Leblond, aka Regit (&lt;eric [at] regit.org&gt;) , and Vincent Deffontaines, aka gryzor (&lt;vincent [at] gryzor.com&gt;). Original idea in 2001, while working on NSM Ldap support. </p>
<p> This manual page was written by Eric Leblond and copyrighted by INL (2003-2005) </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 2 as published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts.</p>
