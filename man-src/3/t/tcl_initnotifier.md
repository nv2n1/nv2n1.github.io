---
title: "tcl_initnotifier(3)"
name: "tcl_initnotifier"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_initnotifier/"
description: "Tcl_CreateEventSource, Tcl_DeleteEventSource, Tcl_SetMaxBlockTime, Tcl_QueueEvent, Tcl_ThreadQueueEvent, Tcl_ThreadAlert, Tcl_GetCurrentThread, Tcl_DeleteEvents, Tcl_InitNotifier, Tcl_FinalizeNotif..."
---

<p>Tcl_CreateEventSource, Tcl_DeleteEventSource, Tcl_SetMaxBlockTime, Tcl_QueueEvent, Tcl_ThreadQueueEvent, Tcl_ThreadAlert, Tcl_GetCurrentThread, Tcl_DeleteEvents, Tcl_InitNotifier, Tcl_FinalizeNotifier, Tcl_WaitForEvent, Tcl_AlertNotifier, Tcl_SetTimer, Tcl_ServiceAll, Tcl_ServiceEvent, Tcl_GetServiceMode, Tcl_SetServiceMode &#8211; the event queue and notifier interfaces </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_CreateEventSource</code>(<i>setupProc, checkProc, clientData</i>)
void
<code>Tcl_DeleteEventSource</code>(<i>setupProc, checkProc, clientData</i>)
void
<code>Tcl_SetMaxBlockTime</code>(<i>timePtr</i>)
void
<code>Tcl_QueueEvent</code>(<i>evPtr, position</i>)
void
<code>Tcl_ThreadQueueEvent</code>(<i>threadId, evPtr, position</i>)
void
<code>Tcl_ThreadAlert</code>(<i>threadId</i>)
Tcl_ThreadId
<code>Tcl_GetCurrentThread</code>()
void
<code>Tcl_DeleteEvents</code>(<i>deleteProc, clientData</i>)
ClientData
<code>Tcl_InitNotifier</code>()
void
<code>Tcl_FinalizeNotifier</code>(<i>clientData</i>)
int
<code>Tcl_WaitForEvent</code>(<i>timePtr</i>)
void
<code>Tcl_AlertNotifier</code>(<i>clientData</i>)
void
<code>Tcl_SetTimer</code>(<i>timePtr</i>)
int
<code>Tcl_ServiceAll</code>()
int
<code>Tcl_ServiceEvent</code>(<i>flags</i>)
int
<code>Tcl_GetServiceMode</code>()
int
<code>Tcl_SetServiceMode</code>(<i>mode</i>)
void
<code>Tcl_ServiceModeHook</code>(<i>mode</i>)
void
<code>Tcl_SetNotifier</code>(<i>notifierProcPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_EventSetupProc <i>*setupProc</i> (in) Procedure to invoke to prepare for event wait in <code>Tcl_DoOneEvent</code>.</p>
<dd>Tcl_EventCheckProc <i>*checkProc</i> (in) Procedure for <code>Tcl_DoOneEvent</code> to invoke after waiting for events. Checks to see if any events have occurred and, if so, queues them.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>setupProc</i>, <i>checkProc</i>, or <i>deleteProc</i>.</p>
<dd>Tcl_Time <i>*timePtr</i> (in) Indicates the maximum amount of time to wait for an event. This is specified as an interval (how long to wait), not an absolute time (when to wakeup). If the pointer passed to <code>Tcl_WaitForEvent</code> is NULL, it means there is no maximum wait time: wait forever if necessary.</p>
<dd>Tcl_Event <i>*evPtr</i> (in) An event to add to the event queue. The storage for the event must have been allocated by the caller using <code>Tcl_Alloc</code> or <code>ckalloc</code>.</p>
<dd>Tcl_QueuePosition <i>position</i> (in) Where to add the new event in the queue: <code>TCL_QUEUE_TAIL</code>, <code>TCL_QUEUE_HEAD</code>, or <code>TCL_QUEUE_MARK</code>.</p>
<dd>Tcl_ThreadId <i>threadId</i> (in) A unique identifier for a thread.</p>
<dd>Tcl_EventDeleteProc <i>*deleteProc</i> (in) Procedure to invoke for each queued event in <code>Tcl_DeleteEvents</code>.</p>
<dd>int <i>flags</i> (in) What types of events to service. These flags are the same as those passed to <code>Tcl_DoOneEvent</code>.</p>
<dd>int <i>mode</i> (in) Indicates whether events should be serviced by <code>Tcl_ServiceAll</code>. Must be one of <code>TCL_SERVICE_NONE</code> or <code>TCL_SERVICE_ALL</code>.</p>
<dd>Tcl_NotifierProcs* <i>notifierProcPtr</i> (in) Structure of function pointers describing notifier procedures that are to replace the ones installed in the executable. See <code>REPLACING THE NOTIFIER</code> for details. </p>
</dl>
<h2>Introduction</h2>
<p>The interfaces described here are used to customize the Tcl event loop. The two most common customizations are to add new sources of events and to merge Tcl&#8217;s event loop with some other event loop, such as one provided by an application in which Tcl is embedded. Each of these tasks is described in a separate section below. </p>
<p> The procedures in this manual entry are the building blocks out of which the Tcl event notifier is constructed. The event notifier is the lowest layer in the Tcl event mechanism. It consists of three things:</p>
<dl COMPACT>
<dt>[1]</p>
<dd>Event sources: these represent the ways in which events can be generated. For example, there is a timer event source that implements the <code>Tcl_CreateTimerHandler</code> procedure and the <code>after</code> command, and there is a file event source that implements the <code>Tcl_CreateFileHandler</code> procedure on Unix systems. An event source must work with the notifier to detect events at the right times, record them on the event queue, and eventually notify higher-level software that they have occurred. The procedures <code>Tcl_CreateEventSource</code>, <code>Tcl_DeleteEventSource</code>, and <code>Tcl_SetMaxBlockTime</code>, <code>Tcl_QueueEvent</code>, and <code>Tcl_DeleteEvents</code> are used primarily by event sources.</p>
<dt>[2]</p>
<dd>The event queue: for non-threaded applications, there is a single queue for the whole application, containing events that have been detected but not yet serviced. Event sources place events onto the queue so that they may be processed in order at appropriate times during the event loop. The event queue guarantees a fair discipline of event handling, so that no event source can starve the others. It also allows events to be saved for servicing at a future time. Threaded applications work in a similar manner, except that there is a separate event queue for each thread containing a Tcl interpreter. <code>Tcl_QueueEvent</code> is used (primarily by event sources) to add events to the event queue and <code>Tcl_DeleteEvents</code> is used to remove events from the queue without processing them. In a threaded application, <code>Tcl_QueueEvent</code> adds an event to the current thread&#8217;s queue, and <code>Tcl_ThreadQueueEvent</code> adds an event to a queue in a specific thread.</p>
<dt>[3]</p>
<dd>The event loop: in order to detect and process events, the application enters a loop that waits for events to occur, places them on the event queue, and then processes them. Most applications will do this by calling the procedure <code>Tcl_DoOneEvent</code>, which is described in a separate manual entry.</dl>
<p> Most Tcl applications need not worry about any of the internals of the Tcl notifier. However, the notifier now has enough flexibility to be retargeted either for a new platform or to use an external event loop (such as the Motif event loop, when Tcl is embedded in a Motif application). The procedures <code>Tcl_WaitForEvent</code> and <code>Tcl_SetTimer</code> are normally implemented by Tcl, but may be replaced with new versions to retarget the notifier (the <code>Tcl_InitNotifier</code>, <code>Tcl_AlertNotifier</code>, <code>Tcl_FinalizeNotifier</code>, <code>Tcl_Sleep</code>, <code>Tcl_CreateFileHandler</code>, and <code>Tcl_DeleteFileHandler</code> must also be replaced; see CREATING A NEW NOTIFIER below for details). The procedures <code>Tcl_ServiceAll</code>, <code>Tcl_ServiceEvent</code>, <code>Tcl_GetServiceMode</code>, and <code>Tcl_SetServiceMode</code> are provided to help connect Tcl&#8217;s event loop to an external event loop such as Motif&#8217;s.</p>
<h2>Notifier Basics</h2>
<p>The easiest way to understand how the notifier works is to consider what happens when <code>Tcl_DoOneEvent</code> is called. <code>Tcl_DoOneEvent</code> is passed a <i>flags</i> argument that indicates what sort of events it is OK to process and also whether or not to block if no events are ready. <code>Tcl_DoOneEvent</code> does the following things:</p>
<dl COMPACT>
<dt>[1]</p>
<dd>Check the event queue to see if it contains any events that can be serviced. If so, service the first possible event, remove it from the queue, and return. It does this by calling <code>Tcl_ServiceEvent</code> and passing in the <i>flags</i> argument.</p>
<dt>[2]</p>
<dd>Prepare to block for an event. To do this, <code>Tcl_DoOneEvent</code> invokes a <i>setup procedure</i> in each event source. The event source will perform event-source specific initialization and possibly call <code>Tcl_SetMaxBlockTime</code> to limit how long <code>Tcl_WaitForEvent</code> will block if no new events occur.</p>
<dt>[3]</p>
<dd>Call <code>Tcl_WaitForEvent</code>. This procedure is implemented differently on different platforms; it waits for an event to occur, based on the information provided by the event sources. It may cause the application to block if <i>timePtr</i> specifies an interval other than 0. <code>Tcl_WaitForEvent</code> returns when something has happened, such as a file becoming readable or the interval given by <i>timePtr</i> expiring. If there are no events for <code>Tcl_WaitForEvent</code> to wait for, so that it would block forever, then it returns immediately and <code>Tcl_DoOneEvent</code> returns 0.</p>
<dt>[4]</p>
<dd>Call a <i>check procedure</i> in each event source. The check procedure determines whether any events of interest to this source occurred. If so, the events are added to the event queue.</p>
<dt>[5]</p>
<dd>Check the event queue to see if it contains any events that can be serviced. If so, service the first possible event, remove it from the queue, and return.</p>
<dt>[6]</p>
<dd>See if there are idle callbacks pending. If so, invoke all of them and return.</p>
<dt>[7]</p>
<dd>Either return 0 to indicate that no events were ready, or go back to step [2] if blocking was requested by the caller. </p>
</dl>
<h2>Creating A New Event Source</h2>
<p>An event source consists of three procedures invoked by the notifier, plus additional C procedures that are invoked by higher-level code to arrange for event-driven callbacks. The three procedures called by the notifier consist of the setup and check procedures described above, plus an additional procedure that is invoked when an event is removed from the event queue for servicing. </p>
<p> The procedure <code>Tcl_CreateEventSource</code> creates a new event source. Its arguments specify the setup procedure and check procedure for the event source. <i>SetupProc</i> should match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_EventSetupProc(
 ClientData <i>clientData</i>,
 int <i>flags</i>);</pre>
</dl>
<p> The <i>clientData</i> argument will be the same as the <i>clientData</i> argument to <code>Tcl_CreateEventSource</code>; it is typically used to point to private information managed by the event source. The <i>flags</i> argument will be the same as the <i>flags</i> argument passed to <code>Tcl_DoOneEvent</code> except that it will never be 0 (<code>Tcl_DoOneEvent</code> replaces 0 with <code>TCL_ALL_EVENTS</code>). <i>Flags</i> indicates what kinds of events should be considered; if the bit corresponding to this event source is not set, the event source should return immediately without doing anything. For example, the file event source checks for the <code>TCL_FILE_EVENTS</code> bit. </p>
<p> <i>SetupProc</i>&#8216;s job is to make sure that the application wakes up when events of the desired type occur. This is typically done in a platform-dependent fashion. For example, under Unix an event source might call <code>Tcl_CreateFileHandler</code>; under Windows it might request notification with a Windows event. For timer-driven event sources such as timer events or any polled event, the event source can call <code>Tcl_SetMaxBlockTime</code> to force the application to wake up after a specified time even if no events have occurred. If no event source calls <code>Tcl_SetMaxBlockTime</code> then <code>Tcl_WaitForEvent</code> will wait as long as necessary for an event to occur; otherwise, it will only wait as long as the shortest interval passed to <code>Tcl_SetMaxBlockTime</code> by one of the event sources. If an event source knows that it already has events ready to report, it can request a zero maximum block time. For example, the setup procedure for the X event source looks to see if there are events already queued. If there are, it calls <code>Tcl_SetMaxBlockTime</code> with a 0 block time so that <code>Tcl_WaitForEvent</code> does not block if there is no new data on the X connection. The <i>timePtr</i> argument to <code>Tcl_WaitForEvent</code> points to a structure that describes a time interval in seconds and microseconds:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_Time {
 long <i>sec</i>;
 long <i>usec</i>;
} Tcl_Time;</pre>
</dl>
<p> The <i>usec</i> field should be less than 1000000. </p>
<p> Information provided to <code>Tcl_SetMaxBlockTime</code> is only used for the next call to <code>Tcl_WaitForEvent</code>; it is discarded after <code>Tcl_WaitForEvent</code> returns. The next time an event wait is done each of the event sources&#8217; setup procedures will be called again, and they can specify new information for that event wait. </p>
<p> If the application uses an external event loop rather than <code>Tcl_DoOneEvent</code>, the event sources may need to call <code>Tcl_SetMaxBlockTime</code> at other times. For example, if a new event handler is registered that needs to poll for events, the event source may call <code>Tcl_SetMaxBlockTime</code> to set the block time to zero to force the external event loop to call Tcl. In this case, <code>Tcl_SetMaxBlockTime</code> invokes <code>Tcl_SetTimer</code> with the shortest interval seen since the last call to <code>Tcl_DoOneEvent</code> or <code>Tcl_ServiceAll</code>. </p>
<p> In addition to the generic procedure <code>Tcl_SetMaxBlockTime</code>, other platform-specific procedures may also be available for <i>setupProc</i>, if there is additional information needed by <code>Tcl_WaitForEvent</code> on that platform. For example, on Unix systems the <code>Tcl_CreateFileHandler</code> interface can be used to wait for file events. </p>
<p> The second procedure provided by each event source is its check procedure, indicated by the <i>checkProc</i> argument to <code>Tcl_CreateEventSource</code>. <i>CheckProc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_EventCheckProc(
 ClientData <i>clientData</i>,
 int <i>flags</i>);</pre>
