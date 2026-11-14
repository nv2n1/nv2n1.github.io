---
title: "lsmcli(1)"
name: "lsmcli"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsmcli/"
description: "lsmcli – libStorageMgmt command line interface"
---

<h2>NAME</h2>
<p> lsmcli &#8211; libStorageMgmt command line interface </p>
<h2>SYNOPSIS</h2>
<p> <code>lsmcli </code><i>command</i> [<i>GLOBAL OPTIONS</i>]&#8230;[<i>COMMAND OPTIONS</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> lsmcli is the command line tool for the libStorageMgmt library. This tool allows users to do one off storage related management operations or to script management of their storage. </p>
<h2>PREREQUISITES</h2>
<dl>
<dt>* libStorageMgmt daemon.</p>
<dd> The daemon &#8216;<code>lsmd</code>&#8216; is required by lsmcli.</p>
<dt>* URI(Uniform Resource Identifier)</p>
<dd> URI is used to identify which plugin to use and how the plugin should communicate with the storage array. The valid URI format is:</p>
<dl>
<dt>
<dd>
<pre>
<code>plugin://&lt;username&gt;@host:&lt;port&gt;?&lt;query_string_parameters&gt;</code>
<br>
<code>plugin+ssl://&lt;username&gt;@host:&lt;port&gt;?&lt;query_string_parameters&gt;</code>
</pre>
</dl>
<dl>
<dt>
<dd> Examples, please refer to &quot;LibStorageMgmt User Guide&quot; for more details:</dl>
<dl>
<dt>
<dd> * Simulator:</p>
<dl>
<dt>
<dd> <code>sim://</code><br />
 <code>simc://</code></dl>
<dl>
<dt>
<dd> * NetApp ONTAP:</p>
<dl>
<dt>
<dd> <code><a href="ontap://username@host">ontap://username@host</a></code><br />
 <code>ontap+<a href="ssl://username@host">ssl://username@host</a></code></dl>
<dl>
<dt>
<dd> * SMI-S supported arrays (eg. EMC CX/VNX, HDS AMS, IBM SVC/DS, LSI MegaRAID and others):</p>
<dl>
<dt>
<dd> <code><a href="smis://username@host:">smis://username@host:</a>&lt;port&gt;?namespace=&lt;namespace&gt;</code><br />
 <code>smis+<a href="ssl://username@host:">ssl://username@host:</a>&lt;port&gt;?namespace=&lt;namespace&gt;</code></dl>
<dl>
<dt>
<dd> You can pass URI to lsmcli via one of these methods:</p>
<dl>
<dt>
<dd> * Using &#8216;<code>-u</code>, <code>&#8211;uri</code>&#8216; argument.<br />
 * Using &#8216;<code>LSMCLI_URI</code>&#8216; environment variable.<br />
 * Add this line into <code>$HOME/.lsmcli</code>:</p>
<dl>
<dt>
<dd> uri=<i>&lt;URI&gt;</i></dl>
<dl>
<dt>* Password</p>
<dd> For storage array password authentication you can pass it to lsmcli via one of the following methods:</p>
<dl>
<dt>
<dd> * &#8216;<code>-P</code>, <code>&#8211;prompt</code>&#8216; argument to prompt for password.<br />
 * &#8216;<code>LSMCLI_PASSWORD</code>&#8216; environment variable.</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>GLOBAL OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show this help message and exit. Will show help message of specific command if specified.</p>
<dt><code>-u</code> <i>&lt;URI&gt;</i>, <code>&#8211;uri</code> <i>&lt;URI&gt;</i></p>
<dd> Uniform Resource Identifier (env LSMCLI_URI)</p>
<dt><code>-P</code>, <code>&#8211;prompt</code></p>
<dd> Prompt for password (env LSMCLI_PASSWORD)</p>
<dt><code>-H</code>, <code>&#8211;human</code></p>
<dd> Print sizes in human readable format (e.g., KiB, MiB, GiB, TiB, PiB, EiB)</p>
<dt><code>-t</code> <i>&lt;SEP&gt;</i>, <code>&#8211;terse</code> <i>&lt;SEP&gt;</i></p>
<dd> Print output in terse form with &quot;SEP&quot; as a record separator without header unless &#8216;&#8211;header&#8217; defined.</p>
<dt><code>&#8211;header</code></p>
<dd> Include the header with terse</p>
<dt><code>-e</code>, <code>&#8211;enum</code></p>
<dd> Display enumerated types as numbers instead of text</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Bypass confirmation prompt for data loss operations</p>
<dt><code>-w</code> <i>&lt;WAIT&gt;</i>, <code>&#8211;wait</code>=<i>&lt;WAIT&gt;</i></p>
<dd> Command timeout value in ms (default = 30s)</p>
<dt><code>-b</code></p>
<dd> Run the command asynchronously instead of waiting for completion. The lsmcli command will exit with exit <a href="/docs/linux/man/7-code/">code</a>(7) and job id will be written to STDOUT when a command is still executing on the storage array. Use &#8216;job-status &#8211;id <i>&lt;job id&gt;</i>&#8216; to inquire on the progress of the command. Some arrays or plugins might not support asynchronous operations, in those circumstances, -b will be ineffective. Command will wait until finished.</p>
<dt><code>-s</code>, <code>&#8211;script</code></p>
<dd> Displaying data in script friendly way.<br />
 Without this option, data is displayed in this manner (default): </p>
