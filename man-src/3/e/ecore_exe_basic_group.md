---
title: "ecore_exe_basic_group(3)"
name: "ecore_exe_basic_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_exe_basic_group/"
description: "Process Spawning Functions – Functions that deal with spawned processes."
---

<p>Process Spawning Functions &#8211; Functions that deal with spawned processes. </p>
<h3>Functions</h3>
<p>EAPI <code>Ecore_Exe</code> * <code>ecore_exe_run</code> (const char *exe_cmd, const void *data)<br />
 <i>Spawns a child process. </i><br />
 EAPI <code>Ecore_Exe</code> * <code>ecore_exe_pipe_run</code> (const char *exe_cmd, Ecore_Exe_Flags flags, const void *data)<br />
 <i>Spawns a child process with its stdin/out available for communication. </i><br />
 EAPI int <code>ecore_exe_send</code> (<code>Ecore_Exe</code> *exe, void *data, int size)<br />
 <i>Sends data to the given child process which it recieves on stdin. </i><br />
 EAPI void <code>ecore_exe_close_stdin</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>The stdin of the given child process will close when the write buffer is empty. </i><br />
 EAPI void <code>ecore_exe_auto_limits_set</code> (<code>Ecore_Exe</code> *exe, int start_bytes, int end_bytes, int start_lines, int end_lines)<br />
 <i>Sets the auto pipe limits for the given process handle. </i><br />
 EAPI <code>Ecore_Exe_Event_Data</code> * <code>ecore_exe_event_data_get</code> (<code>Ecore_Exe</code> *exe, Ecore_Exe_Flags flags)<br />
 <i>Gets the auto pipe data for the given process handle. </i><br />
 EAPI void <code>ecore_exe_tag_set</code> (<code>Ecore_Exe</code> *exe, const char *tag)<br />
 <i>Sets the string tag for the given process handle. </i><br />
 EAPI char * <code>ecore_exe_tag_get</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Retrieves the tag attached to the given process handle. </i><br />
 EAPI void * <code>ecore_exe_free</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Frees the given process handle. </i><br />
 EAPI void <code>ecore_exe_event_data_free</code> (<code>Ecore_Exe_Event_Data</code> *e)<br />
 <i>Frees the given event data. </i><br />
 EAPI pid_t <code>ecore_exe_pid_get</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Retrieves the process ID of the given spawned process. </i><br />
 EAPI char * <code>ecore_exe_cmd_get</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Retrieves the command of the given spawned process. </i><br />
 EAPI void * <code>ecore_exe_data_get</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Retrieves the data attached to the given process handle. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with spawned processes.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_exe_auto_limits_set (<code>Ecore_Exe</code> * exe, int start_bytes, int end_bytes, int start_lines, int end_lines)</h3>
<p>Sets the auto pipe limits for the given process handle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> The given process handle.<br />
 <i>start_bytes</i> limit of bytes at start of output to buffer.<br />
 <i>end_bytes</i> limit of bytes at end of output to buffer.<br />
 <i>start_lines</i> limit of lines at start of output to buffer.<br />
 <i>end_lines</i> limit of lines at end of output to buffer.</dl>
<h3>EAPI void ecore_exe_close_stdin (<code>Ecore_Exe</code> * exe)</h3>
<p>The stdin of the given child process will close when the write buffer is empty. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> The child process</dl>
<h3>EAPI char* ecore_exe_cmd_get (<code>Ecore_Exe</code> * exe)</h3>
<p>Retrieves the command of the given spawned process. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> Handle to the given spawned process.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The command on success. NULL otherwise.</dl>
<h3>EAPI void* ecore_exe_data_get (<code>Ecore_Exe</code> * exe)</h3>
<p>Retrieves the data attached to the given process handle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> The given process handle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer attached to exe.</dl>
<h3>EAPI void ecore_exe_event_data_free (<code>Ecore_Exe_Event_Data</code> * e)</h3>
<p>Frees the given event data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The given event data.</dl>
<p> References _Ecore_Exe_Event_Data::data, and _Ecore_Exe_Event_Data::lines.</p>
<h3>EAPI <code>Ecore_Exe_Event_Data</code>* ecore_exe_event_data_get (<code>Ecore_Exe</code> * exe, Ecore_Exe_Flags flags)</h3>
<p>Gets the auto pipe data for the given process handle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> The given process handle.<br />
 <i>flags</i> Is this a ECORE_EXE_PIPE_READ or ECORE_EXE_PIPE_ERROR?</dl>
