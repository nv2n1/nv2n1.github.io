---
title: "atomic-storage(1)"
name: "atomic-storage"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-storage/"
description: "atomic-storage – Manage container storage."
---

<h2 class="name">NAME</h2>
<p> atomic-storage &#8211; Manage container storage. </p>
<h2>SYNOPSIS</h2>
<p> <code>atomic storage COMMAND [OPTIONS]</code> </p>
<p> atomic storage allows the user to easily manage container storage. You can reset your container environment back to its initial state as well as migrate all images, volumes, and containers from one version of atomic to another. With this command, users can quickly save all their data from the current atomic instance, change the container&#8217;s content storage backend, and then import all their old data to the new system. </p>
<h2>COMMANDS</h2>
<p> <code>export</code> </p>
<p> export command will export all the current images, volumes, and containers to the specified directory (/var/lib/atomic/migrate by default), in the /images, /volumes, /containers subdirectories. </p>
<p> <code>import</code> </p>
<p> import command will import images, volumes, and containers from the specified directory (/var/lib/atomic/migrate by default) into the new atomic instance. </p>
<p> <code>reset</code><br />
&nbsp;<wbr>Remove all containers/images from your system </p>
<p> <code>modify</code><br />
&nbsp;<wbr>Modify the default storage setup </p>
<h2>export OPTIONS</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>&#8211;graph</code> Root of the docker runtime. If you are running docker at the default location (/var/lib/docker), you don&#8217;t need to pass this flag. However if you are running docker at a custom location. This flag must be set. </p>
<p> <code>&#8211;dir</code> Directory in which to temporarily store the files (can be an existing directory, or the command will create one). If no directory is specified, /var/lib/atomic/migrate would be used as default. </p>
<h2>Note:</h2>
<p> Atomic &#8211;assumeyes option can be used </p>
<p> [<code>-y|&#8211;assumeyes</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>Delete image(s)&nbsp;<wbr>without conformation from the user </p>
<h2>import OPTIONS</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>&#8211;graph</code> Root of the docker runtime. If you are running docker at the default location (/var/lib/docker), you don&#8217;t need to pass this flag. However if you are running docker at a custom location. This flag must be set. </p>
<p> <code>&#8211;dir</code> Directory from which to import the files (images, containers and volumes). If this flag is not set atomic storage will assume the import location to be /var/lib/atomic/migrate. Whether you set this flag or use the default, the directory must be present for the import to happen successfully. </p>
<h2>modify OPTIONS</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>&#8211;add-device</code> Add block devices to storage pool. This command will expand your devicemapper storage pool by adding the block device. Only works with devicemapper driver. </p>
<p> <code>&#8211;remove-device</code> Remove block devices from the storage pool. If a device is not empty, this command will try to first move its data to some other device in the pool. </p>
<p> <code>&#8211;remove-unused-devices</code> Remove all block devices from the storage pool that are currently unused. </p>
<p> <code>&#8211;driver</code> Backend storage driver for containers. This options the storage driver. Drivers supported: devicemapper, overlay, overlay2 </p>
<p> <code>&#8211;vgroup</code> The name of the volume group for the storage pool. </p>
<h2>reset OPTIONS</h2>
<p> <code>-h</code> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>&#8211;graph</code> Root of the docker runtime. atomic will search for either /var/lib/docker or /var/lib/docker-latest, if only one exists, atomic will select it as the default. If both exists or you are running docker with a graph storage at a non default location, you need to pass this flag. </p>
<h2>HISTORY</h2>
<p> October 2015, Originally compiled by Shishir Mahajan (shishir dot mahajan at redhat dot com) </p>
<h2>Index</h2>
