---
title: "ecore(3)"
name: "ecore"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore/"
description: "Ecore.h – The file that provides the program utility, main loop and timer functions."
---

<p>Ecore.h &#8211; The file that provides the program utility, main loop and timer functions. </p>
<h2>Synopsis</h2>
<h3>Data Structures</h3>
<p>struct <code>_Ecore_Event_Signal_User</code><br />
 <i>User signal event. </i><br />
 struct <code>_Ecore_Event_Signal_Hup</code><br />
 <i>Hup signal event. </i><br />
 struct <code>_Ecore_Event_Signal_Exit</code><br />
 <i>Exit request event. </i><br />
 struct <code>_Ecore_Event_Signal_Power</code><br />
 <i>Power event. </i><br />
 struct <code>_Ecore_Event_Signal_Realtime</code><br />
 <i>Realtime event. </i><br />
 struct <code>_Ecore_Exe_Event_Add</code><br />
 <i>Process add event. </i><br />
 struct <code>_Ecore_Exe_Event_Del</code><br />
 <i>Process exit event. </i><br />
 struct <code>_Ecore_Exe_Event_Data_Line</code><br />
 <i>&lt; Lines from a child process </i><br />
 struct <code>_Ecore_Exe_Event_Data</code><br />
 <i>Data from a child process event. </i></p>
<h3>Defines</h3>
<p>#define <code>ECORE_CALLBACK_CANCEL</code> 0<br />
 <i>Return value to remove a callback. </i><br />
 #define <code>ECORE_CALLBACK_RENEW</code> 1<br />
 <i>Return value to keep a callback. </i><br />
 #define <code>ECORE_EVENT_SIGNAL_USER</code> 1<br />
 <i>User signal event. </i><br />
 #define <code>ECORE_EVENT_SIGNAL_HUP</code> 2<br />
 <i>Hup signal event. </i><br />
 #define <code>ECORE_EVENT_SIGNAL_EXIT</code> 3<br />
 <i>Exit signal event. </i><br />
 #define <code>ECORE_EVENT_SIGNAL_POWER</code> 4<br />
 <i>Power signal event. </i><br />
 #define <code>ECORE_EVENT_SIGNAL_REALTIME</code> 5<br />
 <i>Realtime signal event. </i></p>
<h3>Typedefs</h3>
<p>typedef void <code>Ecore_Exe</code><br />
 <i>A handle for spawned processes. </i><br />
 typedef void <code>Ecore_Timer</code><br />
 <i>A handle for timers. </i><br />
 typedef void <code>Ecore_Idler</code><br />
 <i>A handle for idlers. </i><br />
 typedef void <code>Ecore_Idle_Enterer</code><br />
 <i>A handle for idle enterers. </i><br />
 typedef void <code>Ecore_Idle_Exiter</code><br />
 <i>A handle for idle exiters. </i><br />
 typedef void <code>Ecore_Fd_Handler</code><br />
 <i>A handle for Fd hanlders. </i><br />
 typedef void <code>Ecore_Event_Handler</code><br />
 <i>A handle for an event handler. </i><br />
 typedef void <code>Ecore_Event_Filter</code><br />
 <i>A handle for an event filter. </i><br />
 typedef void <code>Ecore_Event</code><br />
 <i>A handle for an event. </i><br />
 typedef void <code>Ecore_Animator</code><br />
 <i>A handle for animators. </i><br />
 typedef void <code>Ecore_Poller</code><br />
 <i>A handle for pollers. </i><br />
 typedef struct <code>_Ecore_Event_Signal_User</code> <code>Ecore_Event_Signal_User</code><br />
 <i>User signal event. </i><br />
 typedef struct <code>_Ecore_Event_Signal_Hup</code> <code>Ecore_Event_Signal_Hup</code><br />
 <i>Hup signal event. </i><br />
 typedef struct <code>_Ecore_Event_Signal_Exit</code> <code>Ecore_Event_Signal_Exit</code><br />
 <i>Exit signal event. </i><br />
 typedef struct <code>_Ecore_Event_Signal_Power</code> <code>Ecore_Event_Signal_Power</code><br />
 <i>Power signal event. </i><br />
 typedef struct <code>_Ecore_Event_Signal_Realtime</code> <code>Ecore_Event_Signal_Realtime</code><br />
 <i>Realtime signal event. </i><br />
 typedef struct <code>_Ecore_Exe_Event_Add</code> <code>Ecore_Exe_Event_Add</code><br />
 <i>Spawned Exe add event. </i><br />
 typedef struct <code>_Ecore_Exe_Event_Del</code> <code>Ecore_Exe_Event_Del</code><br />
 <i>Spawned Exe exit event. </i><br />
 typedef struct <code>_Ecore_Exe_Event_Data_Line</code> <code>Ecore_Exe_Event_Data_Line</code><br />
 <i>Lines from a child process. </i><br />
 typedef struct <code>_Ecore_Exe_Event_Data</code> <code>Ecore_Exe_Event_Data</code><br />
 <i>Data from a child process. </i></p>
