---
title: "targetctl(8)"
name: "targetctl"
section: "8"
letter: "t"
url: "/docs/linux/man/8-targetctl/"
description: "targetctl – Save and restore configuration of kernel target"
---

<p><code>targetctl</code> &#8211; Save and restore configuration of kernel target</p>
<h2>Description</h2>
<p><code>targetctl</code> is a low-level script to save and restore the configuration of the LIO kernel target, to and from a file in json format. It is not normally meant to be used by end-users directly, but by system init frameworks, or advanced end-users who are generating the configuration file themselves and need a way to load the configuration without relying on the <code>targetcli</code> configuration shell.</p>
<h2>Usage</h2>
<p><code>targetctl</code> must be invoked as root. Exit status will be 0 if successful, or nonzero if an error was encountered. </p>
<p> <code>targetctl save [config-file]</code> </p>
<p> Saves the current configuration of the kernel target to a file in json format. Since the file may contain cleartext passwords, the file&#8217;s permissions will be set to only allow root access. If <code>config-file</code> is not supplied, <code>targetctl</code> will use the default file location, <code>/etc/target/saveconfig.json.</code> </p>
<p> <code>targetctl restore [config-file]</code> </p>
<p> Removes any existing configuration and replaces it with the configuration described in the file. See <code><a href="/docs/linux/man/5-saveconfig-json/">saveconfig.json</a></code>(5) for more details. If parts of the configuration could not be restored, those parts will be noted in the error output, and the rest of the configuration will still be applied. </p>
<p> <code>targetctl clear</code> </p>
<p> Removes any existing configuration from the running kernel target. </p>
<p> <code>targetctl &#8211;help</code> </p>
<p> Displays usage information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-targetcli/">targetcli</a></code>(8), <code><a href="/docs/linux/man/8-targetd/">targetd</a></code>(8), <code><a href="/docs/linux/man/5-saveconfig-json/">saveconfig.json</a></code>(5)</p>
<h2>Files</h2>
<p><code>/etc/target/saveconfig.json</code> </p>
<p> <code>/sys/kernel/config/target</code></p>
<h2>Author</h2>
<p>Written by Andy Grover &lt;agrover [at] redhat.com&gt;.<br />
 Man page written by Andy Grover &lt;agrover [at] redhat.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs via &lt;targetcli-fb-devel [at] lists.fedorahosted.org&gt;<br />
 or &lt;<a rel="nofollow" href="https://github.com/open-iscsi/rtslib-fb/issues">https://github.com/open-iscsi/rtslib-fb/issues</a>&gt;</p>
