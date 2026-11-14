---
title: "isdn_audio(4)"
name: "isdn_audio"
section: "4"
letter: "i"
url: "/docs/linux/man/4-isdn_audio/"
description: "isdn_audio – audio extension of ttyI ISDN character devices"
---

<p>isdn_audio &#8211; audio extension of ttyI ISDN character devices</p>
<h2>Description</h2>
<p>This document describes the audio related extensions of the modem emulation, provided by <i>/dev/ttyIx</i>. The <font SIZE="-1">ISDN</font> tty devices are equipped with a modem emulation implementing a set of traditional and some special AT commands. This provides easy use together with almost all communication software that uses modem commands: <code><a href="/docs/linux/man/1-minicom/">minicom</a></code>(1), <code><a href="/docs/linux/man/1-seyon/">seyon</a></code>(1), <code><a href="/docs/linux/man/1-xcept/">XCept</a></code>(1), <code><a href="/docs/linux/man/8-uucico/">uucico</a></code>(8), <code><a href="/docs/linux/man/8-mgetty/">mgetty</a></code>(8), <code><a href="/docs/linux/man/8-dip/">dip</a></code>(8), <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8) and more. When enabled during kernel configuration, the emulator is capable of a reduced set of commands to support audio. To use audio features, an <font SIZE="-1">ISDN</font> card with a audio-capable low-level driver is needed. Currently the only audio-capable drivers are the teles and HiSax driver. The port speed of the <font SIZE="-1">ISDN</font> tty devices is always 64000 bps. </p>
<h2>Audio Related At Command Set</h2>
<p>This description does <code>not</code> include the standard AT command set. For a description of the standard AT command set, provided by the Linux <font SIZE="-1">ISDN</font> subsystem, see <code><a href="/docs/linux/man/4-ttyi/">ttyI</a></code>(4). All commands starting with <code>AT+</code> except <code>AT+FCLASS</code> are enabled only, if audio mode is active. The following <code>audio related AT commands</code> are supported by <font SIZE="-1">ISDN</font> tty devices:</p>
<dl>
<dt><code>AT+FCLASS=0</code></p>
<dd>Disable audio mode (default). This command sets register <i>18</i> to <i>4</i>.</p>
<dt><code>AT+FCLASS=8</code></p>
<dd>Enable audio mode. This command sets register <i>18</i> to <i>5</i>.</p>
<dt><code>AT+FCLASS=?</code></p>
<dd>Show possible modes.</p>
<dt><code>AT+FCLASS?</code></p>
<dd>Show current mode.</p>
<dt><code>AT+VNH=</code><i>x</i></p>
<dd>No function, provided for compatibility only.</p>
<dt><code>AT+VNH=?</code></p>
<dd>Always showing &quot;1&quot;.</p>
<dt><code>AT+VNH?</code></p>
<dd>Always showing &quot;1&quot;.</p>
<dt><code>AT+VIP</code></p>
<dd>Reset all audio parameters.</p>
<dt><code>AT+VLS=</code><i>x</i></p>
<dd>Select line <i>x</i>, where <i>x</i> is one of the following:</p>
<dl>
<dd>0 = No device.<br />
 2 = Phone line.</dl>
<dt><code>AT+VLS=?</code></p>
<dd>Always showing &quot;0,2&quot;.</p>
<dt><code>AT+VLS?</code></p>
<dd>Show current line.</p>
<dt><code>AT+VRX</code></p>
<dd>Start audio recording. See below for more information.</p>
<dt><code>AT+VSD=</code><i>x</i><code>,</code><i>y</i></p>
<dd>Set silence-detection parameters.</p>
<dl>
<dd>Possible parameters:<br />
 <i>x</i> = 0 &#8230; 31 sensitivity threshold level.<br />
 (default 0 , deactivated)<br />
 <i>y</i> = 0 &#8230; 255 range of interval in units of 0.1 second. (default 70)</dl>
