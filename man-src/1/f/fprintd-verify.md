---
title: "fprintd-verify(1)"
name: "fprintd-verify"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fprintd-verify/"
description: "fprintd – Fingerprint management daemon, and test applications"
---

<h2 class="name">NAME</h2>
<p> fprintd &#8211; Fingerprint management daemon, and test applications </p>
<h2>SYNOPSIS</h2>
<p> <code>fprintd-enroll</code> [-f finger] [usename] </p>
<p> <code>fprintd-list</code> username [usernames&#8230;] </p>
<p> <code>fprintd-verify</code> [-f finger] [usename] </p>
<p> <code>fprintd-delete</code> username [usernames&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>fprintd</code> command-line utilities. </p>
<p> The <code>fprintd</code> daemon is accessed through <code>D-Bus</code> by those command-line utilities.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>username</code></p>
<dd> The username for the user for which you want to query or modify the fingerprint database. </p>
<p> Not that <code>fprintd-list</code> and <code>fprintd-delete</code> require at least one username to be passed, and support multiple usernames. </p>
<p> <code>fprintd-enroll</code> and <code>fprintd-verify</code> will use the current username if none are passed on the command-line.</p>
<dt><code>-f finger</code></p>
<dd> For <code>fprintd-enroll</code>, the finger to enroll. Possible values are: </p>
<p> left-thumb, left-index-finger, left-middle-finger, left-ring-finger, left-little-finger, right-thumb, right-index-finger, right-middle-finger, right-ring-finger, right-little-finger. </p>
<p> The default is automatic, selecting the first available finger for swipe devices, or all the enrolled fingers, for press devices.</dl>
<h2>TEST APPLICATIONS</h2>
<h3>fprintd-enroll</h3>
<dl>
<dt>
<dd> Will enroll the user&#8217;s right index finger into the database.</dl>
<h3>fprintd-list</h3>
<dl>
<dt>
<dd> Will list the user&#8217;s enrolled fingerprints.</dl>
<h3>fprintd-verify</h3>
<dl>
<dt>
<dd> Will verify the user&#8217;s fingerprints against the database.</dl>
<h3>fprintd-enroll</h3>
<dl>
<dt>
<dd> Will enroll the user&#8217;s right index finger into the database.</dl>
<h2>AUTHOR</h2>
<p> <code>fprintd</code> was written by Bastien Nocera and Daniel Drake.</p>
<h2>DIRECTORIES</h2>
<p> By default, fprintd stores the fingerprints in <code>/var/lib/fprint/</code></p>
<h2>SEE ALSO</h2>
<dl>
<dt><code>gnome-control-center</code></p>
<dd>
</dl>
<h2>Index</h2>
