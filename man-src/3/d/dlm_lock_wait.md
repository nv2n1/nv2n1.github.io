---
title: "dlm_lock_wait(3)"
name: "dlm_lock_wait"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlm_lock_wait/"
description: "dlm_lock – acquire or convert a DLM lock"
---

<h2>NAME</h2>
<p> dlm_lock &#8211; acquire or convert a DLM lock</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libdlm.h&gt;
int dlm_lock(uint32_t mode,
             struct dlm_lksb *lksb,
             uint32_t flags,
             const void *name,
             unsigned int namelen,
             uint32_t parent, /* unused */
             void (*astaddr)(void *astarg),
             void *astarg,
             void (*bastaddr)(void *astarg),
             void *range); /* unused */
int dlm_lock_wait(uint32_t mode,
                  struct dlm_lksb *lksb,
                  uint32_t flags,
                  const void *name,
                  unsigned int namelen,
                  uint32_t parent, /* unused */
                  void *bastarg,
                  void (*bastaddr)(void *bastarg),
                  void *range); /* unused */
int dlm_ls_lock(dlm_lshandle_t lockspace,
                uint32_t mode,
                struct dlm_lksb *lksb,
                uint32_t flags,
                const void *name,
                unsigned int namelen,
                uint32_t parent, /* unused */
                void (*astaddr)(void *astarg),
                void *astarg,
                void (*bastaddr)(void *astarg),
                void *range); /* unused */
int dlm_ls_lock_wait(dlm_lshandle_t lockspace,
                     uint32_t mode,
                     struct dlm_lksb *lksb,
                     uint32_t flags,
                     const void *name,
                     unsigned int namelen,
                     uint32_t parent, /* unusued */
                     void *bastarg,
                     void (*bastaddr)(void *bastarg),
                     void *range); /* unused */
int dlm_ls_lockx(dlm_lshandle_t lockspace,
                 uint32_t mode,
                 struct dlm_lksb *lksb,
                 uint32_t flags,
                 const void *name,
                 unsigned int namelen,
                 uint32_t parent, /* unused */
                 (*astaddr)(void *astarg),
                 void *astarg,
                 void (*bastaddr)(void *astarg),
                 uint64_t *xid,
                 uint64_t *timeout);
</code></pre>
<h2>DESCRIPTION</h2>
<p> dlm_lock and its variants acquire and convert locks in the DLM. </p>
<p> dlm_lock() operations are asynchronous. If the call to dlm_lock returns an error then the operation has failed and the AST routine will not be called. If dlm_lock returns 0 it is still possible that the lock operation will fail. The AST routine will be called when the locking is complete or has failed and the status is returned in the lksb. <code>dlm_lock_wait()</code> will wait until the lock operation has completed and returns the final completion status. <code>dlm_ls_lock()</code> is the same as <code>dlm_lock()</code> but takes a lockspace argument. This lockspace must have been previously opened by <code>dlm_lockspace_open() or</code> <code>dlm_lockspace_create().</code> </p>
<p> For conversion operations the name and namelen are ignored and the lock ID in the LKSB is used to identify the lock to be converted. </p>
<p> If a lock value block is specified then in general, a grant or a conversion to an equal-level or higher-level lock mode reads the lock value from the resource into the caller&#8217;s lock value block. When a lock conversion from EX or PW to an equal-level or lower-level lock mode occurs, the contents of the caller&#8217;s lock value block are written into the resource. If the LVB is invalidated the lksb.sb_flags member will be set to DLM_SBF_VALNOTVALID. Lock values blocks are always 32 bytes long. </p>
<p> If the AST routines or parameter are passed to a conversion operation then they will overwrite those values that were passed to a previous dlm_lock call. </p>
<p> <code>mode</code> Lock mode to acquire or convert to. </p>
<pre>
  LKM_NLMODE    NULL Lock
  LKM_CRMODE    Concurrent read
  LKM_CWMODE    Concurrent write
  LKM_PRMODE    Protected read
  LKM_PWMODE    Protected write
  LKM_EXMODE    Exclusive
