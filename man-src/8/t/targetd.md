---
title: "targetd(8)"
name: "targetd"
section: "8"
letter: "t"
url: "/docs/linux/man/8-targetd/"
description: "targetd"
---

<p><code>targetd</code></p>
<h2>Description</h2>
<p><code>targetd</code> is a service to allow the remote configuration of block device volumes and file systems within dedicated pools. Block devices can be exported to other hosts via iSCSI, and filesystems can be exported via NFS.</p>
<h2>Usage</h2>
<p>Run <code>targetd</code> as root.</p>
<h2>Configuration</h2>
<p><code>targetd</code> uses <code>/etc/target/targetd.yaml</code> for configuration. It is in YAML format. <code>targetd</code> currently uses scalar values and collection values, see example for details.</p>
<h3>Configuration File Settings</h3>
<p><code>block_pools</code><br />
 Sets the LVM Volume Group(s) that targetd will use to allocate volumes. Defaults to &quot;vg-targetd&quot;. </p>
<p> Alternatively, targetd can allocate thinp (thin-provisioned) volumes out of a thinpool LV. These should be listed as &quot;&lt;vgname&gt;/&lt;poolname&gt;&quot;, with the VG and thinpool LV names separated by a &quot;/&quot;. These should already be created; targetd will not create VGs or thinpool LVs. </p>
<p> <code>fs_pools</code><br />
 Sets the mount point(s) that targetd will use to export filesystems over NFS. Defaults to none. </p>
<p> <code>user</code><br />
 <code>password</code><br />
 Sets the username and password required to use the remote API. &quot;user&quot; defaults to <code>admin</code>, but password must be set prior to using targetd. </p>
<p> <code>target_name</code><br />
 Sets the iSCSI target name that <code>targetd</code> will use. Default is <code>iqn.2003-01.org.linux-iscsi.&lt;hostname&gt;:targetd</code>. </p>
<p> <code>ssl</code><br />
 <code>ssl_key</code><br />
 <code>ssl_cert</code><br />
 Settings for enabling SSL/TLS encryption. <code>ssl</code> defaults to <code>off</code>. If enabled, it will default to looking for key and cert files named <code>targetd_key.pem</code> and <code>targetd_cert.pem</code> in <code>/etc/target</code>. These paths may also be specified, using the <code>ssl_key</code> and <code>ssl_cert</code> config settings. </p>
<p> Key and self-signed cert may be generated using openssl: </p>
<p> <code>openssl genrsa -out targetd_key.pem 2048</code><br />
 <code>openssl req -new -x509 -key targetd_key.pem -out targetd_cert.pem -days 9999</code></p>
<h2>Files</h2>
<p><code>/etc/target/targetd.yaml</code><br />
 <code>/etc/target/targetd_key.pem</code><br />
 <code>/etc/target/targetd_cert.pem</code></p>
<h2>See Also</h2>
<p>The remote API is defined at<br />
 &lt;<a rel="nofollow" href="https://github.com/agrover/targetd/blob/master/API.md">https://github.com/agrover/targetd/blob/master/API.md</a>&gt;. </p>
<p> <a href="/docs/linux/man/8-targetcli/">targetcli</a>(8), <a href="/docs/linux/man/8-lvm/">lvm</a>(8), <a href="/docs/linux/man/8-lsmcli/">lsmcli</a>(8)</p>
<h2>Author</h2>
<p>Written by Andy Grover &lt;agrover [at] redhat.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs via &lt;targetd-devel [at] lists.fedorahosted.org&gt;<br />
 or &lt;<a rel="nofollow" href="https://github.com/agrover/targetd/issues">https://github.com/agrover/targetd/issues</a>&gt;</p>