</dl>
<p> The arguments to this procedure are the same as those for <i>setupProc</i>. <code>CheckProc</code> is invoked by <code>Tcl_DoOneEvent</code> after it has waited for events. Presumably at least one event source is now prepared to queue an event. <code>Tcl_DoOneEvent</code> calls each of the event sources in turn, so they all have a chance to queue any events that are ready. The check procedure does two things. First, it must see if any events have triggered. Different event sources do this in different ways. </p>
<p> If an event source&#8217;s check procedure detects an interesting event, it must add the event to Tcl&#8217;s event queue. To do this, the event source calls <code>Tcl_QueueEvent</code>. The <i>evPtr</i> argument is a pointer to a dynamically allocated structure containing the event (see below for more information on memory management issues). Each event source can define its own event structure with whatever information is relevant to that event source. However, the first element of the structure must be a structure of type <code>Tcl_Event</code>, and the address of this structure is used when communicating between the event source and the rest of the notifier. A <code>Tcl_Event</code> has the following definition:</p>
<dl COMPACT>
<dd>
<pre>typedef struct {
 Tcl_EventProc *<i>proc</i>;
 struct Tcl_Event *<i>nextPtr</i>;
} Tcl_Event;</pre>
</dl>
<p> The event source must fill in the <i>proc</i> field of the event before calling <code>Tcl_QueueEvent</code>. The <i>nextPtr</i> is used to link together the events in the queue and should not be modified by the event source. </p>
<p> An event may be added to the queue at any of three positions, depending on the <i>position</i> argument to <code>Tcl_QueueEvent</code>:</p>
<dl COMPACT>
<dt><code>TCL_QUEUE_TAIL</code></p>
<dd>Add the event at the back of the queue, so that all other pending events will be serviced first. This is almost always the right place for new events.</p>
<dt><code>TCL_QUEUE_HEAD</code></p>
<dd>Add the event at the front of the queue, so that it will be serviced before all other queued events.</p>
<dt><code>TCL_QUEUE_MARK</code></p>
<dd>Add the event at the front of the queue, unless there are other events at the front whose position is <code>TCL_QUEUE_MARK</code>; if so, add the new event just after all other <code>TCL_QUEUE_MARK</code> events. This value of <i>position</i> is used to insert an ordered sequence of events at the front of the queue, such as a series of Enter and Leave events synthesized during a grab or ungrab operation in Tk.</dl>
<p> When it is time to handle an event from the queue (steps 1 and 4 above) <code>Tcl_ServiceEvent</code> will invoke the <i>proc</i> specified in the first queued <code>Tcl_Event</code> structure. <i>Proc</i> must match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_EventProc(
 Tcl_Event *<i>evPtr</i>,
 int <i>flags</i>);</pre>