</pre>
<p> <code>flags</code> Affect the operation of the lock call:<br />
LKF_NOQUEUE Don&#8217;t queue the lock. If it cannot be granted return &#8211; EAGAIN<br />
                                                                       LKF_CONVERT Convert an existing lock<br />
                                                                           LKF_VALBLK Lock has a value block<br />
                                                                               LKF_QUECVT Put conversion to the back of the queue<br />
                                                                                   LKF_EXPEDITE Grant a NL lock immediately regardless of other locks<br />
                                                                                       on the conversion queue<br />
                                                                                           LKF_PERSISTENT Specifies a lock that will not be unlocked when the<br />
                                                                                               process exits; it will become an orphan lock.<br />
  LKF_CONVDEADLK  Enable internal conversion deadlock resolution where<br />
                  the lock&#8217;s granted mode may be set to NL and<br />
                  DLM_SBF_DEMOTED is returned in lksb.sb_flags.<br />
  LKF_NODLCKWT    Do not consider this lock when trying to detect<br />
                  deadlock conditions.<br />
  LKF_NODLCKBLK   Not implemented<br />
  LKF_NOQUEUEBAST Send blocking ASTs even for NOQUEUE operations<br />
  LKF_HEADQUE     Add locks to the head of the convert or waiting queue<br />
  LKF_NOORDER     Avoid the VMS rules on grant order<br />
  LKF_ALTPR       If the requested mode can&#8217;t be granted (generally CW),<br />
                  try to grant in PR and return DLM_SBF_ALTMODE.<br />
  LKF_ALTCW       If the requested mode can&#8217;t be granted (generally PR),<br />
                  try to grant in CW and return DLM_SBF_ALTMODE.<br />
  LKF_TIMEOUT     The lock will time out per the timeout arg.</p>
<p> <code>lksb</code> Lock Status block<br />
 This structure contains the returned lock ID, the actual status of the lock operation (all lock ops are asynchronous) and the value block if LKF_VALBLK is set. </p>
<p> <code>name</code><br />
 Name of the lock. Can be binary, max 64 bytes. Ignored for lock conversions. (Should be a string to work with debugging tools.) </p>
<p> <code>namelen<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code><br />
 Length of the above name. Ignored for lock conversions.</p>
<p> <code>parent<tt>&nbsp;<wbr></tt></code><br />
 ID of parent lock or NULL if this is a top-level lock. This is currently unused.</p>
<p> <code>ast<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code><br />
 Address of AST routine to be called when the lock operation<br />
 completes. The final completion status of the lock will be in the lksb. the AST routine must not be NULL. </p>
<p> <code>astargs<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></code><br />
 Argument to pass to the AST routine (most people pass the lksb<br />
 in here but it can be anything you like.) </p>
<p> <code>bast</code><br />
 Blocking AST routine. address of a function to call if this lock is blocking another. The function will be called with astargs. </p>
<p> <code>range</code><br />
 This is unused. </p>
<p> <code>xid</code><br />
 Optional transaction ID for deadlock detection. </p>
<p> <code>timeout</code><br />
 Timeout in centiseconds. If it takes longer than this to acquire the lock (usually because it is already blocked by another lock), then the AST will trigger with ETIMEDOUT as the status. If the lock operation is a conversion then the lock will remain at its current status. If this is a new lock then the lock will not exist and any LKB in the lksb will be invalid. This is ignored without the LKF_TIMEOUT flag. </p>
<h3>Return values</h3>
<p> 0 is returned if the call completed successfully. If not, -1 is returned and errno is set to one of the following: </p>
<pre>
EINVAL          An invalid parameter was passed to the call (eg bad lock
                mode or flag)
ENOMEM          A (kernel) memory allocation failed
EAGAIN          LKF_NOQUEUE was requested and the lock could not be
                granted
EBUSY           The lock is currently being locked or converted
EFAULT          The userland buffer could not be read/written by the
                kernel (this indicates a library problem)
EDEADLOCK       The lock operation is causing a deadlock and has been
                cancelled. If this was a conversion then the lock is
                reverted to its previously granted state. If it was a
                new lock then it has not been granted. (NB Only
                conversion deadlocks are currently detected)
If an error is returned in the AST, then lksb.sb_status is set to the one of the above values instead of zero.
</pre>
<h3>Structures</h3>
<p>struct dlm_lksb {<br />
    int sb_status;    /* Final status of lock operation */<br />
    uint32_t sb_lkid; /* ID of lock. Returned from dlm_lock()<br />
                         on first use. Used as input to<br />
                         dlm_lock() for a conversion operation */<br />
    char sb_flags;    /* Completion flags, see above */<br />
    char sb_lvbptr;   /* Optional pointer to lock value block */<br />
};</p>
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
<p> <code><a href="/docs/linux/man/3-libdlm/">libdlm</a></code>(3), <code><a href="/docs/linux/man/3-dlm_unlock/">dlm_unlock</a></code>(3), <code><a href="/docs/linux/man/3-dlm_open_lockspace/">dlm_open_lockspace</a></code>(3), <code><a href="/docs/linux/man/3-dlm_create_lockspace/">dlm_create_lockspace</a></code>(3), <code><a href="/docs/linux/man/3-dlm_close_lockspace/">dlm_close_lockspace</a></code>(3), <code><a href="/docs/linux/man/3-dlm_release_lockspace/">dlm_release_lockspace</a></code>(3) </p>
<h2>Index</h2>