<p> References _Ecore_Exe_Event_Data::data, ECORE_EXE_PIPE_ERROR, ECORE_EXE_PIPE_ERROR_LINE_BUFFERED, ECORE_EXE_PIPE_READ, ECORE_EXE_PIPE_READ_LINE_BUFFERED, _Ecore_Exe_Event_Data::exe, _Ecore_Exe_Event_Data::lines, and _Ecore_Exe_Event_Data::size.</p>
<h3>EAPI void* ecore_exe_free (<code>Ecore_Exe</code> * exe)</h3>
<p>Frees the given process handle. </p>
<p> Note that the process that the handle represents is unaffected by this function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> The given process handle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data attached to the handle when <code>ecore_exe_run</code> was called.</dl>
<p> References ecore_main_fd_handler_del(), and ecore_timer_del(). </p>
<p> Referenced by ecore_exe_pipe_run().</p>
<h3>EAPI pid_t ecore_exe_pid_get (<code>Ecore_Exe</code> * exe)</h3>
<p>Retrieves the process ID of the given spawned process. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> Handle to the given spawned process.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The process ID on success. -1 otherwise.</dl>
<h3>EAPI <code>Ecore_Exe</code>* ecore_exe_pipe_run (const char * exe_cmd, Ecore_Exe_Flags flags, const void * data)</h3>
<p>Spawns a child process with its stdin/out available for communication. </p>
<p> This function forks and runs the given command using /bin/sh. </p>
<p> Note that the process handle is only valid until a child process terminated event is received. After all handlers for the child process terminated event have been called, the handle will be freed by Ecore. </p>
<p> This function does the same thing as <code>ecore_exe_run()</code>, but also makes the standard in and/or out as well as stderr from the child process available for reading or writing. To write use <code>ecore_exe_send()</code>. To read listen to ECORE_EXE_EVENT_DATA or ECORE_EXE_EVENT_ERROR events (set up handlers). Ecore may buffer read and error data until a newline character if asked for with the flags. All data will be included in the events (newlines will be replaced with NULLS if line buffered). ECORE_EXE_EVENT_DATA events will only happen if the process is run with ECORE_EXE_PIPE_READ enabled in the flags. The same with the error version. Writing will only be allowed with ECORE_EXE_PIPE_WRITE enabled in the flags. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe_cmd</i> The command to run with /bin/sh.<br />
 <i>flags</i> The flag parameters for how to deal with inter-process I/O<br />
 <i>data</i> Data to attach to the returned process handle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A process handle to the spawned process.</dl>
<p> References ecore_event_add(), ECORE_EXE_EVENT_ADD, ecore_exe_free(), ECORE_EXE_PIPE_AUTO, ECORE_EXE_PIPE_ERROR, ECORE_EXE_PIPE_READ, ECORE_EXE_PIPE_WRITE, ecore_exe_terminate(), ECORE_FD_READ, ECORE_FD_WRITE, ecore_main_fd_handler_active_set(), ecore_main_fd_handler_add(), and _Ecore_Exe_Event_Add::exe. </p>
<p> Referenced by ecore_exe_run().</p>
<h3>EAPI <code>Ecore_Exe</code>* ecore_exe_run (const char * exe_cmd, const void * data)</h3>
<p>Spawns a child process. </p>
<p> This is now just a thin wrapper around <code>ecore_exe_pipe_run()</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe_cmd</i> The command to run with /bin/sh.<br />
 <i>data</i> Data to attach to the returned process handle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A process handle to the spawned process.</dl>
<p> References ecore_exe_pipe_run().</p>
<h3>EAPI int ecore_exe_send (<code>Ecore_Exe</code> * exe, void * data, int size)</h3>
<p>Sends data to the given child process which it recieves on stdin. </p>
<p> This function writes to a child processes standard in, with unlimited buffering. This call will never block. It may fail if the system runs out of memory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> The child process to send to<br />
 <i>data</i> The data to send<br />
 <i>size</i> The size of the data to send, in bytes</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if successful, 0 on failure.</dl>
<p> References ECORE_FD_WRITE, and ecore_main_fd_handler_active_set().</p>
<h3>EAPI char* ecore_exe_tag_get (<code>Ecore_Exe</code> * exe)</h3>
<p>Retrieves the tag attached to the given process handle. </p>
<p> There is no need to free it as it just returns the internal pointer value. This value is only valid as long as the exe is valid or until the tag is set to something else on this exe. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> The given process handle.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The string attached to exe.</dl>
<h3>EAPI void ecore_exe_tag_set (<code>Ecore_Exe</code> * exe, const char * tag)</h3>
<p>Sets the string tag for the given process handle. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>exe</i> The given process handle.<br />
 <i>tag</i> The string tag to set on the process handle.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
