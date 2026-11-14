---
title: "panelctl(1)"
name: "panelctl"
section: "1"
letter: "p"
url: "/docs/linux/man/1-panelctl/"
description: "panelctl – manual page for panelctl (libavc1394) 0.1"
---

<h2>NAME</h2>
<p> panelctl &#8211; manual page for panelctl (libavc1394) 0.1</p>
<h2>SYNOPSIS</h2>
<p> <code>panelctl</code> [<i>OPTION</i>] <i>&lt;channel|command&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>panelctl</code> is a command line tool to send control commands via an IEEE1394 link to an AV/C Panel such as the Motorola Digital Consumer Terminal (DCT) series. Or for the non-techies: <code>panelctl</code> lets you remote control your digital cable box via a Firewire cable.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Display debug information</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display this help and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Output version information and exit</dl>
<h3>Channels:</h3>
<dl>
<dt><code>001 &#8211; 999</code></p>
<dd> Tune directly to a specific channel</dl>
<h3>Commands:</h3>
<dl>
<dt><code>ok</code></p>
<dd> Select the highlighted item</p>
<dt><code>up</code></p>
<dd> Move up in the menu or guide</p>
<dt><code>down</code></p>
<dd> Move down in the menu or guide</p>
<dt><code>left</code></p>
<dd> Move left in the menu or guide</p>
<dt><code>right</code></p>
<dd> Move right in the menu or guide</p>
<dt><code>menu</code></p>
<dd> Enter or Exit the Main Menu</p>
<dt><code>lock</code></p>
<dd> Bring up Parental Control screen</p>
<dt><code>guide</code></p>
<dd> Bring up Listings By Time screen</p>
<dt><code>favorite</code></p>
<dd> Scan through just your favorite channels</p>
<dt><code>exit</code></p>
<dd> Return to live TV from the menu or guide</p>
<dt><code>enter</code></p>
<dd> Enter the digital Music menu</p>
<dt><code>channelup</code></p>
<dd> Change channel up</p>
<dt><code>channeldown</code></p>
<dd> Change channel down</p>
<dt><code>last</code></p>
<dd> Return to the previous menu or channel</p>
<dt><code>info</code></p>
<dd> See a description of the current show</p>
<dt><code>help</code></p>
<dd> See helpful information</p>
<dt><code>pageup</code></p>
<dd> Move up one page in the menu or guide</p>
<dt><code>pagedown</code></p>
<dd> Move down one page in the menu or guide</p>
<dt><code>power</code></p>
<dd> Toggle the device on or off</p>
<dt><code>volumeup</code></p>
<dd> Change volume up</p>
<dt><code>volumedown</code></p>
<dd> Change volume down</p>
<dt><code>mute</code></p>
<dd> Toggle sound on or off</p>
<dt><code>play</code></p>
<dd> Play DVR or On-Demand content</p>
<dt><code>stop</code></p>
<dd> Stop DVR or On-Demand content</p>
<dt><code>pause</code></p>
<dd> Pause DVR or On-Demand content</p>
<dt><code>record</code></p>
<dd> Record content on the DVR</p>
<dt><code>rewind</code></p>
<dd> Rewind DVR or On-Demand content</p>
<dt><code>fastforward</code></p>
<dd> Fast Forward DVR or On-Demand content</p>
<dt><code>soundoff</code></p>
<dd> Turn sound off</p>
<dt><code>soundon</code></p>
<dd> Turn sound on</p>
<dt><code>num0 &#8211; num9</code></p>
<dd> Emulate a number key pressed</dl>
<h2>AUTHOR</h2>
<dl>
<dt>Written by Stacey Son, John Woodell, and Dan Dennedy.</p>
<dd></dl>
<h2>COPYRIGHT</h2>
<dl>
<dt>Copyright (C) 2004-2006</p>
<dd></dl>
<h2>SEE ALSO</h2>
<dl>
<dt><code>dvcont</code></p>
<dd>
</dl>
<h2>Index</h2>
