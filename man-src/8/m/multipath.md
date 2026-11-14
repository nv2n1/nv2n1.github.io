---
title: "multipath(8)"
name: "multipath"
section: "8"
letter: "m"
url: "/docs/linux/man/8-multipath/"
description: "multipath – Device mapper target autoconfig"
---

<p>multipath &#8211; Device mapper target autoconfig</p>
<h2>Synopsis</h2>
<p><code>multipath</code> [<code>-v&nbsp;<wbr></code><i>verbosity</i>] [<code>-b&nbsp;<wbr></code><i>bindings_file</i>] [<code>-d</code>] [<code>-h</code>|<code>-l</code>|<code>-ll</code>|<code>-f</code>|<code>-t</code>|<code>-F</code>|<code>-B</code>|<code>-c</code>|<code>-q</code>|<code>-r</code>|<code>-r</code>|<code>-a</code>|<code>-A</code>|<code>-w</code>|<code>]</code> [<code>-p&nbsp;<wbr></code><code>failover</code>|<code>multibus</code>|<code>group_by_serial</code>|<code>group_by_prio</code>|<code>group_by_node_name</code>] [<code>device</code>]</p>
<h2>Description</h2>
<p><code>multipath</code> is used to detect multiple paths to devices for fail-over or performance reasons and coalesces them</p>
<h2>Options</h2>
<dl>
<dt><code>-v level</code></p>
<dd>verbosity, print all paths and multipaths</p>
<dl>
<dd>
<dl>
<dt><code>0</code></p>
<dd>no output</p>
<dt><code>1</code></p>
<dd>print the created or updated multipath names only, for use to feed other tools like kpartx</p>
<dt><code>2 +</code></p>
<dd>print all info : detected paths, coalesced paths (ie multipaths) and device maps</dl>
</dl>
<dt><code>-h</code></p>
<dd>print usage text</p>
<dt><code>-d</code></p>
<dd>dry run, do not create or update devmaps</p>
<dt><code>-l</code></p>
<dd>show the current multipath topology from information fetched in sysfs and the device mapper</p>
<dt><code>-ll</code></p>
<dd>show the current multipath topology from all available information (sysfs, the device mapper, path checkers &#8230;)</p>
<dt><code>-f</code></p>
<dd>flush a multipath device map specified as parameter, if unused</p>
<dt><code>-F</code></p>
<dd>flush all unused multipath device maps</p>
<dt><code>-t</code></p>
<dd>print internal hardware table to stdout</p>
<dt><code>-r</code></p>
<dd>force devmap reload</p>
<dt><code>-i</code></p>
<dd>ignore wwids file when processing devices</p>
<dt><code>-B</code></p>
<dd>treat the bindings file as read only</p>
<dt><code>-b bindings_file</code></p>
<dd>set user_friendly_names bindings file location. The default is /etc/multipath/bindings</p>
<dt><code>-c</code></p>
<dd>check if a block device should be a path in a multipath device</p>
<dt><code>-q</code></p>
<dd>allow device tables with queue_if_no_path when multipathd is not running</p>
<dt><code>-a</code></p>
<dd>add the wwid for the specified device to the wwids file</p>
<dt><code>-A</code></p>
<dd>add wwids from any kernel command line mpath.wwid parameters to the wwids file</p>
<dt><code>-w</code></p>
<dd>remove the wwid for the specified device from the wwids file</p>
<dt><code>-W</code></p>
<dd>reset the wwids file to only include the current multipath devices</p>
<dt><code>-T tm:valid</code></p>
<dd>check if <i>tm</i> matches the multipathd configuration timestamp value from <i>/run/multipathd/timestamp</i> If so, return success if <i>valid</i> is 1. Otherwise, return failure. If the timestamp doesn&#8217;t match continue with multipath execution. This option is designed to be used with -c by the udev rules.</p>
<dt><code>-p</code><i> policy</i></p>
<dd>force new maps to use the specified policy:</p>
<dl>
<dd>
<dl>
<dt><code>failover</code></p>
<dd>1 path per priority group</p>
<dt><code>multibus</code></p>
<dd>all paths in 1 priority group</p>
<dt><code>group_by_serial</code></p>
<dd>1 priority group per serial</p>
<dt><code>group_by_prio</code></p>
<dd>1 priority group per priority value. Priorities are determined by callout programs specified as a global, per-controller or per-multipath option in the configuration file</p>
<dt><code>group_by_node_name</code></p>
<dd>1 priority group per target node name. Target node names are fetched in /sys/class/fc_transport/target*/node_name.</p>
<dt></dl>
</dl>
<dd>Existing maps are not modified.</p>
<dt><code>device</code></p>
<dd>update only the devmap the path pointed by <i>device</i> is in. <i>device</i> is in the /dev/sdb (as shown by udev in the $DEVNAME variable) or major:minor format. <i>device</i> may alternatively be a multipath mapname</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-multipathd/">multipathd</a></code>(8), <code><a href="/docs/linux/man/5-multipath-conf/">multipath.conf</a></code>(5), <code><a href="/docs/linux/man/8-kpartx/">kpartx</a></code>(8), <code><a href="/docs/linux/man/8-udev/">udev</a></code>(8), <code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8) <code><a href="/docs/linux/man/8-hotplug/">hotplug</a></code>(8)</p>
<h2>Authors</h2>
<p><code>multipath</code> was developed by Christophe Varoqui, &lt;christophe.varoqui [at] opensvc.com&gt; and others.</p>