<h3>Enumerations</h3>
<p>enum <code>_Ecore_Fd_Handler_Flags</code> { <code>ECORE_FD_READ</code> = 1, <code>ECORE_FD_WRITE</code> = 2, <code>ECORE_FD_ERROR</code> = 4 } </p>
<p> enum <code>_Ecore_Exe_Flags</code> { <code>ECORE_EXE_PIPE_READ</code> = 1, <code>ECORE_EXE_PIPE_WRITE</code> = 2, <code>ECORE_EXE_PIPE_ERROR</code> = 4, <code>ECORE_EXE_PIPE_READ_LINE_BUFFERED</code> = 8, <code>ECORE_EXE_PIPE_ERROR_LINE_BUFFERED</code> = 16, <code>ECORE_EXE_PIPE_AUTO</code> = 32, <code>ECORE_EXE_RESPAWN</code> = 64, <code>ECORE_EXE_USE_SH</code> = 128, <code>ECORE_EXE_NOT_LEADER</code> = 256 } </p>
<p> enum <code>_Ecore_Poller_Type</code> { <code>ECORE_POLLER_CORE</code> = 0 } </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_init</code> (void)<br />
 <i>Set up connections, signal handlers, sockets etc. </i><br />
 EAPI int <code>ecore_shutdown</code> (void)<br />
 <i>Shut down connections, signal handlers sockets etc. </i><br />
 EAPI void <code>ecore_app_args_set</code> (int argc, const char **argv)<br />
 <i>Set up the programs command-line arguments. </i><br />
 EAPI void <code>ecore_app_args_get</code> (int *argc, char ***argv)<br />
 <i>Return the programs stored command-line arguments. </i><br />
 EAPI void <code>ecore_app_restart</code> (void)<br />
 <i>Restart the program executable with the command-line arguments stored. </i><br />
 EAPI <code>Ecore_Event_Handler</code> * <code>ecore_event_handler_add</code> (int type, int(*func)(void *data, int type, void *event), const void *data)<br />
 <i>Add an event handler. </i><br />
 EAPI void * <code>ecore_event_handler_del</code> (<code>Ecore_Event_Handler</code> *event_handler)<br />
 <i>Delete an event handler. </i><br />
 EAPI <code>Ecore_Event</code> * <code>ecore_event_add</code> (int type, void *ev, void(*func_free)(void *data, void *ev), void *data)<br />
 <i>Add an event to the event queue. </i><br />
 EAPI void * <code>ecore_event_del</code> (<code>Ecore_Event</code> *event)<br />
 <i>Delete an event from the queue. </i><br />
 EAPI int <code>ecore_event_type_new</code> (void)<br />
 <i>Allocate a new event type id sensibly and return the new id. </i><br />
 EAPI <code>Ecore_Event_Filter</code> * <code>ecore_event_filter_add</code> (void *(*func_start)(void *data), int(*func_filter)(void *data, void *loop_data, int type, void *event), void(*func_end)(void *data, void *loop_data), const void *data)<br />
 <i>Add a filter the current event queue. </i><br />
 EAPI void * <code>ecore_event_filter_del</code> (<code>Ecore_Event_Filter</code> *ef)<br />
 <i>Delete an event filter. </i><br />
 EAPI int <code>ecore_event_current_type_get</code> (void)<br />
 <i>Return the current event type being handled. </i><br />
 EAPI void * <code>ecore_event_current_event_get</code> (void)<br />
 <i>Return the current event type pointer handled. </i><br />
 EAPI <code>Ecore_Exe</code> * <code>ecore_exe_run</code> (const char *exe_cmd, const void *data)<br />
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
 EAPI void <code>ecore_exe_event_data_free</code> (<code>Ecore_Exe_Event_Data</code> *data)<br />
 <i>Frees the given event data. </i><br />
 EAPI void * <code>ecore_exe_free</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Frees the given process handle. </i><br />
 EAPI pid_t <code>ecore_exe_pid_get</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Retrieves the process ID of the given spawned process. </i><br />
 EAPI void <code>ecore_exe_tag_set</code> (<code>Ecore_Exe</code> *exe, const char *tag)<br />
 <i>Sets the string tag for the given process handle. </i><br />
 EAPI char * <code>ecore_exe_tag_get</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Retrieves the tag attached to the given process handle. </i><br />
 EAPI char * <code>ecore_exe_cmd_get</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Retrieves the command of the given spawned process. </i><br />
 EAPI void * <code>ecore_exe_data_get</code> (<code>Ecore_Exe</code> *exe)<br />
 <i>Retrieves the data attached to the given process handle. </i><br />
 EAPI void <code>ecore_exe_pause</code> (<code>Ecore_Exe</code> *exe)<br />
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
 <i>Sends a </i>SIGHUP signal to the given spawned process.<br />
 EAPI <code>Ecore_Idler</code> * <code>ecore_idler_add</code> (int(*func)(void *data), const void *data)<br />
 <i>Add an idler handler. </i><br />
 EAPI void * <code>ecore_idler_del</code> (<code>Ecore_Idler</code> *idler)<br />
 <i>Delete an idler callback from the list to be executed. </i><br />
 EAPI <code>Ecore_Idle_Enterer</code> * <code>ecore_idle_enterer_add</code> (int(*func)(void *data), const void *data)<br />
 <i>Add an idle enterer handler. </i><br />
 EAPI <code>Ecore_Idle_Enterer</code> * <code>ecore_idle_enterer_before_add</code> (int(*func)(void *data), const void *data)<br />
 <i>Add an idle enterer handler at the start of the list so it gets called earlier than others. </i><br />
 EAPI void * <code>ecore_idle_enterer_del</code> (<code>Ecore_Idle_Enterer</code> *idle_enterer)<br />
 <i>Delete an idle enterer callback. </i><br />
 EAPI <code>Ecore_Idle_Exiter</code> * <code>ecore_idle_exiter_add</code> (int(*func)(void *data), const void *data)<br />
 <i>Add an idle exiter handler. </i><br />
 EAPI void * <code>ecore_idle_exiter_del</code> (<code>Ecore_Idle_Exiter</code> *idle_exiter)<br />
 <i>Delete an idle exiter handler from the list to be run on exiting idle state. </i><br />
 EAPI void <code>ecore_main_loop_iterate</code> (void)<br />
 <i>Runs a single iteration of the main loop to process everything on the queue. </i><br />
 EAPI void <code>ecore_main_loop_begin</code> (void)<br />
 <i>Runs the application main loop. </i><br />
 EAPI void <code>ecore_main_loop_quit</code> (void)<br />
 <i>Quits the main loop once all the events currently on the queue have been processed. </i><br />
 EAPI <code>Ecore_Fd_Handler</code> * <code>ecore_main_fd_handler_add</code> (int fd, Ecore_Fd_Handler_Flags flags, int(*func)(void *data, <code>Ecore_Fd_Handler</code> *fd_handler), const void *data, int(*buf_func)(void *buf_data, <code>Ecore_Fd_Handler</code> *fd_handler), const void *buf_data)<br />
 <i>Adds a callback for activity on the given file descriptor. </i><br />
 EAPI void * <code>ecore_main_fd_handler_del</code> (<code>Ecore_Fd_Handler</code> *fd_handler)<br />
 <i>Deletes the given FD handler. </i><br />
 EAPI int <code>ecore_main_fd_handler_fd_get</code> (<code>Ecore_Fd_Handler</code> *fd_handler)<br />
 <i>Retrieves the file descriptor that the given handler is handling. </i><br />
 EAPI int <code>ecore_main_fd_handler_active_get</code> (<code>Ecore_Fd_Handler</code> *fd_handler, Ecore_Fd_Handler_Flags flags)<br />
 <i>Return if read, write or error, or a combination thereof, is active on the file descriptor of the given FD handler. </i><br />
 EAPI void <code>ecore_main_fd_handler_active_set</code> (<code>Ecore_Fd_Handler</code> *fd_handler, Ecore_Fd_Handler_Flags flags)<br />
 <i>Set what active streams the given FD handler should be monitoring. </i><br />
 EAPI double <code>ecore_time_get</code> (void)<br />
 <i>Retrieves the current system time as a floating point value in seconds. </i><br />
 EAPI <code>Ecore_Timer</code> * <code>ecore_timer_add</code> (double in, int(*func)(void *data), const void *data)<br />
 <i>Creates a timer to call the given function in the given period of time. </i><br />
 EAPI void * <code>ecore_timer_del</code> (<code>Ecore_Timer</code> *timer)<br />
 <i>Delete the specified timer from the timer list. </i><br />
 EAPI void <code>ecore_timer_interval_set</code> (<code>Ecore_Timer</code> *timer, double in)<br />
 <i>Change the interval the timer ticks of. </i><br />
 EAPI void <code>ecore_timer_delay</code> (<code>Ecore_Timer</code> *timer, double add)<br />
 <i>Add some delay for the next occurence of a timer. </i><br />
 EAPI double <code>ecore_timer_pending_get</code> (<code>Ecore_Timer</code> *timer)<br />
 <i>Get the pending time regarding a timer. </i><br />
 EAPI <code>Ecore_Animator</code> * <code>ecore_animator_add</code> (int(*func)(void *data), const void *data)<br />
 <i>Add a animator to tick off at every animaton tick during main loop execution. </i><br />
 EAPI void * <code>ecore_animator_del</code> (<code>Ecore_Animator</code> *animator)<br />
 <i>Delete the specified animator from the animator list. </i><br />
 EAPI void <code>ecore_animator_frametime_set</code> (double frametime)<br />
 <i>Set the animator call interval in seconds. </i><br />
 EAPI double <code>ecore_animator_frametime_get</code> (void)<br />
 <i>Get the animator call interval in seconds. </i><br />
 EAPI void <code>ecore_poller_poll_interval_set</code> (Ecore_Poller_Type type, double poll_time)<br />
 <i>Sets the time between ticks (in seconds) for the given ticker clock. </i><br />
 EAPI double <code>ecore_poller_poll_interval_get</code> (Ecore_Poller_Type type)<br />
 <i>Gets the time between ticks (in seconds) for the fiven ticker clock. </i><br />
 EAPI <code>Ecore_Poller</code> * <code>ecore_poller_add</code> (Ecore_Poller_Type type, int interval, int(*func)(void *data), const void *data)<br />
 <i>Creates a poller to call the given function at a particular tick interval. </i><br />
 EAPI void * <code>ecore_poller_del</code> (<code>Ecore_Poller</code> *poller)<br />
 <i>Delete the specified poller from the timer list. </i></p>
