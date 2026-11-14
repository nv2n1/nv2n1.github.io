---
title: "xibarrierreleasepointers(3)"
name: "xibarrierreleasepointers"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xibarrierreleasepointers/"
---

XIBarrierReleasePointer, XIBarrierReleasePointers - allow pointer movement across a pointer barrier 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>int XIBarrierReleasePointer( Display *display,
 int deviceid,
 PointerBarrier barrier,
 BarrierEventID eventid);</pre><pre>int XIBarrierReleasePointers( Display *display,
 XIBarrierReleasePointerInfo *barriers,
 int num_barriers);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>deviceid
 Specifies the device allowed to move across the barrier.</pre><pre>barrier
 Specifies the barrier.</pre><pre>eventid
 Specifies the unique event ID for this barrier event sequence.</pre><pre>barriers
 List of deviceid, barrier, eventid triplets.</pre><pre>num_barriers
 Number of elements in barriers.</pre><h2>Description</h2><dl COMPACT><dd><pre>If a pointer is constrained by a pointer barrier, release the pointer
from the barrier and allow it to cross the barrier with the next motion.
If the pointer moves away from the barrier, this request does nothing.</pre></dl><dl COMPACT><dd><pre>This request only releases the pointer for the given barrier event
sequence. If the pointer moves away from or through the barrier, a
XI_BarrierLeave event is generated. Future pointer movement constrained
by this barrier will assign a new eventid and require a new
XIBarrierReleasePointer request.</pre></dl><dl COMPACT><dd><pre>If the pointer is not currently blocked by the barrier or the barrier
event sequence has ended, this request does nothing.</pre></dl><dl COMPACT><dd><pre>XIBarrierReleasePointer and XIBarrierReleasePointers can generate a
BadDevice or BadValue error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist or is not a master pointer device.</pre></dl><dl COMPACT><dd><pre>BadValue
 A value for a PointerBarrier argument does not name a defined
 pointer barrier.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XFixesCreatePointerBarrier/">XFixesCreatePointerBarrier</a>(3)</pre></dl>
