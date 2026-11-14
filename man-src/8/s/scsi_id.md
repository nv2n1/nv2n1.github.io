---
title: "scsi_id(8)"
name: "scsi_id"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scsi_id/"
description: "scsi_id – retrieve and generate a unique SCSI identifier"
---

<p>scsi_id &#8211; retrieve and generate a unique SCSI identifier</p>
<h2>Synopsis</h2>
<p><code>scsi_id</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>scsi_id</code> queries a SCSI device via the SCSI INQUIRY vital product data (VPD) page 0x80 or 0x83 and uses the resulting data to generate a value that is unique across all SCSI devices that properly support page 0x80 or page 0x83. If a result is generated it is sent to standard output, and the program exits with a zero value. If no identifier is output, the program exits with a non-zero value. <code>scsi_id</code> is primarily for use by other utilities such as <code>udev</code> that require a unique SCSI identifier. By default all devices are assumed black listed, the <code>&#8211;whitelisted</code> option must be specified on the command line or in the config file for any useful behaviour. SCSI commands are sent directly to the device via the SG_IO ioctl interface. In order to generate unique values for either page 0x80 or page 0x83, the serial numbers or world wide names are prefixed as follows. Identifiers based on page 0x80 are prefixed by the character &#8216;S&#8217;, the SCSI vendor, the SCSI product (model) and then the the serial number returned by page 0x80. For example: </p>
<pre># /usr/lib/udev/scsi_id --page=0x80 --whitelisted --device=/dev/sda
SIBM 3542 1T05078453</pre>
<p>Identifiers based on page 0x83 are prefixed by the identifier type followed by the page 0x83 identifier. For example, a device with a NAA (Name Address Authority) type of 3 (also in this case the page 0x83 identifier starts with the NAA value of 6): </p>
<pre># /usr/lib/udev/scsi_id --page=0x83 --whitelisted --device=/dev/sda
3600a0b80000b174b000000d63efc5c8c</pre>
<h2>Options</h2>
<dl>
<dt><code>&#8211;blacklisted</code></p>
<dd>The default behaviour &#8211; treat the device as black listed, and do nothing unless a white listed device is found in the scsi_id config-file.</p>
<dt><code>&#8211;device=</code><i>device</i></p>
<dd>Send SG_IO commands to <code>device</code>, such as <code>/dev/sdc</code>.</p>
<dt><code>&#8211;config=</code><i>config-file</i></p>
<dd>Read configuration and black/white list entries from <code>config-file</code> rather than the default <code>/etc/scsi_id.config</code> file.</p>
<dt><code>&#8211;whitelisted</code></p>
<dd>Treat the device as white listed. The <code>&#8211;whitelisted</code> option must be specified on the command line or in the scsi_id configuration file for <code>scsi_id</code> to generate any output.</p>
<dt><code>&#8211;page=</code><i>0x80</i><code>|</code><i>0x83</i><code>|</code><i>pre-spc3-83</i></p>
<dd>Use SCSI INQUIRY VPD page code 0x80, 0x83, or pre-spc3-83. </p>
<p> The default behaviour is to query the available VPD pages, and use page 0x83 if found, else page 0x80 if found, else nothing. </p>
<p> Page pre-spc3-83 should only be utilized for those scsi devices which are not compliant with the SPC-2 or SPC-3 format for page 83. While this option is used for older model 4, 5, and 6 EMC Symmetrix devices, its use with SPC-2 or SPC-3 compliant devices will fallback to the page 83 format supported by these devices.</p>
<dt><code>&#8211;replace-whitespace</code></p>
<dd>Reformat the output : replace all whitespaces by underscores.</p>
<dt><code>&#8211;export</code></p>
<dd>Export all data in KEY=&lt;value&gt; format used to import in other programs.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Generate verbose debugging output.</p>
<dt><code>&#8211;version</code></p>
<dd>Display version number and exit. </p>
</dl>
<h2>Files</h2>
<pre><dl><dt><i>/etc/scsi_id.config</i><dd>Configuration of black/white list entries and per device options:
# one config per line, short match strings match longer strings
# vendor=string[,model=string],options=&lt;per-device scsi_id command line options&gt;
vendor=&quot;ATA&quot;,options=-p 0x80</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-udev/">udev</a></code>(7)</p>
<h2>Authors</h2>
<p>Developed by Patrick Mansfield &lt;patmans [at] us.ibm.com&gt; based on SCSI ID source included in earlier linux 2.5 kernels, sg_utils source, and SCSI specifications.</p>
