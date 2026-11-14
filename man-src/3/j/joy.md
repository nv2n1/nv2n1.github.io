---
title: "joy(3)"
name: "joy"
section: "3"
letter: "j"
url: "/docs/linux/man/3-joy/"
description: "joy – Global array of joystick state information. Allegro game programming library."
---

<h2>NAME</h2>
<p> joy &#8211; Global array of joystick state information. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern JOYSTICK_INFO joy[n];</code></p>
<h2>DESCRIPTION</h2>
<p> Global array of joystick state information, which is updated by the poll_joystick() function. Only the first num_joysticks elements will contain meaningful information. The JOYSTICK_INFO structure is defined as: </p>
<pre><code>
typedef struct JOYSTICK_INFO {
    int flags;                       - status flags for this
                                         joystick
      int num_sticks;
    - how many stick inputs ? int num_buttons;
    - how many buttons      ? JOYSTICK_STICK_INFO stick[n];
    - stick state information
        JOYSTICK_BUTTON_INFO button[n];
    - button state information
} JOYSTICK_INFO;
</code></pre>
<p> The button status is stored in the structure: </p>
<p>typedef struct JOYSTICK_BUTTON_INFO {<br />
    int b;<br />
    &#8211; boolean on / off flag char *name;<br />
    &#8211; description of this button<br />
} JOYSTICK_BUTTON_INFO;<br />
 You may wish to display the button names as part of an input configuration screen to let the user choose what game function will be performed by each button, but in simpler situations you can safely assume that the first two elements in the button array will always be the main trigger controls. </p>
<p> Each joystick will provide one or more stick inputs, of varying types. These can be digital controls which snap to specific positions (eg. a gamepad controller, the coolie hat on a Flightstick Pro or Wingman Extreme, or a normal joystick which hasn&#8217;t yet been calibrated), or they can be full analogue inputs with a smooth range of motion. Sticks may also have different numbers of axes, for example a normal directional control has two, but the Flightstick Pro throttle is only a single axis, and it is possible that the system could be extended in the future to support full 3d controllers. A stick input is described by the structure: </p>
<p>typedef struct JOYSTICK_STICK_INFO {<br />
    int flags;                       &#8211; status flags for this<br />
                                         input<br />
      int num_axis;<br />
    &#8211; how many axes do we<br />
        have<br />
        ? (note the misspelling)<br />
              JOYSTICK_AXIS_INFO axis[n];<br />
    &#8211; axis state information char *name;<br />
    &#8211; description of this input<br />
} JOYSTICK_STICK_INFO;<br />
 A single joystick may provide several different stick inputs, but you can safely assume that the first element in the stick array will always be the main directional controller. </p>
<p> Information about each of the stick axis is stored in the substructure: </p>
<pre><code>
typedef struct JOYSTICK_AXIS_INFO {
    int pos;
    - analogue axis position int d1, d2;
    - digital axis position char *name;
    - description of this axis
} JOYSTICK_AXIS_INFO;
</code></pre>
<p> This provides both analogue input in the pos field (ranging from -128 to 128 or from 0 to 255, depending on the type of the control), and digital values in the d1 and d2 fields. For example, when describing the X-axis position, the pos field will hold the horizontal position of the joystick, d1 will be set if it is moved left, and d2 will be set if it is moved right. Allegro will fill in all these values regardless of whether it is using a digital or analogue joystick, emulating the pos field for digital inputs by snapping it to the min, middle, and maximum positions, and emulating the d1 and d2 values for an analogue stick by comparing the current position with the centre point. </p>
<p> The joystick flags field may contain any combination of the bit flags: </p>
<p> <code>JOYFLAG_DIGITAL</code> This control is currently providing digital input. </p>
<p> <code>JOYFLAG_ANALOGUE</code> This control is currently providing analogue input. </p>
<p> <code>JOYFLAG_CALIB_DIGITAL</code> This control will be capable of providing digital input once it has been calibrated, but is not doing this at the moment. </p>
<p> <code>JOYFLAG_CALIB_ANALOGUE</code> This control will be capable of providing analogue input once it has been calibrated, but is not doing this at the moment. </p>
<p> <code>JOYFLAG_CALIBRATE</code> Indicates that this control needs to be calibrated. Many devices require multiple calibration steps, so you should call the calibrate_joystick() function from a loop until this flag is cleared. </p>
<p> <code>JOYFLAG_SIGNED</code> Indicates that the analogue axis position is in signed format, ranging from -128 to 128. This is the case for all 2d directional controls. </p>
<p> <code>JOYFLAG_UNSIGNED</code> Indicates that the analogue axis position is in unsigned format, ranging from 0 to 255. This is the case for all 1d throttle controls. </p>
<p> Note for people who spell funny: in case you don&#8217;t like having to type &quot;analogue&quot;, there are some #define aliases in allegro/joystick.h that will allow you to write &quot;analog&quot; instead. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_joystick/">install_joystick</a></code>(3), <code><a href="/docs/linux/man/3-poll_joystick/">poll_joystick</a></code>(3), <code><a href="/docs/linux/man/3-num_joysticks/">num_joysticks</a></code>(3), <code><a href="/docs/linux/man/3-calibrate_joystick/">calibrate_joystick</a></code>(3), <code><a href="/docs/linux/man/3-calibrate_joystick_name/">calibrate_joystick_name</a></code>(3), <code><a href="/docs/linux/man/3-exjoy/">exjoy</a></code>(3) </p>
<h2>Index</h2>
