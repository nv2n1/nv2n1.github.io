---
title: "pmix_init(3)"
name: "pmix_init"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmix_init/"
---

PMIx_Init - Initialize the PMIx Client

<h2>Synopsis</h2>

<pre><code>#include &lt;pmix.h&gt;

pmix_status_t PMIx_Init(pmix_proc_t *proc);</code></pre>

<h2>Arguments</h2>

proc : Pointer to a pmix_proc_t object in which the client's namespace and rank are to be returned.

<h2>Description</h2>

Initialize the PMIx client, returning the process identifier assigned to this client's application in the provided pmix_proc_t struct. Passing a parameter of NULL for this parameter is allowed if the user wishes solely to initialize the PMIx system and does not require return of the identifier at that time. 

 When called, the PMIx client will check for the required connection information of the local PMIx server and will establish the connection. If the information is not found, or the server connection fails, then an appropriate error constant will be returned. 

 If successful, the function will return PMIX_SUCCESS and will fill the provided structure with the server-assigned namespace and rank of the process within the application. 

 Note that the PMIx client library is referenced counted, and so multiple calls to PMIx_Init are allowed. Thus, one way to obtain the namespace and rank of the process is to simply call PMIx_Init with a non-NULL parameter.

<h2>Return Value</h2>

Returns PMIX_SUCCESS on success. On error, a negative value corresponding to a PMIx errno is returned.

<h2>Errors</h2>

PMIx errno values are defined in pmix_common.h.

<h2>Notes</h2>



<h2>See Also</h2>



<h2>Authors</h2>

PMIx.
