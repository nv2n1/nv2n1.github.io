---

title: "xbrlapi(1)"
name: "xbrlapi"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xbrlapi/"
description: "xbrlapi – X11 BrlAPI helper for Linux/Unix"
---

<p> <code>xbrlapi</code> [<i>option</i> &#8230;]</p>
<p> <code>xbrlapi</code> connects to a <code>BrlAPI</code> server in order to provide it with the ID of the <code>X11</code> window which currently has focus. It also simulates <code>X</code> keysyms from braille key presses (else brltty would simulate them using a qwerty keyboard). By default, it puts itself in the background, unless option <code>-n</code> is given.</p>
<h2>OPTIONS</h2>
<p> Options are processed sequentially from left to right. If an option is specified more than once, or in case of a conflict, the rightmost specification takes precedence. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>-b</code> [<i>host</i>][:<i>port</i>] (<code>&#8211;brlapi=</code>)</dt>
<dd> The <code>BrlAPI</code> server to connect to.</dd>
<dt><code>-a</code> <i>string</i> (<code>&#8211;auth=</code>)</dt>
<dd> The <code>BrlAPI</code> authorization/authentication string.</dd>
<dt><code>-d</code> <i>display</i> (<code>&#8211;display=</code>)</dt>
<dd> The <code>X</code> display to connect to. If not specified, the content of the <code>DISPLAY</code> environment variable is used.</dd>
<dt><code>-n</code> (<code>&#8211;no-daemon</code>)</dt>
<dd> Keep xbrlapi in the foreground.</dd>
<dt><code>-q</code> (<code>&#8211;quiet</code>)</dt>
<dd> Do not write any text to the braille device.</dd>
<dt><code>-h</code> (<code>&#8211;help</code>)</dt>
<dd> Print a command line usage summary and then exit.</dd>
<dt><code>-H</code> (<code>&#8211;full-help</code>)</dt>
<dd> Print a thorough command line usage summary and then exit.</dd></dl>
<h2>SEE ALSO</h2>
<p> For more details on the purpose of <code>xbrlapi</code>, see <code>BrlAPI</code>&#8216;s on-line manual at [<code><a rel="nofollow" href="http://brltty.app/doc/Manual-BrlAPI/English/BrlAPI-3.html">http://brltty.app/doc/Manual-BrlAPI/English/BrlAPI-3.html</a></code>]. </p>
