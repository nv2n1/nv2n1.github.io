---
title: "zsnes(1)"
name: "zsnes"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zsnes/"
description: "ZSNES – Super Nintendo console emulator"
---

<h2 class="name">NAME</h2>
<p> ZSNES &#8211; Super Nintendo console emulator </p>
<h2>SYNOPSIS</h2>
<p> <code>ZSNES</code> [-?] [-1 #] [-2 #] [-dd] [-dh] [-f #] [-g #] [-h | -l] [-j] [-js #] [-k #] [-m] [-mc] [-md] [-ml #] [-n #] [-o] [-p #] [-r #] [-s] [-sa] [-t | -u] [-v #] [-y] [-z] [-zm #] [-zs #] [romname] </p>
<h2>DESCRIPTION</h2>
<p> <code>ZSNES</code> is an emulator for the Super Nintendo video game console. It is written in a combination of x86 assembly, C, C++, and PSR. It is currently available on Windows, DOS, x86 Linux, x86 Mac OS X, and x86 BSD. </p>
<p> Visit <a rel="nofollow" href="http://www.zsnes.com/">http://www.zsnes.com/</a> for the latest updates. </p>
<h2>OPTIONS</h2>
<p> Note: Many of these options can also be set in the GUI.</p>
<dl>
<dt><code>-?</code></p>
<dd> Display command-line help</p>
<dt><code>-1 # / -2 #</code></p>
<dd> Set controls for Player 1/2 </p>
<pre>
<i>0</i> = None       <i>1</i> = Keyboard/Gamepad
</pre>
<dt><code>-dd</code></p>
<dd> Disable sound DSP emulation</p>
<dt><code>-dh</code></p>
<dd> Disable game hacks</p>
<dt><code>-f #</code></p>
<dd> Enable frame skipping, where <code>#</code> is a numerical value from <i>0-9</i></p>
<dt><code>-g #</code></p>
<dd> Specify gamma correction value, where <code>#</code> is a numerical value from <i>0-15</i></p>
<dt><code>-h</code></p>
<dd> Force HiROM. Cannot be used with <code>-l</code></p>
<dt><code>-j</code></p>
<dd> Disable Mouse (Automatically turns off right mouse click)</p>
<dt><code>-js #</code></p>
<dd> Adjust joystick sensitivity, where <code>#</code> is a numerical value from <i>0-32767</i></p>
<dt><code>-k #</code></p>
<dd> Set volume level, where <code>#</code> is a numerical value from <i>1-100</i></p>
<dt><code>-l</code></p>
<dd> Force LoROM. Cannot be used with <code>-h</code></p>
<dt><code>-m</code></p>
<dd> Disable GUI (Must specify ROM filename)</p>
<dt><code>-mc</code></p>
<dd> Exit ZSNES when closing a movie (use with <code>-zm</code>)</p>
<dt><code>-md</code></p>
<dd> Dump raw video (use with <code>-zm</code>)</p>
<dt><code>-ml</code></p>
<dd> Define movie dump length in amount of frames (use with <code>-md</code>)</p>
<dt><code>-n #</code></p>
<dd> Enable scanlines (when available), where <code>#</code> is one of: </p>
<pre>
0 = none       <i>1</i> = full            <i>2</i> = 25%
<i>3</i> = 50%
</pre>
<dt><code>-o</code></p>
<dd> Disable MMX support</p>
<dt><code>-p #</code></p>
<dd> Change the clock speed of the main CPU, where <code>#</code> is a numerical value from <i>50-150</i>. 100 is the normal speed. Changing this value may have adverse side effects.</p>
<dt><code>-r #</code></p>
<dd> Set audio sampling rate, where <code>#</code> is one of: </p>
<pre>
<i>0</i> = 8 KHz      <i>1</i> = 11.025 KHz     <i>2</i> = 22.05 KHz
<i>3</i> = 44.1 KHz   <i>4</i> = 16 KHz         <i>5</i> = 32 KHz
<i>6</i> = 48 KHz
</pre>
<dt><code>-s</code></p>
<dd> Enable SPC700/DSP emulation (Sound)</p>
<dt><code>-sa</code></p>
<dd> Show files with all extensions (*.*) in GUI. Default is to only show files with one of the extensions listed in <code>romname</code></p>
<dt><code>-t</code></p>
<dd> Force NTSC (60 Hz) timing. Cannot be used with <code>-u</code></p>
<dt><code>-u</code></p>
<dd> Force PAL (50 Hz) timing. Cannot be used with <code>-t</code></p>
<dt><code>-v #</code></p>
<dd> Select video mode, where <code>#</code> is one of: </p>
<pre>
 <i>0</i> = 256x224 R W      <i>1</i> = 256x224 R F      <i>2</i> = 512x448 DR W
 <i>3</i> = 512x448 DR F     <i>4</i> = 640x480 DR F     <i>5</i> = 256x224 OR W
 <i>6</i> = 512x448 ODR      <i>7</i> = 640x480 ODS F    <i>8</i> = 640x480 ODS W
 <i>9</i> = 640x560 ODR W   <i>10</i> = 768x672 ODR W   <i>11</i> = 800x600 ODS F
<i>12</i> = 800x600 ODS W   <i>13</i> = 896x784 ODR W   <i>14</i> = 1024x768 ODS F
<i>15</i> = 1024x768 ODS W  <i>16</i> = 1024x896 ODR W  <i>17</i> = 1280x960 ODS F
<i>18</i> = 1280x1024 ODS F <i>19</i> = 1600x1200 ODS F <i>20</i> = VARIABLE ODR W
<i>21</i> = VARIABLE ODS W  <i>22</i> = CUSTOM OD F
</pre>
<dt><code>-y</code></p>
<dd> Enable Interpolation</p>
<dt><code>-z</code></p>
<dd> Disable stereo sound. Stereo sound is enabled by default</p>
<dt><code>-zm #</code></p>
<dd> Auto load specified movie on startup, where <code>#</code> is a numerical value from <i>0-9</i></p>
<dt><code>-zs #</code></p>
<dd> Auto load specified save state on startup, where <code>#</code> is a numerical value from <i>0-99</i></p>
<dt><code>romname</code></p>
<dd> Name of ROM to auto-load <code>romname</code> is of the format <code>filename.ext</code>, where <code>.ext</code> is one of SMC, SFC, SWC, FIG, MGD, MGH, UFO, BIN, GD3, GD7, USA, EUR, JAP, AUS, ST, BS, DX2, 048, 058, 078, 1 or A. You can also load ROMs which have been compressed with GZip, Zip or JMA. </p>
</dl>
<h2>FILES AND DIRECTORIES</h2>
<dl>
<dt>ZSNES</p>
<dd> The main program.</p>
<dt>~/.zsnes</p>
<dd> This is the directory where ZSNES configuration files are stored. By default, it is also the directory where save states, screenshots, SPC dumps and ZMV movie files are stored, but you can change this behaviour by editing zsnesl.cfg. This directory is created by ZSNES.</p>
<dt>~/.zsnes/zsnesl.cfg</p>
<dd> This file is where configuration settings for ZSNES are stored. It is in a human-readable format and can be edited by hand. It is created by ZSNES.</p>
<dt>~/.zsnes/zmovie.cfg</p>
<dd> This file is where settings specific to AVI dumping are saved. It is created by ZSNES.</p>
<dt>~/.zsnes/zfont.txt</p>
<dd> This file allows you to customize the fonts in the GUI. Enable &quot;Use Custom Font&quot; in the GUI Options menu. It is created by ZSNES.</p>
<dt>~/.zsnes/zinput.cfg</p>
<dd> This file is where input configuration settings for ZSNES are stored. </p>
<p> <code>If for some reason you update your version of ZSNES and it keeps crashing before you can do anything, you should try deleting the above .cfg files and let ZSNES create new ones.</code> </p>
</dl>
<h2>SPECIAL CHIP GAMES</h2>
<p> Many games on the Super Nintendo used custom CPUs in addition to the main SNES CPU. Some of these CPUs have not been fully reverse-engineered, and games that use them may either not work or may experience strange bugs. </p>
<p> You can find more information about these special CPUs at: </p>
<p> <a rel="nofollow" href="http://users.tpg.com.au/advlink/dsp/">http://users.tpg.com.au/advlink/dsp/</a> </p>
<p> <a rel="nofollow" href="http://nsrt.edgeemu.com/INFO/chipinfo.htm">http://nsrt.edgeemu.com/INFO/chipinfo.htm</a> </p>
<h2>GRAPHICS PACKS</h2>
<p> Some games based on the SPC7110 chip, such as Far East of Eden Zero, can use special graphics packs to work around unemulated portions of their custom CPU. These graphics packs must be stored in individual directories within the save directory, which is specified in zsnesl.cfg. By default, this is ~/.zsnes. The directory name of each graphics pack must be capitalized and all files within that directory must be in lowercase. </p>
<p> The proper directory name for a given graphics pack can be found in the readme file included with that pack. </p>
<p> NOTE: As of version 1.40, games which use the S-DD1 chip (Star Ocean and Street Fighter Alpha 2) do not require graphics packs. </p>
<h2>REPORTING BUGS</h2>
<p> You can report bugs using the bug tracker at the ZSNES BountySource page, located at </p>
<p> <a rel="nofollow" href="http://zsnes.bountysource.com/development/">http://zsnes.bountysource.com/development/</a> </p>
<h2>AUTHORS</h2>
<p> Please refer to the &quot;About&quot; section of the documentation. </p>
<h2>ZSNES RELATED WEBSITES</h2>
<dl>
<dt>ZSNES Home Page:</p>
<dd> <a rel="nofollow" href="http://www.zsnes.com/">http://www.zsnes.com/</a></p>
<dt>ZSNES Board:</p>
<dd> <a rel="nofollow" href="http://board.zsnes.com/">http://board.zsnes.com/</a></p>
<dt>ZSNES Project Page:</p>
<dd> <a rel="nofollow" href="https://zsnes.bountysource.com/">https://zsnes.bountysource.com/</a></p>
<dt>ZSNES Repository (SubVersioN):</p>
<dd> <a rel="nofollow" href="https://svn.bountysource.com/zsnes/trunk/">https://svn.bountysource.com/zsnes/trunk/</a></p>
<dt>ZSNES Documentation Online:</p>
<dd> <a rel="nofollow" href="http://zsnes-docs.sf.net/">http://zsnes-docs.sf.net/</a></p>
<dt>ZSNES IRC:</p>
<dd> #zsnes on irc.freenode.net</p>
<dt>ZSNES Docs IRC:</p>
<dd> #zsnes-docs on irc.freenode.net </p>
</dl>
<h2>COPYRIGHT NOTICE</h2>
<p> Copyright &#169; 1997-2007 ZSNES Team </p>
<p> Permission is granted to copy and distribute this manual under the terms of the GNU Free Documentation License. </p>
<h2>Index</h2>
