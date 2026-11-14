---
title: "corosync-qdevice-net-certutil(8)"
name: "corosync-qdevice-net-certutil"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-qdevice-net-certutil/"
description: "corosync-qdevice-net-certutil – tool to generate qdevice model net TLS certificates"
---

<p>corosync-qdevice-net-certutil &#8211; tool to generate qdevice model net TLS certificates</p>
<h2>Synopsis</h2>
<p><code>corosync-qdevice-net-certutil [-i|-m|-M|-r|-s|-Q] [-c certificate] [-n cluster_name]</code></p>
<h2>Description</h2>
<p><code>corosync-qdevice-net-certutil</code> is a frontend for NSS certutil used for generating client certificate for the net model of qdevice.</p>
<h2>Options</h2>
<dl>
<dt><code>-i</code></p>
<dd>Initialize the QDevice Net NSS certificate database. The default directory for the database is /etc/corosync/qdevice/net/. This directory has to be writable by the current user. It needs the QNetd CA certificate passed as the <code>-c</code> parameter. This certificate can be found on the server running QNetd in the file /etc/corosync/qnetd/nssdb/qnetd-cacert.crt.</p>
<dt><code>-m</code></p>
<dd>Import the cluster certificate and key from a pk12 file.</p>
<dt><code>-r</code></p>
<dd>Generate a certificate request. The certificate request is exported into /etc/corosync/qdevice/net/qdevice-net-node.crq. It is necessary to pass the cluster name using the <code>-n</code> parameter. The cluster name has to match the one defined in /etc/corosync/corosync.conf.</p>
<dt><code>-M</code></p>
<dd>Import a signed certificate and export a certificate with private key into pk12 file.</p>
<dt><code>-Q</code></p>
<dd>Use ssh/scp to properly set both <code>corosync-qnetd</code> and <code>corosync-qdevice</code> certificates on all nodes. It&#8217;s highly recommended that you use an ssh agent, or ssh/scp will keep asking for a password &#8211; roughly 8 times the number of nodes.</p>
<dt><code>-c</code></p>
<dd>File with certificate to load.</p>
<dt><code>-n</code></p>
<dd>Name of the cluster.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync-qnetd/">corosync-qnetd</a></code>(8) <code><a href="/docs/linux/man/8-corosync-qdevice/">corosync-qdevice</a></code>(8)</p>
<h2>Author</h2>
<p>Jan Friesse</p>
