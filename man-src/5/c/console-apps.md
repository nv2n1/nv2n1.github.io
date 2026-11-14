---
title: "console-apps(5)"
name: "console-apps"
section: "5"
letter: "c"
url: "/docs/linux/man/5-console-apps/"
description: "console.apps – specify console-accessible privileged applications"
---

<p>console.apps &#8211; specify console-accessible privileged applications</p>
<h2>Description</h2>
<p>The /etc/security/console.apps/ directory should contain one file per application that wishes to allow access to console users. The filename should be the same as the servicename, and the contents are irrelevant; the file may be a zero-length file. The application that the file is used by is free to specify the contents in any way that is useful for it.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_console/">pam_console</a></code>(8)<br />
 <code><a href="/docs/linux/man/5-console-perms/">console.perms</a></code>(5)</p>
<h2>Author</h2>
<p>Michael K. Johnson &lt;johnsonm [at] redhat.com&gt;</p>