<h3>Variables</h3>
<p>EAPI int <code>ECORE_EXE_EVENT_ADD</code><br />
 <i>A child process has been added. </i><br />
 EAPI int <code>ECORE_EXE_EVENT_DEL</code><br />
 <i>A child process has been deleted (it exited, naming consistant with the rest of ecore). </i><br />
 EAPI int <code>ECORE_EXE_EVENT_DATA</code><br />
 <i>Data from a child process. </i><br />
 EAPI int <code>ECORE_EXE_EVENT_ERROR</code><br />
 <i>Errors from a child process. </i></p>
<h2>Detailed Description</h2>
<p>The file that provides the program utility, main loop and timer functions. </p>
<p> This header provides the Ecore event handling loop. For more details, see <code>Main Loop Functions</code>. </p>
<p> For the main loop to be of any use, you need to be able to add events and event handlers. Events for file descriptor events are covered in <code>File Event Handling Functions</code>. </p>
<p> Time functions are covered in <code>Ecore Time Functions</code>. </p>
<p> There is also provision for callbacks for when the loop enters or exits an idle state. See <code>Idle Handlers</code> for more information. </p>
<p> Functions are also provided for spawning child processes using fork. See <code>Process Spawning Functions</code> and <code>Spawned Process Signal Functions</code> for more details.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>_Ecore_Exe_Flags</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>ECORE_EXE_PIPE_READ </i></p>
<dd>Exe Pipe Read mask.</p>
<dt><i>ECORE_EXE_PIPE_WRITE </i></p>
<dd>Exe Pipe Write mask.</p>
<dt><i>ECORE_EXE_PIPE_ERROR </i></p>
<dd>Exe Pipe error mask.</p>
<dt><i>ECORE_EXE_PIPE_READ_LINE_BUFFERED </i></p>
<dd>Reads are buffered until a newline and delivered 1 event per line.</p>
<dt><i>ECORE_EXE_PIPE_ERROR_LINE_BUFFERED </i></p>
<dd>Errors are buffered until a newline and delivered 1 event per line.</p>
<dt><i>ECORE_EXE_PIPE_AUTO </i></p>
<dd>stdout and stderr are buffered automatically</p>
<dt><i>ECORE_EXE_RESPAWN </i></p>
<dd>FIXME: Exe is restarted if it dies.</p>
<dt><i>ECORE_EXE_USE_SH </i></p>
<dd>Use /bin/sh to run the command.</dl>
<dl COMPACT>
<dt><i>ECORE_EXE_NOT_LEADER </i></p>
<dd>Do not use setsid() to have the executed process be its own session leader.</dl>
<h3>enum <code>_Ecore_Fd_Handler_Flags</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>ECORE_FD_READ </i></p>
<dd>Fd Read mask.</p>
<dt><i>ECORE_FD_WRITE </i></p>
<dd>Fd Write mask.</p>
<dt><i>ECORE_FD_ERROR </i></p>
<dd>Fd Error mask.</dl>
<h3>enum <code>_Ecore_Poller_Type</code></h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>ECORE_POLLER_CORE </i></p>
<dd>The core poller interval.</dl>
<h2>Function Documentation</h2>
<h3>EAPI <code>Ecore_Animator</code>* ecore_animator_add (int(*)(void *data) func, const void * data)</h3>
<p>Add a animator to tick off at every animaton tick during main loop execution. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>func</i> The function to call when it ticks off<br />
 <i>data</i> The data to pass to the function</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A handle to the new animator</dl>
