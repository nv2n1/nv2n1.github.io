---
title: "targetcli(8)"
name: "targetcli"
section: "8"
letter: "t"
url: "/docs/linux/man/8-targetcli/"
description: "targetcli – administration shell for storage targets"
---

<p><code>targetcli</code> &#8211; administration shell for storage targets</p>
<h2>Description</h2>
<p><code>targetcli</code> is a shell for viewing, editing, and saving the configuration of the kernel&#8217;s target subsystem, also known as LIO. It enables the administrator to assign local storage resources backed by either files, volumes, local SCSI devices, or ramdisk, and export them to remote systems via network fabrics, such as iSCSI or FCoE. </p>
<p> The configuration layout is tree-based, similar to a filesystem, and is navigated in a similar manner.</p>
<h2>Usage</h2>
<p><code>targetcli</code> </p>
<p> <code>targetcli [cmd]</code> </p>
<p> Invoke <code>targetcli</code> as root to enter the configuration shell, or follow with a command to execute but do not enter the shell. Use <code>ls</code> to list nodes below the current path. Moving around the tree is accomplished by the <code>cd</code> command, or by entering the new location directly. Objects are created using <code>create</code>, removed using <code>delete</code>. Use <code>help &lt;cmd&gt;</code> for additional usage information. Tab-completion is available for commands and command arguments. </p>
<p> Configuration changes in targetcli are made immediately to the underlying kernel target configuration. Settings will not be retained across reboot unless <code>saveconfig</code> is either explicitly called, or implicitly by exiting the shell with the global preference <code>auto_save_on_exit</code> set to <code>true</code>, the default.</p>
<h2>Quickstart</h2>
<p>To create an iSCSI target and share a file-backed LUN without any auth checks: </p>
<p> $ sudo targetcli<br />
 /&gt; backstores/fileio create test /tmp/test.img 100m<br />
 /&gt; iscsi/ create iqn.2006-04.com.example:test-target<br />
 /&gt; cd iscsi/iqn.2006-04.com.example:test-target/tpg1/<br />
 tpg1/&gt; luns/ create /backstores/fileio/test<br />
 tpg1/&gt; set attribute generate_node_acls=1<br />
 tpg1/&gt; exit </p>
