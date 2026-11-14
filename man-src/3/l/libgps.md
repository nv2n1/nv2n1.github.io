---
title: "libgps(3)"
name: "libgps"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libgps/"
description: "libgps – C service library for communicating with the GPS daemon"
---

<h2 class="name">NAME</h2>
<p> libgps &#8211; C service library for communicating with the GPS daemon </p>
<h2>SYNOPSIS</h2>
<pre><code>
C:
#include &lt;gps.h&gt;
</code></pre>
<dl>
<dt> <code>int gps_open(char&nbsp;<wbr>*</code><i>server</i><code>, char&nbsp;<wbr>*&nbsp;<wbr></code><i>port</i><code>, struct gps_data_t&nbsp;<wbr>*</code><i>gpsdata</i><code>);</code></p>
<dt> <code>int gps_send(struct gps_data_t&nbsp;<wbr>*</code><i>gpsdata</i><code>, char&nbsp;<wbr>*</code><i>fmt</i><code>&#8230;);</code></p>
<dt> <code>int gps_read(struct gps_data_t&nbsp;<wbr>*</code><i>gpsdata</i><code>);</code></p>
<dt> <code>bool gps_waiting(const struct gps_data_t&nbsp;<wbr>*</code><i>gpsdata</i><code>, int&nbsp;<wbr></code><i>timeout</i><code>);</code></p>
<dt> <code>char *gps_data(const struct gps_data_t&nbsp;<wbr>*</code><i>gpsdata</i><code>);</code></p>
<dt> <code>int gps_unpack(char&nbsp;<wbr>*</code><i>buf</i><code>, struct gps_data_t&nbsp;<wbr>*</code><i>gpsdata</i><code>);</code></p>
<dt> <code>void gps_close(struct gps_data_t&nbsp;<wbr>*</code><i>gpsdata</i><code>);</code></p>
<dt> <code>int gps_stream(struct gps_data_t&nbsp;<wbr>*</code><i>gpsdata</i><code>, unsigned int</code><i>flags</i><code>, void&nbsp;<wbr>*</code><i>data</i><code>);</code></p>
<dt> <code>const char *gps_errstr(int&nbsp;<wbr></code><i>err</i><code>);</code> </p>
<pre>
<dd>Python:
import gps
session = gps.gps(host=&quot;localhost&quot;, port=&quot;2947&quot;)
session.stream(flags=gps.WATCH_JSON)
for report in session:
    process(report)
del session
</pre>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>libgps</code> is a service library which supports communicating with an instance of the <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8); link it with the linker option -lgps. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Warning</code> </font> </p>
<p> Take care to conditionalize your code on the major and minor API version symbols in gps.h; ideally, force a compilation failure if GPSD_API_MAJOR_VERSION is not a version you recognize. See the GPSD project website for more information on the protocol and API changes. </p>
</dl>
<p> Calling <code>gps_open()</code> initializes a GPS-data structure to hold the data collected by the GPS, and sets up access to <code><a href="/docs/linux/man/1-gpsd/">gpsd</a></code>(1) via either the socket or shared-memory export. The shared-memory export is faster, but does not carry information about device activation and deactivation events and will not allow you to monitor device packet traffic. </p>
<p> <code>gps_open()</code> returns 0 on success, -1 on errors and is re-entrant. errno is set depending on the error returned from the socket or shared-memory interface; see gps.h for values and explanations; also see <code>gps_errstr()</code>. The host address may be a DNS name, an IPv4 dotted quad, an IPV6 address, or the special value <code>GPSD_SHARED_MEMORY</code> referring to the shared-memory export; the library will do the right thing for any of these. </p>
<p> <code>gps_close()</code> ends the session. </p>
<p> <code>gps_send()</code> writes a command to the daemon. It does nothing when using the shared-memory export. The second argument must be a format string containing elements from the command set documented at <code><a href="/docs/linux/man/1-gpsd/">gpsd</a></code>(1). It may have % elements as for <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3), which will be filled in from any following arguments. This function returns a -1 if there was a Unix-level write error, otherwise 0. Please read the LIMITATIONS section for additional information and cautions. See <code>gps_stream()</code> as a possible alternative. </p>
<p> <code>gps_read()</code> accepts a response, or sequence of responses, from the daemon and interprets. This function does either a nonblocking read for data from the daemon or a fetch from shared memory; it returns a count of bytes read for success, -1 with errno set on a Unix-level read error, -1 with errno not set if the socket to the daemon has closed or if the shared-memory segment was unavailable, and 0 if no data is available. </p>
<p> <code>gps_waiting()</code> can be used to check whether there is new data from the daemon. The second argument is the maximum amount of time to wait (in microseconds) on input before returning. It returns true if there is input waiting, false on timeout (no data waiting) or error condition. When using the socket export, this function is a convenience wrapper around a <code><a href="/docs/linux/man/2-select/">select</a></code>(2) call, and zeros <i>errno</i> on entry; you can test <i>errno</i> after exit to get more information about error conditions. </p>
<p> <code>gps_unpack()</code> parses JSON from the argument buffer into the target of the session structure pointer argument. Included in case your application wishes to manage socket I/O itself. </p>
<p> <code>gps_data()</code> returns the contents of the client data buffer (it returns NULL when using the shared-memory export). Use with care; this may fail to be a NUL-terminated string if WATCH_RAW is enabled. </p>
<p> <code>gps_stream()</code> asks gpsd to stream the reports it has at you, to be made available when you poll (not available when using the shared-memory export). The second argument is a flag mask that sets various policy bits; see the list below. Calling <code>gps_stream()</code> more than once with different flag masks is allowed. </p>
<p> WATCH_DISABLE</p>
<dl>
<dt>
<dd> Disable the reporting modes specified by the other WATCH_ flags.</dl>
<p> WATCH_ENABLE</p>
<dl>
<dt>
<dd> Disable the reporting modes specified by the other WATCH_ flags. This is the default.</dl>
<p> WATCH_JSON</p>
<dl>
<dt>
<dd> Enable JSON reporting of data. If WATCH_ENABLE is set, and no other WATCH flags are set, this is the default.</dl>
<p> WATCH_NMEA</p>
<dl>
<dt>
<dd> Enable generated pseudo-NMEA reporting on binary devices.</dl>
<p> WATCH_RARE</p>
<dl>
<dt>
<dd> Enable reporting of binary packets in encoded hex.</dl>
<p> WATCH_RAW</p>
<dl>
<dt>
<dd> Enable literal passthrough of binary packets.</dl>
<p> WATCH_SCALED</p>
<dl>
<dt>
<dd> When reporting AIS or Subframe data, scale integer quantities to floats if they have a divisor or rendering formula associated with them.</dl>
<p> WATCH_NEWSTYLE</p>
<dl>
<dt>
<dd> Force issuing a JSON initialization and getting new-style responses. This is the default.</dl>
<p> WATCH_OLDSTYLE</p>
<dl>
<dt>
<dd> Force issuing a W or R command and getting old-style responses. Warning: this flag (and the capability) will be removed in a future release.</dl>
<p> WATCH_DEVICE</p>
<dl>
<dt>
<dd> Restrict watching to a specified device, patch given as second argument.</dl>
<p> <code>gps_errstr()</code> returns an ASCII string (in English) describing the error indicated by a nonzero return value from <code>gps_open()</code>. </p>
<p> Consult gps.h to learn more about the data members and associated timestamps. Note that information will accumulate in the session structure over time, and the &#8216;valid&#8217; field is not automatically zeroed by each <code>gps_read()</code>. It is up to the client to zero that field when appropriate and to keep an eye on the fix and sentence timestamps. </p>
<p> The Python implementation supports the same facilities as the socket-export calls in the C library; there is no shared-memory interface. <code>gps_open()</code> is replaced by the initialization of a gps session object; the other calls are methods of that object, and have the same names as the corresponding C functions. However, it is simpler just to use the session object as an iterator, as in the example given below. Resources within the session object will be properly released when it is garbage-collected.</p>
<h2>CODE EXAMPLE</h2>
<p> The following is an excerpted and simplified version of the libgps interface code from <code><a href="/docs/linux/man/1-cgps/">cgps</a></code>(1). </p>
<dl>
<dt>
<dd>
<pre><code>
struct gps_data_t gps_data;
ret = gps_open(hostName, hostPort, &amp;gps_data);
(void)gps_stream(&amp;gps_data, WATCH_ENABLE | WATCH_JSON, NULL);
/* Put this in a loop with a call to a high resolution sleep () in it. */
if (gps_waiting(&amp;gps_data, 500)) {
    errno = 0;
    if (gps_read(&amp;gps_data) == -1) {
        ...
    } else {
        /* Display data from the GPS receiver. */
            if (gps_data.set &amp; ...
    }
}
/* When you are done... */
(void)gps_stream(&amp;gps_data, WATCH_DISABLE, NULL);
(void)gps_close(&amp;gps_data);
</code></pre>
</dl>
<h2>LIMITATIONS</h2>
<p> On some systems (those which do not support implicit linking in libraries) you may need to add -lm to your link line when you link libgps. It is always safe to do this. </p>
<p> In the C API, incautious use of <code>gps_send()</code> may lead to subtle bugs. In order to not bloat struct gps_data_t with space used by responses that are not expected to be shipped in close sequence with each other, the storage for fields associated with certain responses are combined in a union. </p>
<p> The risky set of responses includes VERSION, DEVICELIST, RTCM2, RTCM3, SUBFRAME, AIS, GST, and ERROR; it may not be limited to that set. The logic of the daemon&#8217;s watcher mode is careful to avoid dangerous sequences, but you should read and understand the layout of struct gps_data_t before using <code>gps_send()</code> to request any of these responses.</p>
<h2>COMPATIBILITY</h2>
<p> The <code>gps_query()</code> supported in major versions 1 and 2 of this library has been removed. With the new streaming-oriented wire protocol behind this library, it is extremely unwise to assume that the first transmission from the daemon after a command is shipped to it will be the response to command. </p>
<p> If you must send commands to the daemon explicitly, use <code>gps_send()</code> but beware that this ties your code to the GPSD wire protocol. It is not recommended. </p>
<p> In earlier versions of the API <code>gps_read()</code> was a blocking call and there was a POLL_NONBLOCK option to make it nonblocking. <code>gps_waiting()</code> was added to reduce the number of wrong ways to code a polling loop. </p>
<p> See the comment above the symbol GPSD_API_MAJOR_VERSION in gps.h for recent changes.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3). <code><a href="/docs/linux/man/3-libgpsmm/">libgpsmm</a></code>(3).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;, C sample code Charles Curley &lt;charlescurley [at] charlescurley.com&gt; </p>
<h2>Index</h2>
