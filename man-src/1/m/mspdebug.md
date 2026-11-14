---
title: "mspdebug(1)"
name: "mspdebug"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mspdebug/"
description: "MSPDebug – debugging tool for MSP430 MCUs"
---

<h2>NAME</h2>
<p> MSPDebug &#8211; debugging tool for MSP430 MCUs</p>
<h2>SYNOPSIS</h2>
<p> <code>mspdebug</code> [options] <i>driver</i> [<i>command</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> MSPDebug is a command-line tool designed for debugging and programming the MSP430 family of MCUs. It supports the eZ430-F2013, eZ430-RF2500, FET430UIF and Olimex MSP-JTAG-TINY programming tools, as well as a simulation mode. </p>
<p> When started with appropriate options, MSPDebug will attempt to connect to the debugging tool specified and identify the device under test. Once connected, the user is presented with a command prompt which can be used to reflash the device memory, inspect memory and registers, set registers, and control the CPU (single step, run and run to breakpoint). </p>
<p> It supports ELF32, Intel HEX and BSD-style symbol tables (such as the output produced by <code><a href="/docs/linux/man/1-nm/">nm</a></code>(1)). It can also be used as a remote stub for <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1). </p>
<p> On startup, MSPDebug will look for a file called .mspdebug in the user&#8217;s home directory. If it exists, commands will be read and executed from this file before executing any other commands or starting the interactive reader.</p>
<h2>OPTIONS</h2>
<p> Command-line options accepted by MSPDebug are described below. If commands are specified on the end of the command-line, then they are executed after connecting to the device, and the interactive prompt is not started. See the section labelled <code>COMMANDS</code> for more information.</p>
<dl>
<dt>-v <i>voltage</i></p>
<dd> Set the programming voltage. The voltage should be specified as an integer in millivolts. It defaults to 3000 (3.0 V).</p>
<dt>-j</p>
<dd> Use JTAG instead of Spy-Bi-Wire to communicate with the MSP430. This option only works on FET430UIF devices.</p>
<dt>-d <i>device</i></p>
<dd> Specify that the driver should connect via a tty device rather than USB. The supported connection methods vary depending on the driver. See the section <code>DRIVERS</code> below for details.</p>
<dt>-U <i>bus</i>:<i>device</i></p>
<dd> Specify a particular USB device to connect to. Without this option, the first device of the appropriate type is opened.</p>
<dt>-n</p>
<dd> Do not process the startup file (~/.mspdebug).</p>
<dt>&#8211;help</p>
<dd> Display a brief help message and exit.</p>
<dt>&#8211;fet-list</p>
<dd> Display a list of devices supported by the FET driver (the driver used for <code>-R</code> and <code>-u</code> operating modes).</p>
<dt>&#8211;fet-force-id <i>string</i></p>
<dd> When using a FET device, force the connected chip to be recognised by MSPDebug as one of the given type during initialization. This overrides the device ID returned by the FET.</p>
<dt>&#8211;usb-list</p>
<dd> List available USB devices and exit.</dl>
<h2>DRIVERS</h2>
<p> A driver name must be specified on the command line for MSPDebug to connect to. Valid driver names are listed here.</p>
<dl>
<dt><code>rf2500</code></p>
<dd> Connect to an eZ430-RF2500 device. Only USB connection is supported.</p>
<dt><code>olimex</code></p>
<dd> Connect to an Olimex MSP-JTAG-TINY device. Both USB and tty access are supported.</p>
<dt><code>sim</code></p>
<dd> Do not connect to any hardware device, but instead start in simulation mode. A 64k buffer is allocated to simulate the device memory. The CPU core alone is emulated (no peripheral emulation). </p>
<p> During simulation, addresses below 0x0200 are assumed to be IO memory. When data is written to an IO memory address, a message is displayed on the console showing the program counter location, address written to, and data. The data value is also written to simulated RAM at the relevant address. </p>
<p> When data is read from IO memory, the user is notified similarly and prompted to supply the data. At this prompt, address expressions can be entered. If no value is entered, the value is read from simulated RAM. The user can press Ctrl+C to abort an IO request and stop execution. </p>
<p> This mode is intended for testing of changes to MSPDebug, and for aiding the disassembly of MSP430 binaries (as all binary and symbol table formats are still usable in this mode).</p>
<dt><code>uif</code></p>
<dd> Connect to an eZ430-F2013 or a FET430UIF device. The device argument should be the filename of the appropriate tty device. The TI serial converter chips on these devices are supported by newer versions of the Linux kernel, and should appear as /dev/tty<i>XX</i> when attached. </p>
<p> USB connection is not supported for this driver.</p>
<dt><code>uif-bsl</code></p>
<dd> Connect to the bootloader on a FET430UIF device. These devices contain MSP430F419 chips. By sending a special command sequence, you can obtain access to the bootloader and inspect memory on the MSP430F419 in the programming device itself. </p>
<p> Currently, only memory inspection is supported. CPU control via the bootloader is not possible. Memory erase and write is possible, but is currently not implemented, for lack of ability to test it. If implemented, this would allow firmware updates to FET430UIF devices. </p>
<p> USB connection is not supported for this driver.</dl>
<h2>COMMANDS</h2>
<p> MSPDebug can accept commands either through an interactive prompt, or non-interactively when specified on the command line. The supported commands are listed below. </p>
<p> Commands take arguments separated by spaces. Any text string enclosed in double-quotation marks is considered to be a single argument, even if it contains space characters. Within a quoted string, the usual C-style backslash substitutions can be used.</p>
<dl>
<dt><code>=</code> <i>expression</i></p>
<dd> Evaluate an address expression and show both its value, and the result when the value is looked up in reverse in the current symbol table. This result is of the form <i>symbol</i>+<i>offset</i>, where <i>symbol</i> is the name of the nearest symbol not past the address in question. </p>
<p> See the section marked <code>ADDRESS EXPRESSIONS</code> for more information on the syntax of expressions.</p>
<dt><code>break</code></p>
<dd> Show a list of active breakpoints. Breakpoints can be added and removed with the <code>setbreak</code> and <code>delbreak</code> commands. Each breakpoint is numbered with an integer index starting at 0.</p>
<dt><code>cgraph</code> <i>address</i> <i>length</i> [<i>address</i>]</p>
<dd> Construct the call graph of all functions contained or referenced in the given range of memory. If a particular function is specified, then details for that node of the graph are displayed. Otherwise, a summary of all nodes is displayed. </p>
<p> Information from the symbol table is used for hinting at the possible locations of function starts. Any symbol which does not contain a &quot;.&quot; is considered a possible function start. </p>
<p> Callers and callee names are shown prefixed by a &quot;*&quot; where the transition is a tail-call type transition.</p>
<dt><code>delbreak</code> [<i>index</i>]</p>
<dd> Delete one or all breakpoints. If an index is given, the selected breakpoint is deleted. Otherwise, all breakpoints are cleared.</p>
<dt><code>dis</code> <i>address</i> [<i>length</i>]</p>
<dd> Dissassemble a section of memory. Both arguments may be address expressions. If no length is specified, a section of the default length (64 bytes) is disassembled and shown. </p>
<p> If symbols are available, then all addresses used as operands are translated into <i>symbol</i>+<i>offset</i> form.</p>
<dt><code>erase</code></p>
<dd> Erase the device under test. All code memory is erased (but not information or boot memory).</p>
<dt><code>gdb</code> [<i>port</i>]</p>
<dd> Start a GDB remote stub, optionally specifying a TCP port to listen on. If no port is given, the default port is 2000. </p>
<p> MSPDebug will wait for a connection on this port, and then act as a GDB remote stub until GDB disconnects. The basic GDB protocol is supported, plus the monitor commands &quot;erase&quot; and &quot;reset&quot;.</p>
<dt><code>help</code> [<i>command</i>]</p>
<dd> Show a brief listing of available commands. If an argument is specified, show the syntax for the given command. The help text shown when no argument is given is also shown when MSPDebug starts up.</p>
<dt><code>hexout</code> <i>address</i> <i>length</i> <i>filename</i></p>
<dd> Read the specified section of the device memory and save it to an Intel HEX file. The address and length arguments may both be address expressions. </p>
<p> If the specified file already exists, then it will be overwritten. If you need to dump memory from several disjoint memory regions, you can do this by saving each section to a separate file. The resulting files can then be concatenated together to form a single valid HEX file.</p>
<dt><code>isearch</code> <i>address</i> <i>length</i> [<i>options</i> &#8230;]</p>
<dd> Search over the given range for an instruction which matches the specified search criteria. The search may be narrowed by specifying one or more of the following terms:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>opcode</code> <i>opcode</i></p>
<dd> Match the specified opcode. Byte/word specifiers are not recognised, as they are specified with other options.</p>
<dt><code>byte</code></p>
<dd> Match only byte operations.</p>
<dt><code>word</code></p>
<dd> Match only word operations.</p>
<dt><code>jump</code></p>
<dd> Match only jump instructions (conditional and unconditional jumps, but not instructions such as BR which load the program counter explicitly).</p>
<dt><code>single</code></p>
<dd> Match only single-operand instructions.</p>
<dt><code>double</code></p>
<dd> Match only double-operand instructions.</p>
<dt><code>noarg</code></p>
<dd> Match only instructions with no arguments.</p>
<dt><code>src</code> <i>address</i></p>
<dd> Match instructions with the specified value in the source operand. The value may be given as an address expression. Specifying this option implies matching of only double-operand instructions.</p>
<dt><code>dst</code> <i>address</i></p>
<dd> Match instructions with the specified value in the destination operand. This option implies that no-argument instructions are not matched.</p>
<dt><code>srcreg</code> <i>register</i></p>
<dd> Match instructions using the specified register in the source operand. This option implies matching of only double-operand instructions.</p>
<dt><code>dstreg</code> <i>register</i></p>
<dd> Match instructions using the specified register in the destination operand. This option implies that no-argument instructions are not matched.</p>
<dt><code>srcmode</code> <i>mode</i></p>
<dd> Match instructions using the specified mode in the source operand. See below for a list of modes recognised. This option implies matching of only double-operand instructions.</p>
<dt><code>dstmode</code> <i>mode</i></p>
<dd> Match instructions using the specified mode in the destination operand. See below for a list of modes. This option implies that no-argument instructions are not matched.</dl>
</dl>
<p> For single-operand instructions, the operand is considered to be the destination operand. </p>
<p> The seven addressing modes used by the MSP430 are represented by single characters, and are listed here:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>R</code></p>
<dd> Register mode.</p>
<dt><code>I</code></p>
<dd> Indexed mode.</p>
<dt><code>S</code></p>
<dd> Symbolic mode.</p>
<dt><code>&amp;</code></p>
<dd> Absolute mode.</p>
<dt><code>@</code></p>
<dd> Register-indirect mode.</p>
<dt><code>+</code></p>
<dd> Register-indirect mode with auto-increment.</p>
<dt><code>#</code></p>
<dd> Immediate mode.</dl>
</dl>
<dt><code>md</code> <i>address</i> [<i>length</i>]</p>
<dd> Read the specified section of device memory and display it as a canonical-style hexdump. Both arguments may be address expressions. If no length is specified, a section of the default length (64 bytes) is shown. </p>
<p> The output is split into three columns. The first column shows the starting address for the line. The second column lists the hexadecimal values of the bytes. The final column shows the ASCII characters corresponding to printable bytes, and . for non-printing characters.</p>
<dt><code>mw</code> <i>address</i> <i>bytes</i> &#8230;</p>
<dd> Write a sequence of bytes at the given memory address. The address given may be an address expression. Bytes values are two-digit hexadecimal numbers separated by spaces. </p>
<p> Unless used in the simulation mode, this command can only be used for programming flash memory.</p>
<dt><code>opt</code> [<i>name</i>] [<i>value</i>]</p>
<dd> Query, set or list option variables. MSPDebug&#8217;s behaviour can be configured using option variables, described below in the section <code>OPTIONS</code>. </p>
<p> Option variables may be of three types: boolean, numeric or text. Numeric values may be specified as address expressions. </p>
<p> With no arguments, this command displays all available option variables. With just an option name as its argument, it displays the current value of that option.</p>
<dt><code>prog</code> <i>filename</i></p>
<dd> Erase and reprogram the device under test using the binary file supplied. The file format will be auto-detected and may be either Intel HEX or ELF32. </p>
<p> In the case of an ELF32 file, symbols will be automatically loaded from the file into the symbol table (discarding any existing symbols), if they are present. </p>
<p> The CPU is reset and halted before and after programming.</p>
<dt><code>read</code> <i>filename</i></p>
<dd> Read commands from the given file, line by line and process each one. Any lines whose first non-space character is <code>#</code> are ignored. If an error occurs while processing a command, the rest of the file is not processed.</p>
<dt><code>regs</code></p>
<dd> Show the current value of all CPU registers in the device under test.</p>
<dt><code>reset</code></p>
<dd> Reset (and halt) the CPU of the device under test.</p>
<dt><code>run</code></p>
<dd> Start running the CPU. The interactive command prompt is blocked when the CPU is started and the prompt will not appear again until the CPU halts. The CPU will halt if it encounters a breakpoint, or if Ctrl-C is pressed by the user. </p>
<p> After the CPU halts, the current register values are shown as well as a disassembly of the first few instructions at the address selected by the program counter.</p>
<dt><code>set</code> <i>register</i> <i>value</i></p>
<dd> Alter the value of a register. Registers are specified as numbers from 0 through 15. Any leading non-numeric characters are ignored (so a register may be specified as, for example, &quot;R12&quot;). The value argument is an address expression.</p>
<dt><code>setbreak</code> <i>address</i> [<i>index</i>]</p>
<dd> Add a new breakpoint. The breakpoint location is an address expression. An optional index may be specified, indicating that this new breakpoint should overwrite an existing slot. If no index is specified, then the breakpoint will be stored in the next unused slot.</p>
<dt><code>step</code> [<i>count</i>]</p>
<dd> Step the CPU through one or more instructions. After stepping, the new register values are displayed, as well as a disassembly of the instructions at the address selected by the program counter. </p>
<p> An optional count can be specified to step multiple times. If no argument is given, the CPU steps once.</p>
<dt><code>sym clear</code></p>
<dd> Clear the symbol table, deleting all symbols.</p>
<dt><code>sym set</code> <i>name</i> <i>value</i></p>
<dd> Set or alter the value of a symbol. The value given may be an address expression.</p>
<dt><code>sym del</code> <i>name</i></p>
<dd> Delete the given symbol from the symbol table.</p>
<dt><code>sym import</code> <i>filename</i></p>
<dd> Load symbols from the specified file and add them to the symbol table. The file format will be auto-detected and may be either ELF32 or a BSD-style symbol listing (like the output from <code><a href="/docs/linux/man/1-nm/">nm</a></code>(1)). </p>
<p> Symbols can be combined from many sources, as the syms command adds to the existing symbol table without discarding existing symbols.</p>
<dt><code>sym import+</code> <i>filename</i></p>
<dd> This command is similar to <code>sym import</code>, except that the symbol table is not cleared first. By using this command, symbols from multiple sources can be combined.</p>
<dt><code>sym export</code> <i>filename</i></p>
<dd> Save all symbols currently defined to the given file. The symbols are saved as a BSD-style symbol table. Note that symbol types are not stored by MSPDebug, and all symbols are saved as type <code>t</code>.</p>
<dt><code>sym find</code> [<i>regex</i>]</p>
<dd> Search for symbols. If a regular expression is given, then all symbols matching the expression are printed. If no expression is specified, then the entire symbol table is listed.</p>
<dt><code>sym rename</code> <i>regex</i> <i>string</i></p>
<dd> Rename symbols by searching for those matching the given regular expression and substituting the given string for the matched portion. The symbols renamed are displayed, as well as a total count of all symbols renamed.</dl>
<h2>ADDRESS EXPRESSIONS</h2>
<p> Any command which accepts a memory address, length or register value as an argument may be given an address expression. An address expression consists of an algebraic combination of values. </p>
<p> An address value may be either a decimal value, a hexadecimal value preceeded by the prefix <code>0x</code>, or a symbol name. </p>
<p> The operators recognised are the usual algebraic operators: <code>+</code>, <code>&#8211;</code>, <code>*</code>, <code>/</code>, <code>%</code>, <code>(</code> and <code>)</code>. Operator precedence is the same as in C-like languages, and the <code>&#8211;</code> operator may be used as a unary negation operator. </p>
<p> The following are all valid examples of address expressions: </p>
<p> <code>2+2</code><br />
 <code>table_start + (elem_size + elem_pad)*4</code><br />
 <code>main+0x3f</code><br />
 <code>__bss_end-__bss_start</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nm/">nm</a></code>(1), <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/1-objcopy/">objcopy</a></code>(1)</p>
<h2>OPTIONS</h2>
<p> MSPDebug&#8217;s behaviour can be configured via the following variables:</p>
<dl>
<dt><code>color</code> (boolean)</p>
<dd> If true, MSPDebug will colorize debugging output.</p>
<dt><code>gdb_loop</code> (boolean)</p>
<dd> Automatically restart the GDB server after disconnection. If this option is set, then the GDB server keeps running until an error occurs, or the user interrupts with Ctrl+C.</dl>
<h2>BUGS</h2>
<p> If you find any bugs, you should report them to the author at daniel [at] tortek.co.nz. It would help if you could include a transcript of an MSPDebug session illustrating the program, as well as any relevant binaries or other files. Below, known bugs in the current version of MSPDebug are described. </p>
<p> Memory addresses above 0x10000 (in devices with more than 64k of memory) are not accessible. All other memory in these devices is accessible as normal. </p>
<p> When using the GDB remote stub in simulation and an IO read request occurs, any request to interrupt from GDB will not be acknowledged until the IO request is either completed or aborted.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009, 2010 Daniel Beer &lt;daniel [at] tortek.co.nz&gt; </p>
<p> MSPDebug is free software, distributed under the terms of the GNU General Public license (version 2 or later). See the file COPYING included with the source code for more details. </p>
<h2>Index</h2>
