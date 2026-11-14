---
title: "sam_initialize(3)"
name: "sam_initialize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_initialize/"
description: "sam_initialize – Initialize health checking"
---

<p>sam_initialize &#8211; Initialize health checking</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_initialize (int</code> <i>time_interval</i><code>, sam_recovery_policy_t </code><i>recovery_policy</i>); </p>
<h2>Description</h2>
<p>The <code>sam_initialize</code> function is used to initialize health checking of a process. Application can have only one instance of SAM. This function must be called before any other of SAM functions. It is recommended to initialize before the process begins any process initialization. The <i>time_interval</i> parameter is a timeout in milliseconds before taking recovery action after having not received a healthcheck. If <i>time_interval</i> parameter is zero, there is no time limit and no healthcheck must be sent by the process. In this operational mode, a process failure will continue to execute the recovery policy. The <i>recovery_policy</i> is defined as type:  where</p>
<dl>
<dt>SAM_RECOVERY_POLICY_QUIT</p>
<dd>on failure, the process will terminate.</p>
<dt>SAM_RECOVERY_POLICY_RESTART</p>
<dd>on failure, the process will restart.</p>
<dt>SAM_RECOVERY_POLICY_QUORUM</p>
<dd>is not policy. Used only as flag meaning quorum integration</p>
<dt>SAM_RECOVERY_POLICY_QUORUM_QUIT</p>
<dd>same as <i>SAM_RECOVERY_POLICY_QUIT</i> but <code>sam_start (3)</code> will block until corosync becomes quorate and process will be terminated if quorum is lost.</p>
<dt>SAM_RECOVERY_POLICY_QUORUM_RESTART</p>
<dd>same as <i>SAM_RECOVERY_POLICY_RESTART</i> but <code>sam_start (3)</code> will block until corosync becomes quorate and process will be restarted if quorum is lost.</p>
<dt>SAM_RECOVERY_POLICY_CMAP</p>
<dd>is not policy. Used only as flag meaning cmap integration. It can be used with all previous policies. For backward compatibility, SAM_RECOVERY_POLICY_CONFDB with same meaning as <i>SAM_RECOVERY_POLICY_CMAP</i> is also provided.  To perform event driven healthchecking, <code><a href="/docs/linux/man/3-sam_register/">sam_register</a>(3)</code> and <code><a href="/docs/linux/man/3-sam_start/">sam_start</a>(3)</code> functions must called. Event driven healthchecking causes the duplicate standby process running the SAM serve rto periodically request healthchecks from the active process. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>can happened in case of double initialization.</p>
<dt>CS_ERR_INVALID_PARAM</p>
<dd><i>recovery_policy</i> has invalid value. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_register/">sam_register</a></code>(3), <code><a href="/docs/linux/man/3-sam_start/">sam_start</a></code>(3), <code><a href="/docs/linux/man/3-sam_hc_callback_register/">sam_hc_callback_register</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
