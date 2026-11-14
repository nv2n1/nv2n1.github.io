---
title: "vfs_fruit(8)"
name: "vfs_fruit"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_fruit/"
description: "vfs_fruit – Enhanced OS X and Netatalk interoperability"
---

<p>vfs_fruit &#8211; Enhanced OS X and Netatalk interoperability</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = fruit</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The vfs_fruit module provides enhanced compatibility with Apple SMB clients and interoperability with a Netatalk 3 AFP fileserver. </p>
<p> The module should be stacked with vfs_catia if enabling character conversion and must be stacked with vfs_streams_xattr, see the example section for the correct config. </p>
<p> The module enables alternate data streams (ADS) support for a share, intercepts the OS X special streams &quot;AFP_AfpInfo&quot; and &quot;AFP_Resource&quot; and handles them in a special way. All other named streams are deferred to vfs_streams_xattr which must be loaded together with vfs_fruit. </p>
<p> vfs_fruit requires &quot;ea support = yes&quot;. </p>
<p> Be careful when mixing shares with and without vfs_fruit. OS X clients negotiate SMB2 AAPL protocol extensions on the first tcon, so mixing shares with and without fruit will globally disable AAPL if the first tcon is without fruit. </p>
<p> Having shares with ADS support enabled for OS X client is worthwhile because it resembles the behaviour of Apple&#8217;s own SMB server implementation and it avoids certain severe performance degradations caused by Samba&#8217;s case sensitivity semantics. </p>
<p> The OS X metadata and resource fork stream can be stored in a way compatible with Netatalk 3 by setting fruit:resource = file and fruit:metadata = netatalk. </p>
<p> OS X maps NTFS illegal characters to the Unicode private range in SMB requests. By setting fruit:encoding = native, all mapped characters are converted to native ASCII characters. </p>
<p> Finally, share access modes are optionally checked against Netatalk AFP sharing modes by setting fruit:locking = netatalk. </p>
<p> This module is not stackable other then described in this manpage.</p>
<h2>Options</h2>
<p>fruit:resource = [ file | xattr | stream ]</p>
<dl>
<dd>Controls where the OS X resource fork is stored. </p>
<p> Due to a spelling bug in all Samba versions older then 4.6.0, this option can also be given as <i>fruit:ressource</i>, ie with two s. </p>
<p> Settings: </p>
<dl>
<dd>&bull; file (default) &#8211; use a ._ AppleDouble file compatible with OS X and Netatalk</dl>
<dl>
<dd>&bull; xattr &#8211; use a xattr, requires a filesystem with large xattr support and a file IO API compatible with xattrs, this boils down to Solaris and derived platforms and ZFS</dl>
<dl>
<dd>&bull; stream (experimental) &#8211; pass the stream on to the next module in the VFS stack. <i>Warning: </i> this option should not be used with the <i>streams_xattr</i> module due to the extended attributes size limitations of most filesytems.</dl>
</dl>
<p> fruit:metadata = [ stream | netatalk ]</p>
<dl>
<dd>Controls where the OS X metadata stream is stored: </p>
<dl>
<dd>&bull; netatalk (default) &#8211; use Netatalk compatible xattr</dl>
<dl>
<dd>&bull; stream &#8211; pass the stream on to the next module in the VFS stack</dl>
</dl>
<p> fruit:locking = [ netatalk | none ]</p>
<dl>
<dd>
<dl>
<dd>&bull; none (default) &#8211; no cross protocol locking</dl>
<dl>
<dd>&bull; netatalk &#8211; use cross protocol locking with Netatalk</dl>
</dl>
<p> fruit:encoding = [ native | private ]</p>
<dl>
<dd>Controls how the set of illegal NTFS ASCII character, commonly used by OS X clients, are stored in the filesystem. </p>
<p> <i>Important:</i> this is known to not fully work with <i>fruit:metadata=stream</i> or <i>fruit:resource=stream</i>. </p>
<dl>
<dd>&bull; private (default) &#8211; store characters as encoded by the OS X client: mapped to the Unicode private range</dl>
<dl>
<dd>&bull; native &#8211; store characters with their native ASCII value. <i>Important</i>: this option requires the use of <i>vfs_catia</i> in the VFS module stack as shown in the examples section.</dl>
</dl>
<p> fruit:aapl = yes | no</p>
<dl>
<dd>A global option whether to enable Apple&#8217;s SMB2+ extension codenamed AAPL. Default <i>yes</i>. This extension enhances several deficiencies when connecting from Macs: </p>
<dl>
<dd>&bull; directory enumeration is enriched with Mac relevant filesystem metadata (UNIX mode, FinderInfo, resource fork size and effective permission), as a result the Mac client doesn&#8217;t need to fetch this metadata individuallly per directory entry resulting in an often tremendous performance increase.</dl>
<dl>
<dd>&bull; The ability to query and modify the UNIX mode of directory entries.</dl>
</dl>
<p> There&#8217;s a set of per share options that can be used to disable the computation of specific Mac metadata in the directory enumeration context, all are enabled by default: </p>
<dl>
<dd>&bull; readdir_attr:aapl_rsize = true | false</dl>
<dl>
<dd>&bull; readdir_attr:aapl_finder_info = true | false</dl>
<dl>
<dd>&bull; readdir_attr:aapl_max_access = true | false</dl>
<p> fruit:nfs_aces = yes | no</p>
<dl>
<dd>Whether support for querying and modifying the UNIX mode of directory entries via NFS ACEs is enabled, default <i>yes</i>.</dl>
<p> fruit:veto_appledouble = yes | no</p>
<dl>
<dd><i>Note:</i> this option only applies when <i>fruit:resource</i> is set to <i>file</i> (the default). </p>
<p> When <i>fruit:resource</i> is set to <i>file</i>, vfs_fruit may create ._ AppleDouble files. This options controls whether these ._ AppleDouble files are vetoed which prevents the client from accessing them. </p>
<p> Vetoing ._ files may break some applications, eg extracting Mac ZIP archives from Mac clients failes, because they contain ._ files. Setting this option to false will fix this, but the abstraction leak of exposing the internally created ._ files may have other unknown side effects. </p>
<p> The default is <i>yes</i>.</dl>
<p> fruit:copyfile = yes | no</p>
<dl>
<dd>Whether to enable OS X specific copychunk ioctl that requests a copy of a whole file along with all attached metadata. </p>
<p> WARNING: the copyfile request is blocking the client while the server does the copy. </p>
<p> . <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> The default is<br />
 <i>no</i>.</dl>
<p> fruit:posix_rename = yes | no</p>
<dl>
<dd>Whether to enable POSIX directory rename behaviour for OS X clients. Without this, directories can&#8217;t be renamed if any client has any file inside it (recursive!) open. </p>
<p> The default is <i>yes</i>.</dl>
<h2>Examples</h2>
<dl>
<dd>
<pre> <i>[share]</i>
 m[blue]<code>ea support = yes</code>m[]
 m[blue]<code>vfs objects = catia fruit streams_xattr</code>m[]
 m[blue]<code>fruit:resource = file</code>m[]
 m[blue]<code>fruit:metadata = netatalk</code>m[]
 m[blue]<code>fruit:locking = netatalk</code>m[]
 m[blue]<code>fruit:encoding = native</code>m[]</pre>
</dl>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
