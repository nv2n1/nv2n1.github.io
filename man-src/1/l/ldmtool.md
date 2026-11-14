---
title: "ldmtool(1)"
name: "ldmtool"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldmtool/"
description: "ldmtool – A tool to manage Microsoft Windows dynamic disks"
---

<h2 class="name">NAME</h2>
<p> ldmtool &#8211; A tool to manage Microsoft Windows dynamic disks </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ldmtool</code> [options]</p>
<dt> <code>ldmtool</code> [options] scan [<i>device</i>&#8230;]</p>
<dt> <code>ldmtool</code> [options] show diskgroup {<i>disk group GUID</i>}</p>
<dt> <code>ldmtool</code> [options] show {volume | partition | disk} {<i>disk group GUID</i>} {<i>object name</i>}</p>
<dt> <code>ldmtool</code> [options] {create | remove} all</p>
<dt> <code>ldmtool</code> [options] {create | remove} volume {<i>disk group GUID</i>} {<i>volume name</i>}</dl>
<h2>OPTIONS</h2>
<p> <code>-d|&#8211;device</code> <i>device</i></p>
<dl>
<dt>
<dd>
<dd>Automatically scan <i>device</i>.</dl>
<h2>DESCRIPTION</h2>
<p> <code>ldmtool</code> is a tool for managing Microsoft Windows dynamic disks, which use Microsoft&#8217;s LDM metadata. It can inspect them, and also create and remove device-mapper block devices which can be mounted. </p>
<p> Although a filesystem can be mounted read-write and its contents modified, <code>ldmtool</code> is not able to modify the LDM metadata itself. That is, it cannot create, remove or edit dynamic disks. </p>
<p> It is also not able to mount RAID5 volumes which have a partition missing, although it can mount mirrored volumes with a partition missing. However, mounting a volume with a missing partition is not recommended, as ldmtool does not update the LDM metadata in any way. This means Windows will have no way to determine that the partitions are not synchronised when it subsequently mounted, which may result in corruption.</p>
<h2>INVOCATION</h2>
<p> <code>ldmtool</code> can be invoked either as a shell to run multiple actions, or to run a single action and return. If an action is given on the command line it will run in single action mode. If no action is given it will launch a shell.</p>
<h3>Shell mode</h3>
<p> When invoked as a shell, <code>ldmtool</code> will not scan any block devices by default. If any block devices are given on the command line with the <code>-d</code> option, these will be scanned. Otherwise, block devices must be scanned explicitly with the <code>scan</code> action. </p>
<p> Exit shell mode by sending an EOF, or with the quit or exit actions.</p>
<h3>Single action mode</h3>
<p> When invoked to run a single action all block devices will be scanned by default. In this case, if any block devices are specified with the <code>-d</code> option, only those block devices will be scanned.</p>
<h2>RESULTS</h2>
<p> <code>ldmtool</code> returns results as JSON-formatted data. The precise data returned is described in detail below. If a command fails it will not return any JSON data, but will instead display an error message. In shell mode, failure can be detected by the lack of a JSON-formatted result. In single action mode the caller can additionally check the exit code of the command.</p>
<h2>ACTIONS</h2>
<h3>scan [device&#8230;]</h3>
<p> Scan all [device]s for LDM metadata. </p>
<p> Returns a list of all known disk group GUIDs. Note that it doesn&#8217;t just return newly discovered disk groups.</p>
<h3>show diskgroup {<i>GUID</i>}</h3>
<p> Return detailed information about a single disk group. </p>
<p> <code>Returns:</code> </p>
<p> name</p>
<dl>
<dt>
<dd> The human-readable name of the disk group</dl>
<p> guid</p>
<dl>
<dt>
<dd> The Windows-assigned GUID of the disk group</dl>
<p> volumes</p>
<dl>
<dt>
<dd> A list of the names of all volumes in the disk group</dl>
<p> disks</p>
<dl>
<dt>
<dd> A list of the name of all disks in the disk group</dl>
<h3>show volume {<i>disk group GUID</i>} {<i>volume name</i>}</h3>
<p> Return detailed information about a volume. </p>
<p> <code>Returns:</code> </p>
<p> name</p>
<dl>
<dt>
<dd> The name of the volume</dl>
<p> type</p>
<dl>
<dt>
<dd> The volume type. One of: simple , spanned , striped , mirrored , raid5</dl>
<p> size</p>
<dl>
<dt>
<dd> The size of the volume in sectors</dl>
<p> chunk-size</p>
<dl>
<dt>
<dd> The chunk size, in sectors, used by striped and raid5 volumes. For other volume types it will be 0.</dl>
<p> hint</p>
<dl>
<dt>
<dd> The volume mounting hint. This value specifies how Windows expects the volume to be mounted. For a volume with an assigned drive letter, it might be &#8216;E:&#8217;.</dl>
<p> partitions</p>
<dl>
<dt>
<dd> A list of the names of the partitions which constitute this volume.</dl>
<h3>show partition {<i>disk group GUID</i>} {<i>partition name</i>}</h3>
<p> Return detailed information about a partition. </p>
<p> <code>Returns:</code> </p>
<p> name</p>
<dl>
<dt>
<dd> The name of the partition</dl>
<p> start</p>
<dl>
<dt>
<dd> The offset, in sectors, of the start of the partition from the beginning of the disk</dl>
<p> size</p>
<dl>
<dt>
<dd> The size of the partition in sectors</dl>
<p> disk</p>
<dl>
<dt>
<dd> The name of the disk the partition is on</dl>
<h3>show disk {<i>disk group GUID</i>} {<i>disk name</i>}</h3>
<p> Return detailed information about a disk. </p>
<p> <code>Returns:</code> </p>
<p> name</p>
<dl>
<dt>
<dd> The human-readable name of the disk</dl>
<p> guid</p>
<dl>
<dt>
<dd> The GUID of the disk</dl>
<p> present</p>
<dl>
<dt>
<dd> Whether the disk has been discovered during scanning: true or false</dl>
<p> <code>If the disk is present, additionally returns:</code> </p>
<p> device</p>
<dl>
<dt>
<dd> The name of the host device (e.g. /dev/sda)</dl>
<p> data-start</p>
<dl>
<dt>
<dd> The start sector of the data portion of the disk</dl>
<p> data-size</p>
<dl>
<dt>
<dd> The size, in sectors, of the data portion of the disk</dl>
<p> metadata-start</p>
<dl>
<dt>
<dd> The start sector of the metadata portion of the disk</dl>
<p> metadata-size</p>
<dl>
<dt>
<dd> The size, in sectors, of the metadata portion of the disk</dl>
<h3>create {volume&nbsp;{&nbsp;<i>disk group GUID</i>&nbsp;}&nbsp;{&nbsp;<i>volume name</i>&nbsp;} | all}</h3>
<p> Create a device-mapper device for either the specified volume or all volumes in all detected disk groups. </p>
<p> Returns a list of the device-mapper device names which were created by this action. Note that if a device already existed for a volume it will not be returned in this list.</p>
<h3>remove {volume&nbsp;{&nbsp;<i>disk group GUID</i>&nbsp;}&nbsp;{&nbsp;<i>volume name</i>&nbsp;} | all}</h3>
<p> Remove device-mapper devices for either the specified volume or all volumes in all detected disk groups. </p>
<p> Returns a list of the device-mapper device names which were removed by this action. Note that if no device existed for a volume it will not be returned in this list.</p>
<h2>EXAMPLES</h2>
<p> The following examples form a sequence from a single session of ldmtool running in shell mode. </p>
<p> Scan all loop devices for LDM metadata: </p>
<dl>
<dt>
<dd>
<pre><code>
ldm &gt; scan / dev / loop[0 - 9] *
          [
              "03c0c4fc-8b6f-402b-9431-4be2e5823b1c",
              "06495a84-fbfd-11e1-8cf9-52540061f5db"
          ]
</code></pre>
</dl>
<p> Two disk groups were detected. The list contains their GUIDs. </p>
<p> Show detailed information about one of the disk groups: </p>
<dl>
<dt>
<dd>
ldm &gt; show diskgroup 06495a84 &#8211; fbfd &#8211; 11e1 &#8211; 8cf9 &#8211; 52540061f5db<br />
{<br />
    &#8220;name&#8221; : &#8220;WIN-ERRDJSBDAVF-Dg0&#8221;,<br />
             &#8220;guid&#8221; : &#8220;06495a84-fbfd-11e1-8cf9-52540061f5db&#8221;,<br />
                      &#8220;volumes&#8221; : [<br />
                          &#8220;Volume4&#8221;,<br />
                          &#8220;Volume1&#8221;,<br />
                          &#8220;Volume2&#8221;,<br />
                          &#8220;Volume3&#8221;,<br />
                          &#8220;Volume5&#8221;<br />
                      ],<br />
                                  &#8220;disks&#8221; : [<br />
                                      &#8220;Disk1&#8221;,<br />
                                      &#8220;Disk2&#8221;,<br />
                                      &#8220;Disk3&#8221;,<br />
                                      &#8220;Disk4&#8221;,<br />
                                      &#8220;Disk5&#8221;,<br />
                                      &#8220;Disk6&#8221;,<br />
                                      &#8220;Disk7&#8221;,<br />
                                      &#8220;Disk8&#8221;,<br />
                                      &#8220;Disk9&#8221;<br />
                                  ]<br />
}
</dl>
<p> Show detailed information about one of the volumes in the disk group: </p>
<dl>
<dt>
<dd>
<pre><code>
ldm &gt; show volume 06495a84 - fbfd - 11e1 - 8cf9 - 52540061f5db Volume1
{
    "name" : "Volume1",
             "type" : "spanned",
                      "size" : 129024,
                      "chunk-size" : 0,
                      "hint" : "E:",
                               "partitions" : [
                                   "Disk1-01",
                                   "Disk2-01"
                               ]
}
</code></pre>
</dl>
<p> Show detailed information about one of the partitions in the volume: </p>
<dl>
<dt>
<dd>
<pre>
ldm&gt; show partition 06495a84-fbfd-11e1-8cf9-52540061f5db Disk1-01
{
  &quot;name&quot; : &quot;Disk1-01&quot;,
  &quot;start&quot; : 65,
  &quot;size&quot; : 96256,
  &quot;disk&quot; : &quot;Disk1&quot;
}
    