</dl>
<p> The first argument to <i>proc</i> is a pointer to the event, which will be the same as the first argument to the <code>Tcl_QueueEvent</code> call that added the event to the queue. The second argument to <i>proc</i> is the <i>flags</i> argument for the current call to <code>Tcl_ServiceEvent</code>; this is used by the event source to return immediately if its events are not relevant. </p>
<p> It is up to <i>proc</i> to handle the event, typically by invoking one or more Tcl commands or C-level callbacks. Once the event source has finished handling the event it returns 1 to indicate that the event can be removed from the queue. If for some reason the event source decides that the event cannot be handled at this time, it may return 0 to indicate that the event should be deferred for processing later; in this case <code>Tcl_ServiceEvent</code> will go on to the next event in the queue and attempt to service it. There are several reasons why an event source might defer an event. One possibility is that events of this type are excluded by the <i>flags</i> argument. For example, the file event source will always return 0 if the <code>TCL_FILE_EVENTS</code> bit is not set in <i>flags</i>. Another example of deferring events happens in Tk if <code>Tk_RestrictEvents</code> has been invoked to defer certain kinds of window events. </p>
<p> When <i>proc</i> returns 1, <code>Tcl_ServiceEvent</code> will remove the event from the event queue and free its storage. Note that the storage for an event must be allocated by the event source (using <code>Tcl_Alloc</code> or the Tcl macro <code>ckalloc</code>) before calling <code>Tcl_QueueEvent</code>, but it will be freed by <code>Tcl_ServiceEvent</code>, not by the event source. </p>
<p> Threaded applications work in a similar manner, except that there is a separate event queue for each thread containing a Tcl interpreter. Calling <code>Tcl_QueueEvent</code> in a multithreaded application adds an event to the current thread&#8217;s queue. To add an event to another thread&#8217;s queue, use <code>Tcl_ThreadQueueEvent</code>. <code>Tcl_ThreadQueueEvent</code> accepts as an argument a Tcl_ThreadId argument, which uniquely identifies a thread in a Tcl application. To obtain the Tcl_ThreadID for the current thread, use the <code>Tcl_GetCurrentThread</code> procedure. (A thread would then need to pass this identifier to other threads for those threads to be able to add events to its queue.) After adding an event to another thread&#8217;s queue, you then typically need to call <code>Tcl_ThreadAlert</code> to &#8220;wake up&#8221; that thread&#8217;s notifier to alert it to the new event. </p>
<p> <code>Tcl_DeleteEvents</code> can be used to explicitly remove one or more events from the event queue. <code>Tcl_DeleteEvents</code> calls <i>proc</i> for each event in the queue, deleting those for with the procedure returns 1. Events for which the procedure returns 0 are left in the queue. <i>Proc</i> should match the following prototype:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_EventDeleteProc(
 Tcl_Event *<i>evPtr</i>,
 ClientData <i>clientData</i>);</pre>
