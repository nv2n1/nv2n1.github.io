---
title: "rbd(8)"
name: "rbd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rbd/"
description: "rbd – manage rados block device (RBD) images"
---

<p>rbd &#8211; manage rados block device (RBD) images</p>
<h2>Synopsis</h2>
<pre><code>rbd</code> [ -c <i>ceph.conf</i> ] [ -m <i>monaddr</i> ] [ -p | --pool <i>pool</i> ] [
--size <i>size</i> ] [ --order <i>bits</i> ] [ <i>command</i> ... ]</pre>
<h2>Description</h2>
<p><code>rbd</code> is a utility for manipulating rados block device (RBD) images, used by the Linux rbd driver and the rbd storage driver for Qemu/KVM. RBD images are simple block devices that are striped over objects and stored in a RADOS object store. The size of the objects the image is striped over must be a power of two.</p>
<h2>Options</h2>
<dl>
<dt><code>-c ceph.conf, &#8211;conf ceph.conf</code></p>
<dd>Use ceph.conf configuration file instead of the default /etc/ceph/ceph.conf to determine monitor addresses during startup.</p>
<dt><code>-m monaddress[:port]</code></p>
<dd>Connect to specified monitor (instead of looking through ceph.conf).</p>
<dt><code>-p pool, &#8211;pool pool</code></p>
<dd>Interact with the given pool. Required by most commands.</p>
<dt><code>&#8211;no-progress</code></p>
<dd>Do not output progress information (goes to standard error by default for some commands).</dl>
<h2>Parameters</h2>
<dl>
<dt><code>&#8211;image-format format</code></p>
<dd>Specifies which object layout to use. The default is 1.</p>
<dt>&bull;</p>
<dd>format 1 &#8211; Use the original format for a new rbd image. This format is understood by all versions of librbd and the kernel rbd module, but does not support newer features like cloning.</p>
<dt>&bull;</p>
<dd>format 2 &#8211; Use the second rbd format, which is supported by librbd and kernel since version 3.11 (except for striping). This adds support for cloning and is more easily extensible to allow more features in the future.</p>
<dt><code>&#8211;size size-in-mb</code></p>
<dd>Specifies the size (in megabytes) of the new rbd image.</p>
<dt><code>&#8211;order bits</code></p>
<dd>Specifies the object size expressed as a number of bits, such that the object size is <code>1 &lt;&lt; order</code>. The default is 22 (4 MB).</p>
<dt><code>&#8211;stripe-unit size-in-bytes</code></p>
<dd>Specifies the stripe unit size in bytes. See striping section (below) for more details.</p>
<dt><code>&#8211;stripe-count num</code></p>
<dd>Specifies the number of objects to stripe over before looping back to the first object. See striping section (below) for more details.</p>
<dt><code>&#8211;snap snap</code></p>
<dd>Specifies the snapshot name for the specific operation.</p>
<dt><code>&#8211;id username</code></p>
<dd>Specifies the username (without the <code>client.</code> prefix) to use with the map command.</p>
<dt><code>&#8211;keyfile filename</code></p>
<dd>Specifies a file containing the secret to use with the map command. If not specified, <code>client.admin</code> will be used by default.</p>
<dt><code>&#8211;keyring filename</code></p>
<dd>Specifies a keyring file containing a secret for the specified user to use with the map command. If not specified, the default keyring locations will be searched.</p>
<dt><code>&#8211;shared tag</code></p>
<dd>Option for <i>lock add</i> that allows multiple clients to lock the same image if they use the same tag. The tag is an arbitrary string. This is useful for situations where an image must be open from more than one client at once, like during live migration of a virtual machine, or for use underneath a clustered filesystem.</p>
<dt><code>&#8211;format format</code></p>
<dd>Specifies output formatting (default: plain, json, xml)</p>
<dt><code>&#8211;pretty-format</code></p>
<dd>Make json or xml formatted output more human-readable.</p>
<dt><code>-o map-options, &#8211;options map-options</code></p>
<dd>Specifies which options to use when mapping an image. map-options is a comma-separated string of options (similar to <a href="/docs/linux/man/8-mount/">mount</a>(8) mount options). See map options section below for more details.</p>
<dt><code>&#8211;read-only</code></p>
<dd>Map the image read-only. Equivalent to -o ro.</p>
<dt><code>&#8211;image-features features</code></p>
<dd>Specifies which RBD format 2 features are to be enabled when creating an image. The numbers from the desired features below should be added to compute the parameter value: </p>
<p> +1: layering support +2: striping v2 support +4: exclusive locking support +8: object map support</p>
<dt><code>&#8211;image-shared</code></p>
<dd>Specifies that the image will be used concurrently by multiple clients. This will disable features that are dependent upon exclusive ownership of the image.</dl>
<h2>Commands</h2>
<dl>
<dt><code>ls</code> [-l | &#8211;long] [pool-name]</p>
<dd>Will list all rbd images listed in the rbd_directory object. With -l, also show snapshots, and use longer-format output including size, parent (if clone), format, etc.</p>
<dt><code>info</code> [<i>image-name</i>]</p>
<dd>Will dump information (such as size and order) about a specific rbd image. If image is a clone, information about its parent is also displayed. If a snapshot is specified, whether it is protected is shown as well.</p>
<dt><code>create</code> [<i>image-name</i>]</p>
<dd>Will create a new rbd image. You must also specify the size via &#8211;size. The &#8211;stripe-unit and &#8211;stripe-count arguments are optional, but must be used together.</p>
<dt><code>clone</code> [<i>parent-snapname</i>] [<i>image-name</i>]</p>
<dd>Will create a clone (copy-on-write child) of the parent snapshot. Object order will be identical to that of the parent image unless specified. Size will be the same as the parent snapshot. The &#8211;stripe-unit and &#8211;stripe-count arguments are optional, but must be used together. </p>
<p> The parent snapshot must be protected (see <i>rbd snap protect</i>). This requires image format 2.</p>
<dt><code>flatten</code> [<i>image-name</i>]</p>
<dd>If image is a clone, copy all shared blocks from the parent snapshot and make the child independent of the parent, severing the link between parent snap and child. The parent snapshot can be unprotected and deleted if it has no further dependent clones. </p>
<p> This requires image format 2.</p>
<dt><code>children</code> [<i>image-name</i>]</p>
<dd>List the clones of the image at the given snapshot. This checks every pool, and outputs the resulting poolname/imagename. </p>
<p> This requires image format 2.</p>
<dt><code>resize</code> [<i>image-name</i>] [&#8211;allow-shrink]</p>
<dd>Resizes rbd image. The size parameter also needs to be specified. The &#8211;allow-shrink option lets the size be reduced.</p>
<dt><code>rm</code> [<i>image-name</i>]</p>
<dd>Deletes an rbd image (including all data blocks). If the image has snapshots, this fails and nothing is deleted.</p>
<dt><code>export</code> [<i>image-name</i>] [<i>dest-path</i>]</p>
<dd>Exports image to dest path (use &#8211; for stdout).</p>
<dt><code>import</code> [<i>path</i>] [<i>dest-image</i>]</p>
<dd>Creates a new image and imports its data from path (use &#8211; for stdin). The import operation will try to create sparse rbd images if possible. For import from stdin, the sparsification unit is the data block size of the destination image (1 &lt;&lt; order). </p>
<p> The &#8211;stripe-unit and &#8211;stripe-count arguments are optional, but must be used together.</p>
<dt><code>export-diff</code> [<i>image-name</i>] [<i>dest-path</i>] [&#8211;from-snap <i>snapname</i>]</p>
<dd>Exports an incremental diff for an image to dest path (use &#8211; for stdout). If an initial snapshot is specified, only changes since that snapshot are included; otherwise, any regions of the image that contain data are included. The end snapshot is specified using the standard &#8211;snap option or @snap syntax (see below). The image diff format includes metadata about image size changes, and the start and end snapshots. It efficiently represents discarded or &#8216;zero&#8217; regions of the image.</p>
<dt><code>merge-diff</code> [<i>first-diff-path</i>] [<i>second-diff-path</i>] [<i>merged-diff-path</i>]</p>
<dd>Merge two continuous incremental diffs of an image into one single diff. The first diff&#8217;s end snapshot must be equal with the second diff&#8217;s start snapshot. The first diff could be &#8211; for stdin, and merged diff could be &#8211; for stdout, which enables multiple diff files to be merged using something like &#8216;rbd merge-diff first second &#8211; | rbd merge-diff &#8211; third result&#8217;. Note this command currently only support the source incremental diff with stripe_count == 1</p>
<dt><code>import-diff</code> [<i>src-path</i>] [<i>image-name</i>]</p>
<dd>Imports an incremental diff of an image and applies it to the current image. If the diff was generated relative to a start snapshot, we verify that snapshot already exists before continuing. If there was an end snapshot we verify it does not already exist before applying the changes, and create the snapshot when we are done.</p>
<dt><code>diff</code> [<i>image-name</i>] [&#8211;from-snap <i>snapname</i>]</p>
<dd>Dump a list of byte extents in the image that have changed since the specified start snapshot, or since the image was created. Each output line includes the starting offset (in bytes), the length of the region (in bytes), and either &#8216;zero&#8217; or &#8216;data&#8217; to indicate whether the region is known to be zeros or may contain other data.</p>
<dt><code>cp</code> [<i>src-image</i>] [<i>dest-image</i>]</p>
<dd>Copies the content of a src-image into the newly created dest-image. dest-image will have the same size, order, and image format as src-image.</p>
<dt><code>mv</code> [<i>src-image</i>] [<i>dest-image</i>]</p>
<dd>Renames an image. Note: rename across pools is not supported.</p>
<dt><code>snap</code> ls [<i>image-name</i>]</p>
<dd>Dumps the list of snapshots inside a specific image.</p>
<dt><code>snap</code> create [<i>image-name</i>]</p>
<dd>Creates a new snapshot. Requires the snapshot name parameter specified.</p>
<dt><code>snap</code> rollback [<i>image-name</i>]</p>
<dd>Rollback image content to snapshot. This will iterate through the entire blocks array and update the data head content to the snapshotted version.</p>
<dt><code>snap</code> rm [<i>image-name</i>]</p>
<dd>Removes the specified snapshot.</p>
<dt><code>snap</code> purge [<i>image-name</i>]</p>
<dd>Removes all snapshots from an image.</p>
<dt><code>snap</code> protect [<i>image-name</i>]</p>
<dd>Protect a snapshot from deletion, so that clones can be made of it (see <i>rbd clone</i>). Snapshots must be protected before clones are made; protection implies that there exist dependent cloned children that refer to this snapshot. <i>rbd clone</i> will fail on a nonprotected snapshot. </p>
<p> This requires image format 2.</p>
<dt><code>snap</code> unprotect [<i>image-name</i>]</p>
<dd>Unprotect a snapshot from deletion (undo <i>snap protect</i>). If cloned children remain, <i>snap unprotect</i> fails. (Note that clones may exist in different pools than the parent snapshot.) </p>
<p> This requires image format 2.</p>
<dt><code>map</code> [<i>image-name</i>] [-o | &#8211;options <i>map-options</i> ] [&#8211;read-only]</p>
<dd>Maps the specified image to a block device via the rbd kernel module.</p>
<dt><code>unmap</code> [<i>device-path</i>]</p>
<dd>Unmaps the block device that was mapped via the rbd kernel module.</p>
<dt><code>showmapped</code></p>
<dd>Show the rbd images that are mapped via the rbd kernel module.</p>
<dt><code>status</code> [<i>image-name</i>]</p>
<dd>Show the status of the image, including which clients have it open.</p>
<dt><code>lock</code> list [<i>image-name</i>]</p>
<dd>Show locks held on the image. The first column is the locker to use with the <i>lock remove</i> command.</p>
<dt><code>lock</code> add [<i>image-name</i>] [<i>lock-id</i>]</p>
<dd>Lock an image. The lock-id is an arbitrary name for the user&#8217;s convenience. By default, this is an exclusive lock, meaning it will fail if the image is already locked. The &#8211;shared option changes this behavior. Note that locking does not affect any operation other than adding a lock. It does not protect an image from being deleted.</p>
<dt><code>lock</code> remove [<i>image-name</i>] [<i>lock-id</i>] [<i>locker</i>]</p>
<dd>Release a lock on an image. The lock id and locker are as output by lock ls.</p>
<dt><code>bench-write</code> [<i>image-name</i>] &#8211;io-size [<i>io-size-in-bytes</i>] &#8211;io-threads [<i>num-ios-in-flight</i>] &#8211;io-total [<i>total-bytes-to-write</i>]</p>
<dd>Generate a series of sequential writes to the image and measure the write throughput and latency. Defaults are: &#8211;io-size 4096, &#8211;io-threads 16, &#8211;io-total 1GB</dl>
<h2>Image Name</h2>
<p>In addition to using the &#8211;pool and the &#8211;snap options, the image name can include both the pool name and the snapshot name. The image name format is as follows: </p>
<pre>[pool/]image-name[@snap]</pre>
<p>Thus an image name that contains a slash character (&#8216;/&#8217;) requires specifying the pool name explicitly.</p>
<h2>Striping</h2>
<p>RBD images are striped over many objects, which are then stored by the Ceph distributed object store (RADOS). As a result, read and write requests for the image are distributed across many nodes in the cluster, generally preventing any single node from becoming a bottleneck when individual images get large or busy. </p>
<p> The striping is controlled by three parameters:</p>
<dl>
<dt><code>order</code></p>
<dd>The size of objects we stripe over is a power of two, specifically 2^[<i>order</i>] bytes. The default is 22, or 4 MB.</p>
<dt><code>stripe_unit</code></p>
<dd>Each [<i>stripe_unit</i>] contiguous bytes are stored adjacently in the same object, before we move on to the next object.</p>
<dt><code>stripe_count</code></p>
<dd>After we write [<i>stripe_unit</i>] bytes to [<i>stripe_count</i>] objects, we loop back to the initial object and write another stripe, until the object reaches its maximum size (as specified by [<i>order</i>]. At that point, we move on to the next [<i>stripe_count</i>] objects. </p>
<p> By default, [<i>stripe_unit</i>] is the same as the object size and [<i>stripe_count</i>] is 1. Specifying a different [<i>stripe_unit</i>] requires that the STRIPINGV2 feature be supported (added in Ceph v0.53) and format 2 images be used.</dl>
<h2>Map Options</h2>
<p>Most of these options are useful mainly for debugging and benchmarking. The default values are set in the kernel and may therefore depend on the version of the running kernel.</p>
<dl>
<dt>&bull;</p>
<dd>fsid=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee &#8211; FSID that should be assumed by the client.</p>
<dt>&bull;</p>
<dd>ip=a.b.c.d[:p] &#8211; IP and, optionally, port the client should use.</p>
<dt>&bull;</p>
<dd>share &#8211; Enable sharing of client instances with other mappings (default).</p>
<dt>&bull;</p>
<dd>noshare &#8211; Disable sharing of client instances with other mappings.</p>
<dt>&bull;</p>
<dd>crc &#8211; Enable CRC32C checksumming for data writes (default).</p>
<dt>&bull;</p>
<dd>nocrc &#8211; Disable CRC32C checksumming for data writes.</p>
<dt>&bull;</p>
<dd>osdkeepalive=x &#8211; OSD keepalive timeout (default is 5 seconds).</p>
<dt>&bull;</p>
<dd>osd_idle_ttl=x &#8211; OSD idle TTL (default is 60 seconds).</p>
<dt>&bull;</p>
<dd>rw &#8211; Map the image read-write (default).</p>
<dt>&bull;</p>
<dd>ro &#8211; Map the image read-only. Equivalent to &#8211;read-only.</dl>
<h2>Examples</h2>
<p>To create a new rbd image that is 100 GB: </p>
<pre>rbd -p mypool create myimage --size 102400</pre>
<p>or alternatively: </p>
<pre>rbd create mypool/myimage --size 102400</pre>
<p>To use a non-default object size (8 MB): </p>
<pre>rbd create mypool/myimage --size 102400 --order 23</pre>
<p>To delete an rbd image (be careful!): </p>
<pre>rbd rm mypool/myimage</pre>
<p>To create a new snapshot: </p>
<pre>rbd snap create mypool/myimage [at] mysnap</pre>
<p>To create a copy-on-write clone of a protected snapshot: </p>
<pre>rbd clone mypool/myimage [at] mysnap otherpool/cloneimage</pre>
<p>To see which clones of a snapshot exist: </p>
<pre>rbd children mypool/myimage [at] mysnap</pre>
<p>To delete a snapshot: </p>
<pre>rbd snap rm mypool/myimage [at] mysnap</pre>
<p>To map an image via the kernel with cephx enabled: </p>
<pre>rbd map mypool/myimage --id admin --keyfile secretfile</pre>
<p>To unmap an image: </p>
<pre>rbd unmap /dev/rbd0</pre>
<p>To create an image and a clone from it: </p>
<pre>rbd import --image-format 2 image mypool/parent
rbd snap create --snap snapname mypool/parent
rbd snap protect mypool/parent [at] snap
rbd clone mypool/parent [at] snap otherpool/child</pre>
<p>To create an image with a smaller stripe_unit (to better distribute small writes in some workloads): </p>
<pre>rbd -p mypool create myimage --size 102400 --stripe-unit 65536 --stripe-count 16</pre>
<p>To change an image from one image format to another, export it and then import it as the desired image format: </p>
<pre>rbd export mypool/myimage [at] snap /tmp/img
rbd import --image-format 2 /tmp/img mypool/myimage2</pre>
<p>To lock an image for exclusive use: </p>
<pre>rbd lock add mypool/myimage mylockid</pre>
<p>To release a lock: </p>
<pre>rbd lock remove mypool/myimage mylockid client.2485</pre>
<h2>Availability</h2>
<p><code>rbd</code> is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to the Ceph documentation at <i><a rel="nofollow" href="http://ceph.com/docs">http://ceph.com/docs</a></i> for more information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ceph/">ceph</a></code>(8), <code><a href="/docs/linux/man/8-rados/">rados</a></code>(8)</p>
<h2>Copyright</h2>
<p>2010-2014, Inktank Storage, Inc. and contributors. Licensed under Creative Commons BY-SA</p>
