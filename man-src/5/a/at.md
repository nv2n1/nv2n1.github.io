---
title: "at(5)"
name: "at"
section: "5"
letter: "a"
url: "/docs/linux/man/5-at/"
description: "at.allow, at.deny – determine who can submit jobs via at or batch"
---

<p>at.allow, at.deny &#8211; determine who can submit jobs via at or batch</p>
<h2>Description</h2>
<p>The <i>/etc/at.allow</i> and <i>/etc/at.deny</i> files determine which user can submit commands for later execution via <code><a href="/docs/linux/man/1-at/">at</a></code>(1) or <code><a href="/docs/linux/man/1-batch/">batch</a></code>(1)<code>.</code> </p>
<p> The format of the files is a list of usernames, one on each line. Whitespace is not permitted. </p>
<p> If the file <i>/etc/at.allow</i> exists, only usernames mentioned in it are allowed to use <code>at</code>. </p>
<p> If <i>/etc/at.allow</i> does not exist, <i>/etc/at.deny</i> is checked, every username not mentioned in it is then allowed to use <code>at</code>. </p>
<p> An empty <i>/etc/at.deny</i> means that every user may use <code>at</code>. </p>
<p> If neither exists, only the superuser is allowed to use at.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-at/">at</a></code>(1), <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8), <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1), <code><a href="/docs/linux/man/8-atd/">atd</a></code>(8). </p>
