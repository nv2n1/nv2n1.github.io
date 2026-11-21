---

title: "transset(1)"
name: "transset"
section: "1"
letter: "t"
url: "/docs/linux/man/1-transset/"
description: "transset – Set transparency on a window"
---

<p> <code>transset</code> [<i>-options &#8230;</i>] [<i>opacity</i>]</p>
<p> <code>transset</code> is a simple program for X servers supporting the XFIXES, DAMAGE, and COMPOSITE extensions. It lets the user set the transparency on a window. </p>
<p> The <i>opacity</i> value is a number from 0 to 1, with zero being fully transparent and 1 being fully opaque. If no <i>opacity</i> argument is given, a default value of 0.75 is used for the opacity value. If neither <code>&#8211;inc</code> nor <code>&#8211;dec</code> are given, the opacity is treated as an absolute value and set to the given opacity value. If <code>&#8211;inc</code> or <code>&#8211;dec</code> is specified, then the opacity is treated as a relative value to increase or decrease the current opacity by.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>display</i></dt>
<dd> This option specifies the server to use; see <i><a href="/docs/linux/man/7-x/">X</a>(7)</i>.</dd></dl>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> This option displays a help message and exits.</dd></dl>
<dl>
<dt><code>-t</code>, <code>&#8211;toggle</code></dt>
<dd> This option forces a toggle of opacity. If the current opacity is not set to fully opaque (opacity 1.0), it will be reset to fully opaque. If the window is already fully opaque, the opacity will be set normally.</dd></dl>
<dl>
<dt><code>-c</code>, <code>&#8211;click</code></dt>
<dd> This option selects the target window by waiting for the user to click the mouse &#8211; the topmost window under the mouse cursor when the mouse click occurs will be used as the target.</dd></dl>
<dl>
<dt><code>-p</code>, <code>&#8211;point</code></dt>
<dd> This option selects the window currently under the cursor to be the target.</dd></dl>
<dl>
<dt><code>-a</code>, <code>&#8211;actual</code></dt>
<dd> This option selects the window that currently has input focus to be the target.</dd></dl>
<dl>
<dt><code>-n</code>, <code>&#8211;name</code> <i>name</i></dt>
<dd> This option selects the target window by name, where <i>name</i> is matched as a regular expression, unless <code>&#8211;no-regex</code> is also specified.</dd></dl>
<dl>
<dt><code>&#8211;no-regex</code></dt>
<dd> This option disables treating the <i>name</i> argument to <code>&#8211;name</code> as a regular expression.</dd></dl>
<dl>
<dt><code>-i</code>, <code>&#8211;id</code></dt>
<dd> This option selects the target window by window id.</dd></dl>
<dl>
<dt><code>&#8211;inc</code></dt>
<dd> This option increases the window opacity by the given <i>opacity</i> argument.</dd></dl>
<dl>
<dt><code>&#8211;dec</code></dt>
<dd> This option decreases the window opacity by the given <i>opacity</i> argument.</dd></dl>
<dl>
<dt><code>-m</code>, <code>&#8211;min</code> <i>opacity</i></dt>
<dd> This option sets the minimum possible opacity value. It defaults to 0 if this option is not given.</dd></dl>
<dl>
<dt><code>-x</code>, <code>&#8211;max</code> <i>opacity</i></dt>
<dd> This option sets the maximum possible opacity value. It defaults to 1 if this option is not given.</dd></dl>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> This option prints some additional debug info as the program operates.</dd></dl>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> This option prints the program version number and exits.</dd></dl>
<h2>BUGS</h2>
<p> Probably. Please report any you find to <a rel="nofollow" href="https://bugs.freedesktop.org/enter_bug.cgi?product=xorg.">https://bugs.freedesktop.org/enter_bug.cgi?product=xorg.</a></p>
<h2>AUTHORS</h2>
<p> Matthew Hawn </p>
