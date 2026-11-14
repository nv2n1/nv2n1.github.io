---
title: "virt-who-password(8)"
name: "virt-who-password"
section: "8"
letter: "v"
url: "/docs/linux/man/8-virt-who-password/"
description: "virt-who-password – Utility that encrypts passwords for virt-who."
---

<p>virt-who-password &#8211; Utility that encrypts passwords for virt-who.</p>
<h2>Synopsis</h2>
<p>virt-who-password [-h|&#8211;help]</p>
<h2>Usage</h2>
<p>virt-who-password prompts for password and writes encrypted entered password to the standard output. </p>
<p> This utility must be executed as root, because the encryption key is written into file that is only readable by root. Note that root can decrypt the password. </p>
<p> Encryption key is written into file <code>/var/lib/virt-who/key</code>, make sure that this file is only readable and writable by root.</p>
<h2>Author</h2>
<p>Radek Novacek &lt;rnovacek at redhat dot com&gt;</p>