<dt><code>AT+VSD=?</code></p>
<dd>Show possible parameters.</p>
<dt><code>AT+VSD?</code></p>
<dd>Show current parameters.</p>
<dt><code>AT+VSM=</code><i>x</i></p>
<dd>Select audio data format to <i>x</i>, where <i>x</i> is:</p>
<dl>
<dd>2 = ADPCM-2<br />
 3 = ADPCM-3<br />
 4 = ADPCM-4<br />
 5 = aLAW<br />
 6 = uLAW</dl>
<dt><code>AT+VSM=?</code></p>
<dd>Show possible audio data formats.</p>
<dt><code>AT+VSM?</code></p>
<dd>Show current audio data format.</p>
<dt><code>AT+VTX</code></p>
<dd>Start audio playback. See below for more information.</dl>
<h2>General Behaviour</h2>
<p>On incoming calls, if the application responds to a <code>RING</code> by sending <code>ATA</code>, depending on the calling service, the emulator responds with either <code>CONNECT</code> (data call) or <code>VCON</code> (voice call). </p>
<p> When starting audio playback or recording, the emulator responds with <code>CONNECT</code>. After that, the data transfer protocol described below is used. It is possible to initiate full duplex data transfer by issuing <code>AT+VRX+VTX</code> in a <code>single</code> command. In this case, <code>no</code> CONNECT message is sent to the application and the protocol described below is started immediately. </p>
<p> When stopping audio playback or recording, the message returned by the emulator depends on how the data transfer is stopped. If the data transfer is stopped by a remote hangup, <code>NO CARRIER</code> is sent to the application, while stopping data transfer with one of the DLE sequences, <code>VCON</code> is sent. In any case, the message is preceded by the appropriate DLE sequence for end of audio data and/or abort respectively. </p>
<p> On outgoing voice calls, the emulator responds with <code>VCON</code> upon connection setup.</p>
<h2>Audio Data Format</h2>
<p>When recording or playing back audio data, a kind of modified bisync protocol is used. When recording audio data, the modem emulator is considered to be the <code>sender</code>, while the application is the <code>receiver</code>. When playing back, this relationship is reversed: The modem emulator acts as <code>receiver</code>, while the application is the <code>sender</code>. With the bisync protocol the character <code>DLE</code> (0x10) has a special meaning and is used like an escape character. It is always followed by a second character which has the following meanings defined:</p>
<dl>
<dt><code>ETX</code> (0x03)</p>
<dd>End of audio data. This code has to be sent by the <code>sender</code>, indicating end of audio data.</p>
<dt><code>DC4</code> (0x14)</p>
<dd>Abort sending. This code has to be sent by the <code>receiver</code>, when it wishes to abort receiving data. The <code>sender</code> has to reply by stop sending data and finally indicating end of audio data.</p>
<dt><code>DLE</code> (0x10)</p>
<dd>a single byte with value 0x10 in the data stream.</p>
<dt><code>0</code></p>
<dd>Touch-tone &quot;0&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>1</code></p>
<dd>Touch-tone &quot;1&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>2</code></p>
<dd>Touch-tone &quot;2&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>3</code></p>
<dd>Touch-tone &quot;3&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>4</code></p>
<dd>Touch-tone &quot;4&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>5</code></p>
<dd>Touch-tone &quot;5&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>6</code></p>
<dd>Touch-tone &quot;6&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>7</code></p>
<dd>Touch-tone &quot;7&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>8</code></p>
<dd>Touch-tone &quot;8&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>9</code></p>
<dd>Touch-tone &quot;9&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>#</code></p>
<dd>Touch-tone &quot;#&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>*</code></p>
<dd>Touch-tone &quot;*&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>A</code></p>
<dd>Touch-tone &quot;A&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>B</code></p>
<dd>Touch-tone &quot;B&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>C</code></p>
<dd>Touch-tone &quot;C&quot; received. Valid only in direction from emulator to application.</p>
<dt><code>D</code></p>
<dd>Touch-tone &quot;D&quot; received. Valid only in direction from emulator to application.</dl>
<h2>Author</h2>
<p>Fritz Elfert &lt;fritz [at] isdn4linux.de&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-ttyi/">ttyI</a></code>(4). </p>
