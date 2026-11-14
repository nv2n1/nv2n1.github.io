---
title: "nss-systemd(8)"
name: "nss-systemd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nss-systemd/"
description: "nss-systemd, libnss_systemd.so.2 – UNIX user and group name resolution for user/group lookup via Varlink"
---

<p>nss-systemd, libnss_systemd.so.2 &#8211; UNIX user and group name resolution for user/group lookup via Varlink</p>
<h2>Synopsis</h2>
<p>libnss_systemd.so.2</p>
<h2>Description</h2>
<p><code>nss-systemd</code> is a plug-in module for the GNU Name Service Switch (NSS) functionality of the GNU C Library (<code>glibc</code>), providing UNIX user and group name resolution for services implementing the m[blue]<code>User/Group Record Lookup API via Varlink</code>m[]<font SIZE="-2">[1]</font>, such as the system and service manager <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) (for its <i>DynamicUser=</i> feature, see <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5) for details), <code><a href="/docs/linux/man/8-systemd-homed-service/">systemd-homed.service</a></code>(8), or <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8). </p>
<p> This module also ensures that the root and nobody users and groups (i.e. the users/groups with the UIDs/GIDs 0 and 65534) remain resolvable at all times, even if they aren&#8217;t listed in /etc/passwd or /etc/group, or if these files are missing. </p>
<p> This module preferably utilizes <code><a href="/docs/linux/man/8-systemd-userdbd-service/">systemd-userdbd.service</a></code>(8) for resolving users and groups, but also works without the service running. </p>
<p> To activate the NSS module, add &quot;systemd&quot; to the lines starting with &quot;passwd:&quot;, &quot;group:&quot;, &quot;shadow:&quot; and &quot;gshadow:&quot; in /etc/nsswitch.conf. </p>
<p> It is recommended to place &quot;systemd&quot; after the &quot;files&quot; or &quot;compat&quot; entry of the /etc/nsswitch.conf lines so that /etc/passwd, /etc/group, /etc/shadow and /etc/gshadow based mappings take precedence.</p>
<h2>Static Drop-In Json User/Group Records</h2>
<p>Besides user/group records acquired via the aforementioned Varlink IPC interfaces and the synthesized root and nobody accounts, this module also makes user and group accounts available to the system that are defined in static drop-in files in the /etc/userdb/, /run/userdb/, /run/host/userdb/ and /usr/lib/userdb/ directories. </p>
<p> This is a simple mechanism to provide static user and group records via JSON drop-in files. Such user records should be defined in the format described by the m[blue]<code>JSON User Records</code>m[]<font SIZE="-2">[2]</font> specification and be placed in one of the aforementioned directories under a file name composed of the user name suffixed with .user, with a world-readable access mode. A symlink named after the user record&#8217;s UID formatted in decimal and suffixed with .user pointing to the primary record file should be created as well, in order to allow both lookups by username and by UID. Privileged user record data (e.g. hashed UNIX passwords) may optionally be provided as well, in a pair of separate companion files with the .user-privileged suffix. The data should be stored in a regular file named after the user name, suffixed with .user-privileged, and a symlink pointing to it, named after the used numeric UID formatted in decimal with the same suffix. These companion files should not be readable to anyone but root. Example: </p>
<dl>
<dd>
<pre>-rw-r--r--. 1 root root 723 May 10 foobar.user
-rw-------. 1 root root 123 May 10 foobar.user-privileged
lrwxrwxrwx. 1 root root 19 May 10 4711.user -&gt; foobar.user
lrwxrwxrwx. 1 root root 19 May 10 4711.user-privileged -&gt; foobar.user-privileged</pre>
</dl>
<p> Similarly, group records following the format described in m[blue]<code>JSON Group Record</code>m[]<font SIZE="-2">[3]</font> may be defined, using the file suffixes .group and .group-privileged. </p>
<p> The primary user/group record files (i.e. those with the .user and .group suffixes) should not contain the &quot;privileged&quot; section as described in the specifications. The privileged user/group record files (i.e. those with the .user-privileged and .group-privileged suffixes) should contain this section, exclusively. </p>
<p> Note that static user/group records generally do not override conflicting records in /etc/passwd or /etc/group or other account databases. In fact, before dropping in these files a reasonable level of care should be taken to avoid user/group name and UID/GID conflicts.</p>
<h2>Configuration In /Etc/Nsswitch.Conf</h2>
<p>Here is an example /etc/nsswitch.conf file that enables <code>nss-systemd</code> correctly: </p>
<dl>
<dd>
<pre>passwd: compat <code>systemd</code>
group: compat [SUCCESS=merge] <code>systemd</code>
shadow: compat <code>systemd</code>
gshadow: files <code>systemd</code>
hosts: mymachines resolve [!UNAVAIL=return] files myhostname dns
networks: files
protocols: db files
services: db files
ethers: db files
rpc: db files
netgroup: nis</pre>
</dl>
<h2>Example: Mappings Provided By Systemd-Machined.Service</h2>
<p>The container &quot;rawhide&quot; is spawned using <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1): </p>
<dl>
<dd>
<pre># systemd-nspawn -M rawhide --boot --network-veth --private-users=pick
Spawning container rawhide on /var/lib/machines/rawhide.
Selected user namespace base 20119552 and range 65536.
...
$ machinectl --max-addresses=3
MACHINE CLASS SERVICE OS VERSION ADDRESSES
rawhide container systemd-nspawn fedora 30 169.254.40.164 fe80::94aa:3aff:fe7b:d4b9
$ getent passwd vu-rawhide-0 vu-rawhide-81
vu-rawhide-0:*:20119552:65534:vu-rawhide-0:/:/usr/sbin/nologin
vu-rawhide-81:*:20119633:65534:vu-rawhide-81:/:/usr/sbin/nologin
$ getent group vg-rawhide-0 vg-rawhide-81
vg-rawhide-0:*:20119552:
vg-rawhide-81:*:20119633:
$ ps -o user:15,pid,tty,command -e|grep '^vu-rawhide'
vu-rawhide-0 692 ? /lib/systemd/systemd
vu-rawhide-0 731 ? /lib/systemd/systemd-journald
vu-rawhide-192 734 ? /lib/systemd/systemd-networkd
vu-rawhide-193 738 ? /lib/systemd/systemd-resolved
vu-rawhide-0 742 ? /lib/systemd/systemd-logind
vu-rawhide-81 744 ? /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
vu-rawhide-0 746 ? /usr/sbin/sshd -D ...
vu-rawhide-0 752 ? /lib/systemd/systemd --user
vu-rawhide-0 753 ? (sd-pam)
vu-rawhide-0 1628 ? login -- zbyszek
vu-rawhide-1000 1630 ? /lib/systemd/systemd --user
vu-rawhide-1000 1631 ? (sd-pam)
vu-rawhide-1000 1637 pts/8 -zsh</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-exec/">systemd.exec</a></code>(5), <code><a href="/docs/linux/man/8-nss-resolve/">nss-resolve</a></code>(8), <code><a href="/docs/linux/man/8-nss-myhostname/">nss-myhostname</a></code>(8), <code><a href="/docs/linux/man/8-nss-mymachines/">nss-mymachines</a></code>(8), <code><a href="/docs/linux/man/8-systemd-userdbd-service/">systemd-userdbd.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-homed-service/">systemd-homed.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-machined-service/">systemd-machined.service</a></code>(8), <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5), <code><a href="/docs/linux/man/1-getent/">getent</a></code>(1)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>User/Group Record Lookup API via Varlink</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/USER_GROUP_API">https://systemd.io/USER_GROUP_API</a></dl>
<dt> 2.</p>
<dd>JSON User Records</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/USER_RECORD">https://systemd.io/USER_RECORD</a></dl>
<dt> 3.</p>
<dd>JSON Group Record</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/GROUP_RECORD">https://systemd.io/GROUP_RECORD</a></dl>