<p> Although by default targetcli saves the running configuration upon exit, a distribution-specific service must be enabled to restore the saved configuration on reboot. See distribution documentation for specifics, but for example: </p>
<p> $ sudo systemctl enable target.service </p>
<p> See <code>EXAMPLES</code> below for more detailed information on commands and using the shell.</p>
<h2>Backstores</h2>
<p><code>Backstores</code> are different kinds of local storage resources that the kernel target uses to &quot;back&quot; the SCSI devices it exports. The mappings to local storage resources that each backstore creates are called <code>storage objects</code>.</p>
<h3>Fileio</h3>
<p>Allows files to be treated as disk images. When storage objects of this type are created, they can support either write-back or write-thru operation. Using write-back enables the local filesystem cache, which will improve performance but increase the risk of data loss. It is also possible to use fileio with local block device files, if buffered operation is needed. </p>
<p> Fileio also supports using an existing file, or creating a new file. New files are sparsely allocated by default.</p>
<h3>Block</h3>
<p>Allows a local disk block device to be shared.</p>
<h3>Pscsi</h3>
<p>Allows a local SCSI device of any type to be shared. It is generally advised to prefer the block backstore if sharing a block SCSI device is desired.</p>
<h3>Ramdisk</h3>
<p>Allows kernel memory to be shared as a block SCSI device. Since memory is volatile, the contents of the ramdisk will be lost if the system restarts, and this backstore is best used for testing only. </p>
<p> It also supports &quot;nullio&quot; mode, which is not backed by any storage. It discards all writes, and returns all-zeroes for reads.</p>
<h3>Userspace-Backed</h3>
<p>Backstores starting with &quot;user:&quot; are not supported in the kernel, but rely on a userspace process to handle requests. See <code><a href="/docs/linux/man/8-tcmu-runner/">tcmu-runner</a></code>(8) for more information on creating backstores of this type.</p>
<h2>Targets</h2>
<p><code>Targets</code> are instances of a <code>fabric</code>, which adapts the kernel target to a specific transport protocol such as iSCSI, Fibre Channel, or SBP-2. Creating a target in targetcli enables that target to be configured. The name of the target, its WWN (world wide name), may link the configuration to a specific hardware endpoint, like SRP for example, or it may not, like iSCSI. </p>
<p> Aside from &quot;backstores&quot;, all other top-level configuration nodes in targetcli are fabrics that may have targets created for them. Fabrics that require hardware are only listed if the hardware is present and configured properly.</p>
<h3>Creating A Target</h3>
<p>Use the <code>create</code> command within a fabric&#8217;s node to create a target. If the fabric&#8217;s targets are tied to hardware then targetcli will constrain the WWN to available hardware WWNs. These can be shown via tab-completion. If the fabric is not tied to hardware, such as iSCSI, then targetcli will either auto-generate a WWN if none is given, or check that the given WWN has the correct format. All WWNs are prefaced by their type, such as &quot;iqn&quot;, &quot;naa&quot;, or &quot;ib&quot;, and may be given with or without colons. </p>
<p> iSCSI supports multiple WWN formats: iqn, naa, and eui. Other fabrics support single formats only.</p>
<h2>Configuring A Target</h2>
<p>Not all fabrics have the same capabilities. Targets on different fabrics will have different configuration node layouts. iSCSI has the most to configure; other fabrics present subsets of iSCSI&#8217;s feature set.</p>
<h2>Configuring Iscsi</h2>
<p>iSCSI has the most options for configuration.</p>
<h3>Tpgs</h3>
<p>TPGs (Target Portal Groups) allow the iSCSI to support multiple complete configurations within one target. This is useful for complex quality-of-service configurations. targetcli will automatically create one TPG when the target is created, and almost all setups only need one.</p>
<h3>Portals</h3>
<p>An iSCSI target may be reached via multiple IP addresses and ports. These addr:port pairs are called <code>portals</code>. Both IPv4 and IPv6 addresses are supported. </p>
<p> When a target is created, targetcli automatically creates a default portal listening on all IPv4 addresses (shown as 0.0.0.0) on port 3260. If a different configuration is needed, the default portal can be removed and portals configured as desired. </p>
<p> If the hardware supports it, <code>iSER</code> (iSCSI Extensions for RDMA) may be enabled via the <code>enable_iser</code> command within each portal&#8217;s node. Or, if the hardware supports it, hardware offload may be enabled via the <code>enable_offload</code> command within each portal&#8217;s node.</p>
<h3>Luns</h3>
<p>The kernel target exports SCSI Logical Units, also called <code>LUNs</code>. This section links the previously-defined storage objects with the target, and defines which number (the Logical Unit Number) the device will use. Note that if ACLs are being used, a <code>lun mapping</code> must be created under the ACL that refers back to the TPG LUN.</p>
<h3>Acls</h3>
<p>ACLs (Access Control Lists) allow different configuration, depending on the initiator that is connecting to the target. This includes both per-initiator authentication settings as well as per-initiator LUN mappings. </p>
<p> <code>create &lt;wwn&gt;</code> in the <code>acls</code> node creates an ACL for an initiator, and <code>create</code> within the ACL creates a LUN mapping. (This can either refer to the TPG LUN, or to the storage object, in which case the TPG LUN will be configured as well.) Global setting <code>auto_add_mapped_luns</code> affects this, see below.</p>
<h3>Authentication</h3>
<p>iSCSI supports authentication via the CHAP protocol, which uses a username and password. The initiator may be required to supply valid credentials to the target, and the target may also be required to supply credentials back to the initiator. The latter is referred to as <code>mutual authentication</code>. </p>
<p> Furthermore, authentication credentials may be different for each session phase (Discovery or Normal), and authentication in a Normal session may be set at the TPG level, or per-ACL. </p>
<p> <code>Discovery Authentication</code><br />
 iSCSI Discovery sessions allow the initiator to connect to a portal and discover targets with the SendTargets command, but not access them. The four parameters <code>userid</code>, <code>password</code>, <code>mutual_userid</code>, and <code>mutual_password</code> are configured via <code>set discovery_auth</code> command within the top-level iscsi configuration node. 1-way authentication is enabled if userid and password are both set, and mutual authentication is enabled if all four are set. Authentication is disabled by unsetting the parameters. </p>
<p> <code>Normal Authentication</code><br />
 Similarly, the four parameters <code>userid</code>, <code>password</code>, <code>mutual_userid</code>, and <code>mutual_password</code> are configured via <code>set auth</code> command within the TPG node and ACL nodes. However, LIO only uses one or the other, depending on the TPG&#8217;s <code>generate_node_acls</code> attribute setting. If generate_node_acls is 1, the TPG-wide settings will be used. If generate_node_acls is 0, then the user-created ACLs&#8217; settings will be used. </p>