<p>&nbsp;<wbr>ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| Name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| Element Type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>aggr0&nbsp;<wbr>&nbsp;<wbr>| aggr0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| FS,SYSTEM_RESERVED,POOL&nbsp;<wbr>&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>iscsi&nbsp;<wbr>&nbsp;<wbr>| iscsi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| FS,POOL&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8230; </p>
<p> With this option, data is displayed in this manner. </p>
<p>&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| aggr0<br />
&nbsp;<wbr>Name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| aggr0<br />
&nbsp;<wbr>Element Type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| FS,SYSTEM_RESERVED,POOL<br />
&nbsp;<wbr>&#8230;<br />
&nbsp;<wbr>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
&nbsp;<wbr>ID&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| iscsi<br />
&nbsp;<wbr>Name&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| iscsi<br />
&nbsp;<wbr>Element Type&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| FS,POOL<br />
&nbsp;<wbr>&#8230; </p>
<p> Please note:<br />
 To reduce the width of output, NOT all properties will be displayed in default column display. </p>
</dl>
<h2>COMMANDS</h2>
<h3>list</h3>
<p> List information on LSM objects</p>
<dl>
<dt><code>&#8211;type</code> <i>&lt;TYPE&gt;</i></p>
<dd> Required. Valid values are (case insensitive):<br />
 <code>VOLUMES</code>, <code>POOLS</code>, <code>FS</code>, <code>SNAPSHOTS</code>, <code>EXPORTS</code>, <code>NFS_CLIENT_AUTH</code>,<br />
 <code>ACCESS_GROUPS</code>, <code>SYSTEMS</code>, <code>DISKS</code>, <code>PLUGINS</code>, <code>TARGET_PORTS</code>, <code>BATTERIES</code>. </p>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Required for <code>&#8211;type</code>=<code>SNAPSHOTS</code>. List the snapshots of certain filesystem. PLUGINS will list all supported plugins of LSM, not only the current one.</p>
<dt><code>&#8211;sys</code> <i>&lt;SYS_ID&gt;</i></p>
<dd> Search resources from system with SYS_ID. Only supported when querying these types of resources: <code>VOLUMES</code>, <code>POOLS</code>, <code>FS</code>, <code>SNAPSHOTS</code>, <code>DISKS</code>, <code>ACCESS_GROUPS</code>.</p>
<dt><code>&#8211;pool</code> <i>&lt;POOL_ID&gt;</i></p>
<dd> Search resources from pool with POOL_ID. Only supported by these types of resources: <code>VOLUMES</code>, <code>POOLS</code>, <code>FS</code>.</p>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Search resources from volume with VOL_ID. Only supported by these types of resources: <code>VOLUMES</code>, <code>ACCESS_GROUPS</code>.<br />
 To query volume masking status, please use this command:<br />
lsmcli list &#8211;type ACCESS_GROUPS &#8211;vol&nbsp;<wbr>&lt;VOL_ID&gt;</p>
<dt><code>&#8211;disk</code> <i>&lt;DISK_ID&gt;</i></p>
<dd> Search resources from disk with DISK_ID. Only supported by these types of resources: <code>DISK</code>.</p>
<dt><code>&#8211;ag</code> <i>&lt;AG_ID&gt;</i></p>
<dd> Search resources from access group with AG_ID. Only supported by these types of resources: <code>ACCESS_GROUPS</code>, <code>VOLUMES</code>.<br />
 To query volume masking status, please use this command:<br />
