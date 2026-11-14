---
title: "rpc_mkpipe_dentry(9)"
name: "rpc_mkpipe_dentry"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rpc_mkpipe_dentry/"
description: "rpc_mkpipe_dentry – make an rpc_pipefs file for kernel<->userspace communication"
---

<p>rpc_mkpipe_dentry &#8211; make an rpc_pipefs file for kernel&lt;-&gt;userspace communication</p>
<h2>Synopsis</h2>
<pre><code>struct dentry *rpc_mkpipe_dentry(struct dentry *parent, const char *name, void *private, struct rpc_pipe *pipe);</code></pre>
<h2>Arguments</h2>
<p><i>parent</i></p>
<dl>
<dd>
<dd>dentry of directory to create new &#8220;pipe&#8221; in</dl>
<p> <i>name</i></p>
<dl>
<dd>name of pipe</dl>
<p> <i>private</i></p>
<dl>
<dd>private data to associate with the pipe, for the caller&#8217;s use</dl>
<p> <i>pipe</i></p>
<dl>
<dd>rpc_pipe containing input parameters</dl>
<h2>Description</h2>
<p>Data is made available for userspace to read by calls to <code>rpc_queue_upcall</code>. The actual reads will result in calls to <i>ops</i>-&gt;upcall, which will be called with the file pointer, message, and userspace buffer to copy to. </p>
<p> Writes can come at any time, and do not necessarily have to be responses to upcalls. They will result in calls to <i>msg</i>-&gt;downcall. </p>
<p> The <i>private</i> argument passed here will be available to all these methods from the file pointer, via RPC_I(file_inode(file))-&gt;private.</p>
<h2>Copyright</h2>
