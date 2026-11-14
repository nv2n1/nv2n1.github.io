---
title: "libinput-record(1)"
name: "libinput-record"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-record/"
description: "libinput-record – record kernel events"
---

<h2 class="name">NAME</h2>
<p> libinput-record &#8211; record kernel events </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput record [options] [</code><i>/dev/input/event0</i><code> [</code><i>/dev/input/event1</i><code> &#8230;]]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput record</code> tool records kernel events from a device and prints them in a format that can later be replayed with the <code>libinput <a href="/docs/linux/man/1-replay/">replay</a>(1)</code> tool. This tool needs to run as root to read from the device. </p>
<p> The output of this tool is YAML, see <code>FILE FORMAT</code> for more details. By default it prints to stdout unless the <code>-o</code> option is given. </p>
<p> The events recorded are independent of libinput itself, updating or removing libinput will not change the event stream.</p>
<h2>OPTIONS</h2>
<p> If one or more device nodes are given, this tool opens those device nodes. Otherwise, a list of devices is presented and the user can select the device to record. If unsure, run without any arguments.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help</p>
<dt><code>&#8211;all</code></p>
<dd> Record all <i>/dev/input/event*</i> devices available on the system. This option should be used in exceptional cases only, the output file is almost always too noisy and replaying the recording may not be possible. This option requires <code>&#8211;output-file</code> and no device nodes may be provided on the commandline.</p>
<dt><code>&#8211;autorestart=s</code></p>
<dd> Terminate the current recording after <i>s</i> seconds of device inactivity. This option requires that a <code>&#8211;output-file</code> is specified. The output filename is used as prefix, suffixed with the date and time of the recording. The timeout must be greater than 0.</p>
<dt><code>-o filename.yml</code></p>
<dd>
<dt><code>&#8211;output-file=filename.yml</code></p>
<dd> Specifies the output file to use. If <code>&#8211;autorestart</code> is given, the filename is used as prefix only.</p>
<dt><code>&#8211;show-keycodes</code></p>
<dd> Show keycodes as-is in the recording. By default, common keys are obfuscated and printed as <code>KEY_A</code> to avoid information leaks.</p>
<dt><code>&#8211;with-libinput</code></p>
<dd> Record libinput events alongside device events. <code>THIS FEATURE IS EXPERIMENTAL.</code> See section <code>RECORDING LIBINPUT EVENTS</code> for more details. </p>
</dl>
<h2>RECORDING MULTIPLE DEVICES</h2>
<p> Sometimes it is necessary to record the events from multiple devices simultaneously, e.g. when an interaction between a touchpad and a keyboard causes a bug. <code>libinput record</code> records multiple devices with an identical time offset, allowing for correct replay of the interaction. </p>
<p> If multiple devices are recorded, an output filename must be provided. </p>
<p> All devices to be recorded must be provided on the commandline, an example invocation is: </p>
<p> <code>libinput record -o tap-bug /dev/input/event3 /dev/input/event7</code> </p>
<p> Note that when recording multiple devices, only the first device is printed immediately, all other devices and their events are printed on exit. </p>
<h2>RECORDING LIBINPUT EVENTS</h2>
<p> When the <code>&#8211;with-libinput</code> switch is provided, <code>libinput-record</code> initializes a libinput context for the devices being recorded. Events from these contexts are printed alongside the evdev events. <code>THIS FEATURE IS EXPERIMENTAL.</code> </p>
<p> The primary purpose of this feature is debugging and event analysis, no caller may rely on any specific format of the events. </p>
<p> Note that while libinput and <code>libinput-record</code> see the same events from the device nodes, no guarantee can be given about the correct order of events. libinput events may come in earlier or later than the events from the device nodes and for some devices, libinput may internally alter the event stream before processing. </p>
<p> Note that the libinput context created by <code>libinput-record</code> does not affect the running desktop session and does not (can not!) copy any configuration options from that session. </p>
<h2>FILE FORMAT</h2>
<p> The output file format is in YAML and intended to be both human-readable and machine-parseable. Below is a short example YAML file, all keys are detailed further below. </p>
<p> Any parsers must ignore keys not specified in the file format description. The version number field is only used for backwards-incompatible changes. </p>
<pre><code>
version : 1 ndevices : 2 libinput : version : 1.10.0 system : os : "fedora:26" kernel : "4.13.9-200.fc26.x86_64" dmi : "dmi:bvnLENOVO:bvrGJET72WW(2.22):bd02/21/2014:svnLENOVO:..." devices : -node : / dev / input / event9 evdev :
#Name : Synaptics TM2668 - 002
#ID : bus 0x1d vendor 0x6cb product 00 version 00
#Size in mm : 97x68
#Supported Events:
#Event type 0(EV_SYN)
#..abbreviated for man page...
#
    name : Synaptics TM2668 -
    002 id : [ 29, 1739, 0, 0 ] codes : 0 : [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ] #EV_SYN 1 : [ 272, 325, 328, 330, 333, 334, 335 ] #EV_KEY 3 : [ 0, 1, 24, 47, 48, 49, 52, 53, 54, 55, 57, 58 ] #EV_ABS absinfo : 0 : [ 0, 4089, 0, 0, 42 ] 1 : [ 0, 2811, 0, 0, 41 ] 24 : [ 0, 255, 0, 0, 0 ] 47 : [ 0, 4, 0, 0, 0 ] 48 : [ 0, 15, 0, 0, 0 ] 49 : [ 0, 15, 0, 0, 0 ] 52 : [ 0, 1, 0, 0, 0 ] 53 : [ 0, 4089, 0, 0, 42 ] 54 : [ 0, 2811, 0, 0, 41 ] 55 : [ 0, 2, 0, 0, 0 ] 57 : [ 0, 65535, 0, 0, 0 ] 58 : [ 0, 255, 0, 0, 0 ] properties : [ 0, 2, 4 ] hid : [ 12, 23, 34, 45, ... ] udev : properties : -ID_INPUT_MOUSE = 1 - ID_INPUT = 1 quirks : -ModelAppleTouchpad = 1 - AttrSizeHint = 32x32 events : -evdev : -[ 0, 0, 3, 57, 1420 ] #EV_ABS / ABS_MT_TRACKING_ID 1420 - [ 0, 0, 3, 53, 1218 ] #EV_ABS / ABS_MT_POSITION_X 1218 - [ 0, 0, 3, 54, 1922 ] #EV_ABS / ABS_MT_POSITION_Y 1922 - [ 0, 0, 3, 52, 0 ] #EV_ABS / ABS_MT_ORIENTATION 0 - [ 0, 0, 3, 58, 47 ] #EV_ABS / ABS_MT_PRESSURE 47 - [ 0, 0, 1, 330, 1 ] #EV_KEY / BTN_TOUCH 1 - [ 0, 0, 1, 325, 1 ] #EV_KEY / BTN_TOOL_FINGER 1 - [ 0, 0, 3, 0, 1218 ] #EV_ABS / ABS_X 1218 - [ 0, 0, 3, 1, 1922 ] #EV_ABS / ABS_Y 1922 - [ 0, 0, 3, 24, 47 ] #EV_ABS / ABS_PRESSURE 47 - [ 0, 0, 0, 0, 0 ] #-- -- -- -- -- --SYN_REPORT(0)-- -- -- -+0ms - evdev : -[ 0, 11879, 3, 53, 1330 ] #EV_ABS / ABS_MT_POSITION_X 1330 - [ 0, 11879, 3, 54, 1928 ] #EV_ABS / ABS_MT_POSITION_Y 1928 - [ 0, 11879, 3, 58, 46 ] #EV_ABS / ABS_MT_PRESSURE 46 - [ 0, 11879, 3, 0, 1330 ] #EV_ABS / ABS_X 1330 - [ 0, 11879, 3, 1, 1928 ] #EV_ABS / ABS_Y 1928 - [ 0, 11879, 3, 24, 46 ] #EV_ABS / ABS_PRESSURE 46 - [ 0, 11879, 0, 0, 0 ] #-- -- -- -- -- --SYN_REPORT(0)-- -- -- -+0ms
