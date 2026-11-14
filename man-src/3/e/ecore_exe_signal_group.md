---
title: "ecore_exe_signal_group(3)"
name: "ecore_exe_signal_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_exe_signal_group/"
description: "Spawned Process Signal Functions – Functions that send signals to spawned processes."
---

<p>Spawned Process Signal Functions &#8211; Functions that send signals to spawned processes. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_exe_pause</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Pauses the given process by sending it a </i>SIGSTOP signal.<br />
 EAPI void <code>ecore_exe_continue</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Continues the given paused process by sending it a </i>SIGCONT signal.<br />
 EAPI void <code>ecore_exe_interrupt</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Sends the given spawned process a interrupt (</i>SIGINT) signal.<br />
 EAPI void <code>ecore_exe_quit</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Sends the given spawned process a quit (</i>SIGQUIT) signal.<br />
 EAPI void <code>ecore_exe_terminate</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Sends the given spawned process a terminate (</i>SIGTERM) signal.<br />
 EAPI void <code>ecore_exe_kill</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Kills the given spawned process by sending it a </i>SIGKILL signal.<br />
 EAPI void <code>ecore_exe_signal</code> (<code>Ecore_Exe</code> *exe, int num)<br />
 <i>Sends a </i>SIGUSR signal to the given spawned process.<br />
 EAPI void <code>ecore_exe_hup</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Sends a </i>SIGHUP signal to the given spawned process.</p>
<h2>Detailed Description</h2>
<p>Functions that send signals to spawned processes.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_exe_continue (<code>Ecore_Exe</code> * exe)</h3>
<p>Continues the given paused process by sending it a SIGCONT signal. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> Process handle to the given process.</dl>
<h3>EAPI void ecore_exe_hup (<code>Ecore_Exe</code> * exe)</h3>
<p>Sends a SIGHUP signal to the given spawned process. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> Process handle to the given process.</dl>
<h3>EAPI void ecore_exe_interrupt (<code>Ecore_Exe</code> * exe)</h3>
<p>Sends the given spawned process a interrupt (SIGINT) signal. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> Process handle to the given process.</dl>
<h3>EAPI void ecore_exe_kill (<code>Ecore_Exe</code> * exe)</h3>
<p>Kills the given spawned process by sending it a SIGKILL signal. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> Process handle to the given process.</dl>
<p> References ecore_timer_add(), and ecore_timer_del().</p>
<h3>EAPI void ecore_exe_pause (<code>Ecore_Exe</code> * exe)</h3>
<p>Pauses the given process by sending it a SIGSTOP signal. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> Process handle to the given process.</dl>
<h3>EAPI void ecore_exe_quit (<code>Ecore_Exe</code> * exe)</h3>
<p>Sends the given spawned process a quit (SIGQUIT) signal. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> Process handle to the given process.</dl>
<h3>EAPI void ecore_exe_signal (<code>Ecore_Exe</code> * exe, int num)</h3>
<p>Sends a SIGUSR signal to the given spawned process. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> Process handle to the given process.<br />
 <i>num</i> The number user signal to send. Must be either 1 or 2, or the signal will be ignored.</dl>
<h3>EAPI void ecore_exe_terminate (<code>Ecore_Exe</code> * exe)</h3>
<p>Sends the given spawned process a terminate (SIGTERM) signal. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> Process handle to the given process.</dl>
<p> Referenced by ecore_exe_pipe_run().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
