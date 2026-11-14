---
title: "imgbase(8)"
name: "imgbase"
section: "8"
letter: "i"
url: "/docs/linux/man/8-imgbase/"
description: "imgbase – tool to manage writeable filesystems on read-only base images"
---

<p>imgbase &#8211; tool to manage writeable filesystems on read-only base images</p>
<h2>Synopsis</h2>
<p><code>imgbase</code> [<i>OPTION&#8230;</i>] [<i>&lt;COMMAND&gt;</i> [<i>OPTION&#8230;</i>]]</p>
<h2>Description</h2>
<p>imgbase provides a specific management method to derive writeable filesystem layers from read-only base images. It also takes care that the layer which shall be used can be selected at boot time.</p>
<dl>
<dd><font SIZE="+1"> <code>Warning</code> </font><br />
 imgbase is a WIP. That means this manpage is probably out of date and data loss can happen.  This works by using LVM thinpools and thin volumens, combined if a filesystem which supports the TRIM commant (i..e ext4 when it&#8217;s used with the discard mount option). The creation of this layout is described under the section called &#8220;USAGE&#8221;. imgbase needs a volume group, which is then populated with one or more base images (which are read-only thin volumes in a thinpool). For each of this base image one or more write-able layers can be added.</p>
<h2>Usage</h2>
<h3>Creating the layout</h3>
<p>imgbase makes assumptions about the existing LVM layout, if you start from scratch you can use imgbase to create the layout: </p>
<dl>
<dd>
<pre># imgbase layout --init --size 10G /dev/sdb /dev/sdc</pre>
</dl>
<p> This command will create the deafult volume group (HostVG) with a thinpool which is 10G in size, laying on /dev/sdb and /dev/sdc.</p>
<h3>Adding a base</h3>
<p>Once a valid layout was created you can add a base image using the following command: </p>
<dl>
<dd>
<pre># imgbase base --add --size 1G rootfs.img</pre>
</dl>
<p> This will create a new base image. It will create a 1G sized thin volume and populate it with the rootfs.img. The rootfs.img must be smaller than the given size. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The base image name is derived from a pre-defined naming scheme. </p>
</dl>
<h3>Adding a layer</h3>
<p>Once a base image exists you can add a layer by running: </p>
<dl>
<dd>
<pre># imgbase layer --add</pre>
</dl>
<p> This will add a new layer for the latest existing base image. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The layer name is also derived from a pre-defined naming scheme. </p>
</dl>
<h3>Inspection at runtime</h3>
<p>A summary over all base images and their layers can be determined by running: </p>
<dl>
<dd>
<pre># imgbase layout</pre>
</dl>
<p> To get the remaining free space in the used thinpool run: </p>
<dl>
<dd>
<pre># imgbase layout --free-space</pre>
</dl>
<h3>Upgrade to new image</h3>
<dl>
<dd>
<pre># imgbase update --format liveimg FILENAME</pre>
</dl>
<p> Example: </p>
<dl>
<dd>
<pre># imgbase update ovirt-node-ng-4.0.0-0.999.master.20160329.0.el7.squashfs.img</pre>
</dl>
<p> To verify a new base image was added: </p>
<dl>
<dd>
<pre># imgbase layout
ovirt-node-ng-4.0.0-0
 └╼ ovirt-node-ng-4.0.0-0+1
ovirt-node-ng-4.0.0-0.3.master.20160330132038.el7
 └╼ ovirt-node-ng-4.0.0-0.3.master.20160330132038.el7+1</pre>
</dl>
<p> To load the new image: </p>
<dl>
<dd>
<pre># reboot</pre>
</dl>
<p> To verify you are in the new image (after reboot): </p>
<dl>
<dd>
<pre># imgbase w
[INFO] You are on ovirt-node-ng-4.0.0-0+1</pre>
</dl>
<h3>Rollback to previous image</h3>
<p>If you have updated and would like to return to a previous version. The rollback operation will set the bootloader to an earlier version. This defaults to rolling back one update. If you would like to return to a specific version, use &#8211;to. </p>
<p> &#8212; </p>
<p> Example 1: </p>
<p> The example below has two layers: ovirt-node-ng-4.0.0+1, and ovirt-node-ng-4.0.0-20160413.0+1. ovirt-node-ng-4.0.0-20160413.0+1 is the active layer, as shown below. </p>
<p> # imgbase layout ovirt-node-ng-4.0.0-0 └╼ ovirt-node-ng-4.0.0-0+1 ovirt-node-ng-4.0.0-0.20160413.0 └╼ ovirt-node-ng-4.0.0-0.20160413.0+1 </p>
<p> # imgbase w [INFO] You are on ovirt-node-ng-4.0.0-0.20160413.0+1 </p>
<p> imgbase rollback with no arguments will revert to the previous version. In this case, ovirt-node-ng-4.0.0.0+1 </p>
<p> # imgbase rollback </p>
<p> Example 2: rollback to a specific version. </p>
<p> # imgbase rollback &#8211;to ovirt-node-ng-4.0.0-0+1 </p>
<p> After the rollback operation, a reboot is required. # reboot &#8212; </p>
<p> To verify you are in the new image (after reboot): </p>
<dl>
<dd>
<pre># imgbase w
[INFO] You are on ovirt-node-ng-4.0.0-0.3.master.20160330132038.el7+1</pre>
</dl>
<h2>Options</h2>
<p><code>&#8211;debug</code></p>
<dl>
<dd>Output debug informations</dl>
<p> <code>&#8211;dry</code></p>
<dl>
<dd>Do <i>not</i> run the commands, just output what would be run.</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Combine this with <code>&#8211;debug</code> to see the commands This does not work with all commands. </p>
</dl>
<p> Example: </p>
<dl>
<dd>
<pre># imgbase --dry --debug layout --init --size 1G /dev/sda
...
DEBUG:imgbase:Calling: (['vgcreate', 'HostVG', &lt;open file '/dev/sda', mode 'r'
at 0x22bf420&gt;],) {}
DEBUG:imgbase:Calling: (['lvcreate', '--size', '1G', '--thin',
'HostVG/ImagePool'],) {}</pre>
</dl>
<p> <code>&#8211;vg=</code><i>VG</i></p>
<dl>
<dd>By default the volume group HostVG is used. Use this argument to use the volume group name <i>VG</i> instead.</dl>
<p> <code>&#8211;thinpool=</code><i>THINPOOL</i></p>
<dl>
<dd>By default the thinpool ImagePool is used. Use this argument to use the thinpool name <i>THINPOOL</i> instead.</dl>
<p> <code>&#8211;layerformat=</code><i>FMT</i></p>
<dl>
<dd>By default the format Base-%d.%d is used to create and discover existing logical volumes. Use this argument to use the format <i>FMT</i> instead.</dl>
<h2>Availability</h2>
<p>The imgbase command is part of the imgbased package and is available from m[blue]<code><a rel="nofollow" href="https://github.com/fabiand/imgbased/">https://github.com/fabiand/imgbased/</a></code>m[]</p>
<h2>Authors</h2>
<p>Fabian Deutsch</p>