lsmcli list &#8211;type VOLUMES &#8211;ag&nbsp;<wbr>&lt;AG_ID&gt;</p>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Search resources from file system with FS_ID. Only supported by these types of resources: <code>FS</code>.</p>
<dt><code>&#8211;nfs-export</code> <i>&lt;NFS_EXPORT_ID&gt;</i></p>
<dd> Search resources from NFS export with NFS_EXPORT_ID. Only supported by these types of resources: <code>EXPORTS</code>.</p>
<dt><code>&#8211;tgt</code> <i>&lt;TGT_ID&gt;</i></p>
<dd> Search resources from target port with target port ID. Only supported by these types of resources: <code>TARGET_PORTS</code>. </p>
</dl>
<h3>job-status</h3>
<p> Retrieve information about a job. Please see user guide on how to use.</p>
<dl>
<dt><code>&#8211;job</code> <i>&lt;JOB_ID&gt;</i></p>
<dd>
</dl>
<h3>capabilities</h3>
<p> Retrieves array capabilities.</p>
<dl>
<dt><code>&#8211;sys</code> <i>&lt;SYS_ID&gt;</i></p>
<dd> Required. ID of the system to query for capabilities. </p>
</dl>
<h3>plugin-info</h3>
<p> Retrieves plugin description and version for current URI. </p>
<h3>volume-create</h3>
<p> Creates a volume (AKA., logical volume, virtual disk, LUN).</p>
<dl>
<dt><code>&#8211;name</code> <i>&lt;NAME&gt;</i></p>
<dd> Required. Volume name.</p>
<dt><code>&#8211;size</code> <i>&lt;SIZE&gt;</i></p>
<dd> Required. Volume size (See <code>SIZE OPTION</code> for allowed formats).</p>
<dt><code>&#8211;pool</code> <i>&lt;POOL_ID&gt;</i></p>
<dd> Required. ID of pool.</p>
<dt><code>&#8211;provisioning</code> <i>&lt;THINP_TYPE&gt;</i></p>
<dd> Optional. Provisioning type. Valid values are: DEFAULT, THIN, FULL. <code>DEFAULT</code> means let plugin choose. <code>THIN</code> means requiring a Thin Provisioning enabled volume. <code>FULL</code> means requiring a fully allocated volume. </p>
</dl>
<h3>volume-raid-create</h3>
<p> Creates a volume on hardware RAID on given disks.</p>
<dl>
<dt><code>&#8211;name</code> <i>&lt;NAME&gt;</i></p>
<dd> Required. Volume name. Might be altered or ignored due to hardware RAID card vendor limitation.</p>
<dt><code>&#8211;raid-type</code> <i>&lt;RAID_TYPE&gt;</i></p>
<dd> Required. Could be one of these values: <code>RAID0</code>, <code>RAID1</code>, <code>RAID5</code>, <code>RAID6</code>, <code>RAID10</code>, <code>RAID50</code>, <code>RAID60</code>. The supported RAID types of current RAID card could be queried via command &quot;<code>volume-raid-create-cap</code>&quot;.</p>
<dt><code>&#8211;disk</code> <i>&lt;DISK_ID&gt;</i></p>
<dd> Required. Repeatable. The disk ID for new RAID group.</p>
<dt><code>&#8211;strip-size</code> <i>&lt;STRIP_SIZE&gt;</i></p>
<dd> Optional. The size in bytes of strip on each disks. If not defined, will let hardware card to use the vendor default value. The supported stripe size of current RAID card could be queried via command &quot;<code>volume-raid-create-cap</code>&quot;. </p>
</dl>
<h3>volume-raid-create-cap</h3>
<p> Query support status of volume-raid-create command for current hardware RAID card.</p>
<dl>
<dt><code>&#8211;sys</code> <i>&lt;SYS_ID&gt;</i></p>
<dd> Required. ID of the system to query for capabilities. </p>
</dl>
<h3>volume-ident-led-on</h3>
<p> Enable the IDENT LEDs for all physical disks that compose a logical volume.</p>
<dl>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. ID of the volume being targeted. </p>
</dl>
<h3>volume-ident-led-off</h3>
<p> Disable the IDENT LEDs for all physical disks that compose a logical volume.</p>
<dl>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. ID of the volume being targeted. </p>
</dl>
<h3>volume-delete</h3>
<dl>
<dt>Delete a volume given its ID</p>
<dd>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. The ID of volume to delete. </p>
</dl>
<h3>volume-resize</h3>
<dl>
<dt>Re-sizes a volume, requires:</p>
<dd>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. The ID of volume to resize.</p>
<dt><code>&#8211;size</code> <i>&lt;NEW_SIZE&gt;</i></p>
<dd> Required. The new size of volume.(See <code>SIZE OPTION</code> for allowed formats). Due to boundary alignment concern, array might return a volume with slightly bigger size than requested. </p>
</dl>
<h3>volume-replicate</h3>
<p> Creates a new volume and replicates provided volume to it.</p>
<dl>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. The ID of volume to replicate.</p>
<dt><code>&#8211;name</code> <i>&lt;NAME&gt;</i></p>
<dd> Required. The name for new volume to hold replicated data.</p>
<dt><code>&#8211;rep-type</code> <i>&lt;REPL_TYPE&gt;</i> (see <code>VOLUME REPLICATION TYPES)</code></p>
<dd> Required. Valid types of replication are:<br />
 <code>CLONE</code>, <code>COPY</code>, <code>MIRROR_ASYNC</code>, <code>MIRROR_SYNC</code>.</p>
<dt><code>&#8211;pool</code> <i>&lt;POOL_ID&gt;</i></p>
<dd> Optional. The ID of pool where the new volume should be created from. If not specified, plugin or array will choose appropriate pool. </p>
</dl>
<h3>volume-replicate-range</h3>
<p> Replicates a portion of a volume to the same volume or to a different volume.</p>
<dl>
<dt><code>&#8211;src-vol</code> <i>&lt;SRC_VOL_ID&gt;</i></p>
<dd> Required. The ID of replication source volume.</p>
<dt><code>&#8211;dst-vol</code> <i>&lt;DST_VOL_ID&gt;</i></p>
<dd> Required. The ID of replication destination volume.</p>
<dt><code>&#8211;rep-type</code> <i>&lt;REPL_TYPE&gt;</i> (see <code>VOLUME REPLICATION TYPES)</code></p>
<dd> Required. Appropriate types of replication are:<br />
 <code>CLONE</code>, <code>COPY</code>.</p>
