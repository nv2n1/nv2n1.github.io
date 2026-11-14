---
title: "iprconfig(8)"
name: "iprconfig"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iprconfig/"
description: "iprconfig – IBM Power RAID storage adapter configuration/recovery utility"
---

<p>iprconfig &#8211; IBM Power RAID storage adapter configuration/recovery utility</p>
<h2>Synopsis</h2>
<p><code>iprconfig [-e editor] [-k dir] [-c command]</code> </p>
<p> <code>iprconfig &#8211;version &#8211;debug &#8211;force</code></p>
<h2>Description</h2>
<p><code>iprconfig</code> is used to configure IBM Power RAID storage adapters, display information about them, and to perform adapter and disk unit recovery. The menu options are: </p>
<p> <code>1. Display hardware status.</code><br />
 This option can be used to display various information regarding the IBM Power RAID adapters attached to the system and the disk units controlled by them. For each adapter and disk unit, their /dev name, physical location, description, vendor/product ID, and hardware status will be available. Beside each resource is an OPT field. By entering a 1 beside any resource, detailed information about that resource can be obtained. For an adapter resource, this will display the adapter firmware version and the physical location amongst other things. </p>
<p> <code>2. Work with Disk Arrays</code><br />
 This option will present a second menu containing disk array related commands. </p>
