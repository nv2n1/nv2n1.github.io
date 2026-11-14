---
title: "lsblk(8)"
name: "lsblk"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lsblk/"
description: "lsblk – list block devices"
---

<p>lsblk &#8211; list block devices</p>
<h2>Synopsis</h2>
<p><code>lsblk</code> [options] [<i>device</i>&#8230;]</p>
<h2>Description</h2>
<p><code>lsblk</code> lists information about all available or the specified block devices. The <code>lsblk</code> command reads the <code>sysfs</code> filesystem and <code>udev db</code> to gather information. If the udev db is not available or <code>lsblk</code> is compiled without udev support, then it tries to read LABELs, UUIDs and filesystem types from the block device. In this case root permissions are necessary. </p>
<p> The command prints all block devices (except RAM disks) in a tree-like format by default. Use <code>lsblk &#8211;help</code> to get a list of all available columns. </p>
<p> The default output, as well as the default output from options like <code>&#8211;fs</code> and <code>&#8211;topology</code>, is subject to change. So whenever possible, you should avoid using default outputs in your scripts. Always explicitly define expected columns by using <code>&#8211;output</code> <i>columns-list</i> and <code>&#8211;list</code> in environments where a stable output is required. </p>
<p> Note that <code>lsblk</code> might be executed in time when <code>udev</code> does not have all information about recently added or modified devices yet. In this case it is recommended to use <code>udevadm settle</code> before <code>lsblk</code> to synchronize with udev. </p>
<p> The relationship between block devices and filesystems is not always one-to-one. The filesystem may use more block devices, or the same filesystem may be accessible by more paths. This is the reason why <code>lsblk</code> provides MOUNTPOINT and MOUNTPOINTS (pl.) columns. The column MOUNTPOINT displays only one mount point (usually the last mounted instance of the filesystem), and the column MOUNTPOINTS displays by multi-line cell all mount points associated with the device.</p>
<h2>Options</h2>
<p><code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dd>Also list empty devices and RAM disk devices.</dl>
<p> <code>-b</code>, <code>&#8211;bytes</code></p>
<dl>
<dd>Print the SIZE column in bytes rather than in a human-readable format.</dl>
<p> <code>-D</code>, <code>&#8211;discard</code></p>
<dl>
<dd>Print information about the discarding capabilities (TRIM, UNMAP) for each device.</dl>
<p> <code>-d</code>, <code>&#8211;nodeps</code></p>
<dl>
<dd>Do not print holder devices or slaves. For example, <code>lsblk &#8211;nodeps /dev/sda</code> prints information about the sda device only.</dl>
<p> <code>-E</code>, <code>&#8211;dedup</code> <i>column</i></p>
<dl>
<dd>Use <i>column</i> as a de-duplication key to de-duplicate output tree. If the key is not available for the device, or the device is a partition and parental whole-disk device provides the same key than the device is always printed. </p>
<p> The usual use case is to de-duplicate output on system multi-path devices, for example by <code>-E WWN</code>.</dl>
<p> <code>-e</code>, <code>&#8211;exclude</code> <i>list</i></p>
<dl>
<dd>Exclude the devices specified by the comma-separated <i>list</i> of major device numbers. Note that RAM disks (major=1) are excluded by default if <code>&#8211;all</code> is not specified. The filter is applied to the top-level devices only. This may be confusing for <code>&#8211;list</code> output format where hierarchy of the devices is not obvious.</dl>
<p> <code>-f</code>, <code>&#8211;fs</code></p>
<dl>
<dd>Output info about filesystems. This option is equivalent to <code>-o NAME,FSTYPE,FSVER,LABEL,UUID,FSAVAIL,FSUSE%,MOUNTPOINTS</code>. The authoritative information about filesystems and raids is provided by the <code><a href="/docs/linux/man/8-blkid/">blkid</a></code>(8) command.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<p> <code>-I</code>, <code>&#8211;include</code> <i>list</i></p>
<dl>
<dd>Include devices specified by the comma-separated <i>list</i> of major device numbers. The filter is applied to the top-level devices only. This may be confusing for <code>&#8211;list</code> output format where hierarchy of the devices is not obvious.</dl>
<p> <code>-i</code>, <code>&#8211;ascii</code></p>
<dl>
<dd>Use ASCII characters for tree formatting.</dl>
<p> <code>-J</code>, <code>&#8211;json</code></p>
<dl>
<dd>Use JSON output format. It&#8217;s strongly recommended to use <code>&#8211;output</code> and also <code>&#8211;tree</code> if necessary.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dd>Produce output in the form of a list. The output does not provide information about relationships between devices and since version 2.34 every device is printed only once if <code>&#8211;pairs</code> or <code>&#8211;raw</code> not specified (the parsable outputs are maintained in backwardly compatible way).</dl>
<p> <code>-M</code>, <code>&#8211;merge</code></p>
<dl>
<dd>Group parents of sub-trees to provide more readable output for RAIDs and Multi-path devices. The tree-like output is required.</dl>
<p> <code>-m</code>, <code>&#8211;perms</code></p>
<dl>
<dd>Output info about device owner, group and mode. This option is equivalent to <code>-o NAME,SIZE,OWNER,GROUP,MODE</code>.</dl>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dd>Do not print a header line.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dd>Specify which output columns to print. Use <code>&#8211;help</code> to get a list of all supported columns. The columns may affect tree-like output. The default is to use tree for the column &#8216;NAME&#8217; (see also <code>&#8211;tree</code>). </p>
<p> The default list of columns may be extended if <i>list</i> is specified in the format <i>+list</i> (e.g., <code>lsblk -o +UUID</code>).</dl>
<p> <code>-O</code>, <code>&#8211;output-all</code></p>
<dl>
<dd>Output all available columns.</dl>
<p> <code>-P</code>, <code>&#8211;pairs</code></p>
<dl>
<dd>Produce output in the form of key=&quot;value&quot; pairs. The output lines are still ordered by dependencies. All potentially unsafe value characters are hex-escaped (
