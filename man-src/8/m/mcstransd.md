---
title: "mcstransd(8)"
name: "mcstransd"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mcstransd/"
description: "mcstransd – MCS (Multiple Category System) daemon. Translates SELinux MCS/MLS labels to human readable form."
---

<p>mcstransd &#8211; MCS (Multiple Category System) daemon. Translates SELinux MCS/MLS labels to human readable form. </p>
<h2>Synopsis</h2>
<p><code>mcstransd </code> </p>
<h2>Description</h2>
<p>This manual page describes the <code>mcstransd</code> program. This daemon reads /etc/selinux/{SELINUXTYPE}/setrans.conf and /etc/selinux/{SELINUXTYPE}/secolors.conf configuration files, and communicates with libselinux via a socket in /var/run/setrans. It also watches for files created in /var/run/setrans and uses the contents of these files to generate translations to the names. For example writing a file /var/run/setrans/mydomain with content of s0:c1,c2 will cause mcstrans to translate s0:c1,c2 to mydomain. </p>
<h2>Author</h2>
<p>This man page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;. The program was originally written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;. The program was enhanced/rwwritten by Joe Nall &lt;joe [at] nall.com&gt;.</p>
<h2>Files</h2>
<p>/etc/selinux/{SELINUXTYPE}/setrans.conf</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mcs/">mcs</a></code>(8), </p>
