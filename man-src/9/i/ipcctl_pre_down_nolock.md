---
title: "ipcctl_pre_down_nolock(9)"
name: "ipcctl_pre_down_nolock"
section: "9"
letter: "i"
url: "/docs/linux/man/9-ipcctl_pre_down_nolock/"
---

ipcctl_pre_down_nolock - retrieve an ipc and check permissions for some IPC_XXX cmd

<h2>Synopsis</h2>

<pre><code>struct kern_ipc_perm *ipcctl_pre_down_nolock(struct ipc_namespace *ns, struct ipc_ids *ids, int id, int cmd, struct ipc64_perm *perm, int extra_perm);</code></pre>

<h2>Arguments</h2>

<i>ns</i>
<dl><dd><dd>ipc namespace</dl>
 

 <i>ids</i>
<dl><dd>the table of ids where to look for the ipc</dl>
 

 <i>id</i>
<dl><dd>the id of the ipc to retrieve</dl>
 

 <i>cmd</i>
<dl><dd>the cmd to check</dl>
 

 <i>perm</i>
<dl><dd>the permission to set</dl>
 

 <i>extra_perm</i>
<dl><dd>one extra permission parameter used by msq</dl>

<h2>Description</h2>

This function does some common audit and permissions check for some IPC_XXX cmd and is called from semctl_down, shmctl_down and msgctl_down. It must be called without any lock held and - retrieves the ipc with the given id in the given table. - performs some audit and permission check, depending on the given cmd - returns a pointer to the ipc object or otherwise, the corresponding error. 

 Call holding the both the rwsem and the rcu read lock.

<h2>Copyright</h2>


