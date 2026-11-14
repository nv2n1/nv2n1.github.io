---
title: "xgetfeedbackcontrol(3)"
name: "xgetfeedbackcontrol"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetfeedbackcontrol/"
---

XGetFeedbackControl, XChangeFeedbackControl - query and change input device feedbacks 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput.h&gt;</pre><pre>XFeedbackState *XGetFeedbackControl( Display *display,
 XDevice *device,
 int *num_feedbacks);</pre><pre>int XChangeFeedbackControl( Display *display,
 XDevice *device,
 Mask mask,
 XFeedbackControl *control);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>device
 Specifies the device whose feedbacks are to be queried
 or modified.</pre><pre>num_feedbacks
 Specifies an address into which the number of feedbacks
 supported by thedevice is to be returned.</pre><pre>mask
 Specifies a mask specific to each type of feedback that
 describes howthe feedback is to be modified.</pre><pre>control
 Specifies the address of an XFeedbackControl structure
 that containsthe new values for the feedback.</pre><h2>Description</h2><dl COMPACT><dd><pre>These requests are provided to manipulate those input devices
that support feedbacks. A BadMatch error will be generated if
the requested device does not support feedbacks. Whether or not
a given device supports feedbacks can be determined by
examining the information returned by the XOpenDevice request.
For those devices that support feedbacks, XOpenDevice will
return an XInputClassInfo structure with the input_class field
equal to the constant FeedbackClass (defined in the file XI.h).</pre></dl><dl COMPACT><dd><pre>The XGetFeedbackControl request returns a pointer to a list of
XFeedbackState structures. Each item in this list describes one
of the feedbacks supported by the device. The items are
variable length, so each contains its length to allow traversal
to the next item in the list.</pre></dl><dl COMPACT><dd><pre>The feedback classes that are currently defined are:
KbdFeedbackClass, PtrFeedbackClass, StringFeedbackClass,
IntegerFeedbackClass, LedFeedbackClass, and BellFeedbackClass.
These constants are defined in the file XI.h. An input device
may support zero or more classes of feedback, and may support
multiple feedbacks of the same class. Each feedback contains a
class identifier and an id that is unique within that class for
that input device. The id is used to identify the feedback when
making an XChangeFeedbackControl request.</pre></dl><dl COMPACT><dd><pre>XGetFeedbackControl can generate a BadDevice or BadMatch error.</pre></dl><dl COMPACT><dd><pre>The XChangeFeedbackControl request modifies the values of one
feedback on the specified device. The feedback is identified by
the id field of the XFeedbackControl structure that is passed
with the request. The fields of the feedback that are to be
modified are identified by the bits of the mask that is passed
with the request.</pre></dl><dl COMPACT><dd><pre>XChangeFeedbackControl can generate a BadDevice, BadMatch, or
BadValue error.</pre></dl><h3>Structures</h3><dl COMPACT><dd><pre>Each class of feedback is described by a structure specific to
that class. These structures are defined in the file XInput.h.
XFeedbackState and XFeedbackControl are generic structures that
contain three fields that are at the beginning of each class of
feedback:</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
} XFeedbackState, XFeedbackControl;</pre></dl><dl COMPACT><dd><pre>The XKbdFeedbackState structure defines the attributes that are
returned for feedbacks equivalent to those on the X keyboard.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int click;
 int percent;
 int pitch;
 int duration;
 int led_mask;
 int global_auto_repeat;
 char auto_repeats[32];
} XKbdFeedbackState;</pre></dl><dl COMPACT><dd><pre>The XPtrFeedbackState structure defines the attributes that are
returned for feedbacks equivalent to those on the the X
pointer.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int accelNum;
 int accelDenom;
 int threshold;
} XPtrFeedbackState;</pre></dl><dl COMPACT><dd><pre>The XIntegerFeedbackState structure defines attributes that are
returned for integer feedbacks.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int resolution;
 int minVal;
 int maxVal;
} XIntegerFeedbackState;</pre></dl><dl COMPACT><dd><pre>The XStringFeedbackState structure defines the attributes that
are returned for string feedbacks.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int max_symbols;
 int num_syms_supported;
 KeySym *syms_supported;
} XStringFeedbackState;</pre></dl><dl COMPACT><dd><pre>The XBellFeedbackState structure defines the attributes that
are returned for bell feedbacks.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int percent;
 int pitch;
 int duration;
} XBellFeedbackState;</pre></dl><dl COMPACT><dd><pre>The XLedFeedbackState structure defines the attributes that are
returned for LED feedbacks.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int led_values;
} XLedFeedbackState;</pre></dl><dl COMPACT><dd><pre>The XPrtFeedbackControl structure defines the attributes that
can be controlled for pointer feedbacks.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int accelNum;
 int accelDenom;
 int threshold;
} XPtrFeedbackControl;</pre></dl><dl COMPACT><dd><pre>The XKbdFeedbackControl structure defines the attributes that
can be controlled for keyboard feedbacks.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int click;
 int percent;
 int pitch;
 int duration;
 int led_mask;
 int led_value;
 int key;
 int auto_repeat_mode;
} XKbdFeedbackControl;</pre></dl><dl COMPACT><dd><pre>The XStringFeedbackControl structure defines the attributes
that can be controlled for string feedbacks.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int num_keysyms;
 KeySym *syms_to_display;
} XStringFeedbackControl;</pre></dl><dl COMPACT><dd><pre>The XIntegerFeedbackControl structure defines the attributes
that can be controlled for integer feedbacks.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int int_to_display;
} XIntegerFeedbackControl;</pre></dl><dl COMPACT><dd><pre>The XBellFeedbackControl structure defines the attributes that
can be controlled for bell feedbacks.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int percent;
 int pitch;
 int duration;
} XBellFeedbackControl;</pre></dl><dl COMPACT><dd><pre>The XLedFeedbackControl structure defines the attributes that
can be controlled for LED feedbacks.</pre></dl><dl COMPACT><dd><pre>typedef struct {
 XID class;
 int length;
 XID id;
 int led_mask;
 int led_values;
} XLedFeedbackControl;</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The specified device
 does not exist or has not been opened by this client via
 XOpenInputDevice. This error may also occur if some
 other client has caused the specified device to become
 the X keyboard or X pointer device via the
 XChangeKeyboardDevice or XChangePointerDevice requests.</pre></dl><dl COMPACT><dd><pre>BadMatch
 This error may occur if an XGetFeedbackControl request
 was made specifying a device that has no feedbacks, or
 an XChangeFeedbackControl request was made with an
 XFeedbackControl structure that contains an invalid
 feedback type. It may also occur if an invalid
 combination of mask bits is specified ( DvKey but no
 DvAutoRepeatMode for keyboard feedbacks), or if an
 invalid KeySym is specified for a string feedback.</pre></dl><dl COMPACT><dd><pre>BadValue
 Some numeric value falls outside the range of values
 accepted by the XChangeFeedbackControl request. Unless a
 specific range is specified for an argument, the full
 range defined by the argument's type is accepted. Any
 argument defined as a set of alternatives can generate
 this error.</pre></dl>
