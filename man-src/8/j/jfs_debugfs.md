---
title: "jfs_debugfs(8)"
name: "jfs_debugfs"
section: "8"
letter: "j"
url: "/docs/linux/man/8-jfs_debugfs/"
description: "jfs_debugfs – shell-type JFS file system editor"
---

<p><code>jfs_debugfs</code> &#8211; shell-type JFS file system editor</p>
<h2>Synopsis</h2>
<p><code>jfs_debugfs</code> <i>device</i> </p>
<h2>Description</h2>
<p><code>jfs_debugfs</code> is a program which can be used to perform various low-level actions on a JFS formatted device. <i>device</i> is the special file name corresponding to the actual device to be edited (e.g.<code> /dev/hdb1</code>). <code>jfs_debugfs</code> must be run as root. </p>
<h2>Commands</h2>
<dl>
<dt><code>a[lter]</code><i> &lt;block&gt; &lt;offset&gt; &lt;hex_string&gt;</i></p>
<dd>&nbsp;<wbr>replaces the data located at the <i>&lt;offset&gt;</i> of <i>&lt;block&gt;</i> with <i>&lt;hex_string&gt;</i> </p>
<p> <i>&lt;block&gt;</i> is the block number &#8211; given in decimal </p>
<p> <i>&lt;offset&gt;</i> is the offset within that block &#8211; given in hexadecimal </p>
<p> <i>&lt;hex_string&gt;</i> is an even-numbered string of hexadecimal digits to write to the disk </p>
<dt><code>b[tree]</code><i> &lt;block&gt; [&lt;offset&gt;]</i></p>
<dd><code>* not implemented yet *</code><br />
&nbsp;<wbr>displays one node of the btree located at <i>&lt;offset&gt;</i> of <i>&lt;block&gt;</i> and enters a subcommand mode to navigate the btree </p>
<p> <code>SUBCOMMANDS:</code><br />
&nbsp;<wbr>l&nbsp;<wbr>=&gt;&nbsp;<wbr>visit left sibling<br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify current node<br />
&nbsp;<wbr>p&nbsp;<wbr>=&gt;&nbsp;<wbr>visit parent node<br />
&nbsp;<wbr>r&nbsp;<wbr>=&gt;&nbsp;<wbr>visit right sibling<br />
&nbsp;<wbr>[0-9]&nbsp;<wbr>=&gt;&nbsp;<wbr>visit the n&#8217;th child node<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>cb[blfsck]</code></p>
<dd>&nbsp;<wbr>displays the area used by ClearBadBlockList for communication with fsck </p>
<p> <code>SUBCOMMANDS:</code><br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify entries<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>dir[ectory]</code><i> &lt;inode_number&gt; [&lt;file_set&gt;]</i></p>
<dd>&nbsp;<wbr>displays the directory entries at <i>&lt;inode_number&gt;</i> and enters subcommand mode </p>
<p> <i>&lt;inode_number&gt;</i> is the directory&#8217;s inode &#8211; given in decimal </p>
<p> <i>&lt;file_set&gt;</i> currently must be zero </p>
<p> <code>SUBCOMMANDS:</code><br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify entries<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>d[isplay]</code><i> [&lt;block&gt; [&lt;offset&gt; [&lt;format&gt; [&lt;count&gt;]]]]</i></p>
<dd>displays <i>&lt;count&gt;</i> objects located at the <i>&lt;offset&gt;</i> of <i>&lt;block&gt;</i> in <i>&lt;format&gt;</i> </p>
<p> <i>&lt;block&gt;</i> is the block number &#8211; given in decimal </p>
<p> <i>&lt;offset&gt;</i> is the offset within <i>&lt;block&gt;</i> &#8211; given in hexadecimal </p>
<p> <i>&lt;format&gt;</i> is one of the following:<br />
&nbsp;<wbr>a&nbsp;<wbr>=&gt;&nbsp;<wbr>ascii<br />
&nbsp;<wbr>b&nbsp;<wbr>=&gt;&nbsp;<wbr>block allocation map<br />
&nbsp;<wbr>d&nbsp;<wbr>=&gt;&nbsp;<wbr>decimal<br />
&nbsp;<wbr>i&nbsp;<wbr>=&gt;&nbsp;<wbr>inode<br />
&nbsp;<wbr>I&nbsp;<wbr>=&gt;&nbsp;<wbr>inode allocation map<br />
&nbsp;<wbr>s&nbsp;<wbr>=&gt;&nbsp;<wbr>superblock<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>hexadecimal<br />
&nbsp;<wbr>X&nbsp;<wbr>=&gt;&nbsp;<wbr>extent allocation descriptor </p>
<p> <i>&lt;count&gt;</i> is the number of objects to display &#8211; given in decimal </p>
<dt><code>dm[ap]</code></p>
<dd>&nbsp;<wbr>displays aggregate disk&nbsp;<wbr>(block)&nbsp;<wbr>map </p>
<p> <code>SUBCOMMANDS</code><br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify map fields<br />
&nbsp;<wbr>f&nbsp;<wbr>=&gt;&nbsp;<wbr>display free count<br />
&nbsp;<wbr>t&nbsp;<wbr>=&gt;&nbsp;<wbr>display tree levels<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>dt[ree]</code><i> &lt;inode_number&gt; [&lt;file_set&gt;]</i></p>
<dd>&nbsp;<wbr>displays root of the directory btree located at <i>&lt;inode_number&gt;</i> and enters a subcommand mode to navigate the btree </p>
<p> <i>&lt;inode_number&gt;</i> is the directory&#8217;s inode &#8211; given in decimal </p>
<p> <i>&lt;file_set&gt;</i> currently must be zero </p>
<p> <code>SUBCOMMANDS</code><br />
&nbsp;<wbr>l&nbsp;<wbr>=&gt;&nbsp;<wbr>visit left sibling<br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify current node<br />
&nbsp;<wbr>p&nbsp;<wbr>=&gt;&nbsp;<wbr>visit parent node&nbsp;<wbr>(not parent directory)<br />
&nbsp;<wbr>r&nbsp;<wbr>=&gt;&nbsp;<wbr>visit right sibling<br />
&nbsp;<wbr>[0-9]&nbsp;<wbr>=&gt;&nbsp;<wbr>visit the n&#8217;th child node<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>fsckw[sphdr]</code></p>
<dd>&nbsp;<wbr>displays the header of the fsck workspace in the aggregate </p>
<p> <code>SUBCOMMANDS:</code><br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify entries<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>h[elp]</code><i> [&lt;command&gt;]</i></p>
<dd>&nbsp;<wbr>displays help for <i>&lt;command&gt;</i><br />
&nbsp;<wbr>if no command is given, all possible commands are displayed </p>
<dt><code>ia[g]</code><i> [&lt;IAG_number&gt;] [a | s | &lt;file_set&gt;]</i></p>
<dd>&nbsp;<wbr>displays IAG information for <i>&lt;IAG_number&gt;</i> and enters subcommand mode </p>
<p> <i>&lt;IAG_number&gt;</i> is given in decimal </p>
<p> <i>a</i> is to use the primary aggregate inode table </p>
<p> <i>s</i> is to use the secondary aggregate inode table </p>
<p> <i>&lt;file_set&gt;</i> currently must be zero </p>
<p> <code>SUBCOMMANDS</code><br />
&nbsp;<wbr>e&nbsp;<wbr>=&gt;&nbsp;<wbr>display/modify inode extents map<br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify IAG<br />
&nbsp;<wbr>p&nbsp;<wbr>=&gt;&nbsp;<wbr>display/modify persistent map<br />
&nbsp;<wbr>w&nbsp;<wbr>=&gt;&nbsp;<wbr>display/modify working map<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>i[node]</code><i> [&lt;inode_number&gt;] [a | s | &lt;file_set&gt;]</i></p>
<dd>&nbsp;<wbr>displays inode information for <i>&lt;inode_number&gt;</i> and enters subcommand mode </p>
<p> <i>&lt;inode_number&gt;</i> is given in decimal </p>
<p> <i>a</i> is to use the primary aggregate inode table </p>
<p> <i>s</i> is to use the secondary aggregate inode table </p>
<p> <i>&lt;file_set&gt;</i> currently must be zero </p>
<p> <code>SUBCOMMANDS</code><br />
&nbsp;<wbr>a&nbsp;<wbr>=&gt;&nbsp;<wbr>display/modify inode&#8217;s ACL<br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify inode<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>logs[uper]</code></p>
<dd>&nbsp;<wbr>displays the journal log superblock and enters subcommand mode </p>
<p> <code>SUBCOMMANDS</code><br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify journal log superblock<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>q[uit]</code></p>
<dd>&nbsp;<wbr>exits jfs_debugfs </p>
<dt><code>se[t]</code><i> [&lt;variable&gt; &lt;value&gt;]</i></p>
<dd><code>* not implemented yet *</code><br />
&nbsp;<wbr>set user-defined <i>&lt;variable&gt;</i> to <i>&lt;value&gt;</i><br />
&nbsp;<wbr>if no arguments are given, displays all set variables </p>
<p> <i>&lt;variable&gt;</i> must begin with an alphabetic character </p>
<dt><code>su[perblock]</code><i> [p | s]</i></p>
<dd>&nbsp;<wbr>displays superblock data </p>
<p> <i>p</i> displays the primary superblock </p>
<p> <i>s</i> displays the secondary superblock </p>
<p> <code>SUBCOMMANDS:</code><br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify entries<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>s2p[erblock]</code><i> [p | s]</i></p>
<dd>&nbsp;<wbr>displays alternate superblock data </p>
<p> <i>p</i> displays the primary superblock </p>
<p> <i>s</i> displays the secondary superblock </p>
<p> <code>SUBCOMMANDS:</code><br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify entries<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
<dt><code>u[nset]</code><i> &lt;variable&gt;</i></p>
<dd><code>* not implemented yet *</code><br />
&nbsp;<wbr>deletes user-defined <i>&lt;variable&gt;</i> </p>
<dt><code>xt[ree]</code><i> &lt;inode_number&gt; [&lt;file_set&gt;]</i></p>
<dd>&nbsp;<wbr>displays root of the non-directory btree located at <i>&lt;inode_number&gt;</i> and enters a subcommand mode to navigate the btree </p>
<p> <i>&lt;inode_number&gt;</i> is the directory&#8217;s inode &#8211; given in decimal </p>
<p> <i>&lt;file_set&gt;</i> currently must be zero </p>
<p> <code>SUBCOMMANDS</code><br />
&nbsp;<wbr>l&nbsp;<wbr>=&gt;&nbsp;<wbr>visit left sibling<br />
&nbsp;<wbr>m&nbsp;<wbr>=&gt;&nbsp;<wbr>modify current node<br />
&nbsp;<wbr>p&nbsp;<wbr>=&gt;&nbsp;<wbr>visit parent node&nbsp;<wbr>(not parent directory)<br />
&nbsp;<wbr>r&nbsp;<wbr>=&gt;&nbsp;<wbr>visit right sibling<br />
&nbsp;<wbr>[0-9]&nbsp;<wbr>=&gt;&nbsp;<wbr>visit the n&#8217;th child node<br />
&nbsp;<wbr>x&nbsp;<wbr>=&gt;&nbsp;<wbr>exit subcommand mode </p>
</dl>
<h2>Reporting Bugs</h2>
<p>If you find a bug in <code>JFS</code> or <code>jfs_debugfs</code>, please report it via the bug tracking system (&quot;Report Bugs&quot; section) of the JFS project web site: </p>
<pre><a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>
<p>Please send as much pertinent information as possible, including the complete output of running <code>jfs_fsck</code> with the <code>-v</code> and <code>-n</code> options on the JFS device.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-jfs_fsck/">jfs_fsck</a></code>(8), <code><a href="/docs/linux/man/8-jfs_mkfs/">jfs_mkfs</a></code>(8), <code><a href="/docs/linux/man/8-jfs_fscklog/">jfs_fscklog</a></code>(8), <code><a href="/docs/linux/man/8-jfs_logdump/">jfs_logdump</a></code>(8), <code><a href="/docs/linux/man/8-jfs_tune/">jfs_tune</a></code>(8), </p>
<h2>Authors</h2>
<pre>Barry Arndt (barndt [at] us.ibm.com)
William Braswell, Jr.</pre>
<p><code>jfs_debugfs</code> is maintained by IBM. </p>
<pre>See the JFS project web site for more details:
<a rel="nofollow" href="http://jfs.sourceforge.net/">http://jfs.sourceforge.net/</a></pre>
