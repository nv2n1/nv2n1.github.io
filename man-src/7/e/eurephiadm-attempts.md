---
title: "eurephiadm-attempts(7)"
name: "eurephiadm-attempts"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephiadm-attempts/"
description: "eurephiadm attempts – Manage the attempts log in eurephia"
---

<p><code>eurephiadm attempts</code> &#8211; Manage the attempts log in eurephia</p>
<h2>Description</h2>
<p>When a remote user fails to authenticate correctly, the attemp will be logged. After a certain amount of attempts the IP address, certificate and/or user account will be blocked. The <code>eurephiadm attempts</code> command is used to get an overview over what is registered as failed attempts and to give the possibility to reset or delete the registered attempts counter. </p>
<p> Available modes for the attempts command are:</p>
<dl>
<dt><code>-D</code> | <code>&#8211;delete</code></p>
<dd>Delete a registered login attempt</p>
<dt><code>-R</code> | <code>&#8211;reset</code></p>
<dd>Reset a registered login attempt</p>
<dt><code>-l</code> | <code>&#8211;list</code></p>
<dd>List all registered login attempts</p>
<dt><code>-h</code> | <code>&#8211;help</code> &lt;mode&gt;</p>
<dd>Show help</dl>
<h2>Delete Mode</h2>
<p>The attempts delete mode will remove a record from the attempts log.</p>
<h3>One of the following parameters must be given (only one):</h3>
<dl>
<dt><code>-u</code> | <code>&#8211;username</code> &lt;username&gt;</p>
<dd>User name to delete</p>
<dt><code>-d</code> | <code>&#8211;digest</code> &lt;SHA1 digest&gt;</p>
<dd>Certificate SHA1 digest to delete</p>
<dt><code>-i</code> | <code>&#8211;ipaddr</code> &lt;IP address&gt;</p>
<dd>IP address to delete</p>
<dt><code>-a</code> | <code>&#8211;attemptid</code> &lt;ID&gt;</p>
<dd>Attempts record ID to delete</dl>
<h2>Reset Mode</h2>
<p>The attempts reset mode will reset the attempt counter.</p>
<h3>One of the following parameters must be given (only one):</h3>
<dl>
<dt><code>-u</code> | <code>&#8211;username</code> &lt;username&gt;</p>
<dd>User name to reset</p>
<dt><code>-d</code> | <code>&#8211;digest</code> &lt;SHA1 digest&gt;</p>
<dd>Certificate SHA1 digest to reset</p>
<dt><code>-i</code> | <code>&#8211;ipaddr</code> &lt;IP address&gt;</p>
<dd>IP address to reset</p>
<dt><code>-a</code> | <code>&#8211;attemptid</code> &lt;ID&gt;</p>
<dd>Attempts record ID to reset</dl>
<h2>List Mode</h2>
<p>The attempts list mode will show all registered login attempts.</p>
<dl>
<dt><code>-v</code> | <code>&#8211;verbose</code></p>
<dd>Show more details</dl>
<h3>Filters:</h3>
<dl>
<dt><code>-u</code> | <code>&#8211;username</code> &lt;username&gt;</p>
<dd>List only attempts matching the given user name</p>
<dt><code>-d</code> | <code>&#8211;digest</code> &lt;SHA1 digest&gt;</p>
<dd>List only attempts matching the given SHA1 certificate digest</p>
<dt><code>-i</code> | <code>&#8211;ipaddr</code> &lt;IP address&gt;</p>
<dd>List only attempts matching the given IP address</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm-blacklist/">eurephiadm-blacklist</a></code>(7), <code><a href="/docs/linux/man/7-eurephia-config/">eurephia-config</a></code>(7)</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
