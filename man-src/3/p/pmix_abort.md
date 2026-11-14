---
title: "pmix_abort(3)"
name: "pmix_abort"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmix_abort/"
---

PMIx_Abort - Abort the specified processes

<h2>Synopsis</h2>

<pre><code>#include &lt;pmix.h&gt;

pmix_status_t PMIx_Abort(int status, const char msg[],
                         pmix_proc_t procs[], size_t nprocs);</code></pre>

<h2>Arguments</h2>

status : Status value to be returned. A value of zero is permitted by PMIx, but may not be returned by some resource managers. 

 msg : A string message to be displayed 

 procs : An array of pmix_proc_t structures defining the processes to be aborted. A NULL for the proc array indicates that all processes in the caller's nspace are to be aborted. A wildcard value for the rank in any structure indicates that all processes in that nspace are to be aborted. 

 nprocs : Number of pmix_proc_t structures in the procs array

<h2>Description</h2>

Request that the provided array of procs be aborted, returning the provided status and printing the provided message. A NULL for the proc array indicates that all processes in the caller's nspace are to be aborted. 

 The response to this request is somewhat dependent on the specific resource manager and its configuration (e.g., some resource managers will not abort the application if the provided status is zero unless specifically configured to do so), and thus lies outside the control of PMIx itself. However, the client will inform the RM of the request that the application be aborted, regardless of the value of the provided status. 

 Passing a NULL msg parameter is allowed. Note that race conditions caused by multiple processes calling PMIx_Abort are left to the server implementation to resolve with regard to which status is returned and what messages (if any) are printed.

<h2>Return Value</h2>

Returns PMIX_SUCCESS on success. On error, a negative value corresponding to a PMIx errno is returned.

<h2>Errors</h2>

PMIx errno values are defined in pmix_common.h.

<h2>Notes</h2>



<h2>See Also</h2>



<h2>Authors</h2>

PMIx.
