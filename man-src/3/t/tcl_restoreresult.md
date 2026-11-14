---
title: "tcl_restoreresult(3)"
name: "tcl_restoreresult"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_restoreresult/"
description: "Tcl_SaveInterpState, Tcl_RestoreInterpState, Tcl_DiscardInterpState, Tcl_SaveResult, Tcl_RestoreResult, Tcl_DiscardResult – save and restore an interpreter’s state"
---

<p>Tcl_SaveInterpState, Tcl_RestoreInterpState, Tcl_DiscardInterpState, Tcl_SaveResult, Tcl_RestoreResult, Tcl_DiscardResult &#8211; save and restore an interpreter&#8217;s state </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_InterpState
<code>Tcl_SaveInterpState</code>(<i>interp, status</i>)
int
<code>Tcl_RestoreInterpState</code>(<i>interp, state</i>)
<code>Tcl_DiscardInterpState</code>(<i>state</i>)
<code>Tcl_SaveResult</code>(<i>interp, savedPtr</i>)
<code>Tcl_RestoreResult</code>(<i>interp, savedPtr</i>)
<code>Tcl_DiscardResult</code>(<i>savedPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter for which state should be saved.</p>
<dd>int <i>status</i> (in) Return code value to save as part of interpreter state.</p>
<dd>Tcl_InterpState <i>state</i> (in) Saved state token to be restored or discarded.</p>
<dd>Tcl_SavedResult <i>*savedPtr</i> (in) Pointer to location where interpreter result should be saved or restored. </p>
</dl>
<h2>Description</h2>
<p>These routines allows a C procedure to take a snapshot of the current state of an interpreter so that it can be restored after a call to <code>Tcl_Eval</code> or some other routine that modifies the interpreter state. There are two triplets of routines meant to work together. </p>
<p> The first triplet stores the snapshot of interpreter state in an opaque token returned by <code>Tcl_SaveInterpState</code>. That token value may then be passed back to one of <code>Tcl_RestoreInterpState</code> or <code>Tcl_DiscardInterpState</code>, depending on whether the interp state is to be restored. So long as one of the latter two routines is called, Tcl will take care of memory management. </p>
<p> The second triplet stores the snapshot of only the interpreter result (not its complete state) in memory allocated by the caller. These routines are passed a pointer to a <code>Tcl_SavedResult</code> structure that is used to store enough information to restore the interpreter result. This structure can be allocated on the stack of the calling procedure. These routines do not save the state of any error information in the interpreter (e.g. the <code>-errorcode</code> or <code>-errorinfo</code> return options, when an error is in progress). </p>
<p> Because the routines <code>Tcl_SaveInterpState</code>, <code>Tcl_RestoreInterpState</code>, and <code>Tcl_DiscardInterpState</code> perform a superset of the functions provided by the other routines, any new code should only make use of the more powerful routines. The older, weaker routines <code>Tcl_SaveResult</code>, <code>Tcl_RestoreResult</code>, and <code>Tcl_DiscardResult</code> continue to exist only for the sake of existing programs that may already be using them. </p>
<p> <code>Tcl_SaveInterpState</code> takes a snapshot of those portions of interpreter state that make up the full result of script evaluation. This include the interpreter result, the return code (passed in as the <i>status</i> argument, and any return options, including <code>-errorinfo</code> and <code>-errorcode</code> when an error is in progress. This snapshot is returned as an opaque token of type <code>Tcl_InterpState</code>. The call to <code>Tcl_SaveInterpState</code> does not itself change the state of the interpreter. Unlike <code>Tcl_SaveResult</code>, it does not reset the interpreter. </p>
<p> <code>Tcl_RestoreInterpState</code> accepts a <code>Tcl_InterpState</code> token previously returned by <code>Tcl_SaveInterpState</code> and restores the state of the interp to the state held in that snapshot. The return value of <code>Tcl_RestoreInterpState</code> is the status value originally passed to <code>Tcl_SaveInterpState</code> when the snapshot token was created. </p>
<p> <code>Tcl_DiscardInterpState</code> is called to release a <code>Tcl_InterpState</code> token previously returned by <code>Tcl_SaveInterpState</code> when that snapshot is not to be restored to an interp. </p>
<p> The <code>Tcl_InterpState</code> token returned by <code>Tcl_SaveInterpState</code> must eventually be passed to either <code>Tcl_RestoreInterpState</code> or <code>Tcl_DiscardInterpState</code> to avoid a memory leak. Once the <code>Tcl_InterpState</code> token is passed to one of them, the token is no longer valid and should not be used anymore. </p>
<p> <code>Tcl_SaveResult</code> moves the string and object results of <i>interp</i> into the location specified by <i>statePtr</i>. <code>Tcl_SaveResult</code> clears the result for <i>interp</i> and leaves the result in its normal empty initialized state. </p>
<p> <code>Tcl_RestoreResult</code> moves the string and object results from <i>statePtr</i> back into <i>interp</i>. Any result or error that was already in the interpreter will be cleared. The <i>statePtr</i> is left in an uninitialized state and cannot be used until another call to <code>Tcl_SaveResult</code>. </p>
<p> <code>Tcl_DiscardResult</code> releases the saved interpreter state stored at <code>statePtr</code>. The state structure is left in an uninitialized state and cannot be used until another call to <code>Tcl_SaveResult</code>. </p>
<p> Once <code>Tcl_SaveResult</code> is called to save the interpreter result, either <code>Tcl_RestoreResult</code> or <code>Tcl_DiscardResult</code> must be called to properly clean up the memory associated with the saved state. </p>
<h2>Keywords</h2>
<p>result, state, interp</p>
