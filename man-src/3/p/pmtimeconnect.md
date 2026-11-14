---
title: "pmtimeconnect(3)"
name: "pmtimeconnect"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmtimeconnect/"
description: "pmtime, pmTimeConnect, pmTimeDisconnect, pmTimeRecv, pmTimeSendAck, pmTimeShowDialog – time control functions for synchronizing the archive position and update interval between one or more applicat..."
---

<p><code>pmtime</code>, <code>pmTimeConnect</code>, <code>pmTimeDisconnect</code>, <code>pmTimeRecv</code>, <code>pmTimeSendAck</code>, <code>pmTimeShowDialog</code> &#8211; time control functions for synchronizing the archive position and update interval between one or more applications</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmtime.h&gt; </p>
<p> int pmTimeConnect(int </code><i>port</i>, pmTime *<i>state</i>);<br />
 int pmTimeDisconnect(int <i>fd</i>);<br />
 int pmTimeSendAck(int <i>fd</i>, struct timeval *<i>fetchTime</i>);<br />
 int pmTimeShowDialog(int <i>fd</i>, int <i>show</i>);<br />
 int pmTimeRecv(int <i>fd</i>, pmTime *<i>state</i>); </p>
<p> cc &#8230; -lpcp_gui</p>
<h2>Description</h2>
<p>These functions form part of the Performance Metrics Applications Programming Interface (PMAPI) and are intended to provide a uniform mechanism for applications to both replay archive data and report live data in a time synchronized manner. </p>
<p> The <i>pmTime</i> structure has the following fields: </p>
<pre>typedef struct {
 unsigned int magic;
 unsigned int length;
 pm_tctl_command command;
 pm_tctl_source source;
 pm_tctl_state state;
 pm_tctl_mode mode;
 struct timeval delta;
 struct timeval position;
 struct timeval start; /* archive only */
 struct timeval end; /* archive only */
 char data[0]; /* arbitrary length info (TZ) */
} pmTime;</pre>
<p>In the simplest case, the application should call <code>pmTimeConnect</code> to connect to the time control server, <code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1), and then repeatedly call <code>pmTimeRecv</code> in the main loop of the application. On success, <code>pmTimeConnect</code> returns a non-negative file descriptor. In applications which have multiple threads of control, rather than simply blocking in <code>pmTimeRecv</code>, the file descriptor may be used in calls to <code><a href="/docs/linux/man/2-select/">select</a></code>(2). In graphical applications, the file descriptor may be used to interface with the event loop. </p>
<p> The <i>port</i> parameter to <code>pmTimeConnect</code> is the port number of the socket on which the time control server is (or will be) listening for new connections. </p>
<p> The state parameter to <code>pmTimeConnect</code> is used to initialize a new time control server or to pass additional information to an existing time control server. The <i>start</i> and <i>finish</i> fields indicate the chronological bounds interesting to the application. The <i>showdialog</i> field indicates whether the time control server should initially show or hide the dialog. The <i>position</i>, <i>delta,</i> and <i>data</i> fields indicate the initial archive position, update interval, time zone string and time zone label string. </p>
<p> <code>pmTimeRecv</code> blocks until the time control server sends a command message. It then updates the state parameter and returns one of the PM_TCTL command identifiers. </p>
<p> The PM_TCTL_SET command indicates the application should seek to the archive position (see <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3)) returned in the position field of the state parameter. </p>
<p> The PM_TCTL_STEP command indicates the application should perform an update, i.e. advance (or rewind, if delta is negative) to the time indicated by position and then fetch new metric values, update the display or whatever. In order for several application to remain synchronized, the time control server will wait until all applications have acknowledged that they have completed the step command. Applications should call pmTimeSendAck when the step command has been processed. Note that PM_TCTL_STEP is the only command that requires an explicit acknowledgement. </p>
<p> The PM_TCTL_VCRMODE command is used by the time control server to indicate the current VCR mode. </p>
<p> The value is returned in the vcrmode field of the state parameter passed to <code>pmTimeRecv</code>, and remains valid until the next PM_TCTL_VCRMODE command is received. </p>
<p> The PM_TCTL_TZ command indicates the application should use a new time- zone, as indicated in the <i>tz</i> and <i>tzlabel</i> fields of the state parameter. </p>
<p> The PM_TCTL_BOUNDS command is sent to all applications when the time control server changes its chronological bounds. This may occur when a new application connects to the time control server or the user changes the bounds manually. Most applications will ignore this command. </p>
<p> The PM_TCTL_SHOWDIALOG command will be sent to all applications when the visibility of the time control server changes. This allows applications to alter the text in menus or buttons to reflect this change. Applications may change the visibility of the time control dialog using the <code>pmTimeShowDialog</code> function. The initial visibility is determined when the time control dialog is first created by an application calling <code>pmTimeConnect</code> with the showdialog field in the state parameter set to the desired value. </p>
<p> The <code>pmTimeDisconnect</code> function may be used to close the command socket to the time control server. This is useful when applications need to change the connection mode, e.g. to divorce the current time control server and connect to a new one.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmtime/">pmtime</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3). </p>
