---
title: "sd_journal_append-2(3)"
name: "sd_journal_append-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_append-2/"
---

sd_journal_get_fd, sd_journal_get_events, sd_journal_get_timeout, sd_journal_process, sd_journal_wait, sd_journal_reliable_fd, SD_JOURNAL_NOP, SD_JOURNAL_APPEND, SD_JOURNAL_INVALIDATE - Journal change notification interface 

<h2>Synopsis</h2><pre>#include &lt;systemd/sd-journal.h&gt;</pre><dl COMPACT><dt> <b>int sd_journal_get_fd(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b>
<dt> <b>int sd_journal_get_events(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b>
<dt> <b>int sd_journal_get_timeout(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, uint64_t&nbsp;<wbr>*</b><i>timeout_usec</i><b>);</b>
<dt> <b>int sd_journal_process(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b>
<dt> <b>int sd_journal_wait(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, uint64_t&nbsp;<wbr></b><i>timeout_usec</i><b>);</b>
<dt> <b>int sd_journal_reliable_fd(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b></dl><h2>Description</h2><b>sd_journal_get_fd()</b>
<dd>returns a file descriptor that may be asynchronously polled in an external event loop and is signaled as soon as the journal changes, because new entries or files were added, rotation took place, or files have been deleted, and similar. The file descriptor is suitable for usage in <b><a HREF="/docs/linux/man/2-poll/">poll</a></b>(2). Use <b>sd_journal_get_events()</b> for an events mask to watch for. The call takes one argument: the journal context object. Note that not all file systems are capable of generating the necessary events for wakeups from this file descriptor for changes to be noticed immediately. In particular network files systems do not generate suitable file change events in all cases. Cases like this can be detected with <b>sd_journal_reliable_fd()</b>, below. <b>sd_journal_get_timeout()</b> will ensure in these cases that wake-ups happen frequently enough for changes to be noticed, although with a certain latency. 

 <b>sd_journal_get_events()</b> will return the <b>poll()</b> mask to wait for. This function will return a combination of <b>POLLIN</b> and <b>POLLOUT</b> and similar to fill into the &quot;.events&quot; field of <i>struct pollfd</i>. 

 <b>sd_journal_get_timeout()</b> will return a timeout value for usage in <b>poll()</b>. This returns a value in microseconds since the epoch of <b>CLOCK_MONOTONIC</b> for timing out <b>poll()</b> in <i>timeout_usec</i>. See <b><a HREF="/docs/linux/man/2-clock_gettime/">clock_gettime</a></b>(2) for details about <b>CLOCK_MONOTONIC</b>. If there is no timeout to wait for, this will fill in <b>(uint64_t) -1</b> instead. Note that <b>poll()</b> takes a relative timeout in milliseconds rather than an absolute timeout in microseconds. To convert the absolute 'us' timeout into relative 'ms', use code like the following: 

<dl COMPACT><dd><pre>uint64_t t;
int msec;
sd_journal_get_timeout(m, &amp;t);
if (t == (uint64_t) -1)
 msec = -1;
else {
 struct timespec ts;
 uint64_t n;
 clock_getttime(CLOCK_MONOTONIC, &amp;ts);
 n = (uint64_t) ts.tv_sec * 1000000 + ts.tv_nsec / 1000;
 msec = t &gt; n ? (int) ((t - n + 999) / 1000) : 0;
}</pre></dl>
 

 The code above does not do any error checking for brevity's sake. The calculated <i>msec</i> integer can be passed directly as <b>poll()</b>'s timeout parameter. 

 After each <b>poll()</b> wake-up <b>sd_journal_process()</b> needs to be called to process events. This call will also indicate what kind of change has been detected (see below; note that spurious wake-ups are possible). 

 A synchronous alternative for using <b>sd_journal_get_fd()</b>, <b>sd_journal_get_events()</b>, <b>sd_journal_get_timeout()</b> and <b>sd_journal_process()</b> is <b>sd_journal_wait()</b>. It will synchronously wait until the journal gets changed. The maximum time this call sleeps may be controlled with the <i>timeout_usec</i> parameter. Pass <b>(uint64_t) -1</b> to wait indefinitely. Internally this call simply combines <b>sd_journal_get_fd()</b>, <b>sd_journal_get_events()</b>, <b>sd_journal_get_timeout()</b>, <b>poll()</b> and <b>sd_journal_process()</b> into one. 

 <b>sd_journal_reliable_fd()</b> may be used to check whether the wakeup events from the file descriptor returned by <b>sd_journal_get_fd()</b> are known to be immediately triggered. On certain file systems where file change events from the OS are not available (such as NFS) changes need to be polled for repeatedly, and hence are detected only with a certain latency. This call will return a positive value if the journal changes are detected immediately and zero when they need to be polled for and hence might be noticed only with a certain latency. Note that there's usually no need to invoke this function directly as <b>sd_journal_get_timeout()</b> on these file systems will ask for timeouts explicitly anyway.
<h2>Return Value</h2><b>sd_journal_get_fd()</b> returns a valid file descriptor on success or a negative errno-style error code. 

 <b>sd_journal_get_events()</b> returns a combination of <b>POLLIN</b>, <b>POLLOUT</b> and suchlike on success or a negative errno-style error code. 

 <b>sd_journal_reliable_fd()</b> returns a positive integer if the file descriptor returned by <b>sd_journal_get_fd()</b> will generate wake-ups immediately for all journal changes. Returns 0 if there might be a latency involved. 

 <b>sd_journal_process()</b> and <b>sd_journal_wait()</b> return one of <b>SD_JOURNAL_NOP</b>, <b>SD_JOURNAL_APPEND</b> or <b>SD_JOURNAL_INVALIDATE</b> on success or a negative errno-style error code. If <b>SD_JOURNAL_NOP</b> is returned, the journal did not change since the last invocation. If <b>SD_JOURNAL_APPEND</b> is returned, new entries have been appended to the end of the journal. If <b>SD_JOURNAL_INVALIDATE</b>, journal files were added or removed (possibly due to rotation). In the latter event, live-view UIs should probably refresh their entire display, while in the case of <b>SD_JOURNAL_APPEND</b>, it is sufficient to simply continue reading at the previous end of the journal.
<h2>Notes</h2>The <b>sd_journal_get_fd()</b>, <b>sd_journal_get_events()</b>, <b>sd_journal_reliable_fd()</b>, <b>sd_journal_process()</b> and <b>sd_journal_wait()</b> interfaces are available as a shared library, which can be compiled and linked to with the <b>libsystemd</b>&nbsp;<wbr><b><a HREF="/docs/linux/man/1-pkg-config/">pkg-config</a></b>(1) file.
<h2>Examples</h2>Iterating through the journal, in a live view tracking all changes: 

<dl COMPACT><dd><pre>#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;systemd/sd-journal.h&gt;
int main(int argc, char *argv[]) {
 int r;
 sd_journal *j;
 r = sd_journal_open(&amp;j, SD_JOURNAL_LOCAL_ONLY);
 if (r &lt; 0) {
 fprintf(stderr, &quot;Failed to open journal: %s\n&quot;, strerror(-r));
 return 1;
 }
 for (;;) {
 const void *d;
 size_t l;
 r = sd_journal_next(j);
 if (r &lt; 0) {
 fprintf(stderr, &quot;Failed to iterate to next entry: %s\n&quot;, strerror(-r));
 break;
 }
 if (r == 0) {
 /* Reached the end, let's wait for changes, and try again */
 r = sd_journal_wait(j, (uint64_t) -1);
 if (r &lt; 0) {
 fprintf(stderr, &quot;Failed to wait for changes: %s\n&quot;, strerror(-r));
 break;
 }
 continue;
 }
 r = sd_journal_get_data(j, &quot;MESSAGE&quot;, &amp;d, &amp;l);
 if (r &lt; 0) {
 fprintf(stderr, &quot;Failed to read message field: %s\n&quot;, strerror(-r));
 continue;
 }
 printf(&quot;%.*s\n&quot;, (int) l, (const char*) d);
 }
 sd_journal_close(j);
 return 0;
}</pre></dl>
 

 Waiting with <b>poll()</b> (this example lacks all error checking for the sake of simplicity): 

<dl COMPACT><dd><pre>#include &lt;poll.h&gt;
#include &lt;systemd/sd-journal.h&gt;
int wait_for_changes(sd_journal *j) {
 struct pollfd pollfd;
 int msec;
 sd_journal_get_timeout(m, &amp;t);
 if (t == (uint64_t) -1)
 msec = -1;
 else {
 struct timespec ts;
 uint64_t n;
 clock_getttime(CLOCK_MONOTONIC, &amp;ts);
 n = (uint64_t) ts.tv_sec * 1000000 + ts.tv_nsec / 1000;
 msec = t &gt; n ? (int) ((t - n + 999) / 1000) : 0;
 }
 pollfd.fd = sd_journal_get_fd(j);
 pollfd.events = sd_journal_get_events(j);
 poll(&amp;pollfd, 1, msec);
 return sd_journal_process(j);
}</pre></dl><h2>See Also</h2><b><a HREF="/docs/linux/man/1-systemd/">systemd</a></b>(1), <b><a HREF="/docs/linux/man/3-sd-journal/">sd-journal</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></b>(3), <b><a HREF="/docs/linux/man/2-poll/">poll</a></b>(2), <b><a HREF="/docs/linux/man/2-clock_gettime/">clock_gettime</a></b>(2)
