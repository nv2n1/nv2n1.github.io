---
title: "libdspam(3)"
name: "libdspam"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libdspam/"
description: "libdspam – Core message processing and classification library for DSPAM"
---

<h2 class="name">NAME</h2>
<p> libdspam &#8211; Core message processing and classification library for DSPAM </p>
<p> <code>DSPAM</code> Core Analyis Engine Functions</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libdspam.h&gt;
DSPAM_CTX *dspam_init(const char *username, const char *group,
                      const char *home, int operating_mode, u_int32_t flags);
DSPAM_CTX *dspam_create(const char *username, const char *group,
                        const char *home, int operating_mode, u_int32_t flags);
int dspam_addattribute(DSPAM_CTX *CTX, const char *key,
                       const char *value);
int dspam_clearattributes(DSPAM_CTX *CTX);
int dspam_attach(DSPAM_CTX *CTX, void *dbh);
int dspam_process(DSPAM_CTX *CTX, const char *message);
int dspam_getsource(DSPAM_CTX *CTX, char *buf, size_t size);
int dspam_detach(DSPAM_CTX *CTX);
int dspam_destroy(DSPAM_CTX *CTX);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>libdspam</code> provides core message processing and classification functionality. </p>
<p> The <code>dspam_init()</code> function creates and initializes a new classification context and attaches the context to whatever backend storage facility was configured. The <code>user</code> and <code>group</code> arguments provided are used to read and write information stored for the user and group specified. The <code>home</code> argument is used to configure libdspam&#8217;s storage around the base directory specified. The <code>mode</code> specifies the operating mode to initialize the classification context with and may be one of: </p>
<p>&nbsp;<wbr><code>DSM_PROCESS</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Classify and learn the supplied message using whatever training mode is specified<br />
&nbsp;<wbr><code>DSM_CLASSIFY</code>&nbsp;<wbr>&nbsp;<wbr>Classify the supplied message only;&nbsp;<wbr>do not learn or update any counters.<br />
&nbsp;<wbr><code>DSM_TOOLS</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>No processing, attach to storage only </p>
<p> The <code>flags</code> provided further tune the classification context for a specific function. Multiple flags may be OR&#8217;d together. </p>
<p>&nbsp;<wbr><code>DSF_UNLEARN</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Unlearn the message<br />
&nbsp;<wbr><code>DSF_BIAS</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Assign processor bias to unknown tokens<br />
&nbsp;<wbr><code>DSF_SIGNATURE</code>&nbsp;<wbr>A binary signature is requested/provided<br />
&nbsp;<wbr><code>DSF_NOISE</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Apply Bayesian Noise Reduction logic<br />
&nbsp;<wbr><code>DSF_WHITELIST</code>&nbsp;<wbr>Use automatic whitelisting logic<br />
&nbsp;<wbr><code>DSF_MERGED</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Merge group metadata with user&#8217;s in memory </p>
<p> Upon successful completion, <code>dspam_init()</code> will return a pointer to a new <code>classification context</code> structure containing a copy of the configuration passed into dspam_init(), a connected storage driver handle, and a set of preliminary user control data read from storage. </p>
<p> The <code>dspam_create()</code> function performs in exactly the same manner as the dspam_init() function, but does not attach to storage. Instead, the caller must also call <code>dspam_attach()</code> after setting any storage- specific attributes using <code>dspam_addattribute()</code>. This is useful for cases where the implementor would prefer to configure storage internally rather than having libdspam read a configuration from a file. </p>
<p> The <code>dspam_addattribute()</code> function is called to set attributes within the classification context. Some storage drivers support the use of passing specific attributes such as server connect information. The driver-independent attributes supported by DSPAM include: </p>
<p>&nbsp;<wbr><code>IgnoreHeader</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Specify a specific header to ignore&nbsp;<wbr><br />
&nbsp;<wbr><code>LocalMX</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Specify a local mail exchanger to assist in&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>correct results from&nbsp;<wbr><code>dspam_getsource()</code>. </p>
<p> Only driver-dependent attributes need be set prior to a call to <code>dspam_attach()</code>. Driver-independent attributes may be set both before and after storage has been attached. </p>
<p> The <code>dspam_attach()</code> function attaches the storage interface to the classification context and alternatively established an initial connection with storage if <code>dbh</code> is <code>NULL</code>. Some storage drivers support only a NULL value for dbh, while others (such as mysql_drv, pgsql_drv, and sqlite_drv) allow an open database handle to be attached. This function should only be called after an initial call to <code>dspam_create()</code> and should never be called if using <code>dspam_init()</code>, as storage is automatically attached by a call to dspam_init(). </p>
<p> The <code>dspam_process()</code> function performs analysis of the <code>message</code> passed into it and will return zero on successful completion. If successful, CTX-&gt;result will be set to one of three classification results: </p>
<p>&nbsp;<wbr><code>DSR_ISSPAM</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Message was classified as spam<br />
&nbsp;<wbr><code>DSR_ISINNOCENT</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Message was classified as nonspam<br />
&nbsp;<wbr><code>DSR_ISWHITELISTED</code>&nbsp;<wbr>Recipient was automatically whitelisted </p>
<p> Should the call fail, one of the following errors will be returned: </p>
<p>&nbsp;<wbr><code>EINVAL</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>An invalid call or invalid parameter used.<br />
&nbsp;<wbr><code>EUNKNOWN</code>&nbsp;<wbr>&nbsp;<wbr>Unexpected error, such as malloc()&nbsp;<wbr>failure<br />
&nbsp;<wbr><code>EFILE</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Error opening or writing to a file or file handle<br />
&nbsp;<wbr><code>ELOCK</code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Locking failure<br />
&nbsp;<wbr><code>EFAILURE</code>&nbsp;<wbr>&nbsp;<wbr>The operation itself has failed </p>
<p> The <code>dspam_getsource()</code> function extracts the source sender from the message passed in during a call to <code>dspam_process()</code> and writes not more than <code>size</code> bytes to <code>buf</code>. </p>
<p> The <code>dspam_detach()</code> function can be called when a detachment from storage is desired, but the context is still needed. The storage driver is closed, leaving the classification context in place. Once the context is no longer needed, another call to <code>dspam_destroy()</code> should be made. If you are closing storage and destroying the context at the same time, it is not necessary to call this function. Instead you may call <code>dspam_destroy()</code> directly. </p>
<p> The <code>dspam_clearattributes()</code> function is called to clear any attributes previously set using <code>dspam_addattribute()</code> within the classification context. It is necessary to call this function prior to replacing any attributes already written. </p>
<p> The <code>dspam_destroy()</code> function should be called when the context is no longer needed. If a connection was established to storage internally, the connection is closed and all data is flushed and written. If a handle was attached, the handle will remain open. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2012 DSPAM Project<br />
 All rights reserved. </p>
<p> For more information, see <a rel="nofollow" href="http://dspam.sourceforge.net.">http://dspam.sourceforge.net.</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dspam/">dspam</a></code>(1), <code><a href="/docs/linux/man/1-dspam_admin/">dspam_admin</a></code>(1), <code><a href="/docs/linux/man/1-dspam_clean/">dspam_clean</a></code>(1), <code><a href="/docs/linux/man/1-dspam_crc/">dspam_crc</a></code>(1), <code><a href="/docs/linux/man/1-dspam_dump/">dspam_dump</a></code>(1), <code><a href="/docs/linux/man/1-dspam_logrotate/">dspam_logrotate</a></code>(1), <code><a href="/docs/linux/man/1-dspam_merge/">dspam_merge</a></code>(1), <code><a href="/docs/linux/man/1-dspam_stats/">dspam_stats</a></code>(1), <code><a href="/docs/linux/man/1-dspam_train/">dspam_train</a></code>(1) </p>
<h2>Index</h2>