#second device(if any)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  - node : / dev / input / event9 evdev : ...
</code></pre>
<p> Top-level keys are listed below, see the respective subsection for details on each key. </p>
<dl>
<dt><code>version: int</code></p>
<dd> The file format version. This version is only increased for backwards-incompatible changes. A parser must ignore unknown keys to be forwards-compatible.</p>
<dt><code>ndevices: int</code></p>
<dd> The number of device recordings in this file. Always 1 unless recorded with <code>&#8211;multiple</code></p>
<dt><code>libinput: {&#8230;}</code></p>
<dd> A dictionary with libinput-specific information.</p>
<dt><code>system: {&#8230;}</code></p>
<dd> A dictionary with system information.</p>
<dt><code>devices: {&#8230;}</code></p>
<dd> A list of devices containing the description and and events of each device. </p>
</dl>
<h3>libinput</h3>
<dl>
<dt><code>version: string</code></p>
<dd> libinput version </p>
</dl>
<h3>system</h3>
<p> Information about the system</p>
<dl>
<dt><code>os: string</code></p>
<dd> Distribution ID and version, see <i><a href="/docs/linux/man/5-os-release/">os-release</a>(5)</i></p>
<dt><code>kernel: string</code></p>
<dd> Kernel version, see <i><a href="/docs/linux/man/1-uname/">uname</a>(1)</i></p>
<dt><code>dmi: string</code></p>
<dd> DMI modalias, see <i>/sys/class/dmi/id/modalias</i> </p>
</dl>
<h3>devices</h3>
<p> Information about and events from the recorded device nodes</p>
<dl>
<dt><code>node: string</code></p>
<dd> the device node recorded</p>
<dt><code>evdev</code></p>
<dd> A dictionary with the evdev device information.</p>
<dt><code>hid</code></p>
<dd> A list of integers representing the HID report descriptor bytes.</p>
<dt><code>udev</code></p>
<dd> A dictionary with the udev device information.</p>
<dt><code>events</code></p>
<dd> A list of dictionaries with the recorded events</dl>
<h3>evdev</h3>
<dl>
<dt><code>name: string</code></p>
<dd> The device name</p>
<dt><code>id: [bustype, vendor, product, version]</code></p>
<dd> The data from the <code>struct input_id</code>, bustype, vendor, product, version.</p>
<dt><code>codes: {type: [a, b, c ], &#8230;}</code></p>
<dd> All evdev types and codes as nested dictionary. The evdev type is the key, the codes are a list.</p>
<dt><code>absinfo: {code: [min, max, fuzz, flat, resolution], &#8230;}</code></p>
<dd> An array of arrays with 6 decimal elements each, denoting the contents of a <code>struct input_absinfo</code>. The first element is the code (e.g. <code>ABS_X</code>) in decimal format.</p>
<dt><code>properties: [0, 1, &#8230;]</code></p>
<dd> Array with all <code>INPUT_PROP_FOO</code> constants. May be an empty array.</dl>
<h3>udev</h3>
<dl>
<dt><code>properties: list of strings</code></p>
<dd> A list of udev properties in the <code>key=value</code> format. This is not the complete list of properties assigned to the device but a subset that is relevant to libinput. These properties may include properties set on a parent device.</p>
<dt><code>quirks: list of strings</code></p>
<dd> A list of device quirks the <code>key=value</code> format. </p>
</dl>
<h3>events</h3>
<p> A list of the recorded events. The list contains dictionaries Information about the events. The content is a list of dictionaries, with the string identifying the type of event sequence.</p>
<dl>
<dt><code>{ evdev: [ {data: [sec, usec, type, code, value]}, &#8230;] }</code></p>
<dd> Each <code>input_event</code> dictionary contains the contents of a <code>struct input_event</code> in decimal format. The last item in the list is always the <code>SYN_REPORT</code> of this event frame. The next event frame starts a new <code>evdev</code> dictionary entry in the parent <code>events</code> list. </p>
</dl>
<h2>NOTES</h2>
<p> This tool records events from the kernel and is independent of libinput. In other words, updating or otherwise changing libinput will not alter the output from this tool. libinput itself does not need to be in use to record events.</p>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
