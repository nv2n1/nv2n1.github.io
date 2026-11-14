---
title: "nfs-systemd(7)"
name: "nfs-systemd"
section: "7"
letter: "n"
url: "/docs/linux/man/7-nfs-systemd/"
description: "nfs.systemd – managing NFS services through systemd."
---

<p>nfs.systemd &#8211; managing NFS services through systemd.</p>
<h2>Synopsis</h2>
<p>nfs-utils.service<br />
 nfs-server.service<br />
 nfs-client.target<br />
 <i>etc</i></p>
<h2>Description</h2>
<p>The <i>nfs-utils</i> package provides a suite of <i>systemd</i> unit files which allow the various services to be started and managed. These unit files ensure that the services are started in the correct order, and the prerequisites are active before dependant services start. As there are quite few unit files, it is not immediately obvious how best to achieve certain results. The following subsections attempt to cover the issues that are most likely to come up.</p>
<h3>Configuration</h3>
<p>The standard systemd unit files do not provide any easy way to pass any command line arguments to daemons so as to configure their behavior. In many case such configuration can be performed by making changes to <i>/etc/nfs.conf</i> or other configuration files. When that is not convenient, a distribution might provide systemd &quot;drop-in&quot; files which replace the <code>ExecStart=</code> setting to start the program with different arguments. For example a drop-in file <code>systemd/system/nfs-mountd.service.d/local.conf</code> containing</p>
<dl>
<dd>
<pre>[Service]
EnvironmentFile=/etc/sysconfig/nfs
ExecStart=
ExecStart= /usr/sbin/rpc.mountd $RPCMOUNTDOPTS</pre>
</dl>
<p> would cause the <code>nfs-mountd.service</code> unit to run the <i>rpc.mountd</i> program using, for arguments, the value given for <code>RPCMOUNTDOPTS</code> in <i>/etc/sysconfig/nfs</i>. This allows for seamless integration with existing configuration tools.</p>
<h3>Enabling unit files</h3>
<p>There are three unit files which are designed to be manually enabled. All others are automatically run as required. The three are:</p>
<dl>
<dt><code>nfs-client.target</code></p>
<dd>This should be enabled on any host which ever serves as an NFS client. There is little cost in transparently enabling it whenever NFS client software is installed.</p>
<dt><code>nfs-server.service</code></p>
<dd>This must be enabled to provide NFS service to clients. It starts and configures the required daemons in the required order.</p>
<dt><code>nfs-blkmap.service</code></p>
<dd>The <code>blkmapd</code> daemon is only required on NFS clients which are using pNFS (parallel NFS), and particularly using the <code>blocklayout</code> layout protocol. If you might use this particular extension to NFS, the <code>nfs-blkmap.service</code> unit should be enabled.</dl>
<p> Several other units which might be considered to be optional, such as <i>rpc-gssd.service</i> are careful to only start if the required configuration file exists. <i>rpc-gsdd.service</i> will not start if the <i>krb5.keytab</i> file does not exist (typically in <i>/etc</i>).</p>
<h3>Restarting NFS services</h3>
<p>Most NFS daemons can be restarted at any time. They will reload any state that they need, and continue servicing requests. This is rarely necessary though. </p>
<p> When configuration changesare make, it can be hard to know exactly which services need to be restarted to ensure that the configuration takes effect. The simplest approach, which is often the best, is to restart everything. To help with this, the <code>nfs-utils.service</code> unit is provided. It declares appropriate dependencies with other unit files so that</p>
<dl>
<dd><code>systemctl restart nfs-utils</code></dl>
<p> will restart all NFS daemons that are running. This will cause all configuration changes to take effect <i>except</i> for changes to mount options lists in <i>/etc/fstab</i> or <i>/etc/nfsmount.conf</i>. Mount options can only be changed by unmounting and remounting filesystem. This can be a disruptive operation so it should only be done when the value justifies the cost. The command</p>
<dl>
<dd><code>umount -a -t nfs; mount -a -t nfs</code></dl>
<p> should unmount and remount all NFS filesystems.</p>
<h3>Masking unwanted services</h3>
<p>Rarely there may be a desire to prohibit some services from running even though there are normally part of a working NFS system. This may be needed to reduce system load to an absolute minimum, or to reduce attack surface by not running daemons that are not absolutely required. </p>
<p> Two particular services which this can apply to are <i>rpcbind</i> and <i>idmapd</i>. <i>rpcbind</i> is not part of the <i>nfs-utils</i> package, but it used by several NFS services. However it is <code>not</code> needed when only NFSv4 is in use. If a site will never use NFSv3 (or NFSv2) and does not want <i>rpcbind</i> to be running, the correct approach is to run</p>
<dl>
<dd><code>systemctl mask rpcbind</code></dl>
<p> This will disable <i>rpcbind</i>, and the various NFS services which depend on it (and are only needed for NFSv3) will refuse to start, without interfering with the operation of NFSv4 services. In particular, <i>rpc.statd</i> will not run when <i>rpcbind</i> is masked. </p>
<p> <i>idmapd</i> is only needed for NFSv4, and even then is not needed when the client and server agree to use user-ids rather than user-names to identify the owners of files. If <i>idmapd</i> is not needed and not wanted, it can be masked with</p>
<dl>
<dd><code>systemctl mask idmapd</code></dl>
<h2>Files</h2>
<p>/etc/nfs.conf<br />
 /etc/nfsmount.conf<br />
 /etc/idmapd.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-nfs-conf/">nfs.conf</a></code>(5), <code><a href="/docs/linux/man/5-nfsmount-conf/">nfsmount.conf</a></code>(5). </p>
