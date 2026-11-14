---
title: "saveconfig-json(5)"
name: "saveconfig-json"
section: "5"
letter: "s"
url: "/docs/linux/man/5-saveconfig-json/"
description: "saveconfig.json – Saved configuration file for rtslib-fb and LIO kernel target"
---

<p><code>saveconfig.json</code> &#8211; Saved configuration file for rtslib-fb and LIO kernel target</p>
<h2>Description</h2>
<p><code>/etc/target/saveconfig.json</code> is the default location for storing the configuration of the Linux kernel target, also known as LIO. Since the target is in the kernel, tools like <code>targetctl</code> or <code>targetcli</code> must be used to save and restore the configuration across reboots. </p>
<p> Generating or modifying this file by hand, or with other tools, is also supported. This fills a gap for users whose needs are not met by the targetcli configuration shell, who cannot use the rtslib Python library, and yet also wish to avoid directly manipulating LIO&#8217;s configfs interface.</p>
<h2>Overview</h2>
<p>The configuration file is in the &quot;json&quot; text format, which is both human- and machine-readable. Its format is very closely modeled on the layout and terminology that LIO uses. Attributes may be string, boolean, or numeric values. All sizes are expressed in bytes.</p>
<h2>Layout</h2>
<h3>Top Level Summary</h3>
<p><code>storage_objects</code> describes mappings of resources on the local machine that can be used to emulate block devices. </p>
<p> <code>fabric_modules</code> describes settings for LIO fabrics &#8212; the hardware or software protocols that transport SCSI commands &#8212; such as iSCSI or Fibre Channel over Ethernet (FCoE). </p>
<p> <code>targets</code> describes the SCSI target endpoints that export storage objects over a fabric.</p>
<h3>storage_objects</h3>
<p>All storage objects must contain <i>name</i> and <i>plugin</i> values. Each name must be unique for all storage objects of its plugin type. </p>
<p> <i>plugin</i> must be one of: <i>fileio</i>, <i>block</i>, <i>pscsi</i>, or <i>ramdisk</i>. </p>
<p> Objects with plugin value of <i>fileio</i> must also contain <i>dev</i>, which is the full path to the file that is backing the storage object. Optional <i>fileio</i> attributes are <i>wwn</i> (string), <i>write_back</i> (boolean), and <i>size</i> (number). If the file given in <i>dev</i> does not exist, then <i>size</i> must be present, and a backing file of that size will be created. </p>
<p> Objects with plugin value of <i>block</i> must also contain <i>dev</i>, which is the full path to the block device that is backing the storage object. Optional <i>block</i> attributes are <i>wwn</i> (string), <i>write_back</i> (boolean), and <i>readonly</i> (boolean). </p>
<p> Objects with plugin value of <i>pscsi</i> must also contain <i>dev</i>, which is the full path to the SCSI device that is backing the storage object. There are no optional attributes. </p>
<p> Objects with plugin value of <i>ramdisk</i> must also contain <i>size</i> (number), which is the size in bytes of the ramdisk. Optional <i>ramdisk</i> attributes are <i>wwn</i> (string), and <i>nullio</i> (boolean). </p>
<p> All storage object definitions may also contain an <i>attributes</i> object. This contains LIO attribute values, all of which are also optional. Please see LIO documentation for more information on these.</p>
<h3>fabric_modules</h3>
<p>This section is limited to setting discovery authentication settings for fabrics that support it (currently just iscsi). Objects here should contain <i>name</i> (e.g. &quot;iscsi&quot;), <i>userid</i>, <i>password</i>, <i>mutual_userid</i>, and <i>mutual_password</i> string values.</p>
<h3>targets</h3>
<p>Target configuration is modeled on iSCSI, in which a named target can contain multiple sub-configurations called Target Port Groups (TPGs). LIO follows this model for describing configuration even for fabrics that do not support TPGs. </p>
<p> Objects in <i>targets</i> contain just three attributes: <i>wwn</i> is the world-wide name the target has been given. This may start with &quot;iqn&quot;, or &quot;naa&quot;, for example. <i>fabric</i> is the name of the fabric module this target is exported over. Allowed values for this depend on the system configuration, but examples include &quot;iscsi&quot;, &quot;loopback&quot;, and &quot;tcm_fc&quot;. <i>tpgs</i> is a list of objects describing 1 or more TPGs, described below.</p>
<h3>tpgs</h3>
<p>TPG object attributes are all optional. Values not supplied will be set to default values. <i>tag</i> (number) allows the tpg tag to be specified. <i>enable</i> (bool, default to true) allows the TPG to be disabled or enabled. <i>luns</i>, <i>portals</i>, and <i>node_acls</i> contain further lists of objects, descibed below. Finally, <i>userid</i>, <i>password</i>, <i>mutual_userid</i>, and <i>mutual_password</i> allow main-phase authentication values to be set for fabrics (like iSCSI) that support TPG-level authentication. (Please see <i><a href="/docs/linux/man/8-targetcli/">targetcli</a></i>(8) for details on TPG versus ACL-based authentication.) Finally, TPGs can also contain optional <i>attributes</i> and <i>parameters</i> lists, see LIO documentation for more information.</p>
<h3>luns</h3>
<p>This list of objects maps storage objects to the TPG. <i>index</i> is a TPG-unique number for the assignment, which may be used as the LU number for fabrics that do not support ACL mappings. <i>storage_object</i> is a string linking back to a storage object, of the format &quot;/backstores/&lt;plugin&gt;/&lt;name&gt;&quot;, where &lt;plugin&gt; and &lt;name&gt; correspond to a storage object defined under <i>storage_objects</i>.</p>
<h3>portals</h3>
<p>Portals describe connection endpoints for iSCSI targets. Required values are <i>ip_address</i> (string) and <i>port</i> (number). <i>iser</i> (boolean) is an optional value to enable iSER. <i>offload</i> (boolean) is an optional value to enable hardware offload.</p>
<h3>node_acls</h3>
<p>This contains information about explicit initiator LUN mappings. <i>node_wwn</i> (string) must be present. Authentication may also be set on a per-ACL basis with <i>userid</i>, <i>password</i>, <i>mutual_userid</i>, and <i>mutual_password,</i> similar to TPGs. <i>mapped_luns</i> is a list of mapped luns, described below. Finally, node_acls can contain an optional <i>attributes</i> list.</p>
<h3>mapped_luns</h3>
<p>Objects in <i>mapped_luns</i> contain three required attributes. <i>write_protect</i> (boolean) sets the write-protect status of the mapped LUN. <i>tpg_lun</i> (number) corresponds to an existing entry in the TPG&#8217;s <i>luns</i> list. <i>index</i> is the LU number that the mapped LUN will claim.</p>
<h2>Example Configuration</h2>
<p>Since tools generate this file, one good way to understand its format is to use a tool like <code>targetcli</code> to configure a target, then run <code>saveconfig,</code> and view the resulting json file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-targetcli/">targetcli</a></code>(8), <code><a href="/docs/linux/man/8-targetctl/">targetctl</a></code>(8)</p>
<h2>Files</h2>
<p><code>/etc/target/saveconfig.json</code></p>
<h2>Author</h2>
<p>Man page written by Andy Grover &lt;agrover [at] redhat.com&gt;.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs via &lt;targetcli-fb-devel [at] lists.fedorahosted.org&gt;<br />
 or &lt;<a rel="nofollow" href="https://github.com/open-iscsi/rtslib-fb/issues">https://github.com/open-iscsi/rtslib-fb/issues</a>&gt;</p>