<p> Enable generate_node_acls with <code>set attribute generate_node_acls=1</code> within the TPG node. This can be thought of as &quot;ignore ACLs mode&quot; &#8212; both authentication and LUN mapping will then use the TPG settings. </p>
<p> <code>No Authentication</code><br />
 Authentication is disabled by clearing the TPG &quot;authentication&quot; attribute: <code>set attribute authentication=0</code>. Although initiator names are trivially forgeable, generate_node_acls still works here to either ignore user-defined ACLs and allow all, or check that an ACL exists for the connecting initiator.</p>
<h2>Configuring Fibre Channel (Qla2Xxx)</h2>
<p>Operation as a target requires that <code>/sys/module/qla2xxx/parameters/qlini_mode</code> report &quot;disabled&quot;. This may require passing the <code>qlini_mode=disabled</code> parameter to the qla2xxx module when it loads.</p>
<h2>Configuring Fibre Channel Over Ethernet (Tcm_Fc)</h2>
<p>Ensure <code>fcoeadm -i</code> shows a working endpoint.</p>
<h2>Configuring Srp</h2>
<p>SRP (SCSI RDMA Protocol) requires that RDMA-capable hardware is present. It uses &quot;ib&quot; WWNs.</p>
<h2>Configuring Loopback</h2>
<p>Storage objects may be re-exported as local SCSI devices with this fabric.</p>
<h2>Configuring Other Fabrics</h2>
<p>Other fabrics may be present. They are for specialized uses. Use at your own risk.</p>
<h2>Examples</h2>
<h3>Defining A Storage Object Within A Backstore</h3>
<p><code>backstores/fileio create disk1 /disks/disk1.img 140M</code><br />
 Creates a storage object named <i>disk1</i> with the given path and size. <code>targetcli</code> supports common size abbreviations like &#8216;M&#8217;, &#8216;G&#8217;, and &#8216;T&#8217;.</p>
<h3>Exporting A Storage Object Via Iscsi</h3>
<p><code>iscsi/ create</code><br />
 Creates an iSCSI target with a default WWN. It will also create an initial target portal group called <i>tpg1</i>. </p>
<p> <code>iqn.2003-01.org.linux-iscsi.test2.x8664:sn123456789012/tpg1/</code><br />
 An example of changing to the configuration node for the given target&#8217;s first target portal group (TPG). This is equivalent to giving the command prefixed by &quot;cd&quot;. (Although more can be useful for certain setups, most configurations have a single TPG per target. In this case, configuring the TPG is equivalent to configuring the overall target.) </p>
<p> <code>portals/ create</code><br />
 Add a portal, i.e. an IP address and TCP port via which the target can be contacted by initiators. Only required if the default 0.0.0.0:3260 portal is not present. </p>
<p> <code>luns/ create /backstores/fileio/disk1</code><br />
 Create a new LUN in the TPG, attached to the storage object that has previously been defined. The storage object now shows up under the /backstores configuration node as activated. </p>
<p> <code>acls/ create iqn.1994-05.com.redhat:4321576890</code><br />
 Creates an ACL (access control list) entry for the given iSCSI initiator. </p>
<p> <code>acls/iqn.1994-05.com.redhat:4321576890 create 2 0</code><br />
 Gives the initiator access to the first exported LUN (lun0), which the initiator will see as lun2. The default is to give the initiator read/write access; if read-only access was desired, an additional &quot;1&quot; argument would be added to enable write-protect. (Note: if global setting <code>auto_add_mapped_luns</code> is true, this step is not necessary.)</p>
<h3>Exporting A Storage Object Via Fcoe</h3>
<p><code>tcm_fc/ create 20:00:00:19:99:a8:34:bc</code><br />
 Create an FCoE target with the given WWN. <code>targetcli</code> can tab-complete the WWN based on registered FCoE interfaces. If none are found, verify that they are properly configured and are shown in the output of <code>fcoeadm -i</code>. </p>
<p> <code>tcm_fc/20:00:00:19:99:a8:34:bc/</code><br />
 If <code>auto_cd_after_create</code> is set to false, change to the configuration node for the given target, equivalent to giving the command prefixed by <code>cd</code>. </p>
<p> <code>luns/ create /backstores/fileio/disk1</code><br />
 Create a new LUN for the interface, attached to a previously defined storage object. The storage object now shows up under the /backstores configuration node as <code>activated</code>. </p>
