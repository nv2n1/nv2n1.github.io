---
title: "nxtrc(1)"
name: "nxtrc"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nxtrc/"
description: "nxtrc – a program to interact with LEGO NXT via BlueTooth"
---

<h2>NAME</h2>
<p> nxtrc &#8211; a program to interact with LEGO NXT via BlueTooth</p>
<h2>SYNOPSIS</h2>
<p> <code>nxtrc</code> [-s] </p>
<p> <code>nxtrc</code> [-a ADDR] [-v] command</p>
<h2>DESCRIPTION</h2>
<p> NXTRC (NXT Remote Command) is a small program that allows to send various commands to a LEGO Mindstorm NXT Brick. It uses the Bluetooth protocol through the Bluez libraries. </p>
<p> The option <code>-s</code> starts a scan to find BlueTooth devices. If a BT address is given in the command line or is in the Environment Variable BTADDR it connects to the NXT and performs the task specified in &lt;command&gt;. The first time you connect with a device you need to exchange a password, this task is usually done by the Operative System BlueTooth Management (as Kbluetooth under KDE). </p>
<h2>COMMANDS and OPTIONS</h2>
<dl>
<dt>-a</p>
<dd> BlueTooth Address of the NXT, <code>required</code> if BTADDR Environment Variable is not set to the address</p>
<dt>-b</p>
<dd> Get Battery Level</p>
<dt>-d FILE</p>
<dd> Delete FILE frome NXT</p>
<dt>-h</p>
<dd> display a short help text</p>
<dt>-i</p>
<dd> Get info on NXT brick</p>
<dt>-k</p>
<dd> Stop a program running on NXT</p>
<dt>-l[PATT]</p>
<dd> List files on NXT brick matching PATTern if present (e.g. -l*.rxe) N.B. No spaces between -l and PATT! see at the end the patterns allowed</p>
<dt>-m FILE</p>
<dd> Play sound file FILE once</p>
<dt>-M FILE</p>
<dd> Play sound file FILE indefinitely</p>
<dt>-n NAME</p>
<dd> Set NXT name to NAME</p>
<dt>-p FILE</p>
<dd> Run Program FILE on NXT</p>
<dt>-r FILE</p>
<dd> Read FILE frome NXT and save it in the working directory if FILE is already present ask for permission to overwrite</p>
<dt>-v</p>
<dd> Be verbose. This is the only option that can be given with another command. It&#8217;s not always very useful&#8230;.</p>
<dt>-w FILE</p>
<dd> Write FILE on NXT, If FILE is already present ask for permission to overwrite</p>
<dt>-W FILE</p>
<dd> Same as -w forcing overwrite if FILE exists</p>
<dt>-z</p>
<dd> Stop Sound Playback </p>
</dl>
<h2>File Names and Patterns</h2>
<p> On the NXT File names are of the form &quot;Name.Ext&quot; with max 15 characters for the Name and 3 for the Extension. When asking a listing with the <code>-l</code> command you can give a specific file name to see if it&#8217;s on the NXT and list its size, or a Pattern using widlcards. Due to the limitation of the NXT API patterns are limited to the form &quot;*.ext&quot;, &quot;Name.*&quot; or &quot;*.*&quot; this last one is the default and can be omitted. </p>
<h2>EXAMPLES</h2>
<p> scan for devices </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>nxtrc -s&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>00:10:20:30:40:50&nbsp;<wbr>&nbsp;<wbr>NXT1&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>00:01:01:02:03:04&nbsp;<wbr>&nbsp;<wbr>NXT2&nbsp;<wbr> </p>
<p> set up Environment Variable for connection with NXT1 and ask for info </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>export BTADDR=00:10:20:30:40:50 </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>nxtrc -i </p>
<p> load program Prog.rxe on NXT1 and run it </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>nxtrc -W Prog.rxe </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>nxtrc -p Prog.rxe </p>
<h2>EXIT STATUS</h2>
<p> <code>nxtrc</code> returns a zero exit status if it succeeds. Non zero is returned in case of failure.</p>
<h2>AUTHOR</h2>
<p> Gian Piero Puccioni (gianpiero.puccioni (at) isc.cnr.it) </p>
<h2>Index</h2>
