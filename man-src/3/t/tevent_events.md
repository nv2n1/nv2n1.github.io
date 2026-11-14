---
title: "tevent_events(3)"
name: "tevent_events"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tevent_events/"
description: "tevent_events – Chapter 2: Tevent events"
---

<p>tevent_events &#8211; Chapter 2: Tevent events</p>
<h2>Tevent events</h2>
<p>Ok, after reading previous chapter we can start doing something useful. So, the way of creating events is similar for all types &#8211; signals, file descriptors, time or immediate events. At the beginning it is good to know about some typedefs which are set in tevent library and which specify the arguments for each callback. These callbacks are: </p>
<dl>
<dt>&bull;</p>
<dd><code>tevent_timer_handler_t()</code></p>
<dt>&bull;</p>
<dd><code>tevent_immediate_handler_t()</code></p>
<dt>&bull;</p>
<dd><code>tevent_signal_handler_t()</code></p>
<dt>&bull;</p>
<dd><code>tevent_fd_handler_t()</code></dl>
<p> According their names it is obvious that for creating callback for e.g. time event, tevent_timer_handler_t will be used. </p>
<p> The best way how to introduce registering an event and setting up a callback would be example, so examples describing all the types of events follow.</p>
<h3>Time event</h3>
<p>This example shows how to set up an event which will be repeated for a minute with interval of 2 seconds (will be triggered 30 times). After exceeding this limit, the event loop will finish and all the memory resources will be freed. This is just example describing repeated activity, nothing usefull is done within foo function </p>
<pre>#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;tevent.h&gt;
#include &lt;sys/time.h&gt;
struct state {
 struct timeval endtime;
 int counter;
 TALLOC_CTX *ctx;
};
static void callback(struct tevent_context *ev, struct tevent_timer *tim,
 struct timeval current_time, void *private_data)
{
 struct state *data = talloc_get_type_abort(private_data, struct state);
 struct tevent_timer *time_event;
 struct timeval schedule;
 printf(&quot;Data value: %d, data-&gt;counter);
 data-&gt;counter += 1; // increase counter
 // if time has not reached its limit, set another event
 if (tevent_timeval_compare(&amp;current_time, &amp;(data-&gt;endtime)) &lt; 0) {
 // do something
 // set repeat with delay 2 seconds
 schedule = tevent_timeval_current_ofs(2, 0);
 time_event = tevent_add_timer(ev, data-&gt;ctx, schedule, callback, data);
 if (time_event == NULL) { // error ...
 fprintf(stderr, &quot;MEMORY PROBLEM);
 return;
 }
 } else {
 // time limit exceeded
 }
}
int main(void) {
 struct tevent_context *event_ctx;
 TALLOC_CTX *mem_ctx;
 struct tevent_timer *time_event;
 struct timeval schedule;
 mem_ctx = talloc_new(NULL); // parent
 event_ctx = tevent_context_init(mem_ctx);
 struct state *data = talloc(mem_ctx, struct state);
 schedule = tevent_timeval_current_ofs(2, 0); // +2 second time value
 data-&gt;endtime = tevent_timeval_add(&amp;schedule, 60, 0); // one minute time limit
 data-&gt;ctx = mem_ctx;
 data-&gt;counter = 0;
 // add time event
 time_event = tevent_add_timer(event_ctx, mem_ctx, schedule, callback, data);
 if (time_event == NULL) {
 fprintf(stderr, &quot;FAILED);
 return EXIT_FAILURE;
 }
 tevent_loop_wait(event_ctx);
 talloc_free(mem_ctx);
 return EXIT_SUCCESS;
}</pre>
<p>Variable counter is only used for counting the number of triggered functions. List of all available functions which tevent offers for working with time are listed here together with their description. More detailed view at these functions is unnecessary because their purpose and usage is quite simple and clear.</p>
<h3>Immediate event</h3>
<p>These events are, as their name indicates, activated and performed immediately. It means that this kind of events have priority over others (except signal events). So if there is a bulk of events registered and after that a tevent loop is launched, then all the immediate events will be triggered before the other events. Except other immediate events (and signal events) because they are also processed sequentially &#8211; according the order they were scheduled. Signals have the highest priority and therefore they are processed preferentially. Therefore the expression immediate may not correspond exactly to the dictionary definition of &#8216;something without delay&#8217; but rather &#8216;as soon as possible&#8217; after all preceding immediate events. </p>
<p> For creating an immediate event there is a small different which lies in the fact that the creation of such event is done in 2 steps. One represents the creation (memory allocation), the second one represents registering as the event within some tevent context. </p>
<pre>struct tevent_immediate *run(TALLOC_CTX* mem_ctx,
 struct tevent_context event_ctx,
 void * data)
{
 struct tevent_immediate *im;
 im = tevent_create_immediate(mem_ctx);
 if (im == NULL) {
 return NULL;
 }
 tevent_schedule_immediate(im, event_ctx, foo, data);
 return im;
}</pre>
<p>Example which may be compiled and run representing the creation of immediate event. </p>
<pre>#include &lt;stdio.h&gt;
#include &lt;unistd.h&gt;
#include &lt;tevent.h&gt;
struct info_struct {
 int counter;
};
static void foo(struct tevent_context *ev, struct tevent_immediate *im,
 void *private_data)
{
 struct info_struct *data = talloc_get_type_abort(private_data, struct info_struct);
 printf(&quot;Data value: %d, data-&gt;counter);
}
int main (void) {
 struct tevent_context *event_ctx;
 TALLOC_CTX *mem_ctx;
 struct tevent_immediate *im;
 printf(&quot;INIT);
 mem_ctx = talloc_new(NULL);
 event_ctx = tevent_context_init(mem_ctx);
 struct info_struct *data = talloc(mem_ctx, struct info_struct);
 // setting up private data
 data-&gt;counter = 1;
 // first immediate event
 im = tevent_create_immediate(mem_ctx);
 if (im == NULL) {
 fprintf(stderr, &quot;FAILED);
 return EXIT_FAILURE;
 }
 tevent_schedule_immediate(im, event_ctx, foo, data);
 tevent_loop_wait(event_ctx);
 talloc_free(mem_ctx);
 return 0;
}</pre>
<h3>Signal event</h3>
<p>This is an alternative to standard C library functions signal() or sigaction(). The main difference that distinguishes these ways of treating signals is their setting up of handlers for different time intervals of the running program. </p>
<p> While standard C library methods for dealing with signals offer sufficient tools for most cases, they are inadequate for handling signals within the tevent loop. It could be necessary to finish certain tevent requests within the tevent loop without interruption. If a signal was sent to a program at a moment when the tevent loop is in progress, a standard signal handler would not return processing to the application at the very same place and it would quit the tevent loop for ever. In such cases, tevent signal handlers offer the possibility of dealing with these signals by masking them from the rest of application and not quitting the loop, so the other events can still be processed. </p>
<p> Tevent offers also a control function, which enables us to verify whether it is possible to handle signals via tevent, is defined within tevent library and it returns a boolean value revealing the result of the verification. </p>
<pre>bool tevent_signal_support (struct tevent_context *ev)</pre>
<p>Checking for signal support is not necessary, but if it is not guaranteed, this is a good and easy control to prevent unexpected behaviour or failure of the program occurring. Such a test of course does not have to be run every single time you wish to create a signal handler, but simply at the beginning &#8211; during the initialization procedures of the program. Afterthat, simply adapt to each situation that arises. </p>
<pre>#include &lt;stdio.h&gt;
#include &lt;tevent.h&gt;
#include &lt;signal.h&gt;
static void handler(struct tevent_context *ev,
 struct tevent_signal *se,
 int signum,
 int count,
 void *siginfo,
 void *private_data)
{
 // Do something usefull
 printf(&quot;handling signal...);
 exit(EXIT_SUCCESS);
}
int main (void)
{
 struct tevent_context *event_ctx;
 TALLOC_CTX *mem_ctx;
 struct tevent_signal *sig;
 mem_ctx = talloc_new(NULL); //parent
 if (mem_ctx == NULL) {
 fprintf(stderr, &quot;FAILED);
 return EXIT_FAILURE;
 }
 event_ctx = tevent_context_init(mem_ctx);
 if (event_ctx == NULL) {
 fprintf(stderr, &quot;FAILED);
 return EXIT_FAILURE;
 }
 if (tevent_signal_support(event_ctx)) {
 // create signal event
 sig = tevent_add_signal(event_ctx, mem_ctx, SIGINT, 0, handler, NULL);
 if (sig == NULL) {
 fprintf(stderr, &quot;FAILED);
 return EXIT_FAILURE;
 }
 tevent_loop_wait(event_ctx);
 }
 talloc_free(mem_ctx);
 return EXIT_SUCCESS;
}</pre>
<h3>File descriptor event</h3>
<p>Support of events on file descriptors is mainly useful for socket communication but it certainly works flawlessly with standard streams (stdin, stdout, stderr) as well. Working asynchronously with file descriptors enables switching within processing I/O operations. This ability may rise with a greater number of I/O operations and such overlapping leads to enhancement of the throughput. </p>
<p> There are several other functions included in tevent API related to handling file descriptors (there are too many functions defined within tevent therefore just some of them are fully described within this thesis. The declaration of the rest can be easily found on the library’s website or directly from the source code): </p>
<dl>
<dt>&bull;</p>
<dd><code>tevent_fd_set_close_fn()</code> &#8211; can add another function to be called at the moment when a structure tevent fd is freed.</p>
<dt>&bull;</p>
<dd><code>tevent_fd_set_auto_close()</code> &#8211; calling this function can simplify the maintenance of file descriptors, because it instructs tevent to close the appropriate file descriptor when the tevent fd structure is about to be freed.</p>
<dt>&bull;</p>
<dd><code>tevent_fd_get_flags()</code> &#8211; returns flags which are set on the file descriptor connected with this tevent fd structure.</p>
<dt>&bull;</p>
<dd><code>tevent_fd_set_flags()</code> &#8211; sets specified flags on the event’s file descriptor.</dl>
<pre>static void close_fd(struct tevent_context *ev, struct tevent_fd *fd_event,
 int fd, void *private_data)
{
 // processing when fd_event is freed
}
struct static void handler(struct tevent_context *ev,
 struct tevent_fd *fde,
 uint16_t flags,
 void *private_data)
{
 // handling event; reading from a file descriptor
 tevent_fd_set_close_fn (fd_event, close_fd);
}
int run(TALLOC_CTX *mem_ctx, struct tevent_context *event_ctx,
 int fd, uint16_t flags, char *buffer)
{
 struct tevent_fd* fd_event = NULL;
 if (flags &amp; TEVENT_FD_READ) {
 fd_event = tevent_add_fd(event_ctx,
 mem_ctx,
 fd,
 flags,
 handler,
 buffer);
 }
 if (fd_event == NULL) {
 // error handling
 }
 return tevent_loop_once();
}</pre>
<p>&nbsp;<wbr></p>
