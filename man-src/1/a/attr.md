---
title: "attr(1)"
name: "attr"
section: "1"
letter: "a"
url: "/docs/linux/man/1-attr/"
description: "attr – extended attributes on filesystem objects"
---

<h2 class="name">NAME</h2>
<p> attr &#8211; extended attributes on filesystem objects </p>
<h2>SYNOPSIS</h2>
<pre><code>
attr[-LRSq] - s attrname[-V attrvalue] pathname attr[-LRSq] - g attrname pathname attr[-LRSq] - r attrname pathname attr[-LRSq] - l pathname
</code></pre>
<h2>OVERVIEW</h2>
<p> Extended attributes implement the ability for a user to attach name:value pairs to objects within the filesystem. </p>
<p> This document describes the <i>attr</i> command, which is mostly compatible with the IRIX command of the same name. It was originally aimed specifically at users of the XFS filesystem, even though it can be used now on any filesystem that supports extended attributes, but for the generic and more portable interface for filesystem independent extended attribute manipulation, consult the <i><a href="/docs/linux/man/1-getfattr/">getfattr</a></i>(1) and <i><a href="/docs/linux/man/1-setfattr/">setfattr</a></i>(1) documentation. </p>
<p> Extended attributes can be used to store meta-information about the file. For example &quot;character-set=kanji&quot; could tell a document browser to use the Kanji character set when displaying that document and &quot;thumbnail=&#8230;&quot; could provide a reduced resolution overview of a high resolution graphic image. </p>
<p> In supported filesystems, the <i>names</i> can be up to 256 bytes in length, terminated by the first 0 byte. The intent is that they be printable ASCII (or other character set) names for the attribute. The <i>values</i> can be up to 64KB of arbitrary binary data. </p>
<p> Attributes can be attached to all types of inodes: regular files, directories, symbolic links, device nodes, etc. </p>
<p> Extended attributes use 2 disjoint attribute name spaces associated with every filesystem object. They are the <code>root</code> and <code>user</code> address spaces. The <code>root</code> address space is accessible only to the superuser, and then only by specifying a flag argument to the function call. Other users will not see or be able to modify attributes in the <code>root</code> address space. The <code>user</code> address space is protected by the normal file permissions mechanism, so the owner of the file can decide who is able to see and/or modify the value of attributes on any particular file.</p>
<h2>DESCRIPTION</h2>
<p> The <i>attr</i> utility allows the manipulation of extended attributes associated with filesystem objects from within shell scripts. </p>
<p> There are four main operations that <i>attr</i> can perform:</p>
<dl>
<dt><code>GET</code></p>
<dd> The <code>-g attrname</code> option tells <i>attr</i> to search the named object and print (to <tt>stdout</tt>) the value associated with that attribute name. With the <code>-q</code> flag, <tt>stdout</tt> will be exactly and only the value of the attribute, suitable for storage directly into a file or processing via a piped command.</p>
<dt><code>LIST</code></p>
<dd> The <code>-l</code> option tells <i>attr</i> to list the names of all the attributes that are associated with the object, and the number of bytes in the value of each of those attributes. With the <code>-q</code> flag, <tt>stdout</tt> will be a simple list of only the attribute names, one per line, suitable for input into a script.</p>
<dt><code>REMOVE</code></p>
<dd> The <code>-r attrname</code> option tells <i>attr</i> to remove an attribute with the given name from the object if the attribute exists. There is no output on successful completion.</p>
<dt><code>SET/CREATE</code></p>
<dd> The <code>-s attrname</code> option tells <i>attr</i> to set the named attribute of the object to the value read from <tt>stdin</tt>. If an attribute with that name already exists, its value will be replaced with this one. If an attribute with that name does not already exist, one will be created with this value. With the <code>-V attrvalue</code> flag, the attribute will be set to have a value of <code>attrvalue</code> and <tt>stdin</tt> will not be read. With the <code>-q</code> flag, <tt>stdout</tt> will not be used. Without the <code>-q</code> flag, a message showing the attribute name and the entire value will be printed.</dl>
<p> When the <code>-L</code> option is given and the named object is a symbolic link, operate on the attributes of the object referenced by the symbolic link. Without this option, operate on the attributes of the symbolic link itself. </p>
<p> When the <code>-R</code> option is given and the process has appropriate privileges, operate in the <i>root</i> attribute namespace rather that the <i>USER</i> attribute namespace. </p>
<p> The <code>-S</code> option is similar, except it specifies use of the <i>security</i> attribute namespace. </p>
<p> When the <code>-q</code> option is given <i>attr</i> will try to keep quiet. It will output error messages (to <tt>stderr</tt>) but will not print status messages (to <tt>stdout</tt>).</p>
<h2>NOTES</h2>
<p> The standard file interchange/archive programs <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1), and <i><a href="/docs/linux/man/1-cpio/">cpio</a></i>(1) will not archive or restore extended attributes, while the <i><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></i>(8) program will.</p>
<h2>CAVEATS</h2>
<p> The list option present in the IRIX version of this command is not supported. <i>getfattr</i> provides a mechanism to retrieve all of the attribute names.</p>
<h2>AUTHOR</h2>
<p> Andreas Gruenbacher, &lt;<i>a.gruenbacher [at] bestbits.at</i>&gt; and the SGI XFS development team, &lt;<i>linux-xfs [at] oss.sgi.com</i>&gt;. </p>
<p> Please send your bug reports or comments to &lt;<i><a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=attr">https://savannah.nongnu.org/bugs/?group=attr</a></i>&gt; or &lt;<i>acl-devel [at] nongnu.org</i>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-getfattr/">getfattr</a></code>(1), <code><a href="/docs/linux/man/1-setfattr/">setfattr</a></code>(1), <code><a href="/docs/linux/man/3-attr_get/">attr_get</a></code>(3), <code><a href="/docs/linux/man/3-attr_set/">attr_set</a></code>(3), <code><a href="/docs/linux/man/3-attr_multi/">attr_multi</a></code>(3), <code><a href="/docs/linux/man/3-attr_remove/">attr_remove</a></code>(3), <code><a href="/docs/linux/man/5-attr/">attr</a></code>(5), <code><a href="/docs/linux/man/8-xfsdump/">xfsdump</a></code>(8) </p>
<h2>Index</h2>
