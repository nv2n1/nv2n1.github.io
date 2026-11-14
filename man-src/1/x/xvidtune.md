---
title: "xvidtune(1)"
name: "xvidtune"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvidtune/"
description: "xvidtune – video mode tuner for Xorg"
---

<h2 class="name">NAME</h2>
<p> xvidtune &#8211; video mode tuner for Xorg </p>
<h2>SYNOPSIS</h2>
<p> <code>xvidtune</code> [ <code>-show</code> | <code>-prev</code> | <code>-next</code> | <code>-unlock</code> ] [ <i>-toolkitoption</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> Xvidtune is a client interface to the X server video mode extension (XFree86-VidModeExtension). </p>
<p> When given one of the non-toolkit options, xvidtune provides a command line interface to either print or switch the video mode. </p>
<p> Without any options (or with only toolkit options) it presents the user with various buttons and sliders that can be used to interactively adjust existing video modes. It will also print the settings in a format suitable for inclusion in an xorg.conf file. </p>
<p> Normally the Xorg X servers only allow changes to be made with the XFree86-VidModeExtension from clients connected via a local connection type. </p>
<p> Note: The original mode settings can be restored by pressing the `R&#8217; key, and this can be used to restore a stable screen in situations where the screen becomes unreadable. </p>
<p> The available buttons are: </p>
<pre>
<code>Left</code>
<code>Right</code>
<code>Up</code>
<code>Down</code>
</pre>
<dl>
<dt>
<dd> Adjust the video mode so that the display will be moved in the appropriate direction.</dl>
<pre>
<code>Wider</code>
<code>Narrower</code>
<code>Shorter</code>
<code>Taller</code>
</pre>
<dl>
<dt>
<dd> Adjust the video mode so that the display size is altered appropriately.</dl>
<dl>
<dt><code>Quit</code></p>
<dd> Exit the program.</p>
<dt><code>Apply</code></p>
<dd> Adjust the current video mode to match the selected settings.</p>
<dt><code>Auto</code></p>
<dd> Cause the Up/Down/Right/Left, Wider/Narrower/Shorter/Taller, Restore, and the special S3 buttons to be applied immediately. This button can be toggled.</p>
<dt><code>Test</code></p>
<dd> Temporarily switch to the selected settings.</p>
<dt><code>Restore</code></p>
<dd> Return the settings to their original values.</p>
<dt><code>Fetch</code></p>
<dd> Query the server for its current settings.</p>
<dt><code>Show</code></p>
<dd> Print the currently selected settings to stdout in xorg.conf &quot;Modeline&quot; format. The primary selection is similarly set.</p>
<dt><code>Next</code></p>
<dd> Switch the Xserver to the next video mode.</p>
<dt><code>Prev</code></p>
<dd> Switch the Xserver to the previous video mode.</dl>
<p> For some S3-based cards (964 and 968) the following are also available:</p>
<dl>
<dt><code>InvertVCLK</code></p>
<dd> Change the VCLK invert/non-invert state.</p>
<dt><code>EarlySC</code></p>
<dd> Change the Early SC state. This affects screen wrapping.</dl>
<pre>
<code>BlankDelay1</code>
<code>BlankDelay2</code>
</pre>
<dl>
<dt>
<dd> Set the blank delay values. This affects screen wrapping. Acceptable values are in the range 0-7. The values may be incremented or decremented with the `+&#8217; and `-&#8216; buttons, or by pressing the `+&#8217; or `-&#8216; keys in the text field.</dl>
<p> For S3-864/868 based cards <i>InvertVCLK</i> and <i>BlankDelay1</i> may be useful. For S3 Trio32/Trio64 cards only <i>InvertVCLK</i> is available. At the moment there are no default settings available for these chips in the video mode extension and thus this feature is disabled in xvidtune. It can be enabled by setting any of the optional S3 commands in the screen section of xorg.conf, e.g. using</p>
<dl>
<dt>
<dd> <code>blank_delay </code><i>*</i> 0</dl>
<h2>OPTIONS</h2>
<p> <i>xvidtune</i> accepts the standard X Toolkit command line options as well as the following:</p>
<dl>
<dt><code>-show</code></p>
<dd> Print the current settings to stdout in xorg.conf &quot;Modeline&quot; format and exit.</p>
<dt><code>-prev</code></p>
<dd> Switch the Xserver to the previous video mode.</p>
<dt><code>-next</code></p>
<dd> Switch the Xserver to the next video mode.</p>
<dt><code>-unlock</code></p>
<dd> Normally, <i>xvidtune</i> will disable the switching of video modes via hot-keys while it is running. If for some reason the program did not exit cleanly and they are still disabled, the program can be re-run with this option to re-enable the mode switching key combinations.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xrandr/">xrandr</a></code>(1), <code><a href="/docs/linux/man/1-xorg/">Xorg</a></code>(1), <code><a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a></code>(5).</p>
<h2>AUTHORS</h2>
<p> Kaleb S. Keithley, X Consortium.<br />
 Additions and modifications by Jon Tombs, David Dawes, and Joe Moss.</p>
<h2>BUGS</h2>
<p> X Error handling, i.e. when the server does not allow xvidtune clients to write new modes, could be better. </p>
<h2>Index</h2>