<p> This function adds a animator and returns its handle on success and NULL on failure. The function func will be called every N seconds where N is the frametime interval set by <code>ecore_animator_frametime_set()</code>. The function will be passed the data pointer as its parameter. </p>
<p> When the animator func is called, it must return a value of either 1 or 0. If it returns 1 (or ECORE_CALLBACK_RENEW), it will be called again at the next tick, or if it returns 0 (or ECORE_CALLBACK_CANCEL) it will be deleted automatically making any references/handles for it invalid. </p>
<p> References ecore_animator_add(), and ecore_timer_add(). </p>
<p> Referenced by ecore_animator_add().</p>
<h3>EAPI void* ecore_animator_del (<code>Ecore_Animator</code> * animator)</h3>
<p>Delete the specified animator from the animator list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>animator</i> The animator to delete</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer set for the animator</dl>
<p> Delete the specified aqnimator from the set of animators that are executed during main loop execution. This function returns the data parameter that was being passed to the callback on success, or NULL on failure. After this call returns the specified animator object animator is invalid and should not be used again. It will not get called again after deletion. </p>
<p> References ecore_animator_del(). </p>
<p> Referenced by ecore_animator_del().</p>
<h3>EAPI double ecore_animator_frametime_get (void)</h3>
<p>Get the animator call interval in seconds. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The time in second in between animator ticks.</dl>
<p> this function retrieves the time inbetween animator ticks, in seconds. </p>
<p> References ecore_animator_frametime_get(). </p>
<p> Referenced by ecore_animator_frametime_get().</p>
<h3>EAPI void ecore_animator_frametime_set (double frametime)</h3>
<p>Set the animator call interval in seconds. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>frametime</i> The time in seconds in between animator ticks.</dl>
<p> This function sets the time interval (in seconds) inbetween animator ticks. </p>
<p> References ecore_animator_frametime_set(), ecore_timer_add(), and ecore_timer_del(). </p>
<p> Referenced by ecore_animator_frametime_set().</p>
<h3>EAPI void ecore_app_args_get (int * argc, char *** argv)</h3>
<p>Return the programs stored command-line arguments. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>argc</i> A pointer to the return value to hold argc<br />
 <i>argv</i> A pointer to the return value to hold argv</dl>
