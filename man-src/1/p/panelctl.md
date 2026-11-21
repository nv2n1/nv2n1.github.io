---

title: "panelctl(1)"
name: "panelctl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-panelctl/"
description: "panelctl – manual page for panelctl (libavc1394) 0.1"
---

<p> panelctl &#8211; manual page for panelctl (libavc1394) 0.1</p>
<h2>SYNOPSIS</h2>
<p> <code>panelctl</code> [<i>OPTION</i>] <i>&lt;channel|command&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>panelctl</code> is a command line tool to send control commands via an IEEE1394 link to an AV/C Panel such as the Motorola Digital Consumer Terminal (DCT) series. Or for the non-techies: <code>panelctl</code> lets you remote control your digital cable box via a Firewire cable.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> Display debug information</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Display this help and exit</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Output version information and exit</dd></dl>
<h3>Channels:</h3>
<dl>
<dt><code>001 &#8211; 999</code></dt>
<dd> Tune directly to a specific channel</dd></dl>
<h3>Commands:</h3>
<dl>
<dt><code>ok</code></dt>
<dd> Select the highlighted item</dd>
<dt><code>up</code></dt>
<dd> Move up in the menu or guide</dd>
<dt><code>down</code></dt>
<dd> Move down in the menu or guide</dd>
<dt><code>left</code></dt>
<dd> Move left in the menu or guide</dd>
<dt><code>right</code></dt>
<dd> Move right in the menu or guide</dd>
<dt><code>menu</code></dt>
<dd> Enter or Exit the Main Menu</dd>
<dt><code>lock</code></dt>
<dd> Bring up Parental Control screen</dd>
<dt><code>guide</code></dt>
<dd> Bring up Listings By Time screen</dd>
<dt><code>favorite</code></dt>
<dd> Scan through just your favorite channels</dd>
<dt><code>exit</code></dt>
<dd> Return to live TV from the menu or guide</dd>
<dt><code>enter</code></dt>
<dd> Enter the digital Music menu</dd>
<dt><code>channelup</code></dt>
<dd> Change channel up</dd>
<dt><code>channeldown</code></dt>
<dd> Change channel down</dd>
<dt><code>last</code></dt>
<dd> Return to the previous menu or channel</dd>
<dt><code>info</code></dt>
<dd> See a description of the current show</dd>
<dt><code>help</code></dt>
<dd> See helpful information</dd>
<dt><code>pageup</code></dt>
<dd> Move up one page in the menu or guide</dd>
<dt><code>pagedown</code></dt>
<dd> Move down one page in the menu or guide</dd>
<dt><code>power</code></dt>
<dd> Toggle the device on or off</dd>
<dt><code>volumeup</code></dt>
<dd> Change volume up</dd>
<dt><code>volumedown</code></dt>
<dd> Change volume down</dd>
<dt><code>mute</code></dt>
<dd> Toggle sound on or off</dd>
<dt><code>play</code></dt>
<dd> Play DVR or On-Demand content</dd>
<dt><code>stop</code></dt>
<dd> Stop DVR or On-Demand content</dd>
<dt><code>pause</code></dt>
<dd> Pause DVR or On-Demand content</dd>
<dt><code>record</code></dt>
<dd> Record content on the DVR</dd>
<dt><code>rewind</code></dt>
<dd> Rewind DVR or On-Demand content</dd>
<dt><code>fastforward</code></dt>
<dd> Fast Forward DVR or On-Demand content</dd>
<dt><code>soundoff</code></dt>
<dd> Turn sound off</dd>
<dt><code>soundon</code></dt>
<dd> Turn sound on</dd>
<dt><code>num0 &#8211; num9</code></dt>
<dd> Emulate a number key pressed</dd></dl>
<h2>AUTHOR</h2>
<dl>
<dt>Written by Stacey Son, John Woodell, and Dan Dennedy.</dt>
<dd></dd></dl>
<h2>COPYRIGHT</h2>
<dl>
<dt>Copyright (C) 2004-2006</dt>
<dd></dd></dl>
<h2>SEE ALSO</h2>
<dl>
<dt><code>dvcont</code></dt>
<dd>
</dd></dl>
