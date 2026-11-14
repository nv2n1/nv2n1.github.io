---
title: "mcu8051ide(1)"
name: "mcu8051ide"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcu8051ide/"
description: "MCU 8051 IDE – Itegrated development enviroment for MCS-51 based microcontrollers"
---

<h2>NAME</h2>
<p> MCU 8051 IDE &#8211; Itegrated development enviroment for MCS-51 based microcontrollers</p>
<h2>SYNOPSIS</h2>
<p> <code>mcu8051ide</code> [<code>&#8211;help</code>] [<code>-h</code>] [<code>&#8211;compile</code> <i>asm_file</i>] [<code>&#8211;iram-size</code> <i>size</i>] [<code>&#8211;code-size</code> <i>size</i>] [<code>&#8211;xram-size</code> <i>size</i>] [<code>&#8211;no-opt</code>] [<code>&#8211;quiet</code>] [<code>-q</code>] [<code>&#8211;nosplash</code>] [<code>&#8211;nocolor</code>] [<code>-n</code>] [<code>&#8211;version</code>] [<code>-V</code>] [<code>&#8211;defaults</code>] [<code>&#8211;disassemble</code>] [<code>&#8211;minimalized</code>] [<code>&#8211;config-file</code> <i>filename</i>] [<code>&#8211;check-libraries</code>] [<code>&#8211;ignore-last-session</code>] [<code>&#8211;open-project</code> <i>project</i>] [<code>&#8211;reset-user-settings</code>] [<code>&#8211;hex2bin</code> <i>input</i> <i>output</i>] [<code>&#8211;bin2hex</code> <i>input</i> <i>output</i>] [<code>&#8211;sim2hex</code> <i>input</i> <i>output</i>] [<code>&#8211;sim2bin</code> <i>input</i> <i>output</i>] [<code>&#8211;normalize-hex</code> <i>input</i>] [<code>&#8211;auto-indent</code> <i>input</i>] [<code>&#8211;comp-quiet</code>] [<code>&#8211;no-sim</code>] [<code>&#8211;no-bin</code>] [<code>&#8211;no-lst</code>] [<code>&#8211;no-hex</code>] [<code>&#8211;warning-level</code> <i>N</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code> MCU 8051 IDE</code> is tool for developing programs in assembly language and C languge (with SDCC) for micronstollers based on industrial standard MCS-51. It consist of editor with syntax highlight, auto completion, syntax validation and command line, compiler with support for macro-instructions (even macro in macro), simulator, scientific calculator, (rich) text editor for writing to do lists, hexadecimal editor and many other tools. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Display short help text</p>
<dt><code>&#8211;quiet</code>, -q</p>
<dd> Don&#8217;t display status of initialization progress on startup</p>
<dt><code>&#8211;nosplash</code></p>
<dd> Don&#8217;t show splash screen</p>
<dt><code>&#8211;nocolor</code>, -n</p>
<dd> Disable color output</p>
<dt><code>&#8211;version</code>, <code>-V</code></p>
<dd> Display version information</p>
<dt><code>&#8211;defaults</code></p>
<dd> Start with default settings (low level GUI settings (panel sizes &#8230;))</p>
<dt><code>&#8211;minimalized</code></p>
<dd> Start with minimalized window</p>
<dt><code>&#8211;config-file </code><i>filename</i></p>
<dd> Specify path to file containg user settings</p>
<dt><code>&#8211;check-libraries</code></p>
<dd> Check if all nessesary Tcl libraries are avaible</p>
<dt><code>&#8211;ignore-last-session</code></p>
<dd> Start with an empty session (no project will be opened at startup)</p>
<dt><code>&#8211;open-project </code><i>project</i></p>
<dd> Open only this project</p>
<dt><code>&#8211;reset-user-settings</code></p>
<dd> Reset all user settings to defaults</p>
<dt><code>&#8211;hex2bin </code><i>input output</i></p>
<dd> Convert Intel Hex 8 file to binary file</p>
<dt><code>&#8211;bin2hex </code><i>input output</i></p>
<dd> Convert binary file to Intel Hex 8 file</p>
<dt><code>&#8211;sim2hex </code><i>input output</i></p>
<dd> Convert MCU 8051 IDE v0.9.1 simulator file to Intel Hex 8 file</p>
<dt><code>&#8211;sim2bin </code><i>input output</i></p>
<dd> Convert MCU 8051 IDE v0.9.1 simulator file to binary file</p>
<dt><code>&#8211;normalize-hex </code><i>input</i></p>
<dd> Normalize IHEX8 file</p>
<dt><code>&#8211;auto-indent </code><i>input</i></p>
<dd> Reformat indention in source code</p>
<dt><code>&#8211;disassemble </code><i>input</i></p>
<dd> Disaseble IHEX8 code and store result in input.asm</p>
<dt><code>&#8211;compile </code><i>asm_file</i></p>
<dd> Compile asm_file and exit program</p>
<dt><code>&#8211;iram-size </code><i>size</i></p>
<dd> Set size of internal data memory (eg. 1K or 1024) (default: 0x100)</p>
<dt><code>&#8211;code-size </code><i>size</i></p>
<dd> Set size of program memory (eg. 1K or 1024) (default: 0x10000)</p>
<dt><code>&#8211;xram-size </code><i>size</i></p>
<dd> Set size of external data memory (eg. 1K or 1024) (default: 0x10000)</p>
<dt><code>&#8211;no-opt</code></p>
<dd> Disable compiler optimalizations</p>
<dt><code>&#8211;comp-quiet</code></p>
<dd> Suppress compiler console output</p>
<dt><code>&#8211;no-sim</code></p>
<dd> Do not generate SIM file (for MCU 8051 IDE simulator)</p>
<dt><code>&#8211;no-bin</code></p>
<dd> Do not generate binary object code</p>
<dt><code>&#8211;no-lst</code></p>
<dd> Do not generate code listing</p>
<dt><code>&#8211;no-hex</code></p>
<dd>
<dt><code>&#8211;warning-level </code><i>N</i></p>
<dd> Do not generate IHEX8 object code; 3 &#8211; Nothing; 2 &#8211; Errros only; 1 &#8211; Errors + Warnings; 0 &#8211; All (Default) </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/mcu8051ide/data/tips.conf</i></p>
<dd> XML file containing tips. (Dialog &quot;Tip of the day&quot;)</p>
<dt><i>/usr/share/mcu8051ide/data/mcus.conf</i></p>
<dd> XML definition of supported MCUs. <code>Warning: MCU 8051 IDE cannot run without this file.</code> Please do not rely on format of this file. It may be changed in future version without any warning.</p>
<dt><i>~/.mcu8051ide/last_session.conf</i></p>
<dd> INI like definition of the last session.</p>
<dt><i>~/.mcu8051ide/base.conf</i></p>
<dd> Base configuration file. It contains only three configuration keys separated by spaces, please do not rely on format of this file. It may be changed in future version without any warning.</p>
<dt><i>~/.mcu8051ide/config.conf</i></p>
<dd> Main configuration file (INI like). Readable and I hope user friendly. </p>
</dl>
<h2>NOTES</h2>
<p> List of supported porcessors is very short yet. Please post suggestions to martin.osmera [at] gmail.com .</p>
<h2>SUPPORTED PROCESSORS</h2>
<p> 8051, 80C51, 8052, AT89C2051, AT89C4051, AT89C51, AT89C51RC, AT89C52, AT89C55WD, AT89LV51, AT89LV52, AT89LV55, AT89S52, AT89LS51, AT89LS52, AT89S8253, AT89S2051, AT89S4051, AT89S52, AT89LS51, AT89LS52, AT89S8253, AT89S2051, AT89S4051, T87C5101, T83C5101, T83C5102, TS80C32X2, TS80C52X2, TS87C52X2, AT80C32X2, AT80C52X2, AT87C52X2, AT80C54X2, AT80C58X2, AT87C54X2, AT87C58X2, TS80C54X2, TS80C58X2, TS87C54X2, TS87C58X2, TS80C31X2, AT80C31X2 </p>
<h2>TO DO</h2>
<p> Add support for more MCS-51 based microcontrollers. Fix all bugs. </p>
<h2>AUTHOR</h2>
<p> Martin Osmera &lt;martin.osmera [at] gmail.com&gt; </p>
<h2>Index</h2>
