---
title: "hostname(5)"
name: "hostname"
section: "5"
letter: "h"
url: "/docs/linux/man/5-hostname/"
description: "hostname – Local hostname configuration file"
---

<p>hostname &#8211; Local hostname configuration file</p>
<h2>Synopsis</h2>
<p>/etc/hostname</p>
<h2>Description</h2>
<p>The /etc/hostname file configures the name of the local system. Unless overridden as described in the next section, <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) will set this hostname during boot using the <code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2) system call. </p>
<p> The file should contain a single newline-terminated hostname string. Comments (lines starting with a &quot;#&quot;) are ignored. The hostname should be composed of up to 64 7-bit ASCII lower-case alphanumeric characters or hyphens forming a valid DNS domain name. It is recommended that this name contains only a single label, i.e. without any dots. Invalid characters will be filtered out in an attempt to make the name valid, but obviously it is recommended to use a valid name and not rely on this filtering. </p>
<p> You may use <code><a href="/docs/linux/man/1-hostnamectl/">hostnamectl</a></code>(1) to change the value of this file during runtime from the command line. Use <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) to initialize it on mounted (but not booted) system images.</p>
<h2>Hostname Semantics</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) and the associated tools will obtain the hostname in the following ways: </p>
<dl>
<dd>&bull; If the kernel commandline parameter <i>systemd.hostname=</i> specifies a valid hostname, <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) will use it to set the hostname during early boot, see <code><a href="/docs/linux/man/7-kernel-command-line/">kernel-command-line</a></code>(7),</dl>
<dl>
<dd>&bull; Otherwise, the &quot;static&quot; hostname specified by /etc/hostname as described above will be used.</dl>
<dl>
<dd>&bull; Otherwise, a transient hostname may be set during runtime, for example based on information in a DHCP lease, see <code><a href="/docs/linux/man/8-systemd-hostnamed-service/">systemd-hostnamed.service</a></code>(8). Both m[blue]<code>NetworkManager</code>m[]<font SIZE="-2">[1]</font> and <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8) allow this. Note that <code><a href="/docs/linux/man/8-systemd-hostnamed-service/">systemd-hostnamed.service</a></code>(8) gives higher priority to the static hostname, so the transient hostname will only be used if the static hostname is not configured.</dl>
<dl>
<dd>&bull; Otherwise, a fallback hostname configured at compilation time will be used (&quot;localhost&quot;).</dl>
<p> Effectively, the static hostname has higher priority than a transient hostname, which has higher priority than the fallback hostname. Transient hostnames are equivalent, so setting a new transient hostname causes the previous transient hostname to be forgotten. The hostname specified on the kernel command line is like a transient hostname, with the exception that it has higher priority when the machine boots. Also note that those are the semantics implemented by systemd tools, but other programs may also set the hostname.</p>
<h2>History</h2>
<p>The simple configuration file format of /etc/hostname originates from Debian GNU/Linux.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2), <code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1), <code><a href="/docs/linux/man/7-hostname/">hostname</a></code>(7), <code><a href="/docs/linux/man/5-machine-id/">machine-id</a></code>(5), <code><a href="/docs/linux/man/5-machine-info/">machine-info</a></code>(5), <code><a href="/docs/linux/man/1-hostnamectl/">hostnamectl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-hostnamed-service/">systemd-hostnamed.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>NetworkManager</p>
<dl>
<dd><a rel="nofollow" href="https://developer.gnome.org/NetworkManager/stable/">https://developer.gnome.org/NetworkManager/stable/</a></dl>
