---
title: "systemd-hibernate-resume-service(8)"
name: "systemd-hibernate-resume-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-hibernate-resume-service/"
description: "systemd-hibernate-resume [at] .service, systemd-hibernate-resume – Resume from hibernation"
---

<p>systemd-hibernate-resume [at] .service, systemd-hibernate-resume &#8211; Resume from hibernation</p>
<h2>Synopsis</h2>
<p>systemd-hibernate-resume [at] .service </p>
<p> /lib/systemd/systemd-hibernate-resume</p>
<h2>Description</h2>
<p>systemd-hibernate-resume [at] .service initiates the resume from hibernation. It is instantiated with the device to resume from as the template argument. </p>
<p> systemd-hibernate-resume only supports the in-kernel hibernation implementation, known as m[blue]<code>swsusp</code>m[]<font SIZE="-2">[1]</font>. Internally, it works by writing the major:minor of specified device node to /sys/power/resume. </p>
<p> Failing to initiate a resume is not an error condition. It may mean that there was no resume image (e. g. if the system has been simply powered off and not hibernated). In such case, the boot is ordinarily continued.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-hibernate-resume-generator/">systemd-hibernate-resume-generator</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>swsusp</p>
<dl>
<dd><a rel="nofollow" href="https://www.kernel.org/doc/Documentation/power/swsusp.txt">https://www.kernel.org/doc/Documentation/power/swsusp.txt</a></dl>
