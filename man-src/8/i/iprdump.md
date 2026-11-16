---
title: "iprdump(8)"
name: "iprdump"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iprdump/"
description: "iprdump – IBM Power RAID adapter dump utility"
---

<p>iprdump &#8211; IBM Power RAID adapter dump utility</p>
<h2>Synopsis</h2>
<p><code>iprdump [-d directory]</code> </p>
<p> <code>iprdump &#8211;version &#8211;debug &#8211;use-polling &#8211;use-uevents</code></p>
<h2>Description</h2>
<p><code>iprdump</code> is used to gather information in the event of an adapter failure. The dump data will by default be saved in the /var/log/ directory with the prefix iprdump.# where # will be the dump ID of the file. The ipr dump utility will make a log in the system error log when a dump is taken. Iprdump should be started as a service daemon instead of run directly. Nevertheless, it can also be started at any time and will properly handle adapters being dynamically added and removed from the system. When it is run directly it will stay running forever in order to process any dump that might occur. You can start it with &quot;iprdump &#8211;daemon&quot; to force it into the background.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd>Print the version number of <code>iprdump</code></dd>
<dt><code>&#8211;debug</code></dt>
<dd>Enable additional error logging. Enabling this will result in additional errors logging to /var/log/messages.</dd>
<dt><code>-d &lt;directory&gt;</code></dt>
<dd>Directory where dump data is to be stored. Default is /var/log/.</dd>
<dt><code>&#8211;use-polling</code></dt>
<dd>Do not use netlink/uevent notification, but rather poll for adapter and device configuration changes.</dd>
<dt><code>&#8211;use-uevents</code></dt>
<dd>Use netlink/uevent notification rather than polling for adapter and device configuration changes. If not specified, polling will be used until the first uevent notification appears, then netlink will be used.</dd>
<dt><code>&#8211;daemon</code></dt>
<dd>Force the daemon to be run in the background</dd></dl>
<h2>Author</h2>
<p>Originally written by Michael Anderson &lt;mjanders [at] us.ibm.com&gt;. Rewritten for the 2.6 kernel by Brian King &lt;brking [at] us.ibm.com&gt;.</p>