</pre>
</dl>
<p> Show detailed information about the disk containing the partition: </p>
<dl>
<dt>
<dd>
<pre>
ldm&gt; show disk 06495a84-fbfd-11e1-8cf9-52540061f5db Disk1
{
  &quot;name&quot; : &quot;Disk1&quot;,
  &quot;guid&quot; : &quot;06495a85-fbfd-11e1-8cf9-52540061f5db&quot;,
  &quot;present&quot; : true,
  &quot;device&quot; : &quot;/dev/loop15&quot;,
  &quot;data-start&quot; : 63,
  &quot;data-size&quot; : 100289,
  &quot;metadata-start&quot; : 100352,
  &quot;metadata-size&quot; : 2048
}
    
</pre>
</dl>
<p> Create a device-mapper device for a volume: </p>
<dl>
<dt>
<dd>
<pre>
ldm&gt; create volume 06495a84-fbfd-11e1-8cf9-52540061f5db Volume1
[
  &quot;ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume1&quot;
]
    
</pre>
</dl>
<p> A new device-mapper device has been created, called ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume1. Depending on how udev is configured, it will probably now be available as /dev/mapper/ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume1. </p>
<p> Create device-mapper devices for all volumes in both disk groups: </p>
<dl>
<dt>
<dd>
<pre>
ldm&gt; create all
[
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Volume2&quot;,
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Volume1&quot;,
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Volume4&quot;,
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Stripe1&quot;,
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Raid1&quot;,
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Volume3&quot;,
  &quot;ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume4&quot;,
  &quot;ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume2&quot;,
  &quot;ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume3&quot;,
  &quot;ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume5&quot;
]
    
