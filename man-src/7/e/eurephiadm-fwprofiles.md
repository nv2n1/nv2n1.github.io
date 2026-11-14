---
title: "eurephiadm-fwprofiles(7)"
name: "eurephiadm-fwprofiles"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephiadm-fwprofiles/"
description: "eurephiadm fwprofiles – Configuring eurephia firewall profiles"
---

<p>eurephiadm fwprofiles &#8211; Configuring eurephia firewall profiles</p>
<h2>Synopsis</h2>
<p><code>eurephiadm fwprofiles</code> \-\-list|\-l [\-v|\-\-verbose] [\-a|\-\-accessprofile &lt;acc. ID&gt;] [\-f|\-\-fw-destination &lt;name&gt;] [\-i|\-\-uid &lt;user ID&gt;] [\-n|\-\-username &lt;username&gt;] [\-c|\-\-certid &lt;cert ID&gt;] [\-e|\-\-email &lt;e-mail address&gt;] [\-d|\-\-digest &lt;certificate SHA1 digest&gt;]<br />
 <code>eurephiadm fwprofiles</code> \-\-add|\-A [\-d|\-\-description &lt;Description&gt;] [\-f|\-\-fw-destination &lt;name&gt;]<br />
 <code>eurephiadm fwprofiles</code> \-\-delete|\-D [\-a|\-\-accessprofile &lt;acc. ID&gt;] [\-f|\-\-fw-destination &lt;name&gt;]</p>
<h2>Description</h2>
<p>The eurephia plug-in can take advantage of the OS firewall to give a fine grained access control of each OpenVPN client. The preconfigured firewall chains available to eurephia needs to be defined using this eurephiadm command. When the firewall profiles are defined here, they can be assigned to the different user accesses you have enabled.</p>
<h2>Modes</h2>
<p>Available modes for the fwprofiles command are:</p>
<dl>
<dt><code>-A | &#8211;add</code></p>
<dd>[-d|&#8211;description &lt;Description&gt;] [-f|&#8211;fw-destination &lt;name&gt;]<br />
 Add a new firewall profile. Both <code>&#8211;description</code> and <code>&#8211;fw-destination</code> are required. The <code>&#8211;description</code> is just to give a human readable description of the firewall profile name and is only used in the different reports available in <code>eurephiadm</code>.</p>
<dt><code>-D | &#8211;delete</code></p>
<dd>[-a|&#8211;accessprofile &lt;acc. ID&gt;] [-f|&#8211;fw-destination &lt;name&gt;]<br />
 Delete a firewall profile. Either <code>&#8211;accessprofile</code> or <code>&#8211;fw-destination</code> must be provided.</p>
<dt><code>-l | &#8211;list</code></p>
<dd>[-v|&#8211;verbose] [-a|&#8211;accessprofile &lt;acc. ID&gt;] [-f|&#8211;fw-destination &lt;name&gt;] [-i|&#8211;uid &lt;user ID&gt;] [-n|&#8211;username &lt;username&gt;] [-c|&#8211;certid &lt;cert ID&gt;] [-e|&#8211;email &lt;e-mail address&gt;] [-d|&#8211;digest &lt;certificate SHA1 digest&gt;]<br />
 List available firewall profiles. Without any arguments, a simple overview over all registered firewall profiles. If the <code>&#8211;verbose</code> argument is given, the list will be more comprehensive.</p>
<dd>The rest of the arguments are filters which is used to reduce the length of the list. Multiple filters may be added, but they will only work as additional &quot;AND&quot; argument in the query.</p>
<dt><code>-h | &#8211;help</code></p>
<dd>&lt;mode&gt; Show a help screen. Without any arguments, all modes are listed. Providing a mode will show more information about the chosen mode.</dl>
<h2>Filters</h2>
<p>These filters are used by the <code>&#8211;list</code> mode.</p>
<dl>
<dt><code>-a</code> | <code>&#8211;accessprofile</code> &lt;id&gt;</p>
<dd>Numeric ID defining the access profile ID.</p>
<dt><code>-f</code> | <code>&#8211;fw-destination</code> &lt;name&gt;</p>
<dd>The firewall reference for the chain used by the OS when filtering the OpenVPN client traffic.</p>
<dt><code>-i</code> | <code>&#8211;uid</code> &lt;user id&gt;</p>
<dd>Numeric user ID</p>
<dt><code>-n</code> | <code>&#8211;username</code> &lt;username&gt;</p>
<dd>User name</p>
<dt><code>-c</code> | <code>&#8211;certid</code> &lt;certid&gt;</p>
<dd>Numeric reference to a certificate</p>
<dt><code>-e</code> | <code>&#8211;email</code> &lt;email addr&gt;</p>
<dd>e-mail address in certificates</p>
<dt><code>-d</code> | <code>&#8211;digest</code> &lt;SHA1 digest&gt;</p>
<dd>Certificate SHA1 digest</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm/">eurephiadm</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-usercerts/">eurephiadm-usercerts</a></code>(7)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
