---
title: "xboxdrv(1)"
name: "xboxdrv"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xboxdrv/"
description: "xboxdrv – A Xbox/Xbox360 gamepad driver that works in userspace"
---

<h2>NAME</h2>
<p> xboxdrv &#8211; A Xbox/Xbox360 gamepad driver that works in userspace</p>
<h2>SYNOPSIS</h2>
<p> <code>xboxdrv</code> [OPTION]&#8230; [&#8211;] [COMMAND] [ARGUMENTS]</p>
<h2>DESCRIPTION</h2>
<p> <code>xboxdrv</code> is a driver for Xbox and Xbox360 gamepads. It works by reading the raw data from the controller with the userspace library libusb and then passes the interpreted data to the kernel via uinput. This allows <code>xboxdrv</code> to provide regular joystick and event devices, which makes it compatible with all Linux software. </p>
<p> Aside from the pure driver, <code>xboxdrv</code> also includes a rich set of configuration options that allow you to tweak the abilities of the virtual input devices that xboxdrv will create. This includes basic button and axis remapping, as well as more complicated things like mouse and keyboard emulation, auto-fire and throttle control emulation. </p>
<p> It is also possible for <code>xboxdrv</code> to read input data directly from an event device, this allows the use of the configurability of <code>xboxdrv</code> on regular PC joysticks, keyboards and mice and thus lets <code>xboxdrv</code> serve a similar purpose as <code>joy2key</code>. See the option <code>&#8211;evdev</code> below for more information. </p>
<p> When a <code>COMMAND</code> is provided xboxdrv will launch that application and be running till that application exits. This is a convenience function to make it easier to use xboxdrv in wrapper scripts. See the section [Writing Start-Up Scripts for Games] for more information.</p>
<h2>OPTIONS</h2>
<h3>GENERAL OPTIONS</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display help text and exit.</p>
<dt>-V, &#8211;version</p>
<dd> Print the version number and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Print verbose messages.</p>
<dt><code>&#8211;debug</code></p>
<dd> Print even more verbose messages then <code>&#8211;verbose</code>.</p>
<dt><code>-s</code>, <code>&#8211;silent</code></p>
<dd> Do not display controller events on the terminal. For regular use this option should always be used as output data to the terminal can eat up quite a bit of CPU.</p>
<dt><code>&#8211;quiet</code></p>
<dd> Do not display startup text and suppress most other output.</p>
<dt><code>&#8211;priority</code> <i>PRIORITY</i></p>
<dd> Possible values for <i>PRIORITY</i> are &quot;normal&quot; and &quot;realtime&quot;. Realtime scheduling gives the xboxdrv process higher priority and thus allows it to function properly even when the machine is under load. </p>
<p> Note that realtime priority requires running xboxdrv as root, when running xboxdrv as user there is no way to increase the priority. </p>
<p> This option is deprecated, use <code><a href="/docs/linux/man/1-chrt/">chrt</a></code>(1) instead to achive the same effect.</dl>
<h3>LIST OPTIONS</h3>
<dl>
<dt><code>&#8211;help-led</code></p>
<dd> List possible values for the led.</p>
<dt><code>&#8211;help-devices</code></p>
<dd> List supported devices.</p>
<dt><code>&#8211;list-supported-devices</code></p>
<dd> List supported devices (used by xboxdrv-daemon.py).</p>
<dt><code>&#8211;list-supported-devices-xpad</code></p>
<dd> List supported devices in <i>xpad.c</i> style.</p>
<dt><code>&#8211;help-abs</code></p>
<dd> List all allowed EV_ABS symbols.</p>
<dt><code>&#8211;help-rel</code></p>
<dd> List all allowed EV_REL symbols.</p>
<dt><code>&#8211;help-key</code></p>
<dd> List all allowed EV_KEY symbols.</p>
<dt><code>&#8211;help-x11keysym</code></p>
<dd> List all allowed X11 Keysym symbols.</p>
<dt><code>&#8211;help-axis</code></p>
<dd> List all allowed XboxAxis symbols.</p>
<dt><code>&#8211;help-button</code></p>
<dd> List all allowed XboxButton symbols.</p>
<dt><code>&#8211;help-all</code></p>
<dd> List all symbols that can be used in <code>&#8211;ui-buttonmap</code>, <code>&#8211;ui-axismap</code>, <code>&#8211;buttonmap</code> and <code>&#8211;axismap</code>. This option is the same as <code>&#8211;help-abs</code>, <code>&#8211;help-rel</code>, <code>&#8211;help-key</code>, <code>&#8211;help-x11keysym</code>, <code>&#8211;help-axis</code> and <code>&#8211;help-button</code>.</dl>
<h3>CONFIG FILE OPTIONS</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;config</code> <i>FILE</i></p>
<dd> Reads configuration information from <i>FILE</i>. Configurations from file are handling as if they would be command line options at the position of <code>&#8211;config</code> <i>FILE</i>. </p>
<p> The syntax of <i>FILE</i> is the familiar INI syntax used for many configuration files. Regular key/value pairs must go into the [xboxdrv] section. &#8216;#&#8217; and &#8216;;&#8217; can be used for comments. Key names have for most part the same name as command line options. Command line options that take a list of input mappings (&#8211;ui-buttonmap, &#8211;ui-axismap, &#8211;evdev-absmap, &#8230;) can be split of into their own section for better readability. </p>
<p> The <i>examples/</i> directory contains some example configuration files. </p>
<pre><code>
[xboxdrv] silent = true deadzone = 6000 dpad - as - button = true trigger - as - button = true
                                                                 [ui - axismap] x2 = REL_X : 10 y2 = REL_Y : -10 x1 = KEY_A : KEY_D
                                                                                                                                  y1 = KEY_W : KEY_S
                                                                                                                                                   [ui - buttonmap] a = KEY_LEFTSHIFT
                                                                                                                                                       b = BTN_C
                                                                                                                                                           x = BTN_EXTRA
                                                                                                                                                               y = KEY_C
                                                                                                                                                                   [ui - buttonmap] lb = BTN_RIGHT
                                                                                                                                                                       rb = KEY_SPACE
                                                                                                                                                                           [ui - buttonmap] lt = KEY_Z
                                                                                                                                                                               rt = BTN_LEFT
                                                                                                                                                                                   [ui - buttonmap] dl = KEY_4
                                                                                                                                                                                       dr = KEY_2
                                                                                                                                                                                           du = REL_WHEEL : -1 : 150 dd = REL_WHEEL : 1 : 150
                                                                                                                                                                                                                [ui - buttonmap] back = KEY_TAB
                                                                                                                                                                                                                    start = KEY_ESC
#EOF #
</code></pre>
<dt><code>&#8211;alt-config</code> <i>FILE</i></p>
<dd> A shortcut for writing <code>&#8211;next-config</code> <code>&#8211;config</code> <i>FILE</i>. </p>
<p> To load multiple configuration options use: </p>
<pre>
xboxdrv --config first.ini --alt-config second.ini --alt-config third.ini
</pre>
<dt><code>-o</code>, <code>&#8211;option</code> <i>NAME=VALUE</i></p>
<dd> Set an option as if it would come from a config file from the command line.</p>
<dt><code>&#8211;write-config</code> <i>FILE</i></p>
<dd> Write an example configuration file to <i>FILE</i>.</dl>
<h3>DAEMON OPTIONS</h3>
<dl>
<dt><code>-D</code>, <code>&#8211;daemon</code></p>
<dd> Run xboxdrv as daemon. If this option is given xboxdrv will listen to udev for USB connection events and launch driver threads for newly connected controllers. </p>
<p> Configuration options can still be supplied as usual. Note however that xboxdrv when run as daemon will not create new uinput devices on demand, instead it will only create devices once at startup for the given configurations and then assign new controllers to these configurations. While this means xboxdrv can&#8217;t support an unlimited number of controllers, it also means that xboxdrv can allow hot plugging even for applications that don&#8217;t support it themselves, as applications will only see the permanent device files, not the controller that xboxdrv will change around under the hood. </p>
<p> An example configuration that supports three controller would look like this: </p>
<p>xboxdrv &#8211;daemon \<br />
    # config options for the first controller<br />
  &#8211;next-controller \<br />
    # config options for the second controller<br />
  &#8211;next-controller<br />
