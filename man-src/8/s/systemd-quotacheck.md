---
title: "systemd-quotacheck(8)"
name: "systemd-quotacheck"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-quotacheck/"
description: "systemd-quotacheck.service, systemd-quotacheck – File system quota checker logic"
---

<p>systemd-quotacheck.service, systemd-quotacheck &#8211; File system quota checker logic</p>
<h2>Synopsis</h2>
<p>systemd-quotacheck.service </p>
<p> /lib/systemd/systemd-quotacheck</p>
<h2>Description</h2>
<p>systemd-quotacheck.service is a service responsible for file system quota checks. It is run once at boot after all necessary file systems are mounted. It is pulled in only if at least one file system has quotas enabled.</p>
<h2>Kernel Command Line</h2>
<p>systemd-quotacheck understands one kernel command line parameter: </p>
<p> <i>quotacheck.mode=</i></p>
<dl>
<dd>One of &quot;auto&quot;, &quot;force&quot;, &quot;skip&quot;. Controls the mode of operation. The default is &quot;auto&quot;, and ensures that file system quota checks are done when the file system quota checker deems them necessary. &quot;force&quot; unconditionally results in full file system quota checks. &quot;skip&quot; skips any file system quota checks.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8), <code>systemd-fsck [at] .service</code>(8) </p>
