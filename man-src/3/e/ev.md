---
title: "ev(3)"
name: "ev"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ev/"
description: "libev – a high performance full-featured event loop written in C"
---

<h2 class="name">NAME</h2>
<p> libev &#8211; a high performance full-featured event loop written in C </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ev.h&gt;
</code></pre>
<h3><font SIZE="-1">EXAMPLE</font> <font SIZE="-1">PROGRAM</font></h3>
<p>// a single header file is required<br />
#include &lt;ev.h&gt;<br />
#include &lt;stdio.h&gt; // for puts<br />
// every watcher type has its own typedef&#8217;d struct<br />
// with the name ev_TYPE<br />
ev_io stdin_watcher;<br />
ev_timer timeout_watcher;<br />
// all watcher callbacks have a similar signature<br />
// this callback is called when data is readable on stdin<br />
static void<br />
stdin_cb(EV_P_ ev_io *w, int revents)<br />
{<br />
    puts(&#8220;stdin ready&#8221;);<br />
    // for one-shot events, one must manually stop the watcher<br />
    // with its corresponding stop function.<br />
    ev_io_stop(EV_A_ w);<br />
    // this causes all nested ev_loop&#8217;s to stop iterating<br />
    ev_unloop(EV_A_ EVUNLOOP_ALL);<br />
}<br />
// another callback, this time for a time-out<br />
static void<br />
timeout_cb(EV_P_ ev_timer *w, int revents)<br />
{<br />
    puts(&#8220;timeout&#8221;);<br />
    // this causes the innermost ev_loop to stop iterating<br />
    ev_unloop(EV_A_ EVUNLOOP_ONE);<br />
}<br />
int main(void)<br />
{<br />
    // use the default event loop unless you have special needs<br />
    struct ev_loop *loop = ev_default_loop(0);<br />
    // initialise an io watcher, then start it<br />
    // this one will watch for stdin to become readable<br />
    ev_io_init(&amp;stdin_watcher, stdin_cb, /*STDIN_FILENO*/ 0, EV_READ);<br />
    ev_io_start(loop, &amp;stdin_watcher);<br />
    // initialise a timer watcher, then start it<br />
    // simple non-repeating 5.5 second timeout<br />
    ev_timer_init(&amp;timeout_watcher, timeout_cb, 5.5, 0.);<br />
    ev_timer_start(loop, &amp;timeout_watcher);<br />
    // now wait for events to arrive<br />
    ev_loop(loop, 0);<br />
    // unloop was called, so exit<br />
    return 0;<br />
}</p>
<h2>ABOUT THIS DOCUMENT</h2>
<p> This document documents the libev software package. </p>
<p> The newest version of this document is also available as an html-formatted web page you might find easier to navigate when reading it for the first time: &lt;<a rel="nofollow" href="http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod">http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod</a>&gt;. </p>
<p> While this document tries to be as complete as possible in documenting libev, its usage and the rationale behind its design, it is not a tutorial on event-based programming, nor will it introduce event-based programming with libev. </p>
<p> Familarity with event based programming techniques in general is assumed throughout this document.</p>
<h2>ABOUT LIBEV</h2>
<p> Libev is an event loop: you register interest in certain events (such as a file descriptor being readable or a timeout occurring), and it will manage these event sources and provide your program with events. </p>
<p> To do this, it must take more or less complete control over your process (or thread) by executing the <i>event loop</i> handler, and will then communicate events via a callback mechanism. </p>
<p> You register interest in certain events by registering so-called <i>event watchers</i>, which are relatively small C structures you initialise with the details of the event, and then hand it over to libev by <i>starting</i> the watcher.</p>
<h3><font SIZE="-1">FEATURES</font></h3>
<p> Libev supports <tt>&quot;select&quot;</tt>, <tt>&quot;poll&quot;</tt>, the Linux-specific <tt>&quot;epoll&quot;</tt>, the BSD-specific <tt>&quot;kqueue&quot;</tt> and the Solaris-specific event port mechanisms for file descriptor events (<tt>&quot;ev_io&quot;</tt>), the Linux <tt>&quot;inotify&quot;</tt> interface (for <tt>&quot;ev_stat&quot;</tt>), Linux eventfd/signalfd (for faster and cleaner inter-thread wakeup (<tt>&quot;ev_async&quot;</tt>)/signal handling (<tt>&quot;ev_signal&quot;</tt>)) relative timers (<tt>&quot;ev_timer&quot;</tt>), absolute timers with customised rescheduling (<tt>&quot;ev_periodic&quot;</tt>), synchronous signals (<tt>&quot;ev_signal&quot;</tt>), process status change events (<tt>&quot;ev_child&quot;</tt>), and event watchers dealing with the event loop mechanism itself (<tt>&quot;ev_idle&quot;</tt>, <tt>&quot;ev_embed&quot;</tt>, <tt>&quot;ev_prepare&quot;</tt> and <tt>&quot;ev_check&quot;</tt> watchers) as well as file watchers (<tt>&quot;ev_stat&quot;</tt>) and even limited support for fork events (<tt>&quot;ev_fork&quot;</tt>). </p>
<p> It also is quite fast (see this &lt;benchmark&gt; comparing it to libevent for example).</p>
<h3><font SIZE="-1">CONVENTIONS</font></h3>
<p> Libev is very configurable. In this manual the default (and most common) configuration will be described, which supports multiple event loops. For more info about various configuration options please have a look at <font SIZE="-1"><code>EMBED</code></font> section in this manual. If libev was configured without support for multiple event loops, then all functions taking an initial argument of name <tt>&quot;loop&quot;</tt> (which is always of type <tt>&quot;ev_loop *&quot;</tt>) will not have this argument.</p>
<h3><font SIZE="-1">TIME</font> <font SIZE="-1">REPRESENTATION</font></h3>
<p> Libev represents time as a single floating point number, representing the (fractional) number of seconds since the (<font SIZE="-1">POSIX</font>) epoch (somewhere near the beginning of 1970, details are complicated, don&#8217;t ask). This type is called <tt>&quot;ev_tstamp&quot;</tt>, which is what you should use too. It usually aliases to the <tt>&quot;double&quot;</tt> type in C. When you need to do any calculations on it, you should treat it as some floating point value. Unlike the name component <tt>&quot;stamp&quot;</tt> might indicate, it is also used for time differences throughout libev.</p>
<h2>ERROR HANDLING</h2>
<p> Libev knows three classes of errors: operating system errors, usage errors and internal errors (bugs). </p>
<p> When libev catches an operating system error it cannot handle (for example a system call indicating a condition libev cannot fix), it calls the callback set via <tt>&quot;ev_set_syserr_cb&quot;</tt>, which is supposed to fix the problem or abort. The default is to print a diagnostic message and to call <tt>&quot;abort ()&quot;</tt>. </p>
<p> When libev detects a usage error such as a negative timer interval, then it will print a diagnostic message and abort (via the <tt>&quot;assert&quot;</tt> mechanism, so <tt>&quot;NDEBUG&quot;</tt> will disable this checking): these are programming errors in the libev caller and need to be fixed there. </p>
<p> Libev also has a few internal error-checking <tt>&quot;assert&quot;</tt>ions, and also has extensive consistency checking code. These do not trigger under normal circumstances, as they indicate either a bug in libev or worse.</p>
<h2>GLOBAL FUNCTIONS</h2>
<p> These functions can be called anytime, even before initialising the library in any way.</p>
<dl>
<dt>ev_tstamp ev_time ()</p>
<dd> Returns the current time as libev would use it. Please note that the <tt>&quot;ev_now&quot;</tt> function is usually faster and also often returns the timestamp you actually want to know.</p>
<dt>ev_sleep (ev_tstamp interval)</p>
<dd> Sleep for the given interval: The current thread will be blocked until either it is interrupted or the given time interval has passed. Basically this is a sub-second-resolution <tt>&quot;sleep ()&quot;</tt>.</p>
<dt>int ev_version_major ()</p>
<dd>
<dt>int ev_version_minor ()</p>
<dd> You can find out the major and minor <font SIZE="-1">ABI</font> version numbers of the library you linked against by calling the functions <tt>&quot;ev_version_major&quot;</tt> and <tt>&quot;ev_version_minor&quot;</tt>. If you want, you can compare against the global symbols <tt>&quot;EV_VERSION_MAJOR&quot;</tt> and <tt>&quot;EV_VERSION_MINOR&quot;</tt>, which specify the version of the library your program was compiled against. </p>
<p> These version numbers refer to the <font SIZE="-1">ABI</font> version of the library, not the release version. </p>
<p> Usually, it&#8217;s a good idea to terminate if the major versions mismatch, as this indicates an incompatible change. Minor versions are usually compatible to older versions, so a larger minor version alone is usually not a problem. </p>
<p> Example: Make sure we haven&#8217;t accidentally been linked against the wrong version. </p>
<p>assert((&#8220;libev version mismatch&#8221;,<br />
        ev_version_major() == EV_VERSION_MAJOR &amp;&amp; ev_version_minor() &gt;= EV_VERSION_MINOR));</p>
<dt>unsigned int ev_supported_backends ()</p>
<dd> Return the set of all backends (i.e. their corresponding <tt>&quot;EV_BACKEND_*&quot;</tt> value) compiled into this binary of libev (independent of their availability on the system you are running on). See <tt>&quot;ev_default_loop&quot;</tt> for a description of the set values. </p>
<p> Example: make sure we have the epoll method, because yeah this is cool and a must have and can we have a torrent of it please!!!11 </p>
<pre>
   assert ((&quot;sorry, no epoll, no sex&quot;,
            ev_supported_backends () &amp; EVBACKEND_EPOLL));
</pre>
<dt>unsigned int ev_recommended_backends ()</p>
<dd> Return the set of all backends compiled into this binary of libev and also recommended for this platform. This set is often smaller than the one returned by <tt>&quot;ev_supported_backends&quot;</tt>, as for example kqueue is broken on most BSDs and will not be auto-detected unless you explicitly request it (assuming you know what you are doing). This is the set of backends that libev will probe for if you specify no backends explicitly.</p>
<dt>unsigned int ev_embeddable_backends ()</p>
<dd> Returns the set of backends that are embeddable in other event loops. This is the theoretical, all-platform, value. To find which backends might be supported on the current system, you would need to look at <tt>&quot;ev_embeddable_backends () &amp; ev_supported_backends ()&quot;</tt>, likewise for recommended ones. </p>
<p> See the description of <tt>&quot;ev_embed&quot;</tt> watchers for more info.</p>
<dt>ev_set_allocator (void *(*cb)(void *ptr, long size)) [<font SIZE="-1">NOT</font> <font SIZE="-1">REENTRANT</font>]</p>
<dd> Sets the allocation function to use (the prototype is similar &#8211; the semantics are identical to the <tt>&quot;realloc&quot;</tt> C89/SuS/POSIX function). It is used to allocate and free memory (no surprises here). If it returns zero when memory needs to be allocated (<tt>&quot;size != 0&quot;</tt>), the library might abort or take some potentially destructive action. </p>
<p> Since some systems (at least OpenBSD and Darwin) fail to implement correct <tt>&quot;realloc&quot;</tt> semantics, libev will use a wrapper around the system <tt>&quot;realloc&quot;</tt> and <tt>&quot;free&quot;</tt> functions by default. </p>
<p> You could override this function in high-availability programs to, say, free some memory if it cannot allocate memory, to use a special allocator, or even to sleep a while and retry until some memory is available. </p>
<p> Example: Replace the libev allocator with one that waits a bit and then retries (example requires a standards-compliant <tt>&quot;realloc&quot;</tt>). </p>
<p>static void *<br />
persistent_realloc(void *ptr, size_t size)<br />
{<br />
    for (;;) {<br />
        void *newptr = realloc(ptr, size);<br />
        if (newptr)<br />
            return newptr;<br />
        sleep(60);<br />
    }<br />
}<br />
&#8230; ev_set_allocator(persistent_realloc);</p>
<dt>ev_set_syserr_cb (void (*cb)(const char *msg)); [<font SIZE="-1">NOT</font> <font SIZE="-1">REENTRANT</font>]</p>
<dd> Set the callback function to call on a retryable system call error (such as failed select, poll, epoll_wait). The message is a printable string indicating the system call or subsystem causing the problem. If this callback is set, then libev will expect it to remedy the situation, no matter what, when it returns. That is, libev will generally retry the requested operation, or, if the condition doesn&#8217;t go away, do bad stuff (such as abort). </p>
<p> Example: This is basically the same thing that libev does internally, too. </p>
<p>static void<br />
fatal_error(const char *msg)<br />
{<br />
    perror(msg);<br />
    abort();<br />
}<br />
&#8230; ev_set_syserr_cb(fatal_error);
</dl>
<h2>FUNCTIONS CONTROLLING THE EVENT LOOP</h2>
<p> An event loop is described by a <tt>&quot;struct ev_loop *&quot;</tt> (the <tt>&quot;struct&quot;</tt> is <i>not</i> optional in this case, as there is also an <tt>&quot;ev_loop&quot;</tt> <i>function</i>). </p>
<p> The library knows two types of such loops, the <i>default</i> loop, which supports signals and child events, and dynamically created loops which do not.</p>
<dl>
<dt>struct ev_loop *ev_default_loop (unsigned int flags)</p>
<dd> This will initialise the default event loop if it hasn&#8217;t been initialised yet and return it. If the default loop could not be initialised, returns false. If it already was initialised it simply returns it (and ignores the flags. If that is troubling you, check <tt>&quot;ev_backend ()&quot;</tt> afterwards). </p>
<p> If you don&#8217;t know what event loop to use, use the one returned from this function. </p>
<p> Note that this function is <i>not</i> thread-safe, so if you want to use it from multiple threads, you have to lock (note also that this is unlikely, as loops cannot be shared easily between threads anyway). </p>
<p> The default loop is the only loop that can handle <tt>&quot;ev_signal&quot;</tt> and <tt>&quot;ev_child&quot;</tt> watchers, and to do this, it always registers a handler for <tt>&quot;SIGCHLD&quot;</tt>. If this is a problem for your application you can either create a dynamic loop with <tt>&quot;ev_loop_new&quot;</tt> that doesn&#8217;t do that, or you can simply overwrite the <tt>&quot;SIGCHLD&quot;</tt> signal handler <i>after</i> calling <tt>&quot;ev_default_init&quot;</tt>. </p>
<p> The flags argument can be used to specify special behaviour or specific backends to use, and is usually specified as <tt>0</tt> (or <tt>&quot;EVFLAG_AUTO&quot;</tt>). </p>
<p> The following flags are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt>EVFLAG_AUTO</p>
<dd> The default flags value. Use this if you have no clue (it&#8217;s the right thing, believe me).</p>
<dt>EVFLAG_NOENV</p>
<dd> If this flag bit is or&#8217;ed into the flag value (or the program runs setuid or setgid) then libev will <i>not</i> look at the environment variable <tt>&quot;LIBEV_FLAGS&quot;</tt>. Otherwise (the default), this environment variable will override the flags completely if it is found in the environment. This is useful to try out specific backends to test their performance, or to work around bugs.</p>
<dt>EVFLAG_FORKCHECK</p>
<dd> Instead of calling <tt>&quot;ev_default_fork&quot;</tt> or <tt>&quot;ev_loop_fork&quot;</tt> manually after a fork, you can also make libev check for a fork in each iteration by enabling this flag. </p>
<p> This works by calling <tt>&quot;getpid ()&quot;</tt> on every iteration of the loop, and thus this might slow down your event loop if you do a lot of loop iterations and little real work, but is usually not noticeable (on my GNU/Linux system for example, <tt>&quot;getpid&quot;</tt> is actually a simple 5-insn sequence without a system call and thus <i>very</i> fast, but my GNU/Linux system also has <tt>&quot;pthread_atfork&quot;</tt> which is even faster). </p>
<p> The big advantage of this flag is that you can forget about fork (and forget about forgetting to tell libev about forking) when you use this flag. </p>
<p> This flag setting cannot be overridden or specified in the <tt>&quot;LIBEV_FLAGS&quot;</tt> environment variable.</p>
<dt>EVFLAG_NOINOTIFY</p>
<dd> When this flag is specified, then libev will not attempt to use the <i>inotify</i> <font SIZE="-1">API</font> for it&#8217;s <tt>&quot;ev_stat&quot;</tt> watchers. Apart from debugging and testing, this flag can be useful to conserve inotify file descriptors, as otherwise each loop using <tt>&quot;ev_stat&quot;</tt> watchers consumes one inotify handle.</p>
<dt>EVFLAG_NOSIGNALFD</p>
<dd> When this flag is specified, then libev will not attempt to use the <i>signalfd</i> <font SIZE="-1">API</font> for it&#8217;s <tt>&quot;ev_signal&quot;</tt> (and <tt>&quot;ev_child&quot;</tt>) watchers. This is probably only useful to work around any bugs in libev. Consequently, this flag might go away once the signalfd functionality is considered stable, so it&#8217;s useful mostly in environment variables and not in program code.</p>
<dt>EVBACKEND_SELECT (value 1, portable select backend)</p>
<dd> This is your standard <i><a href="/docs/linux/man/2-select/">select</a></i>(2) backend. Not <i>completely</i> standard, as libev tries to roll its own fd_set with no limits on the number of fds, but if that fails, expect a fairly low limit on the number of fds when using this backend. It doesn&#8217;t scale too well (O(highest_fd)), but its usually the fastest backend for a low number of (low-numbered :) fds. </p>
<p> To get good performance out of this backend you need a high amount of parallelism (most of the file descriptors should be busy). If you are writing a server, you should <tt>&quot;accept ()&quot;</tt> in a loop to accept as many connections as possible during one iteration. You might also want to have a look at <tt>&quot;ev_set_io_collect_interval ()&quot;</tt> to increase the amount of readiness notifications you get per iteration. </p>
<p> This backend maps <tt>&quot;EV_READ&quot;</tt> to the <tt>&quot;readfds&quot;</tt> set and <tt>&quot;EV_WRITE&quot;</tt> to the <tt>&quot;writefds&quot;</tt> set (and to work around Microsoft Windows bugs, also onto the <tt>&quot;exceptfds&quot;</tt> set on that platform).</p>
<dt>EVBACKEND_POLL (value 2, poll backend, available everywhere except on windows)</p>
<dd> And this is your standard <i><a href="/docs/linux/man/2-poll/">poll</a></i>(2) backend. It&#8217;s more complicated than select, but handles sparse fds better and has no artificial limit on the number of fds you can use (except it will slow down considerably with a lot of inactive fds). It scales similarly to select, i.e. O(total_fds). See the entry for <tt>&quot;EVBACKEND_SELECT&quot;</tt>, above, for performance tips. </p>
<p> This backend maps <tt>&quot;EV_READ&quot;</tt> to <tt>&quot;POLLIN | POLLERR | POLLHUP&quot;</tt>, and <tt>&quot;EV_WRITE&quot;</tt> to <tt>&quot;POLLOUT | POLLERR | POLLHUP&quot;</tt>.</p>
<dt>EVBACKEND_EPOLL (value 4, Linux)</p>
<dd> For few fds, this backend is a bit little slower than poll and select, but it scales phenomenally better. While poll and select usually scale like O(total_fds) where n is the total number of fds (or the highest fd), epoll scales either <a href="/docs/linux/man/1-o/">O</a>(1) or O(active_fds). </p>
<p> The epoll mechanism deserves honorable mention as the most misdesigned of the more advanced event mechanisms: mere annoyances include silently dropping file descriptors, requiring a system call per change per file descriptor (and unnecessary guessing of parameters), problems with dup and so on. The biggest issue is fork races, however &#8211; if a program forks then <i>both</i> parent and child process have to recreate the epoll set, which can take considerable time (one syscall per file descriptor) and is of course hard to detect. </p>
<p> Epoll is also notoriously buggy &#8211; embedding epoll fds <i>should</i> work, but of course <i>doesn&#8217;t</i>, and epoll just loves to report events for totally <i>different</i> file descriptors (even already closed ones, so one cannot even remove them from the set) than registered in the set (especially on <font SIZE="-1">SMP</font> systems). Libev tries to counter these spurious notifications by employing an additional generation counter and comparing that against the events to filter out spurious ones, recreating the set when required. </p>
<p> While stopping, setting and starting an I/O watcher in the same iteration will result in some caching, there is still a system call per such incident (because the same <i>file descriptor</i> could point to a different <i>file description</i> now), so its best to avoid that. Also, <tt>&quot;dup ()&quot;</tt>&#8216;ed file descriptors might not work very well if you register events for both file descriptors. </p>
<p> Best performance from this backend is achieved by not unregistering all watchers for a file descriptor until it has been closed, if possible, i.e. keep at least one watcher active per fd at all times. Stopping and starting a watcher (without re-setting it) also usually doesn&#8217;t cause extra overhead. A fork can both result in spurious notifications as well as in libev having to destroy and recreate the epoll object, which can take considerable time and thus should be avoided. </p>
<p> All this means that, in practice, <tt>&quot;EVBACKEND_SELECT&quot;</tt> can be as fast or faster than epoll for maybe up to a hundred file descriptors, depending on the usage. So sad. </p>
<p> While nominally embeddable in other event loops, this feature is broken in all kernel versions tested so far. </p>
<p> This backend maps <tt>&quot;EV_READ&quot;</tt> and <tt>&quot;EV_WRITE&quot;</tt> in the same way as <tt>&quot;EVBACKEND_POLL&quot;</tt>.</p>
<dt>EVBACKEND_KQUEUE (value 8, most <font SIZE="-1">BSD</font> clones)</p>
<dd> Kqueue deserves special mention, as at the time of this writing, it was broken on all BSDs except NetBSD (usually it doesn&#8217;t work reliably with anything but sockets and pipes, except on Darwin, where of course it&#8217;s completely useless). Unlike epoll, however, whose brokenness is by design, these kqueue bugs can (and eventually will) be fixed without <font SIZE="-1">API</font> changes to existing programs. For this reason it&#8217;s not being &#8220;auto-detected&#8221; unless you explicitly specify it in the flags (i.e. using <tt>&quot;EVBACKEND_KQUEUE&quot;</tt>) or libev was compiled on a known-to-be-good (-enough) system like NetBSD. </p>
<p> You still can embed kqueue into a normal poll or select backend and use it only for sockets (after having made sure that sockets work with kqueue on the target platform). See <tt>&quot;ev_embed&quot;</tt> watchers for more info. </p>
<p> It scales in the same way as the epoll backend, but the interface to the kernel is more efficient (which says nothing about its actual speed, of course). While stopping, setting and starting an I/O watcher does never cause an extra system call as with <tt>&quot;EVBACKEND_EPOLL&quot;</tt>, it still adds up to two event changes per incident. Support for <tt>&quot;fork ()&quot;</tt> is very bad (but sane, unlike epoll) and it drops fds silently in similarly hard-to-detect cases </p>
<p> This backend usually performs well under most conditions. </p>
<p> While nominally embeddable in other event loops, this doesn&#8217;t work everywhere, so you might need to test for this. And since it is broken almost everywhere, you should only use it when you have a lot of sockets (for which it usually works), by embedding it into another event loop (e.g. <tt>&quot;EVBACKEND_SELECT&quot;</tt> or <tt>&quot;EVBACKEND_POLL&quot;</tt> (but <tt>&quot;poll&quot;</tt> is of course also broken on <font SIZE="-1">OS</font> X)) and, did I mention it, using it only for sockets. </p>
<p> This backend maps <tt>&quot;EV_READ&quot;</tt> into an <tt>&quot;EVFILT_READ&quot;</tt> kevent with <tt>&quot;NOTE_EOF&quot;</tt>, and <tt>&quot;EV_WRITE&quot;</tt> into an <tt>&quot;EVFILT_WRITE&quot;</tt> kevent with <tt>&quot;NOTE_EOF&quot;</tt>.</p>
<dt>EVBACKEND_DEVPOLL (value 16, Solaris 8)</p>
<dd> This is not implemented yet (and might never be, unless you send me an implementation). According to reports, <tt>&quot;/dev/poll&quot;</tt> only supports sockets and is not embeddable, which would limit the usefulness of this backend immensely.</p>
<dt>EVBACKEND_PORT (value 32, Solaris 10)</p>
<dd> This uses the Solaris 10 event port mechanism. As with everything on Solaris, it&#8217;s really slow, but it still scales very well (O(active_fds)). </p>
<p> Please note that Solaris event ports can deliver a lot of spurious notifications, so you need to use non-blocking I/O or other means to avoid blocking when no data (or space) is available. </p>
<p> While this backend scales well, it requires one system call per active file descriptor per loop iteration. For small and medium numbers of file descriptors a &#8220;slow&#8221; <tt>&quot;EVBACKEND_SELECT&quot;</tt> or <tt>&quot;EVBACKEND_POLL&quot;</tt> backend might perform better. </p>
<p> On the positive side, with the exception of the spurious readiness notifications, this backend actually performed fully to specification in all tests and is fully embeddable, which is a rare feat among the OS-specific backends (I vastly prefer correctness over speed hacks). </p>
<p> This backend maps <tt>&quot;EV_READ&quot;</tt> and <tt>&quot;EV_WRITE&quot;</tt> in the same way as <tt>&quot;EVBACKEND_POLL&quot;</tt>.</p>
<dt>EVBACKEND_ALL</p>
<dd> Try all backends (even potentially broken ones that wouldn&#8217;t be tried with <tt>&quot;EVFLAG_AUTO&quot;</tt>). Since this is a mask, you can do stuff such as <tt>&quot;EVBACKEND_ALL &amp; ~EVBACKEND_KQUEUE&quot;</tt>. </p>
<p> It is definitely not recommended to use this flag.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If one or more of the backend flags are or&#8217;ed into the flags value, then only these backends will be tried (in the reverse order as listed here). If none are specified, all backends in <tt>&quot;ev_recommended_backends ()&quot;</tt> will be tried. </p>
<p> Example: This is the most typical usage. </p>
<p>if (!ev_default_loop(0))<br />
    fatal(&#8220;could not initialise libev, bad $LIBEV_FLAGS in environment?&#8221;);</p>
<p> Example: Restrict libev to the select and poll backends, and do not allow environment settings to be taken into account: </p>
<pre>
   ev_default_loop (EVBACKEND_POLL | EVBACKEND_SELECT | EVFLAG_NOENV);
</pre>
<p> Example: Use whatever libev has to offer, but make sure that kqueue is used if available (warning, breaks stuff, best use only with your own private event loop and only if you know the <font SIZE="-1">OS</font> supports your types of fds): </p>
<pre>
   ev_default_loop (ev_recommended_backends () | EVBACKEND_KQUEUE);
</pre>
</dl>
<dt>struct ev_loop *ev_loop_new (unsigned int flags)</p>
<dd> Similar to <tt>&quot;ev_default_loop&quot;</tt>, but always creates a new event loop that is always distinct from the default loop. Unlike the default loop, it cannot handle signal and child watchers, and attempts to do so will be greeted by undefined behaviour (or a failed assertion if assertions are enabled). </p>
<p> Note that this function <i>is</i> thread-safe, and the recommended way to use libev with threads is indeed to create one loop per thread, and using the default loop in the &#8220;main&#8221; or &#8220;initial&#8221; thread. </p>
<p> Example: Try to create a event loop that uses epoll and nothing else. </p>
<p>struct ev_loop *epoller = ev_loop_new(EVBACKEND_EPOLL | EVFLAG_NOENV);<br />
if (!epoller)<br />
    fatal(&#8220;no epoll found here, maybe it hides under your chair&#8221;);</p>
<dt>ev_default_destroy ()</p>
<dd> Destroys the default loop again (frees all memory and kernel state etc.). None of the active event watchers will be stopped in the normal sense, so e.g. <tt>&quot;ev_is_active&quot;</tt> might still return true. It is your responsibility to either stop all watchers cleanly yourself <i>before</i> calling this function, or cope with the fact afterwards (which is usually the easiest thing, you can just ignore the watchers and/or <tt>&quot;free ()&quot;</tt> them for example). </p>
<p> Note that certain global state, such as signal state (and installed signal handlers), will not be freed by this function, and related watchers (such as signal and child watchers) would need to be stopped manually. </p>
<p> In general it is not advisable to call this function except in the rare occasion where you really need to free e.g. the signal handling pipe fds. If you need dynamically allocated loops it is better to use <tt>&quot;ev_loop_new&quot;</tt> and <tt>&quot;ev_loop_destroy&quot;</tt>).</p>
<dt>ev_loop_destroy (loop)</p>
<dd> Like <tt>&quot;ev_default_destroy&quot;</tt>, but destroys an event loop created by an earlier call to <tt>&quot;ev_loop_new&quot;</tt>.</p>
<dt>ev_default_fork ()</p>
<dd> This function sets a flag that causes subsequent <tt>&quot;ev_loop&quot;</tt> iterations to reinitialise the kernel state for backends that have one. Despite the name, you can call it anytime, but it makes most sense after forking, in the child process (or both child and parent, but that again makes little sense). You <i>must</i> call it in the child before using any of the libev functions, and it will only take effect at the next <tt>&quot;ev_loop&quot;</tt> iteration. </p>
<p> On the other hand, you only need to call this function in the child process if and only if you want to use the event library in the child. If you just fork+exec, you don&#8217;t have to call it at all. </p>
<p> The function itself is quite fast and it&#8217;s usually not a problem to call it just in case after a fork. To make this easy, the function will fit in quite nicely into a call to <tt>&quot;pthread_atfork&quot;</tt>: </p>
<pre>
    pthread_atfork (0, 0, ev_default_fork);
</pre>
<dt>ev_loop_fork (loop)</p>
<dd> Like <tt>&quot;ev_default_fork&quot;</tt>, but acts on an event loop created by <tt>&quot;ev_loop_new&quot;</tt>. Yes, you have to call this on every allocated event loop after fork that you want to re-use in the child, and how you do this is entirely your own problem.</p>
<dt>int ev_is_default_loop (loop)</p>
<dd> Returns true when the given loop is, in fact, the default loop, and false otherwise.</p>
<dt>unsigned int ev_loop_count (loop)</p>
<dd> Returns the count of loop iterations for the loop, which is identical to the number of times libev did poll for new events. It starts at <tt>0</tt> and happily wraps around with enough iterations. </p>
<p> This value can sometimes be useful as a generation counter of sorts (it &#8220;ticks&#8221; the number of loop iterations), as it roughly corresponds with <tt>&quot;ev_prepare&quot;</tt> and <tt>&quot;ev_check&quot;</tt> calls.</p>
<dt>unsigned int ev_loop_depth (loop)</p>
<dd> Returns the number of times <tt>&quot;ev_loop&quot;</tt> was entered minus the number of times <tt>&quot;ev_loop&quot;</tt> was exited, in other words, the recursion depth. </p>
<p> Outside <tt>&quot;ev_loop&quot;</tt>, this number is zero. In a callback, this number is <tt>1</tt>, unless <tt>&quot;ev_loop&quot;</tt> was invoked recursively (or from another thread), in which case it is higher. </p>
<p> Leaving <tt>&quot;ev_loop&quot;</tt> abnormally (setjmp/longjmp, cancelling the thread etc.), doesn&#8217;t count as exit.</p>
<dt>unsigned int ev_backend (loop)</p>
<dd> Returns one of the <tt>&quot;EVBACKEND_*&quot;</tt> flags indicating the event backend in use.</p>
<dt>ev_tstamp ev_now (loop)</p>
<dd> Returns the current &#8220;event loop time&#8221;, which is the time the event loop received events and started processing them. This timestamp does not change as long as callbacks are being processed, and this is also the base time used for relative timers. You can treat it as the timestamp of the event occurring (or more correctly, libev finding out about it).</p>
<dt>ev_now_update (loop)</p>
<dd> Establishes the current time by querying the kernel, updating the time returned by <tt>&quot;ev_now ()&quot;</tt> in the progress. This is a costly operation and is usually done automatically within <tt>&quot;ev_loop ()&quot;</tt>. </p>
<p> This function is rarely useful, but when some event callback runs for a very long time without entering the event loop, updating libev&#8217;s idea of the current time is a good idea. </p>
<p> See also &#8220;The special problem of time updates&#8221; in the <tt>&quot;ev_timer&quot;</tt> section.</p>
<dt>ev_suspend (loop)</p>
<dd>
<dt>ev_resume (loop)</p>
<dd> These two functions suspend and resume a loop, for use when the loop is not used for a while and timeouts should not be processed. </p>
<p> A typical use case would be an interactive program such as a game: When the user presses <tt>&quot;^Z&quot;</tt> to suspend the game and resumes it an hour later it would be best to handle timeouts as if no time had actually passed while the program was suspended. This can be achieved by calling <tt>&quot;ev_suspend&quot;</tt> in your <tt>&quot;SIGTSTP&quot;</tt> handler, sending yourself a <tt>&quot;SIGSTOP&quot;</tt> and calling <tt>&quot;ev_resume&quot;</tt> directly afterwards to resume timer processing. </p>
<p> Effectively, all <tt>&quot;ev_timer&quot;</tt> watchers will be delayed by the time spend between <tt>&quot;ev_suspend&quot;</tt> and <tt>&quot;ev_resume&quot;</tt>, and all <tt>&quot;ev_periodic&quot;</tt> watchers will be rescheduled (that is, they will lose any events that would have occured while suspended). </p>
<p> After calling <tt>&quot;ev_suspend&quot;</tt> you <code>must not</code> call <i>any</i> function on the given loop other than <tt>&quot;ev_resume&quot;</tt>, and you <code>must not</code> call <tt>&quot;ev_resume&quot;</tt> without a previous call to <tt>&quot;ev_suspend&quot;</tt>. </p>
<p> Calling <tt>&quot;ev_suspend&quot;</tt>/<tt>&quot;ev_resume&quot;</tt> has the side effect of updating the event loop time (see <tt>&quot;ev_now_update&quot;</tt>).</p>
<dt>ev_loop (loop, int flags)</p>
<dd> Finally, this is it, the event handler. This function usually is called after you initialised all your watchers and you want to start handling events. </p>
<p> If the flags argument is specified as <tt>0</tt>, it will not return until either no event watchers are active anymore or <tt>&quot;ev_unloop&quot;</tt> was called. </p>
<p> Please note that an explicit <tt>&quot;ev_unloop&quot;</tt> is usually better than relying on all watchers to be stopped when deciding when a program has finished (especially in interactive programs), but having a program that automatically loops as long as it has to and no longer by virtue of relying on its watchers stopping correctly, that is truly a thing of beauty. </p>
<p> A flags value of <tt>&quot;EVLOOP_NONBLOCK&quot;</tt> will look for new events, will handle those events and any already outstanding ones, but will not block your process in case there are no events and will return after one iteration of the loop. </p>
<p> A flags value of <tt>&quot;EVLOOP_ONESHOT&quot;</tt> will look for new events (waiting if necessary) and will handle those and any already outstanding ones. It will block your process until at least one new event arrives (which could be an event internal to libev itself, so there is no guarantee that a user-registered callback will be called), and will return after one iteration of the loop. </p>
<p> This is useful if you are waiting for some external event in conjunction with something not expressible using other libev watchers (i.e. &quot;roll your own <tt>&quot;ev_loop&quot;</tt>&quot;). However, a pair of <tt>&quot;ev_prepare&quot;</tt>/<tt>&quot;ev_check&quot;</tt> watchers is usually a better approach for this kind of thing. </p>
<p> Here are the gory details of what <tt>&quot;ev_loop&quot;</tt> does: </p>
<p>   &#8211; Before the first iteration, call any pending watchers.<br />
   * If EVFLAG_FORKCHECK was used, check for a fork.<br />
   &#8211; If a fork was detected (by any means), queue and call all fork watchers.<br />
   &#8211; Queue and call all prepare watchers.<br />
   &#8211; If we have been forked, detach and recreate the kernel state<br />
     as to not disturb the other process.<br />
   &#8211; Update the kernel state with all outstanding changes.<br />
   &#8211; Update the &#8220;event loop time&#8221; (ev_now ()).<br />
   &#8211; Calculate for how long to sleep or block, if at all<br />
     (active idle watchers, EVLOOP_NONBLOCK or not having<br />
     any active watchers at all will result in not sleeping).<br />
   &#8211; Sleep if the I/O and timer collect interval say so.<br />
   &#8211; Block the process, waiting for any events.<br />
   &#8211; Queue all outstanding I/O (fd) events.<br />
   &#8211; Update the &#8220;event loop time&#8221; (ev_now ()), and do time jump adjustments.<br />
   &#8211; Queue all expired timers.<br />
   &#8211; Queue all expired periodics.<br />
   &#8211; Unless any events are pending now, queue all idle watchers.<br />
   &#8211; Queue all check watchers.<br />
   &#8211; Call all queued watchers in reverse order (i.e. check watchers first).<br />
     Signals and child watchers are implemented as I/O watchers, and will<br />
     be handled here by queueing them when their watcher gets executed.<br />
   &#8211; If ev_unloop has been called, or EVLOOP_ONESHOT or EVLOOP_NONBLOCK<br />
     were used, or there are no active watchers, return, otherwise<br />
     continue with step *.</p>
<p> Example: Queue some jobs and then loop until no events are outstanding anymore. </p>
<p>&#8230; queue jobs here, make sure they register event watchers as long&#8230; as they still have work to do(even an idle watcher will do..)<br />
                         ev_loop(my_loop, 0);<br />
&#8230; jobs done or somebody called unloop.yeah !</p>
<dt>ev_unloop (loop, how)</p>
<dd> Can be used to make a call to <tt>&quot;ev_loop&quot;</tt> return early (but only after it has processed all outstanding events). The <tt>&quot;how&quot;</tt> argument must be either <tt>&quot;EVUNLOOP_ONE&quot;</tt>, which will make the innermost <tt>&quot;ev_loop&quot;</tt> call return, or <tt>&quot;EVUNLOOP_ALL&quot;</tt>, which will make all nested <tt>&quot;ev_loop&quot;</tt> calls return. </p>
<p> This &#8220;unloop state&#8221; will be cleared when entering <tt>&quot;ev_loop&quot;</tt> again. </p>
<p> It is safe to call <tt>&quot;ev_unloop&quot;</tt> from otuside any <tt>&quot;ev_loop&quot;</tt> calls.</p>
<dt>ev_ref (loop)</p>
<dd>
<dt>ev_unref (loop)</p>
<dd> Ref/unref can be used to add or remove a reference count on the event loop: Every watcher keeps one reference, and as long as the reference count is nonzero, <tt>&quot;ev_loop&quot;</tt> will not return on its own. </p>
<p> If you have a watcher you never unregister that should not keep <tt>&quot;ev_loop&quot;</tt> from returning, call <i>ev_unref()</i> after starting, and <i>ev_ref()</i> before stopping it. </p>
<p> As an example, libev itself uses this for its internal signal pipe: It is not visible to the libev user and should not keep <tt>&quot;ev_loop&quot;</tt> from exiting if no event watchers registered by it are active. It is also an excellent way to do this for generic recurring timers or from within third-party libraries. Just remember to <i>unref after start</i> and <i>ref before stop</i> (but only if the watcher wasn&#8217;t active before, or was active before, respectively. Note also that libev might stop watchers itself (e.g. non-repeating timers) in which case you have to <tt>&quot;ev_ref&quot;</tt> in the callback). </p>
<p> Example: Create a signal watcher, but keep it from keeping <tt>&quot;ev_loop&quot;</tt> running when nothing else is active. </p>
<p>ev_signal exitsig;<br />
ev_signal_init(&amp;exitsig, sig_cb, SIGINT);<br />
ev_signal_start(loop, &amp;exitsig);<br />
evf_unref(loop);</p>
<p> Example: For some weird reason, unregister the above signal handler again. </p>
<p>ev_ref(loop);<br />
ev_signal_stop(loop, &amp;exitsig);</p>
<dt>ev_set_io_collect_interval (loop, ev_tstamp interval)</p>
<dd>
<dt>ev_set_timeout_collect_interval (loop, ev_tstamp interval)</p>
<dd> These advanced functions influence the time that libev will spend waiting for events. Both time intervals are by default <tt>0</tt>, meaning that libev will try to invoke timer/periodic callbacks and I/O callbacks with minimum latency. </p>
<p> Setting these to a higher value (the <tt>&quot;interval&quot;</tt> <i>must</i> be &gt;= <tt>0</tt>) allows libev to delay invocation of I/O and timer/periodic callbacks to increase efficiency of loop iterations (or to increase power-saving opportunities). </p>
<p> The idea is that sometimes your program runs just fast enough to handle one (or very few) event(s) per loop iteration. While this makes the program responsive, it also wastes a lot of <font SIZE="-1">CPU</font> time to poll for new events, especially with backends like <tt>&quot;select ()&quot;</tt> which have a high overhead for the actual polling but can deliver many events at once. </p>
<p> By setting a higher <i>io collect interval</i> you allow libev to spend more time collecting I/O events, so you can handle more events per iteration, at the cost of increasing latency. Timeouts (both <tt>&quot;ev_periodic&quot;</tt> and <tt>&quot;ev_timer&quot;</tt>) will be not affected. Setting this to a non-null value will introduce an additional <tt>&quot;ev_sleep ()&quot;</tt> call into most loop iterations. The sleep time ensures that libev will not poll for I/O events more often then once per this interval, on average. </p>
<p> Likewise, by setting a higher <i>timeout collect interval</i> you allow libev to spend more time collecting timeouts, at the expense of increased latency/jitter/inexactness (the watcher callback will be called later). <tt>&quot;ev_io&quot;</tt> watchers will not be affected. Setting this to a non-null value will not introduce any overhead in libev. </p>
<p> Many (busy) programs can usually benefit by setting the I/O collect interval to a value near <tt>0.1</tt> or so, which is often enough for interactive servers (of course not for games), likewise for timeouts. It usually doesn&#8217;t make much sense to set it to a lower value than <tt>0.01</tt>, as this approaches the timing granularity of most systems. Note that if you do transactions with the outside world and you can&#8217;t increase the parallelity, then this setting will limit your transaction rate (if you need to poll once per transaction and the I/O collect interval is 0.01, then you can&#8217;t do more than 100 transations per second). </p>
<p> Setting the <i>timeout collect interval</i> can improve the opportunity for saving power, as the program will &#8220;bundle&#8221; timer callback invocations that are &#8220;near&#8221; in time together, by delaying some, thus reducing the number of times the process sleeps and wakes up again. Another useful technique to reduce iterations/wake-ups is to use <tt>&quot;ev_periodic&quot;</tt> watchers and make sure they fire on, say, one-second boundaries only. </p>
<p> Example: we only need 0.1s timeout granularity, and we wish not to poll more often than 100 times per second: </p>
<p>ev_set_timeout_collect_interval(EV_DEFAULT_UC_ 0.1);<br />
ev_set_io_collect_interval(EV_DEFAULT_UC_ 0.01);</p>
<dt>ev_invoke_pending (loop)</p>
<dd> This call will simply invoke all pending watchers while resetting their pending state. Normally, <tt>&quot;ev_loop&quot;</tt> does this automatically when required, but when overriding the invoke callback this call comes handy.</p>
<dt>int ev_pending_count (loop)</p>
<dd> Returns the number of pending watchers &#8211; zero indicates that no watchers are pending.</p>
<dt>ev_set_invoke_pending_cb (loop, void (*invoke_pending_cb)(<font SIZE="-1">EV_P</font>))</p>
<dd> This overrides the invoke pending functionality of the loop: Instead of invoking all pending watchers when there are any, <tt>&quot;ev_loop&quot;</tt> will call this callback instead. This is useful, for example, when you want to invoke the actual watchers inside another context (another thread etc.). </p>
<p> If you want to reset the callback, use <tt>&quot;ev_invoke_pending&quot;</tt> as new callback.</p>
<dt>ev_set_loop_release_cb (loop, void (*release)(<font SIZE="-1">EV_P</font>), void (*acquire)(<font SIZE="-1">EV_P</font>))</p>
<dd> Sometimes you want to share the same loop between multiple threads. This can be done relatively simply by putting mutex_lock/unlock calls around each call to a libev function. </p>
<p> However, <tt>&quot;ev_loop&quot;</tt> can run an indefinite time, so it is not feasible to wait for it to return. One way around this is to wake up the loop via <tt>&quot;ev_unloop&quot;</tt> and <tt>&quot;av_async_send&quot;</tt>, another way is to set these <i>release</i> and <i>acquire</i> callbacks on the loop. </p>
<p> When set, then <tt>&quot;release&quot;</tt> will be called just before the thread is suspended waiting for new events, and <tt>&quot;acquire&quot;</tt> is called just afterwards. </p>
<p> Ideally, <tt>&quot;release&quot;</tt> will just call your mutex_unlock function, and <tt>&quot;acquire&quot;</tt> will just call the mutex_lock function again. </p>
<p> While event loop modifications are allowed between invocations of <tt>&quot;release&quot;</tt> and <tt>&quot;acquire&quot;</tt> (that&#8217;s their only purpose after all), no modifications done will affect the event loop, i.e. adding watchers will have no effect on the set of file descriptors being watched, or the time waited. USe an <tt>&quot;ev_async&quot;</tt> watcher to wake up <tt>&quot;ev_loop&quot;</tt> when you want it to take note of any changes you made. </p>
<p> In theory, threads executing <tt>&quot;ev_loop&quot;</tt> will be async-cancel safe between invocations of <tt>&quot;release&quot;</tt> and <tt>&quot;acquire&quot;</tt>. </p>
<p> See also the locking example in the <tt>&quot;THREADS&quot;</tt> section later in this document.</p>
<dt>ev_set_userdata (loop, void *data)</p>
<dd>
<dt>ev_userdata (loop)</p>
<dd> Set and retrieve a single <tt>&quot;void *&quot;</tt> associated with a loop. When <tt>&quot;ev_set_userdata&quot;</tt> has never been called, then <tt>&quot;ev_userdata&quot;</tt> returns <tt>0.</tt> </p>
<p> These two functions can be used to associate arbitrary data with a loop, and are intended solely for the <tt>&quot;invoke_pending_cb&quot;</tt>, <tt>&quot;release&quot;</tt> and <tt>&quot;acquire&quot;</tt> callbacks described above, but of course can be (ab-)used for any other purpose as well.</p>
<dt>ev_loop_verify (loop)</p>
<dd> This function only does something when <tt>&quot;EV_VERIFY&quot;</tt> support has been compiled in, which is the default for non-minimal builds. It tries to go through all internal structures and checks them for validity. If anything is found to be inconsistent, it will print an error message to standard error and call <tt>&quot;abort ()&quot;</tt>. </p>
<p> This can be used to catch bugs inside libev itself: under normal circumstances, this function will never abort as of course libev keeps its data structures consistent.</dl>
<h2>ANATOMY OF A WATCHER</h2>
<p> In the following description, uppercase <tt>&quot;TYPE&quot;</tt> in names stands for the watcher type, e.g. <tt>&quot;ev_TYPE_start&quot;</tt> can mean <tt>&quot;ev_timer_start&quot;</tt> for timer watchers and <tt>&quot;ev_io_start&quot;</tt> for I/O watchers. </p>
<p> A watcher is a structure that you create and register to record your interest in some event. For instance, if you want to wait for <font SIZE="-1">STDIN</font> to become readable, you would create an <tt>&quot;ev_io&quot;</tt> watcher for that: </p>
<p>static void my_cb(struct ev_loop *loop, ev_io *w, int revents)<br />
{<br />
    ev_io_stop(w);<br />
    ev_unloop(loop, EVUNLOOP_ALL);<br />
}<br />
struct ev_loop *loop = ev_default_loop(0);<br />
ev_io stdin_watcher;<br />
ev_init(&amp;stdin_watcher, my_cb);<br />
ev_io_set(&amp;stdin_watcher, STDIN_FILENO, EV_READ);<br />
ev_io_start(loop, &amp;stdin_watcher);<br />
ev_loop(loop, 0);</p>
<p> As you can see, you are responsible for allocating the memory for your watcher structures (and it is <i>usually</i> a bad idea to do this on the stack). </p>
<p> Each watcher has an associated watcher structure (called <tt>&quot;struct ev_TYPE&quot;</tt> or simply <tt>&quot;ev_TYPE&quot;</tt>, as typedefs are provided for all watcher structs). </p>
<p> Each watcher structure must be initialised by a call to <tt>&quot;ev_init (watcher *, callback)&quot;</tt>, which expects a callback to be provided. This callback gets invoked each time the event occurs (or, in the case of I/O watchers, each time the event loop detects that the file descriptor given is readable and/or writable). </p>
<p> Each watcher type further has its own <tt>&quot;ev_TYPE_set (watcher *, ...)&quot;</tt> macro to configure it, with arguments specific to the watcher type. There is also a macro to combine initialisation and setting in one call: <tt>&quot;ev_TYPE_init (watcher *, callback, ...)&quot;</tt>. </p>
<p> To make the watcher actually watch out for events, you have to start it with a watcher-specific start function (<tt>&quot;ev_TYPE_start (loop, watcher *)&quot;</tt>), and you can stop watching for events at any time by calling the corresponding stop function (<tt>&quot;ev_TYPE_stop (loop, watcher *)&quot;</tt>. </p>
<p> As long as your watcher is active (has been started but not stopped) you must not touch the values stored in it. Most specifically you must never reinitialise it or call its <tt>&quot;ev_TYPE_set&quot;</tt> macro. </p>
<p> Each and every callback receives the event loop pointer as first, the registered watcher structure as second, and a bitset of received events as third argument. </p>
<p> The received events usually include a single bit per event type received (you can receive multiple events at the same time). The possible bit masks are:</p>
<dl>
<dt>EV_READ</p>
<dd>
<dt>EV_WRITE</p>
<dd> The file descriptor in the <tt>&quot;ev_io&quot;</tt> watcher has become readable and/or writable.</p>
<dt>EV_TIMEOUT</p>
<dd> The <tt>&quot;ev_timer&quot;</tt> watcher has timed out.</p>
<dt>EV_PERIODIC</p>
<dd> The <tt>&quot;ev_periodic&quot;</tt> watcher has timed out.</p>
<dt>EV_SIGNAL</p>
<dd> The signal specified in the <tt>&quot;ev_signal&quot;</tt> watcher has been received by a thread.</p>
<dt>EV_CHILD</p>
<dd> The pid specified in the <tt>&quot;ev_child&quot;</tt> watcher has received a status change.</p>
<dt>EV_STAT</p>
<dd> The path specified in the <tt>&quot;ev_stat&quot;</tt> watcher changed its attributes somehow.</p>
<dt>EV_IDLE</p>
<dd> The <tt>&quot;ev_idle&quot;</tt> watcher has determined that you have nothing better to do.</p>
<dt>EV_PREPARE</p>
<dd>
<dt>EV_CHECK</p>
<dd> All <tt>&quot;ev_prepare&quot;</tt> watchers are invoked just <i>before</i> <tt>&quot;ev_loop&quot;</tt> starts to gather new events, and all <tt>&quot;ev_check&quot;</tt> watchers are invoked just after <tt>&quot;ev_loop&quot;</tt> has gathered them, but before it invokes any callbacks for any received events. Callbacks of both watcher types can start and stop as many watchers as they want, and all of them will be taken into account (for example, a <tt>&quot;ev_prepare&quot;</tt> watcher might start an idle watcher to keep <tt>&quot;ev_loop&quot;</tt> from blocking).</p>
<dt>EV_EMBED</p>
<dd> The embedded event loop specified in the <tt>&quot;ev_embed&quot;</tt> watcher needs attention.</p>
<dt>EV_FORK</p>
<dd> The event loop has been resumed in the child process after fork (see <tt>&quot;ev_fork&quot;</tt>).</p>
<dt>EV_ASYNC</p>
<dd> The given async watcher has been asynchronously notified (see <tt>&quot;ev_async&quot;</tt>).</p>
<dt>EV_CUSTOM</p>
<dd> Not ever sent (or otherwise used) by libev itself, but can be freely used by libev users to signal watchers (e.g. via <tt>&quot;ev_feed_event&quot;</tt>).</p>
<dt>EV_ERROR</p>
<dd> An unspecified error has occurred, the watcher has been stopped. This might happen because the watcher could not be properly started because libev ran out of memory, a file descriptor was found to be closed or any other problem. Libev considers these application bugs. </p>
<p> You best act on it by reporting the problem and somehow coping with the watcher being stopped. Note that well-written programs should not receive an error ever, so when your watcher receives it, this usually indicates a bug in your program. </p>
<p> Libev will usually signal a few &#8220;dummy&#8221; events together with an error, for example it might indicate that a fd is readable or writable, and if your callbacks is well-written it can just attempt the operation and cope with the error from <i>read()</i> or <i>write()</i>. This will not work in multi-threaded programs, though, as the fd could already be closed and reused for another thing, so beware.</dl>
<h3><font SIZE="-1">GENERIC</font> <font SIZE="-1">WATCHER</font> <font SIZE="-1">FUNCTIONS</font></h3>
<dl>
<dt>ev_init (ev_TYPE *watcher, callback)</p>
<dd> This macro initialises the generic portion of a watcher. The contents of the watcher object can be arbitrary (so <tt>&quot;malloc&quot;</tt> will do). Only the generic parts of the watcher are initialised, you <i>need</i> to call the type-specific <tt>&quot;ev_TYPE_set&quot;</tt> macro afterwards to initialise the type-specific parts. For each type there is also a <tt>&quot;ev_TYPE_init&quot;</tt> macro which rolls both calls into one. </p>
<p> You can reinitialise a watcher at any time as long as it has been stopped (or never started) and there are no pending events outstanding. </p>
<p> The callback is always of type <tt>&quot;void (*)(struct ev_loop *loop, ev_TYPE *watcher, int revents)&quot;</tt>. </p>
<p> Example: Initialise an <tt>&quot;ev_io&quot;</tt> watcher in two steps. </p>
<p>ev_io w;<br />
ev_init(&amp;w, my_cb);<br />
ev_io_set(&amp;w, STDIN_FILENO, EV_READ);</p>
<dt>ev_TYPE_set (ev_TYPE *, [args])</p>
<dd> This macro initialises the type-specific parts of a watcher. You need to call <tt>&quot;ev_init&quot;</tt> at least once before you call this macro, but you can call <tt>&quot;ev_TYPE_set&quot;</tt> any number of times. You must not, however, call this macro on a watcher that is active (it can be pending, however, which is a difference to the <tt>&quot;ev_init&quot;</tt> macro). </p>
<p> Although some watcher types do not have type-specific arguments (e.g. <tt>&quot;ev_prepare&quot;</tt>) you still need to call its <tt>&quot;set&quot;</tt> macro. </p>
<p> See <tt>&quot;ev_init&quot;</tt>, above, for an example.</p>
<dt>ev_TYPE_init (ev_TYPE *watcher, callback, [args])</p>
<dd> This convenience macro rolls both <tt>&quot;ev_init&quot;</tt> and <tt>&quot;ev_TYPE_set&quot;</tt> macro calls into a single call. This is the most convenient method to initialise a watcher. The same limitations apply, of course. </p>
<p> Example: Initialise and set an <tt>&quot;ev_io&quot;</tt> watcher in one step. </p>
<pre>
   ev_io_init (&amp;w, my_cb, STDIN_FILENO, EV_READ);
</pre>
<dt>ev_TYPE_start (loop *, ev_TYPE *watcher)</p>
<dd> Starts (activates) the given watcher. Only active watchers will receive events. If the watcher is already active nothing will happen. </p>
<p> Example: Start the <tt>&quot;ev_io&quot;</tt> watcher that is being abused as example in this whole section. </p>
<pre>
   ev_io_start (EV_DEFAULT_UC, &amp;w);
</pre>
<dt>ev_TYPE_stop (loop *, ev_TYPE *watcher)</p>
<dd> Stops the given watcher if active, and clears the pending status (whether the watcher was active or not). </p>
<p> It is possible that stopped watchers are pending &#8211; for example, non-repeating timers are being stopped when they become pending &#8211; but calling <tt>&quot;ev_TYPE_stop&quot;</tt> ensures that the watcher is neither active nor pending. If you want to free or reuse the memory used by the watcher it is therefore a good idea to always call its <tt>&quot;ev_TYPE_stop&quot;</tt> function.</p>
<dt>bool ev_is_active (ev_TYPE *watcher)</p>
<dd> Returns a true value iff the watcher is active (i.e. it has been started and not yet been stopped). As long as a watcher is active you must not modify it.</p>
<dt>bool ev_is_pending (ev_TYPE *watcher)</p>
<dd> Returns a true value iff the watcher is pending, (i.e. it has outstanding events but its callback has not yet been invoked). As long as a watcher is pending (but not active) you must not call an init function on it (but <tt>&quot;ev_TYPE_set&quot;</tt> is safe), you must not change its priority, and you must make sure the watcher is available to libev (e.g. you cannot <tt>&quot;free ()&quot;</tt> it).</p>
<dt>callback ev_cb (ev_TYPE *watcher)</p>
<dd> Returns the callback currently set on the watcher.</p>
<dt>ev_cb_set (ev_TYPE *watcher, callback)</p>
<dd> Change the callback. You can change the callback at virtually any time (modulo threads).</p>
<dt>ev_set_priority (ev_TYPE *watcher, priority)</p>
<dd>
<dt>int ev_priority (ev_TYPE *watcher)</p>
<dd> Set and query the priority of the watcher. The priority is a small integer between <tt>&quot;EV_MAXPRI&quot;</tt> (default: <tt>2</tt>) and <tt>&quot;EV_MINPRI&quot;</tt> (default: <tt>&quot;-2&quot;</tt>). Pending watchers with higher priority will be invoked before watchers with lower priority, but priority will not keep watchers from being executed (except for <tt>&quot;ev_idle&quot;</tt> watchers). </p>
<p> If you need to suppress invocation when higher priority events are pending you need to look at <tt>&quot;ev_idle&quot;</tt> watchers, which provide this functionality. </p>
<p> You <i>must not</i> change the priority of a watcher as long as it is active or pending. </p>
<p> Setting a priority outside the range of <tt>&quot;EV_MINPRI&quot;</tt> to <tt>&quot;EV_MAXPRI&quot;</tt> is fine, as long as you do not mind that the priority value you query might or might not have been clamped to the valid range. </p>
<p> The default priority used by watchers when no priority has been set is always <tt>0</tt>, which is supposed to not be too high and not be too low :). </p>
<p> See &#8220;<font SIZE="-1">WATCHER</font> <font SIZE="-1">PRIORITY</font> <font SIZE="-1">MODELS</font>&#8221;, below, for a more thorough treatment of priorities.</p>
<dt>ev_invoke (loop, ev_TYPE *watcher, int revents)</p>
<dd> Invoke the <tt>&quot;watcher&quot;</tt> with the given <tt>&quot;loop&quot;</tt> and <tt>&quot;revents&quot;</tt>. Neither <tt>&quot;loop&quot;</tt> nor <tt>&quot;revents&quot;</tt> need to be valid as long as the watcher callback can deal with that fact, as both are simply passed through to the callback.</p>
<dt>int ev_clear_pending (loop, ev_TYPE *watcher)</p>
<dd> If the watcher is pending, this function clears its pending status and returns its <tt>&quot;revents&quot;</tt> bitset (as if its callback was invoked). If the watcher isn&#8217;t pending it does nothing and returns <tt>0</tt>. </p>
<p> Sometimes it can be useful to &#8220;poll&#8221; a watcher instead of waiting for its callback to be invoked, which can be accomplished with this function.</dl>
<h3><font SIZE="-1">ASSOCIATING</font> <font SIZE="-1">CUSTOM</font> <font SIZE="-1">DATA</font> <font SIZE="-1">WITH</font> A <font SIZE="-1">WATCHER</font></h3>
<p> Each watcher has, by default, a member <tt>&quot;void *data&quot;</tt> that you can change and read at any time: libev will completely ignore it. This can be used to associate arbitrary data with your watcher. If you need more data and don&#8217;t want to allocate memory and store a pointer to it in that data member, you can also &#8220;subclass&#8221; the watcher type and provide your own data: </p>
<p>struct my_io {<br />
    ev_io io;<br />
    int otherfd;<br />
    void *somedata;<br />
    struct whatever *mostinteresting;<br />
};<br />
&#8230; struct my_io w;<br />
ev_io_init(&amp;w.io, my_cb, fd, EV_READ);</p>
<p> And since your callback will be called with a pointer to the watcher, you can cast it back to your own type: </p>
<p>static void my_cb(struct ev_loop *loop, ev_io *w_, int revents)<br />
{<br />
    struct my_io *w = (struct my_io *)w_;<br />
    &#8230;<br />
}</p>
<p> More interesting and less C-conformant ways of casting your callback type instead have been omitted. </p>
<p> Another common scenario is to use some data structure with multiple embedded watchers: </p>
<p>struct my_biggy {<br />
    int some_data;<br />
    ev_timer t1;<br />
    ev_timer t2;<br />
}</p>
<p> In this case getting the pointer to <tt>&quot;my_biggy&quot;</tt> is a bit more complicated: Either you store the address of your <tt>&quot;my_biggy&quot;</tt> struct in the <tt>&quot;data&quot;</tt> member of the watcher (for woozies), or you need to use some pointer arithmetic using <tt>&quot;offsetof&quot;</tt> inside your watchers (for real programmers): </p>
<p>#include &lt;stddef.h&gt;<br />
static void<br />
t1_cb(EV_P_ ev_timer *w, int revents)<br />
{<br />
    struct my_biggy big = (struct my_biggy *)(((char *)w) &#8211; offsetof(struct my_biggy, t1));<br />
}<br />
static void<br />
t2_cb(EV_P_ ev_timer *w, int revents)<br />
{<br />
    struct my_biggy big = (struct my_biggy *)(((char *)w) &#8211; offsetof(struct my_biggy, t2));<br />
}</p>
<h3><font SIZE="-1">WATCHER</font> <font SIZE="-1">PRIORITY</font> <font SIZE="-1">MODELS</font></h3>
<p> Many event loops support <i>watcher priorities</i>, which are usually small integers that influence the ordering of event callback invocation between watchers in some way, all else being equal. </p>
<p> In libev, Watcher priorities can be set using <tt>&quot;ev_set_priority&quot;</tt>. See its description for the more technical details such as the actual priority range. </p>
<p> There are two common ways how these these priorities are being interpreted by event loops: </p>
<p> In the more common lock-out model, higher priorities &#8220;lock out&#8221; invocation of lower priority watchers, which means as long as higher priority watchers receive events, lower priority watchers are not being invoked. </p>
<p> The less common only-for-ordering model uses priorities solely to order callback invocation within a single event loop iteration: Higher priority watchers are invoked before lower priority ones, but they all get invoked before polling for new events. </p>
<p> Libev uses the second (only-for-ordering) model for all its watchers except for idle watchers (which use the lock-out model). </p>
<p> The rationale behind this is that implementing the lock-out model for watchers is not well supported by most kernel interfaces, and most event libraries will just poll for the same events again and again as long as their callbacks have not been executed, which is very inefficient in the common case of one high-priority watcher locking out a mass of lower priority ones. </p>
<p> Static (ordering) priorities are most useful when you have two or more watchers handling the same resource: a typical usage example is having an <tt>&quot;ev_io&quot;</tt> watcher to receive data, and an associated <tt>&quot;ev_timer&quot;</tt> to handle timeouts. Under load, data might be received while the program handles other jobs, but since timers normally get invoked first, the timeout handler will be executed before checking for data. In that case, giving the timer a lower priority than the I/O watcher ensures that I/O will be handled first even under adverse conditions (which is usually, but not always, what you want). </p>
<p> Since idle watchers use the &#8220;lock-out&#8221; model, meaning that idle watchers will only be executed when no same or higher priority watchers have received events, they can be used to implement the &#8220;lock-out&#8221; model when required. </p>
<p> For example, to emulate how many other event libraries handle priorities, you can associate an <tt>&quot;ev_idle&quot;</tt> watcher to each such watcher, and in the normal watcher callback, you just start the idle watcher. The real processing is done in the idle watcher callback. This causes libev to continously poll and process kernel event data for the watcher, but when the lock-out case is known to be rare (which in turn is rare :), this is workable. </p>
<p> Usually, however, the lock-out model implemented that way will perform miserably under the type of load it was designed to handle. In that case, it might be preferable to stop the real watcher before starting the idle watcher, so the kernel will not have to process the event in case the actual processing will be delayed for considerable time. </p>
<p> Here is an example of an I/O watcher that should run at a strictly lower priority than the default, and which should only process data when no other events are pending: </p>
<p>ev_idle idle; // actual processing watcher<br />
ev_io io;     // actual event watcher<br />
static void<br />
io_cb(EV_P_ ev_io *w, int revents)<br />
{<br />
    // stop the I/O watcher, we received the event, but<br />
    // are not yet ready to handle it.<br />
    ev_io_stop(EV_A_ w);<br />
    // start the idle watcher to ahndle the actual event.<br />
    // it will not be executed as long as other watchers<br />
    // with the default priority are receiving events.<br />
    ev_idle_start(EV_A_ &amp; idle);<br />
}<br />
static void<br />
idle_cb(EV_P_ ev_idle *w, int revents)<br />
{<br />
    // actual processing<br />
    read(STDIN_FILENO, &#8230;);<br />
    // have to start the I/O watcher again, as<br />
    // we have handled the event<br />
    ev_io_start(EV_P_ &amp; io);<br />
}<br />
// initialisation<br />
ev_idle_init(&amp;idle, idle_cb);<br />
ev_io_init(&amp;io, io_cb, STDIN_FILENO, EV_READ);<br />
ev_io_start(EV_DEFAULT_ &amp;io);</p>
<p> In the &#8220;real&#8221; world, it might also be beneficial to start a timer, so that low-priority connections can not be locked out forever under load. This enables your program to keep a lower latency for important connections during short periods of high load, while not completely locking out less important ones.</p>
<h2>WATCHER TYPES</h2>
<p> This section describes each watcher in detail, but will not repeat information given in the last section. Any initialisation/set macros, functions and members specific to the watcher type are explained. </p>
<p> Members are additionally marked with either <i>[read-only]</i>, meaning that, while the watcher is active, you can look at the member and expect some sensible content, but you must not modify it (you can modify it while the watcher is stopped to your hearts content), or <i>[read-write]</i>, which means you can expect it to have some sensible content while the watcher is active, but you can also modify it. Modifying it may not do something sensible or take immediate effect (or do anything at all), but libev will not crash or malfunction in any way.</p>
<h3>ev_io &#8211; is this file descriptor readable or writable?</h3>
<p> I/O watchers check whether a file descriptor is readable or writable in each iteration of the event loop, or, more precisely, when reading would not block the process and writing would at least be able to write some data. This behaviour is called level-triggering because you keep receiving events as long as the condition persists. Remember you can stop the watcher if you don&#8217;t want to act on the event and neither want to receive future events. </p>
<p> In general you can register as many read and/or write event watchers per fd as you want (as long as you don&#8217;t confuse yourself). Setting all file descriptors to non-blocking mode is also usually a good idea (but not required if you know what you are doing). </p>
<p> If you cannot use non-blocking mode, then force the use of a known-to-be-good backend (at the time of this writing, this includes only <tt>&quot;EVBACKEND_SELECT&quot;</tt> and <tt>&quot;EVBACKEND_POLL&quot;</tt>). The same applies to file descriptors for which non-blocking operation makes no sense (such as files) &#8211; libev doesn&#8217;t guarentee any specific behaviour in that case. </p>
<p> Another thing you have to watch out for is that it is quite easy to receive &#8220;spurious&#8221; readiness notifications, that is your callback might be called with <tt>&quot;EV_READ&quot;</tt> but a subsequent <tt>&quot;read&quot;</tt>(2) will actually block because there is no data. Not only are some backends known to create a lot of those (for example Solaris ports), it is very easy to get into this situation even with a relatively standard program structure. Thus it is best to always use non-blocking I/O: An extra <tt>&quot;read&quot;</tt>(2) returning <tt>&quot;EAGAIN&quot;</tt> is far preferable to a program hanging until some data arrives. </p>
<p> If you cannot run the fd in non-blocking mode (for example you should not play around with an Xlib connection), then you have to separately re-test whether a file descriptor is really ready with a known-to-be good interface such as poll (fortunately in our Xlib example, Xlib already does this on its own, so its quite safe to use). Some people additionally use <tt>&quot;SIGALRM&quot;</tt> and an interval timer, just to be sure you won&#8217;t block indefinitely. </p>
<p> But really, best use non-blocking mode. </p>
<p> <i>The special problem of disappearing file descriptors</i> </p>
<p> Some backends (e.g. kqueue, epoll) need to be told about closing a file descriptor (either due to calling <tt>&quot;close&quot;</tt> explicitly or any other means, such as <tt>&quot;dup2&quot;</tt>). The reason is that you register interest in some file descriptor, but when it goes away, the operating system will silently drop this interest. If another file descriptor with the same number then is registered with libev, there is no efficient way to see that this is, in fact, a different file descriptor. </p>
<p> To avoid having to explicitly tell libev about such cases, libev follows the following policy: Each time <tt>&quot;ev_io_set&quot;</tt> is being called, libev will assume that this is potentially a new file descriptor, otherwise it is assumed that the file descriptor stays the same. That means that you <i>have</i> to call <tt>&quot;ev_io_set&quot;</tt> (or <tt>&quot;ev_io_init&quot;</tt>) when you change the descriptor even if the file descriptor number itself did not change. </p>
<p> This is how one would do it normally anyway, the important point is that the libev application should not optimise around libev but should leave optimisations to libev. </p>
<p> <i>The special problem of dup&#8217;ed file descriptors</i> </p>
<p> Some backends (e.g. epoll), cannot register events for file descriptors, but only events for the underlying file descriptions. That means when you have <tt>&quot;dup ()&quot;</tt>&#8216;ed file descriptors or weirder constellations, and register events for them, only one file descriptor might actually receive events. </p>
<p> There is no workaround possible except not registering events for potentially <tt>&quot;dup ()&quot;</tt>&#8216;ed file descriptors, or to resort to <tt>&quot;EVBACKEND_SELECT&quot;</tt> or <tt>&quot;EVBACKEND_POLL&quot;</tt>. </p>
<p> <i>The special problem of fork</i> </p>
<p> Some backends (epoll, kqueue) do not support <tt>&quot;fork ()&quot;</tt> at all or exhibit useless behaviour. Libev fully supports fork, but needs to be told about it in the child. </p>
<p> To support fork in your programs, you either have to call <tt>&quot;ev_default_fork ()&quot;</tt> or <tt>&quot;ev_loop_fork ()&quot;</tt> after a fork in the child, enable <tt>&quot;EVFLAG_FORKCHECK&quot;</tt>, or resort to <tt>&quot;EVBACKEND_SELECT&quot;</tt> or <tt>&quot;EVBACKEND_POLL&quot;</tt>. </p>
<p> <i>The special problem of </i><font SIZE="-1"><i>SIGPIPE</i></font><i></i> </p>
<p> While not really specific to libev, it is easy to forget about <tt>&quot;SIGPIPE&quot;</tt>: when writing to a pipe whose other end has been closed, your program gets sent a <font SIZE="-1">SIGPIPE</font>, which, by default, aborts your program. For most programs this is sensible behaviour, for daemons, this is usually undesirable. </p>
<p> So when you encounter spurious, unexplained daemon exits, make sure you ignore <font SIZE="-1">SIGPIPE</font> (and maybe make sure you log the exit status of your daemon somewhere, as that would have given you a big clue). </p>
<p> <i>Watcher-Specific Functions</i></p>
<dl>
<dt>ev_io_init (ev_io *, callback, int fd, int events)</p>
<dd>
<dt>ev_io_set (ev_io *, int fd, int events)</p>
<dd> Configures an <tt>&quot;ev_io&quot;</tt> watcher. The <tt>&quot;fd&quot;</tt> is the file descriptor to receive events for and <tt>&quot;events&quot;</tt> is either <tt>&quot;EV_READ&quot;</tt>, <tt>&quot;EV_WRITE&quot;</tt> or <tt>&quot;EV_READ | EV_WRITE&quot;</tt>, to express the desire to receive the given events.</p>
<dt>int fd [read-only]</p>
<dd> The file descriptor being watched.</p>
<dt>int events [read-only]</p>
<dd> The events being watched.</dl>
<p> <i>Examples</i> </p>
<p> Example: Call <tt>&quot;stdin_readable_cb&quot;</tt> when <font SIZE="-1">STDIN_FILENO</font> has become, well readable, but only once. Since it is likely line-buffered, you could attempt to read a whole line in the callback. </p>
<p>static void<br />
stdin_readable_cb(struct ev_loop *loop, ev_io *w, int revents)<br />
{<br />
    ev_io_stop(loop, w);<br />
    ..read from stdin here(or from w-&gt;fd) and handle any I / O errors<br />
}<br />
&#8230; struct ev_loop *loop = ev_default_init(0);<br />
ev_io stdin_readable;<br />
ev_io_init(&amp;stdin_readable, stdin_readable_cb, STDIN_FILENO, EV_READ);<br />
ev_io_start(loop, &amp;stdin_readable);<br />
ev_loop(loop, 0);</p>
<h3>ev_timer &#8211; relative and optionally repeating timeouts</h3>
<p> Timer watchers are simple relative timers that generate an event after a given time, and optionally repeating in regular intervals after that. </p>
<p> The timers are based on real time, that is, if you register an event that times out after an hour and you reset your system clock to January last year, it will still time out after (roughly) one hour. &#8220;Roughly&#8221; because detecting time jumps is hard, and some inaccuracies are unavoidable (the monotonic clock option helps a lot here). </p>
<p> The callback is guaranteed to be invoked only <i>after</i> its timeout has passed (not <i>at</i>, so on systems with very low-resolution clocks this might introduce a small delay). If multiple timers become ready during the same loop iteration then the ones with earlier time-out values are invoked before ones of the same priority with later time-out values (but this is no longer true when a callback calls <tt>&quot;ev_loop&quot;</tt> recursively). </p>
<p> <i>Be smart about timeouts</i> </p>
<p> Many real-world problems involve some kind of timeout, usually for error recovery. A typical example is an <font SIZE="-1">HTTP</font> request &#8211; if the other side hangs, you want to raise some error after a while. </p>
<p> What follows are some ways to handle this problem, from obvious and inefficient to smart and efficient. </p>
<p> In the following, a 60 second activity timeout is assumed &#8211; a timeout that gets reset to 60 seconds each time there is activity (e.g. each time some data or other life sign was received).</p>
<dl>
<dt>1. Use a timer and stop, reinitialise and start it on activity.</p>
<dd> This is the most obvious, but not the most simple way: In the beginning, start the watcher: </p>
<p>ev_timer_init(timer, callback, 60., 0.);<br />
ev_timer_start(loop, timer);</p>
<p> Then, each time there is some activity, <tt>&quot;ev_timer_stop&quot;</tt> it, initialise it and start it again: </p>
<p>ev_timer_stop(loop, timer);<br />
ev_timer_set(timer, 60., 0.);<br />
ev_timer_start(loop, timer);</p>
<p> This is relatively simple to implement, but means that each time there is some activity, libev will first have to remove the timer from its internal data structure and then add it again. Libev tries to be fast, but it&#8217;s still not a constant-time operation.</p>
<dt>2. Use a timer and re-start it with ev_timer_again inactivity.</p>
<dd> This is the easiest way, and involves using <tt>&quot;ev_timer_again&quot;</tt> instead of <tt>&quot;ev_timer_start&quot;</tt>. </p>
<p> To implement this, configure an <tt>&quot;ev_timer&quot;</tt> with a <tt>&quot;repeat&quot;</tt> value of <tt>60</tt> and then call <tt>&quot;ev_timer_again&quot;</tt> at start and each time you successfully read or write some data. If you go into an idle state where you do not expect data to travel on the socket, you can <tt>&quot;ev_timer_stop&quot;</tt> the timer, and <tt>&quot;ev_timer_again&quot;</tt> will automatically restart it if need be. </p>
<p> That means you can ignore both the <tt>&quot;ev_timer_start&quot;</tt> function and the <tt>&quot;after&quot;</tt> argument to <tt>&quot;ev_timer_set&quot;</tt>, and only ever use the <tt>&quot;repeat&quot;</tt> member and <tt>&quot;ev_timer_again&quot;</tt>. </p>
<p> At start: </p>
<p>ev_init(timer, callback);<br />
timer-&gt;repeat = 60.;<br />
ev_timer_again(loop, timer);</p>
<p> Each time there is some activity: </p>
<pre>
   ev_timer_again (loop, timer);
</pre>
<p> It is even possible to change the time-out on the fly, regardless of whether the watcher is active or not: </p>
<p>timer-&gt;repeat = 30.;<br />
ev_timer_again(loop, timer);</p>
<p> This is slightly more efficient then stopping/starting the timer each time you want to modify its timeout value, as libev does not have to completely remove and re-insert the timer from/into its internal data structure. </p>
<p> It is, however, even simpler than the &#8220;obvious&#8221; way to do it.</p>
<dt>3. Let the timer time out, but then re-arm it as required.</p>
<dd> This method is more tricky, but usually most efficient: Most timeouts are relatively long compared to the intervals between other activity &#8211; in our example, within 60 seconds, there are usually many I/O events with associated activity resets. </p>
<p> In this case, it would be more efficient to leave the <tt>&quot;ev_timer&quot;</tt> alone, but remember the time of last activity, and check for a real timeout only within the callback: </p>
<p>ev_tstamp last_activity; // time of last activity<br />
static void<br />
callback(EV_P_ ev_timer *w, int revents)<br />
{<br />
    ev_tstamp now = ev_now(EV_A);<br />
    ev_tstamp timeout = last_activity + 60.;<br />
    // if last_activity + 60. is older than now, we did time out<br />
    if (timeout &lt; now) {<br />
        // timeout occured, take action<br />
    } else {<br />
        // callback was invoked, but there was some activity, re-arm<br />
        // the watcher to fire in last_activity + 60, which is<br />
        // guaranteed to be in the future, so &#8220;again&#8221; is positive:<br />
        w-&gt;repeat = timeout &#8211; now;<br />
        ev_timer_again(EV_A_ w);<br />
    }<br />
}</p>
<p> To summarise the callback: first calculate the real timeout (defined as &#8220;60 seconds after the last activity&#8221;), then check if that time has been reached, which means something <i>did</i>, in fact, time out. Otherwise the callback was invoked too early (<tt>&quot;timeout&quot;</tt> is in the future), so re-schedule the timer to fire at that future time, to see if maybe we have a timeout then. </p>
<p> Note how <tt>&quot;ev_timer_again&quot;</tt> is used, taking advantage of the <tt>&quot;ev_timer_again&quot;</tt> optimisation when the timer is already running. </p>
<p> This scheme causes more callback invocations (about one every 60 seconds minus half the average time between activity), but virtually no calls to libev to change the timeout. </p>
<p> To start the timer, simply initialise the watcher and set <tt>&quot;last_activity&quot;</tt> to the current time (meaning we just have some activity :), then call the callback, which will &#8220;do the right thing&#8221; and start the timer: </p>
<p>ev_init(timer, callback);<br />
last_activity = ev_now(loop);<br />
callback(loop, timer, EV_TIMEOUT);</p>
<p> And when there is some activity, simply store the current time in <tt>&quot;last_activity&quot;</tt>, no libev calls at all: </p>
<pre>
   last_actiivty = ev_now (loop);
</pre>
<p> This technique is slightly more complex, but in most cases where the time-out is unlikely to be triggered, much more efficient. </p>
<p> Changing the timeout is trivial as well (if it isn&#8217;t hard-coded in the callback :) &#8211; just change the timeout and invoke the callback, which will fix things for you.</p>
<dt>4. Wee, just use a double-linked list for your timeouts.</p>
<dd> If there is not one request, but many thousands (millions&#8230;), all employing some kind of timeout with the same timeout value, then one can do even better: </p>
<p> When starting the timeout, calculate the timeout value and put the timeout at the <i>end</i> of the list. </p>
<p> Then use an <tt>&quot;ev_timer&quot;</tt> to fire when the timeout at the <i>beginning</i> of the list is expected to fire (for example, using the technique #3). </p>
<p> When there is some activity, remove the timer from the list, recalculate the timeout, append it to the end of the list again, and make sure to update the <tt>&quot;ev_timer&quot;</tt> if it was taken from the beginning of the list. </p>
<p> This way, one can manage an unlimited number of timeouts in <a href="/docs/linux/man/1-o/">O</a>(1) time for starting, stopping and updating the timers, at the expense of a major complication, and having to use a constant timeout. The constant timeout ensures that the list stays sorted.</dl>
<p> So which method the best? </p>
<p> Method #2 is a simple no-brain-required solution that is adequate in most situations. Method #3 requires a bit more thinking, but handles many cases better, and isn&#8217;t very complicated either. In most case, choosing either one is fine, with #3 being better in typical situations. </p>
<p> Method #1 is almost always a bad idea, and buys you nothing. Method #4 is rather complicated, but extremely efficient, something that really pays off after the first million or so of active timers, i.e. it&#8217;s usually overkill :) </p>
<p> <i>The special problem of time updates</i> </p>
<p> Establishing the current time is a costly operation (it usually takes at least two system calls): <font SIZE="-1">EV</font> therefore updates its idea of the current time only before and after <tt>&quot;ev_loop&quot;</tt> collects new events, which causes a growing difference between <tt>&quot;ev_now ()&quot;</tt> and <tt>&quot;ev_time ()&quot;</tt> when handling lots of events in one iteration. </p>
<p> The relative timeouts are calculated relative to the <tt>&quot;ev_now ()&quot;</tt> time. This is usually the right thing as this timestamp refers to the time of the event triggering whatever timeout you are modifying/starting. If you suspect event processing to be delayed and you <i>need</i> to base the timeout on the current time, use something like this to adjust for this: </p>
<pre>
   ev_timer_set (&amp;timer, after + ev_now () - ev_time (), 0.);
</pre>
<p> If the event loop is suspended for a long time, you can also force an update of the time returned by <tt>&quot;ev_now ()&quot;</tt> by calling <tt>&quot;ev_now_update ()&quot;</tt>. </p>
<p> <i>The special problems of suspended animation</i> </p>
<p> When you leave the server world it is quite customary to hit machines that can suspend/hibernate &#8211; what happens to the clocks during such a suspend? </p>
<p> Some quick tests made with a Linux 2.6.28 indicate that a suspend freezes all processes, while the clocks (<tt>&quot;times&quot;</tt>, <tt>&quot;CLOCK_MONOTONIC&quot;</tt>) continue to run until the system is suspended, but they will not advance while the system is suspended. That means, on resume, it will be as if the program was frozen for a few seconds, but the suspend time will not be counted towards <tt>&quot;ev_timer&quot;</tt> when a monotonic clock source is used. The real time clock advanced as expected, but if it is used as sole clocksource, then a long suspend would be detected as a time jump by libev, and timers would be adjusted accordingly. </p>
<p> I would not be surprised to see different behaviour in different between operating systems, <font SIZE="-1">OS</font> versions or even different hardware. </p>
<p> The other form of suspend (job control, or sending a <font SIZE="-1">SIGSTOP</font>) will see a time jump in the monotonic clocks and the realtime clock. If the program is suspended for a very long time, and monotonic clock sources are in use, then you can expect <tt>&quot;ev_timer&quot;</tt>s to expire as the full suspension time will be counted towards the timers. When no monotonic clock source is in use, then libev will again assume a timejump and adjust accordingly. </p>
<p> It might be beneficial for this latter case to call <tt>&quot;ev_suspend&quot;</tt> and <tt>&quot;ev_resume&quot;</tt> in code that handles <tt>&quot;SIGTSTP&quot;</tt>, to at least get deterministic behaviour in this case (you can do nothing against <tt>&quot;SIGSTOP&quot;</tt>). </p>
<p> <i>Watcher-Specific Functions and Data Members</i></p>
<dl>
<dt>ev_timer_init (ev_timer *, callback, ev_tstamp after, ev_tstamp repeat)</p>
<dd>
<dt>ev_timer_set (ev_timer *, ev_tstamp after, ev_tstamp repeat)</p>
<dd> Configure the timer to trigger after <tt>&quot;after&quot;</tt> seconds. If <tt>&quot;repeat&quot;</tt> is <tt>0.</tt>, then it will automatically be stopped once the timeout is reached. If it is positive, then the timer will automatically be configured to trigger again <tt>&quot;repeat&quot;</tt> seconds later, again, and again, until stopped manually. </p>
<p> The timer itself will do a best-effort at avoiding drift, that is, if you configure a timer to trigger every 10 seconds, then it will normally trigger at exactly 10 second intervals. If, however, your program cannot keep up with the timer (because it takes longer than those 10 seconds to do stuff) the timer will not fire more than once per event loop iteration.</p>
<dt>ev_timer_again (loop, ev_timer *)</p>
<dd> This will act as if the timer timed out and restart it again if it is repeating. The exact semantics are: </p>
<p> If the timer is pending, its pending status is cleared. </p>
<p> If the timer is started but non-repeating, stop it (as if it timed out). </p>
<p> If the timer is repeating, either start it if necessary (with the <tt>&quot;repeat&quot;</tt> value), or reset the running timer to the <tt>&quot;repeat&quot;</tt> value. </p>
<p> This sounds a bit complicated, see &#8220;Be smart about timeouts&#8221;, above, for a usage example.</p>
<dt>ev_timer_remaining (loop, ev_timer *)</p>
<dd> Returns the remaining time until a timer fires. If the timer is active, then this time is relative to the current event loop time, otherwise it&#8217;s the timeout value currently configured. </p>
<p> That is, after an <tt>&quot;ev_timer_set (w, 5, 7)&quot;</tt>, <tt>&quot;ev_timer_remaining&quot;</tt> returns <tt>5</tt>. When the timer is started and one second passes, <tt>&quot;ev_timer_remain&quot;</tt> will return <tt>4</tt>. When the timer expires and is restarted, it will return roughly <tt>7</tt> (likely slightly less as callback invocation takes some time, too), and so on.</p>
<dt>ev_tstamp repeat [read-write]</p>
<dd> The current <tt>&quot;repeat&quot;</tt> value. Will be used each time the watcher times out or <tt>&quot;ev_timer_again&quot;</tt> is called, and determines the next timeout (if any), which is also when any modifications are taken into account.</dl>
<p> <i>Examples</i> </p>
<p> Example: Create a timer that fires after 60 seconds. </p>
<p>static void<br />
one_minute_cb(struct ev_loop *loop, ev_timer *w, int revents){<br />
    ..one minute over, w is actually stopped right here} ev_timer mytimer;<br />
ev_timer_init(&amp;mytimer, one_minute_cb, 60., 0.);<br />
ev_timer_start(loop, &amp;mytimer);</p>
<p> Example: Create a timeout timer that times out after 10 seconds of inactivity. </p>
<p>static void<br />
timeout_cb(struct ev_loop *loop, ev_timer *w, int revents){<br />
    ..ten seconds without any activity} ev_timer mytimer;<br />
ev_timer_init(&amp;mytimer, timeout_cb, 0., 10.); /* note, only repeat used */<br />
ev_timer_again(&amp;mytimer);                     /* start timer */<br />
ev_loop(loop, 0);<br />
// and in some piece of code that gets executed on any &#8220;activity&#8221;:<br />
// reset the timeout to start ticking again at 10 seconds<br />
ev_timer_again(&amp;mytimer);</p>
<h3>ev_periodic &#8211; to cron or not to cron?</h3>
<p> Periodic watchers are also timers of a kind, but they are very versatile (and unfortunately a bit complex). </p>
<p> Unlike <tt>&quot;ev_timer&quot;</tt>, periodic watchers are not based on real time (or relative time, the physical time that passes) but on wall clock time (absolute time, the thing you can read on your calender or clock). The difference is that wall clock time can run faster or slower than real time, and time jumps are not uncommon (e.g. when you adjust your wrist-watch). </p>
<p> You can tell a periodic watcher to trigger after some specific point in time: for example, if you tell a periodic watcher to trigger &#8220;in 10 seconds&#8221; (by specifying e.g. <tt>&quot;ev_now () + 10.&quot;</tt>, that is, an absolute time not a delay) and then reset your system clock to January of the previous year, then it will take a year or more to trigger the event (unlike an <tt>&quot;ev_timer&quot;</tt>, which would still trigger roughly 10 seconds after starting it, as it uses a relative timeout). </p>
<p> <tt>&quot;ev_periodic&quot;</tt> watchers can also be used to implement vastly more complex timers, such as triggering an event on each &#8220;midnight, local time&#8221;, or other complicated rules. This cannot be done with <tt>&quot;ev_timer&quot;</tt> watchers, as those cannot react to time jumps. </p>
<p> As with timers, the callback is guaranteed to be invoked only when the point in time where it is supposed to trigger has passed. If multiple timers become ready during the same loop iteration then the ones with earlier time-out values are invoked before ones with later time-out values (but this is no longer true when a callback calls <tt>&quot;ev_loop&quot;</tt> recursively). </p>
<p> <i>Watcher-Specific Functions and Data Members</i></p>
<dl>
<dt>ev_periodic_init (ev_periodic *, callback, ev_tstamp offset, ev_tstamp interval, reschedule_cb)</p>
<dd>
<dt>ev_periodic_set (ev_periodic *, ev_tstamp offset, ev_tstamp interval, reschedule_cb)</p>
<dd> Lots of arguments, let&#8217;s sort it out&#8230; There are basically three modes of operation, and we will explain them from simplest to most complex:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> absolute timer (offset = absolute time, interval = 0, reschedule_cb = 0) </p>
<p> In this configuration the watcher triggers an event after the wall clock time <tt>&quot;offset&quot;</tt> has passed. It will not repeat and will not adjust when a time jump occurs, that is, if it is to be run at January 1st 2011 then it will be stopped and invoked when the system clock reaches or surpasses this point in time.</p>
<dt>*</p>
<dd> repeating interval timer (offset = offset within interval, interval &gt; 0, reschedule_cb = 0) </p>
<p> In this mode the watcher will always be scheduled to time out at the next <tt>&quot;offset + N * interval&quot;</tt> time (for some integer N, which can also be negative) and then repeat, regardless of any time jumps. The <tt>&quot;offset&quot;</tt> argument is merely an offset into the <tt>&quot;interval&quot;</tt> periods. </p>
<p> This can be used to create timers that do not drift with respect to the system clock, for example, here is an <tt>&quot;ev_periodic&quot;</tt> that triggers each hour, on the hour (with respect to <font SIZE="-1">UTC</font>): </p>
<pre>
   ev_periodic_set (&amp;periodic, 0., 3600., 0);
</pre>
<p> This doesn&#8217;t mean there will always be 3600 seconds in between triggers, but only that the callback will be called when the system time shows a full hour (<font SIZE="-1">UTC</font>), or more correctly, when the system time is evenly divisible by 3600. </p>
<p> Another way to think about it (for the mathematically inclined) is that <tt>&quot;ev_periodic&quot;</tt> will try to run the callback in this mode at the next possible time where <tt>&quot;time = offset (mod interval)&quot;</tt>, regardless of any time jumps. </p>
<p> For numerical stability it is preferable that the <tt>&quot;offset&quot;</tt> value is near <tt>&quot;ev_now ()&quot;</tt> (the current time), but there is no range requirement for this value, and in fact is often specified as zero. </p>
<p> Note also that there is an upper limit to how often a timer can fire (<font SIZE="-1">CPU</font> speed for example), so if <tt>&quot;interval&quot;</tt> is very small then timing stability will of course deteriorate. Libev itself tries to be exact to be about one millisecond (if the <font SIZE="-1">OS</font> supports it and the machine is fast enough).</p>
<dt>*</p>
<dd> manual reschedule mode (offset ignored, interval ignored, reschedule_cb = callback) </p>
<p> In this mode the values for <tt>&quot;interval&quot;</tt> and <tt>&quot;offset&quot;</tt> are both being ignored. Instead, each time the periodic watcher gets scheduled, the reschedule callback will be called with the watcher as first, and the current time as second argument. </p>
<p> <font SIZE="-1">NOTE:</font> <i>This callback </i><font SIZE="-1"><i>MUST</i></font><i> </i><font SIZE="-1"><i>NOT</i></font><i> stop or destroy any periodic watcher, ever, or make </i><font SIZE="-1"><i>ANY</i></font><i> other event loop modifications whatsoever, unless explicitly allowed by documentation here</i>. </p>
<p> If you need to stop it, return <tt>&quot;now + 1e30&quot;</tt> (or so, fudge fudge) and stop it afterwards (e.g. by starting an <tt>&quot;ev_prepare&quot;</tt> watcher, which is the only event loop modification you are allowed to do). </p>
<p> The callback prototype is <tt>&quot;ev_tstamp (*reschedule_cb)(ev_periodic *w, ev_tstamp now)&quot;</tt>, e.g.: </p>
<p>static ev_tstamp<br />
my_rescheduler(ev_periodic *w, ev_tstamp now)<br />
{<br />
    return now + 60.;<br />
}</p>
<p> It must return the next time to trigger, based on the passed time value (that is, the lowest time value larger than to the second argument). It will usually be called just before the callback will be triggered, but might be called at other times, too. </p>
<p> <font SIZE="-1">NOTE:</font> <i>This callback must always return a time that is higher than or equal to the passed </i>&quot;now&quot;<i> value</i>. </p>
<p> This can be used to create very complex timers, such as a timer that triggers on &#8220;next midnight, local time&#8221;. To do this, you would calculate the next midnight after <tt>&quot;now&quot;</tt> and return the timestamp value for this. How you do this is, again, up to you (but it is not trivial, which is the main reason I omitted it as an example).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>ev_periodic_again (loop, ev_periodic *)</p>
<dd> Simply stops and restarts the periodic watcher again. This is only useful when you changed some parameters or the reschedule callback would return a different time than the last time it was called (e.g. in a crond like program when the crontabs have changed).</p>
<dt>ev_tstamp ev_periodic_at (ev_periodic *)</p>
<dd> When active, returns the absolute time that the watcher is supposed to trigger next. This is not the same as the <tt>&quot;offset&quot;</tt> argument to <tt>&quot;ev_periodic_set&quot;</tt>, but indeed works even in interval and manual rescheduling modes.</p>
<dt>ev_tstamp offset [read-write]</p>
<dd> When repeating, this contains the offset value, otherwise this is the absolute point in time (the <tt>&quot;offset&quot;</tt> value passed to <tt>&quot;ev_periodic_set&quot;</tt>, although libev might modify this value for better numerical stability). </p>
<p> Can be modified any time, but changes only take effect when the periodic timer fires or <tt>&quot;ev_periodic_again&quot;</tt> is being called.</p>
<dt>ev_tstamp interval [read-write]</p>
<dd> The current interval value. Can be modified any time, but changes only take effect when the periodic timer fires or <tt>&quot;ev_periodic_again&quot;</tt> is being called.</p>
<dt>ev_tstamp (*reschedule_cb)(ev_periodic *w, ev_tstamp now) [read-write]</p>
<dd> The current reschedule callback, or <tt>0</tt>, if this functionality is switched off. Can be changed any time, but changes only take effect when the periodic timer fires or <tt>&quot;ev_periodic_again&quot;</tt> is being called.</dl>
<p> <i>Examples</i> </p>
<p> Example: Call a callback every hour, or, more precisely, whenever the system time is divisible by 3600. The callback invocation times have potentially a lot of jitter, but good long-term stability. </p>
<p>static void<br />
clock_cb(struct ev_loop *loop, ev_io *w, int revents){<br />
    &#8230; its now a full hour(UTC, or TAI or whatever your clock follows)} ev_periodic hourly_tick;<br />
ev_periodic_init(&amp;hourly_tick, clock_cb, 0., 3600., 0);<br />
ev_periodic_start(loop, &amp;hourly_tick);</p>
<p> Example: The same as above, but use a reschedule callback to do it: </p>
<p>#include &lt;math.h&gt;<br />
static ev_tstamp<br />
my_scheduler_cb(ev_periodic *w, ev_tstamp now)<br />
{<br />
    return now + (3600. &#8211; fmod(now, 3600.));<br />
}<br />
ev_periodic_init(&amp;hourly_tick, clock_cb, 0., 0., my_scheduler_cb);</p>
<p> Example: Call a callback every hour, starting now: </p>
<p>ev_periodic hourly_tick;<br />
ev_periodic_init(&amp;hourly_tick, clock_cb,<br />
                 fmod(ev_now(loop), 3600.), 3600., 0);<br />
ev_periodic_start(loop, &amp;hourly_tick);</p>
<h3>ev_signal &#8211; signal me when a signal gets signalled!</h3>
<p> Signal watchers will trigger an event when the process receives a specific signal one or more times. Even though signals are very asynchronous, libev will try it&#8217;s best to deliver signals synchronously, i.e. as part of the normal event processing, like any other event. </p>
<p> If you want signals to be delivered truly asynchronously, just use <tt>&quot;sigaction&quot;</tt> as you would do without libev and forget about sharing the signal. You can even use <tt>&quot;ev_async&quot;</tt> from a signal handler to synchronously wake up an event loop. </p>
<p> You can configure as many watchers as you like for the same signal, but only within the same loop, i.e. you can watch for <tt>&quot;SIGINT&quot;</tt> in your default loop and for <tt>&quot;SIGIO&quot;</tt> in another loop, but you cannot watch for <tt>&quot;SIGINT&quot;</tt> in both the default loop and another loop at the same time. At the moment, <tt>&quot;SIGCHLD&quot;</tt> is permanently tied to the default loop. </p>
<p> When the first watcher gets started will libev actually register something with the kernel (thus it coexists with your own signal handlers as long as you don&#8217;t register any with libev for the same signal). </p>
<p> Both the signal mask state (<tt>&quot;sigprocmask&quot;</tt>) and the signal handler state (<tt>&quot;sigaction&quot;</tt>) are unspecified after starting a signal watcher (and after sotpping it again), that is, libev might or might not block the signal, and might or might not set or restore the installed signal handler. </p>
<p> If possible and supported, libev will install its handlers with <tt>&quot;SA_RESTART&quot;</tt> (or equivalent) behaviour enabled, so system calls should not be unduly interrupted. If you have a problem with system calls getting interrupted by signals you can block all signals in an <tt>&quot;ev_check&quot;</tt> watcher and unblock them in an <tt>&quot;ev_prepare&quot;</tt> watcher. </p>
<p> <i>Watcher-Specific Functions and Data Members</i></p>
<dl>
<dt>ev_signal_init (ev_signal *, callback, int signum)</p>
<dd>
<dt>ev_signal_set (ev_signal *, int signum)</p>
<dd> Configures the watcher to trigger on the given signal number (usually one of the <tt>&quot;SIGxxx&quot;</tt> constants).</p>
<dt>int signum [read-only]</p>
<dd> The signal the watcher watches out for.</dl>
<p> <i>Examples</i> </p>
<p> Example: Try to exit cleanly on <font SIZE="-1">SIGINT</font>. </p>
<p>static void<br />
sigint_cb(struct ev_loop *loop, ev_signal *w, int revents)<br />
{<br />
    ev_unloop(loop, EVUNLOOP_ALL);<br />
}<br />
ev_signal signal_watcher;<br />
ev_signal_init(&amp;signal_watcher, sigint_cb, SIGINT);<br />
ev_signal_start(loop, &amp;signal_watcher);</p>
<h3>ev_child &#8211; watch out for process status changes</h3>
<p> Child watchers trigger when your process receives a <font SIZE="-1">SIGCHLD</font> in response to some child status changes (most typically when a child of yours dies or exits). It is permissible to install a child watcher <i>after</i> the child has been forked (which implies it might have already exited), as long as the event loop isn&#8217;t entered (or is continued from a watcher), i.e., forking and then immediately registering a watcher for the child is fine, but forking and registering a watcher a few event loop iterations later or in the next callback invocation is not. </p>
<p> Only the default event loop is capable of handling signals, and therefore you can only register child watchers in the default event loop. </p>
<p> Due to some design glitches inside libev, child watchers will always be handled at maximum priority (their priority is set to <tt>&quot;EV_MAXPRI&quot;</tt> by libev) </p>
<p> <i>Process Interaction</i> </p>
<p> Libev grabs <tt>&quot;SIGCHLD&quot;</tt> as soon as the default event loop is initialised. This is necessary to guarantee proper behaviour even if the first child watcher is started after the child exits. The occurrence of <tt>&quot;SIGCHLD&quot;</tt> is recorded asynchronously, but child reaping is done synchronously as part of the event loop processing. Libev always reaps all children, even ones not watched. </p>
<p> <i>Overriding the Built-In Processing</i> </p>
<p> Libev offers no special support for overriding the built-in child processing, but if your application collides with libev&#8217;s default child handler, you can override it easily by installing your own handler for <tt>&quot;SIGCHLD&quot;</tt> after initialising the default loop, and making sure the default loop never gets destroyed. You are encouraged, however, to use an event-based approach to child reaping and thus use libev&#8217;s support for that, so other libev users can use <tt>&quot;ev_child&quot;</tt> watchers freely. </p>
<p> <i>Stopping the Child Watcher</i> </p>
<p> Currently, the child watcher never gets stopped, even when the child terminates, so normally one needs to stop the watcher in the callback. Future versions of libev might stop the watcher automatically when a child exit is detected (calling <tt>&quot;ev_child_stop&quot;</tt> twice is not a problem). </p>
<p> <i>Watcher-Specific Functions and Data Members</i></p>
<dl>
<dt>ev_child_init (ev_child *, callback, int pid, int trace)</p>
<dd>
<dt>ev_child_set (ev_child *, int pid, int trace)</p>
<dd> Configures the watcher to wait for status changes of process <tt>&quot;pid&quot;</tt> (or <i>any</i> process if <tt>&quot;pid&quot;</tt> is specified as <tt>0</tt>). The callback can look at the <tt>&quot;rstatus&quot;</tt> member of the <tt>&quot;ev_child&quot;</tt> watcher structure to see the status word (use the macros from <tt>&quot;sys/wait.h&quot;</tt> and see your systems <tt>&quot;waitpid&quot;</tt> documentation). The <tt>&quot;rpid&quot;</tt> member contains the pid of the process causing the status change. <tt>&quot;trace&quot;</tt> must be either <tt>0</tt> (only activate the watcher when the process terminates) or <tt>1</tt> (additionally activate the watcher when the process is stopped or continued).</p>
<dt>int pid [read-only]</p>
<dd> The process id this watcher watches out for, or <tt>0</tt>, meaning any process id.</p>
<dt>int rpid [read-write]</p>
<dd> The process id that detected a status change.</p>
<dt>int rstatus [read-write]</p>
<dd> The process exit/trace status caused by <tt>&quot;rpid&quot;</tt> (see your systems <tt>&quot;waitpid&quot;</tt> and <tt>&quot;sys/wait.h&quot;</tt> documentation for details).</dl>
<p> <i>Examples</i> </p>
<p> Example: <tt>&quot;fork()&quot;</tt> a new process and install a child handler to wait for its completion. </p>
<p>ev_child cw;<br />
static void<br />
child_cb(EV_P_ ev_child *w, int revents)<br />
{<br />
    ev_child_stop(EV_A_ w);<br />
    printf(&#8220;process %d exited with status %x
&#8221;, w-&gt;rpid, w-&gt;rstatus);<br />
}<br />
pid_t pid = fork();<br />
if (pid &lt; 0)<br />
    // error<br />
    else if (pid == 0)<br />
    {<br />
        // the forked child executes here<br />
        exit(1);<br />
    }<br />
else {<br />
    ev_child_init(&amp;cw, child_cb, pid, 0);<br />
    ev_child_start(EV_DEFAULT_ &amp; cw);<br />
}</p>
<h3>ev_stat &#8211; did the file attributes just change?</h3>
<p> This watches a file system path for attribute changes. That is, it calls <tt>&quot;stat&quot;</tt> on that path in regular intervals (or when the <font SIZE="-1">OS</font> says it changed) and sees if it changed compared to the last time, invoking the callback if it did. </p>
<p> The path does not need to exist: changing from &#8220;path exists&#8221; to &#8220;path does not exist&#8221; is a status change like any other. The condition &#8220;path does not exist&#8221; (or more correctly &#8220;path cannot be stat&#8217;ed&#8221;) is signified by the <tt>&quot;st_nlink&quot;</tt> field being zero (which is otherwise always forced to be at least one) and all the other fields of the stat buffer having unspecified contents. </p>
<p> The path <i>must not</i> end in a slash or contain special components such as <tt>&quot;.&quot;</tt> or <tt>&quot;..&quot;</tt>. The path <i>should</i> be absolute: If it is relative and your working directory changes, then the behaviour is undefined. </p>
<p> Since there is no portable change notification interface available, the portable implementation simply calls <tt><a href="/docs/linux/man/2-stat/">stat</a>(2)</tt> regularly on the path to see if it changed somehow. You can specify a recommended polling interval for this case. If you specify a polling interval of <tt>0</tt> (highly recommended!) then a <i>suitable, unspecified default</i> value will be used (which you can expect to be around five seconds, although this might change dynamically). Libev will also impose a minimum interval which is currently around <tt>0.1</tt>, but that&#8217;s usually overkill. </p>
<p> This watcher type is not meant for massive numbers of stat watchers, as even with OS-supported change notifications, this can be resource-intensive. </p>
<p> At the time of this writing, the only OS-specific interface implemented is the Linux inotify interface (implementing kqueue support is left as an exercise for the reader. Note, however, that the author sees no way of implementing <tt>&quot;ev_stat&quot;</tt> semantics with kqueue, except as a hint). </p>
<p> <i></i><font SIZE="-1"><i>ABI</i></font><i> Issues (Largefile Support)</i> </p>
<p> Libev by default (unless the user overrides this) uses the default compilation environment, which means that on systems with large file support disabled by default, you get the 32 bit version of the stat structure. When using the library from programs that change the <font SIZE="-1">ABI</font> to use 64 bit file offsets the programs will fail. In that case you have to compile libev with the same flags to get binary compatibility. This is obviously the case with any flags that change the <font SIZE="-1">ABI</font>, but the problem is most noticeably displayed with ev_stat and large file support. </p>
<p> The solution for this is to lobby your distribution maker to make large file interfaces available by default (as e.g. FreeBSD does) and not optional. Libev cannot simply switch on large file support because it has to exchange stat structures with application programs compiled using the default compilation environment. </p>
<p> <i>Inotify and Kqueue</i> </p>
<p> When <tt>&quot;inotify (7)&quot;</tt> support has been compiled into libev and present at runtime, it will be used to speed up change detection where possible. The inotify descriptor will be created lazily when the first <tt>&quot;ev_stat&quot;</tt> watcher is being started. </p>
<p> Inotify presence does not change the semantics of <tt>&quot;ev_stat&quot;</tt> watchers except that changes might be detected earlier, and in some cases, to avoid making regular <tt>&quot;stat&quot;</tt> calls. Even in the presence of inotify support there are many cases where libev has to resort to regular <tt>&quot;stat&quot;</tt> polling, but as long as kernel 2.6.25 or newer is used (2.6.24 and older have too many bugs), the path exists (i.e. stat succeeds), and the path resides on a local filesystem (libev currently assumes only ext2/3, jfs, reiserfs and xfs are fully working) libev usually gets away without polling. </p>
<p> There is no support for kqueue, as apparently it cannot be used to implement this functionality, due to the requirement of having a file descriptor open on the object at all times, and detecting renames, unlinks etc. is difficult. </p>
<p> <i></i>&quot;stat ()&quot;<i> is a synchronous operation</i> </p>
<p> Libev doesn&#8217;t normally do any kind of I/O itself, and so is not blocking the process. The exception are <tt>&quot;ev_stat&quot;</tt> watchers &#8211; those call <tt>&quot;stat ()&quot;</tt>, which is a synchronous operation. </p>
<p> For local paths, this usually doesn&#8217;t matter: unless the system is very busy or the intervals between stat&#8217;s are large, a stat call will be fast, as the path data is usually in memory already (except when starting the watcher). </p>
<p> For networked file systems, calling <tt>&quot;stat ()&quot;</tt> can block an indefinite time due to network issues, and even under good conditions, a stat call often takes multiple milliseconds. </p>
<p> Therefore, it is best to avoid using <tt>&quot;ev_stat&quot;</tt> watchers on networked paths, although this is fully supported by libev. </p>
<p> <i>The special problem of stat time resolution</i> </p>
<p> The <tt>&quot;stat ()&quot;</tt> system call only supports full-second resolution portably, and even on systems where the resolution is higher, most file systems still only support whole seconds. </p>
<p> That means that, if the time is the only thing that changes, you can easily miss updates: on the first update, <tt>&quot;ev_stat&quot;</tt> detects a change and calls your callback, which does something. When there is another update within the same second, <tt>&quot;ev_stat&quot;</tt> will be unable to detect unless the stat data does change in other ways (e.g. file size). </p>
<p> The solution to this is to delay acting on a change for slightly more than a second (or till slightly after the next full second boundary), using a roughly one-second-delay <tt>&quot;ev_timer&quot;</tt> (e.g. <tt>&quot;ev_timer_set (w, 0., 1.02); ev_timer_again (loop, w)&quot;</tt>). </p>
<p> The <tt>.02</tt> offset is added to work around small timing inconsistencies of some operating systems (where the second counter of the current time might be be delayed. One such system is the Linux kernel, where a call to <tt>&quot;gettimeofday&quot;</tt> might return a timestamp with a full second later than a subsequent <tt>&quot;time&quot;</tt> call &#8211; if the equivalent of <tt>&quot;time ()&quot;</tt> is used to update file times then there will be a small window where the kernel uses the previous second to update file times but libev might already execute the timer callback). </p>
<p> <i>Watcher-Specific Functions and Data Members</i></p>
<dl>
<dt>ev_stat_init (ev_stat *, callback, const char *path, ev_tstamp interval)</p>
<dd>
<dt>ev_stat_set (ev_stat *, const char *path, ev_tstamp interval)</p>
<dd> Configures the watcher to wait for status changes of the given <tt>&quot;path&quot;</tt>. The <tt>&quot;interval&quot;</tt> is a hint on how quickly a change is expected to be detected and should normally be specified as <tt>0</tt> to let libev choose a suitable value. The memory pointed to by <tt>&quot;path&quot;</tt> must point to the same path for as long as the watcher is active. </p>
<p> The callback will receive an <tt>&quot;EV_STAT&quot;</tt> event when a change was detected, relative to the attributes at the time the watcher was started (or the last change was detected).</p>
<dt>ev_stat_stat (loop, ev_stat *)</p>
<dd> Updates the stat buffer immediately with new values. If you change the watched path in your callback, you could call this function to avoid detecting this change (while introducing a race condition if you are not the only one changing the path). Can also be useful simply to find out the new values.</p>
<dt>ev_statdata attr [read-only]</p>
<dd> The most-recently detected attributes of the file. Although the type is <tt>&quot;ev_statdata&quot;</tt>, this is usually the (or one of the) <tt>&quot;struct stat&quot;</tt> types suitable for your system, but you can only rely on the POSIX-standardised members to be present. If the <tt>&quot;st_nlink&quot;</tt> member is <tt>0</tt>, then there was some error while <tt>&quot;stat&quot;</tt>ing the file.</p>
<dt>ev_statdata prev [read-only]</p>
<dd> The previous attributes of the file. The callback gets invoked whenever <tt>&quot;prev&quot;</tt> != <tt>&quot;attr&quot;</tt>, or, more precisely, one or more of these members differ: <tt>&quot;st_dev&quot;</tt>, <tt>&quot;st_ino&quot;</tt>, <tt>&quot;st_mode&quot;</tt>, <tt>&quot;st_nlink&quot;</tt>, <tt>&quot;st_uid&quot;</tt>, <tt>&quot;st_gid&quot;</tt>, <tt>&quot;st_rdev&quot;</tt>, <tt>&quot;st_size&quot;</tt>, <tt>&quot;st_atime&quot;</tt>, <tt>&quot;st_mtime&quot;</tt>, <tt>&quot;st_ctime&quot;</tt>.</p>
<dt>ev_tstamp interval [read-only]</p>
<dd> The specified interval.</p>
<dt>const char *path [read-only]</p>
<dd> The file system path that is being watched.</dl>
<p> <i>Examples</i> </p>
<p> Example: Watch <tt>&quot;/etc/passwd&quot;</tt> for attribute changes. </p>
<p>static void<br />
passwd_cb(struct ev_loop *loop, ev_stat *w, int revents)<br />
{<br />
    /* /etc/passwd changed in some way */<br />
    if (w-&gt;attr.st_nlink) {<br />
        printf(&#8220;passwd current size  %ld
&#8221;, (long)w-&gt;attr.st_size);<br />
        printf(&#8220;passwd current atime %ld
&#8221;, (long)w-&gt;attr.st_mtime);<br />
        printf(&#8220;passwd current mtime %ld
&#8221;, (long)w-&gt;attr.st_mtime);<br />
    } else<br />
        /* you shalt not abuse printf for puts */<br />
        puts(&#8220;wow, /etc/passwd is not there, expect problems. &#8221;<br />
             &#8220;if this is windows, they already arrived
&#8221;);<br />
}<br />
&#8230; ev_stat passwd;<br />
ev_stat_init(&amp;passwd, passwd_cb, &#8220;/etc/passwd&#8221;, 0.);<br />
ev_stat_start(loop, &amp;passwd);</p>
<p> Example: Like above, but additionally use a one-second delay so we do not miss updates (however, frequent updates will delay processing, too, so one might do the work both on <tt>&quot;ev_stat&quot;</tt> callback invocation <i>and</i> on <tt>&quot;ev_timer&quot;</tt> callback invocation). </p>
<p>static ev_stat passwd;<br />
static ev_timer timer;<br />
static void<br />
timer_cb(EV_P_ ev_timer *w, int revents)<br />
{<br />
    ev_timer_stop(EV_A_ w);<br />
    /* now it&#8217;s one second after the most recent passwd change */<br />
}<br />
static void<br />
stat_cb(EV_P_ ev_stat *w, int revents)<br />
{<br />
    /* reset the one-second timer */<br />
    ev_timer_again(EV_A_ &amp; timer);<br />
}<br />
&#8230; ev_stat_init(&amp;passwd, stat_cb, &#8220;/etc/passwd&#8221;, 0.);<br />
ev_stat_start(loop, &amp;passwd);<br />
ev_timer_init(&amp;timer, timer_cb, 0., 1.02);</p>
<h3>ev_idle &#8211; when you&#8217;ve got nothing better to do&#8230;</h3>
<p> Idle watchers trigger events when no other events of the same or higher priority are pending (prepare, check and other idle watchers do not count as receiving &#8220;events&#8221;). </p>
<p> That is, as long as your process is busy handling sockets or timeouts (or even signals, imagine) of the same or higher priority it will not be triggered. But when your process is idle (or only lower-priority watchers are pending), the idle watchers are being called once per event loop iteration &#8211; until stopped, that is, or your process receives more events and becomes busy again with higher priority stuff. </p>
<p> The most noteworthy effect is that as long as any idle watchers are active, the process will not block when waiting for new events. </p>
<p> Apart from keeping your process non-blocking (which is a useful effect on its own sometimes), idle watchers are a good place to do &#8220;pseudo-background processing&#8221;, or delay processing stuff to after the event loop has handled all outstanding events. </p>
<p> <i>Watcher-Specific Functions and Data Members</i></p>
<dl>
<dt>ev_idle_init (ev_idle *, callback)</p>
<dd> Initialises and configures the idle watcher &#8211; it has no parameters of any kind. There is a <tt>&quot;ev_idle_set&quot;</tt> macro, but using it is utterly pointless, believe me.</dl>
<p> <i>Examples</i> </p>
<p> Example: Dynamically allocate an <tt>&quot;ev_idle&quot;</tt> watcher, start it, and in the callback, free it. Also, use no error checking, as usual. </p>
<p>static void<br />
idle_cb(struct ev_loop *loop, ev_idle *w, int revents)<br />
{<br />
    free(w);<br />
    // now do something you wanted to do when the program has<br />
    // no longer anything immediate to do.<br />
}<br />
ev_idle *idle_watcher = malloc(sizeof(ev_idle));<br />
ev_idle_init(idle_watcher, idle_cb);<br />
ev_idle_start(loop, idle_watcher);</p>
<h3>ev_prepare and ev_check &#8211; customise your event loop!</h3>
<p> Prepare and check watchers are usually (but not always) used in pairs: prepare watchers get invoked before the process blocks and check watchers afterwards. </p>
<p> You <i>must not</i> call <tt>&quot;ev_loop&quot;</tt> or similar functions that enter the current event loop from either <tt>&quot;ev_prepare&quot;</tt> or <tt>&quot;ev_check&quot;</tt> watchers. Other loops than the current one are fine, however. The rationale behind this is that you do not need to check for recursion in those watchers, i.e. the sequence will always be <tt>&quot;ev_prepare&quot;</tt>, blocking, <tt>&quot;ev_check&quot;</tt> so if you have one watcher of each kind they will always be called in pairs bracketing the blocking call. </p>
<p> Their main purpose is to integrate other event mechanisms into libev and their use is somewhat advanced. They could be used, for example, to track variable changes, implement your own watchers, integrate net-snmp or a coroutine library and lots more. They are also occasionally useful if you cache some data and want to flush it before blocking (for example, in X programs you might want to do an <tt>&quot;XFlush ()&quot;</tt> in an <tt>&quot;ev_prepare&quot;</tt> watcher). </p>
<p> This is done by examining in each prepare call which file descriptors need to be watched by the other library, registering <tt>&quot;ev_io&quot;</tt> watchers for them and starting an <tt>&quot;ev_timer&quot;</tt> watcher for any timeouts (many libraries provide exactly this functionality). Then, in the check watcher, you check for any events that occurred (by checking the pending status of all watchers and stopping them) and call back into the library. The I/O and timer callbacks will never actually be called (but must be valid nevertheless, because you never know, you know?). </p>
<p> As another example, the Perl Coro module uses these hooks to integrate coroutines into libev programs, by yielding to other active coroutines during each prepare and only letting the process block if no coroutines are ready to run (it&#8217;s actually more complicated: it only runs coroutines with priority higher than or equal to the event loop and one coroutine of lower priority, but only once, using idle watchers to keep the event loop from blocking if lower-priority coroutines are active, thus mapping low-priority coroutines to idle/background tasks). </p>
<p> It is recommended to give <tt>&quot;ev_check&quot;</tt> watchers highest (<tt>&quot;EV_MAXPRI&quot;</tt>) priority, to ensure that they are being run before any other watchers after the poll (this doesn&#8217;t matter for <tt>&quot;ev_prepare&quot;</tt> watchers). </p>
<p> Also, <tt>&quot;ev_check&quot;</tt> watchers (and <tt>&quot;ev_prepare&quot;</tt> watchers, too) should not activate (&#8220;feed&#8221;) events into libev. While libev fully supports this, they might get executed before other <tt>&quot;ev_check&quot;</tt> watchers did their job. As <tt>&quot;ev_check&quot;</tt> watchers are often used to embed other (non-libev) event loops those other event loops might be in an unusable state until their <tt>&quot;ev_check&quot;</tt> watcher ran (always remind yourself to coexist peacefully with others). </p>
<p> <i>Watcher-Specific Functions and Data Members</i></p>
<dl>
<dt>ev_prepare_init (ev_prepare *, callback)</p>
<dd>
<dt>ev_check_init (ev_check *, callback)</p>
<dd> Initialises and configures the prepare or check watcher &#8211; they have no parameters of any kind. There are <tt>&quot;ev_prepare_set&quot;</tt> and <tt>&quot;ev_check_set&quot;</tt> macros, but using them is utterly, utterly, utterly and completely pointless.</dl>
<p> <i>Examples</i> </p>
<p> There are a number of principal ways to embed other event loops or modules into libev. Here are some ideas on how to include libadns into libev (there is a Perl module named <tt>&quot;EV::ADNS&quot;</tt> that does this, which you could use as a working example. Another Perl module named <tt>&quot;EV::Glib&quot;</tt> embeds a Glib main context into libev, and finally, <tt>&quot;Glib::EV&quot;</tt> embeds <font SIZE="-1">EV</font> into the Glib event loop). </p>
<p> Method 1: Add <font SIZE="-1">IO</font> watchers and a timeout watcher in a prepare handler, and in a check watcher, destroy them and call into libadns. What follows is pseudo-code only of course. This requires you to either use a low priority for the check watcher or use <tt>&quot;ev_clear_pending&quot;</tt> explicitly, as the callbacks for the IO/timeout watchers might not have been called yet. </p>
<p>static ev_io iow[nfd];<br />
static ev_timer tw;<br />
static void<br />
io_cb(struct ev_loop *loop, ev_io *w, int revents)<br />
{<br />
}<br />
// create io watchers for each fd and a timer before blocking<br />
static void<br />
adns_prepare_cb(struct ev_loop *loop, ev_prepare *w, int revents)<br />
{<br />
    int timeout = 3600000;<br />
    struct pollfd fds[nfd];<br />
    // actual code will need to loop here and realloc etc.<br />
    adns_beforepoll(ads, fds, &amp;nfd, &amp;timeout, timeval_from(ev_time()));<br />
    /* the callback is illegal, but won&#8217;t be called as we stop during check */<br />
    ev_timer_init(&amp;tw, 0, timeout * 1e-3, 0.);<br />
    ev_timer_start(loop, &amp;tw);<br />
    // create one ev_io per pollfd<br />
    for (int i = 0; i &lt; nfd; ++i) {<br />
        ev_io_init(iow + i, io_cb, fds[i].fd,<br />
                   ((fds[i].events &amp; POLLIN ? EV_READ : 0) | (fds[i].events &amp; POLLOUT ? EV_WRITE : 0)));<br />
        fds[i].revents = 0;<br />
        ev_io_start(loop, iow + i);<br />
    }<br />
}<br />
// stop all watchers after blocking<br />
static void<br />
adns_check_cb(struct ev_loop *loop, ev_check *w, int revents)<br />
{<br />
    ev_timer_stop(loop, &amp;tw);<br />
    for (int i = 0; i &lt; nfd; ++i) {<br />
        // set the relevant poll flags<br />
        // could also call adns_processreadable etc. here<br />
        struct pollfd *fd = fds + i;<br />
        int revents = ev_clear_pending(iow + i);<br />
        if (revents &amp; EV_READ)<br />
            fd-&gt;revents |= fd-&gt;events &amp; POLLIN;<br />
        if (revents &amp; EV_WRITE)<br />
            fd-&gt;revents |= fd-&gt;events &amp; POLLOUT;<br />
        // now stop the watcher<br />
        ev_io_stop(loop, iow + i);<br />
    }<br />
     adns_afterpoll (adns, fds, nfd, timeval_from (ev_now (loop));<br />
}</p>
<p> Method 2: This would be just like method 1, but you run <tt>&quot;adns_afterpoll&quot;</tt> in the prepare watcher and would dispose of the check watcher. </p>
<p> Method 3: If the module to be embedded supports explicit event notification (libadns does), you can also make use of the actual watcher callbacks, and only destroy/create the watchers in the prepare watcher. </p>
<p>static void<br />
timer_cb(EV_P_ ev_timer *w, int revents)<br />
{<br />
    adns_state ads = (adns_state)w-&gt;data;<br />
    update_now(EV_A);<br />
    adns_processtimeouts(ads, &amp;tv_now);<br />
}<br />
static void<br />
io_cb(EV_P_ ev_io *w, int revents)<br />
{<br />
    adns_state ads = (adns_state)w-&gt;data;<br />
    update_now(EV_A);<br />
    if (revents &amp; EV_READ)<br />
        adns_processreadable(ads, w-&gt;fd, &amp;tv_now);<br />
    if (revents &amp; EV_WRITE)<br />
        adns_processwriteable(ads, w-&gt;fd, &amp;tv_now);<br />
}<br />
// do not ever call adns_afterpoll</p>
<p> Method 4: Do not use a prepare or check watcher because the module you want to embed is not flexible enough to support it. Instead, you can override their poll function. The drawback with this solution is that the main loop is now no longer controllable by <font SIZE="-1">EV</font>. The <tt>&quot;Glib::EV&quot;</tt> module uses this approach, effectively embedding <font SIZE="-1">EV</font> as a client into the horrible libglib event loop. </p>
<p>static gint<br />
event_poll_func(GPollFD *fds, guint nfds, gint timeout)<br />
{<br />
    int got_events = 0;<br />
    for (n = 0; n &lt; nfds; ++n)<br />
        // create/start io watcher that sets the relevant bits in fds[n] and increment got_events<br />
        if (timeout &gt;= 0)<br />
            // create/start timer<br />
            // poll<br />
            ev_loop(EV_A_ 0);<br />
    // stop timer again<br />
    if (timeout &gt;= 0)<br />
        ev_timer_stop(EV_A_ &amp; to);<br />
    // stop io watchers again &#8211; their callbacks should have set<br />
    for (n = 0; n &lt; nfds; ++n)<br />
        ev_io_stop(EV_A_ iow[n]);<br />
    return got_events;<br />
}</p>
<h3>ev_embed &#8211; when one backend isn&#8217;t enough&#8230;</h3>
<p> This is a rather advanced watcher type that lets you embed one event loop into another (currently only <tt>&quot;ev_io&quot;</tt> events are supported in the embedded loop, other types of watchers might be handled in a delayed or incorrect fashion and must not be used). </p>
<p> There are primarily two reasons you would want that: work around bugs and prioritise I/O. </p>
<p> As an example for a bug workaround, the kqueue backend might only support sockets on some platform, so it is unusable as generic backend, but you still want to make use of it because you have many sockets and it scales so nicely. In this case, you would create a kqueue-based loop and embed it into your default loop (which might use e.g. poll). Overall operation will be a bit slower because first libev has to call <tt>&quot;poll&quot;</tt> and then <tt>&quot;kevent&quot;</tt>, but at least you can use both mechanisms for what they are best: <tt>&quot;kqueue&quot;</tt> for scalable sockets and <tt>&quot;poll&quot;</tt> if you want it to work :) </p>
<p> As for prioritising I/O: under rare circumstances you have the case where some fds have to be watched and handled very quickly (with low latency), and even priorities and idle watchers might have too much overhead. In this case you would put all the high priority stuff in one loop and all the rest in a second one, and embed the second one in the first. </p>
<p> As long as the watcher is active, the callback will be invoked every time there might be events pending in the embedded loop. The callback must then call <tt>&quot;ev_embed_sweep (mainloop, watcher)&quot;</tt> to make a single sweep and invoke their callbacks (the callback doesn&#8217;t need to invoke the <tt>&quot;ev_embed_sweep&quot;</tt> function directly, it could also start an idle watcher to give the embedded loop strictly lower priority for example). </p>
<p> You can also set the callback to <tt>0</tt>, in which case the embed watcher will automatically execute the embedded loop sweep whenever necessary. </p>
<p> Fork detection will be handled transparently while the <tt>&quot;ev_embed&quot;</tt> watcher is active, i.e., the embedded loop will automatically be forked when the embedding loop forks. In other cases, the user is responsible for calling <tt>&quot;ev_loop_fork&quot;</tt> on the embedded loop. </p>
<p> Unfortunately, not all backends are embeddable: only the ones returned by <tt>&quot;ev_embeddable_backends&quot;</tt> are, which, unfortunately, does not include any portable one. </p>
<p> So when you want to use this feature you will always have to be prepared that you cannot get an embeddable loop. The recommended way to get around this is to have a separate variables for your embeddable loop, try to create it, and if that fails, use the normal loop for everything. </p>
<p> <i></i>&quot;ev_embed&quot;<i> and fork</i> </p>
<p> While the <tt>&quot;ev_embed&quot;</tt> watcher is running, forks in the embedding loop will automatically be applied to the embedded loop as well, so no special fork handling is required in that case. When the watcher is not running, however, it is still the task of the libev user to call <tt>&quot;ev_loop_fork ()&quot;</tt> as applicable. </p>
<p> <i>Watcher-Specific Functions and Data Members</i></p>
<dl>
<dt>ev_embed_init (ev_embed *, callback, struct ev_loop *embedded_loop)</p>
<dd>
<dt>ev_embed_set (ev_embed *, callback, struct ev_loop *embedded_loop)</p>
<dd> Configures the watcher to embed the given loop, which must be embeddable. If the callback is <tt>0</tt>, then <tt>&quot;ev_embed_sweep&quot;</tt> will be invoked automatically, otherwise it is the responsibility of the callback to invoke it (it will continue to be called until the sweep has been done, if you do not want that, you need to temporarily stop the embed watcher).</p>
<dt>ev_embed_sweep (loop, ev_embed *)</p>
<dd> Make a single, non-blocking sweep over the embedded loop. This works similarly to <tt>&quot;ev_loop (embedded_loop, EVLOOP_NONBLOCK)&quot;</tt>, but in the most appropriate way for embedded loops.</p>
<dt>struct ev_loop *other [read-only]</p>
<dd> The embedded event loop.</dl>
<p> <i>Examples</i> </p>
<p> Example: Try to get an embeddable event loop and embed it into the default event loop. If that is not possible, use the default loop. The default loop is stored in <tt>&quot;loop_hi&quot;</tt>, while the embeddable loop is stored in <tt>&quot;loop_lo&quot;</tt> (which is <tt>&quot;loop_hi&quot;</tt> in the case no embeddable loop can be used). </p>
<p>struct ev_loop *loop_hi = ev_default_init(0);<br />
struct ev_loop *loop_lo = 0;<br />
ev_embed embed;</p>
<p>// see if there is a chance of getting one that works<br />
// (remember that a flags value of 0 means autodetection)<br />
loop_lo = ev_embeddable_backends() &amp; ev_recommended_backends()<br />
              ? ev_loop_new(ev_embeddable_backends() &amp; ev_recommended_backends())<br />
              : 0;<br />
// if we got one, then embed it, otherwise default to loop_hi<br />
if (loop_lo) {<br />
    ev_embed_init(&amp;embed, 0, loop_lo);<br />
    ev_embed_start(loop_hi, &amp;embed);<br />
} else<br />
    loop_lo = loop_hi;</p>
<p> Example: Check if kqueue is available but not recommended and create a kqueue backend for use with sockets (which usually work with any kqueue implementation). Store the kqueue/socket-only event loop in <tt>&quot;loop_socket&quot;</tt>. (One might optionally use <tt>&quot;EVFLAG_NOENV&quot;</tt>, too). </p>
<p>struct ev_loop *loop = ev_default_init(0);<br />
struct ev_loop *loop_socket = 0;<br />
ev_embed embed;</p>
<p>if (ev_supported_backends() &amp; ~ev_recommended_backends() &amp; EVBACKEND_KQUEUE)<br />
     if ((loop_socket = ev_loop_new (EVBACKEND_KQUEUE))<br />
       {<br />
        ev_embed_init(&amp;embed, 0, loop_socket);<br />
        ev_embed_start(loop, &amp;embed);<br />
       }<br />
   if (!loop_socket)<br />
     loop_socket = loop;<br />
// now use loop_socket for all sockets, and loop for everything else</p>
<h3>ev_fork &#8211; the audacity to resume the event loop after a fork</h3>
<p> Fork watchers are called when a <tt>&quot;fork ()&quot;</tt> was detected (usually because whoever is a good citizen cared to tell libev about it by calling <tt>&quot;ev_default_fork&quot;</tt> or <tt>&quot;ev_loop_fork&quot;</tt>). The invocation is done before the event loop blocks next and before <tt>&quot;ev_check&quot;</tt> watchers are being called, and only in the child after the fork. If whoever good citizen calling <tt>&quot;ev_default_fork&quot;</tt> cheats and calls it in the wrong process, the fork handlers will be invoked, too, of course. </p>
<p> <i>The special problem of life after fork &#8211; how is it possible?</i> </p>
<p> Most uses of <tt>&quot;fork()&quot;</tt> consist of forking, then some simple calls to ste up/change the process environment, followed by a call to <tt>&quot;exec()&quot;</tt>. This sequence should be handled by libev without any problems. </p>
<p> This changes when the application actually wants to do event handling in the child, or both parent in child, in effect &#8220;continuing&#8221; after the fork. </p>
<p> The default mode of operation (for libev, with application help to detect forks) is to duplicate all the state in the child, as would be expected when <i>either</i> the parent <i>or</i> the child process continues. </p>
<p> When both processes want to continue using libev, then this is usually the wrong result. In that case, usually one process (typically the parent) is supposed to continue with all watchers in place as before, while the other process typically wants to start fresh, i.e. without any active watchers. </p>
<p> The cleanest and most efficient way to achieve that with libev is to simply create a new event loop, which of course will be &#8220;empty&#8221;, and use that for new watchers. This has the advantage of not touching more memory than necessary, and thus avoiding the copy-on-write, and the disadvantage of having to use multiple event loops (which do not support signal watchers). </p>
<p> When this is not possible, or you want to use the default loop for other reasons, then in the process that wants to start &#8220;fresh&#8221;, call <tt>&quot;ev_default_destroy ()&quot;</tt> followed by <tt>&quot;ev_default_loop (...)&quot;</tt>. Destroying the default loop will &#8220;orphan&#8221; (not stop) all registered watchers, so you have to be careful not to execute code that modifies those watchers. Note also that in that case, you have to re-register any signal watchers. </p>
<p> <i>Watcher-Specific Functions and Data Members</i></p>
<dl>
<dt>ev_fork_init (ev_signal *, callback)</p>
<dd> Initialises and configures the fork watcher &#8211; it has no parameters of any kind. There is a <tt>&quot;ev_fork_set&quot;</tt> macro, but using it is utterly pointless, believe me.</dl>
<h3>ev_async &#8211; how to wake up another event loop</h3>
<p> In general, you cannot use an <tt>&quot;ev_loop&quot;</tt> from multiple threads or other asynchronous sources such as signal handlers (as opposed to multiple event loops &#8211; those are of course safe to use in different threads). </p>
<p> Sometimes, however, you need to wake up another event loop you do not control, for example because it belongs to another thread. This is what <tt>&quot;ev_async&quot;</tt> watchers do: as long as the <tt>&quot;ev_async&quot;</tt> watcher is active, you can signal it by calling <tt>&quot;ev_async_send&quot;</tt>, which is thread- and signal safe. </p>
<p> This functionality is very similar to <tt>&quot;ev_signal&quot;</tt> watchers, as signals, too, are asynchronous in nature, and signals, too, will be compressed (i.e. the number of callback invocations may be less than the number of <tt>&quot;ev_async_sent&quot;</tt> calls). </p>
<p> Unlike <tt>&quot;ev_signal&quot;</tt> watchers, <tt>&quot;ev_async&quot;</tt> works with any event loop, not just the default loop. </p>
<p> <i>Queueing</i> </p>
<p> <tt>&quot;ev_async&quot;</tt> does not support queueing of data in any way. The reason is that the author does not know of a simple (or any) algorithm for a multiple-writer-single-reader queue that works in all cases and doesn&#8217;t need elaborate support such as pthreads. </p>
<p> That means that if you want to queue data, you have to provide your own queue. But at least I can tell you how to implement locking around your queue:</p>
<dl>
<dt>queueing from a signal handler context</p>
<dd> To implement race-free queueing, you simply add to the queue in the signal handler but you block the signal handler in the watcher callback. Here is an example that does that for some fictitious <font SIZE="-1">SIGUSR1</font> handler: </p>
<p>static ev_async mysig;<br />
static void<br />
sigusr1_handler(void)<br />
{<br />
    sometype data;<br />
    // no locking etc.<br />
    queue_put(data);<br />
    ev_async_send(EV_DEFAULT_ &amp; mysig);<br />
}<br />
static void<br />
mysig_cb(EV_P_ ev_async *w, int revents)<br />
{<br />
    sometype data;<br />
    sigset_t block, prev;<br />
    sigemptyset(&amp;block);<br />
    sigaddset(&amp;block, SIGUSR1);<br />
    sigprocmask(SIG_BLOCK, &amp;block, &amp;prev);<br />
    while (queue_get(&amp;data))<br />
        process(data);<br />
     if (sigismember (&amp;prev, SIGUSR1)<br />
       sigprocmask (SIG_UNBLOCK, &amp;block, 0);<br />
}</p>
<p> (Note: pthreads in theory requires you to use <tt>&quot;pthread_setmask&quot;</tt> instead of <tt>&quot;sigprocmask&quot;</tt> when you use threads, but libev doesn&#8217;t do it either&#8230;).</p>
<dt>queueing from a thread context</p>
<dd> The strategy for threads is different, as you cannot (easily) block threads but you can easily preempt them, so to queue safely you need to employ a traditional mutex lock, such as in this pthread example: </p>
<p>static ev_async mysig;<br />
static pthread_mutex_t mymutex = PTHREAD_MUTEX_INITIALIZER;<br />
static void<br />
otherthread(void)<br />
{<br />
    // only need to lock the actual queueing operation<br />
    pthread_mutex_lock(&amp;mymutex);<br />
    queue_put(data);<br />
    pthread_mutex_unlock(&amp;mymutex);<br />
    ev_async_send(EV_DEFAULT_ &amp; mysig);<br />
}<br />
static void<br />
mysig_cb(EV_P_ ev_async *w, int revents)<br />
{<br />
    pthread_mutex_lock(&amp;mymutex);<br />
    while (queue_get(&amp;data))<br />
        process(data);<br />
    pthread_mutex_unlock(&amp;mymutex);<br />
}
</dl>
<p> <i>Watcher-Specific Functions and Data Members</i></p>
<dl>
<dt>ev_async_init (ev_async *, callback)</p>
<dd> Initialises and configures the async watcher &#8211; it has no parameters of any kind. There is a <tt>&quot;ev_async_set&quot;</tt> macro, but using it is utterly pointless, trust me.</p>
<dt>ev_async_send (loop, ev_async *)</p>
<dd> Sends/signals/activates the given <tt>&quot;ev_async&quot;</tt> watcher, that is, feeds an <tt>&quot;EV_ASYNC&quot;</tt> event on the watcher into the event loop. Unlike <tt>&quot;ev_feed_event&quot;</tt>, this call is safe to do from other threads, signal or similar contexts (see the discussion of <tt>&quot;EV_ATOMIC_T&quot;</tt> in the embedding section below on what exactly this means). </p>
<p> Note that, as with other watchers in libev, multiple events might get compressed into a single callback invocation (another way to look at this is that <tt>&quot;ev_async&quot;</tt> watchers are level-triggered, set on <tt>&quot;ev_async_send&quot;</tt>, reset when the event loop detects that). </p>
<p> This call incurs the overhead of a system call only once per event loop iteration, so while the overhead might be noticeable, it doesn&#8217;t apply to repeated calls to <tt>&quot;ev_async_send&quot;</tt> for the same event loop.</p>
<dt>bool = ev_async_pending (ev_async *)</p>
<dd> Returns a non-zero value when <tt>&quot;ev_async_send&quot;</tt> has been called on the watcher but the event has not yet been processed (or even noted) by the event loop. </p>
<p> <tt>&quot;ev_async_send&quot;</tt> sets a flag in the watcher and wakes up the loop. When the loop iterates next and checks for the watcher to have become active, it will reset the flag again. <tt>&quot;ev_async_pending&quot;</tt> can be used to very quickly check whether invoking the loop might be a good idea. </p>
<p> Not that this does <i>not</i> check whether the watcher itself is pending, only whether it has been requested to make this watcher pending: there is a time window between the event loop checking and resetting the async notification, and the callback being invoked.</dl>
<h2>OTHER FUNCTIONS</h2>
<p> There are some other functions of possible interest. Described. Here. Now.</p>
<dl>
<dt>ev_once (loop, int fd, int events, ev_tstamp timeout, callback)</p>
<dd> This function combines a simple timer and an I/O watcher, calls your callback on whichever event happens first and automatically stops both watchers. This is useful if you want to wait for a single event on an fd or timeout without having to allocate/configure/start/stop/free one or more watchers yourself. </p>
<p> If <tt>&quot;fd&quot;</tt> is less than 0, then no I/O watcher will be started and the <tt>&quot;events&quot;</tt> argument is being ignored. Otherwise, an <tt>&quot;ev_io&quot;</tt> watcher for the given <tt>&quot;fd&quot;</tt> and <tt>&quot;events&quot;</tt> set will be created and started. </p>
<p> If <tt>&quot;timeout&quot;</tt> is less than 0, then no timeout watcher will be started. Otherwise an <tt>&quot;ev_timer&quot;</tt> watcher with after = <tt>&quot;timeout&quot;</tt> (and repeat = 0) will be started. <tt>0</tt> is a valid timeout. </p>
<p> The callback has the type <tt>&quot;void (*cb)(int revents, void *arg)&quot;</tt> and gets passed an <tt>&quot;revents&quot;</tt> set like normal event callbacks (a combination of <tt>&quot;EV_ERROR&quot;</tt>, <tt>&quot;EV_READ&quot;</tt>, <tt>&quot;EV_WRITE&quot;</tt> or <tt>&quot;EV_TIMEOUT&quot;</tt>) and the <tt>&quot;arg&quot;</tt> value passed to <tt>&quot;ev_once&quot;</tt>. Note that it is possible to receive <i>both</i> a timeout and an io event at the same time &#8211; you probably should give io events precedence. </p>
<p> Example: wait up to ten seconds for data to appear on <font SIZE="-1">STDIN_FILENO</font>. </p>
<p>static void stdin_ready(int revents, void *arg)<br />
{<br />
    if (revents &amp; EV_READ)<br />
        /* stdin might have data for us, joy! */;<br />
    else if (revents &amp; EV_TIMEOUT)<br />
        /* doh, nothing entered */;<br />
}<br />
ev_once(STDIN_FILENO, EV_READ, 10., stdin_ready, 0);</p>
<dt>ev_feed_event (struct ev_loop *, watcher *, int revents)</p>
<dd> Feeds the given event set into the event loop, as if the specified event had happened for the specified watcher (which must be a pointer to an initialised but not necessarily started event watcher).</p>
<dt>ev_feed_fd_event (struct ev_loop *, int fd, int revents)</p>
<dd> Feed an event on the given fd, as if a file descriptor backend detected the given events it.</p>
<dt>ev_feed_signal_event (struct ev_loop *loop, int signum)</p>
<dd> Feed an event as if the given signal occurred (<tt>&quot;loop&quot;</tt> must be the default loop!).</dl>
<h2>LIBEVENT EMULATION</h2>
<p> Libev offers a compatibility emulation layer for libevent. It cannot emulate the internals of libevent, so here are some usage hints:</p>
<dl>
<dt>*</p>
<dd> Use it by including &lt;<a href="file:/usr/include/event.h">event.h</a>&gt;, as usual.</p>
<dt>*</p>
<dd> The following members are fully supported: ev_base, ev_callback, ev_arg, ev_fd, ev_res, ev_events.</p>
<dt>*</p>
<dd> Avoid using ev_flags and the EVLIST_*-macros, while it is maintained by libev, it does not work exactly the same way as in libevent (consider it a private <font SIZE="-1">API</font>).</p>
<dt>*</p>
<dd> Priorities are not currently supported. Initialising priorities will fail and all watchers will have the same priority, even though there is an ev_pri field.</p>
<dt>*</p>
<dd> In libevent, the last base created gets the signals, in libev, the first base created (== the default loop) gets the signals.</p>
<dt>*</p>
<dd> Other members are not supported.</p>
<dt>*</p>
<dd> The libev emulation is <i>not</i> <font SIZE="-1">ABI</font> compatible to libevent, you need to use the libev header file and library.</dl>
<h2>C<font SIZE="-2">++</font> SUPPORT</h2>
<p> Libev comes with some simplistic wrapper classes for C<font SIZE="-2">++</font> that mainly allow you to use some convenience methods to start/stop watchers and also change the callback model to a model using method callbacks on objects. </p>
<p> To use it, </p>
<p>#include &lt;ev++.h&gt;</p>
<p> This automatically includes <i>ev.h</i> and puts all of its definitions (many of them macros) into the global namespace. All C<font SIZE="-2">++</font> specific things are put into the <tt>&quot;ev&quot;</tt> namespace. It should support all the same embedding options as <i>ev.h</i>, most notably <tt>&quot;EV_MULTIPLICITY&quot;</tt>. </p>
<p> Care has been taken to keep the overhead low. The only data member the C<font SIZE="-2">++</font> classes add (compared to plain C-style watchers) is the event loop pointer that the watcher is associated with (or no additional members at all if you disable <tt>&quot;EV_MULTIPLICITY&quot;</tt> when embedding libev). </p>
<p> Currently, functions, and static and non-static member functions can be used as callbacks. Other types should be easy to add as long as they only need one additional pointer for context. If you need support for other types of functors please contact the author (preferably after implementing it). </p>
<p> Here is a list of things available in the <tt>&quot;ev&quot;</tt> namespace:</p>
<dl>
<dt>ev::READ, ev::WRITE etc.</p>
<dd> These are just enum values with the same values as the <tt>&quot;EV_READ&quot;</tt> etc. macros from <i>ev.h</i>.</p>
<dt>ev::tstamp, ev::now</p>
<dd> Aliases to the same types/functions as with the <tt>&quot;ev_&quot;</tt> prefix.</p>
<dt>ev::io, ev::timer, ev::periodic, ev::idle, ev::sig etc.</p>
<dd> For each <tt>&quot;ev_TYPE&quot;</tt> watcher in <i>ev.h</i> there is a corresponding class of the same name in the <tt>&quot;ev&quot;</tt> namespace, with the exception of <tt>&quot;ev_signal&quot;</tt> which is called <tt>&quot;ev::sig&quot;</tt> to avoid clashes with the <tt>&quot;signal&quot;</tt> macro defines by many implementations. </p>
<p> All of those classes have these methods:</p>
<dl>
<dt>
<dd>
<dl>
<dt>ev::TYPE::TYPE ()</p>
<dd>
<dt>ev::TYPE::TYPE (struct ev_loop *)</p>
<dd>
<dt>ev::TYPE::~TYPE</p>
<dd> The constructor (optionally) takes an event loop to associate the watcher with. If it is omitted, it will use <tt>&quot;EV_DEFAULT&quot;</tt>. </p>
<p> The constructor calls <tt>&quot;ev_init&quot;</tt> for you, which means you have to call the <tt>&quot;set&quot;</tt> method before starting it. </p>
<p> It will not set a callback, however: You have to call the templated <tt>&quot;set&quot;</tt> method to set a callback before you can start the watcher. </p>
<p> (The reason why you have to use a method is a limitation in C<font SIZE="-2">++</font> which does not allow explicit template arguments for constructors). </p>
<p> The destructor automatically stops the watcher if it is active.</p>
<dt>w-&gt;set&lt;class, &amp;class::method&gt; (object *)</p>
<dd> This method sets the callback method to call. The method has to have a signature of <tt>&quot;void (*)(ev_TYPE &amp;, int)&quot;</tt>, it receives the watcher as first argument and the <tt>&quot;revents&quot;</tt> as second. The object must be given as parameter and is stored in the <tt>&quot;data&quot;</tt> member of the watcher. </p>
<p> This method synthesizes efficient thunking code to call your method from the C callback that libev requires. If your compiler can inline your callback (i.e. it is visible to it at the place of the <tt>&quot;set&quot;</tt> call and your compiler is good :), then the method will be fully inlined into the thunking function, making it as fast as a direct C callback. </p>
<p> Example: simple class declaration and watcher initialisation </p>
<p>struct myclass {<br />
    void io_cb(ev::io &amp;w, int revents)<br />
    {<br />
    }<br />
} myclass obj;<br />
ev::io iow;<br />
iow.set&lt;myclass, &amp;myclass::io_cb&gt;(&amp;obj);</p>
<dt>w-&gt;set (object *)</p>
<dd> This is an <code>experimental</code> feature that might go away in a future version. </p>
<p> This is a variation of a method callback &#8211; leaving out the method to call will default the method to <tt>&quot;operator ()&quot;</tt>, which makes it possible to use functor objects without having to manually specify the <tt>&quot;operator ()&quot;</tt> all the time. Incidentally, you can then also leave out the template argument list. </p>
<p> The <tt>&quot;operator ()&quot;</tt> method prototype must be <tt>&quot;void operator ()(watcher &amp;w, int revents)&quot;</tt>. </p>
<p> See the method-<tt>&quot;set&quot;</tt> above for more details. </p>
<p> Example: use a functor object as callback. </p>
<p>struct myfunctor {<br />
    void operator()(ev::io &amp;w, int revents)<br />
    {<br />
        &#8230;<br />
    }<br />
}</p>
<p>myfunctor f;<br />
ev::io w;<br />
w.set(&amp;f);</p>
<dt>w-&gt;set&lt;function&gt; (void *data = 0)</p>
<dd> Also sets a callback, but uses a static method or plain function as callback. The optional <tt>&quot;data&quot;</tt> argument will be stored in the watcher&#8217;s <tt>&quot;data&quot;</tt> member and is free for you to use. </p>
<p> The prototype of the <tt>&quot;function&quot;</tt> must be <tt>&quot;void (*)(ev::TYPE &amp;w, int)&quot;</tt>. </p>
<p> See the method-<tt>&quot;set&quot;</tt> above for more details. </p>
<p> Example: Use a plain function as callback. </p>
<p>static void io_cb(ev::io &amp;w, int revents)<br />
{<br />
}<br />
iow.set&lt;io_cb&gt;();</p>
<dt>w-&gt;set (struct ev_loop *)</p>
<dd> Associates a different <tt>&quot;struct ev_loop&quot;</tt> with this watcher. You can only do this when the watcher is inactive (and not pending either).</p>
<dt>w-&gt;set ([arguments])</p>
<dd> Basically the same as <tt>&quot;ev_TYPE_set&quot;</tt>, with the same arguments. Must be called at least once. Unlike the C counterpart, an active watcher gets automatically stopped and restarted when reconfiguring it with this method.</p>
<dt>w-&gt;start ()</p>
<dd> Starts the watcher. Note that there is no <tt>&quot;loop&quot;</tt> argument, as the constructor already stores the event loop.</p>
<dt>w-&gt;stop ()</p>
<dd> Stops the watcher if it is active. Again, no <tt>&quot;loop&quot;</tt> argument.</p>
<dt>w-&gt;again () (ev::timer, ev::periodic only)</p>
<dd> For <tt>&quot;ev::timer&quot;</tt> and <tt>&quot;ev::periodic&quot;</tt>, this invokes the corresponding <tt>&quot;ev_TYPE_again&quot;</tt> function.</p>
<dt>w-&gt;sweep () (ev::embed only)</p>
<dd> Invokes <tt>&quot;ev_embed_sweep&quot;</tt>.</p>
<dt>w-&gt;update () (ev::stat only)</p>
<dd> Invokes <tt>&quot;ev_stat_stat&quot;</tt>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Example: Define a class with an <font SIZE="-1">IO</font> and idle watcher, start one of them in the constructor. </p>
<p>class myclass<br />
{<br />
    ev::io io;<br />
    void io_cb(ev::io &amp;w, int revents);<br />
    ev::idle idle;<br />
    void idle_cb(ev::idle &amp;w, int revents);<br />
    myclass(int fd)<br />
    {<br />
        io.set&lt;myclass, &amp;myclass::io_cb&gt;(this);<br />
        idle.set&lt;myclass, &amp;myclass::idle_cb&gt;(this);<br />
        io.start(fd, ev::READ);<br />
    }<br />
};</p>
<h2>OTHER LANGUAGE BINDINGS</h2>
<p> Libev does not offer other language bindings itself, but bindings for a number of languages exist in the form of third-party packages. If you know any interesting language binding in addition to the ones listed here, drop me a note.</p>
<dl>
<dt>Perl</p>
<dd> The <font SIZE="-1">EV</font> module implements the full libev <font SIZE="-1">API</font> and is actually used to test libev. <font SIZE="-1">EV</font> is developed together with libev. Apart from the <font SIZE="-1">EV</font> core module, there are additional modules that implement libev-compatible interfaces to <tt>&quot;libadns&quot;</tt> (<tt>&quot;EV::ADNS&quot;</tt>, but <tt>&quot;AnyEvent::DNS&quot;</tt> is preferred nowadays), <tt>&quot;Net::SNMP&quot;</tt> (<tt>&quot;Net::SNMP::EV&quot;</tt>) and the <tt>&quot;libglib&quot;</tt> event core (<tt>&quot;Glib::EV&quot;</tt> and <tt>&quot;EV::Glib&quot;</tt>). </p>
<p> It can be found and installed via <font SIZE="-1">CPAN</font>, its homepage is at &lt;<a rel="nofollow" href="http://software.schmorp.de/pkg/EV">http://software.schmorp.de/pkg/EV</a>&gt;.</p>
<dt>Python</p>
<dd> Python bindings can be found at &lt;<a rel="nofollow" href="http://code.google.com/p/pyev/">http://code.google.com/p/pyev/</a>&gt;. It seems to be quite complete and well-documented.</p>
<dt>Ruby</p>
<dd> Tony Arcieri has written a ruby extension that offers access to a subset of the libev <font SIZE="-1">API</font> and adds file handle abstractions, asynchronous <font SIZE="-1">DNS</font> and more on top of it. It can be found via gem servers. Its homepage is at &lt;<a rel="nofollow" href="http://rev.rubyforge.org/">http://rev.rubyforge.org/</a>&gt;. </p>
<p> Roger Pack reports that using the link order <tt>&quot;-lws2_32 -lmsvcrt-ruby-190&quot;</tt> makes rev work even on mingw.</p>
<dt>Haskell</p>
<dd> A haskell binding to libev is available at &lt;<a rel="nofollow" href="http://hackage.haskell.org/cgi-bin/hackage-scripts/package/hlibev">http://hackage.haskell.org/cgi-bin/hackage-scripts/package/hlibev</a>&gt;.</p>
<dt>D</p>
<dd> Leandro Lucarella has written a D language binding (<i>ev.d</i>) for libev, to be found at &lt;<a rel="nofollow" href="http://proj.llucax.com.ar/wiki/evd">http://proj.llucax.com.ar/wiki/evd</a>&gt;.</p>
<dt>Ocaml</p>
<dd> Erkki Seppala has written Ocaml bindings for libev, to be found at &lt;<a rel="nofollow" href="http://modeemi.cs.tut.fi/~flux/software/ocaml-ev/">http://modeemi.cs.tut.fi/~flux/software/ocaml-ev/</a>&gt;.</p>
<dt>Lua</p>
<dd> Brian Maher has written a partial interface to libev for lua (only <tt>&quot;ev_io&quot;</tt> and <tt>&quot;ev_timer&quot;</tt>), to be found at &lt;<a rel="nofollow" href="http://github.com/brimworks/lua-ev">http://github.com/brimworks/lua-ev</a>&gt;.</dl>
<h2>MACRO MAGIC</h2>
<p> Libev can be compiled with a variety of options, the most fundamental of which is <tt>&quot;EV_MULTIPLICITY&quot;</tt>. This option determines whether (most) functions and callbacks have an initial <tt>&quot;struct ev_loop *&quot;</tt> argument. </p>
<p> To make it easier to write programs that cope with either variant, the following macros are defined:</p>
<dl>
<dt>EV_A, EV_A_</p>
<dd> This provides the loop <i>argument</i> for functions, if one is required (&#8220;ev loop argument&#8221;). The <tt>&quot;EV_A&quot;</tt> form is used when this is the sole argument, <tt>&quot;EV_A_&quot;</tt> is used when other arguments are following. Example: </p>
<p>ev_unref(EV_A);<br />
ev_timer_add(EV_A_ watcher);<br />
ev_loop(EV_A_ 0);</p>
<p> It assumes the variable <tt>&quot;loop&quot;</tt> of type <tt>&quot;struct ev_loop *&quot;</tt> is in scope, which is often provided by the following macro.</p>
<dt>EV_P, EV_P_</p>
<dd> This provides the loop <i>parameter</i> for functions, if one is required (&#8220;ev loop parameter&#8221;). The <tt>&quot;EV_P&quot;</tt> form is used when this is the sole parameter, <tt>&quot;EV_P_&quot;</tt> is used when other parameters are following. Example: </p>
<p>// this is how ev_unref is being declared<br />
static void ev_unref(EV_P);<br />
// this is how you can declare your typical callback<br />
static void cb(EV_P_ ev_timer *w, int revents)</p>
<p> It declares a parameter <tt>&quot;loop&quot;</tt> of type <tt>&quot;struct ev_loop *&quot;</tt>, quite suitable for use with <tt>&quot;EV_A&quot;</tt>.</p>
<dt>EV_DEFAULT, EV_DEFAULT_</p>
<dd> Similar to the other two macros, this gives you the value of the default loop, if multiple loops are supported (&#8220;ev loop default&#8221;).</p>
<dt>EV_DEFAULT_UC, EV_DEFAULT_UC_</p>
<dd> Usage identical to <tt>&quot;EV_DEFAULT&quot;</tt> and <tt>&quot;EV_DEFAULT_&quot;</tt>, but requires that the default loop has been initialised (<tt>&quot;UC&quot;</tt> == unchecked). Their behaviour is undefined when the default loop has not been initialised by a previous execution of <tt>&quot;EV_DEFAULT&quot;</tt>, <tt>&quot;EV_DEFAULT_&quot;</tt> or <tt>&quot;ev_default_init (...)&quot;</tt>. </p>
<p> It is often prudent to use <tt>&quot;EV_DEFAULT&quot;</tt> when initialising the first watcher in a function but use <tt>&quot;EV_DEFAULT_UC&quot;</tt> afterwards.</dl>
<p> Example: Declare and initialise a check watcher, utilising the above macros so it will work regardless of whether multiple loops are supported or not. </p>
<p>static void<br />
check_cb(EV_P_ ev_timer *w, int revents)<br />
{<br />
    ev_check_stop(EV_A_ w);<br />
}<br />
ev_check check;<br />
ev_check_init(&amp;check, check_cb);<br />
ev_check_start(EV_DEFAULT_ &amp;check);<br />
ev_loop(EV_DEFAULT_ 0);</p>
<h2>EMBEDDING</h2>
<p> Libev can (and often is) directly embedded into host applications. Examples of applications that embed it include the Deliantra Game Server, the <font SIZE="-1">EV</font> perl module, the <font SIZE="-1">GNU</font> Virtual Private Ethernet (gvpe) and rxvt-unicode. </p>
<p> The goal is to enable you to just copy the necessary files into your source directory without having to change even a single line in them, so you can easily upgrade by simply copying (or having a checked-out copy of libev somewhere in your source tree).</p>
<h3><font SIZE="-1">FILESETS</font></h3>
<p> Depending on what features you need you need to include one or more sets of files in your application. </p>
<p> <i></i><font SIZE="-1"><i>CORE</i></font><i> </i><font SIZE="-1"><i>EVENT</i></font><i> </i><font SIZE="-1"><i>LOOP</i></font><i></i> </p>
<p> To include only the libev core (all the <tt>&quot;ev_*&quot;</tt> functions), with manual configuration (no autoconf): </p>
<p>#define EV_STANDALONE 1<br />
#include &#8220;ev.c&#8221;</p>
<p> This will automatically include <i>ev.h</i>, too, and should be done in a single C source file only to provide the function implementations. To use it, do the same for <i>ev.h</i> in all files wishing to use this <font SIZE="-1">API</font> (best done by writing a wrapper around <i>ev.h</i> that you can include instead and where you can put other configuration options): </p>
<p>#define EV_STANDALONE 1<br />
#include &#8220;ev.h&#8221;</p>
<p> Both header files and implementation files can be compiled with a C<font SIZE="-2">++</font> compiler (at least, that&#8217;s a stated goal, and breakage will be treated as a bug). </p>
<p> You need the following files in your source tree, or in a directory in your include path (e.g. in libev/ when using -Ilibev): </p>
<pre>
   ev.h
   ev.c
   ev_vars.h
   ev_wrap.h
   ev_win32.c      required on win32 platforms only
   ev_select.c     only when select backend is enabled (which is enabled by default)
   ev_poll.c       only when poll backend is enabled (disabled by default)
   ev_epoll.c      only when the epoll backend is enabled (disabled by default)
   ev_kqueue.c     only when the kqueue backend is enabled (disabled by default)
   ev_port.c       only when the solaris port backend is enabled (disabled by default)
</pre>
<p> <i>ev.c</i> includes the backend files directly when enabled, so you only need to compile this single file. </p>
<p> <i></i><font SIZE="-1"><i>LIBEVENT</i></font><i> </i><font SIZE="-1"><i>COMPATIBILITY</i></font><i> </i><font SIZE="-1"><i>API</i></font><i></i> </p>
<p> To include the libevent compatibility <font SIZE="-1">API</font>, also include: </p>
<p>#include &#8220;event.c&#8221;</p>
<p> in the file including <i>ev.c</i>, and: </p>
<p>#include &#8220;event.h&#8221;</p>
<p> in the files that want to use the libevent <font SIZE="-1">API</font>. This also includes <i>ev.h</i>. </p>
<p> You need the following additional files for this: </p>
<pre>
   event.h
   event.c
</pre>
<p> <i></i><font SIZE="-1"><i>AUTOCONF</i></font><i> </i><font SIZE="-1"><i>SUPPORT</i></font><i></i> </p>
<p> Instead of using <tt>&quot;EV_STANDALONE=1&quot;</tt> and providing your configuration in whatever way you want, you can also <tt>&quot;m4_include([libev.m4])&quot;</tt> in your <i>configure.ac</i> and leave <tt>&quot;EV_STANDALONE&quot;</tt> undefined. <i>ev.c</i> will then include <i>config.h</i> and configure itself accordingly. </p>
<p> For this of course you need the m4 file: </p>
<pre>
   libev.m4
</pre>
<h3><font SIZE="-1">PREPROCESSOR</font> <font SIZE="-1">SYMBOLS/MACROS</font></h3>
<p> Libev can be configured via a variety of preprocessor symbols you have to define before including any of its files. The default in the absence of autoconf is documented for every option.</p>
<dl>
<dt><font SIZE="-1">EV_STANDALONE</font></p>
<dd> Must always be <tt>1</tt> if you do not use autoconf configuration, which keeps libev from including <i>config.h</i>, and it also defines dummy implementations for some libevent functions (such as logging, which is not supported). It will also not define any of the structs usually found in <i>event.h</i> that are not directly supported by the libev core alone. </p>
<p> In standalone mode, libev will still try to automatically deduce the configuration, but has to be more conservative.</p>
<dt><font SIZE="-1">EV_USE_MONOTONIC</font></p>
<dd> If defined to be <tt>1</tt>, libev will try to detect the availability of the monotonic clock option at both compile time and runtime. Otherwise no use of the monotonic clock option will be attempted. If you enable this, you usually have to link against librt or something similar. Enabling it when the functionality isn&#8217;t available is safe, though, although you have to make sure you link against any libraries where the <tt>&quot;clock_gettime&quot;</tt> function is hiding in (often <i>-lrt</i>). See also <tt>&quot;EV_USE_CLOCK_SYSCALL&quot;</tt>.</p>
<dt><font SIZE="-1">EV_USE_REALTIME</font></p>
<dd> If defined to be <tt>1</tt>, libev will try to detect the availability of the real-time clock option at compile time (and assume its availability at runtime if successful). Otherwise no use of the real-time clock option will be attempted. This effectively replaces <tt>&quot;gettimeofday&quot;</tt> by <tt>&quot;clock_get (CLOCK_REALTIME, ...)&quot;</tt> and will not normally affect correctness. See the note about libraries in the description of <tt>&quot;EV_USE_MONOTONIC&quot;</tt>, though. Defaults to the opposite value of <tt>&quot;EV_USE_CLOCK_SYSCALL&quot;</tt>.</p>
<dt><font SIZE="-1">EV_USE_CLOCK_SYSCALL</font></p>
<dd> If defined to be <tt>1</tt>, libev will try to use a direct syscall instead of calling the system-provided <tt>&quot;clock_gettime&quot;</tt> function. This option exists because on GNU/Linux, <tt>&quot;clock_gettime&quot;</tt> is in <tt>&quot;librt&quot;</tt>, but <tt>&quot;librt&quot;</tt> unconditionally pulls in <tt>&quot;libpthread&quot;</tt>, slowing down single-threaded programs needlessly. Using a direct syscall is slightly slower (in theory), because no optimised vdso implementation can be used, but avoids the pthread dependency. Defaults to <tt>1</tt> on GNU/Linux with glibc 2.x or higher, as it simplifies linking (no need for <tt>&quot;-lrt&quot;</tt>).</p>
<dt><font SIZE="-1">EV_USE_NANOSLEEP</font></p>
<dd> If defined to be <tt>1</tt>, libev will assume that <tt>&quot;nanosleep ()&quot;</tt> is available and will use it for delays. Otherwise it will use <tt>&quot;select ()&quot;</tt>.</p>
<dt><font SIZE="-1">EV_USE_EVENTFD</font></p>
<dd> If defined to be <tt>1</tt>, then libev will assume that <tt>&quot;eventfd ()&quot;</tt> is available and will probe for kernel support at runtime. This will improve <tt>&quot;ev_signal&quot;</tt> and <tt>&quot;ev_async&quot;</tt> performance and reduce resource consumption. If undefined, it will be enabled if the headers indicate GNU/Linux + Glibc 2.7 or newer, otherwise disabled.</p>
<dt><font SIZE="-1">EV_USE_SELECT</font></p>
<dd> If undefined or defined to be <tt>1</tt>, libev will compile in support for the <tt>&quot;select&quot;</tt>(2) backend. No attempt at auto-detection will be done: if no other method takes over, select will be it. Otherwise the select backend will not be compiled in.</p>
<dt><font SIZE="-1">EV_SELECT_USE_FD_SET</font></p>
<dd> If defined to <tt>1</tt>, then the select backend will use the system <tt>&quot;fd_set&quot;</tt> structure. This is useful if libev doesn&#8217;t compile due to a missing <tt>&quot;NFDBITS&quot;</tt> or <tt>&quot;fd_mask&quot;</tt> definition or it mis-guesses the bitset layout on exotic systems. This usually limits the range of file descriptors to some low limit such as 1024 or might have other limitations (winsocket only allows 64 sockets). The <tt>&quot;FD_SETSIZE&quot;</tt> macro, set before compilation, configures the maximum size of the <tt>&quot;fd_set&quot;</tt>.</p>
<dt><font SIZE="-1">EV_SELECT_IS_WINSOCKET</font></p>
<dd> When defined to <tt>1</tt>, the select backend will assume that select/socket/connect etc. don&#8217;t understand file descriptors but wants osf handles on win32 (this is the case when the select to be used is the winsock select). This means that it will call <tt>&quot;_get_osfhandle&quot;</tt> on the fd to convert it to an <font SIZE="-1">OS</font> handle. Otherwise, it is assumed that all these functions actually work on fds, even on win32. Should not be defined on non-win32 platforms.</p>
<dt><font SIZE="-1">EV_FD_TO_WIN32_HANDLE</font></p>
<dd> If <tt>&quot;EV_SELECT_IS_WINSOCKET&quot;</tt> is enabled, then libev needs a way to map file descriptors to socket handles. When not defining this symbol (the default), then libev will call <tt>&quot;_get_osfhandle&quot;</tt>, which is usually correct. In some cases, programs use their own file descriptor management, in which case they can provide this function to map fds to socket handles.</p>
<dt><font SIZE="-1">EV_USE_POLL</font></p>
<dd> If defined to be <tt>1</tt>, libev will compile in support for the <tt>&quot;poll&quot;</tt>(2) backend. Otherwise it will be enabled on non-win32 platforms. It takes precedence over select.</p>
<dt><font SIZE="-1">EV_USE_EPOLL</font></p>
<dd> If defined to be <tt>1</tt>, libev will compile in support for the Linux <tt>&quot;epoll&quot;</tt>(7) backend. Its availability will be detected at runtime, otherwise another method will be used as fallback. This is the preferred backend for GNU/Linux systems. If undefined, it will be enabled if the headers indicate GNU/Linux + Glibc 2.4 or newer, otherwise disabled.</p>
<dt><font SIZE="-1">EV_USE_KQUEUE</font></p>
<dd> If defined to be <tt>1</tt>, libev will compile in support for the <font SIZE="-1">BSD</font> style <tt>&quot;kqueue&quot;</tt>(2) backend. Its actual availability will be detected at runtime, otherwise another method will be used as fallback. This is the preferred backend for <font SIZE="-1">BSD</font> and BSD-like systems, although on most BSDs kqueue only supports some types of fds correctly (the only platform we found that supports ptys for example was NetBSD), so kqueue might be compiled in, but not be used unless explicitly requested. The best way to use it is to find out whether kqueue supports your type of fd properly and use an embedded kqueue loop.</p>
<dt><font SIZE="-1">EV_USE_PORT</font></p>
<dd> If defined to be <tt>1</tt>, libev will compile in support for the Solaris 10 port style backend. Its availability will be detected at runtime, otherwise another method will be used as fallback. This is the preferred backend for Solaris 10 systems.</p>
<dt><font SIZE="-1">EV_USE_DEVPOLL</font></p>
<dd> Reserved for future expansion, works like the <font SIZE="-1">USE</font> symbols above.</p>
<dt><font SIZE="-1">EV_USE_INOTIFY</font></p>
<dd> If defined to be <tt>1</tt>, libev will compile in support for the Linux inotify interface to speed up <tt>&quot;ev_stat&quot;</tt> watchers. Its actual availability will be detected at runtime. If undefined, it will be enabled if the headers indicate GNU/Linux + Glibc 2.4 or newer, otherwise disabled.</p>
<dt><font SIZE="-1">EV_ATOMIC_T</font></p>
<dd> Libev requires an integer type (suitable for storing <tt>0</tt> or <tt>1</tt>) whose access is atomic with respect to other threads or signal contexts. No such type is easily found in the C language, so you can provide your own type that you know is safe for your purposes. It is used both for signal handler &#8220;locking&#8221; as well as for signal and thread safety in <tt>&quot;ev_async&quot;</tt> watchers. </p>
<p> In the absence of this define, libev will use <tt>&quot;sig_atomic_t volatile&quot;</tt> (from <i>signal.h</i>), which is usually good enough on most platforms.</p>
<dt><font SIZE="-1">EV_H</font></p>
<dd> The name of the <i>ev.h</i> header file used to include it. The default if undefined is <tt>&quot;ev.h&quot;</tt> in <i>event.h</i>, <i>ev.c</i> and <i>ev++.h</i>. This can be used to virtually rename the <i>ev.h</i> header file in case of conflicts.</p>
<dt><font SIZE="-1">EV_CONFIG_H</font></p>
<dd> If <tt>&quot;EV_STANDALONE&quot;</tt> isn&#8217;t <tt>1</tt>, this variable can be used to override <i>ev.c</i>&#8216;s idea of where to find the <i>config.h</i> file, similarly to <tt>&quot;EV_H&quot;</tt>, above.</p>
<dt><font SIZE="-1">EV_EVENT_H</font></p>
<dd> Similarly to <tt>&quot;EV_H&quot;</tt>, this macro can be used to override <i>event.c</i>&#8216;s idea of how the <i>event.h</i> header can be found, the default is <tt>&quot;event.h&quot;</tt>.</p>
<dt><font SIZE="-1">EV_PROTOTYPES</font></p>
<dd> If defined to be <tt>0</tt>, then <i>ev.h</i> will not define any function prototypes, but still define all the structs and other symbols. This is occasionally useful if you want to provide your own wrapper functions around libev functions.</p>
<dt><font SIZE="-1">EV_MULTIPLICITY</font></p>
<dd> If undefined or defined to <tt>1</tt>, then all event-loop-specific functions will have the <tt>&quot;struct ev_loop *&quot;</tt> as first argument, and you can create additional independent event loops. Otherwise there will be no support for multiple event loops and there is no first event loop pointer argument. Instead, all functions act on the single default loop.</p>
<dt><font SIZE="-1">EV_MINPRI</font></p>
<dd>
<dt><font SIZE="-1">EV_MAXPRI</font></p>
<dd> The range of allowed priorities. <tt>&quot;EV_MINPRI&quot;</tt> must be smaller or equal to <tt>&quot;EV_MAXPRI&quot;</tt>, but otherwise there are no non-obvious limitations. You can provide for more priorities by overriding those symbols (usually defined to be <tt>&quot;-2&quot;</tt> and <tt>2</tt>, respectively). </p>
<p> When doing priority-based operations, libev usually has to linearly search all the priorities, so having many of them (hundreds) uses a lot of space and time, so using the defaults of five priorities (-2 .. +2) is usually fine. </p>
<p> If your embedding application does not need any priorities, defining these both to <tt>0</tt> will save some memory and <font SIZE="-1">CPU</font>.</p>
<dt><font SIZE="-1">EV_PERIODIC_ENABLE</font></p>
<dd> If undefined or defined to be <tt>1</tt>, then periodic timers are supported. If defined to be <tt>0</tt>, then they are not. Disabling them saves a few kB of code.</p>
<dt><font SIZE="-1">EV_IDLE_ENABLE</font></p>
<dd> If undefined or defined to be <tt>1</tt>, then idle watchers are supported. If defined to be <tt>0</tt>, then they are not. Disabling them saves a few kB of code.</p>
<dt><font SIZE="-1">EV_EMBED_ENABLE</font></p>
<dd> If undefined or defined to be <tt>1</tt>, then embed watchers are supported. If defined to be <tt>0</tt>, then they are not. Embed watchers rely on most other watcher types, which therefore must not be disabled.</p>
<dt><font SIZE="-1">EV_STAT_ENABLE</font></p>
<dd> If undefined or defined to be <tt>1</tt>, then stat watchers are supported. If defined to be <tt>0</tt>, then they are not.</p>
<dt><font SIZE="-1">EV_FORK_ENABLE</font></p>
<dd> If undefined or defined to be <tt>1</tt>, then fork watchers are supported. If defined to be <tt>0</tt>, then they are not.</p>
<dt><font SIZE="-1">EV_ASYNC_ENABLE</font></p>
<dd> If undefined or defined to be <tt>1</tt>, then async watchers are supported. If defined to be <tt>0</tt>, then they are not.</p>
<dt><font SIZE="-1">EV_MINIMAL</font></p>
<dd> If you need to shave off some kilobytes of code at the expense of some speed (but with the full <font SIZE="-1">API</font>), define this symbol to <tt>1</tt>. Currently this is used to override some inlining decisions, saves roughly 30% code size on amd64. It also selects a much smaller 2-heap for timer management over the default 4-heap. </p>
<p> You can save even more by disabling watcher types you do not need and setting <tt>&quot;EV_MAXPRI&quot;</tt> == <tt>&quot;EV_MINPRI&quot;</tt>. Also, disabling <tt>&quot;assert&quot;</tt> (<tt>&quot;-DNDEBUG&quot;</tt>) will usually reduce code size a lot. </p>
<p> Defining <tt>&quot;EV_MINIMAL&quot;</tt> to <tt>2</tt> will additionally reduce the core <font SIZE="-1">API</font> to provide a bare-bones event library. See <tt>&quot;ev.h&quot;</tt> for details on what parts of the <font SIZE="-1">API</font> are still available, and do not complain if this subset changes over time.</p>
<dt><font SIZE="-1">EV_NSIG</font></p>
<dd> The highest supported signal number, +1 (or, the number of signals): Normally, libev tries to deduce the maximum number of signals automatically, but sometimes this fails, in which case it can be specified. Also, using a lower number than detected (<tt>32</tt> should be good for about any system in existance) can save some memory, as libev statically allocates some 12-24 bytes per signal number.</p>
<dt><font SIZE="-1">EV_PID_HASHSIZE</font></p>
<dd> <tt>&quot;ev_child&quot;</tt> watchers use a small hash table to distribute workload by pid. The default size is <tt>16</tt> (or <tt>1</tt> with <tt>&quot;EV_MINIMAL&quot;</tt>), usually more than enough. If you need to manage thousands of children you might want to increase this value (<i>must</i> be a power of two).</p>
<dt><font SIZE="-1">EV_INOTIFY_HASHSIZE</font></p>
<dd> <tt>&quot;ev_stat&quot;</tt> watchers use a small hash table to distribute workload by inotify watch id. The default size is <tt>16</tt> (or <tt>1</tt> with <tt>&quot;EV_MINIMAL&quot;</tt>), usually more than enough. If you need to manage thousands of <tt>&quot;ev_stat&quot;</tt> watchers you might want to increase this value (<i>must</i> be a power of two).</p>
<dt><font SIZE="-1">EV_USE_4HEAP</font></p>
<dd> Heaps are not very cache-efficient. To improve the cache-efficiency of the timer and periodics heaps, libev uses a 4-heap when this symbol is defined to <tt>1</tt>. The 4-heap uses more complicated (longer) code but has noticeably faster performance with many (thousands) of watchers. </p>
<p> The default is <tt>1</tt> unless <tt>&quot;EV_MINIMAL&quot;</tt> is set in which case it is <tt>0</tt> (disabled).</p>
<dt><font SIZE="-1">EV_HEAP_CACHE_AT</font></p>
<dd> Heaps are not very cache-efficient. To improve the cache-efficiency of the timer and periodics heaps, libev can cache the timestamp (<i>at</i>) within the heap structure (selected by defining <tt>&quot;EV_HEAP_CACHE_AT&quot;</tt> to <tt>1</tt>), which uses 8-12 bytes more per watcher and a few hundred bytes more code, but avoids random read accesses on heap changes. This improves performance noticeably with many (hundreds) of watchers. </p>
<p> The default is <tt>1</tt> unless <tt>&quot;EV_MINIMAL&quot;</tt> is set in which case it is <tt>0</tt> (disabled).</p>
<dt><font SIZE="-1">EV_VERIFY</font></p>
<dd> Controls how much internal verification (see <tt>&quot;ev_loop_verify ()&quot;</tt>) will be done: If set to <tt>0</tt>, no internal verification code will be compiled in. If set to <tt>1</tt>, then verification code will be compiled in, but not called. If set to <tt>2</tt>, then the internal verification code will be called once per loop, which can slow down libev. If set to <tt>3</tt>, then the verification code will be called very frequently, which will slow down libev considerably. </p>
<p> The default is <tt>1</tt>, unless <tt>&quot;EV_MINIMAL&quot;</tt> is set, in which case it will be <tt>0</tt>.</p>
<dt><font SIZE="-1">EV_COMMON</font></p>
<dd> By default, all watchers have a <tt>&quot;void *data&quot;</tt> member. By redefining this macro to a something else you can include more and other types of members. You have to define it each time you include one of the files, though, and it must be identical each time. </p>
<p> For example, the perl <font SIZE="-1">EV</font> module uses something like this: </p>
<p>#define EV_COMMON                             \<br />
    SV *self;      /* contains this struct */ \<br />
    SV *cb_sv, *fh /* note no trailing &#8220;;&#8221; */</p>
<dt><font SIZE="-1">EV_CB_DECLARE</font> (type)</p>
<dd>
<dt><font SIZE="-1">EV_CB_INVOKE</font> (watcher, revents)</p>
<dd>
<dt>ev_set_cb (ev, cb)</p>
<dd> Can be used to change the callback member declaration in each watcher, and the way callbacks are invoked and set. Must expand to a struct member definition and a statement, respectively. See the <i>ev.h</i> header file for their default definitions. One possible use for overriding these is to avoid the <tt>&quot;struct ev_loop *&quot;</tt> as first argument in all cases, or to use method calls instead of plain function calls in C<font SIZE="-2">++</font>.</dl>
<h3><font SIZE="-1">EXPORTED</font> <font SIZE="-1">API</font> <font SIZE="-1">SYMBOLS</font></h3>
<p> If you need to re-export the <font SIZE="-1">API</font> (e.g. via a <font SIZE="-1">DLL</font>) and you need a list of exported symbols, you can use the provided <i>Symbol.*</i> files which list all public symbols, one per line: </p>
<pre>
   Symbols.ev      for libev proper
   Symbols.event   for the libevent emulation
</pre>
<p> This can also be used to rename all public symbols to avoid clashes with multiple versions of libev linked together (which is obviously bad in itself, but sometimes it is inconvenient to avoid this). </p>
<p> A sed command like this will create wrapper <tt>&quot;#define&quot;</tt>&#8216;s that you need to include before including <i>ev.h</i>: </p>
<p>   &lt;Symbols.ev sed -e &#8220;s/.*/#define &amp; myprefix_&amp;/&#8221; &gt;wrap.h</p>
<p> This would create a file <i>wrap.h</i> which essentially looks like this: </p>
<p>#define ev_backend myprefix_ev_backend<br />
#define ev_check_start myprefix_ev_check_start<br />
#define ev_check_stop myprefix_ev_check_stop<br />
&#8230;</p>
<h3><font SIZE="-1">EXAMPLES</font></h3>
<p> For a real-world example of a program the includes libev verbatim, you can have a look at the <font SIZE="-1">EV</font> perl module (&lt;<a rel="nofollow" href="http://software.schmorp.de/pkg/EV.html">http://software.schmorp.de/pkg/EV.html</a>&gt;). It has the libev files in the <i>libev/</i> subdirectory and includes them in the <i></i><font SIZE="-1"><i>EV/EVAPI</i></font><i>.h</i> (public interface) and <i></i><font SIZE="-1"><i>EV</i></font><i>.xs</i> (implementation) files. Only the <i></i><font SIZE="-1"><i>EV</i></font><i>.xs</i> file will be compiled. It is pretty complex because it provides its own header file. </p>
<p> The usage in rxvt-unicode is simpler. It has a <i>ev_cpp.h</i> header file that everybody includes and which overrides some configure choices: </p>
<p>#define EV_MINIMAL 1<br />
#define EV_USE_POLL 0<br />
#define EV_MULTIPLICITY 0<br />
#define EV_PERIODIC_ENABLE 0<br />
#define EV_STAT_ENABLE 0<br />
#define EV_FORK_ENABLE 0<br />
#define EV_CONFIG_H &lt;config.h&gt;<br />
#define EV_MINPRI 0<br />
#define EV_MAXPRI 0<br />
#include &#8220;ev++.h&#8221;</p>
<p> And a <i>ev_cpp.C</i> implementation file that contains libev proper and is compiled: </p>
<p>#include &#8220;ev.c&#8221;<br />
#include &#8220;ev_cpp.h&#8221;</p>
<h2>INTERACTION WITH OTHER PROGRAMS OR LIBRARIES</h2>
<h3><font SIZE="-1">THREADS</font> <font SIZE="-1">AND</font> <font SIZE="-1">COROUTINES</font></h3>
<p> <i></i><font SIZE="-1"><i>THREADS</i></font><i></i> </p>
<p> All libev functions are reentrant and thread-safe unless explicitly documented otherwise, but libev implements no locking itself. This means that you can use as many loops as you want in parallel, as long as there are no concurrent calls into any libev function with the same loop parameter (<tt>&quot;ev_default_*&quot;</tt> calls have an implicit default loop parameter, of course): libev guarantees that different event loops share no data structures that need any locking. </p>
<p> Or to put it differently: calls with different loop parameters can be done concurrently from multiple threads, calls with the same loop parameter must be done serially (but can be done from different threads, as long as only one thread ever is inside a call at any point in time, e.g. by using a mutex per loop). </p>
<p> Specifically to support threads (and signal handlers), libev implements so-called <tt>&quot;ev_async&quot;</tt> watchers, which allow some limited form of concurrency on the same event loop, namely waking it up &#8220;from the outside&#8221;. </p>
<p> If you want to know which design (one loop, locking, or multiple loops without or something else still) is best for your problem, then I cannot help you, but here is some generic advice:</p>
<dl>
<dt>*</p>
<dd> most applications have a main thread: use the default libev loop in that thread, or create a separate thread running only the default loop. </p>
<p> This helps integrating other libraries or software modules that use libev themselves and don&#8217;t care/know about threading.</p>
<dt>*</p>
<dd> one loop per thread is usually a good model. </p>
<p> Doing this is almost never wrong, sometimes a better-performance model exists, but it is always a good start.</p>
<dt>*</p>
<dd> other models exist, such as the leader/follower pattern, where one loop is handed through multiple threads in a kind of round-robin fashion. </p>
<p> Choosing a model is hard &#8211; look around, learn, know that usually you can do better than you currently do :-)</p>
<dt>*</p>
<dd> often you need to talk to some other thread which blocks in the event loop. </p>
<p> <tt>&quot;ev_async&quot;</tt> watchers can be used to wake them up from other threads safely (or from signal contexts&#8230;). </p>
<p> An example use would be to communicate signals or other events that only work in the default loop by registering the signal watcher with the default loop and triggering an <tt>&quot;ev_async&quot;</tt> watcher from the default loop watcher callback into the event loop interested in the signal.</dl>
<p> <font SIZE="-1">THREAD</font> <font SIZE="-1">LOCKING</font> <font SIZE="-1">EXAMPLE</font> </p>
<p> Here is a fictitious example of how to run an event loop in a different thread than where callbacks are being invoked and watchers are created/added/removed. </p>
<p> For a real-world example, see the <tt>&quot;EV::Loop::Async&quot;</tt> perl module, which uses exactly this technique (which is suited for many high-level languages). </p>
<p> The example uses a pthread mutex to protect the loop data, a condition variable to wait for callback invocations, an async watcher to notify the event loop thread and an unspecified mechanism to wake up the main thread. </p>
<p> First, you need to associate some data with the event loop: </p>
<p>typedef struct {<br />
    mutex_t lock; /* global loop lock */<br />
    ev_async async_w;<br />
    thread_t tid;<br />
    cond_t invoke_cv;<br />
} userdata;<br />
void prepare_loop(EV_P)<br />
{<br />
    // for simplicity, we use a static userdata struct.<br />
    static userdata u;<br />
    ev_async_init(&amp;u-&gt;async_w, async_cb);<br />
    ev_async_start(EV_A_ &amp; u-&gt;async_w);<br />
    pthread_mutex_init(&amp;u-&gt;lock, 0);<br />
    pthread_cond_init(&amp;u-&gt;invoke_cv, 0);<br />
    // now associate this with the loop<br />
    ev_set_userdata(EV_A_ u);<br />
    ev_set_invoke_pending_cb(EV_A_ l_invoke);<br />
    ev_set_loop_release_cb(EV_A_ l_release, l_acquire);<br />
    // then create the thread running ev_loop<br />
    pthread_create(&amp;u-&gt;tid, 0, l_run, EV_A);<br />
}</p>
<p> The callback for the <tt>&quot;ev_async&quot;</tt> watcher does nothing: the watcher is used solely to wake up the event loop so it takes notice of any new watchers that might have been added: </p>
<p>static void<br />
async_cb(EV_P_ ev_async *w, int revents)<br />
{<br />
    // just used for the side effects<br />
}</p>
<p> The <tt>&quot;l_release&quot;</tt> and <tt>&quot;l_acquire&quot;</tt> callbacks simply unlock/lock the mutex protecting the loop data, respectively. </p>
<p>static void<br />
l_release(EV_P)<br />
{<br />
    userdata *u = ev_userdata(EV_A);<br />
    pthread_mutex_unlock(&amp;u-&gt;lock);<br />
}<br />
static void<br />
l_acquire(EV_P)<br />
{<br />
    userdata *u = ev_userdata(EV_A);<br />
    pthread_mutex_lock(&amp;u-&gt;lock);<br />
}</p>
<p> The event loop thread first acquires the mutex, and then jumps straight into <tt>&quot;ev_loop&quot;</tt>: </p>
<p>void *<br />
l_run(void *thr_arg)<br />
{<br />
    struct ev_loop *loop = (struct ev_loop *)thr_arg;<br />
    l_acquire(EV_A);<br />
    pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, 0);<br />
    ev_loop(EV_A_ 0);<br />
    l_release(EV_A);<br />
    return 0;<br />
}</p>
<p> Instead of invoking all pending watchers, the <tt>&quot;l_invoke&quot;</tt> callback will signal the main thread via some unspecified mechanism (signals? pipe writes? <tt>&quot;Async::Interrupt&quot;</tt>?) and then waits until all pending watchers have been called (in a while loop because a) spurious wakeups are possible and b) skipping inter-thread-communication when there are no pending watchers is very beneficial): </p>
<p>static void<br />
l_invoke(EV_P)<br />
{<br />
    userdata *u = ev_userdata(EV_A);<br />
    while (ev_pending_count(EV_A)) {<br />
        wake_up_other_thread_in_some_magic_or_not_so_magic_way();<br />
        pthread_cond_wait(&amp;u-&gt;invoke_cv, &amp;u-&gt;lock);<br />
    }<br />
}</p>
<p> Now, whenever the main thread gets told to invoke pending watchers, it will grab the lock, call <tt>&quot;ev_invoke_pending&quot;</tt> and then signal the loop thread to continue: </p>
<p>static void<br />
real_invoke_pending(EV_P)<br />
{<br />
    userdata *u = ev_userdata(EV_A);<br />
    pthread_mutex_lock(&amp;u-&gt;lock);<br />
    ev_invoke_pending(EV_A);<br />
    pthread_cond_signal(&amp;u-&gt;invoke_cv);<br />
    pthread_mutex_unlock(&amp;u-&gt;lock);<br />
}</p>
<p> Whenever you want to start/stop a watcher or do other modifications to an event loop, you will now have to lock: </p>
<p>ev_timer timeout_watcher;<br />
userdata *u = ev_userdata(EV_A);<br />
ev_timer_init(&amp;timeout_watcher, timeout_cb, 5.5, 0.);<br />
pthread_mutex_lock(&amp;u-&gt;lock);<br />
ev_timer_start(EV_A_ &amp;timeout_watcher);<br />
ev_async_send(EV_A_ &amp; u-&gt;async_w);<br />
pthread_mutex_unlock(&amp;u-&gt;lock);</p>
<p> Note that sending the <tt>&quot;ev_async&quot;</tt> watcher is required because otherwise an event loop currently blocking in the kernel will have no knowledge about the newly added timer. By waking up the loop it will pick up any new watchers in the next event loop iteration. </p>
<p> <i></i><font SIZE="-1"><i>COROUTINES</i></font><i></i> </p>
<p> Libev is very accommodating to coroutines (&#8220;cooperative threads&#8221;): libev fully supports nesting calls to its functions from different coroutines (e.g. you can call <tt>&quot;ev_loop&quot;</tt> on the same loop from two different coroutines, and switch freely between both coroutines running the loop, as long as you don&#8217;t confuse yourself). The only exception is that you must not do this from <tt>&quot;ev_periodic&quot;</tt> reschedule callbacks. </p>
<p> Care has been taken to ensure that libev does not keep local state inside <tt>&quot;ev_loop&quot;</tt>, and other calls do not usually allow for coroutine switches as they do not call any callbacks.</p>
<h3><font SIZE="-1">COMPILER</font> <font SIZE="-1">WARNINGS</font></h3>
<p> Depending on your compiler and compiler settings, you might get no or a lot of warnings when compiling libev code. Some people are apparently scared by this. </p>
<p> However, these are unavoidable for many reasons. For one, each compiler has different warnings, and each user has different tastes regarding warning options. &#8220;Warn-free&#8221; code therefore cannot be a goal except when targeting a specific compiler and compiler-version. </p>
<p> Another reason is that some compiler warnings require elaborate workarounds, or other changes to the code that make it less clear and less maintainable. </p>
<p> And of course, some compiler warnings are just plain stupid, or simply wrong (because they don&#8217;t actually warn about the condition their message seems to warn about). For example, certain older gcc versions had some warnings that resulted an extreme number of false positives. These have been fixed, but some people still insist on making code warn-free with such buggy versions. </p>
<p> While libev is written to generate as few warnings as possible, &#8220;warn-free&#8221; code is not a goal, and it is recommended not to build libev with any compiler warnings enabled unless you are prepared to cope with them (e.g. by ignoring them). Remember that warnings are just that: warnings, not errors, or proof of bugs.</p>
<h3><font SIZE="-1">VALGRIND</font></h3>
<p> Valgrind has a special section here because it is a popular tool that is highly useful. Unfortunately, valgrind reports are very hard to interpret. </p>
<p> If you think you found a bug (memory leak, uninitialised data access etc.) in libev, then check twice: If valgrind reports something like: </p>
<p>== 2274 == definitely lost : 0 bytes in 0 blocks.== 2274 == possibly lost : 0 bytes in 0 blocks.== 2274 == still reachable : 256 bytes in 1 blocks.</p>
<p> Then there is no memory leak, just as memory accounted to global variables is not a memleak &#8211; the memory is still being referenced, and didn&#8217;t leak. </p>
<p> Similarly, under some circumstances, valgrind might report kernel bugs as if it were a bug in libev (e.g. in realloc or in the poll backend, although an acceptable workaround has been found here), or it might be confused. </p>
<p> Keep in mind that valgrind is a very good tool, but only a tool. Don&#8217;t make it into some kind of religion. </p>
<p> If you are unsure about something, feel free to contact the mailing list with the full valgrind report and an explanation on why you think this is a bug in libev (best check the archives, too :). However, don&#8217;t be annoyed when you get a brisk &#8220;this is no bug&#8221; answer and take the chance of learning how to interpret valgrind properly. </p>
<p> If you need, for some reason, empty reports from valgrind for your project I suggest using suppression lists.</p>
<h2>PORTABILITY NOTES</h2>
<h3><font SIZE="-1">WIN32</font> <font SIZE="-1">PLATFORM</font> <font SIZE="-1">LIMITATIONS</font> <font SIZE="-1">AND</font> <font SIZE="-1">WORKAROUNDS</font></h3>
<p> Win32 doesn&#8217;t support any of the standards (e.g. <font SIZE="-1">POSIX</font>) that libev requires, and its I/O model is fundamentally incompatible with the <font SIZE="-1">POSIX</font> model. Libev still offers limited functionality on this platform in the form of the <tt>&quot;EVBACKEND_SELECT&quot;</tt> backend, and only supports socket descriptors. This only applies when using Win32 natively, not when using e.g. cygwin. </p>
<p> Lifting these limitations would basically require the full re-implementation of the I/O system. If you are into these kinds of things, then note that glib does exactly that for you in a very portable way (note also that glib is the slowest event library known to man). </p>
<p> There is no supported compilation method available on windows except embedding it into other applications. </p>
<p> Sensible signal handling is officially unsupported by Microsoft &#8211; libev tries its best, but under most conditions, signals will simply not work. </p>
<p> Not a libev limitation but worth mentioning: windows apparently doesn&#8217;t accept large writes: instead of resulting in a partial write, windows will either accept everything or return <tt>&quot;ENOBUFS&quot;</tt> if the buffer is too large, so make sure you only write small amounts into your sockets (less than a megabyte seems safe, but this apparently depends on the amount of memory available). </p>
<p> Due to the many, low, and arbitrary limits on the win32 platform and the abysmal performance of winsockets, using a large number of sockets is not recommended (and not reasonable). If your program needs to use more than a hundred or so sockets, then likely it needs to use a totally different implementation for windows, as libev offers the <font SIZE="-1">POSIX</font> readiness notification model, which cannot be implemented efficiently on windows (due to Microsoft monopoly games). </p>
<p> A typical way to use libev under windows is to embed it (see the embedding section for details) and use the following <i>evwrap.h</i> header file instead of <i>ev.h</i>: </p>
<p>#define EV_STANDALONE            /* keeps ev from requiring config.h */<br />
#define EV_SELECT_IS_WINSOCKET 1 /* configure libev for windows select */<br />
#include &#8220;ev.h&#8221;</p>
<p> And compile the following <i>evwrap.c</i> file into your project (make sure you do <i>not</i> compile the <i>ev.c</i> or any other embedded source files!): </p>
<p>#include &#8220;ev.c&#8221;<br />
#include &#8220;evwrap.h&#8221;</p>
<dl>
<dt>The winsocket select function</p>
<dd> The winsocket <tt>&quot;select&quot;</tt> function doesn&#8217;t follow <font SIZE="-1">POSIX</font> in that it requires socket <i>handles</i> and not socket <i>file descriptors</i> (it is also extremely buggy). This makes select very inefficient, and also requires a mapping from file descriptors to socket handles (the Microsoft C runtime provides the function <tt>&quot;_open_osfhandle&quot;</tt> for this). See the discussion of the <tt>&quot;EV_SELECT_USE_FD_SET&quot;</tt>, <tt>&quot;EV_SELECT_IS_WINSOCKET&quot;</tt> and <tt>&quot;EV_FD_TO_WIN32_HANDLE&quot;</tt> preprocessor symbols for more info. </p>
<p> The configuration for a &#8220;naked&#8221; win32 using the Microsoft runtime libraries and raw winsocket select is: </p>
<pre><code>
#define EV_USE_SELECT 1
#define EV_SELECT_IS_WINSOCKET 1 /* forces EV_SELECT_USE_FD_SET, too */
</code></pre>
<p> Note that winsockets handling of fd sets is <a href="/docs/linux/man/n-o/">O</a>(n), so you can easily get a complexity in the O(nAX) range when using win32.</p>
<dt>Limited number of file descriptors</p>
<dd> Windows has numerous arbitrary (and low) limits on things. </p>
<p> Early versions of winsocket&#8217;s select only supported waiting for a maximum of <tt>64</tt> handles (probably owning to the fact that all windows kernels can only wait for <tt>64</tt> things at the same time internally; Microsoft recommends spawning a chain of threads and wait for 63 handles and the previous thread in each. Sounds great!). </p>
<p> Newer versions support more handles, but you need to define <tt>&quot;FD_SETSIZE&quot;</tt> to some high number (e.g. <tt>2048</tt>) before compiling the winsocket select call (which might be in libev or elsewhere, for example, perl and many other interpreters do their own select emulation on windows). </p>
<p> Another limit is the number of file descriptors in the Microsoft runtime libraries, which by default is <tt>64</tt> (there must be a hidden <i>64</i> fetish or something like this inside Microsoft). You can increase this by calling <tt>&quot;_setmaxstdio&quot;</tt>, which can increase this limit to <tt>2048</tt> (another arbitrary limit), but is broken in many versions of the Microsoft runtime libraries. This might get you to about <tt>512</tt> or <tt>2048</tt> sockets (depending on windows version and/or the phase of the moon). To get more, you need to wrap all I/O functions and provide your own fd management, but the cost of calling select (O(nAX)) will likely make this unworkable.</dl>
<h3><font SIZE="-1">PORTABILITY</font> <font SIZE="-1">REQUIREMENTS</font></h3>
<p> In addition to a working ISO-C implementation and of course the backend-specific APIs, libev relies on a few additional extensions:</p>
<dl>
<dt>void (*)(ev_watcher_type *, int revents) must have compatible calling conventions regardless of ev_watcher_type *.</p>
<dd> Libev assumes not only that all watcher pointers have the same internal structure (guaranteed by <font SIZE="-1">POSIX</font> but not by <font SIZE="-1">ISO</font> C for example), but it also assumes that the same (machine) code can be used to call any watcher callback: The watcher callbacks have different type signatures, but libev calls them using an <tt>&quot;ev_watcher *&quot;</tt> internally.</p>
<dt>sig_atomic_t volatile must be thread-atomic as well</p>
<dd> The type <tt>&quot;sig_atomic_t volatile&quot;</tt> (or whatever is defined as <tt>&quot;EV_ATOMIC_T&quot;</tt>) must be atomic with respect to accesses from different threads. This is not part of the specification for <tt>&quot;sig_atomic_t&quot;</tt>, but is believed to be sufficiently portable.</p>
<dt>sigprocmask must work in a threaded environment</p>
<dd> Libev uses <tt>&quot;sigprocmask&quot;</tt> to temporarily block signals. This is not allowed in a threaded program (<tt>&quot;pthread_sigmask&quot;</tt> has to be used). Typical pthread implementations will either allow <tt>&quot;sigprocmask&quot;</tt> in the &#8220;main thread&#8221; or will block signals process-wide, both behaviours would be compatible with libev. Interaction between <tt>&quot;sigprocmask&quot;</tt> and <tt>&quot;pthread_sigmask&quot;</tt> could complicate things, however. </p>
<p> The most portable way to handle signals is to block signals in all threads except the initial one, and run the default loop in the initial thread as well.</p>
<dt>long must be large enough for common memory allocation sizes</p>
<dd> To improve portability and simplify its <font SIZE="-1">API</font>, libev uses <tt>&quot;long&quot;</tt> internally instead of <tt>&quot;size_t&quot;</tt> when allocating its data structures. On non-POSIX systems (Microsoft&#8230;) this might be unexpectedly low, but is still at least 31 bits everywhere, which is enough for hundreds of millions of watchers.</p>
<dt>double must hold a time value in seconds with enough accuracy</p>
<dd> The type <tt>&quot;double&quot;</tt> is used to represent timestamps. It is required to have at least 51 bits of mantissa (and 9 bits of exponent), which is good enough for at least into the year 4000. This requirement is fulfilled by implementations implementing <font SIZE="-1">IEEE</font> 754, which is basically all existing ones. With <font SIZE="-1">IEEE</font> 754 doubles, you get microsecond accuracy until at least 2200.</dl>
<p> If you know of other additional requirements drop me a note.</p>
<h2>ALGORITHMIC COMPLEXITIES</h2>
<p> In this section the complexities of (many of) the algorithms used inside libev will be documented. For complexity discussions about backends see the documentation for <tt>&quot;ev_default_init&quot;</tt>. </p>
<p> All of the following are about amortised time: If an array needs to be extended, libev needs to realloc and move the whole array, but this happens asymptotically rarer with higher number of elements, so <a href="/docs/linux/man/1-o/">O</a>(1) might mean that libev does a lengthy realloc operation in rare cases, but on average it is much faster and asymptotically approaches constant time.</p>
<dl>
<dt>Starting and stopping timer/periodic watchers: O(log skipped_other_timers)</p>
<dd> This means that, when you have a watcher that triggers in one hour and there are 100 watchers that would trigger before that, then inserting will have to skip roughly seven (<tt>&quot;ld 100&quot;</tt>) of these watchers.</p>
<dt>Changing timer/periodic watchers (by autorepeat or calling again): O(log skipped_other_timers)</p>
<dd> That means that changing a timer costs less than removing/adding them, as only the relative motion in the event queue has to be paid for.</p>
<dt>Starting io/check/prepare/idle/signal/child/fork/async watchers: <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<dd> These just add the watcher into an array or at the head of a list.</p>
<dt>Stopping check/prepare/idle/fork/async watchers: <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<dd>
<dt>Stopping an io/signal/child watcher: O(number_of_watchers_for_this_(fd/signal/pid % <font SIZE="-1">EV_PID_HASHSIZE</font>))</p>
<dd> These watchers are stored in lists, so they need to be walked to find the correct watcher to remove. The lists are usually short (you don&#8217;t usually have many watchers waiting for the same fd or signal: one is typical, two is rare).</p>
<dt>Finding the next timer in each loop iteration: <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<dd> By virtue of using a binary or 4-heap, the next timer is always found at a fixed position in the storage array.</p>
<dt>Each change on a file descriptor per loop iteration: O(number_of_watchers_for_this_fd)</p>
<dd> A change means an I/O watcher gets started or stopped, which requires libev to recalculate its status (and possibly tell the kernel, depending on backend and whether <tt>&quot;ev_io_set&quot;</tt> was used).</p>
<dt>Activating one watcher (putting it into the pending state): <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<dd>
<dt>Priority handling: O(number_of_priorities)</p>
<dd> Priorities are implemented by allocating some space for each priority. When doing priority-based operations, libev usually has to linearly search all the priorities, but starting/stopping and activating watchers becomes <a href="/docs/linux/man/1-o/">O</a>(1) with respect to priority handling.</p>
<dt>Sending an ev_async: <a href="/docs/linux/man/1-o/">O</a>(1)</p>
<dd>
<dt>Processing ev_async_send: O(number_of_async_watchers)</p>
<dd>
<dt>Processing signals: O(max_signal_number)</p>
<dd> Sending involves a system call <i>iff</i> there were no other <tt>&quot;ev_async_send&quot;</tt> calls in the current loop iteration. Checking for async and signal events involves iterating over all running async watchers or all signal numbers.</dl>
<h2>GLOSSARY</h2>
<dl>
<dt>active</p>
<dd> A watcher is active as long as it has been started (has been attached to an event loop) but not yet stopped (disassociated from the event loop).</p>
<dt>application</p>
<dd> In this document, an application is whatever is using libev.</p>
<dt>callback</p>
<dd> The address of a function that is called when some event has been detected. Callbacks are being passed the event loop, the watcher that received the event, and the actual event bitset.</p>
<dt>callback invocation</p>
<dd> The act of calling the callback associated with a watcher.</p>
<dt>event</p>
<dd> A change of state of some external event, such as data now being available for reading on a file descriptor, time having passed or simply not having any other events happening anymore. </p>
<p> In libev, events are represented as single bits (such as <tt>&quot;EV_READ&quot;</tt> or <tt>&quot;EV_TIMEOUT&quot;</tt>).</p>
<dt>event library</p>
<dd> A software package implementing an event model and loop.</p>
<dt>event loop</p>
<dd> An entity that handles and processes external events and converts them into callback invocations.</p>
<dt>event model</p>
<dd> The model used to describe how an event loop handles and processes watchers and events.</p>
<dt>pending</p>
<dd> A watcher is pending as soon as the corresponding event has been detected, and stops being pending as soon as the watcher will be invoked or its pending status is explicitly cleared by the application. </p>
<p> A watcher can be pending, but not active. Stopping a watcher also clears its pending status.</p>
<dt>real time</p>
<dd> The physical time that is observed. It is apparently strictly monotonic :)</p>
<dt>wall-clock time</p>
<dd> The time and date as shown on clocks. Unlike real time, it can actually be wrong and jump forwards and backwards, e.g. when the you adjust your clock.</p>
<dt>watcher</p>
<dd> A data structure that describes interest in certain events. Watchers need to be started (attached to an event loop) before they can receive events.</p>
<dt>watcher invocation</p>
<dd> The act of calling the callback associated with a watcher.</dl>
<h2>AUTHOR</h2>
<p> Marc Lehmann &lt;libev [at] schmorp.de&gt;, with repeated corrections by Mikael Magnusson. </p>
<h2>Index</h2>
<dt><a href="#lbAE">ABOUT THIS DOCUMENT</a></p>
<dd>
<dt><a href="#lbAF">ABOUT LIBEV</a></p>
<dd>
<dt><a href="#lbAJ">ERROR HANDLING</a></p>
<dd>
<dt><a href="#lbAK">GLOBAL FUNCTIONS</a></p>
<dd>
<dt><a href="#lbAL">FUNCTIONS CONTROLLING THE EVENT LOOP</a></p>
<dd>
<dt><a href="#lbAM">ANATOMY OF A WATCHER</a></p>
<dd>
<dt><a href="#lbAQ">WATCHER TYPES</a></p>
<dd>
<dt><a href="#lbBC">OTHER FUNCTIONS</a></p>
<dd>
<dt><a href="#lbBD">LIBEVENT EMULATION</a></p>
<dd>
<dt><a href="#lbBE">C<font SIZE="-2">++</font> SUPPORT</a></p>
<dd>
<dt><a href="#lbBF">OTHER LANGUAGE BINDINGS</a></p>
<dd>
<dt><a href="#lbBG">MACRO MAGIC</a></p>
<dd>
<dt><a href="#lbBH">EMBEDDING</a></p>
<dd>
<dt><a href="#lbBM">INTERACTION WITH OTHER PROGRAMS OR LIBRARIES</a></p>
<dd>
<dt><a href="#lbBQ">PORTABILITY NOTES</a></p>
<dd>
<dt><a href="#lbBT">ALGORITHMIC COMPLEXITIES</a></p>
<dd>
<dt><a href="#lbBU">GLOSSARY</a></p>
<dd>
<dt><a href="#lbBV">AUTHOR</a></p>
<dd></dl>