<dt><code>&#8211;src-start</code> <i>&lt;SRC_START_BLK&gt;</i></p>
<dd> Required. Replication source volume start block number. Must in pair with <code>&#8211;count</code> and <code>&#8211;dst-start</code>. If you have several non-continuous block ranges, you can define repeatly define this arugument, like &#8216;<code>&#8211;src-start 0 &#8211;dst-start 0 &#8211;count 1024 &#8211;src-start 2048 &#8211;dst-start 2048 &#8211;count 2048</code>&#8216;</p>
<dt><code>&#8211;dst-start</code> <i>&lt;DST_START_BLK&gt;</i></p>
<dd> Required. Replication destination volume start block number. Must in pair with <code>&#8211;count</code> and <code>&#8211;src-start</code>.</p>
<dt><code>&#8211;count</code> <i>&lt;BLK_COUNT&gt;</i></p>
<dd> Required. The count of replicated block startting from <code>&#8211;src-startR block. Must in pair with &#8211;src-start</code> and <code>&#8211;dst-start</code>. </p>
</dl>
<h3>volume-replicate-range-block-size</h3>
<p> Size of each replicated block on a system in bytes.</p>
<dl>
<dt><code>&#8211;sys</code> <i>&lt;SYS_ID&gt;</i></p>
<dd> Required. ID of the system to query for replicated block size. </p>
</dl>
<h3>volume-dependants</h3>
<p> Returns True if volume has a dependant child, like replication.</p>
<dl>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. The ID of volume to query dependency. </p>
</dl>
<h3>volume-dependants-rm</h3>
<p> Removes volume dependencies(like replication).</p>
<dl>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. The ID of volume to remove dependency. </p>
</dl>
<h3>volume-access-group</h3>
<p> Lists the access group(s) that have access to the provided volume.</p>
<dl>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. The ID of volume to query access. </p>
</dl>
<h3>volume-mask</h3>
<dl>
<dt>Grant access group RW access to certain volume. Like LUN masking</p>
<dd> or NFS export.</p>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. The ID of volume to access.</p>
<dt><code>&#8211;ag</code> <i>&lt;AG_ID&gt;</i></p>
<dd> Required. The ID of access group to grant. </p>
</dl>
<h3>volume-unmask</h3>
<dl>
<dt>Revoke access group RW access to specified volume.</p>
<dd>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. The ID of volume to revoke.</p>
<dt><code>&#8211;ag</code> <i>&lt;AG_ID&gt;</i></p>
<dd> Required. The ID of access group to revoke. </p>
</dl>
<h3>volume-raid-info</h3>
<dl>
<dt>Query RAID information for given volume.</p>
<dd>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. The ID of volume to query. </p>
</dl>
<h3>pool-member-info</h3>
<dl>
<dt>Query RAID information for given pool.</p>
<dd>
<dt><code>&#8211;pool</code> <i>&lt;POOL_ID&gt;</i></p>
<dd> Required. The ID of pool to query. </p>
</dl>
<h3>access-group-create</h3>
<dl>
<dt>Create an access group.</p>
<dd>
<dt><code>&#8211;name</code> <i>&lt;AG_NAME&gt;</i></p>
<dd> Required. The human friendly name for new access group.</p>
<dt><code>&#8211;init</code> <i>&lt;INIT_ID&gt;</i></p>
<dd> Required. The first initiator ID of new access group. WWPN or iSCSI IQN.</p>
<dt><code>&#8211;sys</code> <i>&lt;SYS_ID&gt;</i></p>
<dd> Required. The ID of system where this access group should reside on. </p>
</dl>
<h3>access-group-add</h3>
<p> Adds an initiator to an access group.</p>
<dl>
<dt><code>&#8211;ag</code> <i>&lt;AG_ID&gt;</i></p>
<dd> Required. ID of access group.</p>
<dt><code>&#8211;init</code> <i>&lt;INIT_ID&gt;</i></p>
<dd> Required. ID of initiator to add. WWPN or iSCSI IQN. </p>
</dl>
<h3>access-group-remove</h3>
<p> Removes an initiator from an access group.</p>
<dl>
<dt><code>&#8211;ag</code> <i>&lt;AG_ID&gt;</i></p>
<dd> Required. ID of access group.</p>
<dt><code>&#8211;init</code> <i>&lt;INIT_ID&gt;</i></p>
<dd> Required. ID of initiator to remove. </p>
</dl>
<h3>access-group-delete</h3>
<p> Delete an access group.</p>
<dl>
<dt><code>&#8211;ag</code> <i>&lt;AG_ID&gt;</i></p>
<dd> Required. ID of access group to delete. </p>
</dl>
<h3>access-group-volumes</h3>
<p> Lists the volumes that the access group has been granted access to.</p>
<dl>
<dt><code>&#8211;ag</code> <i>&lt;AG_ID&gt;</i></p>
<dd> Required. The ID of access group to query. </p>
</dl>
<h3>iscsi-chap</h3>
<p> Configures ISCSI inbound/outbound CHAP authentication.</p>
<dl>
<dt><code>&#8211;init</code> <i>&lt;INIT_ID&gt;</i></p>
<dd> Required. The ID of iSCSI initiator to configure.</p>
<dt><code>&#8211;in-user</code> <i>&lt;IN_USER&gt;</i></p>
<dd> Optional. Inbound CHAP user name.</p>
<dt><code>&#8211;in-pass</code> <i>&lt;IN_PASS&gt;</i></p>
<dd> Optional. Inbound CHAP password.</p>
<dt><code>&#8211;out-user</code> <i>&lt;OUT_USER&gt;</i></p>
<dd> Optional. Outbound CHAP user name.</p>
<dt><code>&#8211;out-pass</code> <i>&lt;OUT_PASS&gt;</i></p>
<dd> Optional. Outbound CHAP password. </p>
</dl>
<h3>fs-create</h3>
<p> Creates a filesystem.</p>
<dl>
<dt><code>&#8211;name</code> <i>&lt;NAME&gt;</i></p>
<dd> Required. Human friendly name for new filesystem.</p>
<dt><code>&#8211;size</code> <i>&lt;SIZE&gt;</i></p>
<dd> Required. Volume size(See <code>SIZE OPTION</code> for allowed formats).</p>
<dt><code>&#8211;pool</code> <i>&lt;POOL_ID&gt;</i></p>
<dd> Required. ID of pool to hold the new filesystem. </p>
</dl>
<h3>fs-delete</h3>
<p> Delete a filesystem.</p>
<dl>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Required. ID of the filesystem to delete. </p>
</dl>
<h3>fs-resize</h3>
<p> Resizes a filesystem.</p>
<dl>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Required. ID of the filesystem to resize.</p>
<dt><code>&#8211;size</code> <i>&lt;NEW_SIZE&gt;</i></p>
<dd> Required. New size of filesystem. See <code>SIZE OPTION</code> for allowed formats. </p>
</dl>
<h3>fs-export</h3>
<p> Export a filesystem via NFS.</p>
<dl>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Required. ID of the filesystem to export.</p>
<dt><code>&#8211;exportpath</code> <i>&lt;EXPORT_PATH&gt;</i></p>
<dd> Optional. NFS server export path. e.g. &#8216;/foo/bar&#8217;.</p>
<dt><code>&#8211;anonuid</code> <i>&lt;ANONY_UID&gt;</i></p>
<dd> Optional. The UID(User ID) to map to anonymous user.</p>
<dt><code>&#8211;anongid</code> <i>&lt;ANONY_GID&gt;</i></p>
<dd> Optional. The GID(Group ID) to map to anonymous user.</p>
<dt><code>&#8211;auth-type</code> <i>&lt;AUTH_TYPE&gt;</i></p>
<dd> Optional. NFS client authentication type. This is just a place holder, not supported yet.</p>
<dt><code>&#8211;root-host</code> <i>&lt;ROOT_HOST&gt;</i></p>
<dd> Optional. Repeatable. The host/IP has root access. For two or more hosts/IPs: <code> &#8211;root-host hostA &#8211;root-host hostB</code>&#8216;.</p>
<dt><code>&#8211;ro-host</code> <i>&lt;RO_HOST&gt;</i></p>
<dd> Optional. Repeatable. The host/IP has read only access. For two or more hosts/IPs: &#8216;<code>&#8211;ro-host hostA &#8211;ro-host hostB</code>&#8216;.</p>
<dt><code>&#8211;rw-host</code> <i>&lt;RW_HOST&gt;</i></p>
<dd> Optional. The host/IP has read/write access. For two or more hosts/IPs: <code> &#8211;rw-host hostA &#8211;rw-host hostB</code>&#8216;. </p>
</dl>
<h3>fs-unexport</h3>
<p> Remove an NFS export.</p>
<dl>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Required. ID of the filesystem to unexport. </p>
</dl>
<h3>fs-clone</h3>
<p> Creates a file system clone. The &#8216;clone&#8217; means point in time read writeable space efficient copy of data, AKA. read-writable snapshot.</p>
<dl>
<dt><code>&#8211;src-fs</code> <i>&lt;SRC_FS_ID&gt;</i></p>
<dd> Required. The ID of the filesystem to clone.</p>
<dt><code>&#8211;dst-name</code> <i>&lt;DST_FS_NAME&gt;</i></p>
<dd> Required. The name for newly created destination file system.</p>
<dt><code>&#8211;backing-snapshot</code> <i>&lt;BE_SS_ID&gt;</i></p>
<dd> Optional. Make a FS clone using a previously created snapshot. </p>
</dl>
<h3>fs-snap-create</h3>
<p> Creates a snapshot of specified filesystem. A snapshot is defined as a read only space efficient point in time copy (PIT) of a filesystem. The source filesystem remains modifiable.</p>
<dl>
<dt><code>&#8211;name</code> <i>&lt;SNAP_NAME&gt;</i></p>
<dd> Required. The human friendly name of new snapshot.</p>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Required. The ID of filesystem to create snapshot against. </p>
</dl>
<h3>fs-snap-delete</h3>
<p> Deletes a snapshot.</p>
<dl>
<dt><code>&#8211;snap</code> <i>&lt;SNAP_ID&gt;</i></p>
<dd> Required. The ID of snapshot to delete.</p>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Required. The ID of filesystem. </p>
</dl>
<h3>fs-snap-restore</h3>
<p> Restores a FS or specified files to previous snapshot state. This will discard all the changes to filesystem since snapshot if specific files are not specified in restore.</p>
<dl>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Required. The ID of filesystem to restore.</p>
<dt><code>&#8211;snap</code> <i>&lt;SNAP_ID&gt;</i></p>
<dd> Required. The ID of snapshot to restore.</p>
<dt><code>&#8211;file</code> <i>&lt;FILE_PATH&gt;</i></p>
<dd> Optional. Repeatable. With this option defined, will only restore the defined file(s). <code> &#8211;file fileA &#8211;file pathB</code>&#8216;.</p>
<dt><code>&#8211;fileas</code> <i>&lt;NEW_FILE_PATH&gt;</i></p>
<dd> Optional. Repeatable. With this option defined, the restored file will be saved to specified path and filename, eg. &#8216;<code>&#8211;file fileA &#8211;fileas old_fileA </code>&#8216;. </p>
</dl>
<h3>fs-dependants</h3>
<p> Returns True if a child dependency (snapshot or clone) exists.</p>
<dl>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Required. The ID of filesystem to query.</p>
<dt><code>&#8211;file</code> <i>&lt;FILE_PATH&gt;</i></p>
<dd> Optional. Repeatable. Only check for dependencies on specific file(s), eg. &#8216;<code>&#8211;file fileA &#8211;file pathB</code>&#8216;. </p>
</dl>
<h3>fs-dependants-rm</h3>
<p> Removes filesystem dependencies(snapshot or clone).</p>
<dl>
<dt><code>&#8211;fs</code> <i>&lt;FS_ID&gt;</i></p>
<dd> Required. The ID of filesystem to remove dependency.</p>
<dt><code>&#8211;file</code> <i>&lt;FILE_PATH&gt;</i></p>
<dd> Optional. Repeatable. Only remove dependencies on specific file(s), eg. &#8216;<code>&#8211;file fileA &#8211;file pathB</code>&#8216;. </p>
</dl>
<h3>file-clone</h3>
<p> Creates a clone of a file (thin provisioned). Note: &#8211;src and &#8211;dst need to be paired<br />
&nbsp;<wbr>eg.&nbsp;<wbr>&#8216;<code>&#8211;src fileA &#8211;src fileB &#8211;dst fileA_clone &#8211;dst fileB_clone</code>&#8216;.</p>
<dl>
<dt><code>&#8211;src</code> <i>&lt;SRC_FILE_PATH&gt;</i></p>
<dd> Required. Repeatable. Source file to clone (relative path).</p>
<dt><code>&#8211;dst</code> <i>&lt;DST_FILE_PATH&gt;</i></p>
<dd> Required. Repeatable. Destination file for clone (relative path). </p>
</dl>
<h3>system-read-cache-pct-update</h3>
<p> Change the read cache percentage for a system.</p>
<dl>
<dt><code>&#8211;sys</code> <i>&lt;SYS_ID&gt;</i></p>
<dd> Required. ID of the system being targeted.</p>
<dt><code>&#8211;read-pct</code> <i>&lt;READ_PCT&gt;</i></p>
<dd> The desired percentage of read cache for the targeted system. Write cache will be automatically changed to the remaining percentage available after updating the read cache (if supported by the system). </p>
</dl>
<h3>local-disk-list</h3>
<p> List all disks found on current local operating system. Require permission to open /dev/sdX as read-only, normally root user or disk group would have sufficient permission. </p>
<h3>volume-cache-info</h3>
<p> Query RAM cache information for the desired volume.</p>
<dl>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. ID of the volume to query cache information. </p>
</dl>
<h3>volume-phy-disk-cache-update</h3>
<p> Disable or enable RAM physical disk cache of certain volume.</p>
<dl>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. ID of the volume to change.</p>
<dt><code>&#8211;policy</code> <i>&lt;POLICY&gt;</i></p>
<dd> Required. <code>Enable</code> or <code>Disable</code>. </p>
</dl>
<h3>volume-read-cache-policy-update</h3>
<p> Disable or enable RAM read cache of certain volume.</p>
<dl>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. ID of the volume to change.</p>
<dt><code>&#8211;policy</code> <i>&lt;POLICY&gt;</i></p>
<dd> Required. <code>Enable</code> or <code>Disable</code>. </p>
</dl>
<h3>volume-write-cache-policy-update</h3>
<p> Change volume write cache policy.</p>
<dl>
<dt><code>&#8211;vol</code> <i>&lt;VOL_ID&gt;</i></p>
<dd> Required. ID of the volume to change.</p>
<dt><code>&#8211;policy</code> <i>&lt;POLICY&gt;</i></p>
<dd> Required. <code>WB</code> for write back mode, <code>WT</code> for write through mode, <code>AUTO</code> for auto mode which use <code>WB</code> mode when any battery is OK and use <code>WT</code> mode else. </p>
</dl>
<h3>local-disk-ident-led-on</h3>
<p> Turn on the identification LED for specified disk path. Require permission to open disk path as read-write, normally root user or disk group would have sufficient permission.</p>
<dl>
<dt><code>&#8211;path</code> <i>&lt;DISK_PATH&gt;</i></p>
<dd> Required. Disk path, like <code>/dev/sdb</code>. </p>
</dl>
<h3>local-disk-ident-led-off</h3>
<p> Turn off the identification LED for specified disk path. Require permission to open disk path as read-write, normally root user or disk group would have sufficient permission.</p>
<dl>
<dt><code>&#8211;path</code> <i>&lt;DISK_PATH&gt;</i></p>
<dd> Required. Disk path, like <code>/dev/sdb</code>. </p>
</dl>
<h3>local-disk-fault-led-on</h3>
<p> Turn on the fault LED for specified disk path. Require permission to open disk path as read-write, normally root user or disk group would have sufficient permission.</p>
<dl>
<dt><code>&#8211;path</code> <i>&lt;DISK_PATH&gt;</i></p>
<dd> Required. Disk path, like <code>/dev/sdb</code>. </p>
</dl>
<h3>local-disk-fault-led-off</h3>
<p> Turn off the fault LED for specified disk path. Require permission to open disk path as read-write, normally root user or disk group would have sufficient permission.</p>
<dl>
<dt><code>&#8211;path</code> <i>&lt;DISK_PATH&gt;</i></p>
<dd> Required. Disk path, like <code>/dev/sdb</code>. </p>
<dt>
<dd></dl>
<h2>ALIAS</h2>
<h3>ls</h3>
<p> Alias of &#8216;list &#8211;type systems&#8217;</p>
<h3>lp</h3>
<p> Alias of &#8216;list &#8211;type pools&#8217;</p>
<h3>lv</h3>
<p> Alias of &#8216;list &#8211;type volumes&#8217;</p>
<h3>ld</h3>
<p> Alias of &#8216;list &#8211;type disks&#8217;</p>
<h3>la</h3>
<p> Alias of &#8216;list &#8211;type access_groups&#8217;</p>
<h3>lf</h3>
<p> Alias of &#8216;list &#8211;type fs&#8217;</p>
<h3>lt</h3>
<p> Alias of &#8216;list &#8211;type target_ports&#8217;</p>
<h3>lb</h3>
<p> Alias of &#8216;list &#8211;type batteries&#8217;</p>
<h3>c</h3>
<p>&nbsp;<wbr>Alias of&nbsp;<wbr>&#8216;capabilities&#8217;</p>
<h3>p</h3>
<p>&nbsp;<wbr>Alias of&nbsp;<wbr>&#8216;plugin-info&#8217;</p>
<h3>vc</h3>
<p> Alias of &#8216;volume-create&#8217;</p>
<h3>vrc</h3>
<p> Alias of &#8216;volume-raid-create&#8217;</p>
<h3>vrcc</h3>
<p> Alias of &#8216;volume-raid-create-cap&#8217;</p>
<h3>vilon</h3>
<p> Alias of &#8216;volume-ident-led-on&#8217;</p>
<h3>viloff</h3>
<p> Alias of &#8216;volume-ident-led-off&#8217;</p>
<h3>vd</h3>
<p> Alias of &#8216;volume-delete&#8217;</p>
<h3>vr</h3>
<p> Alias of &#8216;volume-resize&#8217;</p>
<h3>vm</h3>
<p> Alias of &#8216;volume-mask&#8217;</p>
<h3>vu</h3>
<p> Alias of &#8216;volume-unmask&#8217;</p>
<h3>vri</h3>
<p> Alias of &#8216;volume-raid-info&#8217;</p>
<h3>pmi</h3>
<p> Alias of &#8216;pool-member-info&#8217;</p>
<h3>ac</h3>
<p> Alias of &#8216;access-group-create&#8217;</p>
<h3>aa</h3>
<p> Alias of &#8216;access-group-add&#8217;</p>
<h3>ar</h3>
<p> Alias of &#8216;access-group-remove&#8217;</p>
<h3>ad</h3>
<p> Alias of &#8216;access-group-delete&#8217;</p>
<h3>srcps</h3>
<p> Alias of &#8216;system-read-cache-pct-update&#8217;</p>
<h3>ldl</h3>
<p> Alias of &#8216;local-disk-list&#8217;</p>
<h3>vci</h3>
<p> Alias of &#8216;volume-cache-info&#8217;</p>
<h3>vpdcu</h3>
<p> Alias of &#8216;volume-phy-disk-cache-update&#8217;</p>
<h3>vrcpu</h3>
<p> Alias of &#8216;volume-read-cache-policy-update&#8217;</p>
<h3>vwcpu</h3>
<p> Alias of &#8216;volume-write-cache-policy-update&#8217;</p>
<h3>ldilon</h3>
<p> Alias of &#8216;local-disk-ident-led-on&#8217;</p>
<h3>ldiloff</h3>
<p> Alias of &#8216;local-disk-ident-led-off&#8217;</p>
<h3>ldflon</h3>
<p> Alias of &#8216;local-disk-fault-led-on&#8217;</p>
<h3>ldfloff</h3>
<p> Alias of &#8216;local-disk-fault-led-off&#8217; </p>
<dl>
<dt>
<dd></dl>
<h2>SIZE OPTION</h2>
<h3><code>&#8211;size</code> <i>&lt;SIZE&gt;</i></h3>
<p> Storage space size. Format is &#8216;<i>&lt;number&gt;</i>&#8216; + &#8216;<i>&lt;prefix&gt;</i>&#8216;. Example: &quot;10GiB&quot;, &quot;20.5MB&quot;. No postfix indicates bytes. Valid prefixes are:<br />
&nbsp;<wbr>KiB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>2^10 Bytes<br />
&nbsp;<wbr>MiB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>2^20 Bytes<br />
&nbsp;<wbr>GiB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>2^30 Bytes<br />
&nbsp;<wbr>TiB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>2^40 Bytes<br />
&nbsp;<wbr>PiB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>2^50 Bytes<br />
&nbsp;<wbr>EiB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>2^60 Bytes<br />
&nbsp;<wbr>KB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>10^3 Bytes<br />
&nbsp;<wbr>MB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>10^6 Bytes<br />
&nbsp;<wbr>GB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>10^9 Bytes<br />
&nbsp;<wbr>TB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>10^12 Bytes<br />
&nbsp;<wbr>PB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>10^15 Bytes<br />
&nbsp;<wbr>EB,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>10^17 Bytes </p>
<p> These prefixes are supported also, but not recommended:<br />
&nbsp;<wbr>K, M, G, T, P, E,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>equal to KiB, MiB, and etc<br />
&nbsp;<wbr>k, m, g, t, p, e,&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>equal to KiB, MiB, and etc </p>
<h2>FILES</h2>
<dl>
<dt>~/.lsmcli</p>
<dd> lsmcli configuration file, containing name-value pairs separated by &#8216;=&#8217;. The only currently supported configuration option is &#8216;uri&#8217;, such as &#8216;uri=<a href="ontap://user@filer.example.com'.">ontap://user@filer.example.com&#8217;.</a> </p>
<p> Configuration options in .lsmcli are only used if not overridden by command-line option or environment variable. </p>
</dl>
<h2>EXAMPLES (command output omitted for brevity)</h2>
<dl>
<dt>Simulator, list pools (no password required)</p>
<dd> $ lsmcli -u sim:// -l POOLS</p>
<dt>NetApp, list volumes (prompting for password)</p>
<dd> $ lsmcli -u <a href="ontap://root@host/">ontap://root@host/</a> -l VOLUMES -P</p>
<dt>SMI-S, list systems (prompting for password)</p>
<dd>
<pre>
$ lsmcli -u <a href="smispy://username@host:5988/?namespace=root/interop">smispy://username@host:5988/?namespace=root/interop</a> \
        -l SYSTEMS -P
