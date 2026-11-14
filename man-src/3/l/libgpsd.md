---
title: "libgpsd(3)"
name: "libgpsd"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libgpsd/"
description: "libgpsd – service library for GPS applications"
---

<h2 class="name">NAME</h2>
<p> libgpsd &#8211; service library for GPS applications </p>
<h2>SYNOPSIS</h2>
<pre><code>
C:
#include &lt;gpsd.h&gt;
</code></pre>
<dl>
<dt> <code>int gpsd_open_dgps(char&nbsp;<wbr>*&nbsp;<wbr></code><i>dgpsserver</i><code>);</code></p>
<dt> <code>void gpsd_init(struct gps_device_t&nbsp;<wbr>*</code><i>session</i><code>, struct&nbsp;<wbr>*&nbsp;<wbr></code><i>gps_context_t&nbsp;<wbr>*</i><code>, char&nbsp;<wbr>*&nbsp;<wbr></code><i>device</i><code>);</code></p>
<dt> <code>int gpsd_activate(struct gps_device_t&nbsp;<wbr>*</code><i>session</i><code>);</code></p>
<dt> <code>void gpsd_deactivate(struct gps_device_t&nbsp;<wbr>*&nbsp;<wbr></code><i>session</i><code>);</code></p>
<dt> <code>gps_mask_t gpsd_poll(struct gps_device_t&nbsp;<wbr>*&nbsp;<wbr></code><i>session</i><code>);</code></p>
<dt> <code>void gpsd_wrap(struct gps_device_t&nbsp;<wbr>*&nbsp;<wbr></code><i>session</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>libgpsd</code></p>
<dd>is a service library which supports querying GPS devices; link it with the linker option -lgpsd. It is a set of low-level device-handling calls, which <code><a href="/docs/linux/man/1-gpsd/">gpsd</a></code>(1) itself uses. See <code><a href="/docs/linux/man/3-gpsd/">gpsd</a></code>(3) for a description of the high-level interface, which is almost certainly what you want. </p>
<p> Calling <code>gpsd_init()</code> initializes a session structure to hold the data collected by the GPS. </p>
<p> The second argument must be a context structure. The library will use it for information that need to be shared between sessions; presently this includes the leap-second correction and possibly a pointer to a shared-memory segment used to communicate with the Network Time Protocol daemon. </p>
<p> After the session structure has been set up, you may modify some of its members. </p>
<p> <i>gpsd_device</i></p>
<dl>
<dt>
<dd> This member should hold the path name of the device.</dl>
<p> <i>baudrate</i></p>
<dl>
<dt>
<dd> Communication speed in bits per second. For NMEA or SiRF devices, the library automatically hunts through all plausible baud rates, stopping on the one where it sees valid packets. By setting this field you can designate a speed to be tried at the front of the hunt queue</dl>
<p> <code>gpsd_activate()</code> initializes the connection to the GPS. <code>gpsd_deactivate()</code> closes the connection. These functions are provided so that long-running programs can release a connection when there is no activity requiring the GPS, and re-acquire it later. </p>
<p> <code>gpsd_poll()</code> queries the GPS and updates the part of the session structure that holds position, speed, GPS signal quality, and other data returned by the GPS. It returns a mask describing which fields have changed. </p>
<p> <code>gpsd_wrap()</code> ends the session, implicitly performing a <code>gpsd_deactivate()</code>. </p>
<p> The calling application must define one additional function: <code>gpsd_report()</code>. The library will use this to issue ordinary status messages. See gpsd.h in the source distribution for the set of logging levels. </p>
<p> The low-level functions do not allocate or free any dynamic storage. They can thus be used in a long-running application (such as <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8) itself) with a guarantee that they won&#8217;t cause memory leaks.</p>
<h2>BUGS</h2>
<p> Writes to the context structure members are not guarded by a mutex.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt; based partly on earlier work by Remco Treffkorn, Derrick Brashear, and Russ Nelson. </p>
<h2>Index</h2>
