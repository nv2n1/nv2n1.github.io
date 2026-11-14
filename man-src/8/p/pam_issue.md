---
title: "pam_issue(8)"
name: "pam_issue"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_issue/"
description: "pam_issue – PAM module to add issue file to user prompt"
---

<p>pam_issue &#8211; PAM module to add issue file to user prompt</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_issue.so</code> [noesc] [issue=<i>issue-file-name</i>]</dl>
<h2>Description</h2>
<dd>pam_issue is a PAM module to prepend an issue file to the username prompt. It also by default parses escape codes in the issue file similar to some common getty&#8217;s (using ormat). </p>
<p> Recognized escapes: </p>
<p> <code>\d</code></p>
<dl>
<dd>current day</dl>
<p> <code>\l</code></p>
<dl>
<dd>name of this tty</dl>
<p> <code>\m</code></p>
<dl>
<dd>machine architecture (uname -m)</dl>
<p> <code>
</code></p>
<dl>
<dd>machine&#8217;s network node hostname (uname -n)</dl>
<p> <code>\o</code></p>
<dl>
<dd>domain name of this system</dl>
<p> <code></code></p>
<dl>
<dd>release number of operating system (uname -r)</dl>
<p> <code>	</code></p>
<dl>
<dd>current time</dl>
<p> <code>\s</code></p>
<dl>
<dd>operating system name (uname -s)</dl>
<p> <code>
