---
title: "eurephiadm-usercerts(7)"
name: "eurephiadm-usercerts"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephiadm-usercerts/"
description: "eurephiadm usercerts – Managing user accounts and certificate relations"
---

<p><code>eurephiadm usercerts</code><br />
&nbsp;<wbr>&#8211; Managing user accounts and certificate relations</p>
<h2>Description</h2>
<p>For a user to connect to a eurephia enabled OpenVPN server, a user account must have been created and activated and an SSL certificate available to the user must have been registered. The user account and certificate the user may use must then be linked together, and this linking the <code>eurephiadm usercert</code> command takes care of. </p>
<p> It is also this relation which gives you the option to control which network resources the VPN clients may access, by assigning a firewall profile to such user-certificate links. </p>
<p> Available modes for the <code>usercerts</code> command are:</p>
<dl>
<dt><code>-A</code> | <code>&#8211;add</code></p>
<dd>Register a new certificate and user-cert link</p>
<dt><code>-D</code> | <code>&#8211;delete</code></p>
<dd>Delete a certificate and user-cert link</p>
<dt><code>-S</code> | <code>&#8211;set-fwprofile</code></p>
<dd>Sets the firewall access profile for a user-cert link</p>
<dt><code>-l</code> | <code>&#8211;list</code></p>
<dd>List all registered user-cert links</p>
<dt><code>-h</code> | <code>&#8211;help</code> &lt;mode&gt;</p>
<dd>Help about a specific mode</dl>
<p> The list mode will list all registered links between user accounts and certificates.</p>
<h2>List Mode</h2>
<p>The list mode will show all registered user-certificate links</p>
<dl>
<dt><code>-S</code> | <code>&#8211;sort</code> &lt;sort keys&gt;</p>
<dd>Define the sorting of the list </p>
<p> Valid sort keys are:</p>
<dd><code>uid</code><br />
&nbsp;<wbr>Nummeric User ID</p>
<dd><code>certid</code><br />
&nbsp;<wbr>Nummeric Certificate ID</p>
<dd><code>accessprofile</code><br />
&nbsp;<wbr>Nummeric firewall profile ID</p>
<dd><code>registered</code><br />
&nbsp;<wbr>According to when the user-cert was registered</p>
<dd><code>uicid</code><br />
&nbsp;<wbr>Nummeric user-cert link ID</dl>
<h2>Set Fw Profile Mode</h2>
<p>The set-fwprofile mode will update the firewall access profile for a given user-cert link </p>
<p> Options: (both required)</p>
<dl>
<dt><code>-n</code> | <code>&#8211;uicid</code></p>
<dd>Unique record id of certificate and user account link</p>
<dt><code>-a</code> | <code>&#8211;accessprofile</code></p>
<dd>Firewall profile ID</dl>
<h2>Add Mode</h2>
<p>The add mode will register a new link between a user account and a certificate.</p>
<dl>
<dt><code>-c</code> | <code>&#8211;certid</code></p>
<dd>Required &#8211; Certificate ID</p>
<dt><code>-i</code> | <code>&#8211;uid</code></p>
<dd>Required &#8211; User account ID</p>
<dt><code>-a</code> | <code>&#8211;accessprofile</code></p>
<dd>Firewall profile ID to use for this access</dl>
<h2>Delete Mode</h2>
<p>The delete mode will delete a link between a user account and a certificate.</p>
<dl>
<dt><code>-c</code> | <code>&#8211;certid</code></p>
<dd>Certificate ID</p>
<dt><code>-i</code> | <code>&#8211;uid</code></p>
<dd>User account ID</p>
<dt><code>-n</code> | <code>&#8211;uicid</code></p>
<dd>Unique record id of certificate and user account link</p>
<dt><code>-a</code> | <code>&#8211;accessprofile</code></p>
<dd>Firewall profile ID</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm-users/">eurephiadm-users</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-certs/">eurephiadm-certs</a></code>(7), <code><a href="/docs/linux/man/7-eurephiadm-fwprofiles/">eurephiadm-fwprofiles</a></code>(7)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