</pre>
</dl>
<p> Note that ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume1 is not in the list of devices which were created as it already existed. </p>
<p> Remove the device-mapper device for a single volume: </p>
<dl>
<dt>
<dd>
<pre>
ldm&gt; remove volume 06495a84-fbfd-11e1-8cf9-52540061f5db Volume2
[
  &quot;ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume2&quot;
]
    
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
ldm&gt; remove all
[
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Volume2&quot;,
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Volume1&quot;,
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Volume4&quot;,
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Stripe1&quot;,
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Raid1&quot;,
  &quot;ldm_vol_Red-nzv8x6obywgDg0_Volume3&quot;,
  &quot;ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume4&quot;,
  &quot;ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume1&quot;,
  &quot;ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume3&quot;,
  &quot;ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume5&quot;
]
    
</pre>
</dl>
<p> Note that ldm_vol_WIN-ERRDJSBDAVF-Dg0_Volume2 is not in the list of devices which were removed, as it was removed previously.</p>
<h2>AUTHOR</h2>
<p> <code>Matthew Booth</code> &lt;mbooth [at] redhat.com&gt;</p>
<dl>
<dt>
<dd></dl>
<h2>Index</h2>
<dt><a href="#lbAR">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAS">AUTHOR</a></p>
<dd></dl>