</dl>
<p> The <i>clientData</i> argument will be the same as the <i>clientData</i> argument to <code>Tcl_DeleteEvents</code>; it is typically used to point to private information managed by the event source. The <i>evPtr</i> will point to the next event in the queue. </p>
<p> <code>Tcl_DeleteEventSource</code> deletes an event source. The <i>setupProc</i>, <i>checkProc</i>, and <i>clientData</i> arguments must exactly match those provided to the <code>Tcl_CreateEventSource</code> for the event source to be deleted. If no such source exists, <code>Tcl_DeleteEventSource</code> has no effect. </p>
<h2>Creating A New Notifier</h2>
<p>The notifier consists of all the procedures described in this manual entry, plus <code>Tcl_DoOneEvent</code> and <code>Tcl_Sleep</code>, which are available on all platforms, and <code>Tcl_CreateFileHandler</code> and <code>Tcl_DeleteFileHandler</code>, which are Unix-specific. Most of these procedures are generic, in that they are the same for all notifiers. However, none of the procedures are notifier-dependent: <code>Tcl_InitNotifier</code>, <code>Tcl_AlertNotifier</code>, <code>Tcl_FinalizeNotifier</code>, <code>Tcl_SetTimer</code>, <code>Tcl_Sleep</code>, <code>Tcl_WaitForEvent</code>, <code>Tcl_CreateFileHandler</code>, <code>Tcl_DeleteFileHandler</code> and <code>Tcl_ServiceModeHook</code>. To support a new platform or to integrate Tcl with an application-specific event loop, you must write new versions of these procedures. </p>
<p> <code>Tcl_InitNotifier</code> initializes the notifier state and returns a handle to the notifier state. Tcl calls this procedure when initializing a Tcl interpreter. Similarly, <code>Tcl_FinalizeNotifier</code> shuts down the notifier, and is called by <code>Tcl_Finalize</code> when shutting down a Tcl interpreter. </p>
<p> <code>Tcl_WaitForEvent</code> is the lowest-level procedure in the notifier; it is responsible for waiting for an &#8220;interesting&#8221; event to occur or for a given time to elapse. Before <code>Tcl_WaitForEvent</code> is invoked, each of the event sources&#8217; setup procedure will have been invoked. The <i>timePtr</i> argument to <code>Tcl_WaitForEvent</code> gives the maximum time to block for an event, based on calls to <code>Tcl_SetMaxBlockTime</code> made by setup procedures and on other information (such as the <code>TCL_DONT_WAIT</code> bit in <i>flags</i>). </p>
<p> Ideally, <code>Tcl_WaitForEvent</code> should only wait for an event to occur; it should not actually process the event in any way. Later on, the event sources will process the raw events and create Tcl_Events on the event queue in their <i>checkProc</i> procedures. However, on some platforms (such as Windows) this is not possible; events may be processed in <code>Tcl_WaitForEvent</code>, including queuing Tcl_Events and more (for example, callbacks for native widgets may be invoked). The return value from <code>Tcl_WaitForEvent</code> must be either 0, 1, or -1. On platforms such as Windows where events get processed in <code>Tcl_WaitForEvent</code>, a return value of 1 means that there may be more events still pending that have not been processed. This is a sign to the caller that it must call <code>Tcl_WaitForEvent</code> again if it wants all pending events to be processed. A 0 return value means that calling <code>Tcl_WaitForEvent</code> again will not have any effect: either this is a platform where <code>Tcl_WaitForEvent</code> only waits without doing any event processing, or <code>Tcl_WaitForEvent</code> knows for sure that there are no additional events to process (e.g. it returned because the time elapsed). Finally, a return value of -1 means that the event loop is no longer operational and the application should probably unwind and terminate. Under Windows this happens when a WM_QUIT message is received; under Unix it happens when <code>Tcl_WaitForEvent</code> would have waited forever because there were no active event sources and the timeout was infinite. </p>
<p> <code>Tcl_AlertNotifier</code> is used in multithreaded applications to allow any thread to &#8220;wake up&#8221; the notifier to alert it to new events on its queue. <code>Tcl_AlertNotifier</code> requires as an argument the notifier handle returned by <code>Tcl_InitNotifier</code>. </p>
<p> If the notifier will be used with an external event loop, then it must also support the <code>Tcl_SetTimer</code> interface. <code>Tcl_SetTimer</code> is invoked by <code>Tcl_SetMaxBlockTime</code> whenever the maximum blocking time has been reduced. <code>Tcl_SetTimer</code> should arrange for the external event loop to invoke <code>Tcl_ServiceAll</code> after the specified interval even if no events have occurred. This interface is needed because <code>Tcl_WaitForEvent</code> is not invoked when there is an external event loop. If the notifier will only be used from <code>Tcl_DoOneEvent</code>, then <code>Tcl_SetTimer</code> need not do anything. </p>
<p> <code>Tcl_ServiceModeHook</code> is called by the platform-independent portion of the notifier when client code makes a call to <code>Tcl_SetServiceMode</code>. This hook is provided to support operating systems that require special event handling when the application is in a modal loop (the Windows notifier, for instance, uses this hook to create a communication window). </p>
<p> On Unix systems, the file event source also needs support from the notifier. The file event source consists of the <code>Tcl_CreateFileHandler</code> and <code>Tcl_DeleteFileHandler</code> procedures, which are described in the <code>Tcl_CreateFileHandler</code> manual page. </p>
<p> The <code>Tcl_Sleep</code> and <code>Tcl_DoOneEvent</code> interfaces are described in their respective manual pages. </p>
<p> The easiest way to create a new notifier is to look at the code for an existing notifier, such as the files <code>unix/tclUnixNotfy.c</code> or <code>win/tclWinNotify.c</code> in the Tcl source distribution. </p>
<h2>Replacing The Notifier</h2>
<p>A notifier that has been written according to the conventions above can also be installed in a running process in place of the standard notifier. This mechanism is used so that a single executable can be used (with the standard notifier) as a stand-alone program and reused (with a replacement notifier in a loadable extension) as an extension to another program, such as a Web browser plugin. </p>
<p> To do this, the extension makes a call to <code>Tcl_SetNotifier</code> passing a pointer to a <code>Tcl_NotifierProcs</code> data structure. The structure has the following layout:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_NotifierProcs {
 Tcl_SetTimerProc *setTimerProc;
 Tcl_WaitForEventProc *waitForEventProc;
 Tcl_CreateFileHandlerProc *createFileHandlerProc;
 Tcl_DeleteFileHandlerProc *deleteFileHandlerProc;
 Tcl_InitNotifierProc *initNotifierProc;
 Tcl_FinalizeNotifierProc *finalizeNotifierProc;
 Tcl_AlertNotifierProc *alertNotifierProc;
 Tcl_ServiceModeHookProc *serviceModeHookProc;
} Tcl_NotifierProcs;</pre>
</dl>
<p> Following the call to <code>Tcl_SetNotifier</code>, the pointers given in the <code>Tcl_NotifierProcs</code> structure replace whatever notifier had been installed in the process. </p>
<p> It is extraordinarily unwise to replace a running notifier. Normally, <code>Tcl_SetNotifier</code> should be called at process initialization time before the first call to <code>Tcl_InitNotifier</code>. </p>
<h2>External Event Loops</h2>
<p>The notifier interfaces are designed so that Tcl can be embedded into applications that have their own private event loops. In this case, the application does not call <code>Tcl_DoOneEvent</code> except in the case of recursive event loops such as calls to the Tcl commands <code>update</code> or <code>vwait</code>. Most of the time is spent in the external event loop of the application. In this case the notifier must arrange for the external event loop to call back into Tcl when something happens on the various Tcl event sources. These callbacks should arrange for appropriate Tcl events to be placed on the Tcl event queue. </p>
<p> Because the external event loop is not calling <code>Tcl_DoOneEvent</code> on a regular basis, it is up to the notifier to arrange for <code>Tcl_ServiceEvent</code> to be called whenever events are pending on the Tcl event queue. The easiest way to do this is to invoke <code>Tcl_ServiceAll</code> at the end of each callback from the external event loop. This will ensure that all of the event sources are polled, any queued events are serviced, and any pending idle handlers are processed before returning control to the application. In addition, event sources that need to poll for events can call <code>Tcl_SetMaxBlockTime</code> to force the external event loop to call Tcl even if no events are available on the system event queue. </p>
<p> As a side effect of processing events detected in the main external event loop, Tcl may invoke <code>Tcl_DoOneEvent</code> to start a recursive event loop in commands like <code>vwait</code>. <code>Tcl_DoOneEvent</code> will invoke the external event loop, which will result in callbacks as described in the preceding paragraph, which will result in calls to <code>Tcl_ServiceAll</code>. However, in these cases it is undesirable to service events in <code>Tcl_ServiceAll</code>. Servicing events there is unnecessary because control will immediately return to the external event loop and hence to <code>Tcl_DoOneEvent</code>, which can service the events itself. Furthermore, <code>Tcl_DoOneEvent</code> is supposed to service only a single event, whereas <code>Tcl_ServiceAll</code> normally services all pending events. To handle this situation, <code>Tcl_DoOneEvent</code> sets a flag for <code>Tcl_ServiceAll</code> that causes it to return without servicing any events. This flag is called the <i>service mode</i>; <code>Tcl_DoOneEvent</code> restores it to its previous value before it returns. </p>
<p> In some cases, however, it may be necessary for <code>Tcl_ServiceAll</code> to service events even when it has been invoked from <code>Tcl_DoOneEvent</code>. This happens when there is yet another recursive event loop invoked via an event handler called by <code>Tcl_DoOneEvent</code> (such as one that is part of a native widget). In this case, <code>Tcl_DoOneEvent</code> may not have a chance to service events so <code>Tcl_ServiceAll</code> must service them all. Any recursive event loop that calls an external event loop rather than <code>Tcl_DoOneEvent</code> must reset the service mode so that all events get processed in <code>Tcl_ServiceAll</code>. This is done by invoking the <code>Tcl_SetServiceMode</code> procedure. If <code>Tcl_SetServiceMode</code> is passed <code>TCL_SERVICE_NONE</code>, then calls to <code>Tcl_ServiceAll</code> will return immediately without processing any events. If <code>Tcl_SetServiceMode</code> is passed <code>TCL_SERVICE_ALL</code>, then calls to <code>Tcl_ServiceAll</code> will behave normally. <code>Tcl_SetServiceMode</code> returns the previous value of the service mode, which should be restored when the recursive loop exits. <code>Tcl_GetServiceMode</code> returns the current value of the service mode. </p>
<h2>See Also</h2>
<p><code>Tcl_CreateFileHandler</code>, <code>Tcl_DeleteFileHandler</code>, <code>Tcl_Sleep</code>, <code>Tcl_DoOneEvent</code>, <code><a href="/docs/linux/man/3-thread/">Thread</a>(3)</code></p>
<h2>Keywords</h2>
<p>event, notifier, event queue, event sources, file events, timer, idle, service mode, threads</p>
