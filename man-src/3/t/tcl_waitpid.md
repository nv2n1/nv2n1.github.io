---
title: "tcl_waitpid(3)"
name: "tcl_waitpid"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_waitpid/"
description: "Tcl_DetachPids, Tcl_ReapDetachedProcs, Tcl_WaitPid – manage child processes in background"
---

<p>Tcl_DetachPids, Tcl_ReapDetachedProcs, Tcl_WaitPid &#8211; manage child processes in background </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_DetachPids</code>(<i>numPids, pidPtr</i>)
<code>Tcl_ReapDetachedProcs</code>()
Tcl_Pid
<code>Tcl_WaitPid</code>(<i>pid, statusPtr, options</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>numPids</i> (in) Number of process ids contained in the array pointed to by <i>pidPtr</i>.</p>
<dd>int <i>*pidPtr</i> (in) Address of array containing <i>numPids</i> process ids.</p>
<dd>Tcl_Pid <i>pid</i> (in) The id of the process (pipe) to wait for.</p>
<dd>int <i>*statusPtr</i> (out) The result of waiting on a process (pipe). Either 0 or ECHILD.</p>
<dd>int <i>options</i> (in) The options controlling the wait. WNOHANG specifies not to wait when checking the process.
</dl>
<h2>Description</h2>
<p><code>Tcl_DetachPids</code> and <code>Tcl_ReapDetachedProcs</code> provide a mechanism for managing subprocesses that are running in background. These procedures are needed because the parent of a process must eventually invoke the <code>waitpid</code> kernel call (or one of a few other similar kernel calls) to wait for the child to exit. Until the parent waits for the child, the child&#8217;s state cannot be completely reclaimed by the system. If a parent continually creates children and doesn&#8217;t wait on them, the system&#8217;s process table will eventually overflow, even if all the children have exited. </p>
<p> <code>Tcl_DetachPids</code> may be called to ask Tcl to take responsibility for one or more processes whose process ids are contained in the <i>pidPtr</i> array passed as argument. The caller presumably has started these processes running in background and does not want to have to deal with them again. </p>
<p> <code>Tcl_ReapDetachedProcs</code> invokes the <code>waitpid</code> kernel call on each of the background processes so that its state can be cleaned up if it has exited. If the process has not exited yet, <code>Tcl_ReapDetachedProcs</code> does not wait for it to exit; it will check again the next time it is invoked. Tcl automatically calls <code>Tcl_ReapDetachedProcs</code> each time the <code>exec</code> command is executed, so in most cases it is not necessary for any code outside of Tcl to invoke <code>Tcl_ReapDetachedProcs</code>. However, if you call <code>Tcl_DetachPids</code> in situations where the <code>exec</code> command may never get executed, you may wish to call <code>Tcl_ReapDetachedProcs</code> from time to time so that background processes can be cleaned up. </p>
<p> <code>Tcl_WaitPid</code> is a thin wrapper around the facilities provided by the operating system to wait on the end of a spawned process and to check a whether spawned process is still running. It is used by <code>Tcl_ReapDetachedProcs</code> and the channel system to portably access the operating system. </p>
<h2>Keywords</h2>
<p>background, child, detach, process, wait</p>
