---
title: "lxc-create(1)"
name: "lxc-create"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lxc-create/"
description: "lxc-create – creates a container"
---

<h2>NAME</h2>
<p> lxc-create &#8211; creates a container</p>
<h2>SYNOPSIS</h2>
<p> <code>lxc-create</code> {-n <i>name</i>} [-f <i>config_file</i>] {-t <i>template</i>} [-B <i>backingstore</i>] [&#8211; <i>template-options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lxc-create</code> creates a system object where is stored the configuration information and where can be stored user information. The identifier <i>name</i> is used to specify the container to be used with the different lxc commands. </p>
<p> The object is a directory created in <i>/var/lib/lxc</i> and identified by its name. </p>
<p> The object is the definition of the different resources an application can use or can see. The more the configuration file contains information, the more the container is isolated and the more the application is jailed. </p>
<p> If the configuration file <i>config_file</i> is not specified, the container will be created with the default isolation: processes, sysv ipc and mount points.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f </code><i>config_file</i></p>
<dd> Specify the configuration file to configure the virtualization and isolation functionalities for the container.</p>
<dt><code>-t </code><i>template</i></p>
<dd> &#8216;template&#8217; is the short name of an existing &#8216;lxc-template&#8217; script that is called by lxc-create, eg. busybox, debian, fedora, ubuntu or sshd. Refer to the examples in <i>/usr/share/lxc/templates</i> for details of the expected script structure. Alternatively, the full path to an executable template script can also be passed as a parameter. &quot;none&quot; can be used to force lxc-create to skip rootfs creation.</p>
<dt><code>-B </code><i>backingstore</i></p>
<dd> &#8216;backingstore&#8217; is one of &#8216;dir&#8217;, &#8216;lvm&#8217;, &#8216;loop&#8217;, &#8216;btrfs&#8217;, &#8216;zfs&#8217;, or &#8216;best&#8217;. The default is &#8216;dir&#8217;, meaning that the container root filesystem will be a directory under <i>/var/lib/lxc/container/rootfs</i>. This backing store type allows the optional <i>&#8211;dir ROOTFS</i> to be specified, meaning that the container rootfs should be placed under the specified path, rather than the default. (The &#8216;none&#8217; backingstore type is an alias for &#8216;dir&#8217;.) If &#8216;btrfs&#8217; is specified, then the target filesystem must be btrfs, and the container rootfs will be created as a new subvolume. This allows snapshotted clones to be created, but also causes rsync &#8211;one-filesystem to treat it as a separate filesystem. If backingstore is &#8216;lvm&#8217;, then an lvm block device will be used and the following further options are available: <i>&#8211;lvname lvname1</i> will create an LV named <i>lvname1</i> rather than the default, which is the container name. <i>&#8211;vgname vgname1</i> will create the LV in volume group <i>vgname1</i> rather than the default, <i>lxc</i>. <i>&#8211;thinpool thinpool1</i> will create the LV as a thin-provisioned volume in the pool named <i>thinpool1</i> rather than the default, <i>lxc</i>. <i>&#8211;fstype FSTYPE</i> will create an FSTYPE filesystem on the LV, rather than the default, which is ext4. <i>&#8211;fssize SIZE</i> will create a LV (and filesystem) of size SIZE rather than the default, which is 1G. </p>
<p> If backingstore is &#8216;loop&#8217;, you can use <i>&#8211;fstype FSTYPE</i> and <i>&#8211;fssize SIZE</i> as &#8216;lvm&#8217;. The default values for these options are the same as &#8216;lvm&#8217;. </p>
<p> If backingstore is &#8216;best&#8217;, then lxc will try, in order, btrfs, zfs, lvm, and finally a directory backing store.</p>
<dt><code>&#8212; </code><i>template-options</i></p>
<dd> This will pass <i>template-options</i> to the template as arguments. To see the list of options supported by the template, you can run <code>lxc-create -t TEMPLATE -h</code>.</dl>
<h2>COMMON OPTIONS</h2>
<p> These options are common to most of lxc commands.</p>
<dl>
<dt><code>-?, -h, &#8211;help</code></p>
<dd> Print a longer usage message than normal.</p>
<dt><code>&#8211;usage</code></p>
<dd> Give the usage message</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> mute on</p>
<dt><code>-P, &#8211;lxcpath=</code><i>PATH</i></p>
<dd> Use an alternate container path. The default is /var/lib/lxc.</p>
<dt><code>-o, &#8211;logfile=</code><i>FILE</i></p>
<dd> Output to an alternate log <i>FILE</i>. The default is no log.</p>
<dt><code>-l, &#8211;logpriority=</code><i>LEVEL</i></p>
<dd> Set log priority to <i>LEVEL</i>. The default log priority is ERROR. Possible values are : FATAL, CRIT, WARN, ERROR, NOTICE, INFO, DEBUG. </p>
<p> Note that this option is setting the priority of the events log in the alternate log file. It do not have effect on the ERROR events log on stderr.</p>
<dt><code>-n, &#8211;name=</code><i>NAME</i></p>
<dd> Use container identifier <i>NAME</i>. The container identifier format is an alphanumeric string.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version number.</dl>
<h2>DIAGNOSTIC</h2>
<dl>
<dt>The container already exists</p>
<dd> As the message mention it, you try to create a container but there is a container with the same name. You can use the <code>lxc-ls</code> command to list the available containers on the system.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-lxc/">lxc</a></code>(7), <code><a href="/docs/linux/man/1-lxc-create/">lxc-create</a></code>(1), <code><a href="/docs/linux/man/1-lxc-destroy/">lxc-destroy</a></code>(1), <code><a href="/docs/linux/man/1-lxc-start/">lxc-start</a></code>(1), <code><a href="/docs/linux/man/1-lxc-stop/">lxc-stop</a></code>(1), <code><a href="/docs/linux/man/1-lxc-execute/">lxc-execute</a></code>(1), <code><a href="/docs/linux/man/1-lxc-console/">lxc-console</a></code>(1), <code><a href="/docs/linux/man/1-lxc-monitor/">lxc-monitor</a></code>(1), <code><a href="/docs/linux/man/1-lxc-wait/">lxc-wait</a></code>(1), <code><a href="/docs/linux/man/1-lxc-cgroup/">lxc-cgroup</a></code>(1), <code><a href="/docs/linux/man/1-lxc-ls/">lxc-ls</a></code>(1), <code><a href="/docs/linux/man/1-lxc-info/">lxc-info</a></code>(1), <code><a href="/docs/linux/man/1-lxc-freeze/">lxc-freeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-unfreeze/">lxc-unfreeze</a></code>(1), <code><a href="/docs/linux/man/1-lxc-attach/">lxc-attach</a></code>(1), <code><a href="/docs/linux/man/5-lxc-conf/">lxc.conf</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Daniel Lezcano &lt;daniel.lezcano [at] free.fr&gt; </p>
<h2>Index</h2>