<p> <code>Display disk array status</code> is used to display the status of disk arrays on the system. </p>
<p> <code>Create a disk array</code> is used to create a disk array. </p>
<p> <code>Delete a disk array</code> is used to delete disk arrays. Selecting this option will provide you with a list of disk arrays which can be deleted. </p>
<p> <code>Add a device to a disk array</code> is used to include devices of similar capacity into an existing disk array. This function is currently only supported for RAID 5 and RAID 6 disk arrays. </p>
<p> <code>Format device for advanced function</code> is used to format disks to 522 bytes/sector so that they may be used in a disk array. Only disks which are not formatted for advanced function or are formatted for advanced function but are not known to be zeroed will be available for selection for this function. </p>
<p> <code>Format device for JBOD function (512)</code> is used to format disks to 512 bytes/sector so that they may be used as standalone disks. Only disks which are not formatted for JBOD function or are formatted for JBOD function and are in the Format Required state will be available for this function. </p>
<p> <code>Work with hot spares</code> is used to create a hot spare which designates a device as a dedicated hot spare. It is also used to delete a hot spare which unconfigures a previously configured hot spare. </p>
<p> <code>Work with asymmetric access</code> is used to select which path of a disk array will be the primary path in a dual controller environment. Asymmetric Access must be enabled on the adapter first. Not all adapters support asymmetric access and adapters that do provide support may require updated microcode. </p>
<p> <code>Force RAID Consistency Check</code> is used to force a consistency check on a RAID array. All ipr adapters continually perform background consistency checking when idle. This option can be used to force a consistency check to be performed. </p>
<p> <code>Migrate disk array protection</code> is used to change the RAID protection level for an array to another supported level. In some cases, this will require adding more disks to the array. In other cases, disks will be freed. </p>
<p> <code>3. Work with disk unit recovery</code> is used to perform the following disk unit recovery actions: </p>
<p> <code>Concurrent add device</code> is used to concurrently add a new disk to a running system. This feature is only supported with SES (SCSI Enclosure Services) packaging. </p>
<p> <code>Concurrent remove device</code> is used to concurrently remove a disk from a running system. This feature is only supported with SES (SCSI Enclosure Services) packaging. </p>
<p> <code>Initialize and format disk unit</code> is used to issue a SCSI format command to attached devices. A format unit command has special meaning to the adapter and is used as a service action for certain error conditions. Formatting a disk unit will lose all data on that drive. If the disk is attached to an ipr adapter that does not support RAID, the drive will be formatted to 512 bytes/sector. If the disk is attached to an ipr RAID adapter, the block size will not be changed. To change the block size, use the format menu options under the disk arrays menu. </p>
<p> <code>Reclaim IOA cache storage</code> is used to repair cache error conditions. <code>ATTENTION:</code> Use this option with care. This is used to discard data from the cache and may result in data loss. This option is designed to be used by authorized IBM hardware customer engineers. </p>
<p> <code>Rebuild disk unit data</code> is generally used following concurrent maintenance. Select this option after a failing array member device has been replaced to reconstruct the device as an active array member. </p>
<p> <code>Work with resources containing cache battery packs</code> is used to display information regarding rechargeable cache battery packs and to force rechargeable cache battery packs into an error state so that they can be replaced prior to failure. <code>ATTENTION:</code> Once an error has been forced on a rechargeable cache battery pack write caching will be disabled until the battery pack is replaced. </p>
<p> <code>4. Work with SCSI bus configuration</code> is used to change configurable SCSI bus attributes, such as maximum SCSI bus speed, SCSI initiator ID, etc. </p>
<p> <code>5. Work with driver configuration</code> is used to change driver configurable attributes, such as log_level. </p>
<p> <code>6. Work with disk configuration</code> is used to change configurable disk attributes, such as queue depth. </p>
<p> <code>7. Work with adapter configuration</code> is used to change configurable adapter attributes, such as dual adapter settings. Refer to the following command line options: primary, secondary, query-ha-mode, set-ha-mode, set-ioa-asymmetric-access and set-array-asymmetric-access for more information regarding these settings. </p>
<p> <code>8. Download microcode</code> is used to download microcode to ipr adapters and attached SCSI disks. </p>
<p> <code>9. Analyze Log</code> is an option available to analyze /var/log/messages* files. By default it will use vi as the editor to open the concatenated error log files. This can be changed by using option 6 on the <code>Kernel Messages Log </code> menu. Selecting option 1 on the Kernel Messages Log menu will display only the most recent errors logged by the ipr device driver and may be useful to filter out some of the clutter. Option 2 will display all recorded errors logged by the ipr device driver. Option 3 will display all kernel messages. Option 4 will display errors logged by the iprconfig utility. This may be useful for debugging problems. Option 5 can be used to change where the tool looks to find the kernel messages files. The default is to look in /var/log.</p>
<h2>Options</h2>
<dl>
<dt><code>-e editor</code></p>
<dd>Default editor for viewing error logs. The default editor is vi, but can be changed with this parameter.</p>
<dt><code>-k directory</code></p>
<dd>Kernel messages root directory. Root directory to look for kernel messages. Default is /var/log.</p>
<dt><code>-c command</code></p>
<dd>Command line, non-interactive commands. Currently supported commands include:</p>
<dl>
<dd>
<dl>
<dt><code>show-config</code></p>
<dd>Show ipr configuration.</p>
<dt><code>show-alt-config</code></p>
<dd>Show alternate ipr configuration information.</p>
<dt><code>show-ioas</code></p>
<dd>Show all ipr adapters.</p>
<dt><code>show-arrays</code></p>
<dd>Show all ipr arrays.</p>
<dt><code>show-battery-info [IOA]</code></p>
<dd>Show cache battery information for specified IOA. Example:<br />
 <code>iprconfig -c show-battery-info sg5</code></p>
<dt><code>show-details [device]</code></p>
<dd>Show device details for specified device. Example:<br />
 <code>iprconfig -c show-details sda</code></p>
<dt><code>show-hot-spares</code></p>
<dd>Show all configured hot spares.</p>
<dt><code>show-af-disks</code></p>
<dd>Show disks formatted for Advanced Function that are not configured in an array or as a hot spare.</p>
<dt><code>show-all-af-disks</code></p>
<dd>Show all disks formatted for Advanced Function</p>
<dt><code>show-jbod-disks</code></p>
<dd>Show all disks formatted for JBOD Function.</p>
<dt><code>show-slots</code></p>
<dd>Show all disks slots available on the system.</p>
<dt><code>status [device]</code></p>
<dd>Show the status of the specified device. This is the same status as which shows up in the last column of the Display hardware status menu. Can specify either a /dev/sdX name or a /dev/sgX name. Example:<br />
 <code>iprconfig -c status /dev/sda</code> </p>