</pre>
<dt>Targetd, list pools (using env variables for URI and password)</p>
<dd> $ export LSMCLI_URI=targetd://username [at] host:18700<br />
 $ export LSMCLI_PASSWORD=<i>&lt;password&gt;</i><br />
 $ lsmcli -l POOLS</p>
<dt>NexentaStor, create volume (using environment variables for URI and password)</p>
<dd>
<pre>
$ export LSMCLI_URI='<a href="nstor://user@host'">nstor://user@host'</a>
$ export LSMCLI_PASSWORD=<i>&lt;password&gt;</i>
$ lsmcli volume-create --name volume_name --size 1TiB --pool default
</pre>
<dt>SMI-S, create volume (using environment variables for URI and password)</p>
<dd>
<pre>
$ export LSMCLI_URI='smispy+<a href="ssl://user@host:5989?namespace=root/emc'">ssl://user@host:5989?namespace=root/emc'</a>
$ export LSMCLI_PASSWORD=<i>&lt;password&gt;</i>
$ lsmcli volume-create --name volume_name --size 1TiB --pool default
</pre>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>LSMCLI_URI</p>
<dd> The URI for the storage array in question.</p>
<dt>LSMCLI_PASSWORD</p>
<dd> The password to use for the array. </p>
</dl>
<h2>VOLUME REPLICATION TYPES</h2>
<dl>
<dt>CLONE</p>
<dd> A point in time, read writeable, space efficent copy of data.</p>
<dt>COPY</p>
<dd> A full bitwise copy of the data. It occupies the full space.</p>
<dt>MIRROR_SYNC</p>
<dd> Continously updated, realtime with both copies having identical data.</p>
<dt>MIRROR_ASYNC</p>
<dd> Continously updated, with a varying amount of delay and data delta between the source and target. </p>
</dl>
<h2>NOTES</h2>
<dl>
<dt>Plugin installation</p>
<dd> Plugins are installed individually except for the simulators which are always included. </p>
<dt>Secure sockets layer (SSL)</p>
<dd> All of the plugins (except the simulator) support SSL when communicating from the plugin to the array. This is accomplished by adding &quot;+ssl&quot; to the plugin and usually by selecting a different port number from non-SSL communications. </p>
<pre>
$ lsmcli -u smispy+<a href="ssl://username@host:5989/?namespace=interop">ssl://username@host:5989/?namespace=interop</a> \
        list --type SYSTEMS -P
