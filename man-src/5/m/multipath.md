---
title: "multipath(5)"
name: "multipath"
section: "5"
letter: "m"
url: "/docs/linux/man/5-multipath/"
description: "multipath.conf – multipath daemon configuration file"
---

<p>multipath.conf &#8211; multipath daemon configuration file</p>
<h2>Description</h2>
<p><code>multipath.conf</code> is the configuration file for the multipath daemon. It is used to overwrite the built-in configuration table of <code>multipathd</code>. Any line whose first non-white-space character is a &#8216;#&#8217; is considered a comment line. Empty lines are ignored.</p>
<h2>Syntax</h2>
<p>The configuration file contains entries of the form:</p>
<dl>
<dd>
<pre><code>&lt;section&gt; {
<dl><dt><dd>&lt;attribute&gt; &lt;value&gt;
</code><i>...</i>
<code>&lt;subsection&gt; {
<dl><dt><dd>&lt;attribute&gt; &lt;value&gt;
</code><i>...</i>
</dl>
}
</dl>
}</pre>
</dl>
<p> Each <i>section</i> contains one or more attributes or subsections. The recognized keywords for attributes or subsections depend on the section in which they occor. </p>
<p> The following <i>section</i> keywords are recognized:</p>
<dl>
<dt><code>defaults</code></p>
<dd>This section defines default values for attributes which are used whenever no values are given in the appropriate device or multipath sections.</p>
<dt><code>blacklist</code></p>
<dd>This section defines which devices should be excluded from the multipath topology discovery.</p>
<dt><code>blacklist_exceptions</code></p>
<dd>This section defines which devices should be included in the multipath topology discovery, despite being listed in the <i>blacklist</i> section.</p>
<dt><code>multipaths</code></p>
<dd>This section defines the multipath topologies. They are indexed by a <i>World Wide Identifier</i>(wwid), which is taken to be the value of the udev attribute given by the <i>uid_attribute</i> keyword.</p>
<dt><code>devices</code></p>
<dd>This section defines the device-specific settings.</dl>
<h2>defaults section</h2>
<p>The <code>defaults</code> section recognizes the following keywords:</p>
<dl>
<dt><code>polling_interval</code></p>
<dd>interval between two path checks in seconds. For properly functioning paths, the interval between checks will gradually increase to <code>max_polling_interval;</code> default is <i>5</i></p>
<dt><code>max_polling_interval</code></p>
<dd>maximal interval between two path checks in seconds; default is <i>4 * polling_interval</i></p>
<dt><code>multipath_dir</code></p>
<dd>directory where the dynamic shared objects are stored; default is system dependent, commonly <i>/lib/multipath</i></p>
<dt><code>verbosity</code></p>
<dd>default verbosity. Higher values increase the verbosity level. Valid levels are between 0 and 6; default is <i>2</i></p>
<dt><code>reassign_maps</code></p>
<dd>enable reassigning of device-mapper maps. With this option multipathd will remap existing device-mapper maps to always point to multipath device, not the underlying block devices. Possible values are <i>yes</i> and <i>no</i>. Default is <i>yes</i></p>
<dt><code>path_selector</code></p>
<dd>The default path selector algorithm to use; they are offered by the kernel multipath target. There are three selector algorithms.</p>
<dl>
<dd>
<dl>
<dt><code>round-robin 0</code></p>
<dd>Loop through every path in the path group, sending the same amount of IO to each.</p>
<dt><code>queue-length 0</code></p>
<dd>Send the next bunch of IO down the path with the least amount of outstanding IO.</p>
<dt><code>service-time 0</code></p>
<dd>Choose the path for the next bunch of IO based on the amount of outstanding IO to the path and its relative throughput.</dl>
</dl>
<dt><code>path_grouping_policy</code></p>
<dd>The default path grouping policy to apply to unspecified multipaths. Possible values are</p>
<dl>
<dd>
<dl>
<dt><code>failover</code></p>
<dd>1 path per priority group</p>
<dt><code>multibus</code></p>
<dd>all paths in 1 priority group</p>
<dt><code>group_by_serial</code></p>
<dd>1 priority group per serial number</p>
<dt><code>group_by_prio</code></p>
<dd>1 priority group per priority value. Priorities are determined by callout programs specified as a global, per-controller or per-multipath option in the configuration file.</p>
<dt><code>group_by_node_name</code></p>
<dd>1 priority group per target node name. Target node names are fetched in /sys/class/fc_transport/target*/node_name.</p>
<dt>Default value is <i>failover</i>.</p>
<dd></dl>
</dl>
<dt><code>uid_attribute</code></p>
<dd>The udev attribute providing a unique path identifier. Default value is <i>ID_SERIAL</i></p>
<dt><code>prio</code></p>
<dd>The name of the path priority routine. The specified routine should return a numeric value specifying the relative priority of this path. Higher number have a higher priority. <i>none</i> is a valid value. Currently the following path priority routines are implemented:</p>
<dl>
<dd>
<dl>
<dt><code>const</code></p>
<dd>Return a constant priority of <i>1</i>.</p>
<dt><code>emc</code></p>
<dd>Generate the path priority for EMC arrays.</p>
<dt><code>alua</code></p>
<dd>Generate the path priority based on the SCSI-3 ALUA settings.</p>
<dt><code>ontap</code></p>
<dd>Generate the path priority for NetApp arrays.</p>
<dt><code>rdac</code></p>
<dd>Generate the path priority for LSI/Engenio/NetApp E-Series RDAC controller.</p>
<dt><code>hp_sw</code></p>
<dd>Generate the path priority for Compaq/HP controller in active/standby mode.</p>
<dt><code>hds</code></p>
<dd>Generate the path priority for Hitachi HDS Modular storage arrays.</p>
<dt><code>random</code></p>
<dd>Generate a random priority between 1 and 10.</p>
<dt><code>weightedpath</code></p>
<dd>Generate the path priority based on the regular expression and the priority provided as argument. requires prio_args keyword.</p>
<dt>Default value is <code>const</code>.</p>
<dd></dl>
</dl>
<dt><code>prio_args</code></p>
<dd>Arguments to pass to to the prio function. Currently only used with <i>weighted, which needs a value of the form</i> <i>&lt;hbtl|devname&gt; &lt;regex1&gt; &lt;prio1&gt; &lt;regex2&gt; &lt;prio2&gt; &#8230;</i> <i>hbtl</i> regex can be of SCSI H:B:T:L format Ex: 1:0:.:. , *:0:0:. <i>devname</i> regex can be of device name format Ex: sda , sd.e</p>
<dt><code>features</code></p>
<dd>Specify any device-mapper features to be used. Syntax is <i>num list</i> where <i>num</i> is the number of features in <i>list.</i> Possible values for the feature list are</p>
<dl>
<dd>
<dl>
<dt><code>queue_if_no_path</code></p>
<dd>Queue IO if no path is active; identical to the <i>no_path_retry</i> keyword.</p>
<dt><code>no_partitions</code></p>
<dd>Disable automatic partitions generation via kpartx.</dl>
</dl>
<dt><code>path_checker</code></p>
<dd>The default method used to determine the paths state. Possible values are</p>
<dl>
<dd>
<dl>
<dt><code>readsector0</code></p>
<dd>(Deprecated) Read the first sector of the device. This checker is being deprecated, please use <i>directio</i> instead</p>
<dt><code>tur</code></p>
<dd>Issue a <i>TEST UNIT READY</i> command to the device.</p>
<dt><code>emc_clariion</code></p>
<dd>Query the EMC Clariion specific EVPD page 0xC0 to determine the path state.</p>
<dt><code>hp_sw</code></p>
<dd>Check the path state for HP storage arrays with Active/Standby firmware.</p>
<dt><code>rdac</code></p>
<dd>Check the path state for LSI/Engenio/NetApp E-Series RDAC storage controller.</p>
<dt><code>directio</code></p>
<dd>Read the first sector with direct I/O.</p>
<dt>Default value is <i>directio</i>.</p>
<dd></dl>
</dl>
<dt><code>failback</code></p>
<dd>Tell multipathd how to manage path group failback.</p>
<dl>
<dd>
<dl>
<dt><code>immediate</code></p>
<dd>Immediately failback to the highest priority pathgroup that contains active paths.</p>
<dt><code>manual</code></p>
<dd>Do not perform automatic failback.</p>
<dt><code>followover</code></p>
<dd>Only perform automatic failback when the first path of a pathgroup becomes active. This keeps a node from automatically failing back when another node requested the failover.</p>
<dt><code>values &gt; 0</code></p>
<dd>deferred failback (time to defer in seconds)</p>
<dt>Default value is <i>manual</i>.</p>
<dd></dl>
</dl>
<dt><code>rr_min_io</code></p>
<dd>The number of IO to route to a path before switching to the next in the same path group. This is only for BIO based multipath. Default is <i>1000</i></p>
<dt><code>rr_min_io_rq</code></p>
<dd>The number of IO requests to route to a path before switching to the next in the same path group. This is only for request based multipath. Default is <i>1</i></p>
<dt><code>rr_weight</code></p>
<dd>If set to <i>priorities</i> the multipath configurator will assign path weights as &quot;path prio * rr_min_io&quot;. Possible values are <i>priorities</i> or <i>uniform</i>. Default is <i>uniform</i>.</p>
<dt><code>no_path_retry</code></p>
<dd>Specify the number of retries until disable queueing, or <i>fail</i> for immediate failure (no queueing), <i>queue</i> for never stop queueing. Default is 0.</p>
<dt><code>user_friendly_names</code></p>
<dd>If set to <i>yes</i> , using the bindings file <i>/etc/multipath/bindings</i> to assign a persistent and unique alias to the multipath, in the form of mpath&lt;n&gt;. If set to <i>no</i> use the WWID as the alias. In either case this be will be overridden by any specific aliases in the <i>multipaths</i> section. Default is <i>no</i></p>
<dt><code>flush_on_last_del</code></p>
<dd>If set to <i>yes</i> , multipathd will disable queueing when the last path to a device has been deleted. Default is <i>no</i></p>
<dt><code>max_fds</code></p>
<dd>Specify the maximum number of file descriptors that can be opened by multipath and multipathd. This is equivalent to ulimit -n. A value of <i>max</i> will set this to the system limit from /proc/sys/fs/nr_open. If this is not set, the maximum number of open fds is taken from the calling process. It is usually 1024. To be safe, this should be set to the maximum number of paths plus 32, if that number is greated than 1024.</p>
<dt><code>checker_timeout</code></p>
<dd>Specify the timeout to user for path checkers that issue scsi commands with an explicit timeout, in seconds; default taken from <i>/sys/block/sd&lt;x&gt;/device/timeout</i></p>
<dt><code>fast_io_fail_tmo</code></p>
<dd>Specify the number of seconds the scsi layer will wait after a problem has been detected on a FC remote port before failing IO to devices on that remote port. This should be smaller than dev_loss_tmo. Setting this to <i>off</i> will disable the timeout.</p>
<dt><code>dev_loss_tmo</code></p>
<dd>Specify the number of seconds the scsi layer will wait after a problem has been detected on a FC remote port before removing it from the system. This can be set to &quot;infinity&quot; which sets it to the max value of 2147483647 seconds, or 68 years. It will be automatically adjusted to the overall retry interval <i>no_path_retry</i> * <i>polling_interval</i> if a number of retries is given with <i>no_path_retry</i> and the overall retry interval is longer than the specified <i>dev_loss_tmo</i> value. The linux kernel will cap this value to <i>300</i> if <code>fast_io_fail_tmo</code> is not set.</p>
<dt><code>queue_without_daemon</code></p>
<dd>If set to <i>no</i> , when multipathd stops, queueing will be turned off for all devices. This is useful for devices that set no_path_retry. If a machine is shut down while all paths to a device are down, it is possible to hang waiting for IO to return from the device after multipathd has been stopped. Without multipathd running, access to the paths cannot be restored, and the kernel cannot be told to stop queueing IO. Setting queue_without_daemon to <i>no</i> , avoids this problem. Default is <i>yes</i></p>
<dt><code>bindings_file</code></p>
<dd>The full pathname of the binding file to be used when the user_friendly_names option is set. Defaults to <i>/etc/multipath/bindings</i></p>
<dt><code>wwids_file</code></p>
<dd>The full pathname of the wwids file, which is used by multipath to keep track of the wwids for LUNs it has created multipath devices on in the past. Defaults to <i>/etc/multipath/wwids</i></p>
<dt><code>log_checker_err</code></p>
<dd>If set to <i>once</i> , multipathd logs the first path checker error at logging level 2. Any later errors are logged at level 3 until the device is restored. If set to <i>always</i> , multipathd always logs the path checker error at logging level 2. Default is <i>always</i></p>
<dt><code>reservation_key</code></p>
<dd>This is the service action reservation key used by mpathpersist. It must be set for all multipath devices using persistent reservations, and it must be the same as the RESERVATION KEY field of the PERSISTENT RESERVE OUT parameter list which contains an 8-byte value provided by the application client to the device server to identify the I_T nexus. It is unset by default.</p>
<dt><code>retain_attached_hw_handler</code></p>
<dd>If set to <i>yes</i> and the scsi layer has already attached a hardware_handler to the device, multipath will not force the device to use the hardware_handler specified by mutipath.conf. If the scsi layer has not attached a hardware handler, multipath will continue to use its configured hardware handler. Default is <i>no</i></p>
<dt><code>detect_prio</code></p>
<dd>If set to <i>yes</i> , multipath will try to detect if the device supports ALUA. If so, the device will automatically use the <i>alua</i> prioritizer. If not, the prioritizer will be selected as usual. Default is <i>no</i></p>
<dt><code>hw_str_match</code></p>
<dd>If set to <i>yes</i> , the vendor, product, and revision parameters of user device configs will be string matched against the built-in device configs to determine if they should modify an existing config, or create a new one. If set to <i>no</i> , the user device configs will be regular expression matched against the built-in configs instead. Default is <i>no</i></dl>
<h2>blacklist section</h2>
<p>The <i>blacklist</i> section is used to exclude specific device from inclusion in the multipath topology. It is most commonly used to exclude local disks or LUNs for the array controller. </p>
<p> The following keywords are recognized:</p>
<dl>
<dt><code>wwid</code></p>
<dd>The <i>World Wide Identification</i> of a device.</p>
<dt><code>devnode</code></p>
<dd>Regular expression of the device nodes to be excluded.</p>
<dt><code>device</code></p>
<dd>Subsection for the device description. This subsection recognizes the <i>vendor</i> and <i>product</i> keywords. For a full description of these keywords please see the <i>devices</i> section description.</dl>
<h2>blacklist_exceptions section</h2>
<p>The <i>blacklist_exceptions</i> section is used to revert the actions of the <i>blacklist</i> section, ie to include specific device in the multipath topology. This allows one to selectively include devices which would normally be excluded via the <i>blacklist</i> section. </p>
<p> The following keywords are recognized:</p>
<dl>
<dt><code>wwid</code></p>
<dd>The <i>World Wide Identification</i> of a device.</p>
<dt><code>devnode</code></p>
<dd>Regular expression of the device nodes to be excluded.</p>
<dt><code>device</code></p>
<dd>Subsection for the device description. This subsection recognizes the <i>vendor</i> and <i>product</i> keywords. For a full description of these keywords please see the <i>devices</i> section description.</dl>
<h2>multipaths section</h2>
<p>The only recognized attribute for the <code>multipaths</code> section is the <i>multipath</i> subsection. </p>
<p> The <code>multipath</code> subsection recognizes the following attributes:</p>
<dl>
<dt><code>wwid</code></p>
<dd>Index of the container. Mandatory for this subsection.</p>
<dt><code>alias</code></p>
<dd>(Optional) symbolic name for the multipath map.</dl>
<p> The following attributes are optional; if not set the default values are taken from the <i>defaults</i> or <i>devices</i> section: </p>
<dl>
<dd>
<dl>
<dt><code>path_grouping_policy</code></p>
<dd>
<dt><code>path_selector</code></p>
<dd>
<dt><code>prio</code></p>
<dd>
<dt><code>prio_args</code></p>
<dd>
<dt><code>failback</code></p>
<dd>
<dt><code>rr_weight</code></p>
<dd>
<dt><code>flush_on_last_del</code></p>
<dd>
<dt><code>no_path_retry</code></p>
<dd>
<dt><code>rr_min_io</code></p>
<dd>
<dt><code>rr_min_io_q</code></p>
<dd>
<dt><code>features</code></p>
<dd>
<dt><code>reservation_key</code></p>
<dd></dl>
</dl>
<h2>devices section</h2>
<p>The only recognized attribute for the <code>devices</code> section is the <i>device</i> subsection. </p>
<p> The <i>device</i> subsection recognizes the following attributes:</p>
<dl>
<dt><code>vendor</code></p>
<dd>(Mandatory) Vendor identifier</p>
<dt><code>product</code></p>
<dd>(Mandatory) Product identifier</p>
<dt><code>revision</code></p>
<dd>(Optional) Revision identfier</p>
<dt><code>product_blacklist</code></p>
<dd>(Optional) Product strings to blacklist for this vendor</p>
<dt><code>alias_prefix</code></p>
<dd>(Optional) The user_friendly_names prefix to use for this device type, instead of the default &quot;mpath&quot;</p>
<dt><code>hardware_handler</code></p>
<dd>(Optional) The hardware handler to use for this device type. The following hardware handler are implemented:</p>
<dl>
<dd>
<dl>
<dt><code>1 emc</code></p>
<dd>Hardware handler for EMC storage arrays.</p>
<dt><code>1 rdac</code></p>
<dd>Hardware handler for LSI/Engenio/NetApp E-Series RDAC storage controller.</p>
<dt><code>1 hp_sw</code></p>
<dd>Hardware handler for Compaq/HP storage arrays in active/standby mode.</p>
<dt><code>1 alua</code></p>
<dd>Hardware handler for SCSI-3 ALUA compatible arrays.</dl>
</dl>
</dl>
<p> The following attributes are optional; if not set the default values are taken from the <i>defaults</i> section: </p>
<dl>
<dd>
<dl>
<dt><code>path_grouping_policy</code></p>
<dd>
<dt><code>uid_attribute</code></p>
<dd>
<dt><code>path_selector</code></p>
<dd>
<dt><code>path_checker</code></p>
<dd>
<dt><code>prio</code></p>
<dd>
<dt><code>prio_args</code></p>
<dd>
<dt><code>features</code></p>
<dd>
<dt><code>failback</code></p>
<dd>
<dt><code>rr_weight</code></p>
<dd>
<dt><code>no_path_retry</code></p>
<dd>
<dt><code>rr_min_io</code></p>
<dd>
<dt><code>rr_min_io_rq</code></p>
<dd>
<dt><code>fast_io_fail_tmo</code></p>
<dd>
<dt><code>dev_loss_tmo</code></p>
<dd>
<dt><code>flush_on_last_del</code></p>
<dd>
<dt><code>retain_attached_hw_handler</code></p>
<dd>
<dt><code>detect_prio</code></p>
<dd></dl>
</dl>
<h2>Known Issues</h2>
<p>The usage of <code>queue_if_no_path</code> option can lead to <code>D state</code> processes being hung and not killable in situations where all the paths to the LUN go offline. It is advisable to use the <code>no_path_retry</code> option instead. </p>
<p> The use of <code>queue_if_no_path</code> or <code>no_path_retry</code> might lead to a deadlock if the <code>dev_loss_tmo</code> setting results in a device being removed while I/O is still queued. The multipath daemon will update the <code>dev_loss_tmo</code> setting accordingly to avoid this deadlock. Hence if both values are specified the order of precedence is <i>no_path_retry, queue_if_no_path, dev_loss_tmo</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-udev/">udev</a></code>(8), <code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8) <code><a href="/docs/linux/man/8-multipath/">multipath</a></code>(8) <code><a href="/docs/linux/man/8-multipathd/">multipathd</a></code>(8)</p>
<h2>Authors</h2>
<p><code>multipath</code> was developed by Christophe Varoqui, &lt;christophe.varoqui [at] opensvc.com&gt; and others.</p>
