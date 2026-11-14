---
title: "systemd-cryptsetup(8)"
name: "systemd-cryptsetup"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-cryptsetup/"
description: "systemd-cryptsetup [at] .service, systemd-cryptsetup – Full disk decryption logic"
---

<p>systemd-cryptsetup [at] .service, systemd-cryptsetup &#8211; Full disk decryption logic</p>
<h2>Synopsis</h2>
<p>systemd-cryptsetup [at] .service </p>
<p> /usr/lib/systemd/systemd-cryptsetup</p>
<h2>Description</h2>
<p>systemd-cryptsetup [at] .service is a service responsible for setting up encrypted block devices. It is instantiated for each device that requires decryption for access. </p>
<p> systemd-cryptsetup [at] .service will ask for hard disk passwords via the m[blue]<code>password agent logic</code>m[]<font SIZE="-2">[1]</font>, in order to query the user for the password using the right mechanism at boot and during runtime. </p>
<p> At early boot and when the system manager configuration is reloaded this /etc/crypttab is translated into systemd-cryptsetup [at] .service units by <code><a href="/docs/linux/man/8-systemd-cryptsetup-generator/">systemd-cryptsetup-generator</a></code>(8).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-cryptsetup-generator/">systemd-cryptsetup-generator</a></code>(8), <code><a href="/docs/linux/man/5-crypttab/">crypttab</a></code>(5), <code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>password agent logic</p>
<dl>
<dd><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/systemd/PasswordAgents">http://www.freedesktop.org/wiki/Software/systemd/PasswordAgents</a></dl>