</pre>
<dt>SSL error: certificate verify failed</p>
<dd> When using SMI-S plugin with SSL against self-signed SMI-S provider, lsmcli normally quit with &#8216;<code>SSL error: certificate verify failed</code>&#8216;. Please contact SMI-S provider support to setup the self-signed certificate in your system. If you prefer to bypass the certificate check, add &#8216;no_ssl_verify=yes&#8217; at the end of URI, for example:</p>
<dl>
<dt>
<dd>
<pre>
<code>smispy+<a href="ssl://admin@emc-smi:5989?namespace=root/emc">ssl://admin@emc-smi:5989?namespace=root/emc</a>&amp;no_ssl_verify=yes</code>
</pre>
</dl>
</dl>
<h2>BUGS</h2>
<p> Please report bugs to <i>&lt;libstoragemgmt-devel [at] lists.fedorahosted.org&gt;</i></p>
<h2>AUTHOR</h2>
<p> Tony Asleson <i>&lt;tasleson [at] redhat.com&gt;</i><br />
 Gris Ge <i>&lt;fge [at] redhat.com&gt;</i> </p>
<h2>Index</h2>
<dt><a href="#lbDQ">FILES</a></p>
<dd>
<dt><a href="#lbDR">EXAMPLES (command output omitted for brevity)</a></p>
<dd>
<dt><a href="#lbDS">ENVIRONMENT</a></p>
<dd>
<dt><a href="#lbDT">VOLUME REPLICATION TYPES</a></p>
<dd>
<dt><a href="#lbDU">NOTES</a></p>
<dd>
<dt><a href="#lbDV">BUGS</a></p>
<dd>
<dt><a href="#lbDW">AUTHOR</a></p>
<dd></dl>
