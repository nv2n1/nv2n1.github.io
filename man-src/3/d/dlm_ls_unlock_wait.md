---
title: "dlm_ls_unlock_wait(3)"
name: "dlm_ls_unlock_wait"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlm_ls_unlock_wait/"
description: "dlm_unlock – unlock a DLM lock"
---

<h2>NAME</h2>
<p> dlm_unlock &#8211; unlock a DLM lock</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libdlm.h&gt;
int dlm_unlock(uint32_t lkid,
               uint32_t flags, struct dlm_lksb *lksb, void *astarg);
int dlm_unlock_wait(uint32_t lkid,
                    uint32_t flags, struct dlm_lksb *lksb);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>dlm_unlock()</code> unlocks a lock previously acquired by dlm_lock and its variants. </p>
<p> Unless <code>dlm_unlock_wait() </code> is used unlocks are also asynchronous. The AST routine is called when the resource is successfully unlocked (see below). </p>
<p> <code>lkid</code> Lock ID as returned in the lksb </p>
<p> <code>flags</code> flags affecting the unlock operation: </p>
<pre>
  LKF_CANCEL       Cancel a pending lock or conversion. 
                   This returns the lock to it's previously
                   granted mode (in case of a conversion) or
                   unlocks it (in case of a waiting lock).
  LKF_IVVALBLK     Invalidate value block
  LKF_FORCEUNLOCK  Unlock the lock even if it's waiting.
</pre>
<p> <code>lksb</code> LKSB to return status and value block information. </p>
<p> <code>astarg</code> New parameter to be passed to the completion AST. The completion AST routine is the last completion AST routine specified in a dlm_lock call. If dlm_lock_wait() was the last routine to issue a lock, dlm_unlock_wait() must be used to release the lock. If dlm_lock() was the last routine to issue a lock then either dlm_unlock() or dlm_unlock_wait() may be called. </p>
<h3>Return values</h3>
<p> 0 is returned if the call completed successfully. If not, -1 is returned and errno is set to one of the following: </p>
<pre>
EINVAL          An invalid parameter was passed to the call (eg bad
                lock mode or flag)
EINPROGRESS     The lock is already being unlocked
EBUSY           The lock is currently being locked or converted
ENOTEMPTY       An attempt to made to unlock a parent lock that still has
                child locks.
ECANCEL         A lock conversion was successfully cancelled
EUNLOCK         An unlock operation completed successfully
                (sb_status only)
EFAULT          The userland buffer could not be read/written by the
                kernel
</pre>
<p> If an error is returned in the AST, then lksb.sb_status is set to the one of the above numbers instead of zero.</p>
<h2>EXAMPLE</h2>
<pre><code>
int status;
struct dlm_lksb lksb;
status = dlm_lock_wait(LKM_EXMODE,
                       &amp;lksb,
                       LKF_NOQUEUE,
                       "MyLock",
                       strlen("MyLock"),
                       0,     // Parent,
                       NULL,  // bast arg
                       NULL,  // bast routine,
                       NULL); // Range
if (status == 0)
    dlm_unlock_wait(lksb.sb_lkid, 0, &amp;lksb);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libdlm/">libdlm</a></code>(3), <code><a href="/docs/linux/man/3-dlm_lock/">dlm_lock</a></code>(3), <code><a href="/docs/linux/man/3-dlm_open_lockspace/">dlm_open_lockspace</a></code>(3), <code><a href="/docs/linux/man/3-dlm_create_lockspace/">dlm_create_lockspace</a></code>(3), <code><a href="/docs/linux/man/3-dlm_close_lockspace/">dlm_close_lockspace</a></code>(3), <code><a href="/docs/linux/man/3-dlm_release_lockspace/">dlm_release_lockspace</a></code>(3) </p>
<h2>Index</h2>
