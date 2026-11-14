---
title: "hwdb(7)"
name: "hwdb"
section: "7"
letter: "h"
url: "/docs/linux/man/7-hwdb/"
description: "hwdb – Hardware Database"
---

<p>hwdb &#8211; Hardware Database</p>
<h2>Description</h2>
<p>The hardware database is a key-value store for associating modalias-like keys to udev-property-like values. It is used primarily by udev to add the relevant properties to matching devices, but it can also be queried directly.</p>
<h2>Hardware Database Files</h2>
<p>The hwdb files are read from the files located in the system hwdb directory /lib/udev/hwdb.d and the local administration directory /etc/udev/hwdb.d. All hwdb files are collectively sorted and processed in lexical order, regardless of the directories in which they live. However, files with identical filenames replace each other. Files in /etc/ have the highest priority and take precedence over files with the same name in /lib/. This can be used to override a system-supplied hwdb file with a local file if needed; a symlink in /etc/ with the same name as a hwdb file in /lib/, pointing to /dev/null, disables that hwdb file entirely. hwdb files must have the extension .hwdb; other extensions are ignored. </p>
<p> Each hwdb file contains data records consisting of matches and associated key-value pairs. Every record in the hwdb starts with one or more match strings, specifying a shell glob to compare the lookup string against. Multiple match lines are specified in consecutive lines. Every match line is compared individually, and they are combined by OR. Every match line must start at the first character of the line. </p>
<p> Match patterns consist of literal characters, and shell-style wildcards: </p>
<dl>
<dd>&bull; Asterisk &quot;*&quot; matches any number of characters</dl>
<dl>
<dd>&bull; Question mark &quot;?&quot; matches a single character</dl>
<dl>
<dd>&bull; Character list &quot;[<i>chars</i>]&quot; matches one of the characters <i>chars</i> listed between &quot;[&quot; and &quot;]&quot;. A range may be specified as with a dash as &quot;[<i>first</i>&#8211;<i>last</i>]&quot;. The match may be inverted with a caret &quot;[^&#8230;]&quot;.</dl>
<p> The match lines are followed by one or more key-value pair lines, which are recognized by a leading space character. The key name and value are separated by &quot;=&quot;. An empty line signifies the end of a record. Lines beginning with &quot;#&quot; are ignored. </p>
<p> In case multiple records match a given lookup string, the key-value pairs from all records are combined. If a key is specified multiple times, the value from the record with the highest priority is used (each key can have only a single value). The priority is higher when the record is in a file that sorts later lexicographically, and in case of records in the same file, later records have higher priority. </p>
<p> The content of all hwdb files is read by <code><a href="/docs/linux/man/8-systemd-hwdb/">systemd-hwdb</a></code>(8) and compiled to a binary database located at /etc/udev/hwdb.bin, or alternatively /lib/udev/hwdb.bin if you want ship the compiled database in an immutable image. During runtime, only the binary database is used.</p>
<h2>Examples</h2>
<p><code>Example 1. General syntax of hwdb files</code> </p>
<dl>
<dd>
<pre># /lib/udev/hwdb.d/example.hwdb
# Comments can be placed before any records. This is a good spot
# to describe what that file is used for, what kind of properties
# it defines, and the ordering convention.
# A record with three matches and one property
mouse:*:name:*Trackball*:*
mouse:*:name:*trackball*:*
mouse:*:name:*TrackBall*:*
 ID_INPUT_TRACKBALL=1
# The rule above could be also be written in a form that
# matches Tb, tb, TB, tB:
mouse:*:name:*[tT]rack[bB]all*:*
 ID_INPUT_TRACKBALL=1
# A record with a single match and five properties
mouse:usb:v046dp4041:name:Logitech MX Master:*
 MOUSE_DPI=1000@166
 MOUSE_WHEEL_CLICK_ANGLE=15
 MOUSE_WHEEL_CLICK_ANGLE_HORIZONTAL=26
 MOUSE_WHEEL_CLICK_COUNT=24
 MOUSE_WHEEL_CLICK_COUNT_HORIZONTAL=14</pre>
</dl>
<p> <code>Example 2. Overriding of properties</code> </p>
<dl>
<dd>
<pre># /lib/udev/hwdb.d/60-keyboard.hwdb
evdev:atkbd:dmi:bvn*:bvr*:bd*:svnAcer*:pn*:*
 KEYBOARD_KEY_a1=help
 KEYBOARD_KEY_a2=setup
 KEYBOARD_KEY_a3=battery
# Match vendor name &quot;Acer&quot; and any product name starting with &quot;X123&quot;
evdev:atkbd:dmi:bvn*:bvr*:bd*:svnAcer:pnX123*:*
 KEYBOARD_KEY_a2=wlan
# /etc/udev/hwdb.d/70-keyboard.hwdb
# disable wlan key on all at keyboards
evdev:atkbd:*
 KEYBOARD_KEY_a2=reserved
 PROPERTY_WITH_SPACES=some string</pre>
</dl>
<p> If the hwdb consists of those two files, a keyboard with the lookup string &quot;evdev:atkbd:dmi:bvnAcer:bdXXXXX:bd08/05/2010:svnAcer:pnX123&quot; will match all three records, and end up with the following properties: </p>
<dl>
<dd>
<pre>KEYBOARD_KEY_a1=help
KEYBOARD_KEY_a2=reserved
KEYBOARD_KEY_a3=battery
PROPERTY_WITH_SPACES=some string</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-systemd-hwdb/">systemd-hwdb</a></code>(8) </p>
