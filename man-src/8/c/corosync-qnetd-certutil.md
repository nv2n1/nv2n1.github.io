---
title: "corosync-qnetd-certutil(8)"
name: "corosync-qnetd-certutil"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-qnetd-certutil/"
description: "corosync-qnetd-certutil – tool to generate qnetd TLS certificates"
---

<p>corosync-qnetd-certutil &#8211; tool to generate qnetd TLS certificates</p>
<h2>Synopsis</h2>
<p><code>corosync-qnetd-certutil [-i|-s] [-c certificate] [-n cluster_name]</code></p>
<h2>Description</h2>
<p><code>corosync-qnetd-certutil</code> is a frontend for the NSS certutil, it is used for generating the QNetd CA (Certificate Authority), server certificate and signing cluster certificate used by <code>corosync-qdevice</code> when using the model &#8216;net&#8217;.</p>
<h2>Options</h2>
<dl>
<dt><code>-i</code></p>
<dd>Initialize the QNetd NSS certificate database and generate the QNetd CA and server certificates. The default directory for the database is /etc/corosync/qnetd. This directory must be writeable by the current user. The QNetd CA certificate is also exported into the file /etc/corosync/qnetd/nssdb/qnetd-cacert.crt.</p>
<dt><code>-s</code></p>
<dd>Sign the cluster certificate. It is necessary to pass the cluster name (as configured in corosync.conf) and the certificate request file &#8211; see options below. The signed certificate will be written to the file /etc/corosync/qnetd/nssdb/cluster-$ClusterName.crt</p>
<dt><code>-c</code></p>
<dd>Certificate request file to sign.</p>
<dt><code>-n</code></p>
<dd>Name of the cluster.</dl>
<h2>Notes</h2>
<p>If qnetd is executed by a non root user, /etc/corosync/qnetd and its subdirectories must be owned by (or have group access for) the given user. If <code>corosync-qnetd-certutil</code> is executed as root it tries to copy the owner and group of /etc/corosync/qnetd to all of the created files.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync-qnetd/">corosync-qnetd</a></code>(8) <code><a href="/docs/linux/man/8-corosync-qdevice/">corosync-qdevice</a></code>(8)</p>
<h2>Author</h2>
<p>Jan Friesse</p>
