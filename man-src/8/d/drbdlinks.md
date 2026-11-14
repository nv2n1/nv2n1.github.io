---
title: "drbdlinks(8)"
name: "drbdlinks"
section: "8"
letter: "d"
url: "/docs/linux/man/8-drbdlinks/"
description: "drbdlinks – manages links into a shared DRBD partition"
---

<p>drbdlinks &#8211; manages links into a shared DRBD partition</p>
<h2>Synopsis</h2>
<p><code>drbdlinks</code> [<i>OPTION</i>]&#8230; [start|stop|auto|status|monitor|checklinks]</p>
<h2>Description</h2>
<p><code>drbdlinks</code> is a program that will manage creation and removal of symbolic links. It is primarily used with clusters of machines using either shared storage or the &quot;DRBD&quot; replicated block device. While the name of the program is &quot;drbdlinks&quot;, it can be used in any shared-storage sort of environment where the shared storage is only mounted on the active node. In cases like NFS where the shared storage is always mounted on all nodes, drbdlinks is not necessary. The advantage over creating static symbolic links is that package updates often require that directories point at real files, so updates can often fail if you do not have the shared storage mounted. <code>drbdlinks</code> also supports multiple instances of links, in the case of active/active clusters. For example, if you have MySQL running in one resource group, and Apache running in another, you can use the &quot;-c&quot; switch to specify a configuration file for each resource group. A simple configuration file, &quot;/etc/drbdlinks.conf&quot;, specifies the links. This can be used to manage links for /etc/httpd, /var/lib/pgsql, and other system directories that need to appear as if they are local to the system when running applications after a drbd shared partition has been mounted. When run with &quot;start&quot; as the mode, drbdlinks will rename the existing files/directories, and then make symbolic links into the DRBD partition. &quot;stop&quot; does the reverse. Mode &quot;checklinks&quot; will report any links that do not exist in the destination area. During initial setup and configuration, this can help check that you have the destination file-system set up with the required components. If run with &quot;initialize_shared_storage&quot;, destination links specified in the configuration file will be populated from the source storage. This is useful for initial setup to populate the shared storage. Preceding paths will be populated if they share the same name from source to destination. The &quot;monitor&quot; and &quot;status&quot; modes will check the file-system against the configuration file and will report &quot;running&quot; (monitor mode) or &quot;OK&quot; (status mode) if all links appear to be up. Otherwise they report &quot;down&quot; or &quot;stopped&quot; (respectively). By default, the rename appends .drbdlinks to the name, but this can be overridden in the configuration file. The &quot;list&quot; mode just show the list of links, with each line showing the link, destination, and a 0/1 flag for bindMount status. This may be useful for user scripts without having to parse the configuration. An init script is included which runs &quot;stop&quot; before heartbeat starts, and after heartbeat stops. This is done to try to ensure that when the shared partition isn&#8217;t mounted, the links are in their normal state. </p>
<h2>Options</h2>
<p><code>drbdlinks</code> has several options, using either short or long variants. </p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Print a short help message describing the available options and exit. </p>
<dt><code>-c, &#8211;config-file=CONFIGFILE</code></p>
<dd>Specify an alternate config file. The default config file is /etc/drbdlinks.conf. Alternate config files should have a &quot;drbdlinks-&quot; prefix, e.g. &quot;drbdlinks-httpd.conf&quot;. </p>
<dt><code>-s, &#8211;suffix=SUFFIX</code></p>
<dd>Name to append to the local file-system name when the link is in place. The default is &quot;drbdlinks&quot;, which would result in a renamed file like &quot;/etc/httpd.drbdlinks&quot;. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Increase verbosity level by 1 for every occurrence of this option. </p>
</dl>
<h2>Examples</h2>
<p>Here are a few examples of how drbdlinks can be used. The most straight-forward, and default, method for starting drbdlinks:</p>
<dl>
<dd>drbdlinks start</dl>
<p> To use a suffix different from the default when linking to a file or directory, the -s option can be used, specifying the desired string:</p>
<dl>
<dd>drbdlinks -s orig start</dl>
<p> would rename the file-system name to &quot;name.orig&quot;. Increase the verbosity to assist in debugging:</p>
<dl>
<dd>drbdlinks -v -v start</dl>
<p> Use an alternate configuration file, possibly from with a DRBD mounted file-system:</p>
<dl>
<dd>drbdlinks -c /shared1/drbdlinks-httpd.conf start</dl>
<p> This would use the specified configuration file, found on our DRBD device mounted on /shared1. This would allow us to easily keep drbdlinks configurations tied to a specific set of data on a DRBD disk in an active/active sort of HA configuration. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-drbd/">DRBD</a></code>(8), <code><a href="/docs/linux/man/8-drbdadm/">drbdadm</a></code>(8), <code><a href="/docs/linux/man/8-drbdsetup/">drbdsetup</a></code>(8), <code><a href="/docs/linux/man/8-heartbeat/">heartbeat</a></code>(8).</p>
<h2>Author</h2>
<p>drbdlinks was written by Sean Reifschneider &lt;jafo [at] tummy.com&gt;. </p>
<p> This manual page was written by Cyril Bouthors &lt;cyril [at] bouthors.org&gt;, for the Debian project (but may be used by others). Sean Reifschneider modified it for status and monitor arguments, and included it in the base drbdlinks release. Mike Loseke &lt;mike [at] tummy.com&gt; added the sections on options and examples.</p>
