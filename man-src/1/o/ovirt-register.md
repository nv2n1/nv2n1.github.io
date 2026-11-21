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
<p> ovirt-register &#8211;engine-fqdn ENGINE_FQDN [options]</p>
<p> <code>ovirt-register</code> is a command line tool to register hosts to Engine.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Displays a list of options.</dd>
<dt><code>&#8211;engine-fqdn &lt;engine fqdn&gt;</code></dt>
<dd> Specifies the Engine FQND for host registration (See also &#8211;check-fqdn)</dd>
<dt><code>&#8211;node-fqdn &lt;node fqdn&gt;</code></dt>
<dd> Node FQDN or IP address. If not provided, will be used system host name.</dd>
<dt><code>&#8211;node-name &lt;node name&gt;</code></dt>
<dd> Define the node name. If not provided, will be used system short host name (the name before the first dot in the system host name)</dd>
<dt><code>&#8211;engine-https-port &lt;https port&gt;</code></dt>
<dd> Define engine https port. If not provided, will be used 443.</dd>
<dt><code>&#8211;ssh-user</code></dt>
<dd> SSH username to establish the connection with Engine. If not provided, the user which is executing the script will catch and used.</dd>
<dt><code>&#8211;ssh-port</code></dt>
<dd> SSH port to establish the connection with Engine. If not provided, the script will use the default SSH port 22.</dd>
<dt><code>&#8211;nocheck-fqdn</code></dt>
<dd> Disable FQDN check for Engine CA, this option is enabled by default</dd>
<dt><code>&#8211;cafile</code></dt>
<dd> Specify the full path for the Engine CA file, it will be created if doesn&#8217;t exist.</dd>
<dt><code>&#8211;fingerprint</code></dt>
<dd> Specify an existing fingerprint to be validated against Engine CA fingerprint.</dd>
<dt><code>&#8211;vdsm-port</code></dt>
<dd> Specify the listen port of VDSM. If not provided, will be used the default 54321</dd>
<dt><code>&#8211;log &lt;file path&gt;</code></dt>
<dd> Specify a file to redirect the log</dd>
<dt><code>&#8211;force-uuid &lt;UUID&gt;</code></dt>
<dd> Force the UUID of machine. It&#8217;s useful for machines that provides duplicate UUID. You might generate the UUID with: cat /proc/sys/kernel/random/uuid</dd>
<dt><code>&#8211;nopersist-uuid</code></dt>
<dd> Do not Save the UUID in the disk (/etc/vdsm/vdsm.id). The default behaviour is save into the disk. (Use: True or False)</dd></dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2015 Red Hat, Inc. License GPLv2: GNU GPL Version 2 &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. </p>