<dt><code>alt-status [device]</code></p>
<dd>Show the status of the specified device. This is the same status as above with the exception of when a long running command is executing to the device, in which case the percent complete for the long running command is printed. </p>
<dt><code>query-raid-create [IOA]</code></p>
<dd>Show all devices attached to the specified IOA that are candidates for being used in a RAID array. Example:<br />
 <code>iprconfig -c query-raid-create sg5</code></p>
<dt><code>query-raid-delete [IOA]</code></p>
<dd>Show all RAID arrays attached to the specified IOA that can be deleted.<br />
 <code>iprconfig -c query-raid-delete sg5</code></p>
<dt><code>query-hot-spare-create [IOA]</code></p>
<dd>Show all devices attached to the specified IOA that are candidates for being hot spares.</p>
<dt><code>query-hot-spare-delete [IOA]</code></p>
<dd>Show all hot spares attached to the specified IOA that can be deleted.</p>
<dt><code>query-raid-consistency-check</code></p>
<dd>Show all RAID arrays that are candidates for a RAID consistency check.</p>
<dt><code>query-format-for-jbod</code></p>
<dd>Show all disks that can be reformatted for JBOD function.</p>
<dt><code>query-reclaim</code></p>
<dd>Show all IOAs that may need a reclaim cache storage.</p>
<dt><code>query-arrays-raid-include</code></p>
<dd>Show all RAID arrays that can have disks included in them to increase their capacity.</p>
<dt><code>query-devices-raid-include [array]</code></p>
<dd>Show all disks that can be added to the specified array to increase its capacity.</p>
<dt><code>query-supported-raid-levels [IOA]</code></p>
<dd>Show all RAID levels supported by the specified adapter.</p>
<dt><code>query-include-allowed [IOA] [raid level]</code></p>
<dd>Some RAID levels allow for adding additional disks to existing disk arrays to increase their capacity. Prints &quot;yes&quot; to stdout if the specified RAID level supports this function, else prints &quot;no&quot;.</p>
<dt><code>query-max-devices-in-array [IOA] [raid level]</code></p>
<dd>Print the maximum number of devices allowed in a RAID array of the specified RAID level for the specified RAID adapter.</p>
<dt><code>query-min-devices-in-array [IOA] [raid level]</code></p>
<dd>Print the minimum number of devices allowed in a RAID array of the specified RAID level for the specified RAID adapter.</p>
<dt><code>query-min-mult-in-array [IOA] [raid level]</code></p>
<dd>Print the minimum multiple of devices required in a RAID array of the specified RAID level for the specified RAID adapter.</p>
<dt><code>query-supp-stripe-sizes [IOA] [raid level]</code></p>
<dd>Print all supported stripe sizes supported for RAID arrays of the specified RAID level on the specified RAID adapter. Stripe sizes are printed in units of KB.</p>
<dt><code>query-recommended-stripe-size [IOA] [raid level]</code></p>
<dd>Print the default/recommended stripe size for RAID arrays of the specified RAID level on the specified RAID adapter. Stripe size is in units of KB.</p>
<dt><code>query-recovery-format</code></p>
<dd>Show all disks that can be formatted for error recovery purposes.</p>
<dt><code>query-raid-rebuild</code></p>
<dd>Show all disks in RAID arrays that can be rebuilt.</p>
<dt><code>query-format-for-raid</code></p>
<dd>Show all disks that can be formatted such that they can be used in a RAID array or as a hot spare.</p>
<dt><code>query-ucode-level [device]</code></p>
<dd>Show the microcode level that is currently loaded on the specified device. Note: The device specified may be the sg device associated with an IOA, in which case the IOA&#8217;s microcode level will be shown.</p>
<dt><code>ssd-report [device]</code></p>
<dd>Display information about Read Intensive SSD devices in the system.</p>
<dt><code>show-ucode-levels</code></p>
<dd>Show the microcode level that is currently loaded for every device and adapter in the system. If newer microcode is available on the filesystem than what is loaded on the device, an * chararacter will be displayed next to the device.</p>
<dt><code>query-format-timeout [device]</code></p>
<dd>Show the current format timeout to be used when formatting the specified disk. This value is only applicable when the device is currently in Advanced Function format.</p>
<dt><code>query-qdepth [device]</code></p>
<dd>Show the queue depth currently being used for the specified disk.</p>
<dt><code>query-tcq-enable [device]</code></p>
<dd>Print 1 to stdout if tagged queuing is enabled for the specified device, else print 0 to stdout.</p>
<dt><code>query-log-level [IOA]</code></p>
<dd>Print the current log level being used for the specified IOA. Can be a number from 0 to n.</p>
<dt><code>query-add-device</code></p>
<dd>Show all empty disk slots that can have a disk concurrently added.</p>
<dt><code>query-remove-device</code></p>
<dd>Show all disk slots which are either empty or have disks in them which can be concurrently removed from the running system.</p>
<dt><code>query-initiator-id [IOA] [busno]</code></p>
<dd>Show the current SCSI initiator ID used by the IOA for the specified SCSI bus.</p>
<dt><code>query-bus-speed [IOA] [busno]</code></p>
<dd>Show the current maximum SCSI bus speed allowed on the specified SCSI bus.</p>
<dt><code>query-bus-width [IOA] [busno]</code></p>
<dd>Show the current SCSI bus width in units of bits for the specified SCSI bus.</p>
<dt><code>query-path-status [IOA]</code></p>
<dd>Show the current dual path state for the SAS devices attached specified IOA.</p>
<dt><code>query-path-details [device]</code></p>
<dd>Show the current dual path details for the specified SAS device.</p>
<dt><code>query-arrays-raid-migrate</code></p>
<dd>Show the arrays that can be migrated to a different protection level.</p>
<dt><code>query-devices-raid-migrate [array]</code></p>
<dd>Show the AF disks that are candidates to be used in a migration for a given array.</p>
<dt><code>query-raid-levels-raid-migrate [array]</code></p>
<dd>Show the protection levels to which the given array can be migrated.</p>
<dt><code>query-stripe-sizes-raid-migrate [array] [raid level]</code></p>
<dd>Given an array and a protection level, show the valid stripe sizes to which the array can be migrated.</p>
<dt><code>query-devices-min-max-raid-migrate [array] [raid level]</code></p>
<dd>Show the number of devices that will be removed for a migration to a protection level that requires fewer devices. Or, show the minmum number of devices required, the maximum number of devices allowed and the multiple of the number of devices required for a migration that requires more devices.</p>
<dt><code>query-ioas-asymmetric-access</code></p>
<dd>Show the IOAs that support asymmetric access.</p>
<dt><code>query-arrays-asymmetric-access</code></p>
<dd>Show the disk arrays that are candidates for setting their asymmetric access mode to Optimized or Non-Optimized.</p>
<dt><code>query-ioa-asymmetric-access-mode [IOA]</code></p>
<dd>Show the current asymmetric access mode for the given IOA.</p>
<dt><code>query-array-asymmetric-access-mode [array]</code></p>
<dd>Show the current asymmetric access mode for the given disk array.</p>
<dt><code>query-ioa-caching [IOA]</code></p>
<dd>Show whether or not the user requested caching mode for the given IOA is set to default or disabled.</p>
<dt><code>query-array-label [label]</code></p>
<dd>Show the device name of the array with the specified label. Label must have been specified when creating the RAID array. See raid-create command.</p>
<dt><code>query-array-rebuild-rate [IOA]</code></p>
<dd>Show the array rebuild rate for the given IOA. </p>
<dt><code>query-array-rebuild-verify [IOA]</code></p>
<dd>Show whether array rebuild verification is enabled for the given IOA. </p>
<dt><code>query-array [location]</code></p>
<dd>Show the device name of the array of which one of the disks in the array has the specified platform location code.</p>
<dt><code>query-device [location]</code></p>
<dd>Show the device name of the disk that has the specified platform location code.</p>
<dt><code>query-location [device]</code></p>
<dd>The device specified can be either the device name of a disk or the device name of a single disk RAID 0 array. If the specified device name is a disk, the platform location code will be displayed. If the specified device name is a single device RAID 0 array, the platform location of the disk which is a member of the specified array will be displayed.</p>
<dt><code>query-write-cache-policy [device]</code></p>
<dd>Show the current write cache policy for [device].</p>
<dt><code>raid-create [-r raid_level] [-s stripe_size_in_kb] [-l label] [&#8211;skip-format] [-c cache_policy] [devices&#8230;]</code></p>
<dd>Create a RAID array. RAID level can be any supported RAID level for the given adapter, such as 0, 10, 5, 6. Currently supported stripe sizes in kb include 16, 64, and 256. If raid_level is not specified, it will default to RAID 5. If stripe size is not specified, it will default to the recommended stripe size for the selected RAID level. Available cache policies are the same that can be passed to set-write-cache-policy command. If none is specified, write back is assumed. Devices are specified with their full name, either the /dev/sd name or the /dev/sg name is acceptable. On some RAID adapters, a label can also be specified. Example array creation:<br />
 <code>iprconfig -c raid-create -r 5 -s 64 /dev/sda /dev/sdb /dev/sdc</code><br />
 This would create a RAID 5 array with a 64k stripe size using the specified devices.</p>
<dt><code>raid-delete [RAID device]</code></p>
<dd>Delete the specified RAID array. Specify either the /dev/sd name or the /dev/sg name. Only 1 array can be deleted with a single command. Example:<br />
 <code>iprconfig -c raid-delete /dev/sda</code><br />
 This would delete the disk array represented by /dev/sda</p>
<dt><code>raid-include [array] [disk] &#8230; [disk]</code></p>
<dd>Add the specified devices to the specified disk array to increase its capacity. Example:<br />
 <code>iprconfig -c raid-include sda sg6 sg7</code></p>
<dt><code>raid-migrate -r raid_level [-s stripe_size_in_kb] array [disk] &#8230; [disk]</code></p>
<dd>Migrate an existing RAID array to a new RAID protection level. Optionally, a new stripe size can be given. In some cases one or more new disks must be added for the migration to succeed. Example:<br />
 <code>iprconfig -c raid-migrate -r 10 -s 64 sda sg5 sg6</code></p>
<dt><code>format-for-raid [disk] &#8230; [disk]</code></p>
<dd>Format the specified disks for Advanced Function so they can be used in a RAID array or as a hot spare.</p>
<dt><code>format-for-jbod [disk] &#8230; [disk]</code></p>
<dd>Format the specified disks for JBOD Function so they can be used as standalone disks.</p>
<dt><code>recovery-format [disk] &#8230; [disk]</code></p>
<dd>Format the specified disks as directed by the reference guide for error recovery purposes.</p>
<dt><code>hot-spare-create [disk]</code></p>
<dd>Create a hot spare using the specified Advanced Function disk.</p>
<dt><code>hot-spare-delete [disk]</code></p>
<dd>Delete the specified hot spare.</p>
<dt><code>disrupt-device [disk]</code></p>
<dd>Force the specified Advanced Function device failed.</p>
<dt><code>reclaim-cache [IOA]</code></p>
<dd>Reclaim the specified IOA&#8217;s write cache. <code>ATTENTION:</code> Use this option with care. This is used to discard data from the cache and may result in data loss. This option is designed to be used by authorized IBM hardware customer engineers.</p>
<dt><code>reclaim-unknown-cache [IOA]</code></p>
<dd>Reclaim the specified IOA&#8217;s write cache and allow unknown data loss. <code>ATTENTION:</code> Use this option with care. This is used to discard data from the cache and WILL result in data loss. This option is designed to be used by authorized IBM hardware customer engineers.</p>
<dt><code>raid-consistency-check [array]</code></p>
<dd>Force a full RAID consistency check on the specified array. This command will return before the RAID consistency check has completed. Use the <code>status</code> command to check the status of the command.</p>
<dt><code>raid-rebuild [disk]</code></p>
<dd>Following a disk replacement for a failed disk in a RAID array, use this command to rebuild the failed disk&#8217;s data onto the new disk and return the disk array to the <code>Active</code> state.</p>
<dt><code>update-ucode [device] [microcode file]</code></p>
<dd>Update the microcode on the specified device (IOA or disk) with the specified microcode file. <code>ATTENTION:</code> Limited checking of the microcode image is done. Make sure the specified microcode file is the correct file for the specified device.</p>
<dt><code>update-all-ucodes</code></p>
<dd>Update the microcode of every device with the latest version found in the system.</p>
<dt><code>set-format-timeout [disk] [timeout in hours]</code></p>
<dd>Set the format timeout to be used when formatting the specified disk.</p>
<dt><code>set-qdepth [device] [queue depth]</code></p>
<dd>Set the queue depth for the specified device or disk array.</p>
<dt><code>set-tcq-enable [device] [0 = disable, 1 = enable]</code></p>
<dd>Enable/disable tagged command queueing for the specified device.</p>
<dt><code>set-log-level [IOA] [log level]</code></p>
<dd>Set the error logging verbosity to use for the specified IOA. Default is 2.</p>
<dt><code>set-write-cache-policy [device] [writeback|writethrough]</code></p>
<dd>Set the write cache policy for [device]. Available policies are writeback and writethrough. This command supports JBOD disk (write cache) and Volume Sets (vset write cache). Example:<br />
 <code>iprconfig -c set-write-cache-policy sdp writeback</code></p>
<dt><code>identify-disk [disk] [0 = turn off identify LED, 1 = turn on identify LED]</code></p>
<dd>Turn on/off the disk identify LED for the specified disk. This function may or may not be available depending on the hardware packaging.</p>
<dt><code>identify-slot [location] [0 = turn off identify LED, 1 = turn on identify LED]</code></p>
<dd>Turn on/off the disk identify LED for the specified location. This function may or may not be available depending on the hardware packaging. Example:<br />
 <code>iprconfig -c identify-slot 0000:d8:01.0/0:1:1: 1</code></p>
<dt><code>remove-disk [disk] [0 = turn off identify LED, 1 = turn on identify LED]</code></p>
<dd>Turn on/off the disk remove identify LED for the specified device. When 1 is specified as the second argument, the specified disk is set to the remove state. When in this state, the disk may be removed. Once the disk has been physically removed, iprconfig must be invoked again with the second argument set to 0. This turns off the slot identifier light and logically removes the disk from the host operating system.</p>
<dt><code>remove-slot [location] [0 = turn off identify LED, 1 = turn on identify LED]</code></p>
<dd>Turn on/off the disk remove identify LED for the specified location. When 1 is specified as the second argument, the specified location is set to the remove state. When in this state, the disk may be removed. Once the disk has been physically removed, iprconfig must be invoked again with the second argument set to 0. This turns off the slot identifier light and logically removes the disk from the host operating system. Example:<br />
 <code>iprconfig -c remove-slot 0000:d8:01.0/0:1:1: 1</code></p>
<dt><code>add-slot [location] [0 = turn off identify LED, 1 = turn on identify LED]</code></p>
<dd>Turn on/off the disk insert identify LED for the specified location. When 1 is specified as the second argument, the specified location is set to the insert state. When in this state, the disk may be inserted. Once the disk has been physically inserted, iprconfig must be invoked again with the second argument set to 0. This turns off the slot identifier light and logically adds the disk to the host operating system. Example:<br />
 <code>iprconfig -c add-slot 0000:d8:01.0/0:1:1: 1</code></p>
<dt><code>set-initiator-id [IOA] [busno] [initiator id]</code></p>
<dd>Set the IOA&#8217;s SCSI initiator ID for the specified bus. Must be a value between 0 and 7 and must not conflict with any other device on the SCSI bus.</p>
<dt><code>set-bus-speed [IOA] [busno] [speed in MB/sec]</code></p>
<dd>Set the maximum SCSI bus speed allowed on the specified SCSI bus.</p>
<dt><code>set-bus-width [IOA] [busno] [bus width in # bits]</code></p>
<dd>Set the SCSI bus width to use for the specified SCSI bus. Example:<br />
 <code>iprconfig -c set-bus-width sg5 0 16</code></p>
<dt><code>primary [IOA]</code></p>
<dd>Set the adapter as the <code>preferred primary </code> adapter. This is used in dual initiator RAID configurations to indicate which adapter should be the <code>primary</code> adapter. The <code>primary </code> adapter should be the adapter receiving the majority of the I/O. Example:<br />
 <code>iprconfig -c primary sg5</code></p>
<dt><code>secondary [IOA]</code></p>
<dd>Set the adapter to indicate it is not the <code>preferred primary </code> adapter. See the notes for the <code>preferred primary</code> for additional information. Example:<br />
 <code>iprconfig -c secondary sg5</code></p>
<dt><code>set-all-primary</code></p>
<dd>Set all attached ipr adapters as the <code>preferred primary </code> adapter. This can be used when running a dual initiator RAID HA configuration. This command can be run on the <code>primary </code> system to quickly enable the <code>preferred primary </code> mode for all attached adapters. Refer to /etc/ha.d/resource.d/iprha for an example of how this might be used. Example:<br />
 <code>iprconfig -c set-all-primary</code></p>
<dt><code>set-all-secondary</code></p>
<dd>Set all attached ipr adapters to indicate they are not the <code>preferred primary </code> adapter. Example:<br />
 <code>iprconfig -c set-all-secondary</code></p>
<dt><code>query-ha-mode [IOA]</code></p>
<dd>When an adapter is configured in a highly available dual adapter configuration, it may be able to be configured in one of two ways. The default mode is <code>Normal. </code> This mode is used for all SCSI adapters and many SAS adapters. Some SAS adapters also support a <code>JBOD </code> dual adapter configuration. This mode is to be used when the dual adapter configuration is to consist of JBOD disks rather than RAID arrays. If the adapter is <code>NOT </code> going to be used in a dual adapter configuration, this mode <code>MUST </code> be set to <code>Normal.</code> Example:<br />
 <code>iprconfig -c query-ha-mode sg5</code></p>
<dt><code>set-ha-mode [IOA] [Normal | RAID]</code></p>
<dd>Used to set the high-availability mode of the adapter. Refer to the <code>query-ha-mode </code> command for more information regarding these settings. Example:<br />
 <code>iprconfig -c set-ha-mode sg5 Normal</code></p>
<dt><code>set-array-asymmetric-access-mode [array] [Optimized | Non-Optimized]</code></p>
<dd>Used to set the asymmetric access mode of the disk array. Example:<br />
 <code>iprconfig -c set-array-asymmetric-access-mode sda Optimized</code></p>
<dt><code>set-ioa-asymmetric-access-mode [IOA] [Enabled | Disabled]</code></p>
<dd>Used to set the asymmetric access mode of the IOA.<br />
 Example:<br />
 <code>iprconfig -c set-ioa-asymmetric-access-mode sg5 Enabled</code></p>
<dt><code>set-ioa-caching [IOA] [Default | Disabled]</code></p>
<dd>Used to set the requested caching mode of the IOA.<br />
 Example:<br />
 <code>iprconfig -c set-ioa-caching sg5 Disabled</code></p>
<dt><code>set-array-rebuild-verify [IOA] [enable | disable | default]</code></p>
<dd>Used to define whether to perform verification during an array rebuild. Enabling this can affect performance. The default value is disabled.<br />
 Example:<br />
 <code>iprconfig -c set-array-rebuild-rate sg5 disable</code></p>
<dt><code>set-array-rebuild-rate [IOA] [Rebuild Rate | default]</code></p>
<dd>Used to set the rebuilt rate ratio of the IOA. [Rebuild Rate] must be in range 10..100. If &#8216;default&#8217; is used, the IOA will reset to the implementation default rate. The value actually configured may not be the exact rate configured by the user, but an approximation to the closest rate supported by the IOA.<br />
 Example:<br />
 <code>iprconfig -c set-array-rebuild-rate sg5 10</code></p>
<dt><code>get-live-dump [IOA]</code></p>
<dd>Dump the IOA&#8217;s implementation unique critical information. The dump data will be saved in the /var/log/ directory with the pattern ipr-CCIN-PCI_ADDRESS-dump-TIMESTAMP.<br />
 Example:<br />
 <code>iprconfig -c get-live-dump sg5</code> </p>
<dt><code>dump</code></p>
<dd>Display detailed hardware and system information on standard output. In case a report file is needed, the iprsos command will create one at /var/log/iprsos.log.<br />
 Example:<br />
 <code>iprconfig -c dump</code>
</dl>
</dl>
<dt><code>&#8211;version</code></p>
<dd>Print version number of <code>iprconfig</code></p>
<dt><code>&#8211;debug</code></p>
<dd>Enable additional error logging. Enabling this will result in additional errors logging to /var/log/messages.</p>
<dt><code>&#8211;force</code></p>
<dd>Disable safety checks. Use this to disable safety checks in iprconfig. This will allow you to format devices that are not at the appropriate code levels. Only use this option if you really know what you are doing.</dl>
<h2>Author</h2>
<p>Brian King &lt;brking [at] us.ibm.com&gt;</p>
<h2>Notes</h2>
<dl>
<dt><code>Notes on using under iSeries 5250 telnet</code></p>
<dd></dl>
<p> Only use this utility across 5250 telnet when there are no other options available to you. Since there may be occasions when 5250 telnet is your only option to access your iSeries Linux console, every attempt has been made to make this utility usable under 5250 telnet. By following a few guidelines, you can make your 5250 telnet experience more productive and much less frustrating. 1. First of all, it will be helpful to know how the keys are mapped under 5250 telnet. From the 5250 telnet window, hit ESC. This will get you to the <code>Send TELNET Control Functions</code> menu. Take option 6 to display the keyboard map. Take note of how TAB, ESC, CTLC, and SENDWOCR are bound. They will be useful in the future. 2. When selecting menu options, enter the menu number, followed by the enter key, same as usual. 3. When typing single character commands (eg. r=Refresh), type the single character followed by the SENDWOCR key (F11 by default). 4. When on a device/array/IOA selection screen (eg. Display Disk Unit Details), do NOT use the arrow keys to navigate. Instead use the TAB key (F7 by default) to navigate these screens. 5. Beware of the backspace and delete keys. As a rule do NOT use them. 6. When editing the root kernel message log directory or the default editor, you may use the arrow keys, but not the backspace and delete keys. Use the space bar to remove already typed characters. </p>
