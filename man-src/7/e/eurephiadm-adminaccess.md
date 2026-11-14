---
title: "eurephiadm-adminaccess(7)"
name: "eurephiadm-adminaccess"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephiadm-adminaccess/"
description: "eurephiadm adminaccess – Access control for eurephia administration features"
---

<p><code>eurephiadm adminaccess</code> &#8211; Access control for eurephia administration features</p>
<h2>Description</h2>
<p>The <code>eurephiadm adminaccess</code> is used to grant eurephia users access to the different administration modules in eurephia. </p>
<p> Available modes for the <code>adminaccess</code> command are:</p>
<dl>
<dt><code>-G</code> | <code>&#8211;grant</code></p>
<dd>Grant a specific access level to a user</p>
<dt><code>-R</code> | <code>&#8211;revoke</code></p>
<dd>Revoke access levels</p>
<dt><code>-l</code> | <code>&#8211;list</code></p>
<dd>List all granted accesses</p>
<dt> <code>-h</code> | <code>&#8211;help</code> &lt;mode&gt; Help about a specific mode</dl>
<h2>List Mode</h2>
<dd>The list mode will show the granted user access levels</p>
<dl>
<dt><code>-i</code> | <code>&#8211;uid</code></p>
<dd>User account ID</p>
<dt><code>-u</code> | <code>&#8211;username</code></p>
<dd>User name</p>
<dt><code>-I</code> | <code>&#8211;interface</code></p>
<dd>Which interfaces to show (default &quot;C&quot;)</p>
<dt> <code>-a</code> | <code>&#8211;access-level</code></p>
<dd>Which access level to show</dl>
<h2>Grant Mode</h2>
<p>The grant mode will grant a user access to a specified access level.</p>
<dl>
<dt><code>-i</code> | <code>&#8211;uid</code></p>
<dd>User account ID</p>
<dt><code>-I</code> | <code>&#8211;interface</code></p>
<dd>Grant access through which interface (default &quot;C&quot;)</p>
<dt> <code>-a</code> | <code>&#8211;access-level</code></p>
<dd>Which access level to grant access to</dl>
<h2>Revoke Mode</h2>
<p>The revoke mode will remove an access from the desired user accounts.</p>
<dl>
<dt><code>-i</code> | <code>&#8211;uid</code></p>
<dd>User account ID</p>
<dt><code>-I</code> | <code>&#8211;interface</code></p>
<dd>Revoke access from interface (default &quot;C&quot;)</p>
<dt> <code>-a</code> | <code>&#8211;access-level</code></p>
<dd>Which access level to revoke access from</dl>
<h2>Access Levels</h2>
<dl>
<dt><code>attempts</code></p>
<dd>This access level grants access to the <code>eurephiadm attempts</code> command. The attempts command can list, reset or delete login attempts records in the database.</p>
<dt><code>blacklist</code></p>
<dd>This is similar to the attempts access. It provides access to the <code>eurphiadm blacklist</code> command, where you can list, add or delete blacklisted usernames, certificate digests or IP addresses.</p>
<dt><code>certadmin</code></p>
<dd>This level is needed to use the <code>eurephiadm certs</code> command. This commands provides you access to list, add or delete certificate information which the eurephia plug-in will use during the authentication process.</p>
<dt><code>config</code></p>
<dd>This level grants access to the <code>eurephiadm config</code> and <code>eurephiadm show-config</code> commands. The latter command will list out both the <code>eurephiadm</code> config file and all configuration parameters in the database. The <code>config</code> command is used to set or delete configuration parameters in the database.</p>
<dt><code>fwprofiles</code></p>
<dd>This access level is needed to list, add or delete firewall profiles eurephia which may use.</p>
<dt><code>useradmin</code></p>
<dd>This provides access to the <code>eurephiadm users</code> and <code>eurephiadm usercerts</code> commands, which is used to create or delete user accounts and link the user accounts together with a certificate and a firewall access profile.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm/">eurephiadm</a></code>(7)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
