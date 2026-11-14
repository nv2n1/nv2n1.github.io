---
title: "pam_postgresok(8)"
name: "pam_postgresok"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_postgresok/"
description: "pam_postgresok – simple check of real UID and corresponding account name"
---

<p>pam_postgresok &#8211; simple check of real UID and corresponding account name</p>
<h2>Synopsis</h2>
<p><code>auth sufficient pam_postgresok.so</code> </p>
<h2>Description</h2>
<p>pam_postgresok.so is designed to check that the real UID of the calling process belongs to the &quot;postgres&quot; user and equal to 26 (the value assigned to that user on Red Hat Linux systems). </p>
<h2>Arguments</h2>
<dl>
<dt>debug</p>
<dd>Enable module debugging. The module will log its progress to syslog. </p>
</dl>
<h2>Bugs</h2>
<p>Let&#8217;s hope not, but if you find any, please report them via the &quot;Bug Track&quot; link at <a rel="nofollow" href="http://bugzilla.redhat.com/bugzilla/">http://bugzilla.redhat.com/bugzilla/</a> </p>
<h2>Files</h2>
<p>/usr/share/doc/setup-*/uidgid</p>
<h2>Author</h2>
<p>Fernando Nasser &lt;fnasser [at] redhat.com&gt;</p>