#config options for the third controller</p>
<p> The <code>&#8211;match</code> option can be used to limit the controller slots to only those controllers that match the given RULE and thus be used to assign configurations only to specific controllers.</p>
<dt><code>&#8211;detach</code></p>
<dd> Detaches xboxdrv from the current shell, only valid if <code>&#8211;daemon</code> is given.</p>
<dt><code>&#8211;pid-file</code> <i>FILE</i></p>
<dd> Write the xboxdrv daemon process id to FILE.</p>
<dt><code>&#8211;dbus</code> <i>BUS</i></p>
<dd> Set which bus type xboxdrv should connect to. Allowed values for BUS are session, system, disabled and auto. The default is auto, which will detect the appropriate bus type depending on if xboxdrv is run as root (system or as user (session). Running with disabled will disable D-Bus support completely.</p>
<dt><code>&#8211;on-connect</code> <i>EXE</i></p>
<dd> Launches <i>EXE</i> when a controller gets connected. As arguments &quot;<i>BUSDEV</i>:<i>DEVNUM</i>&quot;, &quot;<i>idVendor</i>:<i>idProduct</i>&quot;, &quot;<i>NAME</i> are provided.</p>
<dt><code>&#8211;on-disconnect</code> <i>EXE</i></p>
<dd> Launches <i>EXE</i> when a controller gets disconnected. As arguments &quot;<i>BUSDEV</i>:<i>DEVNUM</i>&quot;, &quot;<i>idVendor</i>:<i>idProduct</i>&quot;, &quot;<i>NAME</i> are provided.</dl>
<h3>DEVICE OPTIONS</h3>
<dl>
<dt><code>-L</code>, <code>&#8211;list-controller</code></p>
<dd> List available controllers on the system.</p>
<dt><code>-i</code>, <code>&#8211;id</code> <i>N</i></p>
<dd> Use controller with id N (default: 0), use <code>&#8211;list-controller</code> to obtain a list of available controller.</p>
<dt><code>-w</code>, <code>&#8211;wid</code> <i>N</i></p>
<dd> Use wireless controller with wid N (default: 0).</p>
<dt><code>&#8211;device-by-path</code> <i>BUS:DEV</i></p>
<dd> Use the controller at BUS:DEV, do not do any automatic scanning. Useful for cases when a controller isn&#8217;t known by xboxdrv, but supports one of the given protocols.</p>
<dt><code>&#8211;device-by-id</code> <i>VENDOR:PRODUCT</i></p>
<dd> Use device that matches VENDOR:PRODUCT (as returned by <code>lsusb</code>). Useful for cases when a controller isn&#8217;t known by xboxdrv, but supports one of the given protocols.</p>
<dt><code>&#8211;type</code> <i>TYPE</i></p>
<dd> Ignore autodetection and enforce the controller type. Possible values for <i>TYPE</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> xbox</p>
<dt>&bull;</p>
<dd> xbox-mat</p>
<dt>&bull;</p>
<dd> xbox360</p>
<dt>&bull;</p>
<dd> xbox360-wireless</p>
<dt>&bull;</p>
<dd> xbox360-guitar</p>
<dt>&bull;</p>
<dd> firestorm</p>
<dt>&bull;</p>
<dd> firestorm-vsb</p>
<dt>&bull;</p>
<dd> saitek-p2500</p>
<dt>&bull;</p>
<dd> generic-usb</dl>
</dl>
<p> The <code>generic-usb</code> type is a special type that will work with any USB controller, it will however not interpret the input it gets, but just dump it to the console for development purposes. See <code>&#8211;generic-usb-spec</code> for further information.</p>
<dt><code>-d</code>, <code>&#8211;detach-kernel-driver</code></p>
<dd> Detaches the kernel driver that is currently associated with the given device. This is useful when you have the xpad module loaded and want to use xboxdrv without unloading it.</p>
<dt><code>&#8211;generic-usb-spec</code> <i>NAME=VALUE,&#8230;</i></p>
<dd> Allows to specify from which endpoint <code>generic-usb</code> will read. The spec as the form of <i>NAME=VALUE,&#8230;</i>. Allowed values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>vid=HEX</p>
<dd> The vendor id of the controller to which this spec applies</p>
<dt>pid=HEX</p>
<dd> The product id of the controller to which this spec applies</p>
<dt>if=NUM</p>
<dd> The interface from which GenericUSBController should be read</p>
<dt>ep=NUM</p>
<dd> The endpoint from which GenericUSBController should be read</dl>
</dl>
</dl>
<h3>EVDEV OPTION</h3>
<dl>
<dt><code>&#8211;evdev</code> <i>DEVICE</i></p>
<dd> Allows you to read input data from a regular event device. This allows you to use <code>xboxdrv</code> on regular PC joysticks. The data that is read from the event device is converted internally into a XboxMsg object and then passed through the same configuration pipeline as it would be for a regular Xbox360 controller. This allows you to make use of all the regular configurability, but limits you to the number of axis and buttons that an Xbox360 controller provides. </p>
<p> As a regular PC joystick will most likely already create a <i>/dev/input/jsX</i> device by itself, you might need to get rid of that so that a game will properly detect the joystick device created by <code>xboxdrv</code>. The easiest way to accomplish that is to simply delete the old joystick and rename the device that <code>xboxdrv</code> created to <i>/dev/input/js0</i>. When you use udev, this operation should be harmless and automatically reverse itself when you remove the controller and plug it back in or when you reboot the computer.</p>
<dt><code>&#8211;evdev-debug</code></p>
<dd> The evdev event handler will print all received events to stdout, this makes it easy to see which events a given controller sends.</p>
<dt><code>&#8211;evdev-no-grab</code></p>
<dd> By default the evdev driver will grab the device, thus making it impossible for other applications to receive events from that device. This is done to avoid confusing applications, as otherwise an app would receive every event twice, once from the original device and once from the virtual xboxdrv one. In some cases this behaviour is undesired, such when mapping only an otherwise unhandled subset of keys of an device, i.e. mapping the multimedia keys on a keyboard, so this option turns the grab off.</p>
<dt><code>&#8211;evdev-absmap</code> <i>ABSMAP,&#8230;</i></p>
<dd>
<pre>
ABSMAP = EVDEV_ABS [ &quot;+&quot;, &quot;-&quot; ] &quot;=&quot; XBOXAXIS ;
</pre>
<p> Sets how evdev events are mapped to Xbox axis events. An example configuration would look like this: </p>
<pre>
--evdev-absmap ABS_X=x1,ABS_Y=y1,ABS_RZ=x2,ABS_THROTTLE=y2,ABS_HAT0X=dpad_x,ABS_HAT0Y=dpad_y
</pre>
<p> <code>xboxdrv</code> will output on startup a full list of event names that the given event device supports and that can be used in place of <i>EVDEV_ABS</i>. </p>
<p> It is also possible to map half-axis with a command like: </p>
<pre>
--evdev-absmap ABS_Y+=LT,ABS_Y-=RT
</pre>
<p> This will map the upward movement of the Y axis to the left trigger and the downward movement to the right trigger.</p>
<dt><code>&#8211;evdev-keymap</code> <i>KEYMAP</i></p>
<dd> Sets how evdev events are mapped to Xbox controller events. An example configuration would look like this: </p>
<pre>
--evdev-keymap BTN_TRIGGER=a,BTN_THUMB=b,BTN_THUMB2=x
</pre>
<p> <code>xboxdrv</code> will output on start a full list of event names that the given event device supports.</dl>
<h3>STATUS OPTIONS</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;led</code> <i>NUM</i></p>
<dd> Set LED status. Possible values for <i>NUM</i> are: </p>
<p> <code>LED Status Codes</code> </p>
<table>
<tr VALIGN=top>
<td ALIGN=right> Num </td>
<td> Behavior
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 0 </td>
<td> off
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 1 </td>
<td> all blinking
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 2 </td>
<td> 1/top-left blink, then on
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 3 </td>
<td> 2/top-right blink, then on
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 4 </td>
<td> 3/bottom-left blink, then on
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 5 </td>
<td> 4/bottom-right blink, then on
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 6 </td>
<td> 1/top-left on
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 7 </td>
<td> 2/top-right on
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 8 </td>
<td> 3/bottom-left on
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 9 </td>
<td> 4/bottom-right on
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 10 </td>
<td> rotate
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 11 </td>
<td> blink
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 12 </td>
<td> blink slower
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 13 </td>
<td> rotate with two lights
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 14 </td>
<td> blink
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right> 15 </td>
<td> blink once
</td>
</tr>
</table>
<dt><code>&#8211;rumble-gain</code> <i>AMOUNT</i></p>
<dd> You can change the rumble strength via: </p>
<pre>
$ xboxdrv --rumble-gain 50%
</pre>
<p> Values larger then 100% are possible as well and will amplify small rumble commands, rumble commands already at the maximum will stay unchanged.</p>
<dt><code>-q</code>, <code>&#8211;quit</code></p>
<dd> Exit xboxdrv after setting LED or rumble values.</dl>
<h3>CHATPAD OPTIONS (EXPERIMENTAL)</h3>
<p> Chatpad support is still experimental. Basic keyboard usage will work, there is however currently no support for customization or the green and orange key modifiers. </p>
<p> Starting xboxdrv multiple times in a row with the <code>&#8211;chatpad</code> option can crash the controller. Unplugging it and plugging it back in should reset it.</p>
<dl>
<dt><code>&#8211;chatpad</code></p>
<dd> Enables the support for the Xbox360 Chatpad. WARNING: This is preliminary code, it will crash your gamepad when xboxdrv is started multiple times and won&#8217;t provide proper keymapping for any of the umlauts and special characters.</p>
<dt><code>&#8211;chatpad-no-init</code></p>
<dd> This will start chatpad support with out sending the init sequence, thus potentially avoiding crashing the controller if xboxdrv is started multiple times.</p>
<dt><code>&#8211;chatpad-debug</code></p>
<dd> Output raw chatpad data to the stdout for debugging purpose.</dl>
<h3>HEADSET OPTIONS (EXPERIMENTAL, XBOX360 USB ONLY)</h3>
<p> Xboxdrv does not support the headset, the options below are for developers only and will dump raw headset data, not .wav files.</p>
<dl>
<dt><code>&#8211;headset</code></p>
<dd> Enable headset support and dump incoming data to stdout.</p>
<dt><code>&#8211;headset-dump</code> <i>FILE</i></p>
<dd> Enable headset support and dump incoming data to FILE.</p>
<dt><code>&#8211;headset-play</code> <i>FILE</i></p>
<dd> Enable headset support and send FILE to the headset for playback.</dl>
<h3>FORCE FEEDBACK</h3>
<dl>
<dt><code>&#8211;force-feedback</code></p>
<dd> Enables the standard kernel force feedback interface. It is disabled by default as it causes trouble with some applications running in Wine. </p>
<p> Since the Xbox360 controller supports just rumble not full force feedback, xboxdrv tries to emulate other effects. This emulation hasn&#8217;t been tested much and might not always work as expected. Bug reports and test cases are welcome. </p>
<p> Note that you must close the application that is using force feedback always before you close the xboxdrv driver, else you might end up with a hanging non-interruptable xboxdrv process that will require a reboot to get rid of. </p>
<p> When using xboxdrv in daemon mode with multiple controller slots you have to enable force feedback for each slot separately.</p>
<dt><code>&#8211;ff-device</code> <i>DEVICEID</i></p>
<dd> Select to which virtual device the force-feedback callbacks will be connected to, it defaults to joystick. Other allowed values are mouse, keyboard and any integer number. See <code>&#8211;ui-buttonmap</code> for further information on how device-ids work.</p>
<dt><code>-R</code>, <code>&#8211;test-rumble</code></p>
<dd> Pressing LT will move the left rumble motor and pressing RT will move the right one. Rumble motor strength depends on how hard you press. This is useful for testing the rumble motors.</p>
<dt><code>-r</code>, <code>&#8211;rumble</code> <i>L,R</i></p>
<dd> Set the speed for both rumble motors. Values from 0 to 255 are accepted, the default is 0,0.</dl>
<h3>CONTROLLER SLOT OPTIONS</h3>
<p> Controller slots are used when running xboxdrv in daemon mode. Each slot represents a complete controller configuration. If you want to use multiple controller in daemon mode you have to supply multiple controller slots.</p>
<dl>
<dt><code>&#8211;controller-slot</code> <i>N</i></p>
<dd> Switches to the controller slot with the number N, numbering starts at zero.</p>
<dt><code>&#8211;next-controller</code></p>
<dd> Switches to the next controller slot.</p>
<dt><code>&#8211;match</code> <i>RULE,&#8230;</i></p>
<dd> Limits a controller slot to devices that match any one of the given rules. Possible match rules are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>usbid=<i>VENDOR</i>:<i>PRODUCT</i></p>
<dd> Match controllers that have the given USB vendor and product ids.</p>
<dt>vendor=<i>VENDOR</i></p>
<dd> Match controllers that have the given USB idVendor.</p>
<dt>product=<i>PRODUCT</i></p>
<dd> Match controllers that have the given USB idProduct.</p>
<dt>property=<i>PROPERTY</i>:<i>VALUE</i></p>
<dd> Match against an arbitrary udev property, with name <i>PROPERTY</i> and value <i>VALUE</i>.</p>
<dt>usbpath=<i>BUS</i>:<i>DEV</i></p>
<dd> Match against the USB path given by <i>BUS</i> and <i>DEV</i>.</p>
<dt>usbserial=<i>SERIAL</i></p>
<dd> Match against the USB iSerial number.</dl>
</dl>
<dt><code>&#8211;match-group</code> <i>RULE,&#8230;</i></p>
<dd> Limits a controller slot to devices that match all of the given rules. Possible match rules are the same as for <code>&#8211;match</code>.</dl>
<h3>CONFIG SLOT OPTIONS</h3>
<p> You can use multiple configurations, called config slots, with your controller. You switch between those multiple configurations by pressing the Guide button by default, but you can also set another button via the option <code>&#8211;toggle</code>.</p>
<dl>
<dt><code>&#8211;config-slot</code> <i>NUM</i></p>
<dd> Select the config slot <i>NUM</i>.</p>
<dt><code>&#8211;next-config</code></p>
<dd> Allows the creation of an alternative uinput configuration to which one can toggle at runtime by pressing the ui-toggle button (defaults to guide). </p>
<p>$ xboxdrv&#8211; mouse&#8211; next &#8211; config&#8211; ui &#8211; axismap X1 = ABS_X, Y1 = ABS_Y&#8211; ui &#8211; buttonmap A = JS_0, B = JS_1</p>
<p> The above configuration would install mouse emulation as first configuration and a simple joystick emulation as second configuration. Allowing toggling between mouse emulation and joystick handling by pressing the guide button. </p>
<p> Not that <code>&#8211;next-config</code> is currently limited to only configurations done with <code>&#8211;ui-buttonmap</code> and <code>&#8211;ui-axismap</code>, autofire, throttle emulation, deadzones and all other things can currently not be switched at runtime.</p>
<dt><code>&#8211;toggle</code> <i>XBOXBTN</i></p>
<dd> Sets the button that will be used to toggle between different different configurations. A value of &#8216;void&#8217; will disable the toggle button. If no toggle button is specified, the guide button will be used to toggle between configurations.</dl>
<h3>CONFIGURATION OPTIONS</h3>
<dl>
<dt><code>&#8211;modifier </code><i>MOD</i></p>
<dd> Add a modifier to the modifier stack, see [Modifier] for a full list of possible modifier.</p>
<dt><code>&#8211;timeout </code><i>MSEC</i></p>
<dd> Specify the number of miliseconds that xboxdrv will wait for events from the controller before moving on and processing things like auto-fire or relative-axis. Default value is 10, smaller values will give you a higher resolution auto fire and relative event movement, but will waste some more CPU.</p>
<dt><code>-b, &#8211;buttonmap BUTTON=BUTTON,&#8230;</code></p>
<dd> Button remapping is available via the <code>&#8211;buttonmap</code> option. If you want to swap button A and B start with: </p>
<pre>
$ xboxdrv --buttonmap A=B,B=A
</pre>
<p> If you want all face buttons send out A button events: </p>
<pre>
$ xboxdrv --buttonmap B=A,X=A,Y=A
</pre>
<p> Possible button names are (aliases are in parenthesis): </p>
<p> <code>Button Names</code> </p>
<table BORDER>
<tr VALIGN=top>
<td> Name </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td> start, back </td>
<td> start, back buttons
</td>
</tr>
<tr VALIGN=top>
<td> guide </td>
<td> big X-button in the middle (Xbox360 only)
</td>
</tr>
<tr VALIGN=top>
<td> <a href="/docs/linux/man/1-a/">a</a>(1), <a href="/docs/linux/man/2-b/">b</a>(2), <a href="/docs/linux/man/3-x/">x</a>(3), <a href="/docs/linux/man/4-y/">y</a>(4) </td>
<td> face buttons
</td>
</tr>
<tr VALIGN=top>
<td> black, white </td>
<td> black, white buttons (Xbox1 only, mapped to lb, rb on Xbox360)
</td>
</tr>
<tr VALIGN=top>
<td> <a href="/docs/linux/man/5-lb/">lb</a>(5), <a href="/docs/linux/man/6-rb/">rb</a>(6) </td>
<td> shoulder buttons (Xbox360 only, mapped to black, white on Xbox1)
</td>
</tr>
<tr VALIGN=top>
<td> <a href="/docs/linux/man/7-lt/">lt</a>(7), <a href="/docs/linux/man/8-rt/">rt</a>(8) </td>
<td> analog trigger (needs &#8211;trigger-as-button option)
</td>
</tr>
<tr VALIGN=top>
<td> tl, tr </td>
<td> pressing the left or right analog stick
</td>
</tr>
<tr VALIGN=top>
<td> du(up), dd(down), dl(left), dr(right) </td>
<td> dpad directions (needs &#8211;dpad-as-button option)
</td>
</tr>
<tr VALIGN=top>
<td> green, red, yellow, blue, orange </td>
<td> guitar buttons
</td>
</tr>
</table>
<p> Just like with <code>&#8211;ui-buttonmap</code> you can add button filter to each button.</p>
<dt><code>&#8211;axismap</code> <i>AXIS=MAPPING,&#8230;</i></p>
<dd> Axis remapping is available via &#8211;axismap and works the same as button mapping. In addition you can supply a sign to indicate that an axis should be inverted. So if you want to invert the y1 axis start with: </p>
<pre>
$ xboxdrv --axismap -Y1=Y1
</pre>
<p> If you want to swap the left and right stick start with: </p>
<pre>
$ xboxdrv --axismap X2=X1,Y2=Y1,X1=X2,Y1=Y2
</pre>
<p> Possible axis names are: x1, y1, x2, y2, lt, rt </p>
<p> Swaping lt or rt with x1, y1, x2, y2 will not work properly, since their range is different. </p>
<p> Just like with <code>&#8211;ui-axismap</code> you can add axis filter to each axis.</dl>
<h3>MODIFIER PRESET CONFIGURATION OPTIONS</h3>
<p> The options in this sections are sortcuts for <code>&#8211;modifier</code> options. Unlike <code>&#8211;modifier</code> they are not order depended, but have a predefined order that is used no matter the order in which the options are given.</p>
<dl>
<dt><code>&#8211;autofire BUTTON=FREQUENCY,&#8230;</code></p>
<dd> Autofire mapping allows you to let a button automatically fire with a given frequency in miliseconds: </p>
<pre>
$ xboxdrv --autofire A=250
</pre>
<p> Combining <code>&#8211;autofire</code> with button map allows you to have one button act as autofire while another one, emitting the same signal, acts normally. </p>
<pre>
$ xboxdrv --autofire B=250 --buttonmap B=A
</pre>
<dt><code>&#8211;axis-sensitivty </code><i>AXIS=SENSITIVITY</i>,&#8230;</p>
<dd> The sensitive of an axis can be adjusted via &#8211;axis-sensitivty: </p>
<pre>
$ xboxdrv --axis-sensitivty X1=-1.0,Y1=-1.0
</pre>
<p> A value of 0 gives you the default linear sensitivity, values larger then 0 will give you higher sensitivity, while values smaller then 0 will give you lower sensitivity. Sensitivity values in the range of [-1, 1] will generally give good results, everything beyond that won&#8217;t be of much practical use. </p>
<p> Sensitivity works by applying: </p>
<pre>
t = 2 ** sensitivity;
pos = (1.0f - (1.0f - pos) ** t) ** (1 / t);
</pre>
<p> To the value of the axis, this means that both the minimum value and the maximum value of the axis will always stay the same, just the response inbetween changes. </p>
<p> For a complete freeform way to change the axis response see the <code>Response Curve Filter</code>.</p>
<dt><code>&#8211;calibration </code><i>CALIBRATIONSPEC</i></p>
<dd> If your gamepad for some reason can&#8217;t reach the maximum value or isn&#8217;t centered properly you can fix that via the calibration options: </p>
<pre>
$ xboxdrv --calibration X2=-32768:0:32767
</pre>
<p> X2 is the axis name and the three values that follow are min, center and max. Simply insert the values that jstest reports when your axis is in the respective positions. </p>
<p> You can also use the calibration option if you want to make your joystick more sensitive. A setting of: </p>
<pre>
xboxdrv --calibration AXIS=MIN:CENTER:MAX,...
</pre>
<p> Will cause the joystick device report maximum position when your stick is only moved half the way.</p>
<dt><code>&#8211;deadzone </code><i>NUM</i></p>
<dd> The deadzone is the area at which the sticks do not report any events. The default is zero, which gives the best sensitifity but might also cause trouble in some games in that the character or camera might move without moving the stick. To fix this one has to set the value to something higher: </p>
<pre>
$ xboxdrv --deadzone 4000
</pre>
<p> A value of 4000 works quite well for most games. </p>
<p> You can also give the deadzone in percentage: </p>
<pre>
$ xboxdrv --deadzone 15%
</pre>
<dt><code>&#8211;deadzone-trigger </code><i>NUM</i></p>
<dd> The left and right trigger have a separate deadzone value which can be specified with: </p>
<pre>
$ xboxdrv --deadzone-trigger 15%  
</pre>
<dt><code>&#8211;dpad-rotation</code> <i>DEGREE</i></p>
<dd> Allows you to rotate the dpad. <i>DEGREE</i> must be a multiple of 45. This can be useful in isometric games where the playfield itself is rotated, thus a: </p>
<pre>
xboxdrv --dpad-rotation 45
</pre>
<p> Will give you controls that are relative to your character instead of your viewpoint.</p>
<dt><code>&#8211;four-way-restrictor</code></p>
<dd> The <code>&#8211;four-way-restrictor</code> option allows to limit the movement on both analogsticks to only four directions (up, down, left, right), the diagonals (up/left, up/right, down/left, down/right) are filtered out from the output. This option is useful for games such as Tetris, that don&#8217;t need diagonals and where you don&#8217;t want to accidently trigger the down-move while trying to do a left/right move.</p>
<dt><code>&#8211;relative-axis AXIS=NUM,&#8230;</code></p>
<dd> The function <code>&#8211;relative-axis</code> allows you to change the behaviour of an axis so that your movement of it moves its value up or down instead of applying it directly. This allows you to simulate throttle control for flightsim games. </p>
<p> Since the axis might be upside down, you might want to use the <code>&#8211;axismap</code> function to reverse it. </p>
<pre>
$ xboxdrv --relative-axis y2=64000 --axismap -y2=y2
</pre>
<dt><code>&#8211;square-axis</code></p>
<dd> The Xbox360 gamepad, as most other current day gamepads, features a circular movement range, which restricts the movement so that the distance to the center never gets beyond 1. This means that when you have the controller at the top/left the value reported is (0.7, 0.7) (i.e. length 1, angle 45) instead of (1,1). This behaviour is different then most classic PC joysticks, which had a square range and would report (1,1) when hold in the top/left corner. </p>
<p> Some old games (i.e. mostly DOS stuff) require a square movement range and will not function properly with the Xbox360 gamepad. Via the <code>&#8211;square-axis</code> option you can work around this issue and diagonals will be reported as (1,1).</dl>
<h3>UINPUT PRESET CONFIGURATION OPTIONS</h3>
<p> The following options are simple shortcuts for common configurations that can be accomplished manually by using <code>&#8211;ui-buttonmap</code> and <code>&#8211;ui-axismap</code>.</p>
<dl>
<dt><code>&#8211;trigger-as-button</code></p>
<dd> LT and RT send button instead of axis events</p>
<dt><code>&#8211;trigger-as-zaxis</code></p>
<dd> Combine LT and RT to form a zaxis instead</p>
<dt><code>&#8211;dpad-as-button</code></p>
<dd> The DPad sends button instead of axis events.</p>
<dt><code>&#8211;dpad-only</code></p>
<dd> Both sticks are ignored, only the DPad sends out axis events. Useful for games that might get confused by additional analog axis. Combining this option with <code>&#8211;trigger-as-button</code> is recommend in most situations.</p>
<dt><code>&#8211;guitar</code></p>
<dd> Sets a predefined button and axis mapping for use with guitar controllers. This mainly gets rid of a few unnecessary buttons and axis not used by a guitar controller.</p>
<dt><code>-m, &#8211;mouse</code></p>
<dd> Lets the controller act as a mouse. It is indendical to: </p>
<p>$ xboxdrv&#8211; dpad &#8211; as &#8211; button&#8211; deadzone 4000 &#8211;trigger &#8211; as &#8211; zaxis&#8211; axismap &#8220;-y2=y2,-trigger=trigger&#8221; &#8211;ui &#8211; axismap &#8220;x1=REL_X:15:20,y1=REL_Y:15:20,y2=REL_WHEEL:5:100,x2=REL_HWHEEL:5:100,trigger=REL_WHEEL:5:100&#8221; &#8211;ui &#8211; buttonmap &#8220;a=BTN_LEFT,b=BTN_RIGHT,x=BTN_MIDDLE,y=KEY_ENTER,rb=KEY_PAGEDOWN,lb=KEY_PAGEUP,&#8221; &#8211;ui &#8211; buttonmap &#8220;dl=KEY_LEFT,dr=KEY_RIGHT,du=KEY_UP,dd=KEY_DOWN,&#8221; &#8211;ui &#8211; buttonmap &#8220;start=KEY_FORWARD,back=KEY_BACK,guide=KEY_ESC,tl=void,tr=void&#8221;</p>
<p> You can customize it by the usual means, just make sure that <code>&#8211;mouse</code> comes before your customization options on the command line. </p>
<p> Note that if you have your mouse buttons switched you must adjust the above to match your mouse configuration or the button events will come out wrong.</p>
<dt><code>&#8211;mimic-xpad</code></p>
<dd> Causes xboxdrv to use the same axis and button names as the xpad kernel driver for wired Xbox360 controller</p>
<dt><code>&#8211;mimic-xpad-wireless</code></p>
<dd> Causes xboxdrv to use the same axis and button names as the xpad kernel driver for wired Xbox360 controller</dl>
<h3>UINPUT CONFIGURATION OPTIONS</h3>
<dl>
<dt><code>&#8211;no-uinput</code></p>
<dd> Do not to start UInput, instead simply read events from the controller, useful for debugging.</p>
<dt><code>&#8211;no-extra-devices</code></p>
<dd> By default xboxdrv will allocate multiple uinput devices and sort events to each of them. Thus mouse related events like BTN_LEFT or REL_X will go to a virtual mouse device, while ABS_X events would go to a virtual joystick device and KEY_ESC would go to a virtual keyboard device. </p>
<p> This option disables that automatism and all events will go to the same virtual device. </p>
<p> Manual assignment to a specific device (i.e. KEY_ESC [at] keyboard, BTN_A [at] joystick, &#8230;) is still possible.</p>
<dt><code>&#8211;no-extra-events</code></p>
<dd> By default xboxdrv will allocate multiple uinput devices and sort events to each of them. Thus mouse related events like BTN_LEFT or REL_X will go to a virtual mouse device, while ABS_X events would go to a virtual joystick device and KEY_ESC would go to a virtual keyboard device. </p>
<p> To make sure sure that a mouse, keyboard or joystick device is properly detected by Xorg, the kernel or libraries such SDL xboxdrv will insert extra dummy events. For example a mouse device needs REL_X and REL_Y events to be detected as such, but a configuration that only wants to emulate the mouse buttons won&#8217;t provide those, thus xboxdrv will add them automatically. The <code>&#8211;no-extra-events</code> option will switch this behaviour off.</p>
<dt><code>&#8211;device-name NAME</code></p>
<dd> Changes the descriptive name the device will have. This options acts the same as &#8211;device-names <i>CURRENTSLOT</i>.auto=<i>NAME</i></p>
<dt><code>&#8211;device-names TYPE.SLOT=NAME,&#8230;</code></p>
<dd> Changes the descriptive name the device will have. <i>TYPE</i> is one of mouse, keyboard, joystick, auto or a number. <i>SLOT</i> is a slot number or auto. The auto name acts as wild card and matches everything.</p>
<dt><code>&#8211;device-usbid VENDOR:PRODUCT:VERSION:BUS</code></p>
<dd> Changes the vendor, product, version and bus id that the device will have. The last two arguments are optional. This options acts the same as &#8211;device-usbids <i>CURRENTSLOT</i>.auto=<i>VENDOR:PRODUCT:VERSION:BUS</i></p>
<dt><code>&#8211;device-usbids TYPE.SLOT=VENDOR:PRODUCT:VERSION:BUS,&#8230;</code></p>
<dd> Changes the vendor, product, version and bus id the device will have. <i>TYPE</i> is one of mouse, keyboard, joystick, auto or a number. <i>SLOT</i> is a slot number or auto. The auto name acts as wild card and matches everything.</p>
<dt><code>&#8211;ui-clear</code></p>
<dd> Removes all uinput mappings and will leave the driver in a blank state and only map those things you added yourself. If you only want to get rid of individual buttons you can use the &#8216;void&#8217; event.</p>
<dt><code>&#8211;ui-buttonmap</code> <i>UIBUTTONSPEC,&#8230;</i></p>
<dd>
UIBUTTONSPEC = XBOXBUTTON[&#8220;+&#8221; XBOXBUTTON][&#8220;^&#8221; FILTER]&#8230; &#8220;=&#8221;(RELSPEC | BTNSPEC | EXECSPEC);<br />
RELSPEC = [DEVICEID &#8220;-&#8220;] &#8220;REL_&#8221;[&#8220;:&#8221;[VALUE][&#8220;:&#8221; REPEAT]];<br />
BTNSPEC = [DEVICEID &#8220;-&#8220;]((&#8220;BTN_&#8221; NAME) | (&#8220;KEY_&#8221; NAME)) { &#8220;+&#8221; BTNSPEC };<br />
EXECSPEC = PROGRAM{&#8220;:&#8221; ARGUMENT};<br />
XBOXBUTTON = &#8220;a&#8221; | &#8220;b&#8221; | &#8220;x&#8221; | &#8220;y&#8221; | &#8220;lb&#8221; | &#8220;rb&#8221; | &#8220;lt&#8221; | &#8220;rt&#8221; |<br />
             &#8220;tl&#8221; | &#8220;tr&#8221; | &#8220;start&#8221; | &#8220;select&#8221; | &#8220;back&#8221; | &#8220;guide&#8221; | &#8220;black&#8221; | &#8220;white&#8221;;<br />
FILTER = &#8220;toggle&#8221; | &#8220;invert&#8221; | &#8220;autofire&#8221;[&#8220;:&#8221; RATE][&#8220;:&#8221; DELAY] | log[&#8220;:&#8221; STRING];<br />
NAME = STRING;<br />
VALUE = NUMBER;<br />
REPEAT = NUMBER;<br />
DEVICEID = NUMBER;</p>
<p> Allows you to change the event code that is send to the kernel for buttons. The usage is similar to the normal button mapping, except that the right hand side is an event name from <i>/usr/include/linux/input.h</i>. You can use all <code>KEY_</code> or <code>BTN_</code> codes for <code>&#8211;ui-buttonmap</code>. </p>
<p> If the right hand side is left empty all the supplied filters will be added to the already existing button binding instead of a new one. </p>
<p> Aside from the named keys, you can also give the input code directly as number via the syntax <code>KEY_#</code><i>NUM</i>. </p>
<p> Instead of the low level <code>KEY_</code> names, which represent keycodes, you can also use the higher level X11 keysyms <code>XK_</code>, the keysyms have the advantage that they map directly to the key you expect, while a <code>KEY_</code> name gets mangled by the X11 keymap and will often not report what you expect in case you use a keymap that is different then your keyboard (i.e. dvorak on a qwerty keyboard). </p>
<p> A full list of valid X11 keysyms can be optained with <code>&#8211;help-x11keysym</code>. </p>
<p> For joystick buttons there is in addition to the <code>BTN_JOYSTICK</code>, <code>BTN_X</code>, etc. macros the special name <code>JS_$NUM</code>, which sets the given button to the $NUMS joystick button, i.e.: </p>
<pre>
$ xboxdrv --ui-clear --ui-buttonmap A=JS_0,B=JS_1
</pre>
<p> Note that this will only work if no other joystick button ids are in the way. </p>
<p> You can also map a button to a <code>REL_</code> event. In that case you can supply additional paramaters in the form of: </p>
<pre>
$ xboxdrv --ui-buttonmap X=REL_???:VALUE:REPEAT
</pre>
<p> <i>VALUE</i> gives the value of the event (default: 10) </p>
<p> <i>REPEAT</i> gives the number of milisecond to pass before the event is fired again (default: 5) </p>
<p> The special &#8216;void&#8217; event allows you to clear any existing bindings for a given button, which can be useful in cases when a game only supports a limited number of buttons. </p>
<p> You can also prepend a device_id to the UIBUTTONSPEC which allows you to create multiple uinput devices. By default &#8216;auto&#8217; is assumed as device_id which automatically try to do the right thing, sending keyboard events to a keyboard device and mouse events to a mouse device. Other possible values are &#8216;mouse&#8217; and &#8216;keyboard&#8217;. A device_id of &#8216;0&#8217; refers to the first joystick device, values larger then 0 to the second, third, etc. </p>
<p> Note that the &#8216;mouse&#8217; and &#8216;keyboard&#8217; device_id names do not give you a mouse or keyboard device, these are just symbolic names for the devices into which xboxdrv will sort events that look like a mouse or keyboard event. The final determination of which device gets handled as what will be done by the Kernel or Xorg depending on what events a device provides. </p>
<p> An example configuration making use of device_id would look like this: </p>
<p>xboxdrv &#8211; s&#8211; ui &#8211; clear&#8211; ui &#8211; buttonmap A = JS_0 @0, B = JS_1 @0 &#8211;ui &#8211; axismap X2 = ABS_X @0, Y2 = ABS_Y @0 &#8211;ui &#8211; buttonmap X = JS_0 @0, Y = 1 &#8211; JS_1 @0 &#8211;ui &#8211; axismap X2 = ABS_X @1, Y2 = ABS_Y @1</p>
<p> In this example the left stick creates a joystick device and the right stick creates a separate joystick device. </p>
<p> When using multiple controller slots you can additionally append the slot id and thus assign events across controller slot boundaries. The syntax for that is: </p>
<p>BTN_A @{deviceid}.<br />
{<br />
    slotid<br />
}</p>
<p> Instead of giving just a single button, it is also possible to give two buttons to <code>&#8211;ui-buttonmap</code> to allow shifting: </p>
<pre>
xboxdrv -s \
  --ui-clear \
  --ui-buttonmap A=JS_0,B=JS_1,LB+A=JS_2,LB+B=JS_3
</pre>
<p> In this example LB acts as shift button, if A is pressed without LB it will send out a JS_0 event, but if LB is pressed it will send a JS_2 event instead. This allows you to multiply the number of available buttons on the controller. </p>
<p> See the section KEYBOARD EMULATION below on how to resolve issues with Xorg not detecting the virtual keyboard that xboxdrv creates. </p>
<p> You can also apply filters to button events: </p>
<pre>
xboxdrv -s \
  --ui-buttonmap A^toggle=JS_0
</pre>
<p> For documentation on the filters you can apply to events see [Button Filter].</p>
<dt><code>&#8211;ui-axismap</code> <i>UIAXISSPEC,&#8230;</i></p>
<dd>
UIAXISSPEC = [XBOXBTN &#8220;+&#8221;] XBOXAXIS { &#8220;^&#8221; FILTER } &#8220;=&#8221;(RELSPEC | RELREP | KEYSPEC | ABSSPEC);<br />
KEYSPEC = [&#8220;key:&#8221;] &#8220;KEY_&#8221; NAME &#8220;:&#8221;<br />
                   &#8220;KEY_&#8221; NAME &#8220;:&#8221; THRESHOLD;<br />
RELSPEC = [&#8220;rel:&#8221;] &#8220;REL_&#8221; NAME &#8220;:&#8221; VALUE &#8220;:&#8221; REPEAT;<br />
RELREP = &#8220;rel-repeat:&#8221;<br />
         &#8220;REL_&#8221; NAME &#8220;:&#8221; VALUE &#8220;:&#8221; REPEAT;<br />
ABSSPEC = [&#8220;abs:&#8221;] &#8220;ABS_&#8221; NAME;<br />
FILTER = (&#8220;calibration&#8221; | &#8220;cal&#8221;) &#8220;:&#8221; MIN &#8220;:&#8221; CENTER &#8220;:&#8221; MAX |<br />
         (&#8220;sensitifity&#8221; | &#8220;sen&#8221;) &#8220;:&#8221; SENSITIFITY |<br />
         (&#8220;deadzone&#8221; | &#8220;dead&#8221;) &#8220;:&#8221; MIN &#8220;:&#8221; MAX &#8220;:&#8221; SMOOTH |<br />
         (&#8220;relative&#8221; | &#8220;rel&#8221;) &#8220;:&#8221; SPEED |<br />
         (&#8220;responsecurve&#8221; | &#8220;response&#8221; | &#8220;resp&#8221;){&#8220;:&#8221; VALUE} XBOXBTN = &#8220;a&#8221; | &#8220;b&#8221; | &#8220;x&#8221; | &#8220;y&#8221; | &#8220;start&#8221; | &#8220;back&#8221; | &#8220;guide&#8221; | &#8220;lb&#8221; | &#8220;rb&#8221; | &#8230; XBOXAXIS = &#8220;x1&#8221; | &#8220;y1&#8221; | &#8220;x2&#8221; | &#8220;y2&#8221; | &#8220;z&#8221; | &#8220;lt&#8221; | &#8220;rt&#8221; | &#8220;dpad_x&#8221; | &#8220;dpad_y&#8221;;<br />
VALUE = NUMBER;<br />
REPEAT = NUMBER;<br />
THRESHOLD = NUMBER;<br />
NAME = STRING;</p>
<p> Similar to <code>&#8211;ui-buttonmap</code> this option allows you to change the event code that is send to the kernel for axes. The events that are available are the same as for <code>&#8211;ui-buttonmap</code>. </p>
<pre>
$ xboxdrv --ui-axismap X1=REL_???:VALUE:REPEAT
</pre>
<p> <i>VALUE</i> gives the maximum value of the event, the actual value that gets send is <i>VALUE</i> * axis_state. (default: 10) </p>
<p> <i>REPEAT</i> gives the number of milisecond to pass before the event is fired again (default: 5). </p>
<p> The value of -1 has a special meaning, it will result in the REL event being fired as soon as possible (i.e. every <i>timeout</i> miliseconds). This is the recomment way for handling mouse emulation, as it will keep REL events syncronized and thus avoid jaggies in the movement, that will result from manually specifying a timeout. </p>
<pre>
$ xboxdrv --ui-axismap X1=KEY_UP:KEY_DOWN:THRESHOLD
</pre>
<p> <i>KEY_UP</i> gives the keycode to be send when the axis is moved up </p>
<p> <i>KEY_DOWN</i> gives the keycode to be send when the axis is moved down </p>
<p> <i>THRESHOLD</i> gives the threshold that triggers the sending of an event </p>
<p> Just like <code>&#8211;ui-buttonmap</code>, you can also use shift keys in place of the XBOXAXIS: </p>
<pre>
$ xboxdrv --ui-axismap X1=ABS_X,LB+X1=ABS_RX
</pre>
<p> This allows you to send ABS_X events normally and ABS_RX events when the LB button is held down. </p>
<p> For information on how to use axis filters, see [Axis Filter].</dl>
<h2>INPUT EVENT HANDLER</h2>
<p> Input event handler decide what comes out of the virtual input devices that xboxdrv creates. They for example decide that when button A is pressed on a gamepad, that a virtual keyboard will emit a press of the space key. </p>
<p> Furthermore input event handler can also perform some basic transformation of the input signals, thus a joystick can be used to send WASD keys.</p>
<h3>BUTTON EVENT HANDLER</h3>
<p> A button event handler decides what happens when a button is pressed, it needs to be specified with the <code>&#8211;ui-buttonmap</code> option. The example below shows the simplest use case: </p>
<pre>
$ xboxdrv --ui-buttonmap A=key:KEY_A
</pre>
<p> Here <code>key</code> is the name of the button event handler, while <code>KEY_A</code> is an argument for the event handler. What kind of arguments an event handler allows depends on the event handler. </p>
<p> There is also a shorthand form of specifing event handlers by just writing: </p>
<pre>
$ xboxdrv --ui-buttonmap A=KEY_A
</pre>
<p> Here no handler is specified explicitly, if that is the case, the appropriate handler will be guessed based on the event type. EV_KEY events will be handled by the <code>key</code> handler, EV_REL by the <code>rel</code> handler and EV_ABS by the <code>abs</code> handler.</p>
<dl>
<dt><code>key</code>:<i>KEY_EVENT</i>, <code>key</code>:<i>KEY_EVENT</i>:<i>KEY_EVENT</i>:<i>HOLD_THRESHOLD_MSEC</i></p>
<dd> The <code>key</code> handler is the most basic one, it maps a button directly to a virtual key or another button. </p>
<p> If additional arguments are supplied the button will be able to send out two different events. The first event specified will be send when the button is clicked normally, while the second event will be send in case the button is hold down for the time specified in <i>HOLD_THRESHOLD_MSEC</i>. </p>
<p> An example for the hold button would look like: </p>
<pre>
xboxdrv \
  --ui-buttonmap A=JS_0:JS_1:500
</pre>
<p> This will send JS_0 events when the button is pressed and switch to JS_1 events when the button was hold for 500 miliseconds. </p>
<p> The hold button feature is useful to effectly double the number of available buttons, thus the dpad can for example be used to send out eight different button events instead of just four, which is enough to handle weapons in most FPS games.</p>
<dt><code>abs</code></p>
<dd> not yet implemented</p>
<dt><code>rel</code>:<i>REL_EVENT</i>:<i>VALUE</i>:<i>REPEAT</i></p>
<dd> The rel handler will send out a REL event whenever the button is pressed. <i>VALUE</i> gives the value of the event that will be send, while <i>REPEAT</i> gives the number of miliseconds till the event will be send again. </p>
<p> A typical use for REL events is emulation of the scroll wheel of a mouse, an example configuration would be: </p>
<pre>
xboxdrv \
  --ui-buttonmap Y=rel:REL_WHEEL:1:500,A=rel:REL_WHEEL:-1:500
</pre>
<p> Here Y will scroll up and A will scroll down.</p>
<dt><code>cycle-key</code>:<i>KEY_EVENT</i>:&#8230;</p>
<dd> The cycle-key handler will switch the <i>KEY_EVENT</i> that gets send with each button press. This is useful in situations where a range of buttons should be mapped to a single key. For example a FPS might have weapons mapped from 1 to 6, but only a single key on the gamepad is free, thus one could write: </p>
<pre>
xboxdrv \
  --ui-buttonmap A=cycle-key:KEY_1:KEY_2:KEY_3:KEY_4:KEY_5:KEY_6
</pre>
<dt><code>cycle-key-named:</code><i>NAME</i><code>:</code><i>KEY_EVENT</i><code>:&#8230;</code></p>
<dd> The <code>cycle-key-named</code> handler works exactly like the <code>cycle-key</code> handler, except that a name has to be supplied for the cycle sequence. The name of the sequence is used by <code>cycle-key-ref</code> to access the sequence and reuse it for another button. </p>
<p> In this simple example A is used to toggle through all weapon keys forward, while B is used to toggle the keys backwards: </p>
<pre>
xboxdrv \
  --ui-buttonmap A=cycle-key-named:weapons:KEY_1:KEY_2:KEY_3:KEY_4,B=cycle-key-ref:weapons
</pre>
<dt><code>cycle-key-ref</code>:<i>NAME</i>:<i>DIRECTION</i>, <code>sequence-key-ref</code>:<i>NAME</i>:<i>DIRECTION</i></p>
<dd> The <code>cycle-key-ref</code> handler will access and reuse the named cycle keysequence given by <i>NAME</i>. If <i>DIRECTION</i> can either be &#8216;forward&#8217; or &#8216;backward&#8217;, if no direction is supplied it will default to &#8216;backward&#8217;. </p>
<p> See <code>cycle-key-named</code> for a full example.</p>
<dt><code>sequence-key-named:</code><i>NAME</i><code>:</code><i>KEY_EVENT</i><code>:&#8230;</code></p>
<dd> The <code>sequence-key-named</code> works exactly the same as the <code>cycle-key-named</code>, with the only difference being that the <code>sequence-key-named</code> will not wrap around when reaching the beginning or end of the sequence. </p>
<p> This behaviour is useful in flight simulations or other games where thrusters might be controllered by numeric keys and it wouldn&#8217;t make much sense to jump from zero to full thrust in one go. </p>
<p> To move backwards through the sequence another key must be bound to <code>sequence-key-ref</code>.</p>
<dt><code>exec</code></p>
<dd> The exec button handler allows to launch an application when the button was pressed. An example would look like this: </p>
<pre>
xboxdrv \
  --ui-buttonmap A=exec:/home/juser/local/bin/screenshot.sh
</pre>
<p> Possible uses for the button are the ability to do screenshots or perform other tasks that are outside the main application you are using xboxdrv with.</p>
<dt><code>macro</code></p>
<dd> A button can be bound to a macro via: </p>
<pre>
xboxdrv \
  --ui-buttonmap A=macro:/home/juser/.xboxdrv/somefile.macro
</pre>
<p> The <i>.macro</i> file has the form of: </p>
<pre>
send KEY_LEFTSHIFT 1
wait 500
send KEY_LEFTSHIFT 0
</pre>
<p> All abs, rel and key events can be send from a macro file.</dl>
<h3>AXIS EVENT HANDLER</h3>
<p> Axis event handler decide what happens when an axis is moved. Like button event handler they come in different forms and like button event handler they provide a shortcut form. EV_KEY events will be handled by the <code>key</code> handler, EV_REL by the <code>rel</code> handler and EV_ABS by the <code>abs</code> handler.</p>
<dl>
<dt><code>abs</code>:<i>ABS_EVENT</i></p>
<dd> The <code>abs</code> handler is the simplest of them all, it will simply send out the value it gets as input as the given <i>ABS_EVENT</i> event to the kernel. Thus a basic configuration to make the left stick behave as joystick would look like this: </p>
<pre>
xboxdrv \
  --ui-axismap X1=abs:ABS_X,Y1=abs:ABS_Y
</pre>
<dt><code>key</code>:<i>KEY_UP</i>:<i>KEY_DOWN</i>:<i>THRESHOLD</i></p>
<dd> <i>KEY_UP</i> gives the keycode to be send when the axis is moved up </p>
<p> <i>KEY_DOWN</i> gives the keycode to be send when the axis is moved down </p>
<p> <i>THRESHOLD</i> gives the threshold that triggers the sending of an event </p>
<p> Just like <code>&#8211;ui-buttonmap</code>, you can also use shift keys in place of the XBOXAXIS: </p>
<pre>
$ xboxdrv --ui-axismap X1=ABS_X,LB+X1=ABS_RX
</pre>
<p> This allows you to send ABS_X events normally and ABS_RX events when the LB button is held down.</p>
<dt><code>rel</code>:<i>REL_EVENT</i>:<i>VALUE</i>:<i>REPEAT</i></p>
<dd> <i>VALUE</i> gives the maximum value of the event, the actual value that gets send is <i>VALUE</i> * axis_state. (default: 10) </p>
<p> <i>REPEAT</i> gives the number of milisecond to pass before the event is fired again (default: 5). </p>
<p> The value of -1 has a special meaning, it will result in the REL event being fired as soon as possible (i.e. every <i>timeout</i> miliseconds). This is the recomment way for handling mouse emulation, as it will keep REL events syncronized and thus avoid jaggies in the movement, that will result from manually specifying a timeout. </p>
<p> The <code>rel</code> handler is mainly useful for mouse pointer emulation, if you want to emulate a mouse scroll wheel use the <code>rel-repeat</code> handler instead.</p>
<dt><code>rel-repeat</code>:<i>REL_EVENT</i>:<i>VALUE</i>:<i>REPEAT</i></p>
<dd> The <code>rel-repeat</code> handler is similar to the <code>rel</code> handler, but optimized for emulating the scroll wheel of a mouse. </p>
<p> <i>VALUE</i> isn&#8217;t scaled to how far the axis has moved, instead it is constant, instead the time given in <i>REPEAT</i> is scaled according to the axis movement. Thus the further the stick is moved, the more events will be send. </p>
<p> The need for both <code>rel-repeat</code> and <code>rel</code> arises from the fact that Xorg converts scroll wheel movement to button presses before they are handed to an application, thus an application never properly sees the changes in <i>VALUE</i>, by scaling <i>REPEAT</i> instead that problem is worked around.</dl>
<h2>INPUT FILTER</h2>
<p> Input filter allow to manipulate the events that come from the controller. They can be used on <code>&#8211;buttonmap</code>, <code>&#8211;axismap</code>, <code>&#8211;ui-buttonmap</code> and <code>&#8211;ui-axismap</code>. The difference between the two is that the <code>&#8211;ui-&#8230;</code> versions applies to the uinput events, while the other version applies to Xbox360 controller events.</p>
<h3>BUTTON FILTER</h3>
<dl>
<dt><code>tog</code>, <code>toggle</code></p>
<dd> The toggle filter will turn the button into a toggle button, clicking the button will set it to pressed state and pressing it again will unpress it. Useful for games where you might want to permanently run or duck without holding the button pressed.</p>
<dt><code>inv</code>, <code>invert</code></p>
<dd> The invert filter will keep the button in pressed state when it is not pressed and in unpressed state when it is pressed.</p>
<dt><code>auto</code>, <code>autofire</code>:<i>RATE</i>:<i>DELAY</i></p>
<dd> The autofire filter allows to repeatatly send button press events when the button is held down. It takes two optional parameters: </p>
<p> <i>RATE</i> is the number of miliseconds between button press events. </p>
<p> <i>DELAY</i> the amount of miliseconds till the autofire will start, before that delay the button will act as normal.</p>
<dt><code>click-press</code></p>
<dd> The <code>click-press</code> filter will transmit a single button click when the button is pressed.</p>
<dt><code>click-release</code></p>
<dd> The <code>click-release</code> filter will transmit a single button click when the button is released.</p>
<dt><code>click-both</code></p>
<dd> The <code>click-both</code> filter will transmit a single button click when the button is pressed and another one when it is released.</p>
<dt><code>const</code>:<i>VALUE</i></p>
<dd> The const filter will ignore the input signal and send a constant value to the output. This can be used for example in combination with multiple configurations to signal a game or another application which configuration is currently active.</p>
<dt><code>delay</code>:<i>TIME</i></p>
<dd> A button has to be held down for TIME miliseconds before it will emit an event, press events shorter then that will be ignored.</p>
<dt><code>log</code>:<i>STRING</i></p>
<dd> The log filter will output everything to stdout that goes through it to, this is useful for debugging the filter. A <i>STRING</i> can be provided as parameter that will be outputed before the event.</dl>
<h3>AXIS FILTER</h3>
<dl>
<dt><code>cal</code>, <code>calibration</code>:<i>MIN</i>:<i>CENTER</i>:<i>MAX</i></p>
<dd> See <code>&#8211;calibration</code>.</p>
<dt><code>sen</code>, <code>sensitivity</code>:<i>SENSITIVITY</i></p>
<dd> See <code>&#8211;axis-sensitivity</code>.</p>
<dt><code>dead</code>, <code>deadzone</code>:<i>VALUE</i>, <code>deadzone</code>:<i>MIN</i>:<i>CENTER</i>:<i>MAX</i></p>
<dd> Deadzone filter applies a deadzone to the current axis. If only <i>MIN</i> is provided, the parameter will be interpreted as <i>-MIN:MIN:1</i>. If the argument is 1, smooth filtering will be applied so that the end of the deadzone is 0. Setting the argument to 0 will apply a simple cut-off filter, where all events smaller then the threshold are ignored.</p>
<dt><code>rel</code>, <code>relative</code>:<i>SPEED</i></p>
<dd> See <code>&#8211;relative-axis</code>.</p>
<dt><code>resp</code>, <code>response</code>:<i>VALUES</i>:&#8230;</p>
<dd> The response curve filter allows you to completely change the way an axis reacts. The filter takes a list of <i>VALUES</i> that are then linearly interpolated and spread across the full range of the axis. An example would look like this: </p>
<pre>
xboxdrv \
 --ui-axismap x1^resp:-32768:-4000:0:4000:32767
</pre>
<p> Here the X1 axis is manipulated so that it will have a lower sensitivity in the center and a higher one on the outside.</p>
<dt><code>const</code>:<i>VALUE</i></p>
<dd> The const filter will ignore the input signal and send a constant value to the output. This can be used for example in combination with multiple configurations to signal a game or another application which configuration is currently active.</p>
<dt><code>log</code>:<i>STRING</i></p>
<dd> The log filter will output everything to stdout that goes through it to, this is useful for debugging the filter. A <i>STRING</i> can be provided as parameter that will be outputed before the event.</dl>
<h3>MODIFIER</h3>
<p> While button and axis filter only apply to a single axis or button at a time, modifiers apply to the complete controller at once and can thus be used to perform modifications that require input from multiple axis or buttons. Most of the modifiers explained below replicate functionality provided by regular options, but allow more fine tuning, such as limiting the effects to a single analog stick instead of just applyig it to all. Note that modifiers are applied one after the other, so order is important.</p>
<dl>
<dt><code>dpad-rotate</code>=<i>DEGREE</i></p>
<dd> See <code>&#8211;dpad-rotation</code>.</p>
<dt><code>dpad-restrictor</code>=<i>RESTRICTON</i></p>
<dd> Restricts the dpad movement, values for <i>RESTRICTON</i> can be: </p>
<p> x-axis: only allow movement in the X axis </p>
<p> y-axis: only allow movement in the Y axis </p>
<p> fourway: allow movement in X and Y axis, but filter out diagonals</p>
<dt><code>4wayrest</code>, <code>four-way-restrictor</code>=<i>XAXIS</i>:<i>YAXIS</i></p>
<dd> See <code>&#8211;four-way-restrictor</code>.</p>
<dt><code>square</code>, <code>square-axis</code>=<i>XAXIS</i>:<i>YAXIS</i></p>
<dd> See <code>&#8211;square-axis</code>.</p>
<dt><code>rotate</code>=<i>XAXIS</i>:<i>YAXIS</i>:<i>DEGREE</i>:<i>MIRROR</i></p>
<dd> Rotates the stick given by <i>XAXIS</i> and <i>YAXIS</i> by <i>DEGREE</i> and optionally <i>MIRRORS</i> it.</p>
<dt><code>stat</code>, <code>statistic</code></p>
<dd> The statistic modifier doesn&#8217;t actually modify anything, instead it collects statistics on the controller, such as how many times a button has been pressed. The results of the collections will be displayed on shutdown of xboxdrv. </p>
<p> Note that the stat modifier is part of the modifier stack, thus to get correct results you must make sure that it comes first in the stack when it should work on real events and not be confused by auto-fire or similar modifications.</dl>
<h2>RUNNING XBOXDRV</h2>
<h3>USING A SINGLE CONTROLLER</h3>
<p> Plug in your Xbox360 gamepad and then unload the xpad driver via: </p>
<pre>
$ rmmod xpad
</pre>
<p> If you want to permanently unload it add the following line to <i>/etc/modprobe.d/blacklist.conf</i>: </p>
<pre>
blacklist xpad
</pre>
<p> Next you have to load the uinput kernel module which allows userspace programms to create virtual input devices and the joydev module handles the <i>/dev/input/jsX</i> devices: </p>
<pre>
$ modprobe uinput
$ modprobe joydev
</pre>
<p> You also have to make sure that you have access rights to /dev/input/uinput, either add yourself to the appropriate group, adjust the permissions or run xboxdrv as root. </p>
<p> Once ensured that xpad is out of the way and everything is in place start the userspace driver with: </p>
<pre>
$ xboxdrv
</pre>
<p> Or in case you don&#8217;t have the neccesary rights (being in group root should often be enough) start the driver as root via: </p>
<pre>
$ sudo xboxdrv
</pre>
<p> This will create /dev/input/js0 and allow you to access the gamepad from any game. To exit the driver press Ctrl-c. </p>
<p> By default xboxdrv will echo all controller events to the console, this makes it easy to see if things are properly working, but will eat a lot of CPU, thus it is strongly recomment to disabled that output with the <code>&#8211;silent</code> option. </p>
<p> The trigger buttons are handled by xboxdrv normally as axis, giving you analog feedback, while this reproduces the Xbox360 controller the most accurately, it will confuse many and only be useful in a few, racing games mainly. So in the majority of cases it is recomment to change the triggers to regular buttons via: </p>
<pre>
$ xboxdrv --trigger-as-button
</pre>
<h3>USING MULTIPLE CONTROLLER</h3>
<p> If you want to use multiple wired controllers you need to start multiple instances of the xboxdrv driver and append the -i argument to select the appropriate controller like this: </p>
<pre>
$ xboxdrv -i 1
</pre>
<p> If you have multiple wireless controller you need to start multiple instances of the xboxdrv driver and append the <code>&#8211;wid</code> option like this: </p>
<pre>
$ xboxdrv --wid 1
</pre>
<p> You have to sync the wireless controller as usual. </p>
<p> To see a list of all the controllers that xboxdrv detects being connected to your system use: </p>
<pre>
$ xboxdrv --list-controller
</pre>
<h3>HOTPLUGGING AND XBOXDRV DAEMON</h3>
<p> To allow hotplugging of gamepads xboxdrv has to be run in daemon mode. This is accomplished with the <code>&#8211;daemon</code> option: </p>
<pre>
$ xboxdrv --daemon
</pre>
<p> When launched in daemon mode xboxdrv will listen to udev events and thus be notified whenever a new USB device gets plugged into the computer. It will then match that device against its list of supported devices and launch a separate thread to handle that gamepad. </p>
<p> Note that xboxdrv will not allow an arbitrary large number of controllers to be used in that mode, it can only handle as many controllers as you have allocated controller slots at startup. New slots can be allocated with <code>&#8211;next-controller</code> and by default one slot is always allocated, thus to support three controller you would run it with: </p>
<pre>
$ xboxdrv --daemon --next-controller --next-controller
</pre>
<p> Each controller slot can be configured individually and you can limit which gamepad gets assigned to which slot with the <code>&#8211;match</code> option. </p>
<p> Note that xboxdrv will create the virtual uinput devices on startup, not when a gamepad gets plugged in, this allows to plug in gamepads even after a game or an application like XBMC has already been launched and still have it all function properly. </p>
<p> In daemon mode xboxdrv can be detached from the current shell via <code>&#8211;detach</code>, to get a handle on it to kill it you can write its pid via the <code>&#8211;pid-file</code>: </p>
<pre>
$ sudo xboxdrv --daemon --detach --pid-file /var/run/xboxdrv.pid
</pre>
<h2>XBOXDRV DAEMON DBUS INTERFACE</h2>
<p> When Xboxdrv is run as daemon it will export some API functions via D-Bus, thus allowing to make configuration changes at runtime. The D-Bus interface can be accessed either by the numerous language bindings provided or via the generic command line tool <code>dbus-send</code> or by the more userfriendly <code>xboxdrvctl</code> tool. Examples below are given for the raw <code>dbus-send</code>. </p>
<p> Introspection is provided via the usual means: </p>
<p>dbus &#8211; send&#8211; session&#8211; type = method_call&#8211; print &#8211; reply&#8211; dest = org.seul.Xboxdrv / org / seul / Xboxdrv org.freedesktop.DBus.Introspectable.Introspect dbus &#8211; send&#8211; session&#8211; type = method_call&#8211; print &#8211; reply&#8211; dest = org.seul.Xboxdrv / org / seul / Xboxdrv / ControllerSlots / 0 org.freedesktop.DBus.Introspectable.Introspect dbus &#8211; send&#8211; session&#8211; type = method_call&#8211; print &#8211; reply&#8211; dest = org.seul.Xboxdrv / org / seul / Xboxdrv / Daemon org.freedesktop.DBus.Introspectable.Introspect</p>
<p> Status information on available slots, configuration and active controllers can be obtained via: </p>
<p>dbus &#8211; send&#8211; session&#8211; type = method_call&#8211; print &#8211; reply&#8211; dest = org.seul.Xboxdrv / org / seul / Xboxdrv / Daemon org.seul.Xboxdrv.Daemon.Status</p>
<p> Setting the LED on controller 0 can be done via: </p>
<p>dbus &#8211; send&#8211; session&#8211; type = method_call&#8211; print &#8211; reply&#8211; dest = org.seul.Xboxdrv / org / seul / Xboxdrv / ControllerSlots / 0 org.seul.Xboxdrv.Controller.SetLed int32 : 4</p>
<p> Setting the rumble motors on controller 0 can be done via: </p>
<p>dbus &#8211; send&#8211; session&#8211; type = method_call&#8211; print &#8211; reply&#8211; dest = org.seul.Xboxdrv / org / seul / Xboxdrv / ControllerSlots / 0 org.seul.Xboxdrv.Controller.SetRumble int32 : 255 int32 : 255</p>
<p> Setting a specific controller slot configuration, just as <code>&#8211;toggle BTN</code> allows, can be done with: </p>
<p>dbus &#8211; send&#8211; session&#8211; type = method_call&#8211; print &#8211; reply&#8211; dest = org.seul.Xboxdrv / org / seul / Xboxdrv / ControllerSlots / 0 org.seul.Xboxdrv.Controller.SetConfig int32 : 2</p>
<h2>TESTING</h2>
<p> Knowing how to test a xboxdrv configuration is absolutely crucial in understanding what is wrong in a given setup. Testing the configuration in a game is most often not helpful, since you won&#8217;t see the true cause beyond endless layers of abstraction between you and the actual events. Luckily there are a few tools you can use to test, all of these are command line based and it is recomment that you get familar with them when you want to do any more complex configuration.</p>
<h3>EVTEST</h3>
<p> evtest lets you read raw input events from <i>/dev/input/eventX</i>. The event devices are the very core of all event handling, things like the joystick devices are derived from the event device, so if you want to fix some issue on the joystick device, you have to fix the event device. </p>
<p> evtest is available in the tools/ directory or as part of your distribution in the package <i>evtest</i>. your distribution.</p>
<h3>JSTEST</h3>
<p> jstest lets you read the output out of a joystick event device (/dev/input/js0). </p>
<p> jstest is available in the tools/ directory or as part of your distribution <i>joystick</i>.</p>
<h3>SDL-JSTEST</h3>
<p> sdl-jstest lets you see events as games using SDL see them. This is very important when you want to set and test the SDL_LINUX_JOYSTICK environment variables. </p>
<p> It is currently available via: </p>
<pre>
$ svn co <a href="svn://svn.berlios.de/windstille/trunk/sdl-jstest">svn://svn.berlios.de/windstille/trunk/sdl-jstest</a>
</pre>
<p> Or from the same Ubuntu PPA that also contains xboxdrv in the package <i>sdl-jstest</i>.</p>
<h3>XEV</h3>
<p> xev lets you see the events that Xorg sees. Note however that you might not see all events, since some will be grapped by your Window manager before they reach xev, this is normal. </p>
<p> xev is part of every Linux distribution, on Ubuntu its available via: </p>
<pre>
$ apt-get install x11-utils
</pre>
<h3>JSCALC AND JSCALIBRATOR</h3>
<p> Both of these tools lets you calibrate your gamepad, however with pretty much all current gamepads this is no longer needed and actually harmful as it might overwrite a perfectly good working configuration with a broken one (unplugging the gamepad or a reboot will fix that). So avoid them unless you clearly understand the issues of using them. </p>
<p> If your gamepad produces incorrect data and you do want to calibrate it you might want to check out the option <code>&#8211;calibration</code>, which lets you tweak the way xboxdrv interprets your gamepad data.</p>
<h3>MOUSE</h3>
<p> No tools for testing the output on /dev/input/mouseX are known.</p>
<h3>NOTE</h3>
<p> If the tools provide no output at all, this might not be due to a wrong configuration, but due to Xorg grabbing your event device and locking it, see Xorg section for possible fixes.</p>
<h2>EXAMPLES</h2>
<p> The configurations below are just a few random examples, further examples can be found in the <i>examples/</i> directory of the xboxdrv source tree or in <i>/usr/share/doc/xboxdrv/examples/</i>.</p>
<h3>TURNING TRIGGERS INTO BUTTONS</h3>
<p> By default xboxdrv will handle the trigger as analog axis, not buttons, while this is beneficial for racing games, it will confuse many other games, thus xboxdrv provides an easy way to change the handling into buttons via the <code>&#8211;trigger-as-button</code> option: </p>
<pre>
$ xboxdrv --trigger-as-button
</pre>
<h3>CONFIGURE A DEADZONE</h3>
<p> Many gamepads don&#8217;t center exactly at zero, but at random values around it. This &#8216;noise&#8217; can confuse some games and is thus be best filtered out, this can be accomplished with: </p>
<pre>
$ xboxdrv --deadzone 25%
</pre>
<p> The percentance is the amount of noise that will get filtered out, you can also give raw device values if you leave out the % sign. If you want to have a deadzone only on a specific axis you have to use axis filter: </p>
<pre>
$ xboxdrv --buttonmap X1^deadzone:15000
</pre>
<h3>KEYBOARD EMULATION</h3>
<p> The following configuration will cause xboxdrv to emulate a keyboard, which can be useful for games that are played with keyboard, like Flash games or games that don&#8217;t support a joystick. Since different games use different keyboard keys you might have to adjust the keybindings to fit the game: </p>
<pre>
$ xboxdrv \
  --ui-clear \
  --ui-buttonmap a=XK_a,b=XK_b,x=XK_x,y=XK_y \
  --ui-buttonmap dl=XK_Left,dr=XK_Right,du=XK_Up,dd=XK_Down
</pre>
<h3>FIGHTING GAMES:</h3>
<p> In this configuration the left and right trigger get turned into digital buttons. All axis except the dpad are ignored. RB and RT are mapped to act as if buttons 1,2 and 3 are pressed simultaniously which is useful for some special attacks. Instead of using the native button names, the 1,2,3,&#8230; aliases are used, which makes things a little easier to read: </p>
<p>$ xboxdrv&#8211; dpad &#8211; only&#8211; trigger &#8211; as &#8211; button&#8211; buttonmap lb = 1, x = 2, y = 3, lt = 4, a = 5, b = 6 &#8211;buttonmap rb = 1, rb = 2, rb = 3 &#8211;buttonmap rt = 4, rt = 5, rt = 6</p>
<h3>CH FLIGHTSTICK EMULATION IN DOSBOX:</h3>
<p> In <i>dosbox.conf</i> set: </p>
<pre>
[joystick]
joysticktype = ch
</pre>
<p> Start xboxdrv with: </p>
<p>$ xboxdrv &#8211; s&#8211; trigger &#8211; as &#8211; zaxis&#8211; square &#8211; axis&#8211; relative &#8211; axis y2 = 64000 &#8211;axismap &#8211; y2 = x2, x2 = y2</p>
<p> Your right analog stick will act as trottle control, the trigger as rudder. Using <code>&#8211;modifier</code> to install a four-way restrictor might also be worth a consideration to not accidently touch the throttle when the rudder is moved.</p>
<h3>USING MOUSE EMULATION AND JOYSTICK AT THE SAME TIME</h3>
<p> To use mouse emulation and joystick at the same time you have to register two configuration with xboxdrv, this works via: </p>
<pre>
$ xboxdrv --next-config --mouse
</pre>
<p> The <code>&#8211;next-config</code> option will open up a second configuration and all configuration options on the right side of it will go there, while everything on the left side of it will go into the first configuration. Toggling between the configurations works with the guide button, you can have as many configuratios as you want.</p>
<h3>MAPPING EVERY BUTTON MULTIPLE</h3>
<p> Some games might require more buttons then your gamepad has, in those situation it can be useful to map a button twice by using shifted buttons: </p>
<p>$ xboxdrv \<br />
  &#8211;ui-clear \<br />
  &#8211;ui-axismap X1=ABS_X,Y1=ABS_Y \<br />
  &#8211;ui-buttonmap a=JS_0,b=JS_1,x=JS_2,y=JS_3 \<br />
  &#8211;ui-buttonmap lb+a=JS_4,lb+b=JS_5,lb+x=JS_6,lb+y=JS_7 \<br />
  &#8211;ui-buttonmap rb+a=JS_8,rb+b=JS_9,rb+x=JS_10,rb+y=JS_11<br />
.fi<br />
Here all face buttons are get mapped three times, once when<br />
pressed normally, once when pressed while LB is held down and<br />
once when RB is held down, thus given you for the six buttons<br />
12 virtual ones.</p>
<h3>SAUERBRATEN</h3>
<p> First analogstick gets mapped te cursor keys, second analogstick gets mapped to mouse. Note: This is just an incomplete example, not a perfectly playable configuration, you have to do tweaking yourself. </p>
<p>$ xboxdrv&#8211; ui &#8211; axismap x2 = REL_X : 10, y2 = REL_Y : -10, x1 = KEY_LEFT : KEY_RIGHT, y1 = KEY_UP : KEY_DOWN&#8211; ui &#8211; buttonmap a = BTN_RIGHT, b = BTN_LEFT, x = BTN_EXTRA&#8211; ui &#8211; buttonmap rb = KEY_5, lb = KEY_6, lt = BTN_LEFT, rt = BTN_RIGHT&#8211; ui &#8211; buttonmap y = KEY_ENTER, dl = KEY_4, dr = KEY_2, du = KEY_1, dd = KEY_3, back = KEY_TAB, start = KEY_ESC &#8211; s&#8211; deadzone 6000 &#8211;dpad &#8211; as &#8211; button&#8211; trigger &#8211; as &#8211; button</p>
<h3>WARSOW</h3>
<p> Note: This is just an incomplete example, not a perfectly playable configuration, you have to do tweaking yourself. </p>
<p>$ xboxdrv&#8211; ui &#8211; axismap x2 = REL_X : 10, y2 = REL_Y : -10, x1 = KEY_A : KEY_D, y1 = KEY_W : KEY_S&#8211; ui &#8211; buttonmap a = KEY_LEFTSHIFT, b = BTN_C, x = BTN_EXTRA, y = KEY_C&#8211; ui &#8211; buttonmap lb = BTN_RIGHT, rb = KEY_SPACE&#8211; ui &#8211; buttonmap lt = KEY_Z, rt = BTN_LEFT&#8211; ui &#8211; buttonmap dl = KEY_4, dr = KEY_2, du = REL_WHEEL : -1 : 150, dd = REL_WHEEL : 1 : 150 &#8211;ui &#8211; buttonmap back = KEY_TAB, start = KEY_ESC &#8211; s&#8211; deadzone 6000 &#8211;dpad &#8211; as &#8211; button&#8211; trigger &#8211; as &#8211; button</p>
<h2>WRITING START-UP SCRIPTS FOR GAMES</h2>
<p> When you want full game specific configurability and automatic launching of xboxdrv, it is easiest to write little startup scripts for your games that will launch xboxdrv, launch your game and then when the game is finished tear down xboxdrv: </p>
<pre>
#!/bin/sh
exec xboxdrv \
  --trigger-as-button -s \
  -- \
  your_favorite_game
# EOF #
</pre>
<p> Here <i>your_favorite_game</i> is the executable of your game and is passed to xboxdrv as last argument. This will cause xboxdrv to start the game and keep running as long as the game is running, when the game is done, xboxdrv will quit automatically. </p>
<p> If you want to pass parameters to the game you have to add a <code>&#8212;</code> separator, as otherwise your options to the game would be eaten up by xboxdrv.</p>
<h2>SDL NOTES</h2>
<p> To let SDL know which axis act as a hat and which act as normal axis you have to set an environment variable: </p>
<pre>
$ SDL_LINUX_JOYSTICK=&quot;'Xbox Gamepad (userspace driver)' 6 1 0&quot;
$ export SDL_LINUX_JOYSTICK
</pre>
<p> You might also need in addition use this (depends on the way SDL was compiled): </p>
<pre>
$ SDL_JOYSTICK_DEVICE=&quot;/dev/input/js0&quot;
$ export SDL_JOYSTICK_DEVICE
</pre>
<p> This will let the DPad act as Hat in SDL based application. For many games the driver will work without this, but especially in Dosbox this variable is very important. </p>
<p> If you use options in xboxdrv that change the number of axis you have to adjust the variable accordingly, see:</p>
<dl>
<dt>&bull;</p>
<dd> &lt;<a href="ftp://ptah.lnf.kth.se/pub/misc/sdl-env-vars">ftp://ptah.lnf.kth.se/pub/misc/sdl-env-vars</a>&gt;</p>
<dt>SDL_LINUX_JOYSTICK</p>
<dd> Special joystick configuration string for linux. The format is <code>&quot;name numaxes numhats numballs&quot;</code> where name is the name string of the joystick (possibly in single quotes), and the rest are the number of axes, hats and balls respectively.</p>
<dt>SDL_JOYSTICK_DEVICE</p>
<dd> Joystick device to use in the linux joystick driver, in addition to the usual: <i>/dev/js*</i>, <i>/dev/input/event*</i>, <i>/dev/input/js*</i></dl>
<h2>TROUBLESHOOTING</h2>
<h3>&quot;NO XBOX OR XBOX360 CONTROLLER FOUND&quot;</h3>
<p> This means that either your controller isn&#8217;t plugged in or is not recognized by the driver. To fix this you need to know the idVendor and the idProduct numbers, which you can find out via: </p>
<pre>
$ lsusb -v
</pre>
<p> Once done you can try to add them to this array in <i>src/xpad_device.cpp</i>: </p>
<pre><code>
XPadDevice xpad_devices[] = {...}
</code></pre>
<p> If you have success with that, send a patch to &lt;grumbel [at] gmail.com&gt;, if not, contact me too, I might be able to provide additional help. </p>
<p> As an alternative you can also use the &#8211;device and &#8211;type option to enforce a USB device as well as a controller type an bypass any auto detection.</p>
<h3>&quot;UNKNOWN DATA: BYTES: 3 DATA: &#8230;&quot;</h3>
<p> This means that your controller is sending data that isn&#8217;t understood by the driver. If your controller still works, you can just ignore it, the Xbox360 controller seems to send out useless data every now and then. If your controller does not work and you get plenty of those lines when you move the sticks or press buttons it means that your controller talks an un-understood protocol and some reverse enginiering is required. Contact &lt;grumbel [at] gmail.com&gt; and include the output of: </p>
<pre>
$ lsusb -v
</pre>
<p> Along with all the &quot;Unknown data&quot; lines you get.</p>
<h3>&quot;ERROR: NO STUITABLE UINPUT DEVICE FOUND&quot;</h3>
<p> Make sure that uinput and joydev kernel modules are loaded. Make sure that you have a /dev/input/uinput, /dev/uinput or /dev/misc/uinput and permissions to access it. </p>
<p> Before reporting this as a bug make sure you have tested if the driver itself works with: </p>
<pre>
$ xboxdrv --no-uinput -v
</pre>
<h3>THE WIRELESS CONTROLLER DOESN&#8217;T WORK</h3>
<p> You have to sync the controller befor it can be used, restart of the driver isn&#8217;t needed and the driver should let you now when it recieves a connection after you sync the controller.</p>
<h3>KEYBOARD EMULATION</h3>
<p> When you try to let xboxdrv send a keyboard events via <code>&#8211;ui-buttonmap</code> or <code>&#8211;ui-axismap</code> Xorg must register the device as keyboard device to work properly. This seems to work automatically when you bind more then two keyboard keys, if you bind less you need to create the file <i>/etc/hal/fdi/preprobe/xboxdrv.fdi</i> containing: </p>
<pre>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;deviceinfo version=&quot;0.2&quot;&gt;
  &lt;device&gt;
    &lt;match key=&quot;input.product&quot; string=&quot;Xbox Gamepad (userspace driver) - Keyboard Emulation&quot;&gt;
      &lt;addset key=&quot;info.capabilities&quot; type=&quot;strlist&quot;&gt;input.keys&lt;/addset&gt;
    &lt;/match&gt;
  &lt;/device&gt;
&lt;/deviceinfo&gt;
</pre>
<p> This will tell HAL and later Xorg that xboxdrv acts as keyboard.</p>
<h3>WACOM ISSUES</h3>
<p> In some older kernels a Wacom graphic tablet creates a joystick device, so xboxdrv or any other real joysticks ends up as <i>/dev/input/js1</i> instead of <i>/dev/input/js0</i>. In many games this causes the joystick to not function any more. </p>
<p> A temporary workaround for this is to simply delete the joystick device js0 and replace it with a symbolic link js1 via: </p>
<pre>
$ sudo ln -sf /dev/input/js1 /dev/input/js0
</pre>
<p> This workaround will only last till the next reboot, since the device names are dynamically created, but for the time being there doesn&#8217;t seem to any other way to easily work around this issue. </p>
<p> In newer kernels this issue is fixed.</p>
<h3>UINPUT ISSUES</h3>
<p> On Ubuntu 9.04 the permissions of the uinput device have changed to 0640, meaning only root has access to the device. To change this back so that users in the group root have access the device and in turn can run xboxdrv without sudo you have to create a file called <i>/etc/udev/rules.d/55-permissions-uinput.rules</i> with the content: </p>
<pre>
KERNEL==&quot;uinput&quot;, MODE=&quot;0660&quot;, GROUP=&quot;root&quot;
</pre>
<h3>WINE ISSUES</h3>
<p> When using the Xbox360 gamepad in Wine it is not specially handled as Xbox360 gamepad, but as generic DirectInput gamepad. This means games will not display the proper button labels, but just numbers (i.e. &#8216;Btn1&#8217; instead of &#8216;A&#8217; for example). Aside from that it should work fine. </p>
<p> XInput support (the Microsoft DirectInput replacment, not the Xorg xinput) is as of January 2011 not implemented in Wine, so games that require XInput and don&#8217;t have an DirectInput fallback will not work with a Xbox360 controller, unofficial patches however do exist.</p>
<h2>XORG ISSUES</h2>
<p> If you start xboxdrv and instead of having a fully working joystick, you end up controlling the mouse that might be due to recent changes in Xorg and its device hotplug handling. There are four workarounds, the one that involves editing <i>/etc/hal/fdi/policy/preferences.fdi</i> is the recommont one.</p>
<h3>TEMPORARY WORKAROUND USING HAL-DEVICE</h3>
<p> Get the device id from hal: </p>
<pre>
$ hal-find-by-property --key 'info.product' --string 'Xbox Gamepad (userspace driver)'
</pre>
<p> Then remove the device from hal with: </p>
<pre>
$ hal-device -r $DEVICEID
</pre>
<h3>TEMPORARY WORKAROUND USING XINPUT</h3>
<p> Second workaround works with xinput: </p>
<pre>
$ xinput list
$ xinput set-int-prop $DEVICEID 'Device Enabled' 32 0
</pre>
<h3>PERMANENT WORKAROUND USING .FDI FILES</h3>
<p> The former two workarounds are just temporary and have to be redone after each start of xboxdrv, the last workaround is a permanent one: </p>
<p> You have to edit: </p>
<p> <i>/etc/hal/fdi/policy/preferences.fdi</i> </p>
<p> And insert the following lines: </p>
<pre>
&lt;match key=&quot;input.product&quot; string=&quot;Xbox Gamepad (userspace driver)&quot;&gt;
  &lt;remove key=&quot;input.x11_driver&quot; /&gt;
&lt;/match&gt;
</pre>
<h3>PERMANENT WORKAROUND BY DISABLING DEVICE AUTO DETECTION</h3>
<p> A fourth workaround involved disabling the autodetection of Xorg completly, you can do that by adding the following lines to <i>/etc/X11/xorg.conf</i>: </p>
<pre>
Section &quot;ServerFlags&quot;
  Option &quot;AutoAddDevices&quot; &quot;False&quot;
EndSection
</pre>
<p> Note that without auto detection you will have to manually configure all your mice and keyboards or your Xorg Server won&#8217;t start up properly. So unless you are already familiar with editing Xorg you better avoid this workaround. Workaround 3) has basically the same effect, except that auto detection only gets disabled for the single device it is causing problems.</p>
<h2>FORCE FEEDBACK PROGRAMMING</h2>
<p> For documentation on the FF interface see:</p>
<dl>
<dt>&bull;</p>
<dd> &lt;<a rel="nofollow" href="http://github.com/github/linux-2.6/blob/f3b8436ad9a8ad36b3c9fa1fe030c7f38e5d3d0b/Documentation/input/ff.txt">http://github.com/github/linux-2.6/blob/f3b8436ad9a8ad36b3c9fa1fe030c7f38e5d3d0b/Documentation/input/ff.txt</a>&gt;</p>
<dt>&bull;</p>
<dd> <i>/usr/include/linux/input.h</i></dl>
<p> Additional, non Linux related, force feedback related information can be found at:</p>
<dl>
<dt>&bull;</p>
<dd> &lt;<a rel="nofollow" href="http://www.immersion.com/developer/downloads/ImmFundamentals/HTML/">http://www.immersion.com/developer/downloads/ImmFundamentals/HTML/</a>&gt;</p>
<dt>&bull;</p>
<dd> &lt;<a rel="nofollow" href="http://msdn.microsoft.com/en-us/library/bb219655(VS.85).aspx">http://msdn.microsoft.com/en-us/library/bb219655(VS.85).aspx</a>&gt;</dl>
<p> <code>fftest</code> is an application you can use to test the force feedback interface. </p>
<p> Force feedback is disabed by default since it causes trouble in certain application. &quot;Tomb Raider: Legend&quot; for example when run in Wine crashes at startup when rumble is enabled, while it works perfectly normal when rumble is disabled.</p>
<h2>BUGS</h2>
<h3>X11 KEYSYM ISSUES</h3>
<p> X11 keysyms might not work correctly in <code>&#8211;ui-buttonmap a=XK_Foobar</code> when Foobar is mapped to multiple keycodes in the keymap. </p>
<p> Workaround: Use <code>KEY_</code> instead or cleanup your keymap </p>
<p> Newer versions of Xorg will also do perform some auto configuration that might lead to your keymap being switched whenever a new keyboard is detected, in cases of custom Xmodmaps this might confuse xboxdrv and make the XK_ style names unusable. No workaround for that is known right now.</p>
<h3>NON-INTERRUPTABLE PROCESSES DUE TO FORCE FEEDBACK</h3>
<p> Force feedback support is brittle, if you Ctrl-c the driver in the wrong moment you will end up with a dead uninterruptable process and basically have to reboot. This looks like it might be a kernel issue and not a xboxdrv one. </p>
<p> Workaround: Kill the app that uses xboxdrv before xboxdrv itself.</p>
<h3>QUESTIONS, BUG REPORTS AND FEATURE REQUESTS</h3>
<p> Bug reports and feature request can be report to the xboxdrv issue tracker at: </p>
<p> &lt;<a rel="nofollow" href="https://github.com/Grumbel/xboxdrv/issues/new">https://github.com/Grumbel/xboxdrv/issues/new</a>&gt; </p>
<p> General questions and requests for configuration help should be directed to the xboxdrv mailing list at: </p>
<p> &lt;<a rel="nofollow" href="http://groups.google.com/group/xboxdrv">http://groups.google.com/group/xboxdrv</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2010-2011 Ingo Ruhnke &lt;grumbel [at] gmail.com&gt; License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt; . This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xboxdrvctl/">xboxdrvctl</a></code>(1), <code><a href="/docs/linux/man/1-evtest/">evtest</a></code>(1), <code><a href="/docs/linux/man/1-jstest/">jstest</a></code>(1), <code><a href="/docs/linux/man/1-jstest-gtk/">jstest-gtk</a></code>(1), <code><a href="/docs/linux/man/1-xev/">xev</a></code>(1), <code><a href="/docs/linux/man/1-fftest/">fftest</a></code>(1), <code><a href="/docs/linux/man/1-lsusb/">lsusb</a></code>(1) </p>
<h2>Index</h2>
