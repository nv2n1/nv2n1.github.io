---
title: "eurephiadm-blacklist(7)"
name: "eurephiadm-blacklist"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephiadm-blacklist/"
description: "eurephiadm blacklist – Manage the eurephia blacklist"
---

<p><code>eurephiadm blacklist</code> &#8211; Manage the eurephia blacklist</p>
<h2>Description</h2>
<p>After a configured amount of failed attempts, IP addresses, certificates and/or user names will get blacklisted. The <code>eurephiadm blacklist</code> command can be used to delete blacklist entries, or even explicitly add new blacklist entries manually. </p>
<p> Available modes for the blacklist command are:</p>
<dl>
<dt><code>-l</code> | <code>&#8211;list</code></p>
<dd>List all entries on the blacklist</p>
<dt><code>-A</code> | <code>&#8211;add</code></p>
<dd>Add an entry to the blacklist</p>
<dt><code>-D</code> | <code>&#8211;delete</code></p>
<dd>Delete an entry from the blacklist</p>
<dt><code>-h</code> | <code>&#8211;help</code> [&lt;mode&gt;]</p>
<dd>Show help</dl>
<h2>List Mode</h2>
<p>The blacklist list mode will show registered entries in the blacklist.</p>
<dl>
<dt><code>-v</code> | <code>&#8211;verbose</code></p>
<dd>Show more details</dl>
<h3>Filters:</h3>
<dl>
<dt><code>-u</code> | <code>&#8211;username</code> &lt;username&gt;</p>
<dd>User name</p>
<dt><code>-d</code> | <code>&#8211;digest</code> &lt;SHA1 digest&gt;</p>
<dd>Certificate SHA1 digest</p>
<dt><code>-i</code> | <code>&#8211;ipaddr</code> &lt;ip address&gt;</p>
<dd>IP address</dl>
<h2>Add Mode</h2>
<p>The blacklist add mode will register a new entry to be blacklisted.</p>
<h3>One of the following parameters must be given (only one):</h3>
<dl>
<dt><code>-u</code> | <code>&#8211;username</code> &lt;username&gt;</p>
<dd>User name</p>
<dt><code>-d</code> | <code>&#8211;digest</code> &lt;SHA1 digest&gt;</p>
<dd>Certificate SHA1 digest</p>
<dt><code>-i</code> | <code>&#8211;ipaddr</code> &lt;ip address&gt;</p>
<dd>IP address</dl>
<h2>Delete Mode</h2>
<p>The blacklist delete mode will remove a blacklisted entry.</p>
<h3>One of the following parameters must be given (only one):</h3>
<dl>
<dt><code>-u</code> | <code>&#8211;username</code> &lt;username&gt;</p>
<dd>User name</p>
<dt><code>-d</code> | <code>&#8211;digest</code> &lt;SHA1 digest&gt;</p>
<dd>Certificate SHA1 digest</p>
<dt><code>-i</code> | <code>&#8211;ipaddr</code> &lt;ip address&gt;</p>
<dd>IP address</p>
<dt><code>-b</code> | <code>&#8211;blid</code> &lt;ID&gt;</p>
<dd>Blacklist record ID</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm-attempts/">eurephiadm-attempts</a></code>(7), <code><a href="/docs/linux/man/7-eurephia-config/">eurephia-config</a></code>(7)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
