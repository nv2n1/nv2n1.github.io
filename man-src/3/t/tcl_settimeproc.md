---
title: "tcl_settimeproc(3)"
name: "tcl_settimeproc"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_settimeproc/"
description: "Tcl_GetTime, Tcl_SetTimeProc, Tcl_QueryTimeProc – get date and time"
---

<p>Tcl_GetTime, Tcl_SetTimeProc, Tcl_QueryTimeProc &#8211; get date and time </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_GetTime</code>(<i>timePtr</i>)
<code>Tcl_SetTimeProc</code>(<i>getProc, scaleProc, clientData</i>)
<code>Tcl_QueryTimeProc</code>(<i>getProcPtr, scaleProcPtr, clientDataPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Time * <i>timePtr</i> (out) Points to memory in which to store the date and time information.</p>
<dd>Tcl_GetTimeProc * <i>getProc</i> (in) Pointer to handler function replacing <code>Tcl_GetTime</code>&#8216;s access to the OS.</p>
<dd>Tcl_ScaleTimeProc * <i>scaleProc</i> (in) Pointer to handler function for the conversion of time delays in the virtual domain to real-time.</p>
<dd>ClientData * <i>clientData</i> (in) Value passed through to the two handler functions.</p>
<dd>Tcl_GetTimeProc ** <i>getProcPtr</i> (inout) Pointer to place the currently registered get handler function into.</p>
<dd>Tcl_ScaleTimeProc ** <i>scaleProcPtr</i> (inout) Pointer to place the currently registered scale handler function into.</p>
<dd>ClientData ** <i>clientDataPtr</i> (inout) Pointer to place the currently registered pass-through value into.
</dl>
<h2>Description</h2>
<p>The <code>Tcl_GetTime</code> function retrieves the current time as a <i>Tcl_Time</i> structure in memory the caller provides. This structure has the following definition:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_Time {
 long sec;
 long usec;
} Tcl_Time;</pre>
</dl>
<p> On return, the <i>sec</i> member of the structure is filled in with the number of seconds that have elapsed since the <i>epoch:</i> the epoch is the point in time of 00:00 UTC, 1 January 1970. This number does <i>not</i> count leap seconds &#8211; an interval of one day advances it by 86400 seconds regardless of whether a leap second has been inserted. </p>
<p> The <i>usec</i> member of the structure is filled in with the number of microseconds that have elapsed since the start of the second designated by <i>sec</i>. The Tcl library makes every effort to keep this number as precise as possible, subject to the limitations of the computer system. On multiprocessor variants of Windows, this number may be limited to the 10- or 20-ms granularity of the system clock. (On single-processor Windows systems, the <i>usec</i> field is derived from a performance counter and is highly precise.) </p>
<p> The <code>Tcl_SetTime</code> function registers two related handler functions with the core. The first handler function is a replacement for <code>Tcl_GetTime</code>, or rather the OS access made by <code>Tcl_GetTime</code>. The other handler function is used by the Tcl notifier to convert wait/block times from the virtual domain into real time. </p>
<p> The <code>Tcl_QueryTime</code> function returns the currently registered handler functions. If no external handlers were set then this will return the standard handlers accessing and processing the native time of the OS. The arguments to the function are allowed to be NULL; and any argument which is NULL is ignored and not set. </p>
<p> Any handler pair specified has to return data which is consistent between them. In other words, setting one handler of the pair to something assuming a 10-times slowdown, and the other handler of the pair to something assuming a two-times slowdown is wrong and not allowed. </p>
<p> The set handler functions are allowed to run the delivered time backwards, however this should be avoided. We have to allow it as the native time can run backwards as the user can fiddle with the system time one way or other. Note that the insertion of the hooks will not change the behaviour of the Tcl core with regard to this situation, i.e. the existing behaviour is retained.</p>
<h2>See Also</h2>
<p>clock</p>
<h2>Keywords</h2>
<p>date, time</p>
