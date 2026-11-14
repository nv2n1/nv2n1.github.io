---
title: "xdevicebell(3)"
name: "xdevicebell"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdevicebell/"
---

XDeviceBell - ring a bell on a device supported through the input extension 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>Status XDeviceBell( Display *display,
 XDevice *device,
 XID feedbackclass,
 XID feedbackid,
 int percent);
display
 Specifies the connection to the X server.</pre><pre>device
 Specifies the device with which the bell is associated.</pre><pre>feedbackclass
 Specifies the class of the feedback with which the bell
 is associated.</pre><pre>feedbackid
 Specifies the id of the feedback with which the bell is
 associated.</pre><pre>percent
 Specifies the volume in the range -100 to 100 at which
 the bell should be rung.</pre><h2>Description</h2><dl COMPACT><dd><pre>The XDeviceBell request causes the server to ring a bell on the
specified feedback of the specified device, if possible. The
specified volume is relative to the base volume for the bell.
If an invalid device is specified, a BadDevice error will be
returned. The feedbackclass and feedbackid parameters contain
values returned by an XGetFeedbackControl request and uniquely
identify the bell to ring. If a feedbackclass is specified that
does not support a bell, or if a nonexistent feedbackid is
specified, or a percent value is specified that is not in the
range -100 to 100, a BadValue error will be returned.</pre></dl><dl COMPACT><dd><pre>The volume at which the bell is rung when the percent argument
is nonnegative is: base - [(base * percent) / 100] + percent</pre></dl><dl COMPACT><dd><pre>The volume at which the bell rings when the percent argument is
negative is: base + [(base * percent) / 100]</pre></dl><dl COMPACT><dd><pre>To change the base volume of the bell, use
XChangeFeedbackControl.</pre></dl><dl COMPACT><dd><pre>XDeviceBell can generate a BadDevice or a BadValue error.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The specified device
 does not exist, or has not been opened by this client
 via XOpenInputDevice.</pre></dl><dl COMPACT><dd><pre>BadValue
 An invalid feedbackclass, feedbackid, or percent value
 was specified.</pre></dl><h2>See Also</h2><dl COMPACT><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/3-XChangeFeedbackControl/">XChangeFeedbackControl</a>(3), <a HREF="//www.systutorials.com/docs/linux/man/3-XBell/">XBell</a>(3)</pre></dl>