<p> When called, this funciton returns the arguments for the program stored by <code>ecore_app_args_set()</code>. The integer pointed to by argc will be filled, if the pointer is not NULL, and the string array pointer argv will be filled also if the pointer is not NULL. The values they are filled with will be the same set by <code>ecore_app_args_set()</code>. </p>
<p> References ecore_app_args_get(). </p>
<p> Referenced by ecore_app_args_get(), ecore_config_args_parse(), and ecore_x_window_defaults_set().</p>
<h3>EAPI void ecore_app_args_set (int argc, const char ** argv)</h3>
<p>Set up the programs command-line arguments. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>argc</i> The same as passed as argc to the programs main() function<br />
 <i>argv</i> The same as passed as argv to the programs main() function</dl>
<p> A call to this function will store the programs command-line arguments for later use by <code>ecore_app_restart()</code> or <code>ecore_app_args_get()</code>. </p>
<p> References ecore_app_args_set(). </p>
<p> Referenced by ecore_app_args_set().</p>
<h3>EAPI void ecore_app_restart (void)</h3>
<p>Restart the program executable with the command-line arguments stored. </p>
<p> This function will restart &amp; re-execute this program in place of itself using the command-line arguments stored by <code>ecore_app_args_set()</code>. This is an easy way for a program to restart itself for cleanup purposes, configuration reasons or in the event of a crash. </p>
<p> References ecore_app_restart(). </p>
<p> Referenced by ecore_app_restart().</p>
<h3>EAPI <code>Ecore_Event</code>* ecore_event_add (int type, void * ev, void(*)(void *data, void *ev) func_free, void * data)</h3>
<p>Add an event to the event queue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>type</i> The event type to add to the end of the event queue<br />
 <i>ev</i> The private data structure for this event type<br />
 <i>func_free</i> The function to be called to free this private structure<br />
 <i>data</i> The data pointer to be passed to the free function</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A Handle for that event</dl>
