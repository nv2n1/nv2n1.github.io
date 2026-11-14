---
title: "o2cb_ctl(8)"
name: "o2cb_ctl"
section: "8"
letter: "o"
url: "/docs/linux/man/8-o2cb_ctl/"
description: "o2cb_ctl – Control program for the O2CB cluster service."
---

<p>o2cb_ctl &#8211; Control program for the <i>O2CB</i> cluster service.</p>
<h2>Synopsis</h2>
<p><code>o2cb_ctl </code> <code>-C</code> <code>-n</code> <i>object</i> <code>-t</code> type [<code>-i</code>] [<code>-a</code> <i>attribute</i> ]<br />
 <code>o2cb_ctl </code> <code>-D</code> <code>-n</code> <i>object</i> [<code>-u</code>]<br />
 <code>o2cb_ctl </code> <code>-I</code> [<code>-o-z</code>] <code>-l</code> <i>manager</i>&gt; [<code>-n</code> <i>object</i>&gt;] [<code>-t</code> <i>type</i>] [<code>-a</code> <i>attribute</i>]<br />
 <code>o2cb_ctl </code> <code>-H</code> [<code>-n</code> <i>object</i>] [<code>-t</code> <i>type</i>&gt;] [<code>-a</code> <i>attribute</i>&gt;]<br />
 <code>o2cb_ctl </code> <code>-h</code><br />
 <code>o2cb_ctl </code> <code>-V</code> </p>
<h2>Description</h2>
<p><code>o2cb_ctl</code> is the control program for the <i>O2CB</i> cluster service. Users are not advised to use this program directly but instead use the <i>O2CB</i> init service and/or <i>ocfs2console</i>. </p>
<h2>Options</h2>
<dl>
<dt><code>-C</code></p>
<dd>Create an object in the OCFS2 Cluster Configuration. </p>
<dt><code>-D</code></p>
<dd>Delete an object from the existing OCFS2 Cluster Configuration. </p>
<dt><code>-I</code></p>
<dd>Print information about the OCFS2 Cluster Configuration. </p>
<dt><code>-H</code></p>
<dd>Change an object or objects in the existing OCFS2 Cluster Configuration. </p>
<dt><code>-h</code></p>
<dd>Displays help and exit. </p>
<dt><code>-V</code></p>
<dd>Print version and exit. </p>
</dl>
<h2>Other Options</h2>
<dl>
<dt><code>-a</code> <i>&lt;attribute&gt;</i></p>
<dd>With <code>-C</code>, <i>&lt;attribute&gt;</i> is in format &quot;parameter=value&quot;, where the parameter is a valid parameter that can be set in the file <i>/etc/ocfs2/cluster.conf</i>. With <code>-I</code>, <i>&lt;attribute&gt;</i> may be &quot;parameter&quot;, indicating an attribute to be listed in the output, or it may be &quot;parameter==value&quot;, indicating that only objects matching &quot;parameter=value&quot; are to be displayed. </p>
<dt><code>-i</code></p>
<dd>Valid only with <code>-C</code>. When creating something (<i>node</i> or <i>cluster</i>), it will also install it in the live cluster. If the parameter is not specified, then only update the <i>/etc/ocfs2/cluster.conf</i>. </p>
<dt><code>-n</code> <i>object</i></p>
<dd><i>object</i> is usually the node name or cluster name. In the <i>/etc/ocfs2/cluster.conf</i> file, it would be the value of the name parameter for any of the sections (<i>cluster</i> or <i>node</i>). </p>
<dt><code>-o</code></p>
<dd>Valid only with <code>-I</code>. Using this parameter, if one asks o2cb_ctl to list all nodes, it will output it in a format suitable for shell parsing. </p>
<dt><code>-t</code> <i>type</i></p>
<dd><i>type</i> can be cluster, node or heartbeat. </p>
<dt><code>-u</code></p>
<dd>Valid only with <code>-D</code>. When deleting something (<i>node</i> or <i>cluster</i>), it will also remove it from the live cluster. If the parameter is not specified, then only update the <i>/etc/ocfs2/cluster.conf</i>. </p>
<dt><code>-z</code></p>
<dd>Valid only with <code>-I</code>. This is the default. If one asks o2cb_ctl to list all nodes, it will give a verbose listing. </p>
</dl>
<h2>Examples</h2>
<dl>
<dd>Add node5 to an offline cluster: $ o2cb_ctl -C -n node5 -t node -a number=5<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-a ip_address=192.168.0.5 -a ip_port=7777</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-a cluster=mycluster</p>
<dt>Add node10 to an online cluster:</p>
<dd>$ o2cb_ctl -C -i -n node10 -t node -a number=10<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-a ip_address=192.168.1.10 -a ip_port=7777</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-a cluster=mycluster<br />
 Note the -i argument.</p>
<dt>Query the IP address of node5:</p>
<dd>$ o2cb_ctl -I -n node5 -a ip_address</p>
<dt>Change the IP address of node5:</p>
<dd>$ o2cb_ctl -H -n node5 -a ip_address=192.168.1.5 </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-ocfs2/">mkfs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-fsck-ocfs2/">fsck.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-tunefs-ocfs2/">tunefs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-mounted-ocfs2/">mounted.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-ocfs2console/">ocfs2console</a>(8)</code> <code><a href="/docs/linux/man/7-o2cb/">o2cb</a>(7)</code> </p>
<h2>Authors</h2>
<p>Oracle Corporation</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2009 Oracle. All rights reserved.</p>
