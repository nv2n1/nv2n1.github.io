---
title: "sam_overview(8)"
name: "sam_overview"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sam_overview/"
description: "sam_overview – Overview of the Simple Availability Manager"
---

<p>sam_overview &#8211; Overview of the Simple Availability Manager</p>
<h2>Overview</h2>
<p>The SAM library provide a tool to check the health of an application. The main purpose of SAM is to restart a local process when it fails to respond to a healthcheck request in a configured time interval. </p>
<p> During <code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a>(3)</code>, a duplicate copy of the process is created using the <code><a href="/docs/linux/man/3-fork/">fork</a>(3)</code> system call. This duplicate process copy contains the logic for executing the SAM server. The SAM server is responsible for requesting healthchecks from the active process, and controlling the lifecycle of the active process when it fails. If the active process fails to respond to the healthcheck request sent by the SAM server, it will be sent a user configurable signal (default SIGTERM) to request shutdown of the application. After a configured time interval, the process will be forcibly killed by being sent a SIGKILL signal. Once the active process terminates, the SAM server will create a new active process. </p>
<p> The Simple Availability Manager is meant to be used in conjunction with the cpg service. Used together, it is possible to restart a cpg process that fails healthchecking during operation. </p>
<p> The main features of SAM include: </p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>A configurable recovery policy.</p>
<dt>&bull;</p>
<dd>A configurable time interval for health check operations.</p>
<dt>&bull;</p>
<dd>A notification via signal before recovery action is taken.</p>
<dt>&bull;</p>
<dd>A mechanism to indicate to the application the number of times an active process has been created by the SAM server.</p>
<dt>&bull;</p>
<dd>Both application driven health checking and event driven health checking.</dl>
</dl>
<h2>Initializing SAM</h2>
<p>The SAM library is initialized by <code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a>(3)</code>. <code><a href="/docs/linux/man/3-sam_initalize/">sam_initalize</a>(3)</code> may only be called once per process. Calling it more then once has undefined results and is not recommended or tested.</p>
<h2>Setting warning callback</h2>
<p>User configurable signal (default <i>SIGTERM</i>) is sent to the application when a recovery action is planned. The application can use the <code><a href="/docs/linux/man/3-signal/">signal</a>(3)</code> system call to monitor for this signal. </p>
<p> There are no special constraints on what SAM apis may be called in a warning callback. After <i>time_interval</i> expires, a SIGKILL signal is sent to the active process to force its termination.</p>
<h2>Registering the active process</h2>
<p>The active process is registered with SAM by calling <code><a href="/docs/linux/man/3-sam_register/">sam_register</a>(3)</code>. This function should only be called one time in a process. After a recovery action is taken, the new active process will begin execution at the next line of code in a user process after <code><a href="/docs/linux/man/3-sam_register/">sam_register</a>(3)</code>.</p>
<h2>Enabling event driven healthchecking</h2>
<p>Two types of healthchecking are available to the user. The first model is one where the user application healthchecks during its normal operation. It is never requested to healtcheck, and if the active process doesn&#8217;t respond within the time interval, the process will be restarted. </p>
<p> A more useful mechanism for healthchecking is event driven healthchecking. Because this model is directed by the SAM server, It isn&#8217;t necessary to guess or add timers to the active process to signal a healthcheck operation is successful. To use event driven healthchecking, the <code><a href="/docs/linux/man/3-sam_hc_callback_register/">sam_hc_callback_register</a>(3)</code> function should be executed.</p>
<h2>Quorum integration</h2>
<p>SAM has special policies (<i>SAM_RECOVERY_POLICY_QUIT</i> and <i>SAM_RECOVERY_POLICY_RESTART</i>) for integration with quorum service. This policies changes SAM behaviour in two aspects.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Call of <code><a href="/docs/linux/man/3-sam_start/">sam_start</a>(3)</code> blocks until corosync becomes quorate</p>
<dt>&bull;</p>
<dd>User selected recovery action is taken immediately after lost of quorum.</dl>
</dl>
<h2>Storing user data</h2>
<p>Sometimes there is need to store some data, which survives between instances. One can in such case use files, databases, &#8230; or much simpler in memory solution presented by <code><a href="/docs/linux/man/3-sam_data_store/">sam_data_store</a>(3)</code>, <code><a href="/docs/linux/man/3-sam_data_restore/">sam_data_restore</a>(3)</code> and <code><a href="/docs/linux/man/3-sam_data_getsize/">sam_data_getsize</a>(3)</code> functions.</p>
<h2>Confdb integration</h2>
<p>SAM has policy flag used for confdb system integration (<i>SAM_RECOVERY_POLICY_CONFDB</i>). If process is registered with this flag, new confdb object PROCESS_NAME:PID is created with following keys:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd><i>recovery</i> &#8211; will be quit or restart depending on policy</p>
<dt>&bull;</p>
<dd><i>poll_period</i> &#8211; period of health checking in milliseconds</p>
<dt>&bull;</p>
<dd><i>last_updated</i> &#8211; Timestamp (in nanoseconds) of the last health check.</p>
<dt>&bull;</p>
<dd><i>state</i> &#8211; state of process (can be one of registered, started, failed, waiting for quorum)</dl>
</dl>
<p> Object is automatically deleted if process exits with stopped health checking. </p>
<p> Confdb integration with corosync wathdog can be used in implicit and explicit way. </p>
<p> Implicit way is achieved by setting recovery policy to QUIT and let process exit with started health checking. If this happened, object is not deleted and corosync watchdog will take required action. </p>
<p> Explicit way is useful for situations, when developer can deal with some non-fatal fall of application. This mode is achieved by setting policy to RESTART and using SAM same as without Confdb integration. If real fail is needed (like too many restarts at all, per/sec, &#8230;), it&#8217;s possible to use <code><a href="/docs/linux/man/3-sam_mark_failed/">sam_mark_failed</a>(3)</code> and let corosync watchdog take required action.</p>
<h2>Bugs</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a></code>(3), <code><a href="/docs/linux/man/3-sam_data_getsize/">sam_data_getsize</a></code>(3), <code><a href="/docs/linux/man/3-sam_data_restore/">sam_data_restore</a></code>(3), <code><a href="/docs/linux/man/3-sam_data_store/">sam_data_store</a></code>(3), <code><a href="/docs/linux/man/3-sam_finalize/">sam_finalize</a></code>(3), <code><a href="/docs/linux/man/3-sam_mark_failed/">sam_mark_failed</a></code>(3), <code><a href="/docs/linux/man/3-sam_start/">sam_start</a></code>(3), <code><a href="/docs/linux/man/3-sam_stop/">sam_stop</a></code>(3), <code><a href="/docs/linux/man/3-sam_register/">sam_register</a></code>(3), <code><a href="/docs/linux/man/3-sam_warn_signal_set/">sam_warn_signal_set</a></code>(3), <code><a href="/docs/linux/man/3-sam_hc_send/">sam_hc_send</a></code>(3), <code><a href="/docs/linux/man/3-sam_hc_callback_register/">sam_hc_callback_register</a></code>(3) </p>