<p> On success this function returns a handle to an event on the event queue, or NULL if it fails. If it succeeds, an event of type type will be added to the queue for processing by event handlers added by <code>ecore_event_handler_add()</code>. The ev parameter will be a pointer to the event private data that is specific to that event type. When the event is no longer needed, func_free will be called and passed the private structure pointer for cleaning up. If func_free is NULL, free() will be called with the private structure pointer. func_free is passed data as its data parameter. </p>
<p> References ecore_event_add(). </p>
<p> Referenced by ecore_con_server_connect(), ecore_event_add(), ecore_exe_pipe_run(), ecore_imf_context_commit_event_add(), ecore_imf_context_delete_surrounding_event_add(), ecore_imf_context_preedit_changed_event_add(), ecore_imf_context_preedit_end_event_add(), ecore_imf_context_preedit_start_event_add(), and ecore_job_add().</p>
<h3>EAPI void* ecore_event_current_event_get (void)</h3>
<p>Return the current event type pointer handled. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current event pointer being handled if inside a handler callback</dl>
<p> If the program is currently inside an Ecore event handler callback this will return the pointer of the current event being processed. If Ecore is not inside an event handler, NULL will be returned. </p>
<p> This is useful when certain Ecore modules such as Ecore_Evas &#8216;swallow&#8217; events and not all the original information is passed on. In special cases this extra information may be useful or needed and using this call can let the program access the event data if the type of the event is handled by the program. </p>
<p> References ecore_event_current_event_get(). </p>
<p> Referenced by ecore_event_current_event_get().</p>
<h3>EAPI int ecore_event_current_type_get (void)</h3>
<p>Return the current event type being handled. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current event type being handled if inside a handler callback</dl>
<p> If the program is currently inside an Ecore event handler callback this will return the type of the current event being processed. If Ecore is not inside an event handler, ECORE_EVENT_NONE is returned. </p>
<p> This is useful when certain Ecore modules such as Ecore_Evas &#8216;swallow&#8217; events and not all the original information is passed on. In special cases this extra information may be useful or needed and using this call can let the program know if the event type being handled is one it wants to get more information about. </p>
<p> References ecore_event_current_type_get(). </p>
<p> Referenced by ecore_event_current_type_get().</p>
<h3>EAPI void* ecore_event_del (<code>Ecore_Event</code> * event)</h3>
<p>Delete an event from the queue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event</i> The event handle to delete</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer originally set for the event free function</dl>
<p> This deletes the event event from the event queue, and returns the data parameer originally set when adding it with <code>ecore_event_add()</code>. This does not immediately call the free function, and it may be called later on cleanup, and so if the free function depends on the data pointer to work, you should defer cleaning of this till the free function is called later. </p>
<p> References ecore_event_del(). </p>
<p> Referenced by ecore_event_del(), and ecore_job_del().</p>
<h3>EAPI <code>Ecore_Event_Filter</code>* ecore_event_filter_add (void *(*)(void *data) func_start, int(*)(void *data, void *loop_data, int type, void *event) func_filter, void(*)(void *data, void *loop_data) func_end, const void * data)</h3>
<p>Add a filter the current event queue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>func_start</i> Function to call just before filtering and return data<br />
 <i>func_filter</i> Function to call on each event<br />
 <i>func_end</i> Function to call after the queu has been filtered<br />
 <i>data</i> Data to pass to the filter functions</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A filter handle</dl>
