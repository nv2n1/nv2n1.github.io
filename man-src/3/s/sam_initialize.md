---
title: "sam_initialize(3)"
name: "sam_initialize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_initialize/"
description: "sam_initialize – Initialize health checking"
---
<p>sam_initialize &#8211; Initialize health checking  </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/sam.h&gt;</code> </p>
<p> <code>cs_error_t sam_initialize (int</code> <i>time_interval</i><code>, sam_recovery_policy_t </code><i>recovery_policy</i>); </p>
<h2>DESCRIPTION</h2>
<p>The <code>sam_initialize</code> function is used to initialize health checking of a process. </p>
<p>Application can have only one instance of SAM. This function must be called before any other of SAM functions. It is recommended to initialize before the process begins any process initialization. </p>
<p>The <i>time_interval</i> parameter is a timeout in milliseconds before taking recovery action after having not received a healthcheck. </p>
<p>If <i>time_interval</i> parameter is zero, there is no time limit and no healthcheck must be sent by the process. In this operational mode, a process failure will continue to execute the recovery policy. </p>
<p>The <i>recovery_policy</i> is defined as type: </p>
<pre><code>  typedef enum {
        SAM_RECOVERY_POLICY_QUIT = 1,
        SAM_RECOVERY_POLICY_RESTART = 2,
        SAM_RECOVERY_POLICY_QUORUM = 0x08,
        SAM_RECOVERY_POLICY_QUORUM_QUIT = SAM_RECOVERY_POLICY_QUORUM | SAM_RECOVERY_POLICY_QUIT,
        SAM_RECOVERY_POLICY_QUORUM_RESTART = SAM_RECOVERY_POLICY_QUORUM | SAM_RECOVERY_POLICY_RESTART,
        SAM_RECOVERY_POLICY_CMAP = 0x10,
        SAM_RECOVERY_POLICY_CONFDB = 0x10,
  } sam_recovery_policy_t;
</code></pre>
<p>where </p>
<dl>
<dt>SAM_RECOVERY_POLICY_QUIT</dt>
<dd> <p> on failure, the process will terminate. </p>
 </dd>
<dt>SAM_RECOVERY_POLICY_RESTART</dt>
<dd> <p> on failure, the process will restart. </p>
 </dd>
<dt>SAM_RECOVERY_POLICY_QUORUM</dt>
<dd> <p> is not policy. Used only as flag meaning quorum integration </p>
 </dd>
<dt>SAM_RECOVERY_POLICY_QUORUM_QUIT</dt>
<dd> <p> same as <i>SAM_RECOVERY_POLICY_QUIT</i> but <code>sam_start (3)</code> will block until corosync becomes quorate and process will be terminated if quorum is lost. </p>
 </dd>
<dt>SAM_RECOVERY_POLICY_QUORUM_RESTART</dt>
<dd> <p> same as <i>SAM_RECOVERY_POLICY_RESTART</i> but <code>sam_start (3)</code> will block until corosync becomes quorate and process will be restarted if quorum is lost. </p>
 </dd>
<dt>SAM_RECOVERY_POLICY_CMAP</dt>
<dd> <p> is not policy. Used only as flag meaning cmap integration. It can be used with all previous policies. For backward compatibility, SAM_RECOVERY_POLICY_CONFDB with same meaning as <i>SAM_RECOVERY_POLICY_CMAP</i> is also provided. </p>
 </dd></dl>
<p>To perform event driven healthchecking, <code><a href="/docs/linux/man/3-sam_register/">sam_register</a>(3)</code> and <code><a href="/docs/linux/man/3-sam_start/">sam_start</a>(3)</code> functions must called. Event driven healthchecking causes the duplicate standby process running the SAM serve rto periodically request healthchecks from the active process. </p>
<h2>RETURN VALUE</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>ERRORS</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</dt>
<dd> <p> can happened in case of double initialization. </p>
 </dd>
<dt>CS_ERR_INVALID_PARAM</dt>
<dd> <p> <i>recovery_policy</i> has invalid value. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-sam_register/">sam_register</a></code>(3), <code><a href="/docs/linux/man/3-sam_start/">sam_start</a></code>(3), <code><a href="/docs/linux/man/3-sam_hc_callback_register/">sam_hc_callback_register</a></code>(3) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">RETURN VALUE</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">ERRORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">SEE ALSO</a></dt>
<dd>  </dd></dl>
