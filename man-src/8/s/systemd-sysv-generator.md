---
title: "systemd-sysv-generator(8)"
name: "systemd-sysv-generator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-sysv-generator/"
description: "systemd-sysv-generator – Unit generator for SysV init scripts"
---

<p>systemd-sysv-generator &#8211; Unit generator for SysV init scripts</p>
<h2>Synopsis</h2>
<p>/lib/systemd/system-generators/systemd-sysv-generator</p>
<h2>Description</h2>
<p>systemd-sysv-generator is a generator that creates wrapper .service units for m[blue]<code>SysV init</code>m[]<font SIZE="-2">[1]</font> scripts in /etc/init.d/* at boot and when configuration of the system manager is reloaded. This will allow <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) to support them similarly to native units. </p>
<p> m[blue]<code>LSB headers</code>m[]<font SIZE="-2">[2]</font> in SysV init scripts are interpreted, and the ordering specified in the header is turned into dependencies between the generated unit and other units. The LSB facilities &quot;$remote_fs&quot;, &quot;$network&quot;, &quot;$named&quot;, &quot;$portmap&quot;, &quot;$time&quot; are supported and will be turned into dependencies on specific native systemd targets. See <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for more details. </p>
<p> SysV runlevels have corresponding systemd targets (runlevel<i>X</i>.target). The wrapper unit that is generated will be wanted by those targets which correspond to runlevels for which the script is enabled. </p>
<p> <code>systemd</code> does not support SysV scripts as part of early boot, so all wrapper units are ordered after basic.target. </p>
<p> systemd-sysv-generator implements <code><a href="/docs/linux/man/7-systemd-generator/">systemd.generator</a></code>(7).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>SysV init</p>
<dl>
<dd><a rel="nofollow" href="https://savannah.nongnu.org/projects/sysvinit">https://savannah.nongnu.org/projects/sysvinit</a></dl>
<dt> 2.</p>
<dd>LSB headers</p>
<dl>
<dd><a rel="nofollow" href="http://refspecs.linuxbase.org/LSB_3.1.1/LSB-Core-generic/LSB-Core-generic/iniscrptact.html">http://refspecs.linuxbase.org/LSB_3.1.1/LSB-Core-generic/LSB-Core-generic/iniscrptact.html</a></dl>
