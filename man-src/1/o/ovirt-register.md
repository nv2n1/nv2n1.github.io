---
title: "ovirt-register(1)"
name: "ovirt-register"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ovirt-register/"
description: "ovirt-register – oVirt registration tool for hosts"
---

<h2>NAME</h2>
<p> ovirt-register &#8211; oVirt registration tool for hosts</p>
<h2>SYNOPSIS</h2>
<p> ovirt-register &#8211;engine-fqdn ENGINE_FQDN [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>ovirt-register</code> is a command line tool to register hosts to Engine.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays a list of options.</p>
<dt><code>&#8211;engine-fqdn &lt;engine fqdn&gt;</code></p>
<dd> Specifies the Engine FQND for host registration (See also &#8211;check-fqdn)</p>
<dt><code>&#8211;node-fqdn &lt;node fqdn&gt;</code></p>
<dd> Node FQDN or IP address. If not provided, will be used system host name.</p>
<dt><code>&#8211;node-name &lt;node name&gt;</code></p>
<dd> Define the node name. If not provided, will be used system short host name (the name before the first dot in the system host name)</p>
<dt><code>&#8211;engine-https-port &lt;https port&gt;</code></p>
<dd> Define engine https port. If not provided, will be used 443.</p>
<dt><code>&#8211;ssh-user</code></p>
<dd> SSH username to establish the connection with Engine. If not provided, the user which is executing the script will catch and used.</p>
<dt><code>&#8211;ssh-port</code></p>
<dd> SSH port to establish the connection with Engine. If not provided, the script will use the default SSH port 22.</p>
<dt><code>&#8211;nocheck-fqdn</code></p>
<dd> Disable FQDN check for Engine CA, this option is enabled by default</p>
<dt><code>&#8211;cafile</code></p>
<dd> Specify the full path for the Engine CA file, it will be created if doesn&#8217;t exist.</p>
<dt><code>&#8211;fingerprint</code></p>
<dd> Specify an existing fingerprint to be validated against Engine CA fingerprint.</p>
<dt><code>&#8211;vdsm-port</code></p>
<dd> Specify the listen port of VDSM. If not provided, will be used the default 54321</p>
<dt><code>&#8211;log &lt;file path&gt;</code></p>
<dd> Specify a file to redirect the log</p>
<dt><code>&#8211;force-uuid &lt;UUID&gt;</code></p>
<dd> Force the UUID of machine. It&#8217;s useful for machines that provides duplicate UUID. You might generate the UUID with: cat /proc/sys/kernel/random/uuid</p>
<dt><code>&#8211;nopersist-uuid</code></p>
<dd> Do not Save the UUID in the disk (/etc/vdsm/vdsm.id). The default behaviour is save into the disk. (Use: True or False)</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2015 Red Hat, Inc. License GPLv2: GNU GPL Version 2 &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. </p>
<h2>Index</h2>
