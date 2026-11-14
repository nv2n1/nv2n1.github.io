---
title: "iscsiuio(8)"
name: "iscsiuio"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iscsiuio/"
description: "iscsiuio – iSCSI UserSpace I/O driver"
---

<p>iscsiuio &#8211; iSCSI UserSpace I/O driver</p>
<h2>Synopsis</h2>
<p><code>iscsiuio</code> [<code>-d</code>-f<code>-v</code>] </p>
<h2>Description</h2>
<p>iscsiuio is the UserSpace I/O driver for the QLogic NetXtreme II BCM5706/5708/5709 series PCI/PCI-X Gigabit Ethernet Network Interface Card (NIC) and for the QLogic NetXtreme II BCM57710/57711/57712/57800/57810/57840 series PCI-E 10 Gigabit Ethernet Network Interface Card. The driver has been tested on 2.6.28 kernels and above. </p>
<p> Refer to the README.TXT from the driver package on how to compile and install the driver. </p>
<p> Refer to various Linux documentations on how to configure network protocol and address.</p>
<h2>Driver Dependencies</h2>
<h2>Parameters</h2>
<p>There are very few parameters when running this application.</p>
<dl>
<dt><code>-d</code><i>&lt;debug</i><code>level&gt;</code></p>
<dd>This is to enable debug mode where debug messages will be sent to stdout The following debug modes are supported</dl>
<dl>
<dd>DEBUG 4 &#8211; Print all messages </p>
<p> INFO 3 &#8211; Print messages needed to follow the uIP code (default) </p>
<p> WARN 2 &#8211; Print warning messages </p>
<p> ERROR 1 &#8211; Only print critical errors</dl>
<dl>
<dt>
<dt><code>-f</code></p>
<dd>
<dd>This is to enable foreground mode so that this application doesn&#8217;t get sent into the background.</dl>
<dl>
<dt><code>-v</code></p>
<dd>This is to print the version.</dl>
<dl>
<dt><code>-p</code><i>&lt;pidfile&gt;</i></p>
<dd>Use pidfile (default /var/run/iscsiuio.pid )</dl>
<dl>
<dt><code>-h</code></p>
<dd>Display this help and exit. </p>
</dl>
<h2>Author</h2>
<p>Benjamin Li &#8211; benli [at] broadcom.com </p>
<p> Eddie Wai &#8211; eddie.wai [at] broadcom.com</p>
<h2>Maintained by</h2>
<p>QLogic-Storage-Upstream [at] qlogic.com</p>
