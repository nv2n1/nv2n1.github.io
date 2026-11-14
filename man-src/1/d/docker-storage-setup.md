---
title: "docker-storage-setup(1)"
name: "docker-storage-setup"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-storage-setup/"
description: "docker-storage-setup – Grows the root filesystem and sets up storage for docker."
---

<h2>NAME</h2>
<p> docker-storage-setup &#8211; Grows the root filesystem and sets up storage for docker.</p>
<h2>SYNOPSIS</h2>
<p> docker-storage-setup [OPTIONS]</p>
<h2>OPTIONS</h2>
<p> &#8211;help<br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> &#8211;reset<br />
&nbsp;<wbr>&nbsp;<wbr>Reset your docker storage to init state. Reset does not try to remove volume groups or try to remove any of the disks added previously.<br />
&nbsp;<wbr>&nbsp;<wbr> Note: The &#8211;reset command is not sufficient to cleanup your docker environment. This option is used by other tools. (atomic storage reset) </p>
<h2>EXAMPLES</h2>
<p> Run docker-storage-setup after setting up your configuration in /etc/sysconfig/docker-storage-setup. One can look at /usr/lib/docker-storage-setup/docker-storage-setup for various options and their default settings. Anything user wants to change, should be changed in /etc/sysconfig/docker-storage-setup. This is the file which will override any settings specified in /usr/lib/docker-storage-setup/docker-storage-setup. </p>
<p> lvm2 version should be same or higher than lvm2-2.02.112 for lvm thin pool functionality to work properly. </p>
<p> Supported options for the configuration file: </p>
<p> STORAGE_DRIVER:<br />
Specify a storage driver to be used with docker. Default<br />
driver is&nbsp;<wbr>&quot;devicemapper&quot;. Other valid values are overlay,<br />
overlay2 and&nbsp;<wbr>&quot;&quot;. Empty string tells docker-storage-setup to<br />
not do any storage setup. </p>
<p> EXTRA_DOCKER_STORAGE_OPTIONS:<br />
A set of extra options that should be passed to the Docker<br />
daemon. </p>
<p> DEVS: A quoted, space-separated list of devices to be used.<br />
If a drive is partitioned and contains a&nbsp;<wbr>${dev}1 partition,<br />
that partition will be configured for use. Unpartitioned<br />
drives will be partitioned and configured for use. If&nbsp;<wbr>&quot;VG&quot;<br />
is not specified, then use of the root disk&#8217;s extra space<br />
is implied. </p>
<p> VG: The volume group to use for docker storage. Defaults to the<br />
volume group where the root filesystem resides.&nbsp;<wbr>&nbsp;<wbr>If VG is<br />
specified and the volume group does not exist, it will be<br />
created&nbsp;<wbr>(which requires that&nbsp;<wbr>&quot;DEVS&quot;&nbsp;<wbr>be nonempty, since we don&#8217;t<br />
currently support putting a second partition on the root disk). </p>
<p>lvm2 version should be same or higher than lvm2-2.02.112 for lvm<br />
thin pool functionality to work properly. </p>
<p> GROWPART:<br />
One can use this option to enable/disable growing of partition<br />
table backing root volume group. This is intended for<br />
virtualization and cloud installations. By default it is<br />
disabled. Use GROWPART=true to enable automatic partition<br />
table resizing. </p>
<p> AUTO_EXTEND_POOL:<br />
Enable automatic extension of pool by lvm. lvm can monitor<br />
the pool and automatically extend it when pool is getting full. </p>
<p> POOL_AUTOEXTEND_THRESHOLD:<br />
Determines the pool extension threshold in terms of percentage<br />
of pool size. For example, if threshold is 60, that means when<br />
pool is 60%&nbsp;<wbr>full, threshold has been hit. </p>
<p> POOL_AUTOEXTEND_PERCENT:<br />
Determines the amount by which pool needs to be grown. This is<br />
specified in terms of&nbsp;<wbr>%&nbsp;<wbr>of pool size. So a value of 20 means<br />
that when threshold is hit, pool will be grown by 20%&nbsp;<wbr>of existing<br />
pool size. </p>
<p> CHUNK_SIZE:<br />
Controls the chunk size/block size of thin pool. Value of CHUNK_SIZE<br />
be suitable to be passed to &#8211;chunk-size option of lvconvert. </p>
<p> DEVICE_WAIT_TIMEOUT:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Specifies a device wait timeout value in seconds. In<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>certain cases required devices might not be immediately<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>available and docker-storage-setup might decide to wait for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>it. This timeout specifies how long one should wait for the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>device. Default is 60 seconds. One can disable the wait by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specifying a value of 0. </p>
<p> WIPE_SIGNATURES:<br />
Wipe any signatures found on disk. Valid values are<br />
true/false and default value is false. By default if any<br />
signatures are found on disk operation is aborted. If this value<br />
is set to true, then signatures will either be wiped or<br />
overwritten as suitable. This also means that if there is any<br />
data on disk, it will be lost. </p>
<p> DOCKER_ROOT_VOLUME:<br />
By default no new volume and filesystem will be setup<br />
for docker root dir. Docker creates&nbsp;<wbr>/var/lib/docker/&nbsp;<wbr>on<br />
top of underlying filesystem for storing images and containers. </p>
<p>To carve out a separate logical volume for storing docker<br />
images/containers/volumes data, set DOCKER_ROOT_VOLUME=yes<br />
NOTE: devicemapper stores images/containers on thin pool. </p>
<p>docker-storage-setup creates a logical volume with an XFS<br />
filesystem mounted on docker root directory<br />
(default:&nbsp;<wbr>/var/lib/docker). </p>
<p> DOCKER_ROOT_VOLUME_SIZE:<br />
Specify the desired size for docker root volume. It defaults<br />
to 40%&nbsp;<wbr>of all free space. </p>
<p>DOCKER_ROOT_VOLUME_SIZE can take values acceptable to<br />
&quot;lvcreate -L&quot;&nbsp;<wbr>as well as some values acceptable to to&nbsp;<wbr><br />
&quot;lvcreate -l&quot;. If user intends to pass values acceptable&nbsp;<wbr><br />
to&nbsp;<wbr>&quot;lvcreate -l&quot;, then only those values which contains&nbsp;<wbr>&quot;%&quot;&nbsp;<wbr><br />
in syntax are acceptable.&nbsp;<wbr>&nbsp;<wbr>If value does not contain&nbsp;<wbr>&quot;%&quot;&nbsp;<wbr>it&nbsp;<wbr><br />
is assumed value is suitable for&nbsp;<wbr>&quot;lvcreate -L&quot;. </p>
<p>NOTE: If both STORAGE_DRIVER=devicemapper and&nbsp;<wbr><br />
DOCKER_ROOT_VOLUME=yes is set, docker-storage-setup would set<br />
up the thin pool for devicemapper first, followed by docker&nbsp;<wbr><br />
root volume. e.g if free space in the volume group is 10G,&nbsp;<wbr><br />
devicemapper thin pool size would be 4G&nbsp;<wbr>(40%&nbsp;<wbr>of 10G)&nbsp;<wbr>and docker<br />
root volume would be 2.4G&nbsp;<wbr>(40%&nbsp;<wbr>of 6G). </p>
<p> The options below should be specified as values acceptable to &#8216;lvextend -L&#8217;: </p>
<p> ROOT_SIZE: The size to which the root filesystem should be grown. </p>
<p> DATA_SIZE: The desired size for the docker data LV. Defaults to using<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>40%&nbsp;<wbr>free space in the VG after the root LV and docker<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>metadata LV have been allocated/grown. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>DATA_SIZE can take values acceptable to&nbsp;<wbr>&quot;lvcreate -L&quot;&nbsp;<wbr>as<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>well as some values acceptable to&nbsp;<wbr>&quot;lvcreate -l&quot;. If user<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>intends to pass values acceptable to&nbsp;<wbr>&quot;lvcreate -l&quot;, then<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only those values which contains&nbsp;<wbr>&quot;%&quot;&nbsp;<wbr>in syntax are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>acceptable.&nbsp;<wbr>&nbsp;<wbr>If value does not contain&nbsp;<wbr>&quot;%&quot;&nbsp;<wbr>it is assumed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>value is suitable for&nbsp;<wbr>&quot;lvcreate -L&quot;. </p>
<p> MIN_DATA_SIZE:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Specifies the minimum size of the data volume. If sufficient<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>free space is not available, the pool creation will fail. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Value should be a number followed by a optional suffix.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;bBsSkKmMgGtTpPeE&quot;&nbsp;<wbr>are valid suffixes. If no suffix is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specified then value will be considered as megabyte unit. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Both upper and lower case suffix represent same unit of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>size. Use suffix B for Bytes, S for sectors as 512 bytes, K<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>for kibibytes&nbsp;<wbr>(1024 bytes), M for mebibytes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(1024 kibibytes), G for gibibytes, T for tebibytes, P for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>pebibytes and E for exbibytes. </p>
<p> Sample </p>
<p> A simple, sample /etc/sysconfig/docker-storage-setup: </p>
<p> DEVS=/dev/vdb </p>
<p> DATA_SIZE=8GB </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-atomic/">atomic</a></code>(1) </p>
<h2>HISTORY</h2>
<p> November 2014, originally compiled by Joe Brockmeier &lt;jzb [at] redhat.com&gt; based on comments in Andy Grimm&#8217;s &lt;agrimm [at] redhat.com&gt; script.</p>
<h2>AUTHORS</h2>
<p> Joe Brockmeier Andy Grimm </p>
<h2>Index</h2>
