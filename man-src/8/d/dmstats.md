---
title: "dmstats(8)"
name: "dmstats"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dmstats/"
description: "dmstats — device-mapper statistics management"
---

<p>dmstats &#8212; device-mapper statistics management</p>
<h2>Synopsis</h2>
<p><code>dmsetup</code> <code>stats</code> <i>command</i> [OPTIONS] </p>
<dl>
<dt> <code>dmstats</code> <i>command</i> <i>device_name</i> | <code>&#8211;major</code> <i>major</i> <code>&#8211;minor</code> <i>minor</i> | <code>-u</code>|<code>&#8211;uuid</code> <i>uuid</i> [<code>-v</code>|<code>&#8211;verbose]</code></p>
<dt> <code>dmstats</code> <code>clear</code> <i>device_name</i> [<code>&#8211;allprograms</code>|<code>&#8211;programid</code> <i>id</i>] [<code>&#8211;allregions</code>|<code>&#8211;regionid</code> <i>id</i>]</p>
<dt> <code>dmstats</code> <code>create</code> <i>device_name&#8230;</i>|<i>file_path&#8230;</i>|<i></i><code>&#8211;alldevices</code> [<code>&#8211;areas</code> <i>nr_areas</i>|<i></i><code>&#8211;areasize</code> <i>area_size</i>] [<code>&#8211;bounds</code> <i>histogram_boundaries</i>] [<code>&#8211;filemap</code>] [<code>&#8211;follow</code> <i>follow_mode</i>] [<code>&#8211;foreground</code>] [<code>&#8211;nomonitor</code>] [<code>&#8211;nogroup</code>] [<code>&#8211;precise</code>] [<code>&#8211;start</code> <i>start_sector</i> <code>&#8211;length</code> <i>length</i>|<i></i><code>&#8211;segments</code>] [<code>&#8211;userdata</code> <i>user_data</i>] [<code>&#8211;programid</code> <i>id</i>]</p>
<dt> <code>dmstats</code> <code>delete</code> <i>device_name</i>|<i></i><code>&#8211;alldevices</code> [<code>&#8211;allprograms</code>|<code>&#8211;programid</code> <i>id</i>] [<code>&#8211;allregions</code>|<code>&#8211;regionid</code> <i>id</i>]</p>
<dt> <code>dmstats</code> <code>group</code> [<i>device_name</i>|<i></i><code>&#8211;alldevices</code>] [<code>&#8211;alias</code> <i>name</i>] [<code>&#8211;regions</code> <i>regions</i>]</p>
<dt> <code>dmstats</code> <code>help</code> [<code>-c</code>|<code>-C</code>|<code>&#8211;columns</code>]</p>
<dt> <code>dmstats</code> <code>list</code> [<i>device_name</i>] [<code>&#8211;histogram</code>] [<code>&#8211;allprograms</code>|<code>&#8211;programid</code> <i>id</i>] [<code>&#8211;units</code> <i>units</i>] [<code>&#8211;area</code>] [<code>&#8211;region</code>] [<code>&#8211;group</code>] [<code>&#8211;nosuffix</code>] [<code>&#8211;notimesuffix</code>] [<code>-v</code>|<code>&#8211;verbose]</code></p>
<dt> <code>dmstats</code> <code>print</code> [<i>device_name</i>] [<code>&#8211;clear</code>] [<code>&#8211;allprograms</code>|<code>&#8211;programid</code> <i>id</i>] [<code>&#8211;allregions</code>|<code>&#8211;regionid</code> <i>id</i>]</p>
<dt> <code>dmstats</code> <code>report</code> [<i>device_name</i>] [<code>&#8211;interval</code> <i>seconds</i>] [<code>&#8211;count</code> <i>count</i>] [<code>&#8211;units</code> <i>units</i>] [<code>&#8211;histogram</code>] [<code>&#8211;allprograms</code>|<code>&#8211;programid</code> <i>id</i>] [<code>&#8211;allregions</code>|<code>&#8211;regionid</code> <i>id</i>] [<code>&#8211;area</code>] [<code>&#8211;region</code>] [<code>&#8211;group</code>] [<code>-O</code>|<code>&#8211;sort</code> <i>sort_fields</i>] [<code>-S</code>|<code>&#8211;select</code> <i>selection</i>] [<code>&#8211;units</code> <i>units</i>] [<code>&#8211;nosuffix</code>] [<code>&#8211;notimesuffix</code>]</p>
<dt> <code>dmstats</code> <code>ungroup</code> [<i>device_name</i>|<i></i><code>&#8211;alldevices</code>] [<code>&#8211;groupid</code> <i>id</i>]</p>
<dt> <code>dmstats</code> <code>update_filemap</code> <i>file_path</i> [<code>&#8211;groupid</code> <i>id</i>] [<code>&#8211;follow</code> <i>follow_mode</i>] [<code>&#8211;foreground</code>]</dl>
<h2>Description</h2>
<dd>The dmstats program manages IO statistics regions for devices that use the device-mapper driver. Statistics regions may be created, deleted, listed and reported on using the tool. </p>
<p> The first argument to dmstats is a <i>command</i>. </p>
<p> The second argument is the <i>device name</i>, <i>uuid</i> or <i>major</i> and <i>minor</i> numbers. </p>
<p> Further options permit the selection of regions, output format control, and reporting behaviour. </p>
<p> When no device argument is given dmstats will by default operate on all device-mapper devices present. The <code>create</code> and <code>delete</code> commands require the use of <code>&#8211;alldevices</code> when used in this way.</p>
<h2>Options</h2>
<dl>
<dt> <code>&#8211;alias</code> <i>name</i></p>
<dd>
<dd>Specify an alias name for a group.</p>
<dt> <code>&#8211;alldevices</code></p>
<dd>
<dd>If no device arguments are given allow operation on all devices when creating or deleting regions.</p>
<dt> <code>&#8211;allprograms</code></p>
<dd>
<dd>Include regions from all program IDs for list and report operations. </p>
<dt> <code>&#8211;allregions</code></p>
<dd>
<dd>Include all present regions for commands that normally accept a single region identifier.</p>
<dt> <code>&#8211;area</code></p>
<dd>
<dd>When peforming a list or report, include objects of type area in the results.</p>
<dt> <code>&#8211;areas</code> <i>nr_areas</i></p>
<dd>
<dd>Specify the number of statistics areas to create within a new region.</p>
<dt> <code>&#8211;areasize</code> <i>area_size</i>[ <code>b</code>|<code>B</code>|<code>s</code>|<code>S</code>|<code>k</code>|<code>K</code>|<code>m</code>|<code>M</code>|<code>g</code>|<code>G</code>|<code>t</code>|<code>T</code>|<code>p</code>|<code>P</code>|<code>e</code>|<code>E</code>]</p>
<dd>
<dd>Specify the size of areas into which a new region should be divided. An optional suffix selects units of: (<code>b</code>)ytes, (<code>s</code>)ectors, (<code>k</code>)ilobytes, (<code>m</code>)egabytes, (<code>g</code>)igabytes, (<code>t</code>)erabytes, (<code>p</code>)etabytes, (<code>e</code>)xabytes.</p>
<dt> <code>&#8211;clear</code></p>
<dd>
<dd>When printing statistics counters, also atomically reset them to zero.</p>
<dt> <code>&#8211;count</code> <i>count</i></p>
<dd>
<dd>Specify the iteration count for repeating reports. If the count argument is zero reports will continue to repeat until interrupted.</p>
<dt> <code>&#8211;group</code></p>
<dd>
<dd>When peforming a list or report, include objects of type group in the results.</p>
<dt> <code>&#8211;filemap</code></p>
<dd>
<dd>Instead of creating regions on a device as specified by command line options, open the file found at each <code>file_path</code> argument, and create regions corresponding to the locations of the on-disk extents allocated to the file(s).</p>
<dt> <code>&#8211;nomonitor</code></p>
<dd>
<dd>Disable the <code>dmfilemapd</code> daemon when creating new file mapped groups. Normally the device-mapper filemap monitoring daemon, <code>dmfilemapd</code>, is started for each file mapped group to update the set of regions as the file changes on-disk: use of this option disables this behaviour. </p>
<p> Regions in the group may still be updated with the <code>update_filemap</code> command, or by starting the daemon manually.</p>
<dt> <code>&#8211;follow</code> <i>follow_mode</i></p>
<dd>
<dd>Specify the <code>dmfilemapd</code> file following mode. The file map monitoring daemon can monitor files in two distinct ways: the mode affects the behaviour of the daemon when a file under monitoring is renamed or unlinked, and the conditions which cause the daemon to terminate. </p>
<p> The <code>follow_mode</code> argument is either &quot;inode&quot;, for follow-inode mode, or &quot;path&quot;, for follow-path. </p>
<p> If follow-inode mode is used, the daemon will hold the file open, and continue to update regions from the same file descriptor. This means that the mapping will follow rename, move (within the same file system), and unlink operations. This mode is useful if the file is expected to be moved, renamed, or unlinked while it is being monitored. </p>
<p> In follow-inode mode, the daemon will exit once it detects that the file has been unlinked and it is the last holder of a reference to it. </p>
<p> If follow-path is used, the daemon will re-open the provided path on each monitoring iteration. This means that the group will be updated to reflect a new file being moved to the same path as the original file. This mode is useful for files that are expected to be updated via unlink and rename. </p>
<p> In follow-path mode, the daemon will exit if the file is removed and not replaced within a brief tolerance interval. </p>
<p> In either mode, the daemon exits automatically if the monitored group is removed.</p>
<dt> <code>&#8211;foreground</code></p>
<dd>
<dd>Specify that the <code>dmfilemapd</code> daemon should run in the foreground. The daemon will not fork into the background, and will replace the <code>dmstats</code> command that started it.</p>
<dt> <code>&#8211;groupid</code> <i>id</i></p>
<dd>
<dd>Specify the group to operate on.</p>
<dt> <code>&#8211;bounds</code> <i>histogram_boundaries</i>[<code>ns</code>|<code>us</code>|<code>ms</code>|<code>s</code>]</p>
<dd>
<dd>Specify the boundaries of a latency histogram to be tracked for the region as a comma separated list of latency values. Latency values are given in nanoseconds. An optional unit suffix of <code>ns</code>, <code>us</code>, <code>ms</code>, or <code>s</code> may be given after each value to specify units of nanoseconds, microseconds, miliseconds or seconds respectively.</p>
<dt> <code>&#8211;histogram</code></p>
<dd>
<dd>When used with the <code>report</code> and <code>list</code> commands select default fields that emphasize latency histogram data.</p>
<dt> <code>&#8211;interval</code> <i>seconds</i></p>
<dd>
<dd>Specify the interval in seconds between successive iterations for repeating reports. If <code>&#8211;interval</code> is specified but <code>&#8211;count</code> is not, reports will continue to repeat until interrupted.</p>
<dt> <code>&#8211;length</code> <i>length</i>[ <code>b</code>|<code>B</code>|<code>s</code>|<code>S</code>|<code>k</code>|<code>K</code>|<code>m</code>|<code>M</code>|<code>g</code>|<code>G</code>|<code>t</code>|<code>T</code>|<code>p</code>|<code>P</code>|<code>e</code>|<code>E</code>]</p>
<dd>
<dd>Specify the length of a new statistics region in sectors. An optional suffix selects units of: (<code>b</code>)ytes, (<code>s</code>)ectors, (<code>k</code>)ilobytes, (<code>m</code>)egabytes, (<code>g</code>)igabytes, (<code>t</code>)erabytes, (<code>p</code>)etabytes, (<code>e</code>)xabytes.</p>
<dt> <code>-j</code>|<code>&#8211;major</code> <i>major</i></p>
<dd>
<dd>Specify the major number.</p>
<dt> <code>-m</code>|<code>&#8211;minor</code> <i>minor</i></p>
<dd>
<dd>Specify the minor number.</p>
<dt> <code>&#8211;nogroup</code></p>
<dd>
<dd>When creating regions mapping the extents of a file in the file system, do not create a group or set an alias.</p>
<dt> <code>&#8211;nosuffix</code></p>
<dd>
<dd>Suppress the suffix on output sizes. Use with <code>&#8211;units</code> (except h and H) if processing the output.</p>
<dt> <code>&#8211;notimesuffix</code></p>
<dd>
<dd>Suppress the suffix on output time values. Histogram boundary values will be reported in units of nanoseconds.</p>
<dt> <code>-o</code>|<code>&#8211;options</code></p>
<dd>
<dd>Specify which report fields to display.</p>
<dt> <code>-O</code>|<code>&#8211;sort</code> <i>sort_fields</i></p>
<dd>
<dd>Sort output according to the list of fields given. Precede any sort field with &#8216;<code>&#8211;</code>&#8216; for a reverse sort on that column.</p>
<dt> <code>&#8211;precise</code></p>
<dd>
<dd>Attempt to use nanosecond precision counters when creating new statistics regions.</p>
<dt> <code>&#8211;programid</code> <i>id</i></p>
<dd>
<dd>Specify a program ID string. When creating new statistics regions this string is stored with the region. Subsequent operations may supply a program ID in order to select only regions with a matching value. The default program ID for dmstats-managed regions is &quot;dmstats&quot;.</p>
<dt> <code>&#8211;region</code></p>
<dd>
<dd>When peforming a list or report, include objects of type region in the results.</p>
<dt> <code>&#8211;regionid</code> <i>id</i></p>
<dd>
<dd>Specify the region to operate on.</p>
<dt> <code>&#8211;regions</code> <i>region_list</i></p>
<dd>
<dd>Specify a list of regions to group. The group list is a comma-separated list of region identifiers. Continuous sequences of identifiers may be expressed as a hyphen separated range, for example: &#8216;1-10&#8217;.</p>
<dt> <code>&#8211;relative</code></p>
<dd>
<dd>If displaying the histogram report show relative (percentage) values instead of absolute counts.</p>
<dt> <code>-S</code>|<code>&#8211;select</code> <i>selection</i></p>
<dd>
<dd>Display only rows that match <i>selection</i> criteria. All rows with the additional &quot;selected&quot; column (<code>-o selected</code>) showing 1 if the row matches the <i>selection</i> and 0 otherwise. The selection criteria are defined by specifying column names and their valid values while making use of supported comparison operators.</p>
<dt> <code>&#8211;start</code> <i>start</i>[ <code>b</code>|<code>B</code>|<code>s</code>|<code>S</code>|<code>k</code>|<code>K</code>|<code>m</code>|<code>M</code>|<code>g</code>|<code>G</code>|<code>t</code>|<code>T</code>|<code>p</code>|<code>P</code>|<code>e</code>|<code>E</code>]</p>
<dd>
<dd>Specify the start offset of a new statistics region in sectors. An optional suffix selects units of: (<code>b</code>)ytes, (<code>s</code>)ectors, (<code>k</code>)ilobytes, (<code>m</code>)egabytes, (<code>g</code>)igabytes, (<code>t</code>)erabytes, (<code>p</code>)etabytes, (<code>e</code>)xabytes.</p>
<dt> <code>&#8211;segments</code></p>
<dd>
<dd>When used with <code>create</code>, create a new statistics region for each target contained in the given device(s). This causes a separate region to be allocated for each segment of the device. </p>
<p> The newly created regions are automatically placed into a group unless the <code>&#8211;nogroup</code> option is given. When grouping is enabled a group alias may be specified using the <code>&#8211;alias</code> option.</p>
<dt> <code>&#8211;units</code> [<i>units</i>]<i></i>[<code>h</code>|<code>H</code>| <code>b</code>|<code>B</code>|<code>s</code>|<code>S</code>|<code>k</code>|<code>K</code>|<code>m</code>|<code>M</code>|<code>g</code>|<code>G</code>|<code>t</code>|<code>T</code>|<code>p</code>|<code>P</code>|<code>e</code>|<code>E</code>]</p>
<dd>
<dd>Set the display units for report output. All sizes are output in these units: (<code>h</code>)uman-readable, (<code>b</code>)ytes, (<code>s</code>)ectors, (<code>k</code>)ilobytes, (<code>m</code>)egabytes, (<code>g</code>)igabytes, (<code>t</code>)erabytes, (<code>p</code>)etabytes, (<code>e</code>)xabytes. Can also specify custom units e.g. <code>&#8211;units 3M</code>.</p>
<dt> <code>&#8211;userdata</code> <i>user_data</i></p>
<dd>
<dd>Specify user data (a word) to be stored with a new region. The value is added to any internal auxilliary data (for example, group information), and stored with the region in the aux_data field provided by the kernel. Whitespace is not permitted.</p>
<dt> <code>-u</code>|<code>&#8211;uuid</code></p>
<dd>
<dd>Specify the uuid.</p>
<dt> <code>-v</code>|<code>&#8211;verbose</code> [<code>-v</code>|<code>&#8211;verbose</code>]</p>
<dd>
<dd>Produce additional output.</dl>
<h2>Commands</h2>
<dl>
<dt> <code>clear</code> <i>device_name</i> [<code>&#8211;allprograms</code>|<code>&#8211;programid</code> <i>id</i>] [<code>&#8211;allregions</code>|<code>&#8211;regionid</code> <i>id</i>]</p>
<dd>
<dd>Instructs the kernel to clear statistics counters for the speficied regions (with the exception of in-flight IO counters).</p>
<dt> <code>create</code> <i>device_name&#8230;</i>|<i>file_path&#8230;</i>|<i></i><code>&#8211;alldevices</code> [<code>&#8211;areas</code> <i>nr_areas</i>|<i></i><code>&#8211;areasize</code> <i>area_size</i>] [<code>&#8211;bounds</code> <i>histogram_boundaries</i>] [<code>&#8211;filemap</code>] [<code>&#8211;follow</code> <i>follow_mode</i>] [<code>&#8211;foreground</code>] [<code>&#8211;nomonitor</code>] [<code>&#8211;nogroup</code>] [<code>&#8211;precise</code>] [<code>&#8211;start</code> <i>start_sector</i> <code>&#8211;length</code> <i>length</i>|<i></i><code>&#8211;segments</code>] [<code>&#8211;userdata</code> <i>user_data</i>] [<code>&#8211;programid</code> <i>id</i>]</p>
<dd>
<dd>Creates one or more new statistics regions on the specified device(s). </p>
<p> The region will span the entire device unless <code>&#8211;start</code> and <code>&#8211;length</code> or <code>&#8211;segments</code> are given. The <code>&#8211;start</code> an <code>&#8211;length</code> options allow a region of arbitrary length to be placed at an arbitrary offset into the device. The <code>&#8211;segments</code> option causes a new region to be created for each target in the corresponding device-mapper device&#8217;s table. </p>
<p> If the <code>&#8211;precise</code> option is used the command will attempt to create a region using nanosecond precision counters. </p>
<p> If <code>&#8211;bounds</code> is given a latency histogram will be tracked for the new region. The boundaries of the histogram bins are given as a comma separated list of latency values. There is an implicit lower bound of zero on the first bin and an implicit upper bound of infinity (or the configured interval duration) on the final bin. </p>
<p> Latencies are given in nanoseconds. An optional unit suffix of ns, us, ms, or s may be given after each value to specify units of nanoseconds, microseconds, miliseconds or seconds respectively, so for example, 10ms is equivalent to 10000000. Latency values with a precision of less than one milisecond can only be used when precise timestamps are enabled: if <code>&#8211;precise</code> is not given and values less than one milisecond are used it will be enabled automatically. </p>
<p> An optional <code>program_id</code> or <code>user_data</code> string may be associated with the region. A <code>program_id</code> may then be used to select regions for subsequent list, print, and report operations. The <code>user_data</code> stores an arbitrary string and is not used by dmstats or the device-mapper kernel statistics subsystem. </p>
<p> By default dmstats creates regions with a <code>program_id</code> of &quot;dmstats&quot;. </p>
<p> On success the <code>region_id</code> of the newly created region is printed to stdout. </p>
<p> If the <code>&#8211;filemap</code> option is given with a regular file, or list of files, as the <code>file_path</code> argument, instead of creating regions with parameters specified on the command line, <code>dmstats</code> will open the files located at <code>file_path</code> and create regions corresponding to the physical extents allocated to the file. This can be used to monitor statistics for individual files in the file system, for example, virtual machine images, swap areas, or large database files. </p>
<p> To work with the <code>&#8211;filemap</code> option, files must be located on a local file system, backed by a device-mapper device, that supports physical extent data using the FIEMAP ioctl (Ext4 and XFS for e.g.). </p>
<p> By default regions that map a file are placed into a group and the group alias is set to the basename of the file. This behaviour can be overridden with the <code>&#8211;alias</code> and <code>&#8211;nogroup</code> options. </p>
<p> Creating a group that maps a file automatically starts a daemon, <code>dmfilemapd</code> to monitor the file and update the mapping as the extents allocated to the file change. This behaviour can be disabled using the <code>&#8211;nomonitor</code> option. </p>
<p> Use the <code>&#8211;group</code> option to only display information for groups when listing and reporting.</p>
<dt> <code>delete</code> <i>device_name</i>|<i></i><code>&#8211;alldevices</code> [<code>&#8211;allprograms</code>|<code>&#8211;programid</code> <i>id</i>] [<code>&#8211;allregions</code>|<code>&#8211;regionid</code> <i>id</i>]</p>
<dd>
<dd>Delete the specified statistics region. All counters and resources used by the region are released and the region will not appear in the output of subsequent list, print, or report operations. </p>
<p> All regions registered on a device may be removed using <code>&#8211;allregions</code>. </p>
<p> To remove all regions on all devices both <code>&#8211;allregions</code> and <code>&#8211;alldevices</code> must be used. </p>
<p> If a <code>&#8211;groupid</code> is given instead of a <code>&#8211;regionid</code> the command will attempt to delete the group and all regions that it contains. </p>
<p> If a deleted region is the first member of a group of regions the group will also be removed.</p>
<dt> <code>group</code> [<i>device_name</i>|<i></i><code>&#8211;alldevices</code>] [<code>&#8211;alias</code> <i>name</i>] [<code>&#8211;regions</code> <i>regions</i>]</p>
<dd>
<dd>Combine one or more statistics regions on the specified device into a group. </p>
<p> The list of regions to be grouped is specified with <code>&#8211;regions</code> and an optional alias may be assigned with <code>&#8211;alias</code>. The set of regions is given as a comma-separated list of region identifiers. A continuous range of identifers spanning from <code>R1</code> to <code>R2</code> may be expressed as &#8216;<code>R1</code>&#8211;<code>R2</code>&#8216;. </p>
<p> Regions that have a histogram configured can be grouped: in this case the number of histogram bins and their bounds must match exactly. </p>
<p> On success the group list and newly created <code>group_id</code> are printed to stdout. </p>
<p> The group metadata is stored with the first (lowest numbered) <code>region_id</code> in the group: deleting this region will also delete the group and other group members will be returned to their prior state.</p>
<dt> <code>help</code> [<code>-c</code>|<code>-C</code>|<code>&#8211;columns</code>]</p>
<dd>
<dd>Outputs a summary of the commands available, optionally including the list of report fields.</p>
<dt> <code>list</code> [<i>device_name</i>] [<code>&#8211;histogram</code>] [<code>&#8211;allprograms</code>|<code>&#8211;programid</code> <i>id</i>] [<code>&#8211;units</code> <i>units</i>] [<code>&#8211;area</code>] [<code>&#8211;region</code>] [<code>&#8211;group</code>] [<code>&#8211;nosuffix</code>] [<code>&#8211;notimesuffix</code>] [<code>-v</code>|<code>&#8211;verbose]</code></p>
<dd>
<dd>List the statistics regions, areas, or groups registered on the device. If the <code>&#8211;allprograms</code> switch is given all regions will be listed regardless of region program ID values. </p>
<p> By default only regions and groups are included in list output. If <code>-v</code> or <code>&#8211;verbose</code> is given the report will also include a row of information for each configured group and for each area contained in each region displayed. </p>
<p> Regions that contain a single area are by default omitted from the verbose list since their properties are identical to the area that they contain &#8211; to view all regions regardless of the number of areas present use <code>&#8211;region</code>). To also view the areas contained within regions use <code>&#8211;area</code>. </p>
<p> If <code>&#8211;histogram</code> is given the report will include the bin count and latency boundary values for any configured histograms.</p>
<dt> <code>print</code> [<i>device_name</i>] [<code>&#8211;clear</code>] [<code>&#8211;allprograms</code>|<code>&#8211;programid</code> <i>id</i>] [<code>&#8211;allregions</code>|<code>&#8211;regionid</code> <i>id</i>]</p>
<dd>
<dd>Print raw statistics counters for the specified region or for all present regions.</p>
<dt> <code>report</code> [<i>device_name</i>] [<code>&#8211;interval</code> <i>seconds</i>] [<code>&#8211;count</code> <i>count</i>] [<code>&#8211;units</code> <i>units</i>] [<code>&#8211;histogram</code>] [<code>&#8211;allprograms</code>|<code>&#8211;programid</code> <i>id</i>] [<code>&#8211;allregions</code>|<code>&#8211;regionid</code> <i>id</i>] [<code>&#8211;area</code>] [<code>&#8211;region</code>] [<code>&#8211;group</code>] [<code>-O</code>|<code>&#8211;sort</code> <i>sort_fields</i>] [<code>-S</code>|<code>&#8211;select</code> <i>selection</i>] [<code>&#8211;units</code> <i>units</i>] [<code>&#8211;nosuffix</code>] [<code>&#8211;notimesuffix</code>]</p>
<dd>
<dd>Start a report for the specified object or for all present objects. If the count argument is specified, the report will repeat at a fixed interval set by the <code>&#8211;interval</code> option. The default interval is one second. </p>
<p> If the <code>&#8211;allprograms</code> switch is given, all regions will be listed, regardless of region program ID values. </p>
<p> If the <code>&#8211;histogram</code> is given the report will include the histogram values and latency boundaries. </p>
<p> If the <code>&#8211;relative</code> is used the default histogram field displays bin values as a percentage of the total number of I/Os. </p>
<p> Object types (areas, regions and groups) to include in the report are selected using the <code>&#8211;area</code>, <code>&#8211;region</code>, and <code>&#8211;group</code> options.</p>
<dt> <code>ungroup</code> [<i>device_name</i>|<i></i><code>&#8211;alldevices</code>] [<code>&#8211;groupid</code> <i>id</i>]</p>
<dd>
<dd>Remove an existing group and return all the group&#8217;s regions to their original state. </p>
<p> The group to be removed is specified using <code>&#8211;groupid</code>.</p>
<dt> <code>update_filemap</code> <i>file_path</i> [<code>&#8211;groupid</code> <i>id</i>] [<code>&#8211;follow</code> <i>follow_mode</i>] [<code>&#8211;foreground</code>]</p>
<dd>
<dd>Update a group of <code>dmstats</code> regions specified by <code>group_id</code>, that were previously created with <code>&#8211;filemap</code>, either directly, or by starting the monitoring daemon, <code>dmfilemapd</code>. </p>
<p> This will add and remove regions to reflect changes in the allocated extents of the file on-disk, since the time that it was crated or last updated. </p>
<p> Use of this command is not normally needed since the <code>dmfilemapd</code> daemon will automatically monitor filemap groups and perform these updates when required. </p>
<p> If a filemapped group was created with <code>&#8211;nomonitor</code>, or the daemon has been killed, the <code>update_filemap</code> can be used to manually force an update or start a new daemon. </p>
<p> Use <code>&#8211;nomonitor</code> to force a direct update and disable starting the monitoring daemon.</dl>
<h2>Regions, Areas, And Groups</h2>
<p>The device-mapper statistics facility allows separate performance counters to be maintained for arbitrary regions of devices. A region may span any range: from a single sector to the whole device. A region may be further sub-divided into a number of distinct areas (one or more), each with its own counter set. In this case a summary value for the entire region is also available for use in reports. </p>
<p> In addition, one or more regions on one device can be combined into a statistics group. Groups allow several regions to be aggregated and reported as a single entity; counters for all regions and areas are summed and used to report totals for all group members. Groups also permit the assignment of an optional alias, allowing meaningful names to be associated with sets of regions. </p>
<p> The group metadata is stored with the first (lowest numbered) <code>region_id</code> in the group: deleting this region will also delete the group and other group members will be returned to their prior state. </p>
<p> By default new regions span the entire device. The <code>&#8211;start</code> and <code>&#8211;length</code> options allows a region of any size to be placed at any location on the device. </p>
<p> Using offsets it is possible to create regions that map individual objects within a block device (for example: partitions, files in a file system, or stripes or other structures in a RAID volume). Groups allow several non-contiguous regions to be assembled together for reporting and data aggregation. </p>
<p> A region may be either divided into the specified number of equal-sized areas, or into areas of the given size by specifying one of <code>&#8211;areas</code> or <code>&#8211;areasize</code> when creating a region with the <code>create</code> command. Depending on the size of the areas and the device region the final area within the region may be smaller than requested. </p>
<p> <code>Region identifiers</code> </p>
<p> Each region is assigned an identifier when it is created that is used to reference the region in subsequent operations. Region identifiers are unique within a given device (including across different <code>program_id</code> values). </p>
<p> Depending on the sequence of create and delete operations, gaps may exist in the sequence of <code>region_id</code> values for a particular device. </p>
<p> The <code>region_id</code> should be treated as an opaque identifier used to reference the region. </p>
<p> <code>Group identifiers</code> </p>
<p> Groups are also assigned an integer identifier at creation time; like region identifiers, group identifiers are unique within the containing device. </p>
<p> The <code>group_id</code> should be treated as an opaque identifier used to reference the group.</p>
<h2>File Mapping</h2>
<p>Using <code>&#8211;filemap</code>, it is possible to create regions that correspond to the extents of a file in the file system. This allows IO statistics to be monitored on a per-file basis, for example to observe large database files, virtual machine images, or other files of interest. </p>
<p> To be able to use file mapping, the file must be backed by a device-mapper device, and in a file system that supports the FIEMAP ioctl (and which returns data describing the physical location of extents). This currently includes <code><a href="/docs/linux/man/5-xfs/">xfs</a>(5)</code> and <code><a href="/docs/linux/man/5-ext4/">ext4</a>(5)</code>. </p>
<p> By default the regions making up a file are placed together in a group, and the group alias is set to the <code><a href="/docs/linux/man/3-basename/">basename</a>(3)</code> of the file. This allows statistics to be reported for the file as a whole, aggregating values for the regions making up the group. To see only the whole file (group) when using the <code>list</code> and <code>report</code> commands, use <code>&#8211;group</code>. </p>
<p> Since it is possible for the file to change after the initial group of regions is created, the <code>update_filemap</code> command, and <code>dmfilemapd</code> daemon are provided to update file mapped groups either manually or automatically. </p>
<p> <code>File follow modes</code> </p>
<p> The file map monitoring daemon can monitor files in two distinct ways: follow-inode mode, and follow-path mode. </p>
<p> The mode affects the behaviour of the daemon when a file under monitoring is renamed or unlinked, and the conditions which cause the daemon to terminate. </p>
<p> If follow-inode mode is used, the daemon will hold the file open, and continue to update regions from the same file descriptor. This means that the mapping will follow rename, move (within the same file system), and unlink operations. This mode is useful if the file is expected to be moved, renamed, or unlinked while it is being monitored. </p>
<p> In follow-inode mode, the daemon will exit once it detects that the file has been unlinked and it is the last holder of a reference to it. </p>
<p> If follow-path is used, the daemon will re-open the provided path on each monitoring iteration. This means that the group will be updated to reflect a new file being moved to the same path as the original file. This mode is useful for files that are expected to be updated via unlink and rename. </p>
<p> In follow-path mode, the daemon will exit if the file is removed and not replaced within a brief tolerance interval (one second). </p>
<p> To stop the daemon, delete the group containing the mapped regions: the daemon will automatically shut down. </p>
<p> The daemon can also be safely killed at any time and the group kept: if the file is still being allocated the mapping will become progressively out-of-date as extents are added and removed (in this case the daemon can be re-started or the group updated manually with the <code>update_filemap</code> command). </p>
<p> See the <code>create</code> command and <code>&#8211;filemap</code>, <code>&#8211;follow</code>, and <code>&#8211;nomonitor</code> options for further information. </p>
<p> <code>Limitations</code> </p>
<p> The daemon attempts to maintain good synchronisation between the file extents and the regions contained in the group, however, since it can only react to new allocations once they have been written, there are inevitably some IO events that cannot be counted when a file is growing, particularly if the file is being extended by a single thread writing beyond end-of-file (for example, the <code>dd</code> program). </p>
<p> There is a further loss of events in that there is currently no way to atomically resize a <code>dmstats</code> region and preserve its current counter values. This affects files when they grow by extending the final extent, rather than allocating a new extent: any events that had accumulated in the region between any prior operation and the resize are lost. </p>
<p> File mapping is currently most effective in cases where the majority of IO does not trigger extent allocation. Future updates may address these limitations when kernel support is available.</p>
<h2>Report Fields</h2>
<p>The dmstats report provides several types of field that may be added to the default field set, or used to create custom reports. </p>
<p> All performance counters and metrics are calculated per-area.</p>
<h3>Derived metrics</h3>
<p>A number of metrics fields are included that provide high level performance indicators. These are based on the fields provided by the conventional Linux iostat program and are derived from the basic counter values provided by the kernel for each area.</p>
<dl>
<dt><code>reads_merged_per_sec</code></p>
<dd>Reads merged per second.</p>
<dt><code>writes_merged_per_sec</code></p>
<dd>Writes merged per second.</p>
<dt><code>reads_per_sec</code></p>
<dd>Reads completed per second.</p>
<dt><code>writes_per_sec</code></p>
<dd>Writes completed per second.</p>
<dt><code>read_size_per_sec</code></p>
<dd>Size of data read per second.</p>
<dt><code>write_size_per_sec</code></p>
<dd>Size of data written per second.</p>
<dt><code>avg_request_size</code></p>
<dd>Average request size.</p>
<dt><code>queue_size</code></p>
<dd>Average queue size.</p>
<dt><code>await</code></p>
<dd>The average wait time for read and write operations.</p>
<dt><code>r_await</code></p>
<dd>The average wait time for read operations.</p>
<dt><code>w_await</code></p>
<dd>The average wait time for write operations.</p>
<dt><code>throughput</code></p>
<dd>The device throughput in operations per second.</p>
<dt><code>service_time</code></p>
<dd>The average service time (in milliseconds) for operations issued to the device.</p>
<dt><code>util</code></p>
<dd>Percentage of CPU time during which I/O requests were issued to the device (bandwidth utilization for the device). Device saturation occurs when this value is close to 100%.</dl>
<h3>Group, region and area meta fields</h3>
<p>Meta fields provide information about the groups, regions, or areas that the statistics values relate to. This includes the region and area identifier, start, length, and counts, as well as the program ID and user data values.</p>
<dl>
<dt><code>region_id</code></p>
<dd>Region identifier. This is a non-negative integer returned by the kernel when a statistics region is created.</p>
<dt><code>region_start</code></p>
<dd>The region start location. Display units are selected by the <code>&#8211;units</code> option.</p>
<dt><code>region_len</code></p>
<dd>The length of the region. Display units are selected by the <code>&#8211;units</code> option.</p>
<dt><code>area_id</code></p>
<dd>Area identifier. Area identifiers are assigned by the device-mapper statistics library and uniquely identify each area within a region. Each ID corresponds to a distinct set of performance counters for that area of the statistics region. Area identifiers are always monotonically increasing within a region so that higher ID values correspond to greater sector addresses within the area and no gaps in the sequence of identifiers exist.</p>
<dt><code>area_start</code></p>
<dd>The area start location. Display units are selected by the <code>&#8211;units</code> option.</p>
<dt><code>area_len</code></p>
<dd>The length of the area. Display units are selected by the <code>&#8211;units</code> option.</p>
<dt><code>area_count</code></p>
<dd>The number of areas in this region.</p>
<dt><code>program_id</code></p>
<dd>The program ID value associated with this region.</p>
<dt><code>user_data</code></p>
<dd>The user data value associated with this region.</p>
<dt><code>group_id</code></p>
<dd>Group identifier. This is a non-negative integer returned by the dmstats <code>group</code> command when a statistics group is created.</p>
<dt><code>interval_ns</code></p>
<dd>The estimated interval over which the current counter values have accumulated. The value is reported as an interger expressed in units of nanoseconds.</p>
<dt><code>interval</code></p>
<dd>The estimated interval over which the current counter values have accumulated. The value is reported as a real number in units of seconds.</dl>
<h3>Basic counters</h3>
<p>Basic counters provide access to the raw counter data from the kernel, allowing further processing to be carried out by another program. </p>
<p> The kernel provides thirteen separate counters for each statistics area. The first eleven of these match the counters provided in /proc/diskstats or /sys/block/*/*/stat. The final pair provide separate counters for read and write time.</p>
<dl>
<dt><code>read_count</code></p>
<dd>Count of reads completed this interval.</p>
<dt><code>reads_merged_count</code></p>
<dd>Count of reads merged this interval.</p>
<dt><code>read_sector_count</code></p>
<dd>Count of 512 byte sectors read this interval.</p>
<dt><code>read_time</code></p>
<dd>Accumulated duration of all read requests (ns).</p>
<dt><code>write_count</code></p>
<dd>Count of writes completed this interval.</p>
<dt><code>writes_merged_count</code></p>
<dd>Count of writes merged this interval.</p>
<dt><code>write_sector_count</code></p>
<dd>Count of 512 byte sectors written this interval.</p>
<dt><code>write_time</code></p>
<dd>Accumulated duration of all write requests (ns).</p>
<dt><code>in_progress_count</code></p>
<dd>Count of requests currently in progress.</p>
<dt><code>io_ticks</code></p>
<dd>Nanoseconds spent servicing requests.</p>
<dt><code>queue_ticks</code></p>
<dd>This field is incremented at each I/O start, I/O completion, I/O merge, or read of these stats by the number of I/Os in progress multiplied by the number of milliseconds spent doing I/O since the last update of this field. This can provide an easy measure of both I/O completion time and the backlog that may be accumulating.</p>
<dt><code>read_ticks</code></p>
<dd>Nanoseconds spent servicing reads.</p>
<dt><code>write_ticks</code></p>
<dd>Nanoseconds spent servicing writes.</dl>
<h3>Histogram fields</h3>
<p>Histograms measure the frequency distribution of user specified I/O latency intervals. Histogram bin boundaries are specified when a region is created. </p>
<p> A brief representation of the histogram values and latency intervals can be included in the report using these fields.</p>
<dl>
<dt><code>hist_count</code></p>
<dd>A list of the histogram counts for the current statistics area in order of ascending latency value. Each value represents the number of I/Os with latency times falling into that bin&#8217;s time range during the sample period.</p>
<dt><code>hist_count_bounds</code></p>
<dd>A list of the histogram counts for the current statistics area in order of ascending latency value including bin boundaries: each count is prefixed by the lower bound of the corresponding histogram bin.</p>
<dt><code>hist_count_ranges</code></p>
<dd>A list of the histogram counts for the current statistics area in order of ascending latency value including bin boundaries: each count is prefixed by both the lower and upper bounds of the corresponding histogram bin.</p>
<dt><code>hist_percent</code></p>
<dd>A list of the relative histogram values for the current statistics area in order of ascending latency value, expressed as a percentage. Each value represents the proportion of I/Os with latency times falling into that bin&#8217;s time range during the sample period.</p>
<dt><code>hist_percent_bounds</code></p>
<dd>A list of the relative histogram values for the current statistics area in order of ascending latency value, expressed as a percentage and including bin boundaries. Each value represents the proportion of I/Os with latency times falling into that bin&#8217;s time range during the sample period and is prefixed with the corresponding bin&#8217;s lower bound.</p>
<dt><code>hist_percent_ranges</code></p>
<dd>A list of the relative histogram values for the current statistics area in order of ascending latency value, expressed as a percentage and including bin boundaries. Each value represents the proportion of I/Os with latency times falling into that bin&#8217;s time range during the sample period and is prefixed with the corresponding bin&#8217;s lower and upper bounds.</p>
<dt><code>hist_bounds</code></p>
<dd>A list of the histogram boundary values for the current statistics area in order of ascending latency value. The values are expressed in whole units of seconds, miliseconds, microseconds or nanoseconds with a suffix indicating the unit.</p>
<dt><code>hist_ranges</code></p>
<dd>A list of the histogram bin ranges for the current statistics area in order of ascending latency value. The values are expressed as &quot;LOWER-UPPER&quot; in whole units of seconds, miliseconds, microseconds or nanoseconds with a suffix indicating the unit.</p>
<dt><code>hist_bins</code></p>
<dd>The number of latency histogram bins configured for the area.</dl>
<h2>Examples</h2>
<p>Create a whole-device region with one area on vg00/lvol1<br />
 # <code>dmstats create vg00/lvol1</code><br />
 vg00/lvol1: Created new region with 1 area(s) as region ID 0 </p>
<p> Create a 32M region 1G into device d0<br />
 # <code>dmstats create &#8211;start 1G &#8211;length 32M d0</code><br />
 d0: Created new region with 1 area(s) as region ID 0 </p>
<p> Create a whole-device region with 8 areas on every device </p>
<p> # <code>dmstats create &#8211;areas 8</code><br />
 vg00-lvol1: Created new region with 8 area(s) as region ID 0<br />
 vg00-lvol2: Created new region with 8 area(s) as region ID 0<br />
 vg00-lvol3: Created new region with 8 area(s) as region ID 0<br />
 vg01-lvol0: Created new region with 8 area(s) as region ID 2<br />
 vg01-lvol1: Created new region with 8 area(s) as region ID 0<br />
 vg00-lvol2: Created new region with 8 area(s) as region ID 1 </p>
<p> Delete all regions on all devices </p>
<p> # <code>dmstats delete &#8211;alldevices &#8211;allregions</code> </p>
<p> Create a whole-device region with areas 10GiB in size on vg00/lvol1 using dmsetup </p>
<p> # <code>dmsetup stats create &#8211;areasize 10G vg00/lvol1</code><br />
 vg00-lvol1: Created new region with 5 area(s) as region ID 1 </p>
<p> Create a 1GiB region with 16 areas at the start of vg00/lvol1<br />
 # <code>dmstats create &#8211;start 0 &#8211;len 1G &#8211;areas=16 vg00/lvol1</code><br />
 vg00-lvol1: Created new region with 16 area(s) as region ID 0 </p>
<p> List the statistics regions registered on vg00/lvol1<br />
 # <code>dmstats list vg00/lvol1</code><br />
 Name RgID RStart RSize #Areas ASize ProgID<br />
 vg00-lvol1 0 0 61.00g 1 61.00g dmstats<br />
 vg00-lvol1 1 61.00g 19.20g 1 19.20g dmstats<br />
 vg00-lvol1 2 80.20g 2.14g 1 2.14g dmstats </p>
<p> Display five statistics reports for vg00/lvol1 at an interval of one second </p>
<p> # <code>dmstats report &#8211;interval 1 &#8211;count 5 vg00/lvol1</code><br />
 # <code>dmstats report</code><br />
 Name RgID ArID AStart ASize RRqM/s WRqM/s R/s W/s RSz/s WSz/s AvRqSz QSize Util% AWait RdAWa WrAWa<br />
 vg_hex-lv_home 0 0 0 61.00g 0.00 0.00 0.00 218.00 0 1.04m 4.50k 2.97 81.70 13.62 0.00 13.62<br />
 vg_hex-lv_home 1 0 61.00g 19.20g 0.00 0.00 0.00 5.00 0 548.00k 109.50k 0.14 11.00 27.40 0.00 27.40<br />
 vg_hex-lv_home 2 0 80.20g 2.14g 0.00 0.00 0.00 14.00 0 1.15m 84.00k 0.39 18.70 27.71 0.00 27.71 </p>
<p> Create one region for reach target contained in device vg00/lvol1 </p>
<p> # <code>dmstats create &#8211;segments vg00/lvol1</code><br />
 vg00-lvol1: Created new region with 1 area(s) as region ID 0<br />
 vg00-lvol1: Created new region with 1 area(s) as region ID 1<br />
 vg00-lvol1: Created new region with 1 area(s) as region ID 2 </p>
<p> Create regions mapping each file in the directory images/ and place them into separate groups, each named after the corresponding file<br />
 # <code>dmstats create &#8211;filemap images/*</code><br />
 images/vm1.qcow2: Created new group with 87 region(s) as group ID 0.<br />
 images/vm1-1.qcow2: Created new group with 8 region(s) as group ID 87.<br />
 images/vm2.qcow2: Created new group with 11 region(s) as group ID 95.<br />
 images/vm2-1.qcow2: Created new group with 1454 region(s) as group ID 106.<br />
 images/vm3.img: Created new group with 2 region(s) as group ID 1560. </p>
<p> Print raw counters for region 4 on device d0<br />
 # <code>dmstats print &#8211;regionid 4 d0</code><br />
 2097152+65536 0 0 0 0 29 0 264 701 0 41 701 0 41</p>
<h2>Authors</h2>
<p>Bryn M. Reeves &lt;bmr [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8) LVM2 resource page: <a rel="nofollow" href="https://www.sourceware.org/lvm2/">https://www.sourceware.org/lvm2/</a><br />
 Device-mapper resource page: <a rel="nofollow" href="http://sources.redhat.com/dm/">http://sources.redhat.com/dm/</a><br />
 Device-mapper statistics kernel documentation<br />
 <i>Documentation/device-mapper/statistics.txt</i> </p>
