---
title: "sd_journal_wait(3)"
name: "sd_journal_wait"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_wait/"
description: "sd_journal_get_fd, sd_journal_get_events, sd_journal_get_timeout, sd_journal_process, sd_journal_wait, sd_journal_reliable_fd, SD_JOURNAL_NOP, SD_JOURNAL_APPEND, SD_JOURNAL_INVALIDATE – Journal cha..."
---

<p>sd_journal_get_fd, sd_journal_get_events, sd_journal_get_timeout, sd_journal_process, sd_journal_wait, sd_journal_reliable_fd, SD_JOURNAL_NOP, SD_JOURNAL_APPEND, SD_JOURNAL_INVALIDATE &#8211; Journal change notification interface </p>
<h2>Synopsis</h2>
<pre>
#include &lt;systemd/sd-journal.h&gt;
</pre>
<dl COMPACT>
<dt> <code>int sd_journal_get_fd(sd_journal&nbsp;<wbr>*</code><i>j</i><code>);</code></p>
<dt> <code>int sd_journal_get_events(sd_journal&nbsp;<wbr>*</code><i>j</i><code>);</code></p>
<dt> <code>int sd_journal_get_timeout(sd_journal&nbsp;<wbr>*</code><i>j</i><code>, uint64_t&nbsp;<wbr>*</code><i>timeout_usec</i><code>);</code></p>
<dt> <code>int sd_journal_process(sd_journal&nbsp;<wbr>*</code><i>j</i><code>);</code></p>
<dt> <code>int sd_journal_wait(sd_journal&nbsp;<wbr>*</code><i>j</i><code>, uint64_t&nbsp;<wbr></code><i>timeout_usec</i><code>);</code></p>
<dt> <code>int sd_journal_reliable_fd(sd_journal&nbsp;<wbr>*</code><i>j</i><code>);</code></dl>
<h2>Description</h2>
<p> <code>sd_journal_get_fd()</code></p>
<dd>returns a file descriptor that may be asynchronously polled in an external event loop and is signaled as soon as the journal changes, because new entries or files were added, rotation took place, or files have been deleted, and similar. The file descriptor is suitable for usage in <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2). Use <code>sd_journal_get_events()</code> for an events mask to watch for. The call takes one argument: the journal context object. Note that not all file systems are capable of generating the necessary events for wakeups from this file descriptor for changes to be noticed immediately. In particular network files systems do not generate suitable file change events in all cases. Cases like this can be detected with <code>sd_journal_reliable_fd()</code>, below. <code>sd_journal_get_timeout()</code> will ensure in these cases that wake-ups happen frequently enough for changes to be noticed, although with a certain latency. </p>
<p> <code>sd_journal_get_events()</code> will return the <code>poll()</code> mask to wait for. This function will return a combination of <code>POLLIN</code> and <code>POLLOUT</code> and similar to fill into the &quot;.events&quot; field of <i>struct pollfd</i>. </p>
<p> <code>sd_journal_get_timeout()</code> will return a timeout value for usage in <code>poll()</code>. This returns a value in microseconds since the epoch of <code>CLOCK_MONOTONIC</code> for timing out <code>poll()</code> in <i>timeout_usec</i>. See <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) for details about <code>CLOCK_MONOTONIC</code>. If there is no timeout to wait for, this will fill in <code>(uint64_t) -1</code> instead. Note that <code>poll()</code> takes a relative timeout in milliseconds rather than an absolute timeout in microseconds. To convert the absolute &#8216;us&#8217; timeout into relative &#8216;ms&#8217;, use code like the following: </p>
<dl COMPACT>
<dt>
<dd>
<pre>
uint64_t t;
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
</pre>
</dl>
<p> The code above does not do any error checking for brevity&#8217;s sake. The calculated <i>msec</i> integer can be passed directly as <code>poll()</code>&#8216;s timeout parameter. </p>
<p> After each <code>poll()</code> wake-up <code>sd_journal_process()</code> needs to be called to process events. This call will also indicate what kind of change has been detected (see below; note that spurious wake-ups are possible). </p>
<p> A synchronous alternative for using <code>sd_journal_get_fd()</code>, <code>sd_journal_get_events()</code>, <code>sd_journal_get_timeout()</code> and <code>sd_journal_process()</code> is <code>sd_journal_wait()</code>. It will synchronously wait until the journal gets changed. The maximum time this call sleeps may be controlled with the <i>timeout_usec</i> parameter. Pass <code>(uint64_t) -1</code> to wait indefinitely. Internally this call simply combines <code>sd_journal_get_fd()</code>, <code>sd_journal_get_events()</code>, <code>sd_journal_get_timeout()</code>, <code>poll()</code> and <code>sd_journal_process()</code> into one. </p>
<p> <code>sd_journal_reliable_fd()</code> may be used to check whether the wakeup events from the file descriptor returned by <code>sd_journal_get_fd()</code> are known to be immediately triggered. On certain file systems where file change events from the OS are not available (such as NFS) changes need to be polled for repeatedly, and hence are detected only with a certain latency. This call will return a positive value if the journal changes are detected immediately and zero when they need to be polled for and hence might be noticed only with a certain latency. Note that there&#8217;s usually no need to invoke this function directly as <code>sd_journal_get_timeout()</code> on these file systems will ask for timeouts explicitly anyway.</p>
<h2>Return Value</h2>
<p> <code>sd_journal_get_fd()</code> returns a valid file descriptor on success or a negative errno-style error code. </p>
<p> <code>sd_journal_get_events()</code> returns a combination of <code>POLLIN</code>, <code>POLLOUT</code> and suchlike on success or a negative errno-style error code. </p>
<p> <code>sd_journal_reliable_fd()</code> returns a positive integer if the file descriptor returned by <code>sd_journal_get_fd()</code> will generate wake-ups immediately for all journal changes. Returns 0 if there might be a latency involved. </p>
<p> <code>sd_journal_process()</code> and <code>sd_journal_wait()</code> return one of <code>SD_JOURNAL_NOP</code>, <code>SD_JOURNAL_APPEND</code> or <code>SD_JOURNAL_INVALIDATE</code> on success or a negative errno-style error code. If <code>SD_JOURNAL_NOP</code> is returned, the journal did not change since the last invocation. If <code>SD_JOURNAL_APPEND</code> is returned, new entries have been appended to the end of the journal. If <code>SD_JOURNAL_INVALIDATE</code>, journal files were added or removed (possibly due to rotation). In the latter event, live-view UIs should probably refresh their entire display, while in the case of <code>SD_JOURNAL_APPEND</code>, it is sufficient to simply continue reading at the previous end of the journal.</p>
<h2>Notes</h2>
<p> The <code>sd_journal_get_fd()</code>, <code>sd_journal_get_events()</code>, <code>sd_journal_reliable_fd()</code>, <code>sd_journal_process()</code> and <code>sd_journal_wait()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>Examples</h2>
<p> Iterating through the journal, in a live view tracking all changes: </p>
<dl COMPACT>
<dt>
<dd>
<pre>
#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;systemd/sd-journal.h&gt;
int main(int argc, char *argv[]) {
  int r;
  sd_journal *j;
  r = sd_journal_open(&amp;j, SD_JOURNAL_LOCAL_ONLY);
  if (r &lt; 0) {
    fprintf(stderr, &quot;Failed to open journal: %s
&quot;, strerror(-r));
    return 1;
  }
  for (;;)  {
    const void *d;
    size_t l;
    r = sd_journal_next(j);
    if (r &lt; 0) {
      fprintf(stderr, &quot;Failed to iterate to next entry: %s
&quot;, strerror(-r));
      break;
    }
    if (r == 0) {
      /* Reached the end, let's wait for changes, and try again */
      r = sd_journal_wait(j, (uint64_t) -1);
      if (r &lt; 0) {
        fprintf(stderr, &quot;Failed to wait for changes: %s
&quot;, strerror(-r));
        break;
      }
      continue;
    }
    r = sd_journal_get_data(j, &quot;MESSAGE&quot;, &amp;d, &amp;l);
    if (r &lt; 0) {
      fprintf(stderr, &quot;Failed to read message field: %s
&quot;, strerror(-r));
      continue;
    }
    printf(&quot;%.*s
&quot;, (int) l, (const char*) d);
  }
  sd_journal_close(j);
  return 0;
}
</pre>
</dl>
<p> Waiting with <code>poll()</code> (this example lacks all error checking for the sake of simplicity): </p>
<dl COMPACT>
<dt>
<dd>
<pre>
#include &lt;poll.h&gt;
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
}
</pre>
</dl>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2)</p>
