---
title: "systemd-hibernate-resume-generator(8)"
name: "systemd-hibernate-resume-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-hibernate-resume-generator/"
description: "systemd-hibernate-resume-generator – Unit generator for resume= kernel parameter"
---

<p>systemd-hibernate-resume-generator &#8211; Unit generator for resume= kernel parameter</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-hibernate-resume-generator</p>
<h2>Description</h2>
<p><code>systemd-hibernate-resume-generator</code> is a generator that initiates the procedure to resume the system from hibernation. It instantiates the <code>systemd-hibernate-resume [at] .service</code>(8) unit according to the value of <code>resume=</code> parameter specified on the kernel command line, which will instruct the kernel to resume the system from the hibernation image on that device.</p>
<h2>Kernel Command Line</h2>
<p>systemd-hibernate-resume-generator understands the following kernel command line parameters: </p>
<p> <i>resume=</i></p>
<dl>
<dd>Takes a path to the resume device. Both persistent block device paths like /dev/disk/by-foo/bar and <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5)-style specifiers like &quot;FOO=bar&quot; are supported.</dl>
<p> <i>resumeflags=</i></p>
<dl>
<dd>Takes the resume device mount options to use. Defaults <i>rootflags=</i> if not specified.</dl>
<p> <i>noresume</i></p>
<dl>
<dd>Do not try to resume from hibernation. If this parameter is present, <i>resume=</i> is ignored.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code>systemd-hibernate-resume [at] .service</code>(8), <code><a href="/docs/linux/man/7-kernel-command-line/">kernel-command-line</a></code>(7) </p>