<p> This adds a filter to call callbacks to loop through the event queue and filter events out of the queue. On failure NULL is returned. On success a Filter handle is returned. Filters are called on the queue just before Event handler processing to try and remove redundant events. Just as processing starts func_start is called and passed the data pointer. This function returns a pointer that is used as loop_data that is now passed to func_filter as loop_data. func_filter is also passed data and the event type and private event structure. If this callback returns 0, the event is removed from the queue. If it returns 1, the event is kept. When processing is finished func_end is called and is passed the loop_data and data pointer to clean up. </p>
<p> References ecore_event_filter_add(). </p>
<p> Referenced by ecore_event_filter_add(), and ecore_x_init().</p>
<h3>EAPI void* ecore_event_filter_del (<code>Ecore_Event_Filter</code> * ef)</h3>
<p>Delete an event filter. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ef</i> The event filter handle</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data set for the filter</dl>
<p> Delete a filter that has been added by its ef handle. On success this will return the data pointer set when this filter was added. On failure NULL is returned. </p>
<p> References ecore_event_filter_del(). </p>
<p> Referenced by ecore_event_filter_del().</p>
<h3>EAPI <code>Ecore_Event_Handler</code>* ecore_event_handler_add (int type, int(*)(void *data, int type, void *event) func, const void * data)</h3>
<p>Add an event handler. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>type</i> The type of the event this handler will get called for<br />
 <i>func</i> The function to call when the event is found in the queue<br />
 <i>data</i> A data pointer to pass to the called function func</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new Event handler, or NULL on failure</dl>
