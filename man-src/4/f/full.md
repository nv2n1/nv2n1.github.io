---
title: "full(4)"
name: "full"
section: "4"
letter: "f"
url: "/docs/linux/man/4-full/"
description: "full – always full device"
---

<p>full &#8211; always full device</p>
<h2>Configuration</h2>
<p>If your system does not have <i>/dev/full</i> created already, it can be created with the following commands: </p>
<p> mknod -m 666 /dev/full c 1 7 chown root:root /dev/full</p>
<h2>Description</h2>
<p>The file <i>/dev/full</i> has major device number 1 and minor device number 7. </p>
<p> Writes to the <i>/dev/full</i> device fail with an <code>ENOSPC</code> error. This can be used to test how a program handles disk-full errors. </p>
<p> Reads from the <i>/dev/full</i> device will return 
