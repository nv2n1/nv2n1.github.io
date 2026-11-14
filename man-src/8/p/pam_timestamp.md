---
title: "pam_timestamp(8)"
name: "pam_timestamp"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_timestamp/"
description: "pam_timestamp – Authenticate using cached successful authentication attempts"
---

<p>pam_timestamp &#8211; Authenticate using cached successful authentication attempts</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_timestamp.so</code> [timestampdir=<i>directory</i>] [timestamp_timeout=<i>number</i>] [verbose] [debug]</dl>
<h2>Description</h2>
<dd>In a nutshell, <i>pam_timestamp</i> caches successful authentication attempts, and allows you to use a recent successful attempt as the basis for authentication. This is similar mechanism which is used in <code>sudo</code>. </p>
<p> When an application opens a session using <i>pam_timestamp</i>, a timestamp file is created in the <i>timestampdir</i> directory for the user. When an application attempts to authenticate the user, a <i>pam_timestamp</i> will treat a sufficiently recent timestamp file as grounds for succeeding.</p>
<h2>Options</h2>
<p><code>timestampdir=</code><i>directory</i></p>
<dl>
<dd>Specify an alternate directory where <i>pam_timestamp</i> creates timestamp files.</dl>
<p> <code>timestamp_timeout=</code><i>number</i></p>
<dl>
<dd>How long should <i>pam_timestamp</i> treat timestamp as valid after their last modification date (in seconds). Default is 300 seconds.</dl>
<p> <code>verbose</code></p>
<dl>
<dd>Attempt to inform the user when access is granted.</dl>
<p> <code>debug</code></p>
<dl>
<dd>Turns on debugging messages sent to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3).</dl>
<h2>Module Types Provided</h2>
<p>The <code>auth</code> and <code>session</code> module types are provided.</p>
<h2>Return Values</h2>
<p>PAM_AUTH_ERR</p>
<dl>
<dd>The module was not able to retrieve the user name or no valid timestamp file was found.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Everything was successful.</dl>
<p> PAM_SESSION_ERR</p>
<dl>
<dd>Timestamp file could not be created or updated.</dl>
<h2>Notes</h2>
<p>Users can get confused when they are not always asked for passwords when running a given program. Some users reflexively begin typing information before noticing that it is not being asked for.</p>
<h2>Examples</h2>
<dl>
<dd>
<pre>auth sufficient pam_timestamp.so verbose
auth required pam_unix.so
session required pam_unix.so
session optional pam_timestamp.so</pre>
</dl>
<h2>Files</h2>
<p>/var/run/pam_timestamp/&#8230;</p>
<dl>
<dd>timestamp files and directories</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_timestamp_check/">pam_timestamp_check</a></code>(8), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7)</p>
<h2>Author</h2>
<p>pam_timestamp was written by Nalin Dahyabhai.</p>
