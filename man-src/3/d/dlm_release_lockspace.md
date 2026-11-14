---
title: "dlm_release_lockspace(3)"
name: "dlm_release_lockspace"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlm_release_lockspace/"
description: "dlm_create_lockspace, dlm_open_lockspace, dlm_close_lockspace, dlm_release_lockspace – manipulate DLM lockspaces"
---

<h2>NAME</h2>
<p> dlm_create_lockspace, dlm_open_lockspace, dlm_close_lockspace, dlm_release_lockspace &#8211; manipulate DLM lockspaces</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libdlm.h&gt;
dlm_lshandle_t dlm_create_lockspace(const char *name, mode_t mode);
dlm_lshandle_t dlm_new_lockspace(const char *name, mode_t mode,
                                 uint32_t flags);
dlm_lshandle_t dlm_open_lockspace(const char *name);
int dlm_close_lockspace(dlm_lshandle_t ls);
int dlm_release_lockspace(const char *name, dlm_lshandle_t ls,
                          int force);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The DLM allows locks to be partitioned into &quot;lockspaces&quot;, and these can be manipulated by userspace calls. It is possible (though not recommended) for an application to have multiple lockspaces open at one time. </p>
<p> Many of the DLM calls work on the &quot;default&quot; lockspace, which should be fine for most users. The calls with _ls_ in them allow you to isolate your application from all others running in the cluster. Remember, lockspaces are a cluster-wide resource, so if you create a lockspace called &quot;myls&quot; it will share locks with a lockspace called &quot;myls&quot; on all nodes. These calls allow users to create &amp; remove lockspaces, and users to connect to existing lockspace to store their locks there. </p>
<h3>dlm_lshandle_t dlm_create_lockspace(const char *name, mode_t mode);</h3>
<p> This creates a lockspace called &lt;name&gt; and the mode of the file user to access it will be &lt;mode&gt; (subject to umask as usual). The lockspace must not already exist on this node, if it does -1 will be returned and errno will be set to EEXIST. If you really want to use this lockspace you can then use dlm_open_lockspace() below. The name is the name of a misc device that will be created in /dev/misc.<br />
 On success a handle to the lockspace is returned, which can be used to pass into subsequent dlm_ls_lock/unlock calls. Make no assumptions as to the content of this handle as it&#8217;s content may change in future.<br />
 The caller must have CAP_SYSADMIN privileges to do this operation. </p>
<p> Return codes: 0 is returned if the call completed successfully. If not, -1 is returned and errno is set to one of the following: </p>
<pre>
EINVAL          An invalid parameter was passed to the call
ENOMEM          A (kernel) memory allocation failed
EEXIST          The lockspace already exists
EPERM           Process does not have capability to create lockspaces
ENOSYS          A fatal error occurred initializing the DLM
Any error returned by the open() system call
</pre>
<h3>int dlm_new_lockspace(const char *name, mode_t mode, uint32_t flags)</h3>
<p> Performs the same function as <code>dlm_create_lockspace()</code> above, but passes some creation flags to the call that affect the lockspace being created. Currently supported flags are: </p>
<pre>
DLM_LSFL_TIMEWARN the dlm should emit warnings over netlink when locks
                  have been waiting too long; required for deadlock
                  detection
</pre>
<h3>int dlm_release_lockspace(const char *name, dlm_lshandle_t ls, int force)</h3>
<p> Deletes a lockspace. If the lockspace still has active locks then -1 will be returned and errno set to EBUSY. Both the lockspace handle /and/ the name must be specified. This call also closes the lockspace and stops the thread associated with the lockspace, if any.<br />
 Note that other nodes in the cluster may still have locks open on this lockspace. This call only removes the lockspace from the current node. If the force flag is set then the lockspace will be removed even if another user on this node has active locks in it. Existing users will NOT be notified if you do this, so be careful.<br />
 The caller must have CAP_SYSADMIN privileges to do this operation. </p>
<p> Return codes: 0 is returned if the call completed successfully. If not, -1 is returned and errno is set to one of the following: </p>
<pre>
EINVAL          An invalid parameter was passed to the call
EPERM           Process does not have capability to release lockspaces
EBUSY           The lockspace could not be freed because it still
                contains locks and force was not set.
</pre>
<h3>dlm_lshandle_t dlm_open_lockspace(const char *name)</h3>
<p> Opens an already existing lockspace and returns a handle to it. </p>
<p> Return codes: 0 is returned if the call completed successfully. If not, -1 is returned and errno is set to an error returned by the open() system call</p>
<h3>int dlm_close_lockspace(dlm_lshandle_t ls)</h3>
<p> Close the lockspace. Any locks held by this process will be freed. If a thread is associated with this lockspace then it will be stopped. </p>
<p> Return codes: 0 is returned if the call completed successfully. If not, -1 is returned and errno is set to one of the following: </p>
<pre>
EINVAL          lockspace was not a valid lockspace handle
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libdlm/">libdlm</a></code>(3), <code><a href="/docs/linux/man/3-dlm_unlock/">dlm_unlock</a></code>(3), <code><a href="/docs/linux/man/3-dlm_lock/">dlm_lock</a></code>(3), </p>
<h2>Index</h2>
