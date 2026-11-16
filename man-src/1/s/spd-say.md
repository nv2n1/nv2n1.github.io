---
title: "spd-say(1)"
name: "spd-say"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spd-say/"
description: "spd-say – send text-to-speech output request to speech-dispatcher"
---

<h2 class="name">NAME</h2>
<p> spd-say &#8211; send text-to-speech output request to speech-dispatcher </p>
<h2>SYNOPSIS</h2>
<p> <code>spd-say</code> [<i>,options/</i>] <i>,&quot;some text&quot;/</i></p>
<h2>DESCRIPTION</h2>
<p> send text-to-speech output request to speech-dispatcher</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code>, <code>&#8211;rate</code></dt>
<dd> Set the rate of the speech (between <code>-100</code> and +100, default: 0)</dd>
<dt><code>-p</code>, <code>&#8211;pitch</code></dt>
<dd> Set the pitch of the speech (between <code>-100</code> and +100, default: 0)</dd>
<dt><code>-R</code>, <code>&#8211;pitch-range</code></dt>
<dd> Set the pitch range of the speech (between <code>-100</code> and +100, default: 0)</dd>
<dt><code>-i</code>, <code>&#8211;volume</code></dt>
<dd> Set the volume (intensity) of the speech (between <code>-100</code> and +100, default: 0)</dd>
<dt><code>-o</code>, <code>&#8211;output-module</code></dt>
<dd> Set the output module</dd>
<dt><code>-O</code>, <code>&#8211;list-output-modules</code></dt>
<dd> Get the list of output modules</dd>
<dt><code>-I</code>, <code>&#8211;sound-icon</code></dt>
<dd> Play the sound icon</dd>
<dt><code>-l</code>, <code>&#8211;language</code></dt>
<dd> Set the language (ISO code)</dd>
<dt><code>-t</code>, <code>&#8211;voice-type</code></dt>
<dd> Set the preferred voice type (male1, male2, male3, female1, female2 female3, child_male, child_female)</dd>
<dt><code>-L</code>, <code>&#8211;list-synthesis-voices</code></dt>
<dd> Get the list of synthesis voices</dd>
<dt><code>-y</code>, <code>&#8211;synthesis-voice</code></dt>
<dd> Set the synthesis voice</dd>
<dt><code>-c</code>, <code>&#8211;character</code></dt>
<dd> Speak the character</dd>
<dt><code>-k</code>, <code>&#8211;key</code></dt>
<dd> Speak the key</dd>
<dt><code>-m</code>, <code>&#8211;punctuation-mode</code></dt>
<dd> Set the punctuation mode (none, some, most, all)</dd>
<dt><code>-s</code>, <code>&#8211;spelling</code></dt>
<dd> Spell the message</dd>
<dt><code>-x</code>, <code>&#8211;ssml</code></dt>
<dd> Set SSML mode on (default: off)</dd>
<dt><code>-e</code>, <code>&#8211;pipe-mode</code></dt>
<dd> Pipe from stdin to stdout plus Speech Dispatcher</dd>
<dt><code>-P</code>, <code>&#8211;priority</code></dt>
<dd> Set priority of the message (important, message, text, notification, progress;default: text)</dd>
<dt><code>-N</code>, <code>&#8211;application-name</code></dt>
<dd> Set the application name used to establish the connection to specified string value (default: spd-say)</dd>
<dt><code>-n</code>, <code>&#8211;connection-name</code></dt>
<dd> Set the connection name used to establish the connection to specified string value (default: main)</dd>
<dt><code>-w</code>, <code>&#8211;wait</code></dt>
<dd> Wait till the message is spoken or discarded</dd>
<dt><code>-S</code>, <code>&#8211;stop</code></dt>
<dd> Stop speaking the message being spoken</dd>
<dt><code>-C</code>, <code>&#8211;cancel</code></dt>
<dd> Cancel all messages</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Print version and copyright info</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print this info</dd></dl>
<p> Please report bugs to speechd-discuss [at] nongnu.org</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2012 Brailcom, o.p.s.<br />
 This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. Please see COPYING for more details.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>spd-say</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>spd-say</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info spd-say</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