<p> <code>acls/ create 00:99:88:77:66:55:44:33</code><br />
 Create an ACL (access control list), for defining the resources each initiator may access. The default behavior is to auto-map existing LUNs to the ACL; see help for more information. </p>
<p> The LUN should now be accessible via FCoE.</p>
<h2>Other Commands</h2>
<p><code>saveconfig</code><br />
 Save the current configuration settings to a file, from which settings will be restored if the system is rebooted. By default, this will save the configuration to <i>/etc/target/saveconfig.json</i>. </p>
<p> This command is executed from the configuration root node. </p>
<p> <code>restoreconfig</code><br />
 Restore target configuration from a file, the default is the file listed under <code>saveconfig</code>. This will fail if there is already an established config, unless the <i>clear_existing</i> option is set to <i>true</i>. </p>
<p> This command is executed from the configuration root node. </p>
<p> <code>clearconfig</code><br />
 Clears the entire current local configuration. The parameter <i>confirm=true</i> must also be given, as a precaution. </p>
<p> This command is executed from the configuration root node. </p>
<p> <code>sessions [ list | detail ] [sid]</code><br />
 Lists the current open sessions or a specific session, with or without details. </p>
<p> This command is executed from the configuration root node. </p>
<p> <code>exit</code><br />
 Leave the configuration shell.</p>
<h2>Settings Groups</h2>
<p>Settings are broken into groups. Individual settings are accessed by <code>get &lt;group&gt; &lt;setting&gt;</code> and <code>set &lt;group&gt; &lt;setting&gt;=&lt;value&gt;</code>, and the settings of an entire group may be displayed by <code>get &lt;group&gt;</code>. All except for <i>global</i> are associated with a particular configuration node.</p>
<h3>Global</h3>
<p>Shell-related user-specific settings are in <i>global</i>, and are visible from all configuration nodes. They are mostly shell display options, but some starting with <code>auto_</code> affect shell behavior and may merit customization. These include <code>auto_save_on_exit</code>, which controls if exiting targetcli saves the configuration; <code>auto_add_mapped_luns</code>, to automatically add existing LUNs to new ACLs, and new LUNS to existing ACLs; and <code>auto_cd_after_create</code>, to change working path to newly-created nodes. Global settings are user-specific and are saved to ~/.targetcli/ upon exit, unlike other groups, which are system-wide and kept in <code>/etc/target/saveconfig.json</code>.</p>
<h3>Backstore-Specific</h3>
<p><code>attribute</code><br />
 /backstore/&lt;type&gt;/&lt;name&gt; configuration node. Contains values relating to the backstore and storage object.</p>
<h3>Iscsi-Specific</h3>
<p><code>discovery_auth</code><br />
 /iscsi configuration node. Set the normal and mutual authentication userid and password for discovery sessions, as well as enabling or disabling it. By default it is disabled &#8212; no authentication is required for discovery. </p>
<p> <code>parameter</code><br />
 /iscsi/&lt;target_iqn&gt;/tpgX configuration node. ISCSI-specific parameters such as <i>AuthMethod</i>, <i>MaxBurstLength</i>, <i>IFMarker</i>, <i>DataDigest</i>, and similar. </p>
<p> <code>attribute</code><br />
 /iscsi/&lt;target_iqn&gt;/tpgX configuration node. Contains implementation-specific settings for the TPG, such as <code>authentication</code>, to enforce or disable authentication for the full-feature phase (i.e. non-discovery). </p>
<p> <code>auth</code><br />
 /iscsi/&lt;target_iqn&gt;/tpgX/acls/&lt;initiator_iqn&gt; configuration node. Set the userid and password for full-feature phase for this ACL.</p>
<h2>Files</h2>
<p><code>/etc/target/saveconfig.json</code><br />
 <code>/etc/target/backup/*</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-targetctl/">targetctl</a></code>(8), <code><a href="/docs/linux/man/8-tcmu-runner/">tcmu-runner</a></code>(8)</p>
<h2>Author</h2>
<p>Written by Jerome Martin &lt;jxm [at] risingtidesystems.com&gt;.<br />
 Man page written by Andy Grover &lt;agrover [at] redhat.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs via &lt;targetcli-fb-devel [at] lists.fedorahosted.org&gt;<br />
 or &lt;<a rel="nofollow" href="https://github.com/open-iscsi/targetcli-fb/issues">https://github.com/open-iscsi/targetcli-fb/issues</a>&gt;</p>
