---
title: "autofs(8)"
name: "autofs"
section: "8"
letter: "a"
url: "/docs/linux/man/8-autofs/"
description: "Service control for the automounter"
---

<p>Service control for the automounter</p>
<h2>Synopsis</h2>
<p>If a SysV init script system is being used:<br />
 <code>/etc/rc.d/init.d/autofs</code> <i>start|stop|restart|reload|status</i> </p>
<p> or if the systemd init system is being used:<br />
 <code>systemctl</code> <i>start|stop|restart|reload|status</i> <code>autofs.service</code></p>
<h2>Description</h2>
<p><code>autofs</code> controls the operation of the <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8) daemon(s) running on the Linux system. Usually <code>autofs</code> is invoked at system boot time with the <i>start</i> parameter and at shutdown time with the <i>stop</i> parameter. Service control actions can also be manually invoked by the system administrator to shut down, restart, reload or obtain service status. </p>
<h2>Operation</h2>
<p><code>autofs</code> will consult a configuration file <i>/etc/auto.master</i> (see <code><a href="/docs/linux/man/5-auto-master/">auto.master</a></code>(5)) by default to find mount points on the system. For each of those mount points <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8) will mount and start a thread, with the appropriate parameters, to manage the mount point. </p>
<p> <code>/etc/rc.d/init.d/autofs reload</code> or <code>systemctl autofs.service reload</code> will check the current auto.master map against the current automount managed mounts. It will terminate those daemons or threads (depending on <code>autofs</code> version) whose entries have been removed, re-read the automount maps for entries that have changed and start new daemons or threads for entries that have been added. </p>
<p> If an indirect map is modified then the change will become effective immediately. If an indirect map uses the <code>browse</code> option, the master map contains direct mount maps or the <i>auto.master</i> map is modified then the <code>autofs</code> service control reload action must be rerun to activate the changes. </p>
<p> <code>/etc/rc.d/init.d/autofs status</code> or <code>systemctl autofs.service status</code> will display the status of, <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8) ,running or not. When using the systemd init system the status output includes somewhat more information related to the service status. </p>
<p> <code><a href="/docs/linux/man/1-systemctl/">systemctl</a>(1)</code> has more functions than the actions mentioned here, see <code><a href="/docs/linux/man/1-systemctl/">systemctl</a>(1)</code> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-automount/">automount</a></code>(8), <code><a href="/docs/linux/man/5-autofs/">autofs</a></code>(5), <code><a href="/docs/linux/man/5-autofs-conf/">autofs.conf</a></code>(5), <code><a href="/docs/linux/man/5-auto-master/">auto.master</a></code>(5). <code><a href="/docs/linux/man/5-autofs_ldap_auth-conf/">autofs_ldap_auth.conf</a></code>(5) <code><a href="/docs/linux/man/1-systemctl/">systemctl</a>(1)</code></p>
<h2>Author</h2>
<p>This manual page was written by Christoph Lameter &lt;chris [at] waterf.org&gt;, for the Debi GNU/Linux system. Edited by H. Peter Anvin &lt;hpa [at] transmeta.com&gt; and Ian Kent &lt;raven [at] themaw.net&gt;.</p>