<p> Add an event handler to the list of handlers. This will, on success, return a handle to the event handler object that was created, that can be used later to remove the handler using <code>ecore_event_handler_del()</code>. The type parameter is the iteger of the event type that will trigger this callback to be called. The callback func is called when this event is processed and will be passed the event type, a pointer to the private event structure that is specific to that event type, and a data pointer that is provided in this call as the data parameter. </p>
<p> When the callback func is called, it must return 1 or 0. If it returns 1 (or ECORE_CALLBACK_RENEW), It will keep being called as per normal, for each handler set up for that event type. If it returns 0 (or ECORE_CALLBACK_CANCEL), it will cease processing handlers for that particular event, so all handler set to handle that event type that have not already been called, will not be. </p>
<p> References ecore_event_handler_add(). </p>
<p> Referenced by ecore_event_handler_add(), and ecore_ipc_init().</p>
<h3>EAPI void* ecore_event_handler_del (<code>Ecore_Event_Handler</code> * event_handler)</h3>
<p>Delete an event handler. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>event_handler</i> Event handler handle to delete</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>Data passed to handler</dl>
<p> Delete a specified event handler from the handler list. On success this will delete the event handler and return the pointer passed as data when the handler was added by <code>ecore_event_handler_add()</code>. On failure NULL will be returned. Once a handler is deleted it will no longer be called. </p>
<p> References ecore_event_handler_del(). </p>
<p> Referenced by ecore_event_handler_del(), and ecore_ipc_shutdown().</p>
<h3>EAPI int ecore_event_type_new (void)</h3>
<p>Allocate a new event type id sensibly and return the new id. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new event type id.</dl>
<p> This function allocates a new event type id and returns it. Once an event type has been allocated it can never be de-allocated during the life of the program. There is no guarantee of the contents of this event ID, or how it is calculated, except that the ID will be unique to the current instance of the process. </p>
<p> References ecore_event_type_new(). </p>
<p> Referenced by ecore_con_init(), ecore_con_url_init(), ecore_event_type_new(), ecore_fb_init(), ecore_imf_init(), ecore_ipc_init(), and ecore_x_init().</p>
<h3>EAPI int ecore_init (void)</h3>
<p>Set up connections, signal handlers, sockets etc. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 or greater on success, 0 otherwise</dl>
<p> This function sets up all singal handlers and the basic event loop. If it succeeds, 1 will be returned, otherwise 0 will be returned. </p>
<pre> #include &lt;<a href="file:/usr/include/Ecore.h">Ecore.h</a>&gt;
 int main(int argc, char **argv)
 {
 if (!ecore_init())
 {
 printf('ERROR: Cannot init Ecore!);
 return -1;
 }
 ecore_main_loop_begin();
 ecore_shutdown();
 }</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI <code>Ecore_Poller</code>* ecore_poller_add (Ecore_Poller_Type type, int interval, int(*)(void *data) func, const void * data)</h3>
<p>Creates a poller to call the given function at a particular tick interval. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>type</i> The ticker type to attach the poller to<br />
 <i>interval</i> The poll interval<br />
 <i>func</i> The given function. If func returns 1, the poller is rescheduled for the next tick interval.<br />
 <i>data</i> Data to pass to func when it is called.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A poller object on success. NULL on failure.</dl>
<p> This function adds a poller callback that is to be called regularly along with all other poller callbacks so the pollers are synchronized with all other pollers running off the same poller type and at the same tick interval. This should be used for polling things when polling is desired or required, and you do not have specific requirements on the exact times to poll and want to avoid extra process wakeups for polling. This will save power as the CPU has more of a chance to go into a low power state the longer it is asleep for, so this should be used if you are at all power conscious. </p>
<p> The type parameter defines the poller tick type (there is a virtual clock ticking all the time &#8211; though ecore avoids making it tick when there will not be any work to do at that tick point). There is only one ticker at the moment &#8211; that is ECORE_POLLER_CORE. This is here for future expansion if multiple clocks with different frequencies are really required. The default time between ticks for the ECORE_POLLER_CORE ticker is 0.125 seconds. </p>
<p> The interval is the number of ticker ticks that will pass by in between invocations of the func callback. This must be between 1 and 32768 inclusive, and must be a power of 2 (i.e. 1, 2, 4, 8, 16, &#8230; 16384, 32768). If it is 1, then the function will be called every tick. if it is 2, then it will be called every 2nd tick, if it is 8, then every 8th tick etc. Exactly which tick is undefined, as only the interval between calls can be defined. Ecore will endeavour to keep pollers synchronised and to call as many in 1 wakeup event as possible. </p>
<p> This function adds a poller and returns its handle on success and NULL on failure. The function func will be called at tick intervals described above. The function will be passed the data pointer as its parameter. </p>
<p> When the poller func is called, it must return a value of either 1 (or ECORE_CALLBACK_RENEW) or 0 (or ECORE_CALLBACK_CANCEL). If it returns 1, it will be called again at the next tick, or if it returns 0 it will be deleted automatically making any references/handles for it invalid. </p>
<p> References ecore_poller_add(). </p>
<p> Referenced by ecore_poller_add().</p>
<h3>EAPI void* ecore_poller_del (<code>Ecore_Poller</code> * poller)</h3>
<p>Delete the specified poller from the timer list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>poller</i> The poller to delete.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer set for the timer when <code>ecore_poller_add</code> was called. NULL is returned if the function is unsuccessful.</dl>
<p> Note: poller must be a valid handle. If the poller function has already returned 0, the handle is no longer valid (and does not need to be delete). </p>
<p> References ecore_poller_del(). </p>
<p> Referenced by ecore_poller_del().</p>
<h3>EAPI double ecore_poller_poll_interval_get (Ecore_Poller_Type type)</h3>
<p>Gets the time between ticks (in seconds) for the fiven ticker clock. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>type</i> The ticker type to query</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The time in seconds between ticks of the ticker clock</dl>
<p> This will get the time between ticks of the specifider ticker clock. </p>
<p> References ecore_poller_poll_interval_get(). </p>
<p> Referenced by ecore_poller_poll_interval_get().</p>
<h3>EAPI void ecore_poller_poll_interval_set (Ecore_Poller_Type type, double poll_time)</h3>
<p>Sets the time between ticks (in seconds) for the given ticker clock. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>type</i> The ticker type to adjust<br />
 <i>poll_time</i> The time (in seconds) between ticks of the clock</dl>
<p> This will adjust the time between ticks of the given ticker type defined by type to the time period defined by poll_time. </p>
<p> References ecore_poller_poll_interval_set(). </p>
<p> Referenced by ecore_poller_poll_interval_set().</p>
<h3>EAPI int ecore_shutdown (void)</h3>
<p>Shut down connections, signal handlers sockets etc. </p>
<p> This function shuts down all things set up in <code>ecore_init()</code> and cleans up all event queues, handlers, filters, timers, idlers, idle enterers/exiters etc. set up after <code>ecore_init()</code> was called. </p>
<p> Do not call this function from any callback that may be called from the main loop, as the main loop will then fall over and not function properly.</p>
<h2>Variable Documentation</h2>
<h3>EAPI int <code>ECORE_EXE_EVENT_DATA</code></h3>
<p>Data from a child process. </p>
<h3>EAPI int <code>ECORE_EXE_EVENT_DEL</code></h3>
<p>A child process has been deleted (it exited, naming consistant with the rest of ecore). </p>
<h3>EAPI int <code>ECORE_EXE_EVENT_ERROR</code></h3>
<p>Errors from a child process. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
