---
title: "nvme-format(1)"
name: "nvme-format"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-format/"
---

<h2 class="name">NAME</h2>
 

 nvme-format - Format an NVMe device 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme format&lt;device&gt;[--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
                   [--lbaf = &lt;lbaf&gt; | -l&lt;lbaf&gt;]
                   [--ses = &lt;ses&gt; | -s&lt;ses&gt;]
                   [--pil = &lt;pil&gt; | -p&lt;pil&gt;]
                   [--pi = &lt;pi&gt; | -i&lt;pi&gt;]
                   [--ms = &lt;ms&gt; | -m&lt;ms&gt;]
</code></pre>

<h2>DESCRIPTION</h2>

 

 For the NVMe device given, send an nvme Format Namespace admin command and provides the results. 

 The &lt;device&gt; parameter is mandatory and may be either the NVMe character device (ex: /dev/nvme0), or a namespace block device (ex: /dev/nvme0n1). If the character device is given, the namespace identifier will default to 0xffffffff to send the format to all namespace, but can be overridden to any namespace with the <i>namespace-id</i> option. If the block device is given, the namespace identifier will default to the namespace id of the block device given, but can be overridden with the same option. 

 On success, the program will automatically issue BLKRRPART ioctl to force rescanning the namespaces. If the driver is recent enough, this will automatically update the physical block size. If it is not recent enough, you will need to remove and rescan your device some other way for the new block size to be visible.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> Send the format command for the specified nsid. This can be used to override the default value for either character device (0xffffffff) or the block device (result from NVME_IOCTL_ID).</dl>
 

 -l &lt;lbaf&gt;, --lbaf=&lt;lbaf&gt;
<dl>
<dt>
<dd> LBA Format: This field specifies the LBA format to apply to the NVM media. This corresponds to the LBA formats indicated in the Identify Namespace command. Defaults to 0.</dl>
 

 -s &lt;ses&gt;, --ses=&lt;ses&gt;
<dl>
<dt>
<dd> Secure Erase Settings: This field specifies whether a secure erase should be performed as part of the format and the type of the secure erase operation. The erase applies to all user data, regardless of location (e.g., within an exposed LBA, within a cache, within deallocated LBAs, etc). Defaults to 0. <table BORDER> <tr VALIGN=top><td> Value </td><td> Definition 
</td></tr> <tr VALIGN=top><td> 0 </td><td> No secure erase operation requested 
</td></tr> <tr VALIGN=top><td> 1 </td><td> User Data Erase: All user data shall be erased, contents of the user data after the erase is indeterminate (e.g., the user data may be zero filled, one filled, etc). The controller may perform a cryptographic erase when a User Data Erase is requested if all user data is encrypted. 
</td></tr> <tr VALIGN=top><td> 2 </td><td> Cryptographic Erase: All user data shall be erased cryptographically. This is accomplished by deleting the encryption key. 
</td></tr> <tr VALIGN=top><td> 3-7 </td><td> Reserved 
</td></tr> </table> 

</dl>
 

 -p &lt;pil&gt;, --pil=&lt;pil&gt;
<dl>
<dt>
<dd> Protection Information Location: If set to '1' and protection information is enabled, then protection information is transferred as the first eight bytes of metadata. If cleared to '0' and protection information is enabled, then protection information is transferred as the last eight bytes of metadata. Defaults to 0.</dl>
 

 -i &lt;pi&gt;, --pi=&lt;pi&gt;
<dl>
<dt>
<dd> Protection Information: This field specifies whether end-to-end data protection is enabled and the type of protection information. Defaults to 0. <table BORDER> <tr VALIGN=top><td> Value </td><td> Definition 
</td></tr> <tr VALIGN=top><td> 0 </td><td> Protection information is not enabled 
</td></tr> <tr VALIGN=top><td> 1 </td><td> Protection information is enabled, Type 1 
</td></tr> <tr VALIGN=top><td> 2 </td><td> Protection information is enabled, Type 2 
</td></tr> <tr VALIGN=top><td> 3 </td><td> Protection information is enabled, Type 3 
</td></tr> <tr VALIGN=top><td> 4-7 </td><td> Reserved 
</td></tr> </table> 

</dl>
 

 -m &lt;ms&gt;, --ms=&lt;ms&gt;
<dl>
<dt>
<dd> Metadata Settings: This field is set to '1' if the metadata is transferred as part of an extended data LBA. This field is cleared to '0' if the metadata is transferred as part of a separate buffer. The metadata may include protection information, based on the Protection Information (PI) field. Defaults to 0.</dl>

<h2>EXAMPLES</h2>

 

<dl>
<dt>
<dd> &bull; Format the device using all defaults: 

<dl>
<dt>
<dd> <pre>
# nvme format /dev/nvme0n1
</pre></dl>
</dl>
 

<dl>
<dt>
<dd> &bull; Format namespace 1 with user data secure erase settings and protection information: 

<dl>
<dt>
<dd> <pre>
# nvme format /dev/nvme0 --namespace-id=1 --ses=1 --pi=1
</pre></dl>
</dl>

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


