---
title: "zclock(3)"
name: "zclock"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zclock/"
description: "zclock – millisecond clocks and delays"
---

<p>zclock &#8211; millisecond clocks and delays</p>
<h2>Synopsis</h2>
<pre>// Sleep for a number of milliseconds
CZMQ_EXPORT void
 zclock_sleep (int msecs);
// Return current system clock as milliseconds. Note that this clock can
// jump backwards (if the system clock is changed) so is unsafe to use for
// timers and time offsets. Use zclock_mono for that instead.
CZMQ_EXPORT int64_t
 zclock_time (void);
// Return current monotonic clock in milliseconds. Use this when you compute
// time offsets. The monotonic clock is not affected by system changes and
// so will never be reset backwards, unlike a system clock.
CZMQ_EXPORT int64_t
 zclock_mono (void);
// Return current monotonic clock in microseconds. Use this when you compute
// time offsets. The monotonic clock is not affected by system changes and
// so will never be reset backwards, unlike a system clock.
CZMQ_EXPORT int64_t
 zclock_usecs (void);
// Return formatted date/time as fresh string. Free using zstr_free().
CZMQ_EXPORT char *
 zclock_timestr (void);
// Self test of this class
CZMQ_EXPORT void
 zclock_test (bool verbose);</pre>
<h2>Description</h2>
<p>The zclock class provides essential sleep and system time functions, used to slow down threads for testing, and calculate timers for polling. Wraps the non-portable system calls in a simple portable API. </p>
<p> The Win32 Sleep() call defaults to 16ms resolution unless the system timer resolution is increased with a call to timeBeginPeriod() permitting 1ms granularity.</p>
<h2>Example</h2>
<p><code>From zclock_test method</code>. </p>
<pre><code>int64_t start = zclock_time();
zclock_sleep(10);
assert((zclock_time() - start) &gt;= 10);
start = zclock_mono();
int64_t usecs = zclock_usecs();
zclock_sleep(10);
assert((zclock_mono() - start) &gt;= 10);
assert((zclock_usecs() - usecs) &gt;= 10000);
char *timestr = zclock_timestr();
if (verbose)
    puts(timestr);
free(timestr);
</code></pre>
<h2>Authors</h2>
<p>The czmq manual was written by the authors in the AUTHORS file.</p>
<h2>Resources</h2>
<p>Main web site: m[blue]m[] </p>
<p> Report bugs to the email &lt;m[blue]<code>zeromq-dev [at] lists.zeromq.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991-2012 iMatix Corporation &#8212; <a rel="nofollow" href="http://www.imatix.com">http://www.imatix.com</a> Copyright other contributors as noted in the AUTHORS file. This file is part of CZMQ, the high-level C binding for 0MQ: <a href="http://czmq.zeromq.org">http://czmq.zeromq.org</a> This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> LICENSE included with the czmq distribution.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>zeromq-dev [at] lists.zeromq.org</p>
<dl>
<dd>mailto:zeromq-dev [at] lists.zeromq.org</dl>
