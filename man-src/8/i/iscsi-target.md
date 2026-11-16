---
title: "iscsi-target(8)"
name: "iscsi-target"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iscsi-target/"
description: "iscsi-target – service remote iSCSI requests"
---

<p><code>iscsi-target</code> &#8211; service remote iSCSI requests</p>
<h2>Synopsis</h2>
<p>[-<code>46DV</code> ] [-<code>b </code><i>block length</i> ] [-<code>f </code><i>configuration file</i> ] [-<code>p </code><i>port number</i> ] [-<code>s </code><i>maximum number of sessions</i> ] [-<code>t </code><i>target name</i> ] [-<code>v </code><i>verbose arg</i> ]</p>
<h2>Description</h2>
<p>is the server for iSCSI requests from iSCSI initiators. listens for discovery and login requests on the required port, and responds to those requests appropriately. Options and operands available for <code>iscsi-target</code></p>
<dl>
<dt><code>-4</code></dt>
<dd>will listen for IPv4 connections, and respond back using IPv4. This is the default address family.</dd>
<dt><code>-6</code></dt>
<dd>will listen for IPv6 connections, and respond back using IPv6.</dd>
<dt><code>-b </code><i>blocksize</i></dt>
<dd>Specify the underlying block size for iSCSI storage which will be served. The possible sizes are: 512, 1024, 2048, and 4096 bytes, with the default being 512 bytes.</dd>
<dt><code>-D</code></dt>
<dd>When this option is specified, will not detach itself from the controlling tty, and will not become a daemon. This can be useful for debugging purposes.</dd>
<dt><code>-f </code><i>configfile</i></dt>
<dd>Use the named file as the configuration file. The default file can be found in <i>/etc/iscsi/targets</i> See <a href="/docs/linux/man/5-targets/">targets</a>(5) for more information.</dd>
<dt><code>-p </code><i>port number</i></dt>
<dd>Use the port number provided as the argument as the port on which to listen for iSCSI service requests from initiators.</dd>
<dt><code>-s </code><i>maximum number of sessions</i></dt>
<dd>Allow the maximum number of sessions to be initiated when connecting to the target.</dd>
<dt><code>-t </code><i>filename</i></dt>
<dd>The target name (as it appears to the iSCSI initiator) can be specified using this flag.</dd>
<dt><code>-V</code></dt>
<dd>will print the utility name and version number, and the address for bug reports, and then exit.</dd>
<dt><code>-v </code><i>argument</i></dt>
<dd>The amount of information shown can be varied by using this command. Possible values of <i>argument</i> are <i>net</i> to show network-related information, <i>iscsi</i> to show iSCSI protocol-related information, <i>scsi</i> to show SCSI protocol information, and <i>all</i> to show information from all of the above arguments.</dd></dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/iscsi/targets </code></dt>
<dd>the list of exported storage</dd>
<dt><code>/var/run/iscsi-target.pid </code></dt>
<dd>the PID of the currently running</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-targets/">targets</a>(5)</p>
<h2>History</h2>
<p>The utility first appeared in Nx 4.0 .</p>
