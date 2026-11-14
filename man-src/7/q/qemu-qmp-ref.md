---
title: "qemu-qmp-ref(7)"
name: "qemu-qmp-ref"
section: "7"
letter: "q"
url: "/docs/linux/man/7-qemu-qmp-ref/"
description: "qemu-qmp-ref – QEMU QMP Reference Manual"
---

<p>qemu-qmp-ref &#8211; QEMU QMP Reference Manual</p>
<h2>Description</h2>
<h3>Introduction</h3>
<p>This document describes all commands currently supported by <font SIZE="-1">QMP.</font> Most of the time their usage is exactly the same as in the user Monitor, this means that any other document which also describe commands (the manpage, <font SIZE="-1">QEMU</font>&#8216;s manual, etc) can and should be consulted. <font SIZE="-1">QMP</font> has two types of commands: regular and query commands. Regular commands usually change the Virtual Machine&#8217;s state someway, while query commands just return information. The sections below are divided accordingly. It&#8217;s important to observe that all communication examples are formatted in a reader-friendly way, so that they&#8217;re easier to understand. However, in real protocol usage, they&#8217;re emitted as a single line. Also, the following notation is used to denote data flow: Example: </p>
<pre> -&gt; data issued by the Client
 
 &lt;- Server data response</pre>
<p>Please, refer to the <font SIZE="-1">QMP</font> specification (docs/interop/qmp-spec.txt) for detailed information on the Server command and response formats.</p>
<h3>Stability Considerations</h3>
<p>The current <font SIZE="-1">QMP</font> command set (described in this file) may be useful for a number of use cases, however it&#8217;s limited and several commands have bad defined semantics, specially with regard to command completion. These problems are going to be solved incrementally in the next <font SIZE="-1">QEMU</font> releases and we&#8217;re going to establish a deprecation policy for badly defined commands. If you&#8217;re planning to adopt <font SIZE="-1">QMP,</font> please observe the following:</p>
<dl>
<dt>1.</p>
<dd>The deprecation policy will take effect and be documented soon, please check the documentation of each used command as soon as a new release of <font SIZE="-1">QEMU</font> is available</p>
<dt>2.</p>
<dd><font SIZE="-1">DO NOT</font> rely on anything which is not explicit documented</p>
<dt>3.</p>
<dd>Errors, in special, are not documented. Applications should <font SIZE="-1">NOT</font> check for specific errors classes or data (it&#8217;s strongly recommended to only check for the &#8220;error&#8221; key)</dl>
<h3><font SIZE="-1">QMP</font> errors</h3>
<p><code>QapiErrorClass</code> (Enum) <font SIZE="-1">QEMU</font> error classes <code>Values:</code></p>
<dl>
<dt>&quot;GenericError&quot;</p>
<dd>this is used for errors that don&#8217;t require a specific error class. This should be the default case for most errors</p>
<dt>&quot;CommandNotFound&quot;</p>
<dd>the requested command has not been found</p>
<dt>&quot;DeviceNotActive&quot;</p>
<dd>a device has failed to be become active</p>
<dt>&quot;DeviceNotFound&quot;</p>
<dd>the requested device has not been found</p>
<dt>&quot;KVMMissingCap&quot;</p>
<dd>the requested operation can&#8217;t be fulfilled because a required <font SIZE="-1">KVM</font> capability is missing</dl>
<p> <code>Since:</code> 1.2</p>
<h3>Common data types</h3>
<p><code>IoOperationType</code> (Enum) An enumeration of the I/O operation types <code>Values:</code></p>
<dl>
<dt>&quot;read&quot;</p>
<dd>read operation</p>
<dt>&quot;write&quot;</p>
<dd>write operation</dl>
<p> <code>Since:</code> 2.1 <code>OnOffAuto</code> (Enum) An enumeration of three options: on, off, and auto <code>Values:</code></p>
<dl>
<dt>&quot;auto&quot;</p>
<dd><font SIZE="-1">QEMU</font> selects the value between on and off</p>
<dt>&quot;on&quot;</p>
<dd>Enabled</p>
<dt>&quot;off&quot;</p>
<dd>Disabled</dl>
<p> <code>Since:</code> 2.2 <code>OnOffSplit</code> (Enum) An enumeration of three values: on, off, and split <code>Values:</code></p>
<dl>
<dt>&quot;on&quot;</p>
<dd>Enabled</p>
<dt>&quot;off&quot;</p>
<dd>Disabled</p>
<dt>&quot;split&quot;</p>
<dd>Mixed</dl>
<p> <code>Since:</code> 2.6 <code>String</code> (Object) A fat type wrapping &#8216;str&#8217;, to be embedded in lists. <code>Members:</code></p>
<dl>
<dt>&quot;str: string&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 1.2 <code>StrOrNull</code> (Alternate) This is a string value or the explicit lack of a string (null pointer in C). Intended for cases when &#8216;optional absent&#8217; already has a different meaning. <code>Members:</code></p>
<dl>
<dt>&quot;s: string&quot;</p>
<dd>the string value</p>
<dt>&quot;n: null&quot;</p>
<dd>no string value</dl>
<p> <code>Since:</code> 2.10 <code>OffAutoPCIBAR</code> (Enum) An enumeration of options for specifying a <font SIZE="-1">PCI BAR</font> <code>Values:</code></p>
<dl>
<dt>&quot;off&quot;</p>
<dd>The specified feature is disabled</p>
<dt>&quot;auto&quot;</p>
<dd>The <font SIZE="-1">PCI BAR</font> for the feature is automatically selected</p>
<dt>&quot;bar0&quot;</p>
<dd><font SIZE="-1">PCI BAR0</font> is used for the feature</p>
<dt>&quot;bar1&quot;</p>
<dd><font SIZE="-1">PCI BAR1</font> is used for the feature</p>
<dt>&quot;bar2&quot;</p>
<dd><font SIZE="-1">PCI BAR2</font> is used for the feature</p>
<dt>&quot;bar3&quot;</p>
<dd><font SIZE="-1">PCI BAR3</font> is used for the feature</p>
<dt>&quot;bar4&quot;</p>
<dd><font SIZE="-1">PCI BAR4</font> is used for the feature</p>
<dt>&quot;bar5&quot;</p>
<dd><font SIZE="-1">PCI BAR5</font> is used for the feature</dl>
<p> <code>Since:</code> 2.12 <code>PCIELinkSpeed</code> (Enum) An enumeration of PCIe link speeds in units of GT/s <code>Values:</code></p>
<dl>
<dt>&quot;2_5&quot;</p>
<dd>2.5GT/s</p>
<dt>5</p>
<dd>5.0GT/s</p>
<dt>8</p>
<dd>8.0GT/s</p>
<dt>16</p>
<dd>16.0GT/s</dl>
<p> <code>Since:</code> 4.0 <code>PCIELinkWidth</code> (Enum) An enumeration of PCIe link width <code>Values:</code></p>
<dl>
<dt>1</p>
<dd>x1</p>
<dt>2</p>
<dd>x2</p>
<dt>4</p>
<dd>x4</p>
<dt>8</p>
<dd>x8</p>
<dt>12</p>
<dd>x12</p>
<dt>16</p>
<dd>x16</p>
<dt>32</p>
<dd>x32</dl>
<p> <code>Since:</code> 4.0</p>
<h3>Socket data types</h3>
<p><code>NetworkAddressFamily</code> (Enum) The network address family <code>Values:</code></p>
<dl>
<dt>&quot;ipv4&quot;</p>
<dd><font SIZE="-1">IPV4</font> family</p>
<dt>&quot;ipv6&quot;</p>
<dd><font SIZE="-1">IPV6</font> family</p>
<dt>&quot;unix&quot;</p>
<dd>unix socket</p>
<dt>&quot;vsock&quot;</p>
<dd>vsock family (since 2.8)</p>
<dt>&quot;unknown&quot;</p>
<dd>otherwise</dl>
<p> <code>Since:</code> 2.1 <code>InetSocketAddressBase</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;host: string&quot;</p>
<dd>host part of the address</p>
<dt>&quot;port: string&quot;</p>
<dd>port part of the address</dl>
<p> <code>InetSocketAddress</code> (Object) Captures a socket address or address range in the Internet namespace. <code>Members:</code></p>
<dl>
<dt>&quot;numeric: boolean&quot; (optional)</p>
<dd>true if the host/port are guaranteed to be numeric, false if name resolution should be attempted. Defaults to false. (Since 2.9)</p>
<dt>&quot;to: int&quot; (optional)</p>
<dd>If present, this is range of possible addresses, with port between <tt>&quot;port&quot;</tt> and <tt>&quot;to&quot;</tt>.</p>
<dt>&quot;ipv4: boolean&quot; (optional)</p>
<dd>whether to accept IPv4 addresses, default try both IPv4 and IPv6</p>
<dt>&quot;ipv6: boolean&quot; (optional)</p>
<dd>whether to accept IPv6 addresses, default try both IPv4 and IPv6</p>
<dt>&quot;keep-alive: boolean&quot; (optional)</p>
<dd>enable keep-alive when connecting to this socket. Not supported for passive sockets. (Since 4.2)</p>
<dt>The members of &quot;InetSocketAddressBase&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.3 <code>UnixSocketAddress</code> (Object) Captures a socket address in the local (&#8220;Unix socket&#8221;) namespace. <code>Members:</code></p>
<dl>
<dt>&quot;path: string&quot;</p>
<dd>filesystem path to use</dl>
<p> <code>Since:</code> 1.3 <code>VsockSocketAddress</code> (Object) Captures a socket address in the vsock namespace. <code>Members:</code></p>
<dl>
<dt>&quot;cid: string&quot;</p>
<dd>unique host identifier</p>
<dt>&quot;port: string&quot;</p>
<dd>port</dl>
<p> <code>Note:</code> string types are used to allow for possible future hostname or service resolution support. <code>Since:</code> 2.8 <code>SocketAddressLegacy</code> (Object) Captures the address of a socket, which could also be a named file descriptor <code>Members:</code></p>
<dl>
<dt>&quot;type&quot;</p>
<dd>One of &#8220;inet&#8221;, &#8220;unix&#8221;, &#8220;vsock&#8221;, &#8220;fd&#8221;</p>
<dt>&quot;data: InetSocketAddress&quot; when &quot;type&quot; is &quot;inet&quot;</p>
<dd>
<dt>&quot;data: UnixSocketAddress&quot; when &quot;type&quot; is &quot;unix&quot;</p>
<dd>
<dt>&quot;data: VsockSocketAddress&quot; when &quot;type&quot; is &quot;vsock&quot;</p>
<dd>
<dt>&quot;data: String&quot; when &quot;type&quot; is &quot;fd&quot;</p>
<dd></dl>
<p> <code>Note:</code> This type is deprecated in favor of SocketAddress. The difference between SocketAddressLegacy and SocketAddress is that the latter is a flat union rather than a simple union. Flat is nicer because it avoids nesting on the wire, i.e. that form has fewer {}. <code>Since:</code> 1.3 <code>SocketAddressType</code> (Enum) Available SocketAddress types <code>Values:</code></p>
<dl>
<dt>&quot;inet&quot;</p>
<dd>Internet address</p>
<dt>&quot;unix&quot;</p>
<dd>Unix domain socket</p>
<dt>&quot;vsock&quot;</p>
<dd><font SIZE="-1">VMCI</font> address</p>
<dt>&quot;fd&quot;</p>
<dd>decimal is for file descriptor number, otherwise a file descriptor name. Named file descriptors are permitted in monitor commands, in combination with the &#8216;getfd&#8217; command. Decimal file descriptors are permitted at startup or other contexts where no monitor context is active.</dl>
<p> <code>Since:</code> 2.9 <code>SocketAddress</code> (Object) Captures the address of a socket, which could also be a named file descriptor <code>Members:</code></p>
<dl>
<dt>&quot;type: SocketAddressType&quot;</p>
<dd>Transport type</p>
<dt>The members of &quot;InetSocketAddress&quot; when &quot;type&quot; is &quot;inet&quot;</p>
<dd>
<dt>The members of &quot;UnixSocketAddress&quot; when &quot;type&quot; is &quot;unix&quot;</p>
<dd>
<dt>The members of &quot;VsockSocketAddress&quot; when &quot;type&quot; is &quot;vsock&quot;</p>
<dd>
<dt>The members of &quot;String&quot; when &quot;type&quot; is &quot;fd&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.9</p>
<h3><font SIZE="-1">VM</font> run state</h3>
<p><code>RunState</code> (Enum) An enumeration of <font SIZE="-1">VM</font> run states. <code>Values:</code></p>
<dl>
<dt>&quot;debug&quot;</p>
<dd><font SIZE="-1">QEMU</font> is running on a debugger</p>
<dt>&quot;finish-migrate&quot;</p>
<dd>guest is paused to finish the migration process</p>
<dt>&quot;inmigrate&quot;</p>
<dd>guest is paused waiting for an incoming migration. Note that this state does not tell whether the machine will start at the end of the migration. This depends on the command-line -S option and any invocation of &#8216;stop&#8217; or &#8216;cont&#8217; that has happened since <font SIZE="-1">QEMU</font> was started.</p>
<dt>&quot;internal-error&quot;</p>
<dd>An internal error that prevents further guest execution has occurred</p>
<dt>&quot;io-error&quot;</p>
<dd>the last <font SIZE="-1">IOP</font> has failed and the device is configured to pause on I/O errors</p>
<dt>&quot;paused&quot;</p>
<dd>guest has been paused via the &#8216;stop&#8217; command</p>
<dt>&quot;postmigrate&quot;</p>
<dd>guest is paused following a successful &#8216;migrate&#8217;</p>
<dt>&quot;prelaunch&quot;</p>
<dd><font SIZE="-1">QEMU</font> was started with -S and guest has not started</p>
<dt>&quot;restore-vm&quot;</p>
<dd>guest is paused to restore <font SIZE="-1">VM</font> state</p>
<dt>&quot;running&quot;</p>
<dd>guest is actively running</p>
<dt>&quot;save-vm&quot;</p>
<dd>guest is paused to save the <font SIZE="-1">VM</font> state</p>
<dt>&quot;shutdown&quot;</p>
<dd>guest is shut down (and -no-shutdown is in use)</p>
<dt>&quot;suspended&quot;</p>
<dd>guest is suspended (<font SIZE="-1">ACPI S3</font>)</p>
<dt>&quot;watchdog&quot;</p>
<dd>the watchdog action is configured to pause and has been triggered</p>
<dt>&quot;guest-panicked&quot;</p>
<dd>guest has been panicked as a result of guest <font SIZE="-1">OS</font> panic</p>
<dt>&quot;colo&quot;</p>
<dd>guest is paused to save/restore <font SIZE="-1">VM</font> state under colo checkpoint, <font SIZE="-1">VM</font> can not get into this state unless colo capability is enabled for migration. (since 2.8)</p>
<dt>&quot;preconfig&quot;</p>
<dd><font SIZE="-1">QEMU</font> is paused before board specific init callback is executed. The state is reachable only if the &#8211;preconfig <font SIZE="-1">CLI</font> option is used. (Since 3.0)</dl>
<p> <code>ShutdownCause</code> (Enum) An enumeration of reasons for a Shutdown. <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>No shutdown request pending</p>
<dt>&quot;host-error&quot;</p>
<dd>An error prevents further use of guest</p>
<dt>&quot;host-qmp-quit&quot;</p>
<dd>Reaction to the <font SIZE="-1">QMP</font> command &#8216;quit&#8217;</p>
<dt>&quot;host-qmp-system-reset&quot;</p>
<dd>Reaction to the <font SIZE="-1">QMP</font> command &#8216;system_reset&#8217;</p>
<dt>&quot;host-signal&quot;</p>
<dd>Reaction to a signal, such as <font SIZE="-1">SIGINT</font></p>
<dt>&quot;host-ui&quot;</p>
<dd>Reaction to a <font SIZE="-1">UI</font> event, like window close</p>
<dt>&quot;guest-shutdown&quot;</p>
<dd>Guest shutdown/suspend request, via <font SIZE="-1">ACPI</font> or other hardware-specific means</p>
<dt>&quot;guest-reset&quot;</p>
<dd>Guest reset request, and command line turns that into a shutdown</p>
<dt>&quot;guest-panic&quot;</p>
<dd>Guest panicked, and command line turns that into a shutdown</p>
<dt>&quot;subsystem-reset&quot;</p>
<dd>Partial guest reset that does not trigger <font SIZE="-1">QMP</font> events and ignores &#8211;no-reboot. This is useful for sanitizing hypercalls on s390 that are used during kexec/kdump/boot</dl>
<p> <code>StatusInfo</code> (Object) Information about <font SIZE="-1">VCPU</font> run state <code>Members:</code></p>
<dl>
<dt>&quot;running: boolean&quot;</p>
<dd>true if all VCPUs are runnable, false if not runnable</p>
<dt>&quot;singlestep: boolean&quot;</p>
<dd>true if VCPUs are in single-step mode</p>
<dt>&quot;status: RunState&quot;</p>
<dd>the virtual machine <tt>&quot;RunState&quot;</tt></dl>
<p> <code>Since:</code> 0.14.0 <code>Notes:</code> <tt>&quot;singlestep&quot;</tt> is enabled through the <font SIZE="-1">GDB</font> stub <code>query-status</code> (Command) Query the run status of all VCPUs <code>Returns:</code> <tt>&quot;StatusInfo&quot;</tt> reflecting all VCPUs <code>Since:</code> 0.14.0 <code>Example:</code> </p>
<pre><code>-&gt;{&quot;execute&quot; : &quot;query-status&quot;} &lt; -
{
    &quot;return&quot;:
    {
        &quot;running&quot; : true,
                    &quot;singlestep&quot; : false,
                                   &quot;status&quot; : &quot;running&quot;
    }
}</code></pre>
<p> <font SIZE="-1"><code>SHUTDOWN</code></font> (Event) Emitted when the virtual machine has shut down, indicating that qemu is about to exit. <code>Arguments:</code></p>
<dl>
<dt>&quot;guest: boolean&quot;</p>
<dd>If true, the shutdown was triggered by a guest request (such as a guest-initiated <font SIZE="-1">ACPI</font> shutdown request or other hardware-specific action) rather than a host request (such as sending qemu a <font SIZE="-1">SIGINT</font>). (since 2.10)</p>
<dt>&quot;reason: ShutdownCause&quot;</p>
<dd>The <tt>&quot;ShutdownCause&quot;</tt> which resulted in the <font SIZE="-1">SHUTDOWN.</font> (since 4.0)</dl>
<p> <code>Note:</code> If the command-line option &#8220;-no-shutdown&#8221; has been specified, qemu will not exit, and a <font SIZE="-1">STOP</font> event will eventually follow the <font SIZE="-1">SHUTDOWN</font> event <code>Since:</code> 0.12.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;SHUTDOWN&quot;, &quot;data&quot;: { &quot;guest&quot;: true },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1267040730, &quot;microseconds&quot;: 682951 } }</pre>
<p><font SIZE="-1"><code>POWERDOWN</code></font> (Event) Emitted when the virtual machine is powered down through the power control system, such as via <font SIZE="-1">ACPI.</font> <code>Since:</code> 0.12.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;POWERDOWN&quot;,
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1267040730, &quot;microseconds&quot;: 682951 } }</pre>
<p><font SIZE="-1"><code>RESET</code></font> (Event) Emitted when the virtual machine is reset <code>Arguments:</code></p>
<dl>
<dt>&quot;guest: boolean&quot;</p>
<dd>If true, the reset was triggered by a guest request (such as a guest-initiated <font SIZE="-1">ACPI</font> reboot request or other hardware-specific action) rather than a host request (such as the <font SIZE="-1">QMP</font> command system_reset). (since 2.10)</p>
<dt>&quot;reason: ShutdownCause&quot;</p>
<dd>The <tt>&quot;ShutdownCause&quot;</tt> of the <font SIZE="-1">RESET.</font> (since 4.0)</dl>
<p> <code>Since:</code> 0.12.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;RESET&quot;, &quot;data&quot;: { &quot;guest&quot;: false },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1267041653, &quot;microseconds&quot;: 9518 } }</pre>
<p><font SIZE="-1"><code>STOP</code></font> (Event) Emitted when the virtual machine is stopped <code>Since:</code> 0.12.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;STOP&quot;,
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1267041730, &quot;microseconds&quot;: 281295 } }</pre>
<p><font SIZE="-1"><code>RESUME</code></font> (Event) Emitted when the virtual machine resumes execution <code>Since:</code> 0.12.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;RESUME&quot;,
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1271770767, &quot;microseconds&quot;: 582542 } }</pre>
<p><font SIZE="-1"><code>SUSPEND</code></font> (Event) Emitted when guest enters a hardware suspension state, for example, S3 state, which is sometimes called standby state <code>Since:</code> 1.1 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;SUSPEND&quot;,
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1344456160, &quot;microseconds&quot;: 309119 } }</pre>
<p><font SIZE="-1"><code>SUSPEND_DISK</code></font> (Event) Emitted when guest enters a hardware suspension state with data saved on disk, for example, S4 state, which is sometimes called hibernate state <code>Note:</code> <font SIZE="-1">QEMU</font> shuts down (similar to event <tt>&quot;SHUTDOWN&quot;</tt>) when entering this state <code>Since:</code> 1.2 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;SUSPEND_DISK&quot;,
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1344456160, &quot;microseconds&quot;: 309119 } }</pre>
<p><font SIZE="-1"><code>WAKEUP</code></font> (Event) Emitted when the guest has woken up from suspend state and is running <code>Since:</code> 1.1 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;WAKEUP&quot;,
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1344522075, &quot;microseconds&quot;: 745528 } }</pre>
<p><font SIZE="-1"><code>WATCHDOG</code></font> (Event) Emitted when the watchdog device&#8217;s timer is expired <code>Arguments:</code></p>
<dl>
<dt>&quot;action: WatchdogAction&quot;</p>
<dd>action that has been taken</dl>
<p> <code>Note:</code> If action is &#8220;reset&#8221;, &#8220;shutdown&#8221;, or &#8220;pause&#8221; the <font SIZE="-1">WATCHDOG</font> event is followed respectively by the <font SIZE="-1">RESET, SHUTDOWN,</font> or <font SIZE="-1">STOP</font> events <code>Note:</code> This event is rate-limited. <code>Since:</code> 0.13.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;WATCHDOG&quot;,
 &quot;data&quot;: { &quot;action&quot;: &quot;reset&quot; },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1267061043, &quot;microseconds&quot;: 959568 } }</pre>
<p><code>WatchdogAction</code> (Enum) An enumeration of the actions taken when the watchdog device&#8217;s timer is expired <code>Values:</code></p>
<dl>
<dt>&quot;reset&quot;</p>
<dd>system resets</p>
<dt>&quot;shutdown&quot;</p>
<dd>system shutdown, note that it is similar to <tt>&quot;powerdown&quot;</tt>, which tries to set to system status and notify guest</p>
<dt>&quot;poweroff&quot;</p>
<dd>system poweroff, the emulator program exits</p>
<dt>&quot;pause&quot;</p>
<dd>system pauses, similar to <tt>&quot;stop&quot;</tt></p>
<dt>&quot;debug&quot;</p>
<dd>system enters debug state</p>
<dt>&quot;none&quot;</p>
<dd>nothing is done</p>
<dt>&quot;inject-nmi&quot;</p>
<dd>a non-maskable interrupt is injected into the first <font SIZE="-1">VCPU</font> (all <font SIZE="-1">VCPUS</font> on x86) (since 2.4)</dl>
<p> <code>Since:</code> 2.1 <code>watchdog-set-action</code> (Command) Set watchdog action <code>Arguments:</code></p>
<dl>
<dt>&quot;action: WatchdogAction&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.11 <font SIZE="-1"><code>GUEST_PANICKED</code></font> (Event) Emitted when guest <font SIZE="-1">OS</font> panic is detected <code>Arguments:</code></p>
<dl>
<dt>&quot;action: GuestPanicAction&quot;</p>
<dd>action that has been taken, currently always &#8220;pause&#8221;</p>
<dt>&quot;info: GuestPanicInformation&quot; (optional)</p>
<dd>information about a panic (since 2.9)</dl>
<p> <code>Since:</code> 1.5 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;GUEST_PANICKED&quot;,
 &quot;data&quot;: { &quot;action&quot;: &quot;pause&quot; } }</pre>
<p><code>GuestPanicAction</code> (Enum) An enumeration of the actions taken when guest <font SIZE="-1">OS</font> panic is detected <code>Values:</code></p>
<dl>
<dt>&quot;pause&quot;</p>
<dd>system pauses</p>
<dt>&quot;poweroff&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.1 (poweroff since 2.8) <code>GuestPanicInformationType</code> (Enum) An enumeration of the guest panic information types <code>Values:</code></p>
<dl>
<dt>&quot;hyper-v&quot;</p>
<dd>hyper-v guest panic information type</p>
<dt>&quot;s390&quot;</p>
<dd>s390 guest panic information type (Since: 2.12)</dl>
<p> <code>Since:</code> 2.9 <code>GuestPanicInformation</code> (Object) Information about a guest panic <code>Members:</code></p>
<dl>
<dt>&quot;type: GuestPanicInformationType&quot;</p>
<dd>Crash type that defines the hypervisor specific information</p>
<dt>The members of &quot;GuestPanicInformationHyperV&quot; when &quot;type&quot; is &quot;hyper-v&quot;</p>
<dd>
<dt>The members of &quot;GuestPanicInformationS390&quot; when &quot;type&quot; is &quot;s390&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.9 <code>GuestPanicInformationHyperV</code> (Object) Hyper-V specific guest panic information (<font SIZE="-1">HV</font> crash MSRs) <code>Members:</code></p>
<dl>
<dt>&quot;arg1: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;arg2: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;arg3: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;arg4: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;arg5: int&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.9 <code>S390CrashReason</code> (Enum) Reason why the <font SIZE="-1">CPU</font> is in a crashed state. <code>Values:</code></p>
<dl>
<dt>&quot;unknown&quot;</p>
<dd>no crash reason was set</p>
<dt>&quot;disabled-wait&quot;</p>
<dd>the <font SIZE="-1">CPU</font> has entered a disabled wait state</p>
<dt>&quot;extint-loop&quot;</p>
<dd>clock comparator or cpu timer interrupt with new <font SIZE="-1">PSW</font> enabled for external interrupts</p>
<dt>&quot;pgmint-loop&quot;</p>
<dd>program interrupt with <font SIZE="-1">BAD</font> new <font SIZE="-1">PSW</font></p>
<dt>&quot;opint-loop&quot;</p>
<dd>operation exception interrupt with invalid code at the program interrupt new <font SIZE="-1">PSW</font></dl>
<p> <code>Since:</code> 2.12 <code>GuestPanicInformationS390</code> (Object) S390 specific guest panic information (<font SIZE="-1">PSW</font>) <code>Members:</code></p>
<dl>
<dt>&quot;core: int&quot;</p>
<dd>core id of the <font SIZE="-1">CPU</font> that crashed</p>
<dt>&quot;psw-mask: int&quot;</p>
<dd>control fields of guest <font SIZE="-1">PSW</font></p>
<dt>&quot;psw-addr: int&quot;</p>
<dd>guest instruction address</p>
<dt>&quot;reason: S390CrashReason&quot;</p>
<dd>guest crash reason</dl>
<p> <code>Since:</code> 2.12</p>
<h3>Cryptography</h3>
<p><code>QCryptoTLSCredsEndpoint</code> (Enum) The type of network endpoint that will be using the credentials. Most types of credential require different setup / structures depending on whether they will be used in a server versus a client. <code>Values:</code></p>
<dl>
<dt>&quot;client&quot;</p>
<dd>the network endpoint is acting as the client</p>
<dt>&quot;server&quot;</p>
<dd>the network endpoint is acting as the server</dl>
<p> <code>Since:</code> 2.5 <code>QCryptoSecretFormat</code> (Enum) The data format that the secret is provided in <code>Values:</code></p>
<dl>
<dt>&quot;raw&quot;</p>
<dd>raw bytes. When encoded in <font SIZE="-1">JSON</font> only valid <font SIZE="-1">UTF-8</font> sequences can be used</p>
<dt>&quot;base64&quot;</p>
<dd>arbitrary base64 encoded binary data</dl>
<p> <code>Since:</code> 2.6 <code>QCryptoHashAlgorithm</code> (Enum) The supported algorithms for computing content digests <code>Values:</code></p>
<dl>
<dt>&quot;md5&quot;</p>
<dd><font SIZE="-1">MD5.</font> Should not be used in any new code, legacy compat only</p>
<dt>&quot;sha1&quot;</p>
<dd><font SIZE="-1">SHA-1.</font> Should not be used in any new code, legacy compat only</p>
<dt>&quot;sha224&quot;</p>
<dd><font SIZE="-1">SHA-224.</font> (since 2.7)</p>
<dt>&quot;sha256&quot;</p>
<dd><font SIZE="-1">SHA-256.</font> Current recommended strong hash.</p>
<dt>&quot;sha384&quot;</p>
<dd><font SIZE="-1">SHA-384.</font> (since 2.7)</p>
<dt>&quot;sha512&quot;</p>
<dd><font SIZE="-1">SHA-512.</font> (since 2.7)</p>
<dt>&quot;ripemd160&quot;</p>
<dd><font SIZE="-1">RIPEMD-160.</font> (since 2.7)</dl>
<p> <code>Since:</code> 2.6 <code>QCryptoCipherAlgorithm</code> (Enum) The supported algorithms for content encryption ciphers <code>Values:</code></p>
<dl>
<dt>&quot;aes-128&quot;</p>
<dd><font SIZE="-1">AES</font> with 128 bit / 16 byte keys</p>
<dt>&quot;aes-192&quot;</p>
<dd><font SIZE="-1">AES</font> with 192 bit / 24 byte keys</p>
<dt>&quot;aes-256&quot;</p>
<dd><font SIZE="-1">AES</font> with 256 bit / 32 byte keys</p>
<dt>&quot;des-rfb&quot;</p>
<dd><font SIZE="-1">RFB</font> specific variant of single <font SIZE="-1">DES.</font> Do not use except in <font SIZE="-1">VNC.</font></p>
<dt>&quot;3des&quot;</p>
<dd>3DES(<font SIZE="-1">EDE</font>) with 192 bit / 24 byte keys (since 2.9)</p>
<dt>&quot;cast5-128&quot;</p>
<dd>Cast5 with 128 bit / 16 byte keys</p>
<dt>&quot;serpent-128&quot;</p>
<dd>Serpent with 128 bit / 16 byte keys</p>
<dt>&quot;serpent-192&quot;</p>
<dd>Serpent with 192 bit / 24 byte keys</p>
<dt>&quot;serpent-256&quot;</p>
<dd>Serpent with 256 bit / 32 byte keys</p>
<dt>&quot;twofish-128&quot;</p>
<dd>Twofish with 128 bit / 16 byte keys</p>
<dt>&quot;twofish-192&quot;</p>
<dd>Twofish with 192 bit / 24 byte keys</p>
<dt>&quot;twofish-256&quot;</p>
<dd>Twofish with 256 bit / 32 byte keys</dl>
<p> <code>Since:</code> 2.6 <code>QCryptoCipherMode</code> (Enum) The supported modes for content encryption ciphers <code>Values:</code></p>
<dl>
<dt>&quot;ecb&quot;</p>
<dd>Electronic Code Book</p>
<dt>&quot;cbc&quot;</p>
<dd>Cipher Block Chaining</p>
<dt>&quot;xts&quot;</p>
<dd><font SIZE="-1">XEX</font> with tweaked code book and ciphertext stealing</p>
<dt>&quot;ctr&quot;</p>
<dd>Counter (Since 2.8)</dl>
<p> <code>Since:</code> 2.6 <code>QCryptoIVGenAlgorithm</code> (Enum) The supported algorithms for generating initialization vectors for full disk encryption. The &#8216;plain&#8217; generator should not be used for disks with sector numbers larger than 2^32, except where compatibility with pre-existing Linux dm-crypt volumes is required. <code>Values:</code></p>
<dl>
<dt>&quot;plain&quot;</p>
<dd>64-bit sector number truncated to 32-bits</p>
<dt>&quot;plain64&quot;</p>
<dd>64-bit sector number</p>
<dt>&quot;essiv&quot;</p>
<dd>64-bit sector number encrypted with a hash of the encryption key</dl>
<p> <code>Since:</code> 2.6 <code>QCryptoBlockFormat</code> (Enum) The supported full disk encryption formats <code>Values:</code></p>
<dl>
<dt>&quot;qcow&quot;</p>
<dd>QCow/QCow2 built-in AES-CBC encryption. Use only for liberating data from old images.</p>
<dt>&quot;luks&quot;</p>
<dd><font SIZE="-1">LUKS</font> encryption format. Recommended for new images</dl>
<p> <code>Since:</code> 2.6 <code>QCryptoBlockOptionsBase</code> (Object) The common options that apply to all full disk encryption formats <code>Members:</code></p>
<dl>
<dt>&quot;format: QCryptoBlockFormat&quot;</p>
<dd>the encryption format</dl>
<p> <code>Since:</code> 2.6 <code>QCryptoBlockOptionsQCow</code> (Object) The options that apply to QCow/QCow2 AES-CBC encryption format <code>Members:</code></p>
<dl>
<dt>&quot;key-secret: string&quot; (optional)</p>
<dd>the <font SIZE="-1">ID</font> of a QCryptoSecret object providing the decryption key. Mandatory except when probing image for metadata only.</dl>
<p> <code>Since:</code> 2.6 <code>QCryptoBlockOptionsLUKS</code> (Object) The options that apply to <font SIZE="-1">LUKS</font> encryption format <code>Members:</code></p>
<dl>
<dt>&quot;key-secret: string&quot; (optional)</p>
<dd>the <font SIZE="-1">ID</font> of a QCryptoSecret object providing the decryption key. Mandatory except when probing image for metadata only.</dl>
<p> <code>Since:</code> 2.6 <code>QCryptoBlockCreateOptionsLUKS</code> (Object) The options that apply to <font SIZE="-1">LUKS</font> encryption format initialization <code>Members:</code></p>
<dl>
<dt>&quot;cipher-alg: QCryptoCipherAlgorithm&quot; (optional)</p>
<dd>the cipher algorithm for data encryption Currently defaults to &#8216;aes-256&#8217;.</p>
<dt>&quot;cipher-mode: QCryptoCipherMode&quot; (optional)</p>
<dd>the cipher mode for data encryption Currently defaults to &#8216;xts&#8217;</p>
<dt>&quot;ivgen-alg: QCryptoIVGenAlgorithm&quot; (optional)</p>
<dd>the initialization vector generator Currently defaults to &#8216;plain64&#8217;</p>
<dt>&quot;ivgen-hash-alg: QCryptoHashAlgorithm&quot; (optional)</p>
<dd>the initialization vector generator hash Currently defaults to &#8216;sha256&#8217;</p>
<dt>&quot;hash-alg: QCryptoHashAlgorithm&quot; (optional)</p>
<dd>the master key hash algorithm Currently defaults to &#8216;sha256&#8217;</p>
<dt>&quot;iter-time: int&quot; (optional)</p>
<dd>number of milliseconds to spend in <font SIZE="-1">PBKDF</font> passphrase processing. Currently defaults to 2000. (since 2.8)</p>
<dt>The members of &quot;QCryptoBlockOptionsLUKS&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.6 <code>QCryptoBlockOpenOptions</code> (Object) The options that are available for all encryption formats when opening an existing volume <code>Members:</code></p>
<dl>
<dt>The members of &quot;QCryptoBlockOptionsBase&quot;</p>
<dd>
<dt>The members of &quot;QCryptoBlockOptionsQCow&quot; when &quot;format&quot; is &quot;qcow&quot;</p>
<dd>
<dt>The members of &quot;QCryptoBlockOptionsLUKS&quot; when &quot;format&quot; is &quot;luks&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.6 <code>QCryptoBlockCreateOptions</code> (Object) The options that are available for all encryption formats when initializing a new volume <code>Members:</code></p>
<dl>
<dt>The members of &quot;QCryptoBlockOptionsBase&quot;</p>
<dd>
<dt>The members of &quot;QCryptoBlockOptionsQCow&quot; when &quot;format&quot; is &quot;qcow&quot;</p>
<dd>
<dt>The members of &quot;QCryptoBlockCreateOptionsLUKS&quot; when &quot;format&quot; is &quot;luks&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.6 <code>QCryptoBlockInfoBase</code> (Object) The common information that applies to all full disk encryption formats <code>Members:</code></p>
<dl>
<dt>&quot;format: QCryptoBlockFormat&quot;</p>
<dd>the encryption format</dl>
<p> <code>Since:</code> 2.7 <code>QCryptoBlockInfoLUKSSlot</code> (Object) Information about the <font SIZE="-1">LUKS</font> block encryption key slot options <code>Members:</code></p>
<dl>
<dt>&quot;active: boolean&quot;</p>
<dd>whether the key slot is currently in use</p>
<dt>&quot;key-offset: int&quot;</p>
<dd>offset to the key material in bytes</p>
<dt>&quot;iters: int&quot; (optional)</p>
<dd>number of <font SIZE="-1">PBKDF2</font> iterations for key material</p>
<dt>&quot;stripes: int&quot; (optional)</p>
<dd>number of stripes for splitting key material</dl>
<p> <code>Since:</code> 2.7 <code>QCryptoBlockInfoLUKS</code> (Object) Information about the <font SIZE="-1">LUKS</font> block encryption options <code>Members:</code></p>
<dl>
<dt>&quot;cipher-alg: QCryptoCipherAlgorithm&quot;</p>
<dd>the cipher algorithm for data encryption</p>
<dt>&quot;cipher-mode: QCryptoCipherMode&quot;</p>
<dd>the cipher mode for data encryption</p>
<dt>&quot;ivgen-alg: QCryptoIVGenAlgorithm&quot;</p>
<dd>the initialization vector generator</p>
<dt>&quot;ivgen-hash-alg: QCryptoHashAlgorithm&quot; (optional)</p>
<dd>the initialization vector generator hash</p>
<dt>&quot;hash-alg: QCryptoHashAlgorithm&quot;</p>
<dd>the master key hash algorithm</p>
<dt>&quot;payload-offset: int&quot;</p>
<dd>offset to the payload data in bytes</p>
<dt>&quot;master-key-iters: int&quot;</p>
<dd>number of <font SIZE="-1">PBKDF2</font> iterations for key material</p>
<dt>&quot;uuid: string&quot;</p>
<dd>unique identifier for the volume</p>
<dt>&quot;slots: array of QCryptoBlockInfoLUKSSlot&quot;</p>
<dd>information about each key slot</dl>
<p> <code>Since:</code> 2.7 <code>QCryptoBlockInfo</code> (Object) Information about the block encryption options <code>Members:</code></p>
<dl>
<dt>The members of &quot;QCryptoBlockInfoBase&quot;</p>
<dd>
<dt>The members of &quot;QCryptoBlockInfoLUKS&quot; when &quot;format&quot; is &quot;luks&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.7</p>
<h3>Block devices</h3>
<p><i>Block core (</i><font SIZE="-1"><i>VM</i></font><i> unrelated)</i> <i>Background jobs</i> <code>JobType</code> (Enum) Type of a background job. <code>Values:</code></p>
<dl>
<dt>&quot;commit&quot;</p>
<dd>block commit job type, see &#8220;block-commit&#8221;</p>
<dt>&quot;stream&quot;</p>
<dd>block stream job type, see &#8220;block-stream&#8221;</p>
<dt>&quot;mirror&quot;</p>
<dd>drive mirror job type, see &#8220;drive-mirror&#8221;</p>
<dt>&quot;backup&quot;</p>
<dd>drive backup job type, see &#8220;drive-backup&#8221;</p>
<dt>&quot;create&quot;</p>
<dd>image creation job type, see &#8220;blockdev-create&#8221; (since 3.0)</dl>
<p> <code>Since:</code> 1.7 <code>JobStatus</code> (Enum) Indicates the present state of a given job in its lifetime. <code>Values:</code></p>
<dl>
<dt>&quot;undefined&quot;</p>
<dd>Erroneous, default state. Should not ever be visible.</p>
<dt>&quot;created&quot;</p>
<dd>The job has been created, but not yet started.</p>
<dt>&quot;running&quot;</p>
<dd>The job is currently running.</p>
<dt>&quot;paused&quot;</p>
<dd>The job is running, but paused. The pause may be requested by either the <font SIZE="-1">QMP</font> user or by internal processes.</p>
<dt>&quot;ready&quot;</p>
<dd>The job is running, but is ready for the user to signal completion. This is used for long-running jobs like mirror that are designed to run indefinitely.</p>
<dt>&quot;standby&quot;</p>
<dd>The job is ready, but paused. This is nearly identical to <tt>&quot;paused&quot;</tt>. The job may return to <tt>&quot;ready&quot;</tt> or otherwise be canceled.</p>
<dt>&quot;waiting&quot;</p>
<dd>The job is waiting for other jobs in the transaction to converge to the waiting state. This status will likely not be visible for the last job in a transaction.</p>
<dt>&quot;pending&quot;</p>
<dd>The job has finished its work, but has finalization steps that it needs to make prior to completing. These changes will require manual intervention via <tt>&quot;job-finalize&quot;</tt> if auto-finalize was set to false. These pending changes may still fail.</p>
<dt>&quot;aborting&quot;</p>
<dd>The job is in the process of being aborted, and will finish with an error. The job will afterwards report that it is <tt>&quot;concluded&quot;</tt>. This status may not be visible to the management process.</p>
<dt>&quot;concluded&quot;</p>
<dd>The job has finished all work. If auto-dismiss was set to false, the job will remain in the query list until it is dismissed via <tt>&quot;job-dismiss&quot;</tt>.</p>
<dt>&quot;null&quot;</p>
<dd>The job is in the process of being dismantled. This state should not ever be visible externally.</dl>
<p> <code>Since:</code> 2.12 <code>JobVerb</code> (Enum) Represents command verbs that can be applied to a job. <code>Values:</code></p>
<dl>
<dt>&quot;cancel&quot;</p>
<dd>see <tt>&quot;job-cancel&quot;</tt></p>
<dt>&quot;pause&quot;</p>
<dd>see <tt>&quot;job-pause&quot;</tt></p>
<dt>&quot;resume&quot;</p>
<dd>see <tt>&quot;job-resume&quot;</tt></p>
<dt>&quot;set-speed&quot;</p>
<dd>see <tt>&quot;block-job-set-speed&quot;</tt></p>
<dt>&quot;complete&quot;</p>
<dd>see <tt>&quot;job-complete&quot;</tt></p>
<dt>&quot;dismiss&quot;</p>
<dd>see <tt>&quot;job-dismiss&quot;</tt></p>
<dt>&quot;finalize&quot;</p>
<dd>see <tt>&quot;job-finalize&quot;</tt></dl>
<p> <code>Since:</code> 2.12 <font SIZE="-1"><code>JOB_STATUS_CHANGE</code></font> (Event) Emitted when a job transitions to a different status. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The job identifier</p>
<dt>&quot;status: JobStatus&quot;</p>
<dd>The new job status</dl>
<p> <code>Since:</code> 3.0 <code>job-pause</code> (Command) Pause an active job. This command returns immediately after marking the active job for pausing. Pausing an already paused job is an error. The job will pause as soon as possible, which means transitioning into the <font SIZE="-1">PAUSED</font> state if it was <font SIZE="-1">RUNNING,</font> or into <font SIZE="-1">STANDBY</font> if it was <font SIZE="-1">READY.</font> The corresponding <font SIZE="-1">JOB_STATUS_CHANGE</font> event will be emitted. Cancelling a paused job automatically resumes it. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The job identifier.</dl>
<p> <code>Since:</code> 3.0 <code>job-resume</code> (Command) Resume a paused job. This command returns immediately after resuming a paused job. Resuming an already running job is an error. <tt>&quot;id&quot;</tt> : The job identifier. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 3.0 <code>job-cancel</code> (Command) Instruct an active background job to cancel at the next opportunity. This command returns immediately after marking the active job for cancellation. The job will cancel as soon as possible and then emit a <font SIZE="-1">JOB_STATUS_CHANGE</font> event. Usually, the status will change to <font SIZE="-1">ABORTING,</font> but it is possible that a job successfully completes (e.g. because it was almost done and there was no opportunity to cancel earlier than completing the job) and transitions to <font SIZE="-1">PENDING</font> instead. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The job identifier.</dl>
<p> <code>Since:</code> 3.0 <code>job-complete</code> (Command) Manually trigger completion of an active job in the <font SIZE="-1">READY</font> state. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The job identifier.</dl>
<p> <code>Since:</code> 3.0 <code>job-dismiss</code> (Command) Deletes a job that is in the <font SIZE="-1">CONCLUDED</font> state. This command only needs to be run explicitly for jobs that don&#8217;t have automatic dismiss enabled. This command will refuse to operate on any job that has not yet reached its terminal state, <font SIZE="-1">JOB_STATUS_CONCLUDED.</font> For jobs that make use of <font SIZE="-1">JOB_READY</font> event, job-cancel or job-complete will still need to be used as appropriate. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The job identifier.</dl>
<p> <code>Since:</code> 3.0 <code>job-finalize</code> (Command) Instructs all jobs in a transaction (or a single job if it is not part of any transaction) to finalize any graph changes and do any necessary cleanup. This command requires that all involved jobs are in the <font SIZE="-1">PENDING</font> state. For jobs in a transaction, instructing one job to finalize will force <font SIZE="-1">ALL</font> jobs in the transaction to finalize, so it is only necessary to instruct a single member job to finalize. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The identifier of any job in the transaction, or of a job that is not part of any transaction.</dl>
<p> <code>Since:</code> 3.0 <code>JobInfo</code> (Object) Information about a job. <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The job identifier</p>
<dt>&quot;type: JobType&quot;</p>
<dd>The kind of job that is being performed</p>
<dt>&quot;status: JobStatus&quot;</p>
<dd>Current job state/status</p>
<dt>&quot;current-progress: int&quot;</p>
<dd>Progress made until now. The unit is arbitrary and the value can only meaningfully be used for the ratio of <tt>&quot;current-progress&quot;</tt> to <tt>&quot;total-progress&quot;</tt>. The value is monotonically increasing.</p>
<dt>&quot;total-progress: int&quot;</p>
<dd>Estimated <tt>&quot;current-progress&quot;</tt> value at the completion of the job. This value can arbitrarily change while the job is running, in both directions.</p>
<dt>&quot;error: string&quot; (optional)</p>
<dd>If this field is present, the job failed; if it is still missing in the <font SIZE="-1">CONCLUDED</font> state, this indicates successful completion. The value is a human-readable error message to describe the reason for the job failure. It should not be parsed by applications.</dl>
<p> <code>Since:</code> 3.0 <code>query-jobs</code> (Command) Return information about jobs. <code>Returns:</code> a list with a <tt>&quot;JobInfo&quot;</tt> for each active job <code>Since:</code> 3.0 <code>SnapshotInfo</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>unique snapshot id</p>
<dt>&quot;name: string&quot;</p>
<dd>user chosen name</p>
<dt>&quot;vm-state-size: int&quot;</p>
<dd>size of the <font SIZE="-1">VM</font> state</p>
<dt>&quot;date-sec: int&quot;</p>
<dd><font SIZE="-1">UTC</font> date of the snapshot in seconds</p>
<dt>&quot;date-nsec: int&quot;</p>
<dd>fractional part in nano seconds to be used with date-sec</p>
<dt>&quot;vm-clock-sec: int&quot;</p>
<dd><font SIZE="-1">VM</font> clock relative to boot in seconds</p>
<dt>&quot;vm-clock-nsec: int&quot;</p>
<dd>fractional part in nano seconds to be used with vm-clock-sec</dl>
<p> <code>Since:</code> 1.3 <code>ImageInfoSpecificQCow2EncryptionBase</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;format: BlockdevQcow2EncryptionFormat&quot;</p>
<dd>The encryption format</dl>
<p> <code>Since:</code> 2.10 <code>ImageInfoSpecificQCow2Encryption</code> (Object) <code>Members:</code></p>
<dl>
<dt>The members of &quot;ImageInfoSpecificQCow2EncryptionBase&quot;</p>
<dd>
<dt>The members of &quot;QCryptoBlockInfoLUKS&quot; when &quot;format&quot; is &quot;luks&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.10 <code>ImageInfoSpecificQCow2</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;compat: string&quot;</p>
<dd>compatibility level</p>
<dt>&quot;data-file: string&quot; (optional)</p>
<dd>the filename of the external data file that is stored in the image and used as a default for opening the image (since: 4.0)</p>
<dt>&quot;data-file-raw: boolean&quot; (optional)</p>
<dd>True if the external data file must stay valid as a standalone (read-only) raw image without looking at qcow2 metadata (since: 4.0)</p>
<dt>&quot;lazy-refcounts: boolean&quot; (optional)</p>
<dd>on or off; only valid for compat &gt;= 1.1</p>
<dt>&quot;corrupt: boolean&quot; (optional)</p>
<dd>true if the image has been marked corrupt; only valid for compat &gt;= 1.1 (since 2.2)</p>
<dt>&quot;refcount-bits: int&quot;</p>
<dd>width of a refcount entry in bits (since 2.3)</p>
<dt>&quot;encrypt: ImageInfoSpecificQCow2Encryption&quot; (optional)</p>
<dd>details about encryption parameters; only set if image is encrypted (since 2.10)</p>
<dt>&quot;bitmaps: array of Qcow2BitmapInfo&quot; (optional)</p>
<dd>A list of qcow2 bitmap details (since 4.0)</dl>
<p> <code>Since:</code> 1.7 <code>ImageInfoSpecificVmdk</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;create-type: string&quot;</p>
<dd>The create type of <font SIZE="-1">VMDK</font> image</p>
<dt>&quot;cid: int&quot;</p>
<dd>Content id of image</p>
<dt>&quot;parent-cid: int&quot;</p>
<dd>Parent <font SIZE="-1">VMDK</font> image&#8217;s cid</p>
<dt>&quot;extents: array of ImageInfo&quot;</p>
<dd>List of extent files</dl>
<p> <code>Since:</code> 1.7 <code>ImageInfoSpecific</code> (Object) A discriminated record of image format specific information structures. <code>Members:</code></p>
<dl>
<dt>&quot;type&quot;</p>
<dd>One of &#8220;qcow2&#8221;, &#8220;vmdk&#8221;, &#8220;luks&#8221;</p>
<dt>&quot;data: ImageInfoSpecificQCow2&quot; when &quot;type&quot; is &quot;qcow2&quot;</p>
<dd>
<dt>&quot;data: ImageInfoSpecificVmdk&quot; when &quot;type&quot; is &quot;vmdk&quot;</p>
<dd>
<dt>&quot;data: QCryptoBlockInfoLUKS&quot; when &quot;type&quot; is &quot;luks&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.7 <code>ImageInfo</code> (Object) Information about a <font SIZE="-1">QEMU</font> image file <code>Members:</code></p>
<dl>
<dt>&quot;filename: string&quot;</p>
<dd>name of the image file</p>
<dt>&quot;format: string&quot;</p>
<dd>format of the image file</p>
<dt>&quot;virtual-size: int&quot;</p>
<dd>maximum capacity in bytes of the image</p>
<dt>&quot;actual-size: int&quot; (optional)</p>
<dd>actual size on disk in bytes of the image</p>
<dt>&quot;dirty-flag: boolean&quot; (optional)</p>
<dd>true if image is not cleanly closed</p>
<dt>&quot;cluster-size: int&quot; (optional)</p>
<dd>size of a cluster in bytes</p>
<dt>&quot;encrypted: boolean&quot; (optional)</p>
<dd>true if the image is encrypted</p>
<dt>&quot;compressed: boolean&quot; (optional)</p>
<dd>true if the image is compressed (Since 1.7)</p>
<dt>&quot;backing-filename: string&quot; (optional)</p>
<dd>name of the backing file</p>
<dt>&quot;full-backing-filename: string&quot; (optional)</p>
<dd>full path of the backing file</p>
<dt>&quot;backing-filename-format: string&quot; (optional)</p>
<dd>the format of the backing file</p>
<dt>&quot;snapshots: array of SnapshotInfo&quot; (optional)</p>
<dd>list of <font SIZE="-1">VM</font> snapshots</p>
<dt>&quot;backing-image: ImageInfo&quot; (optional)</p>
<dd>info of the backing image (since 1.6)</p>
<dt>&quot;format-specific: ImageInfoSpecific&quot; (optional)</p>
<dd>structure supplying additional format-specific information (since 1.7)</dl>
<p> <code>Since:</code> 1.3 <code>ImageCheck</code> (Object) Information about a <font SIZE="-1">QEMU</font> image file check <code>Members:</code></p>
<dl>
<dt>&quot;filename: string&quot;</p>
<dd>name of the image file checked</p>
<dt>&quot;format: string&quot;</p>
<dd>format of the image file checked</p>
<dt>&quot;check-errors: int&quot;</p>
<dd>number of unexpected errors occurred during check</p>
<dt>&quot;image-end-offset: int&quot; (optional)</p>
<dd>offset (in bytes) where the image ends, this field is present if the driver for the image format supports it</p>
<dt>&quot;corruptions: int&quot; (optional)</p>
<dd>number of corruptions found during the check if any</p>
<dt>&quot;leaks: int&quot; (optional)</p>
<dd>number of leaks found during the check if any</p>
<dt>&quot;corruptions-fixed: int&quot; (optional)</p>
<dd>number of corruptions fixed during the check if any</p>
<dt>&quot;leaks-fixed: int&quot; (optional)</p>
<dd>number of leaks fixed during the check if any</p>
<dt>&quot;total-clusters: int&quot; (optional)</p>
<dd>total number of clusters, this field is present if the driver for the image format supports it</p>
<dt>&quot;allocated-clusters: int&quot; (optional)</p>
<dd>total number of allocated clusters, this field is present if the driver for the image format supports it</p>
<dt>&quot;fragmented-clusters: int&quot; (optional)</p>
<dd>total number of fragmented clusters, this field is present if the driver for the image format supports it</p>
<dt>&quot;compressed-clusters: int&quot; (optional)</p>
<dd>total number of compressed clusters, this field is present if the driver for the image format supports it</dl>
<p> <code>Since:</code> 1.4 <code>MapEntry</code> (Object) Mapping information from a virtual block range to a host file range <code>Members:</code></p>
<dl>
<dt>&quot;start: int&quot;</p>
<dd>the start byte of the mapped virtual range</p>
<dt>&quot;length: int&quot;</p>
<dd>the number of bytes of the mapped virtual range</p>
<dt>&quot;data: boolean&quot;</p>
<dd>whether the mapped range has data</p>
<dt>&quot;zero: boolean&quot;</p>
<dd>whether the virtual blocks are zeroed</p>
<dt>&quot;depth: int&quot;</p>
<dd>the depth of the mapping</p>
<dt>&quot;offset: int&quot; (optional)</p>
<dd>the offset in file that the virtual sectors are mapped to</p>
<dt>&quot;filename: string&quot; (optional)</p>
<dd>filename that is referred to by <tt>&quot;offset&quot;</tt></dl>
<p> <code>Since:</code> 2.6 <code>BlockdevCacheInfo</code> (Object) Cache mode information for a block device <code>Members:</code></p>
<dl>
<dt>&quot;writeback: boolean&quot;</p>
<dd>true if writeback mode is enabled</p>
<dt>&quot;direct: boolean&quot;</p>
<dd>true if the host page cache is bypassed (O_DIRECT)</p>
<dt>&quot;no-flush: boolean&quot;</p>
<dd>true if flush requests are ignored for the device</dl>
<p> <code>Since:</code> 2.3 <code>BlockDeviceInfo</code> (Object) Information about the backing device for a block device. <code>Members:</code></p>
<dl>
<dt>&quot;file: string&quot;</p>
<dd>the filename of the backing device</p>
<dt>&quot;node-name: string&quot; (optional)</p>
<dd>the name of the block driver node (Since 2.0)</p>
<dt>&quot;ro: boolean&quot;</p>
<dd>true if the backing device was open read-only</p>
<dt>&quot;drv: string&quot;</p>
<dd>the name of the block format used to open the backing device. As of 0.14.0 this can be: &#8216;blkdebug&#8217;, &#8216;bochs&#8217;, &#8216;cloop&#8217;, &#8216;cow&#8217;, &#8216;dmg&#8217;, &#8216;file&#8217;, &#8216;file&#8217;, &#8216;ftp&#8217;, &#8216;ftps&#8217;, &#8216;host_cdrom&#8217;, &#8216;host_device&#8217;, &#8216;http&#8217;, &#8216;https&#8217;, &#8216;luks&#8217;, &#8216;nbd&#8217;, &#8216;parallels&#8217;, &#8216;qcow&#8217;, &#8216;qcow2&#8217;, &#8216;raw&#8217;, &#8216;vdi&#8217;, &#8216;vmdk&#8217;, &#8216;vpc&#8217;, &#8216;vvfat&#8217; 2.2: &#8216;archipelago&#8217; added, &#8216;cow&#8217; dropped 2.3: &#8216;host_floppy&#8217; deprecated 2.5: &#8216;host_floppy&#8217; dropped 2.6: &#8216;luks&#8217; added 2.8: &#8216;replication&#8217; added, &#8216;tftp&#8217; dropped 2.9: &#8216;archipelago&#8217; dropped</p>
<dt>&quot;backing_file: string&quot; (optional)</p>
<dd>the name of the backing file (for copy-on-write)</p>
<dt>&quot;backing_file_depth: int&quot;</p>
<dd>number of files in the backing file chain (since: 1.2)</p>
<dt>&quot;encrypted: boolean&quot;</p>
<dd>true if the backing device is encrypted</p>
<dt>&quot;encryption_key_missing: boolean&quot;</p>
<dd>Deprecated; always false</p>
<dt>&quot;detect_zeroes: BlockdevDetectZeroesOptions&quot;</p>
<dd>detect and optimize zero writes (Since 2.1)</p>
<dt>&quot;bps: int&quot;</p>
<dd>total throughput limit in bytes per second is specified</p>
<dt>&quot;bps_rd: int&quot;</p>
<dd>read throughput limit in bytes per second is specified</p>
<dt>&quot;bps_wr: int&quot;</p>
<dd>write throughput limit in bytes per second is specified</p>
<dt>&quot;iops: int&quot;</p>
<dd>total I/O operations per second is specified</p>
<dt>&quot;iops_rd: int&quot;</p>
<dd>read I/O operations per second is specified</p>
<dt>&quot;iops_wr: int&quot;</p>
<dd>write I/O operations per second is specified</p>
<dt>&quot;image: ImageInfo&quot;</p>
<dd>the info of image used (since: 1.6)</p>
<dt>&quot;bps_max: int&quot; (optional)</p>
<dd>total throughput limit during bursts, in bytes (Since 1.7)</p>
<dt>&quot;bps_rd_max: int&quot; (optional)</p>
<dd>read throughput limit during bursts, in bytes (Since 1.7)</p>
<dt>&quot;bps_wr_max: int&quot; (optional)</p>
<dd>write throughput limit during bursts, in bytes (Since 1.7)</p>
<dt>&quot;iops_max: int&quot; (optional)</p>
<dd>total I/O operations per second during bursts, in bytes (Since 1.7)</p>
<dt>&quot;iops_rd_max: int&quot; (optional)</p>
<dd>read I/O operations per second during bursts, in bytes (Since 1.7)</p>
<dt>&quot;iops_wr_max: int&quot; (optional)</p>
<dd>write I/O operations per second during bursts, in bytes (Since 1.7)</p>
<dt>&quot;bps_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;bps_max&quot;</tt> burst period, in seconds. (Since 2.6)</p>
<dt>&quot;bps_rd_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;bps_rd_max&quot;</tt> burst period, in seconds. (Since 2.6)</p>
<dt>&quot;bps_wr_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;bps_wr_max&quot;</tt> burst period, in seconds. (Since 2.6)</p>
<dt>&quot;iops_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;iops&quot;</tt> burst period, in seconds. (Since 2.6)</p>
<dt>&quot;iops_rd_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;iops_rd_max&quot;</tt> burst period, in seconds. (Since 2.6)</p>
<dt>&quot;iops_wr_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;iops_wr_max&quot;</tt> burst period, in seconds. (Since 2.6)</p>
<dt>&quot;iops_size: int&quot; (optional)</p>
<dd>an I/O size in bytes (Since 1.7)</p>
<dt>&quot;group: string&quot; (optional)</p>
<dd>throttle group name (Since 2.4)</p>
<dt>&quot;cache: BlockdevCacheInfo&quot;</p>
<dd>the cache mode used for the block device (since: 2.3)</p>
<dt>&quot;write_threshold: int&quot;</p>
<dd>configured write threshold for the device. 0 if disabled. (Since 2.3)</p>
<dt>&quot;dirty-bitmaps: array of BlockDirtyInfo&quot; (optional)</p>
<dd>dirty bitmaps information (only present if node has one or more dirty bitmaps) (Since 4.2)</dl>
<p> <code>Since:</code> 0.14.0 <code>BlockDeviceIoStatus</code> (Enum) An enumeration of block device I/O status. <code>Values:</code></p>
<dl>
<dt>&quot;ok&quot;</p>
<dd>The last I/O operation has succeeded</p>
<dt>&quot;failed&quot;</p>
<dd>The last I/O operation has failed</p>
<dt>&quot;nospace&quot;</p>
<dd>The last I/O operation has failed due to a no-space condition</dl>
<p> <code>Since:</code> 1.0 <code>BlockDeviceMapEntry</code> (Object) Entry in the metadata map of the device (returned by &#8220;qemu-img map&#8221;) <code>Members:</code></p>
<dl>
<dt>&quot;start: int&quot;</p>
<dd>Offset in the image of the first byte described by this entry (in bytes)</p>
<dt>&quot;length: int&quot;</p>
<dd>Length of the range described by this entry (in bytes)</p>
<dt>&quot;depth: int&quot;</p>
<dd>Number of layers (0 = top image, 1 = top image&#8217;s backing file, etc.) before reaching one for which the range is allocated. The value is in the range 0 to the depth of the image chain &#8211; 1.</p>
<dt>&quot;zero: boolean&quot;</p>
<dd>the sectors in this range read as zeros</p>
<dt>&quot;data: boolean&quot;</p>
<dd>reading the image will actually read data from a file (in particular, if <tt>&quot;offset&quot;</tt> is present this means that the sectors are not simply preallocated, but contain actual data in raw format)</p>
<dt>&quot;offset: int&quot; (optional)</p>
<dd>if present, the image file stores the data for this range in raw format at the given offset.</dl>
<p> <code>Since:</code> 1.7 <code>DirtyBitmapStatus</code> (Enum) An enumeration of possible states that a dirty bitmap can report to the user. <code>Values:</code></p>
<dl>
<dt>&quot;frozen&quot;</p>
<dd>The bitmap is currently in-use by some operation and is immutable. If the bitmap was <tt>&quot;active&quot;</tt> prior to the operation, new writes by the guest are being recorded in a temporary buffer, and will not be lost. Generally, bitmaps are cleared on successful use in an operation and the temporary buffer is committed into the bitmap. On failure, the temporary buffer is merged back into the bitmap without first clearing it. Please refer to the documentation for each bitmap-using operation, See also <tt>&quot;blockdev-backup&quot;</tt>, <tt>&quot;drive-backup&quot;</tt>.</p>
<dt>&quot;disabled&quot;</p>
<dd>The bitmap is not currently recording new writes by the guest. This is requested explicitly via <tt>&quot;block-dirty-bitmap-disable&quot;</tt>. It can still be cleared, deleted, or used for backup operations.</p>
<dt>&quot;active&quot;</p>
<dd>The bitmap is actively monitoring for new writes, and can be cleared, deleted, or used for backup operations.</p>
<dt>&quot;locked&quot;</p>
<dd>The bitmap is currently in-use by some operation and is immutable. If the bitmap was <tt>&quot;active&quot;</tt> prior to the operation, it is still recording new writes. If the bitmap was <tt>&quot;disabled&quot;</tt>, it is not recording new writes. (Since 2.12)</p>
<dt>&quot;inconsistent&quot;</p>
<dd>This is a persistent dirty bitmap that was marked in-use on disk, and is unusable by <font SIZE="-1">QEMU.</font> It can only be deleted. Please rely on the inconsistent field in <tt>&quot;BlockDirtyInfo&quot;</tt> instead, as the status field is deprecated. (Since 4.0)</dl>
<p> <code>Since:</code> 2.4 <code>BlockDirtyInfo</code> (Object) Block dirty bitmap information. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot; (optional)</p>
<dd>the name of the dirty bitmap (Since 2.4)</p>
<dt>&quot;count: int&quot;</p>
<dd>number of dirty bytes according to the dirty bitmap</p>
<dt>&quot;granularity: int&quot;</p>
<dd>granularity of the dirty bitmap in bytes (since 1.4)</p>
<dt>&quot;status: DirtyBitmapStatus&quot;</p>
<dd>Deprecated in favor of <tt>&quot;recording&quot;</tt> and <tt>&quot;locked&quot;</tt>. (since 2.4)</p>
<dt>&quot;recording: boolean&quot;</p>
<dd>true if the bitmap is recording new writes from the guest. Replaces `active` and `disabled` statuses. (since 4.0)</p>
<dt>&quot;busy: boolean&quot;</p>
<dd>true if the bitmap is in-use by some operation (<font SIZE="-1">NBD</font> or jobs) and cannot be modified via <font SIZE="-1">QMP</font> or used by another operation. Replaces `locked` and `frozen` statuses. (since 4.0)</p>
<dt>&quot;persistent: boolean&quot;</p>
<dd>true if the bitmap was stored on disk, is scheduled to be stored on disk, or both. (since 4.0)</p>
<dt>&quot;inconsistent: boolean&quot; (optional)</p>
<dd>true if this is a persistent bitmap that was improperly stored. Implies <tt>&quot;persistent&quot;</tt> to be true; <tt>&quot;recording&quot;</tt> and <tt>&quot;busy&quot;</tt> to be false. This bitmap cannot be used. To remove it, use <tt>&quot;block-dirty-bitmap-remove&quot;</tt>. (Since 4.0)</dl>
<p> <code>Since:</code> 1.3 <code>Qcow2BitmapInfoFlags</code> (Enum) An enumeration of flags that a bitmap can report to the user. <code>Values:</code></p>
<dl>
<dt>&quot;in-use&quot;</p>
<dd>This flag is set by any process actively modifying the qcow2 file, and cleared when the updated bitmap is flushed to the qcow2 image. The presence of this flag in an offline image means that the bitmap was not saved correctly after its last usage, and may contain inconsistent data.</p>
<dt>&quot;auto&quot;</p>
<dd>The bitmap must reflect all changes of the virtual disk by any application that would write to this qcow2 file.</dl>
<p> <code>Since:</code> 4.0 <code>Qcow2BitmapInfo</code> (Object) Qcow2 bitmap information. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>the name of the bitmap</p>
<dt>&quot;granularity: int&quot;</p>
<dd>granularity of the bitmap in bytes</p>
<dt>&quot;flags: array of Qcow2BitmapInfoFlags&quot;</p>
<dd>flags of the bitmap</dl>
<p> <code>Since:</code> 4.0 <code>BlockLatencyHistogramInfo</code> (Object) Block latency histogram. <code>Members:</code></p>
<dl>
<dt>&quot;boundaries: array of int&quot;</p>
<dd>list of interval boundary values in nanoseconds, all greater than zero and in ascending order. For example, the list [10, 50, 100] produces the following histogram intervals: [0, 10), [10, 50), [50, 100), [100, +inf).</p>
<dt>&quot;bins: array of int&quot;</p>
<dd>list of io request counts corresponding to histogram intervals. len(<tt>&quot;bins&quot;</tt>) = len(<tt>&quot;boundaries&quot;</tt>) + 1 For the example above, <tt>&quot;bins&quot;</tt> may be something like [3, 1, 5, 2], and corresponding histogram looks like: 5| * 4| * 3| 2| * 1| +&#8212;&#8212;&#8212;&#8212;&#8212;&#8212; 10 50 100</dl>
<p> <code>Since:</code> 4.0 <code>block-latency-histogram-set</code> (Command) Manage read, write and flush latency histograms for the device. If only <tt>&quot;id&quot;</tt> parameter is specified, remove all present latency histograms for the device. Otherwise, add/reset some of (or all) latency histograms. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The name or <font SIZE="-1">QOM</font> path of the guest device.</p>
<dt>&quot;boundaries: array of int&quot; (optional)</p>
<dd>list of interval boundary values (see description in BlockLatencyHistogramInfo definition). If specified, all latency histograms are removed, and empty ones created for all io types with intervals corresponding to <tt>&quot;boundaries&quot;</tt> (except for io types, for which specific boundaries are set through the following parameters).</p>
<dt>&quot;boundaries-read: array of int&quot; (optional)</p>
<dd>list of interval boundary values for read latency histogram. If specified, old read latency histogram is removed, and empty one created with intervals corresponding to <tt>&quot;boundaries-read&quot;</tt>. The parameter has higher priority then <tt>&quot;boundaries&quot;</tt>.</p>
<dt>&quot;boundaries-write: array of int&quot; (optional)</p>
<dd>list of interval boundary values for write latency histogram.</p>
<dt>&quot;boundaries-flush: array of int&quot; (optional)</p>
<dd>list of interval boundary values for flush latency histogram.</dl>
<p> <code>Returns:</code> error if device is not found or any boundary arrays are invalid. <code>Since:</code> 4.0 <code>Example:</code> set new histograms for all io types with intervals<br />
        [0, 10), [10, 50), [50, 100), [100, +inf):</p>
<p>        -&gt; { &quot;execute&quot;: &quot;block-latency-histogram-set&quot;,<br />
             &quot;arguments&quot;: { &quot;id&quot;: &quot;drive0&quot;,<br />
                            &quot;boundaries&quot;: [10, 50, 100] } }<br />
        &lt;- {<br />
    &quot;return&quot;:<br />
    {<br />
    } } <code>Example:</code> set new histogram only for write, other histograms will remain<br />
        not changed (or not created):</p>
<p>        -&gt; { &quot;execute&quot;: &quot;block-latency-histogram-set&quot;,<br />
             &quot;arguments&quot;: { &quot;id&quot;: &quot;drive0&quot;,<br />
                            &quot;boundaries-write&quot;: [10, 50, 100] } }<br />
        &lt;-<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>Example:</code> set new histograms with the following intervals:<br />
          read, flush: [0, 10), [10, 50), [50, 100), [100, +inf)<br />
          write: [0, 1000), [1000, 5000), [5000, +inf)</p>
<p>        -&gt; { &quot;execute&quot;: &quot;block-latency-histogram-set&quot;,<br />
             &quot;arguments&quot;: { &quot;id&quot;: &quot;drive0&quot;,<br />
                            &quot;boundaries&quot;: [10, 50, 100],<br />
                            &quot;boundaries-write&quot;: [1000, 5000] } }<br />
        &lt;- {<br />
    &quot;return&quot;:<br />
    {<br />
    } } <code>Example:</code> remove all latency histograms :</p>
<p>        -&gt;{&quot;execute&quot; : &quot;block-latency-histogram-set&quot;,<br />
           &quot;arguments&quot; : {&quot;id&quot; : &quot;drive0&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>BlockInfo</code> (Object) Block device information. This structure describes a virtual device and the backing device associated with it. <code>Members:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>The device name associated with the virtual device.</p>
<dt>&quot;qdev: string&quot; (optional)</p>
<dd>The qdev <font SIZE="-1">ID,</font> or if no <font SIZE="-1">ID</font> is assigned, the <font SIZE="-1">QOM</font> path of the block device. (since 2.10)</p>
<dt>&quot;type: string&quot;</p>
<dd>This field is returned only for compatibility reasons, it should not be used (always returns &#8216;unknown&#8217;)</p>
<dt>&quot;removable: boolean&quot;</p>
<dd>True if the device supports removable media.</p>
<dt>&quot;locked: boolean&quot;</p>
<dd>True if the guest has locked this device from having its media removed</p>
<dt>&quot;tray_open: boolean&quot; (optional)</p>
<dd>True if the device&#8217;s tray is open (only present if it has a tray)</p>
<dt>&quot;dirty-bitmaps: array of BlockDirtyInfo&quot; (optional)</p>
<dd>dirty bitmaps information (only present if the driver has one or more dirty bitmaps) (Since 2.0) Deprecated in 4.2; see BlockDeviceInfo instead.</p>
<dt>&quot;io-status: BlockDeviceIoStatus&quot; (optional)</p>
<dd><tt>&quot;BlockDeviceIoStatus&quot;</tt>. Only present if the device supports it and the <font SIZE="-1">VM</font> is configured to stop on errors (supported device models: virtio-blk, <font SIZE="-1">IDE, SCSI</font> except scsi-generic)</p>
<dt>&quot;inserted: BlockDeviceInfo&quot; (optional)</p>
<dd><tt>&quot;BlockDeviceInfo&quot;</tt> describing the device if media is present</dl>
<p> <code>Since:</code> 0.14.0 <code>BlockMeasureInfo</code> (Object) Image file size calculation information. This structure describes the size requirements for creating a new image file. The size requirements depend on the new image file format. File size always equals virtual disk size for the &#8216;raw&#8217; format, even for sparse <font SIZE="-1">POSIX</font> files. Compact formats such as &#8216;qcow2&#8217; represent unallocated and zero regions efficiently so file size may be smaller than virtual disk size. The values are upper bounds that are guaranteed to fit the new image file. Subsequent modification, such as internal snapshot or bitmap creation, may require additional space and is not covered here. <code>Members:</code></p>
<dl>
<dt>&quot;required: int&quot;</p>
<dd>Size required for a new image file, in bytes.</p>
<dt>&quot;fully-allocated: int&quot;</p>
<dd>Image file size, in bytes, once data has been written to all sectors.</dl>
<p> <code>Since:</code> 2.10 <code>query-block</code> (Command) Get a list of BlockInfo for all virtual block devices. <code>Returns:</code> a list of <tt>&quot;BlockInfo&quot;</tt> describing each virtual block device. Filter nodes that were created implicitly are skipped over. <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-block&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;io-status&quot; : &quot;ok&quot;,<br />
            &quot;device&quot; : &quot;ide0-hd0&quot;,<br />
            &quot;locked&quot; : false,<br />
            &quot;removable&quot; : false,<br />
            &quot;inserted&quot; : {<br />
                &quot;ro&quot; : false,<br />
                &quot;drv&quot; : &quot;qcow2&quot;,<br />
                &quot;encrypted&quot; : false,<br />
                &quot;file&quot; : &quot;disks/test.qcow2&quot;,<br />
                &quot;backing_file_depth&quot; : 1,<br />
                &quot;bps&quot; : 1000000,<br />
                &quot;bps_rd&quot; : 0,<br />
                &quot;bps_wr&quot; : 0,<br />
                &quot;iops&quot; : 1000000,<br />
                &quot;iops_rd&quot; : 0,<br />
                &quot;iops_wr&quot; : 0,<br />
                &quot;bps_max&quot; : 8000000,<br />
                &quot;bps_rd_max&quot; : 0,<br />
                &quot;bps_wr_max&quot; : 0,<br />
                &quot;iops_max&quot; : 0,<br />
                &quot;iops_rd_max&quot; : 0,<br />
                &quot;iops_wr_max&quot; : 0,<br />
                &quot;iops_size&quot; : 0,<br />
                &quot;detect_zeroes&quot; : &quot;on&quot;,<br />
                &quot;write_threshold&quot; : 0,<br />
                &quot;image&quot; : {<br />
                    &quot;filename&quot; : &quot;disks/test.qcow2&quot;,<br />
                    &quot;format&quot; : &quot;qcow2&quot;,<br />
                    &quot;virtual-size&quot; : 2048000,<br />
                    &quot;backing_file&quot; : &quot;base.qcow2&quot;,<br />
                    &quot;full-backing-filename&quot; : &quot;disks/base.qcow2&quot;,<br />
                    &quot;backing-filename-format&quot; : &quot;qcow2&quot;,<br />
                    &quot;snapshots&quot; : [<br />
                        {<br />
                            &quot;id&quot; : &quot;1&quot;,<br />
                            &quot;name&quot; : &quot;snapshot1&quot;,<br />
                            &quot;vm-state-size&quot; : 0,<br />
                            &quot;date-sec&quot; : 10000200,<br />
                            &quot;date-nsec&quot; : 12,<br />
                            &quot;vm-clock-sec&quot; : 206,<br />
                            &quot;vm-clock-nsec&quot; : 30<br />
                        }<br />
                    ],<br />
                    &quot;backing-image&quot; : {<br />
                        &quot;filename&quot; : &quot;disks/base.qcow2&quot;,<br />
                        &quot;format&quot; : &quot;qcow2&quot;,<br />
                        &quot;virtual-size&quot; : 2048000<br />
                    }<br />
                }<br />
            },<br />
            &quot;qdev&quot; : &quot;ide_disk&quot;,<br />
            &quot;type&quot; : &quot;unknown&quot;<br />
        },<br />
        {<br />
            &quot;io-status&quot; : &quot;ok&quot;,<br />
            &quot;device&quot; : &quot;ide1-cd0&quot;,<br />
            &quot;locked&quot; : false,<br />
            &quot;removable&quot; : true,<br />
            &quot;qdev&quot; : &quot;/machine/unattached/device[23]&quot;,<br />
            &quot;tray_open&quot; : false,<br />
            &quot;type&quot; : &quot;unknown&quot;<br />
        },<br />
        {<br />
            &quot;device&quot; : &quot;floppy0&quot;,<br />
            &quot;locked&quot; : false,<br />
            &quot;removable&quot; : true,<br />
            &quot;qdev&quot; : &quot;/machine/unattached/device[20]&quot;,<br />
            &quot;type&quot; : &quot;unknown&quot;<br />
        },<br />
        {<br />
            &quot;device&quot; : &quot;sd0&quot;,<br />
            &quot;locked&quot; : false,<br />
            &quot;removable&quot; : true,<br />
            &quot;type&quot; : &quot;unknown&quot;<br />
        }<br />
    ]<br />
} <code>BlockDeviceTimedStats</code> (Object) Statistics of a block device during a given interval of time. <code>Members:</code></p>
<dl>
<dt>&quot;interval_length: int&quot;</p>
<dd>Interval used for calculating the statistics, in seconds.</p>
<dt>&quot;min_rd_latency_ns: int&quot;</p>
<dd>Minimum latency of read operations in the defined interval, in nanoseconds.</p>
<dt>&quot;min_wr_latency_ns: int&quot;</p>
<dd>Minimum latency of write operations in the defined interval, in nanoseconds.</p>
<dt>&quot;min_flush_latency_ns: int&quot;</p>
<dd>Minimum latency of flush operations in the defined interval, in nanoseconds.</p>
<dt>&quot;max_rd_latency_ns: int&quot;</p>
<dd>Maximum latency of read operations in the defined interval, in nanoseconds.</p>
<dt>&quot;max_wr_latency_ns: int&quot;</p>
<dd>Maximum latency of write operations in the defined interval, in nanoseconds.</p>
<dt>&quot;max_flush_latency_ns: int&quot;</p>
<dd>Maximum latency of flush operations in the defined interval, in nanoseconds.</p>
<dt>&quot;avg_rd_latency_ns: int&quot;</p>
<dd>Average latency of read operations in the defined interval, in nanoseconds.</p>
<dt>&quot;avg_wr_latency_ns: int&quot;</p>
<dd>Average latency of write operations in the defined interval, in nanoseconds.</p>
<dt>&quot;avg_flush_latency_ns: int&quot;</p>
<dd>Average latency of flush operations in the defined interval, in nanoseconds.</p>
<dt>&quot;avg_rd_queue_depth: number&quot;</p>
<dd>Average number of pending read operations in the defined interval.</p>
<dt>&quot;avg_wr_queue_depth: number&quot;</p>
<dd>Average number of pending write operations in the defined interval.</dl>
<p> <code>Since:</code> 2.5 <code>BlockDeviceStats</code> (Object) Statistics of a virtual block device or a block backing device. <code>Members:</code></p>
<dl>
<dt>&quot;rd_bytes: int&quot;</p>
<dd>The number of bytes read by the device.</p>
<dt>&quot;wr_bytes: int&quot;</p>
<dd>The number of bytes written by the device.</p>
<dt>&quot;unmap_bytes: int&quot;</p>
<dd>The number of bytes unmapped by the device (Since 4.2)</p>
<dt>&quot;rd_operations: int&quot;</p>
<dd>The number of read operations performed by the device.</p>
<dt>&quot;wr_operations: int&quot;</p>
<dd>The number of write operations performed by the device.</p>
<dt>&quot;flush_operations: int&quot;</p>
<dd>The number of cache flush operations performed by the device (since 0.15.0)</p>
<dt>&quot;unmap_operations: int&quot;</p>
<dd>The number of unmap operations performed by the device (Since 4.2)</p>
<dt>&quot;rd_total_time_ns: int&quot;</p>
<dd>Total time spent on reads in nanoseconds (since 0.15.0).</p>
<dt>&quot;wr_total_time_ns: int&quot;</p>
<dd>Total time spent on writes in nanoseconds (since 0.15.0).</p>
<dt>&quot;flush_total_time_ns: int&quot;</p>
<dd>Total time spent on cache flushes in nanoseconds (since 0.15.0).</p>
<dt>&quot;unmap_total_time_ns: int&quot;</p>
<dd>Total time spent on unmap operations in nanoseconds (Since 4.2)</p>
<dt>&quot;wr_highest_offset: int&quot;</p>
<dd>The offset after the greatest byte written to the device. The intended use of this information is for growable sparse files (like qcow2) that are used on top of a physical device.</p>
<dt>&quot;rd_merged: int&quot;</p>
<dd>Number of read requests that have been merged into another request (Since 2.3).</p>
<dt>&quot;wr_merged: int&quot;</p>
<dd>Number of write requests that have been merged into another request (Since 2.3).</p>
<dt>&quot;unmap_merged: int&quot;</p>
<dd>Number of unmap requests that have been merged into another request (Since 4.2)</p>
<dt>&quot;idle_time_ns: int&quot; (optional)</p>
<dd>Time since the last I/O operation, in nanoseconds. If the field is absent it means that there haven&#8217;t been any operations yet (Since 2.5).</p>
<dt>&quot;failed_rd_operations: int&quot;</p>
<dd>The number of failed read operations performed by the device (Since 2.5)</p>
<dt>&quot;failed_wr_operations: int&quot;</p>
<dd>The number of failed write operations performed by the device (Since 2.5)</p>
<dt>&quot;failed_flush_operations: int&quot;</p>
<dd>The number of failed flush operations performed by the device (Since 2.5)</p>
<dt>&quot;failed_unmap_operations: int&quot;</p>
<dd>The number of failed unmap operations performed by the device (Since 4.2)</p>
<dt>&quot;invalid_rd_operations: int&quot;</p>
<dd>The number of invalid read operations performed by the device (Since 2.5)</p>
<dt>&quot;invalid_wr_operations: int&quot;</p>
<dd>The number of invalid write operations performed by the device (Since 2.5)</p>
<dt>&quot;invalid_flush_operations: int&quot;</p>
<dd>The number of invalid flush operations performed by the device (Since 2.5)</p>
<dt>&quot;invalid_unmap_operations: int&quot;</p>
<dd>The number of invalid unmap operations performed by the device (Since 4.2)</p>
<dt>&quot;account_invalid: boolean&quot;</p>
<dd>Whether invalid operations are included in the last access statistics (Since 2.5)</p>
<dt>&quot;account_failed: boolean&quot;</p>
<dd>Whether failed operations are included in the latency and last access statistics (Since 2.5)</p>
<dt>&quot;timed_stats: array of BlockDeviceTimedStats&quot;</p>
<dd>Statistics specific to the set of previously defined intervals of time (Since 2.5)</p>
<dt>&quot;rd_latency_histogram: BlockLatencyHistogramInfo&quot; (optional)</p>
<dd><tt>&quot;BlockLatencyHistogramInfo&quot;</tt>. (Since 4.0)</p>
<dt>&quot;wr_latency_histogram: BlockLatencyHistogramInfo&quot; (optional)</p>
<dd><tt>&quot;BlockLatencyHistogramInfo&quot;</tt>. (Since 4.0)</p>
<dt>&quot;flush_latency_histogram: BlockLatencyHistogramInfo&quot; (optional)</p>
<dd><tt>&quot;BlockLatencyHistogramInfo&quot;</tt>. (Since 4.0)</dl>
<p> <code>Since:</code> 0.14.0 <code>BlockStatsSpecificFile</code> (Object) File driver statistics <code>Members:</code></p>
<dl>
<dt>&quot;discard-nb-ok: int&quot;</p>
<dd>The number of successful discard operations performed by the driver.</p>
<dt>&quot;discard-nb-failed: int&quot;</p>
<dd>The number of failed discard operations performed by the driver.</p>
<dt>&quot;discard-bytes-ok: int&quot;</p>
<dd>The number of bytes discarded by the driver.</dl>
<p> <code>Since:</code> 4.2 <code>BlockStatsSpecific</code> (Object) Block driver specific statistics <code>Members:</code></p>
<dl>
<dt>&quot;driver: BlockdevDriver&quot;</p>
<dd>Not documented</p>
<dt>The members of &quot;BlockStatsSpecificFile&quot; when &quot;driver&quot; is &quot;file&quot;</p>
<dd>
<dt>The members of &quot;BlockStatsSpecificFile&quot; when &quot;driver&quot; is &quot;host_device&quot;</p>
<dd></dl>
<p> <code>Since:</code> 4.2 <code>BlockStats</code> (Object) Statistics of a virtual block device or a block backing device. <code>Members:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>If the stats are for a virtual block device, the name corresponding to the virtual block device.</p>
<dt>&quot;node-name: string&quot; (optional)</p>
<dd>The node name of the device. (Since 2.3)</p>
<dt>&quot;qdev: string&quot; (optional)</p>
<dd>The qdev <font SIZE="-1">ID,</font> or if no <font SIZE="-1">ID</font> is assigned, the <font SIZE="-1">QOM</font> path of the block device. (since 3.0)</p>
<dt>&quot;stats: BlockDeviceStats&quot;</p>
<dd>A <tt>&quot;BlockDeviceStats&quot;</tt> for the device.</p>
<dt>&quot;driver-specific: BlockStatsSpecific&quot; (optional)</p>
<dd>Optional driver-specific stats. (Since 4.2)</p>
<dt>&quot;parent: BlockStats&quot; (optional)</p>
<dd>This describes the file block device if it has one. Contains recursively the statistics of the underlying protocol (e.g. the host file for a qcow2 image). If there is no underlying protocol, this field is omitted</p>
<dt>&quot;backing: BlockStats&quot; (optional)</p>
<dd>This describes the backing block device if it has one. (Since 2.0)</dl>
<p> <code>Since:</code> 0.14.0 <code>query-blockstats</code> (Command) Query the <tt>&quot;BlockStats&quot;</tt> for all virtual block devices. <code>Arguments:</code></p>
<dl>
<dt>&quot;query-nodes: boolean&quot; (optional)</p>
<dd>If true, the command will query all the block nodes that have a node name, in a list which will include &#8220;parent&#8221; information, but not &#8220;backing&#8221;. If false or omitted, the behavior is as before &#8211; query all the device backends, recursively including their &#8220;parent&#8221; and &#8220;backing&#8221;. Filter nodes that were created implicitly are skipped over in this mode. (Since 2.3)</dl>
<p> <code>Returns:</code> A list of <tt>&quot;BlockStats&quot;</tt> for each virtual block devices. <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-blockstats&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;device&quot; : &quot;ide0-hd0&quot;,<br />
            &quot;parent&quot; : {<br />
                &quot;stats&quot; : {<br />
                    &quot;wr_highest_offset&quot; : 3686448128,<br />
                    &quot;wr_bytes&quot; : 9786368,<br />
                    &quot;wr_operations&quot; : 751,<br />
                    &quot;rd_bytes&quot; : 122567168,<br />
                    &quot;rd_operations&quot; : 36772 &quot;wr_total_times_ns&quot; : 313253456 &quot;rd_total_times_ns&quot; : 3465673657 &quot;flush_total_times_ns&quot; : 49653 &quot;flush_operations&quot; : 61,<br />
                    &quot;rd_merged&quot; : 0,<br />
                    &quot;wr_merged&quot; : 0,<br />
                    &quot;idle_time_ns&quot; : 2953431879,<br />
                    &quot;account_invalid&quot; : true,<br />
                    &quot;account_failed&quot; : false<br />
                }<br />
            },<br />
            &quot;stats&quot; : {<br />
                &quot;wr_highest_offset&quot; : 2821110784,<br />
                &quot;wr_bytes&quot; : 9786368,<br />
                &quot;wr_operations&quot; : 692,<br />
                &quot;rd_bytes&quot; : 122739200,<br />
                &quot;rd_operations&quot; : 36604 &quot;flush_operations&quot; : 51,<br />
                &quot;wr_total_times_ns&quot; : 313253456 &quot;rd_total_times_ns&quot; : 3465673657 &quot;flush_total_times_ns&quot; : 49653,<br />
                &quot;rd_merged&quot; : 0,<br />
                &quot;wr_merged&quot; : 0,<br />
                &quot;idle_time_ns&quot; : 2953431879,<br />
                &quot;account_invalid&quot; : true,<br />
                &quot;account_failed&quot; : false<br />
            },<br />
            &quot;qdev&quot; : &quot;/machine/unattached/device[23]&quot;<br />
        },<br />
        {<br />
            &quot;device&quot; : &quot;ide1-cd0&quot;,<br />
            &quot;stats&quot; : {<br />
                &quot;wr_highest_offset&quot; : 0,<br />
                &quot;wr_bytes&quot; : 0,<br />
                &quot;wr_operations&quot; : 0,<br />
                &quot;rd_bytes&quot; : 0,<br />
                &quot;rd_operations&quot; : 0 &quot;flush_operations&quot; : 0,<br />
                &quot;wr_total_times_ns&quot; : 0 &quot;rd_total_times_ns&quot; : 0 &quot;flush_total_times_ns&quot; : 0,<br />
                &quot;rd_merged&quot; : 0,<br />
                &quot;wr_merged&quot; : 0,<br />
                &quot;account_invalid&quot; : false,<br />
                &quot;account_failed&quot; : false<br />
            },<br />
            &quot;qdev&quot; : &quot;/machine/unattached/device[24]&quot;<br />
        },<br />
        {<br />
            &quot;device&quot; : &quot;floppy0&quot;,<br />
            &quot;stats&quot; : {<br />
                &quot;wr_highest_offset&quot; : 0,<br />
                &quot;wr_bytes&quot; : 0,<br />
                &quot;wr_operations&quot; : 0,<br />
                &quot;rd_bytes&quot; : 0,<br />
                &quot;rd_operations&quot; : 0 &quot;flush_operations&quot; : 0,<br />
                &quot;wr_total_times_ns&quot; : 0 &quot;rd_total_times_ns&quot; : 0 &quot;flush_total_times_ns&quot; : 0,<br />
                &quot;rd_merged&quot; : 0,<br />
                &quot;wr_merged&quot; : 0,<br />
                &quot;account_invalid&quot; : false,<br />
                &quot;account_failed&quot; : false<br />
            },<br />
            &quot;qdev&quot; : &quot;/machine/unattached/device[16]&quot;<br />
        },<br />
        {<br />
            &quot;device&quot; : &quot;sd0&quot;,<br />
            &quot;stats&quot; : {<br />
                &quot;wr_highest_offset&quot; : 0,<br />
                &quot;wr_bytes&quot; : 0,<br />
                &quot;wr_operations&quot; : 0,<br />
                &quot;rd_bytes&quot; : 0,<br />
                &quot;rd_operations&quot; : 0 &quot;flush_operations&quot; : 0,<br />
                &quot;wr_total_times_ns&quot; : 0 &quot;rd_total_times_ns&quot; : 0 &quot;flush_total_times_ns&quot; : 0,<br />
                &quot;rd_merged&quot; : 0,<br />
                &quot;wr_merged&quot; : 0,<br />
                &quot;account_invalid&quot; : false,<br />
                &quot;account_failed&quot; : false<br />
            }<br />
        }<br />
    ]<br />
} <code>BlockdevOnError</code> (Enum) An enumeration of possible behaviors for errors on I/O operations. The exact meaning depends on whether the I/O was initiated by a guest or by a block job <code>Values:</code></p>
<dl>
<dt>&quot;report&quot;</p>
<dd>for guest operations, report the error to the guest; for jobs, cancel the job</p>
<dt>&quot;ignore&quot;</p>
<dd>ignore the error, only report a <font SIZE="-1">QMP</font> event (<font SIZE="-1">BLOCK_IO_ERROR</font> or <font SIZE="-1">BLOCK_JOB_ERROR</font>)</p>
<dt>&quot;enospc&quot;</p>
<dd>same as <tt>&quot;stop&quot;</tt> on <font SIZE="-1">ENOSPC,</font> same as <tt>&quot;report&quot;</tt> otherwise.</p>
<dt>&quot;stop&quot;</p>
<dd>for guest operations, stop the virtual machine; for jobs, pause the job</p>
<dt>&quot;auto&quot;</p>
<dd>inherit the error handling policy of the backend (since: 2.7)</dl>
<p> <code>Since:</code> 1.3 <code>MirrorSyncMode</code> (Enum) An enumeration of possible behaviors for the initial synchronization phase of storage mirroring. <code>Values:</code></p>
<dl>
<dt>&quot;top&quot;</p>
<dd>copies data in the topmost image to the destination</p>
<dt>&quot;full&quot;</p>
<dd>copies data from all images to the destination</p>
<dt>&quot;none&quot;</p>
<dd>only copy data written from now on</p>
<dt>&quot;incremental&quot;</p>
<dd>only copy data described by the dirty bitmap. (since: 2.4)</p>
<dt>&quot;bitmap&quot;</p>
<dd>only copy data described by the dirty bitmap. (since: 4.2) Behavior on completion is determined by the BitmapSyncMode.</dl>
<p> <code>Since:</code> 1.3 <code>BitmapSyncMode</code> (Enum) An enumeration of possible behaviors for the synchronization of a bitmap when used for data copy operations. <code>Values:</code></p>
<dl>
<dt>&quot;on-success&quot;</p>
<dd>The bitmap is only synced when the operation is successful. This is the behavior always used for &#8216;<font SIZE="-1">INCREMENTAL</font>&#8216; backups.</p>
<dt>&quot;never&quot;</p>
<dd>The bitmap is never synchronized with the operation, and is treated solely as a read-only manifest of blocks to copy.</p>
<dt>&quot;always&quot;</p>
<dd>The bitmap is always synchronized with the operation, regardless of whether or not the operation was successful.</dl>
<p> <code>Since:</code> 4.2 <code>MirrorCopyMode</code> (Enum) An enumeration whose values tell the mirror block job when to trigger writes to the target. <code>Values:</code></p>
<dl>
<dt>&quot;background&quot;</p>
<dd>copy data in background only.</p>
<dt>&quot;write-blocking&quot;</p>
<dd>when data is written to the source, write it (synchronously) to the target as well. In addition, data is copied in background just like in <tt>&quot;background&quot;</tt> mode.</dl>
<p> <code>Since:</code> 3.0 <code>BlockJobInfo</code> (Object) Information about a long-running block device operation. <code>Members:</code></p>
<dl>
<dt>&quot;type: string&quot;</p>
<dd>the job type (&#8216;stream&#8217; for image streaming)</p>
<dt>&quot;device: string&quot;</p>
<dd>The job identifier. Originally the device name but other values are allowed since <font SIZE="-1">QEMU 2.7</font></p>
<dt>&quot;len: int&quot;</p>
<dd>Estimated <tt>&quot;offset&quot;</tt> value at the completion of the job. This value can arbitrarily change while the job is running, in both directions.</p>
<dt>&quot;offset: int&quot;</p>
<dd>Progress made until now. The unit is arbitrary and the value can only meaningfully be used for the ratio of <tt>&quot;offset&quot;</tt> to <tt>&quot;len&quot;</tt>. The value is monotonically increasing.</p>
<dt>&quot;busy: boolean&quot;</p>
<dd>false if the job is known to be in a quiescent state, with no pending I/O. Since 1.3.</p>
<dt>&quot;paused: boolean&quot;</p>
<dd>whether the job is paused or, if <tt>&quot;busy&quot;</tt> is true, will pause itself as soon as possible. Since 1.3.</p>
<dt>&quot;speed: int&quot;</p>
<dd>the rate limit, bytes per second</p>
<dt>&quot;io-status: BlockDeviceIoStatus&quot;</p>
<dd>the status of the job (since 1.3)</p>
<dt>&quot;ready: boolean&quot;</p>
<dd>true if the job may be completed (since 2.2)</p>
<dt>&quot;status: JobStatus&quot;</p>
<dd>Current job state/status (since 2.12)</p>
<dt>&quot;auto-finalize: boolean&quot;</p>
<dd>Job will finalize itself when <font SIZE="-1">PENDING,</font> moving to the <font SIZE="-1">CONCLUDED</font> state. (since 2.12)</p>
<dt>&quot;auto-dismiss: boolean&quot;</p>
<dd>Job will dismiss itself when <font SIZE="-1">CONCLUDED,</font> moving to the <font SIZE="-1">NULL</font> state and disappearing from the query list. (since 2.12)</p>
<dt>&quot;error: string&quot; (optional)</p>
<dd>Error information if the job did not complete successfully. Not set if the job completed successfully. (since 2.12.1)</dl>
<p> <code>Since:</code> 1.1 <code>query-block-jobs</code> (Command) Return information about long-running block device operations. <code>Returns:</code> a list of <tt>&quot;BlockJobInfo&quot;</tt> for each active block job <code>Since:</code> 1.1 <code>block_passwd</code> (Command) This command sets the password of a block device that has not been open with a password and requires one. This command is now obsolete and will always return an error since 2.10 <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;node-name: string&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;password: string&quot;</p>
<dd>Not documented</dl>
<p> <code>block_resize</code> (Command) Resize a block image while a guest is running. Either <tt>&quot;device&quot;</tt> or <tt>&quot;node-name&quot;</tt> must be set but not both. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>the name of the device to get the image resized</p>
<dt>&quot;node-name: string&quot; (optional)</p>
<dd>graph node name to get the image resized (Since 2.0)</p>
<dt>&quot;size: int&quot;</p>
<dd>new image size in bytes</dl>
<p> <code>Returns:</code> nothing on success If <tt>&quot;device&quot;</tt> is not a valid block device, DeviceNotFound <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block_resize&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;scratch&quot;, &quot;size&quot; : 1073741824}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>NewImageMode</code> (Enum) An enumeration that tells <font SIZE="-1">QEMU</font> how to set the backing file path in a new image file. <code>Values:</code></p>
<dl>
<dt>&quot;existing&quot;</p>
<dd><font SIZE="-1">QEMU</font> should look for an existing image file.</p>
<dt>&quot;absolute-paths&quot;</p>
<dd><font SIZE="-1">QEMU</font> should create a new image with absolute paths for the backing file. If there is no backing file available, the new image will not be backed either.</dl>
<p> <code>Since:</code> 1.1 <code>BlockdevSnapshotSync</code> (Object) Either <tt>&quot;device&quot;</tt> or <tt>&quot;node-name&quot;</tt> must be set but not both. <code>Members:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>the name of the device to take a snapshot of.</p>
<dt>&quot;node-name: string&quot; (optional)</p>
<dd>graph node name to generate the snapshot from (Since 2.0)</p>
<dt>&quot;snapshot-file: string&quot;</p>
<dd>the target of the new overlay image. If the file exists, or if it is a device, the overlay will be created in the existing file/device. Otherwise, a new file will be created.</p>
<dt>&quot;snapshot-node-name: string&quot; (optional)</p>
<dd>the graph node name of the new image (Since 2.0)</p>
<dt>&quot;format: string&quot; (optional)</p>
<dd>the format of the overlay image, default is &#8216;qcow2&#8217;.</p>
<dt>&quot;mode: NewImageMode&quot; (optional)</p>
<dd>whether and how <font SIZE="-1">QEMU</font> should create a new image, default is &#8216;absolute-paths&#8217;.</dl>
<p> <code>BlockdevSnapshot</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;node: string&quot;</p>
<dd>device or node name that will have a snapshot taken.</p>
<dt>&quot;overlay: string&quot;</p>
<dd>reference to the existing block device that will become the overlay of <tt>&quot;node&quot;</tt>, as part of taking the snapshot. It must not have a current backing file (this can be achieved by passing &#8220;backing&#8221;: null to blockdev-add).</dl>
<p> <code>Since:</code> 2.5 <code>BackupCommon</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;job-id: string&quot; (optional)</p>
<dd>identifier for the newly-created block job. If omitted, the device name will be used. (Since 2.7)</p>
<dt>&quot;device: string&quot;</p>
<dd>the device name or node-name of a root node which should be copied.</p>
<dt>&quot;sync: MirrorSyncMode&quot;</p>
<dd>what parts of the disk image should be copied to the destination (all the disk, only the sectors allocated in the topmost image, from a dirty bitmap, or only new I/O).</p>
<dt>&quot;speed: int&quot; (optional)</p>
<dd>the maximum speed, in bytes per second. The default is 0, for unlimited.</p>
<dt>&quot;bitmap: string&quot; (optional)</p>
<dd>The name of a dirty bitmap to use. Must be present if sync is &#8220;bitmap&#8221; or &#8220;incremental&#8221;. Can be present if sync is &#8220;full&#8221; or &#8220;top&#8221;. Must not be present otherwise. (Since 2.4 (drive-backup), 3.1 (blockdev-backup))</p>
<dt>&quot;bitmap-mode: BitmapSyncMode&quot; (optional)</p>
<dd>Specifies the type of data the bitmap should contain after the operation concludes. Must be present if a bitmap was provided, Must <font SIZE="-1">NOT</font> be present otherwise. (Since 4.2)</p>
<dt>&quot;compress: boolean&quot; (optional)</p>
<dd>true to compress data, if the target format supports it. (default: false) (since 2.8)</p>
<dt>&quot;on-source-error: BlockdevOnError&quot; (optional)</p>
<dd>the action to take on an error on the source, default &#8216;report&#8217;. &#8216;stop&#8217; and &#8216;enospc&#8217; can only be used if the block device supports io-status (see BlockInfo).</p>
<dt>&quot;on-target-error: BlockdevOnError&quot; (optional)</p>
<dd>the action to take on an error on the target, default &#8216;report&#8217; (no limitations, since this applies to a different block device than <tt>&quot;device&quot;</tt>).</p>
<dt>&quot;auto-finalize: boolean&quot; (optional)</p>
<dd>When false, this job will wait in a <font SIZE="-1">PENDING</font> state after it has finished its work, waiting for <tt>&quot;block-job-finalize&quot;</tt> before making any block graph changes. When true, this job will automatically perform its abort or commit actions. Defaults to true. (Since 2.12)</p>
<dt>&quot;auto-dismiss: boolean&quot; (optional)</p>
<dd>When false, this job will wait in a <font SIZE="-1">CONCLUDED</font> state after it has completely ceased all work, and awaits <tt>&quot;block-job-dismiss&quot;</tt>. When true, this job will automatically disappear from the query list without user intervention. Defaults to true. (Since 2.12)</p>
<dt>&quot;filter-node-name: string&quot; (optional)</p>
<dd>the node name that should be assigned to the filter driver that the backup job inserts into the graph above node specified by <tt>&quot;drive&quot;</tt>. If this option is not given, a node name is autogenerated. (Since: 4.2)</dl>
<p> <code>Note:</code> <tt>&quot;on-source-error&quot;</tt> and <tt>&quot;on-target-error&quot;</tt> only affect background I/O. If an error occurs during a guest write request, the device&#8217;s rerror/werror actions will be used. <code>Since:</code> 4.2 <code>DriveBackup</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;target: string&quot;</p>
<dd>the target of the new image. If the file exists, or if it is a device, the existing file/device will be used as the new destination. If it does not exist, a new file will be created.</p>
<dt>&quot;format: string&quot; (optional)</p>
<dd>the format of the new destination, default is to probe if <tt>&quot;mode&quot;</tt> is &#8216;existing&#8217;, else the format of the source</p>
<dt>&quot;mode: NewImageMode&quot; (optional)</p>
<dd>whether and how <font SIZE="-1">QEMU</font> should create a new image, default is &#8216;absolute-paths&#8217;.</p>
<dt>The members of &quot;BackupCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.6 <code>BlockdevBackup</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;target: string&quot;</p>
<dd>the device name or node-name of the backup target node.</p>
<dt>The members of &quot;BackupCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.3 <code>blockdev-snapshot-sync</code> (Command) Takes a synchronous snapshot of a block device. For the arguments, see the documentation of BlockdevSnapshotSync. <code>Returns:</code> nothing on success If <tt>&quot;device&quot;</tt> is not a valid block device, DeviceNotFound <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-snapshot-sync&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;ide-hd0&quot;,<br />
                  &quot;snapshot-file&quot; :<br />
                      &quot;/some/place/my-image&quot;,<br />
                  &quot;format&quot; : &quot;qcow2&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>blockdev-snapshot</code> (Command) Takes a snapshot of a block device. Take a snapshot, by installing &#8216;node&#8217; as the backing image of &#8216;overlay&#8217;. Additionally, if &#8216;node&#8217; is associated with a block device, the block device changes to using &#8216;overlay&#8217; as its new active image. For the arguments, see the documentation of BlockdevSnapshot. <code>Since:</code> 2.5 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-add&quot;,<br />
   &quot;arguments&quot; : {&quot;driver&quot; : &quot;qcow2&quot;,<br />
                  &quot;node-name&quot; : &quot;node1534&quot;,<br />
                  &quot;file&quot; : {&quot;driver&quot; : &quot;file&quot;,<br />
                            &quot;filename&quot; : &quot;hd1.qcow2&quot;},<br />
                  &quot;backing&quot; : null}}</p>
<p>    &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
    }</p>
<p>        -&gt; {&quot;execute&quot; : &quot;blockdev-snapshot&quot;,<br />
            &quot;arguments&quot; : {&quot;node&quot; : &quot;ide-hd0&quot;,<br />
                           &quot;overlay&quot; : &quot;node1534&quot;}} &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
    } <code>change-backing-file</code> (Command) Change the backing file in the image file metadata. This does not cause <font SIZE="-1">QEMU</font> to reopen the image file to reparse the backing filename (it may, however, perform a reopen to change permissions from r/o -&gt; r/w -&gt; r/o, if needed). The new backing file string is written into the image file metadata, and the <font SIZE="-1">QEMU</font> internal strings are updated. <code>Arguments:</code></p>
<dl>
<dt>&quot;image-node-name: string&quot;</p>
<dd>The name of the block driver state node of the image to modify. The &#8220;device&#8221; argument is used to verify &#8220;image-node-name&#8221; is in the chain described by &#8220;device&#8221;.</p>
<dt>&quot;device: string&quot;</p>
<dd>The device name or node-name of the root node that owns image-node-name.</p>
<dt>&quot;backing-file: string&quot;</p>
<dd>The string to write as the backing file. This string is not validated, so care should be taken when specifying the string or the image chain may not be able to be reopened again.</dl>
<p> <code>Returns:</code> Nothing on success If &#8220;device&#8221; does not exist or cannot be determined, DeviceNotFound <code>Since:</code> 2.1 <code>block-commit</code> (Command) Live commit of data from overlay image nodes into backing nodes &#8211; i.e., writes data between &#8216;top&#8217; and &#8216;base&#8217; into &#8216;base&#8217;. <code>Arguments:</code></p>
<dl>
<dt>&quot;job-id: string&quot; (optional)</p>
<dd>identifier for the newly-created block job. If omitted, the device name will be used. (Since 2.7)</p>
<dt>&quot;device: string&quot;</p>
<dd>the device name or node-name of a root node</p>
<dt>&quot;base-node: string&quot; (optional)</p>
<dd>The node name of the backing image to write data into. If not specified, this is the deepest backing image. (since: 3.1)</p>
<dt>&quot;base: string&quot; (optional)</p>
<dd>Same as <tt>&quot;base-node&quot;</tt>, except that it is a file name rather than a node name. This must be the exact filename string that was used to open the node; other strings, even if addressing the same file, are not accepted (deprecated, use <tt>&quot;base-node&quot;</tt> instead)</p>
<dt>&quot;top-node: string&quot; (optional)</p>
<dd>The node name of the backing image within the image chain which contains the topmost data to be committed down. If not specified, this is the active layer. (since: 3.1)</p>
<dt>&quot;top: string&quot; (optional)</p>
<dd>Same as <tt>&quot;top-node&quot;</tt>, except that it is a file name rather than a node name. This must be the exact filename string that was used to open the node; other strings, even if addressing the same file, are not accepted (deprecated, use <tt>&quot;base-node&quot;</tt> instead)</p>
<dt>&quot;backing-file: string&quot; (optional)</p>
<dd>The backing file string to write into the overlay image of &#8216;top&#8217;. If &#8216;top&#8217; is the active layer, specifying a backing file string is an error. This filename is not validated. If a pathname string is such that it cannot be resolved by <font SIZE="-1">QEMU,</font> that means that subsequent <font SIZE="-1">QMP</font> or <font SIZE="-1">HMP</font> commands must use node-names for the image in question, as filename lookup methods will fail. If not specified, <font SIZE="-1">QEMU</font> will automatically determine the backing file string to use, or error out if there is no obvious choice. Care should be taken when specifying the string, to specify a valid filename or protocol. (Since 2.1) If top == base, that is an error. If top == active, the job will not be completed by itself, user needs to complete the job with the block-job-complete command after getting the ready event. (Since 2.0) If the base image is smaller than top, then the base image will be resized to be the same size as top. If top is smaller than the base image, the base will not be truncated. If you want the base image size to match the size of the smaller top, you can safely truncate it yourself once the commit operation successfully completes.</p>
<dt>&quot;speed: int&quot; (optional)</p>
<dd>the maximum speed, in bytes per second</p>
<dt>&quot;filter-node-name: string&quot; (optional)</p>
<dd>the node name that should be assigned to the filter driver that the commit job inserts into the graph above <tt>&quot;top&quot;</tt>. If this option is not given, a node name is autogenerated. (Since: 2.9)</p>
<dt>&quot;auto-finalize: boolean&quot; (optional)</p>
<dd>When false, this job will wait in a <font SIZE="-1">PENDING</font> state after it has finished its work, waiting for <tt>&quot;block-job-finalize&quot;</tt> before making any block graph changes. When true, this job will automatically perform its abort or commit actions. Defaults to true. (Since 3.1)</p>
<dt>&quot;auto-dismiss: boolean&quot; (optional)</p>
<dd>When false, this job will wait in a <font SIZE="-1">CONCLUDED</font> state after it has completely ceased all work, and awaits <tt>&quot;block-job-dismiss&quot;</tt>. When true, this job will automatically disappear from the query list without user intervention. Defaults to true. (Since 3.1)</dl>
<p> <code>Returns:</code> Nothing on success If <tt>&quot;device&quot;</tt> does not exist, DeviceNotFound Any other error returns a GenericError. <code>Since:</code> 1.3 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block-commit&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;virtio0&quot;,<br />
                  &quot;top&quot; : &quot;/tmp/snap1.qcow2&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>drive-backup</code> (Command) Start a point-in-time copy of a block device to a new destination. The status of ongoing drive-backup operations can be checked with query-block-jobs where the BlockJobInfo.type field has the value &#8216;backup&#8217;. The operation can be stopped before it has completed using the block-job-cancel command. <code>Arguments:</code> the members of <tt>&quot;DriveBackup&quot;</tt> <code>Returns:</code> nothing on success If <tt>&quot;device&quot;</tt> is not a valid block device, GenericError <code>Since:</code> 1.6 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;drive-backup&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;drive0&quot;,<br />
                  &quot;sync&quot; : &quot;full&quot;,<br />
                  &quot;target&quot; : &quot;backup.img&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>blockdev-backup</code> (Command) Start a point-in-time copy of a block device to a new destination. The status of ongoing blockdev-backup operations can be checked with query-block-jobs where the BlockJobInfo.type field has the value &#8216;backup&#8217;. The operation can be stopped before it has completed using the block-job-cancel command. <code>Arguments:</code> the members of <tt>&quot;BlockdevBackup&quot;</tt> <code>Returns:</code> nothing on success If <tt>&quot;device&quot;</tt> is not a valid block device, DeviceNotFound <code>Since:</code> 2.3 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-backup&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;src-id&quot;,<br />
                  &quot;sync&quot; : &quot;full&quot;,<br />
                  &quot;target&quot; : &quot;tgt-id&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>query-named-block-nodes</code> (Command) Get the named block driver list <code>Returns:</code> the list of BlockDeviceInfo <code>Since:</code> 2.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-named-block-nodes&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [ {&quot;ro&quot; : false,<br />
                  &quot;drv&quot; : &quot;qcow2&quot;,<br />
                  &quot;encrypted&quot; : false,<br />
                  &quot;file&quot; : &quot;disks/test.qcow2&quot;,<br />
                  &quot;node-name&quot; : &quot;my-node&quot;,<br />
                  &quot;backing_file_depth&quot; : 1,<br />
                  &quot;bps&quot; : 1000000,<br />
                  &quot;bps_rd&quot; : 0,<br />
                  &quot;bps_wr&quot; : 0,<br />
                  &quot;iops&quot; : 1000000,<br />
                  &quot;iops_rd&quot; : 0,<br />
                  &quot;iops_wr&quot; : 0,<br />
                  &quot;bps_max&quot; : 8000000,<br />
                  &quot;bps_rd_max&quot; : 0,<br />
                  &quot;bps_wr_max&quot; : 0,<br />
                  &quot;iops_max&quot; : 0,<br />
                  &quot;iops_rd_max&quot; : 0,<br />
                  &quot;iops_wr_max&quot; : 0,<br />
                  &quot;iops_size&quot; : 0,<br />
                  &quot;write_threshold&quot; : 0,<br />
                  &quot;image&quot; : {<br />
                      &quot;filename&quot; : &quot;disks/test.qcow2&quot;,<br />
                      &quot;format&quot; : &quot;qcow2&quot;,<br />
                      &quot;virtual-size&quot; : 2048000,<br />
                      &quot;backing_file&quot; : &quot;base.qcow2&quot;,<br />
                      &quot;full-backing-filename&quot; : &quot;disks/base.qcow2&quot;,<br />
                      &quot;backing-filename-format&quot; : &quot;qcow2&quot;,<br />
                      &quot;snapshots&quot; : [<br />
                          {<br />
                              &quot;id&quot; : &quot;1&quot;,<br />
                              &quot;name&quot; : &quot;snapshot1&quot;,<br />
                              &quot;vm-state-size&quot; : 0,<br />
                              &quot;date-sec&quot; : 10000200,<br />
                              &quot;date-nsec&quot; : 12,<br />
                              &quot;vm-clock-sec&quot; : 206,<br />
                              &quot;vm-clock-nsec&quot; : 30<br />
                          }<br />
                      ],<br />
                      &quot;backing-image&quot; : {<br />
                          &quot;filename&quot; : &quot;disks/base.qcow2&quot;,<br />
                          &quot;format&quot; : &quot;qcow2&quot;,<br />
                          &quot;virtual-size&quot; : 2048000<br />
                      }<br />
                  }} ]<br />
} <code>XDbgBlockGraphNodeType</code> (Enum) <code>Values:</code></p>
<dl>
<dt>&quot;block-backend&quot;</p>
<dd>corresponds to BlockBackend</p>
<dt>&quot;block-job&quot;</p>
<dd>corresonds to BlockJob</p>
<dt>&quot;block-driver&quot;</p>
<dd>corresponds to BlockDriverState</dl>
<p> <code>Since:</code> 4.0 <code>XDbgBlockGraphNode</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;id: int&quot;</p>
<dd>Block graph node identifier. This <tt>&quot;id&quot;</tt> is generated only for x-debug-query-block-graph and does not relate to any other identifiers in Qemu.</p>
<dt>&quot;type: XDbgBlockGraphNodeType&quot;</p>
<dd>Type of graph node. Can be one of block-backend, block-job or block-driver-state.</p>
<dt>&quot;name: string&quot;</p>
<dd>Human readable name of the node. Corresponds to node-name for block-driver-state nodes; is not guaranteed to be unique in the whole graph (with block-jobs and block-backends).</dl>
<p> <code>Since:</code> 4.0 <code>BlockPermission</code> (Enum) Enum of base block permissions. <code>Values:</code></p>
<dl>
<dt>&quot;consistent-read&quot;</p>
<dd>A user that has the &#8220;permission&#8221; of consistent reads is guaranteed that their view of the contents of the block device is complete and self-consistent, representing the contents of a disk at a specific point. For most block devices (including their backing files) this is true, but the property cannot be maintained in a few situations like for intermediate nodes of a commit block job.</p>
<dt>&quot;write&quot;</p>
<dd>This permission is required to change the visible disk contents.</p>
<dt>&quot;write-unchanged&quot;</p>
<dd>This permission (which is weaker than <font SIZE="-1">BLK_PERM_WRITE</font>) is both enough and required for writes to the block node when the caller promises that the visible disk content doesn&#8217;t change. As the <font SIZE="-1">BLK_PERM_WRITE</font> permission is strictly stronger, either is sufficient to perform an unchanging write.</p>
<dt>&quot;resize&quot;</p>
<dd>This permission is required to change the size of a block node.</p>
<dt>&quot;graph-mod&quot;</p>
<dd>This permission is required to change the node that this BdrvChild points to.</dl>
<p> <code>Since:</code> 4.0 <code>XDbgBlockGraphEdge</code> (Object) Block Graph edge description for x-debug-query-block-graph. <code>Members:</code></p>
<dl>
<dt>&quot;parent: int&quot;</p>
<dd>parent id</p>
<dt>&quot;child: int&quot;</p>
<dd>child id</p>
<dt>&quot;name: string&quot;</p>
<dd>name of the relation (examples are &#8216;file&#8217; and &#8216;backing&#8217;)</p>
<dt>&quot;perm: array of BlockPermission&quot;</p>
<dd>granted permissions for the parent operating on the child</p>
<dt>&quot;shared-perm: array of BlockPermission&quot;</p>
<dd>permissions that can still be granted to other users of the child while it is still attached to this parent</dl>
<p> <code>Since:</code> 4.0 <code>XDbgBlockGraph</code> (Object) Block Graph &#8211; list of nodes and list of edges. <code>Members:</code></p>
<dl>
<dt>&quot;nodes: array of XDbgBlockGraphNode&quot;</p>
<dd>Not documented</p>
<dt>&quot;edges: array of XDbgBlockGraphEdge&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 4.0 <code>x-debug-query-block-graph</code> (Command) Get the block graph. <code>Since:</code> 4.0 <code>drive-mirror</code> (Command) Start mirroring a block device&#8217;s writes to a new destination. target specifies the target of the new image. If the file exists, or if it is a device, it will be used as the new destination for writes. If it does not exist, a new file will be created. format specifies the format of the mirror image, default is to probe if mode=&#8217;existing&#8217;, else the format of the source. <code>Arguments:</code> the members of <tt>&quot;DriveMirror&quot;</tt> <code>Returns:</code> nothing on success If <tt>&quot;device&quot;</tt> is not a valid block device, GenericError <code>Since:</code> 1.3 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;drive-mirror&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;ide-hd0&quot;,<br />
                  &quot;target&quot; : &quot;/some/place/my-image&quot;,<br />
                  &quot;sync&quot; : &quot;full&quot;,<br />
                  &quot;format&quot; : &quot;qcow2&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>DriveMirror</code> (Object) A set of parameters describing drive mirror setup. <code>Members:</code></p>
<dl>
<dt>&quot;job-id: string&quot; (optional)</p>
<dd>identifier for the newly-created block job. If omitted, the device name will be used. (Since 2.7)</p>
<dt>&quot;device: string&quot;</p>
<dd>the device name or node-name of a root node whose writes should be mirrored.</p>
<dt>&quot;target: string&quot;</p>
<dd>the target of the new image. If the file exists, or if it is a device, the existing file/device will be used as the new destination. If it does not exist, a new file will be created.</p>
<dt>&quot;format: string&quot; (optional)</p>
<dd>the format of the new destination, default is to probe if <tt>&quot;mode&quot;</tt> is &#8216;existing&#8217;, else the format of the source</p>
<dt>&quot;node-name: string&quot; (optional)</p>
<dd>the new block driver state node name in the graph (Since 2.1)</p>
<dt>&quot;replaces: string&quot; (optional)</p>
<dd>with sync=full graph node name to be replaced by the new image when a whole image copy is done. This can be used to repair broken Quorum files. (Since 2.1)</p>
<dt>&quot;mode: NewImageMode&quot; (optional)</p>
<dd>whether and how <font SIZE="-1">QEMU</font> should create a new image, default is &#8216;absolute-paths&#8217;.</p>
<dt>&quot;speed: int&quot; (optional)</p>
<dd>the maximum speed, in bytes per second</p>
<dt>&quot;sync: MirrorSyncMode&quot;</p>
<dd>what parts of the disk image should be copied to the destination (all the disk, only the sectors allocated in the topmost image, or only new I/O).</p>
<dt>&quot;granularity: int&quot; (optional)</p>
<dd>granularity of the dirty bitmap, default is 64K if the image format doesn&#8217;t have clusters, 4K if the clusters are smaller than that, else the cluster size. Must be a power of 2 between 512 and 64M (since 1.4).</p>
<dt>&quot;buf-size: int&quot; (optional)</p>
<dd>maximum amount of data in flight from source to target (since 1.4).</p>
<dt>&quot;on-source-error: BlockdevOnError&quot; (optional)</p>
<dd>the action to take on an error on the source, default &#8216;report&#8217;. &#8216;stop&#8217; and &#8216;enospc&#8217; can only be used if the block device supports io-status (see BlockInfo).</p>
<dt>&quot;on-target-error: BlockdevOnError&quot; (optional)</p>
<dd>the action to take on an error on the target, default &#8216;report&#8217; (no limitations, since this applies to a different block device than <tt>&quot;device&quot;</tt>).</p>
<dt>&quot;unmap: boolean&quot; (optional)</p>
<dd>Whether to try to unmap target sectors where source has only zero. If true, and target unallocated sectors will read as zero, target image sectors will be unmapped; otherwise, zeroes will be written. Both will result in identical contents. Default is true. (Since 2.4)</p>
<dt>&quot;copy-mode: MirrorCopyMode&quot; (optional)</p>
<dd>when to copy data to the destination; defaults to &#8216;background&#8217; (Since: 3.0)</p>
<dt>&quot;auto-finalize: boolean&quot; (optional)</p>
<dd>When false, this job will wait in a <font SIZE="-1">PENDING</font> state after it has finished its work, waiting for <tt>&quot;block-job-finalize&quot;</tt> before making any block graph changes. When true, this job will automatically perform its abort or commit actions. Defaults to true. (Since 3.1)</p>
<dt>&quot;auto-dismiss: boolean&quot; (optional)</p>
<dd>When false, this job will wait in a <font SIZE="-1">CONCLUDED</font> state after it has completely ceased all work, and awaits <tt>&quot;block-job-dismiss&quot;</tt>. When true, this job will automatically disappear from the query list without user intervention. Defaults to true. (Since 3.1)</dl>
<p> <code>Since:</code> 1.3 <code>BlockDirtyBitmap</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;node: string&quot;</p>
<dd>name of device/node which the bitmap is tracking</p>
<dt>&quot;name: string&quot;</p>
<dd>name of the dirty bitmap</dl>
<p> <code>Since:</code> 2.4 <code>BlockDirtyBitmapAdd</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;node: string&quot;</p>
<dd>name of device/node which the bitmap is tracking</p>
<dt>&quot;name: string&quot;</p>
<dd>name of the dirty bitmap (must be less than 1024 bytes)</p>
<dt>&quot;granularity: int&quot; (optional)</p>
<dd>the bitmap granularity, default is 64k for block-dirty-bitmap-add</p>
<dt>&quot;persistent: boolean&quot; (optional)</p>
<dd>the bitmap is persistent, i.e. it will be saved to the corresponding block device image file on its close. For now only Qcow2 disks support persistent bitmaps. Default is false for block-dirty-bitmap-add. (Since: 2.10)</p>
<dt>&quot;disabled: boolean&quot; (optional)</p>
<dd>the bitmap is created in the disabled state, which means that it will not track drive changes. The bitmap may be enabled with block-dirty-bitmap-enable. Default is false. (Since: 4.0)</dl>
<p> <code>Since:</code> 2.4 <code>BlockDirtyBitmapMergeSource</code> (Alternate) <code>Members:</code></p>
<dl>
<dt>&quot;local: string&quot;</p>
<dd>name of the bitmap, attached to the same node as target bitmap.</p>
<dt>&quot;external: BlockDirtyBitmap&quot;</p>
<dd>bitmap with specified node</dl>
<p> <code>Since:</code> 4.1 <code>BlockDirtyBitmapMerge</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;node: string&quot;</p>
<dd>name of device/node which the <tt>&quot;target&quot;</tt> bitmap is tracking</p>
<dt>&quot;target: string&quot;</p>
<dd>name of the destination dirty bitmap</p>
<dt>&quot;bitmaps: array of BlockDirtyBitmapMergeSource&quot;</p>
<dd>name(s) of the source dirty bitmap(s) at <tt>&quot;node&quot;</tt> and/or fully specifed BlockDirtyBitmap elements. The latter are supported since 4.1.</dl>
<p> <code>Since:</code> 4.0 <code>block-dirty-bitmap-add</code> (Command) Create a dirty bitmap with a name on the node, and start tracking the writes. <code>Returns:</code> nothing on success If <tt>&quot;node&quot;</tt> is not a valid block device or node, DeviceNotFound If <tt>&quot;name&quot;</tt> is already taken, GenericError with an explanation <code>Since:</code> 2.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block-dirty-bitmap-add&quot;,<br />
   &quot;arguments&quot; : {&quot;node&quot; : &quot;drive0&quot;, &quot;name&quot; : &quot;bitmap0&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>block-dirty-bitmap-remove</code> (Command) Stop write tracking and remove the dirty bitmap that was created with block-dirty-bitmap-add. If the bitmap is persistent, remove it from its storage too. <code>Returns:</code> nothing on success If <tt>&quot;node&quot;</tt> is not a valid block device or node, DeviceNotFound If <tt>&quot;name&quot;</tt> is not found, GenericError with an explanation if <tt>&quot;name&quot;</tt> is frozen by an operation, GenericError <code>Since:</code> 2.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block-dirty-bitmap-remove&quot;,<br />
   &quot;arguments&quot; : {&quot;node&quot; : &quot;drive0&quot;, &quot;name&quot; : &quot;bitmap0&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>block-dirty-bitmap-clear</code> (Command) Clear (reset) a dirty bitmap on the device, so that an incremental backup from this point in time forward will only backup clusters modified after this clear operation. <code>Returns:</code> nothing on success If <tt>&quot;node&quot;</tt> is not a valid block device, DeviceNotFound If <tt>&quot;name&quot;</tt> is not found, GenericError with an explanation <code>Since:</code> 2.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block-dirty-bitmap-clear&quot;,<br />
   &quot;arguments&quot; : {&quot;node&quot; : &quot;drive0&quot;, &quot;name&quot; : &quot;bitmap0&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>block-dirty-bitmap-enable</code> (Command) Enables a dirty bitmap so that it will begin tracking disk changes. <code>Returns:</code> nothing on success If <tt>&quot;node&quot;</tt> is not a valid block device, DeviceNotFound If <tt>&quot;name&quot;</tt> is not found, GenericError with an explanation <code>Since:</code> 4.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block-dirty-bitmap-enable&quot;,<br />
   &quot;arguments&quot; : {&quot;node&quot; : &quot;drive0&quot;, &quot;name&quot; : &quot;bitmap0&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>block-dirty-bitmap-disable</code> (Command) Disables a dirty bitmap so that it will stop tracking disk changes. <code>Returns:</code> nothing on success If <tt>&quot;node&quot;</tt> is not a valid block device, DeviceNotFound If <tt>&quot;name&quot;</tt> is not found, GenericError with an explanation <code>Since:</code> 4.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block-dirty-bitmap-disable&quot;,<br />
   &quot;arguments&quot; : {&quot;node&quot; : &quot;drive0&quot;, &quot;name&quot; : &quot;bitmap0&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>block-dirty-bitmap-merge</code> (Command) Merge dirty bitmaps listed in <tt>&quot;bitmaps&quot;</tt> to the <tt>&quot;target&quot;</tt> dirty bitmap. Dirty bitmaps in <tt>&quot;bitmaps&quot;</tt> will be unchanged, except if it also appears as the <tt>&quot;target&quot;</tt> bitmap. Any bits already set in <tt>&quot;target&quot;</tt> will still be set after the merge, i.e., this operation does not clear the target. On error, <tt>&quot;target&quot;</tt> is unchanged. The resulting bitmap will count as dirty any clusters that were dirty in any of the source bitmaps. This can be used to achieve backup checkpoints, or in simpler usages, to copy bitmaps. <code>Returns:</code> nothing on success If <tt>&quot;node&quot;</tt> is not a valid block device, DeviceNotFound If any bitmap in <tt>&quot;bitmaps&quot;</tt> or <tt>&quot;target&quot;</tt> is not found, GenericError If any of the bitmaps have different sizes or granularities, GenericError <code>Since:</code> 4.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block-dirty-bitmap-merge&quot;,<br />
   &quot;arguments&quot; : {&quot;node&quot; : &quot;drive0&quot;, &quot;target&quot; : &quot;bitmap0&quot;, &quot;bitmaps&quot; : [&quot;bitmap1&quot;]}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>BlockDirtyBitmapSha256</code> (Object) <font SIZE="-1">SHA256</font> hash of dirty bitmap data <code>Members:</code></p>
<dl>
<dt>&quot;sha256: string&quot;</p>
<dd><font SIZE="-1">ASCII</font> representation of <font SIZE="-1">SHA256</font> bitmap hash</dl>
<p> <code>Since:</code> 2.10 <code>x-debug-block-dirty-bitmap-sha256</code> (Command) Get bitmap <font SIZE="-1">SHA256.</font> <code>Returns:</code> BlockDirtyBitmapSha256 on success If <tt>&quot;node&quot;</tt> is not a valid block device, DeviceNotFound If <tt>&quot;name&quot;</tt> is not found or if hashing has failed, GenericError with an explanation <code>Since:</code> 2.10 <code>blockdev-mirror</code> (Command) Start mirroring a block device&#8217;s writes to a new destination. <code>Arguments:</code></p>
<dl>
<dt>&quot;job-id: string&quot; (optional)</p>
<dd>identifier for the newly-created block job. If omitted, the device name will be used. (Since 2.7)</p>
<dt>&quot;device: string&quot;</p>
<dd>The device name or node-name of a root node whose writes should be mirrored.</p>
<dt>&quot;target: string&quot;</p>
<dd>the id or node-name of the block device to mirror to. This mustn&#8217;t be attached to guest.</p>
<dt>&quot;replaces: string&quot; (optional)</p>
<dd>with sync=full graph node name to be replaced by the new image when a whole image copy is done. This can be used to repair broken Quorum files.</p>
<dt>&quot;speed: int&quot; (optional)</p>
<dd>the maximum speed, in bytes per second</p>
<dt>&quot;sync: MirrorSyncMode&quot;</p>
<dd>what parts of the disk image should be copied to the destination (all the disk, only the sectors allocated in the topmost image, or only new I/O).</p>
<dt>&quot;granularity: int&quot; (optional)</p>
<dd>granularity of the dirty bitmap, default is 64K if the image format doesn&#8217;t have clusters, 4K if the clusters are smaller than that, else the cluster size. Must be a power of 2 between 512 and 64M</p>
<dt>&quot;buf-size: int&quot; (optional)</p>
<dd>maximum amount of data in flight from source to target</p>
<dt>&quot;on-source-error: BlockdevOnError&quot; (optional)</p>
<dd>the action to take on an error on the source, default &#8216;report&#8217;. &#8216;stop&#8217; and &#8216;enospc&#8217; can only be used if the block device supports io-status (see BlockInfo).</p>
<dt>&quot;on-target-error: BlockdevOnError&quot; (optional)</p>
<dd>the action to take on an error on the target, default &#8216;report&#8217; (no limitations, since this applies to a different block device than <tt>&quot;device&quot;</tt>).</p>
<dt>&quot;filter-node-name: string&quot; (optional)</p>
<dd>the node name that should be assigned to the filter driver that the mirror job inserts into the graph above <tt>&quot;device&quot;</tt>. If this option is not given, a node name is autogenerated. (Since: 2.9)</p>
<dt>&quot;copy-mode: MirrorCopyMode&quot; (optional)</p>
<dd>when to copy data to the destination; defaults to &#8216;background&#8217; (Since: 3.0)</p>
<dt>&quot;auto-finalize: boolean&quot; (optional)</p>
<dd>When false, this job will wait in a <font SIZE="-1">PENDING</font> state after it has finished its work, waiting for <tt>&quot;block-job-finalize&quot;</tt> before making any block graph changes. When true, this job will automatically perform its abort or commit actions. Defaults to true. (Since 3.1)</p>
<dt>&quot;auto-dismiss: boolean&quot; (optional)</p>
<dd>When false, this job will wait in a <font SIZE="-1">CONCLUDED</font> state after it has completely ceased all work, and awaits <tt>&quot;block-job-dismiss&quot;</tt>. When true, this job will automatically disappear from the query list without user intervention. Defaults to true. (Since 3.1)</dl>
<p> <code>Returns:</code> nothing on success. <code>Since:</code> 2.6 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-mirror&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;ide-hd0&quot;,<br />
                  &quot;target&quot; : &quot;target0&quot;,<br />
                  &quot;sync&quot; : &quot;full&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>block_set_io_throttle</code> (Command) Change I/O throttle limits for a block drive. Since <font SIZE="-1">QEMU 2.4,</font> each device with I/O limits is member of a throttle group. If two or more devices are members of the same group, the limits will apply to the combined I/O of the whole group in a round-robin fashion. Therefore, setting new I/O limits to a device will affect the whole group. The name of the group can be specified using the &#8216;group&#8217; parameter. If the parameter is unset, it is assumed to be the current group of that device. If it&#8217;s not in any group yet, the name of the device will be used as the name for its group. The &#8216;group&#8217; parameter can also be used to move a device to a different group. In this case the limits specified in the parameters will be applied to the new group only. I/O limits can be disabled by setting all of them to 0. In this case the device will be removed from its group and the rest of its members will not be affected. The &#8216;group&#8217; parameter is ignored. <code>Arguments:</code> the members of <tt>&quot;BlockIOThrottle&quot;</tt> <code>Returns:</code> Nothing on success If <tt>&quot;device&quot;</tt> is not a valid block device, DeviceNotFound <code>Since:</code> 1.1 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block_set_io_throttle&quot;,<br />
   &quot;arguments&quot; : {&quot;id&quot; : &quot;virtio-blk-pci0/virtio-backend&quot;,<br />
                  &quot;bps&quot; : 0,<br />
                  &quot;bps_rd&quot; : 0,<br />
                  &quot;bps_wr&quot; : 0,<br />
                  &quot;iops&quot; : 512,<br />
                  &quot;iops_rd&quot; : 0,<br />
                  &quot;iops_wr&quot; : 0,<br />
                  &quot;bps_max&quot; : 0,<br />
                  &quot;bps_rd_max&quot; : 0,<br />
                  &quot;bps_wr_max&quot; : 0,<br />
                  &quot;iops_max&quot; : 0,<br />
                  &quot;iops_rd_max&quot; : 0,<br />
                  &quot;iops_wr_max&quot; : 0,<br />
                  &quot;bps_max_length&quot; : 0,<br />
                  &quot;iops_size&quot; : 0}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
    }</p>
<p>        -&gt; {&quot;execute&quot; : &quot;block_set_io_throttle&quot;,<br />
            &quot;arguments&quot; : {&quot;id&quot; : &quot;ide0-1-0&quot;,<br />
                           &quot;bps&quot; : 1000000,<br />
                           &quot;bps_rd&quot; : 0,<br />
                           &quot;bps_wr&quot; : 0,<br />
                           &quot;iops&quot; : 0,<br />
                           &quot;iops_rd&quot; : 0,<br />
                           &quot;iops_wr&quot; : 0,<br />
                           &quot;bps_max&quot; : 8000000,<br />
                           &quot;bps_rd_max&quot; : 0,<br />
                           &quot;bps_wr_max&quot; : 0,<br />
                           &quot;iops_max&quot; : 0,<br />
                           &quot;iops_rd_max&quot; : 0,<br />
                           &quot;iops_wr_max&quot; : 0,<br />
                           &quot;bps_max_length&quot; : 60,<br />
                           &quot;iops_size&quot; : 0}} &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
    } <code>BlockIOThrottle</code> (Object) A set of parameters describing block throttling. <code>Members:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>Block device name (deprecated, use <tt>&quot;id&quot;</tt> instead)</p>
<dt>&quot;id: string&quot; (optional)</p>
<dd>The name or <font SIZE="-1">QOM</font> path of the guest device (since: 2.8)</p>
<dt>&quot;bps: int&quot;</p>
<dd>total throughput limit in bytes per second</p>
<dt>&quot;bps_rd: int&quot;</p>
<dd>read throughput limit in bytes per second</p>
<dt>&quot;bps_wr: int&quot;</p>
<dd>write throughput limit in bytes per second</p>
<dt>&quot;iops: int&quot;</p>
<dd>total I/O operations per second</p>
<dt>&quot;iops_rd: int&quot;</p>
<dd>read I/O operations per second</p>
<dt>&quot;iops_wr: int&quot;</p>
<dd>write I/O operations per second</p>
<dt>&quot;bps_max: int&quot; (optional)</p>
<dd>total throughput limit during bursts, in bytes (Since 1.7)</p>
<dt>&quot;bps_rd_max: int&quot; (optional)</p>
<dd>read throughput limit during bursts, in bytes (Since 1.7)</p>
<dt>&quot;bps_wr_max: int&quot; (optional)</p>
<dd>write throughput limit during bursts, in bytes (Since 1.7)</p>
<dt>&quot;iops_max: int&quot; (optional)</p>
<dd>total I/O operations per second during bursts, in bytes (Since 1.7)</p>
<dt>&quot;iops_rd_max: int&quot; (optional)</p>
<dd>read I/O operations per second during bursts, in bytes (Since 1.7)</p>
<dt>&quot;iops_wr_max: int&quot; (optional)</p>
<dd>write I/O operations per second during bursts, in bytes (Since 1.7)</p>
<dt>&quot;bps_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;bps_max&quot;</tt> burst period, in seconds. It must only be set if <tt>&quot;bps_max&quot;</tt> is set as well. Defaults to 1. (Since 2.6)</p>
<dt>&quot;bps_rd_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;bps_rd_max&quot;</tt> burst period, in seconds. It must only be set if <tt>&quot;bps_rd_max&quot;</tt> is set as well. Defaults to 1. (Since 2.6)</p>
<dt>&quot;bps_wr_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;bps_wr_max&quot;</tt> burst period, in seconds. It must only be set if <tt>&quot;bps_wr_max&quot;</tt> is set as well. Defaults to 1. (Since 2.6)</p>
<dt>&quot;iops_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;iops&quot;</tt> burst period, in seconds. It must only be set if <tt>&quot;iops_max&quot;</tt> is set as well. Defaults to 1. (Since 2.6)</p>
<dt>&quot;iops_rd_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;iops_rd_max&quot;</tt> burst period, in seconds. It must only be set if <tt>&quot;iops_rd_max&quot;</tt> is set as well. Defaults to 1. (Since 2.6)</p>
<dt>&quot;iops_wr_max_length: int&quot; (optional)</p>
<dd>maximum length of the <tt>&quot;iops_wr_max&quot;</tt> burst period, in seconds. It must only be set if <tt>&quot;iops_wr_max&quot;</tt> is set as well. Defaults to 1. (Since 2.6)</p>
<dt>&quot;iops_size: int&quot; (optional)</p>
<dd>an I/O size in bytes (Since 1.7)</p>
<dt>&quot;group: string&quot; (optional)</p>
<dd>throttle group name (Since 2.4)</dl>
<p> <code>Since:</code> 1.1 <code>ThrottleLimits</code> (Object) Limit parameters for throttling. Since some limit combinations are illegal, limits should always be set in one transaction. All fields are optional. When setting limits, if a field is missing the current value is not changed. <code>Members:</code></p>
<dl>
<dt>&quot;iops-total: int&quot; (optional)</p>
<dd>limit total I/O operations per second</p>
<dt>&quot;iops-total-max: int&quot; (optional)</p>
<dd>I/O operations burst</p>
<dt>&quot;iops-total-max-length: int&quot; (optional)</p>
<dd>length of the iops-total-max burst period, in seconds It must only be set if <tt>&quot;iops-total-max&quot;</tt> is set as well.</p>
<dt>&quot;iops-read: int&quot; (optional)</p>
<dd>limit read operations per second</p>
<dt>&quot;iops-read-max: int&quot; (optional)</p>
<dd>I/O operations read burst</p>
<dt>&quot;iops-read-max-length: int&quot; (optional)</p>
<dd>length of the iops-read-max burst period, in seconds It must only be set if <tt>&quot;iops-read-max&quot;</tt> is set as well.</p>
<dt>&quot;iops-write: int&quot; (optional)</p>
<dd>limit write operations per second</p>
<dt>&quot;iops-write-max: int&quot; (optional)</p>
<dd>I/O operations write burst</p>
<dt>&quot;iops-write-max-length: int&quot; (optional)</p>
<dd>length of the iops-write-max burst period, in seconds It must only be set if <tt>&quot;iops-write-max&quot;</tt> is set as well.</p>
<dt>&quot;bps-total: int&quot; (optional)</p>
<dd>limit total bytes per second</p>
<dt>&quot;bps-total-max: int&quot; (optional)</p>
<dd>total bytes burst</p>
<dt>&quot;bps-total-max-length: int&quot; (optional)</p>
<dd>length of the bps-total-max burst period, in seconds. It must only be set if <tt>&quot;bps-total-max&quot;</tt> is set as well.</p>
<dt>&quot;bps-read: int&quot; (optional)</p>
<dd>limit read bytes per second</p>
<dt>&quot;bps-read-max: int&quot; (optional)</p>
<dd>total bytes read burst</p>
<dt>&quot;bps-read-max-length: int&quot; (optional)</p>
<dd>length of the bps-read-max burst period, in seconds It must only be set if <tt>&quot;bps-read-max&quot;</tt> is set as well.</p>
<dt>&quot;bps-write: int&quot; (optional)</p>
<dd>limit write bytes per second</p>
<dt>&quot;bps-write-max: int&quot; (optional)</p>
<dd>total bytes write burst</p>
<dt>&quot;bps-write-max-length: int&quot; (optional)</p>
<dd>length of the bps-write-max burst period, in seconds It must only be set if <tt>&quot;bps-write-max&quot;</tt> is set as well.</p>
<dt>&quot;iops-size: int&quot; (optional)</p>
<dd>when limiting by iops max size of an I/O in bytes</dl>
<p> <code>Since:</code> 2.11 <code>block-stream</code> (Command) Copy data from a backing file into a block device. The block streaming operation is performed in the background until the entire backing file has been copied. This command returns immediately once streaming has started. The status of ongoing block streaming operations can be checked with query-block-jobs. The operation can be stopped before it has completed using the block-job-cancel command. The node that receives the data is called the top image, can be located in any part of the chain (but always above the base image; see below) and can be specified using its device or node name. Earlier qemu versions only allowed &#8216;device&#8217; to name the top level node; presence of the &#8216;base-node&#8217; parameter during introspection can be used as a witness of the enhanced semantics of &#8216;device&#8217;. If a base file is specified then sectors are not copied from that base file and its backing chain. When streaming completes the image file will have the base file as its backing file. This can be used to stream a subset of the backing file chain instead of flattening the entire image. On successful completion the image file is updated to drop the backing file and the <font SIZE="-1">BLOCK_JOB_COMPLETED</font> event is emitted. <code>Arguments:</code></p>
<dl>
<dt>&quot;job-id: string&quot; (optional)</p>
<dd>identifier for the newly-created block job. If omitted, the device name will be used. (Since 2.7)</p>
<dt>&quot;device: string&quot;</p>
<dd>the device or node name of the top image</p>
<dt>&quot;base: string&quot; (optional)</p>
<dd>the common backing file name. It cannot be set if <tt>&quot;base-node&quot;</tt> is also set.</p>
<dt>&quot;base-node: string&quot; (optional)</p>
<dd>the node name of the backing file. It cannot be set if <tt>&quot;base&quot;</tt> is also set. (Since 2.8)</p>
<dt>&quot;backing-file: string&quot; (optional)</p>
<dd>The backing file string to write into the top image. This filename is not validated. If a pathname string is such that it cannot be resolved by <font SIZE="-1">QEMU,</font> that means that subsequent <font SIZE="-1">QMP</font> or <font SIZE="-1">HMP</font> commands must use node-names for the image in question, as filename lookup methods will fail. If not specified, <font SIZE="-1">QEMU</font> will automatically determine the backing file string to use, or error out if there is no obvious choice. Care should be taken when specifying the string, to specify a valid filename or protocol. (Since 2.1)</p>
<dt>&quot;speed: int&quot; (optional)</p>
<dd>the maximum speed, in bytes per second</p>
<dt>&quot;on-error: BlockdevOnError&quot; (optional)</p>
<dd>the action to take on an error (default report). &#8216;stop&#8217; and &#8216;enospc&#8217; can only be used if the block device supports io-status (see BlockInfo). Since 1.3.</p>
<dt>&quot;auto-finalize: boolean&quot; (optional)</p>
<dd>When false, this job will wait in a <font SIZE="-1">PENDING</font> state after it has finished its work, waiting for <tt>&quot;block-job-finalize&quot;</tt> before making any block graph changes. When true, this job will automatically perform its abort or commit actions. Defaults to true. (Since 3.1)</p>
<dt>&quot;auto-dismiss: boolean&quot; (optional)</p>
<dd>When false, this job will wait in a <font SIZE="-1">CONCLUDED</font> state after it has completely ceased all work, and awaits <tt>&quot;block-job-dismiss&quot;</tt>. When true, this job will automatically disappear from the query list without user intervention. Defaults to true. (Since 3.1)</dl>
<p> <code>Returns:</code> Nothing on success. If <tt>&quot;device&quot;</tt> does not exist, DeviceNotFound. <code>Since:</code> 1.1 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block-stream&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;virtio0&quot;,<br />
                  &quot;base&quot; : &quot;/tmp/master.qcow2&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>block-job-set-speed</code> (Command) Set maximum speed for a background block operation. This command can only be issued when there is an active block job. Throttling can be disabled by setting the speed to 0. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>The job identifier. This used to be a device name (hence the name of the parameter), but since <font SIZE="-1">QEMU 2.7</font> it can have other values.</p>
<dt>&quot;speed: int&quot;</p>
<dd>the maximum speed, in bytes per second, or 0 for unlimited. Defaults to 0.</dl>
<p> <code>Returns:</code> Nothing on success If no background operation is active on this device, DeviceNotActive <code>Since:</code> 1.1 <code>block-job-cancel</code> (Command) Stop an active background block operation. This command returns immediately after marking the active background block operation for cancellation. It is an error to call this command if no operation is in progress. The operation will cancel as soon as possible and then emit the <font SIZE="-1">BLOCK_JOB_CANCELLED</font> event. Before that happens the job is still visible when enumerated using query-block-jobs. Note that if you issue &#8216;block-job-cancel&#8217; after &#8216;drive-mirror&#8217; has indicated (via the event <font SIZE="-1">BLOCK_JOB_READY</font>) that the source and destination are synchronized, then the event triggered by this command changes to <font SIZE="-1">BLOCK_JOB_COMPLETED,</font> to indicate that the mirroring has ended and the destination now has a point-in-time copy tied to the time of the cancellation. For streaming, the image file retains its backing file unless the streaming operation happens to complete just as it is being cancelled. A new streaming operation can be started at a later time to finish copying all data from the backing file. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>The job identifier. This used to be a device name (hence the name of the parameter), but since <font SIZE="-1">QEMU 2.7</font> it can have other values.</p>
<dt>&quot;force: boolean&quot; (optional)</p>
<dd>If true, and the job has already emitted the event <font SIZE="-1">BLOCK_JOB_READY,</font> abandon the job immediately (even if it is paused) instead of waiting for the destination to complete its final synchronization (since 1.3)</dl>
<p> <code>Returns:</code> Nothing on success If no background operation is active on this device, DeviceNotActive <code>Since:</code> 1.1 <code>block-job-pause</code> (Command) Pause an active background block operation. This command returns immediately after marking the active background block operation for pausing. It is an error to call this command if no operation is in progress or if the job is already paused. The operation will pause as soon as possible. No event is emitted when the operation is actually paused. Cancelling a paused job automatically resumes it. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>The job identifier. This used to be a device name (hence the name of the parameter), but since <font SIZE="-1">QEMU 2.7</font> it can have other values.</dl>
<p> <code>Returns:</code> Nothing on success If no background operation is active on this device, DeviceNotActive <code>Since:</code> 1.3 <code>block-job-resume</code> (Command) Resume an active background block operation. This command returns immediately after resuming a paused background block operation. It is an error to call this command if no operation is in progress or if the job is not paused. This command also clears the error status of the job. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>The job identifier. This used to be a device name (hence the name of the parameter), but since <font SIZE="-1">QEMU 2.7</font> it can have other values.</dl>
<p> <code>Returns:</code> Nothing on success If no background operation is active on this device, DeviceNotActive <code>Since:</code> 1.3 <code>block-job-complete</code> (Command) Manually trigger completion of an active background block operation. This is supported for drive mirroring, where it also switches the device to write to the target path only. The ability to complete is signaled with a <font SIZE="-1">BLOCK_JOB_READY</font> event. This command completes an active background block operation synchronously. The ordering of this command&#8217;s return with the <font SIZE="-1">BLOCK_JOB_COMPLETED</font> event is not defined. Note that if an I/O error occurs during the processing of this command: 1) the command itself will fail; 2) the error will be processed according to the rerror/werror arguments that were specified when starting the operation. A cancelled or paused job cannot be completed. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>The job identifier. This used to be a device name (hence the name of the parameter), but since <font SIZE="-1">QEMU 2.7</font> it can have other values.</dl>
<p> <code>Returns:</code> Nothing on success If no background operation is active on this device, DeviceNotActive <code>Since:</code> 1.3 <code>block-job-dismiss</code> (Command) For jobs that have already concluded, remove them from the block-job-query list. This command only needs to be run for jobs which were started with <font SIZE="-1">QEMU 2.12+</font> job lifetime management semantics. This command will refuse to operate on any job that has not yet reached its terminal state, <font SIZE="-1">JOB_STATUS_CONCLUDED.</font> For jobs that make use of the <font SIZE="-1">BLOCK_JOB_READY</font> event, block-job-cancel or block-job-complete will still need to be used as appropriate. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The job identifier.</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 2.12 <code>block-job-finalize</code> (Command) Once a job that has manual=true reaches the pending state, it can be instructed to finalize any graph changes and do any necessary cleanup via this command. For jobs in a transaction, instructing one job to finalize will force <font SIZE="-1">ALL</font> jobs in the transaction to finalize, so it is only necessary to instruct a single member job to finalize. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The job identifier.</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 2.12 <code>BlockdevDiscardOptions</code> (Enum) Determines how to handle discard requests. <code>Values:</code></p>
<dl>
<dt>&quot;ignore&quot;</p>
<dd>Ignore the request</p>
<dt>&quot;unmap&quot;</p>
<dd>Forward as an unmap request</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevDetectZeroesOptions</code> (Enum) Describes the operation mode for the automatic conversion of plain zero writes by the <font SIZE="-1">OS</font> to driver specific optimized zero write commands. <code>Values:</code></p>
<dl>
<dt>&quot;off&quot;</p>
<dd>Disabled (default)</p>
<dt>&quot;on&quot;</p>
<dd>Enabled</p>
<dt>&quot;unmap&quot;</p>
<dd>Enabled and even try to unmap blocks if possible. This requires also that <tt>&quot;BlockdevDiscardOptions&quot;</tt> is set to unmap for this device.</dl>
<p> <code>Since:</code> 2.1 <code>BlockdevAioOptions</code> (Enum) Selects the <font SIZE="-1">AIO</font> backend to handle I/O requests <code>Values:</code></p>
<dl>
<dt>&quot;threads&quot;</p>
<dd>Use qemu&#8217;s thread pool</p>
<dt>&quot;native&quot;</p>
<dd>Use native <font SIZE="-1">AIO</font> backend (only Linux and Windows)</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevCacheOptions</code> (Object) Includes cache-related options for block devices <code>Members:</code></p>
<dl>
<dt>&quot;direct: boolean&quot; (optional)</p>
<dd>enables use of O_DIRECT (bypass the host page cache; default: false)</p>
<dt>&quot;no-flush: boolean&quot; (optional)</p>
<dd>ignore any flush requests for the device (default: false)</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevDriver</code> (Enum) Drivers that are supported in block device operations. <code>Values:</code></p>
<dl>
<dt>&quot;vxhs&quot;</p>
<dd>Since 2.10</p>
<dt>&quot;throttle&quot;</p>
<dd>Since 2.11</p>
<dt>&quot;nvme&quot;</p>
<dd>Since 2.12</p>
<dt>&quot;copy-on-read&quot;</p>
<dd>Since 3.0</p>
<dt>&quot;blklogwrites&quot;</p>
<dd>Since 3.0</p>
<dt>&quot;blkreplay&quot;</p>
<dd>Since 4.2</p>
<dt>&quot;blkdebug&quot;</p>
<dd>Not documented</p>
<dt>&quot;blkverify&quot;</p>
<dd>Not documented</p>
<dt>&quot;bochs&quot;</p>
<dd>Not documented</p>
<dt>&quot;cloop&quot;</p>
<dd>Not documented</p>
<dt>&quot;dmg&quot;</p>
<dd>Not documented</p>
<dt>&quot;file&quot;</p>
<dd>Not documented</p>
<dt>&quot;ftp&quot;</p>
<dd>Not documented</p>
<dt>&quot;ftps&quot;</p>
<dd>Not documented</p>
<dt>&quot;gluster&quot;</p>
<dd>Not documented</p>
<dt>&quot;host_cdrom&quot;</p>
<dd>Not documented</p>
<dt>&quot;host_device&quot;</p>
<dd>Not documented</p>
<dt>&quot;http&quot;</p>
<dd>Not documented</p>
<dt>&quot;https&quot;</p>
<dd>Not documented</p>
<dt>&quot;iscsi&quot;</p>
<dd>Not documented</p>
<dt>&quot;luks&quot;</p>
<dd>Not documented</p>
<dt>&quot;nbd&quot;</p>
<dd>Not documented</p>
<dt>&quot;nfs&quot;</p>
<dd>Not documented</p>
<dt>&quot;null-aio&quot;</p>
<dd>Not documented</p>
<dt>&quot;null-co&quot;</p>
<dd>Not documented</p>
<dt>&quot;parallels&quot;</p>
<dd>Not documented</p>
<dt>&quot;qcow&quot;</p>
<dd>Not documented</p>
<dt>&quot;qcow2&quot;</p>
<dd>Not documented</p>
<dt>&quot;qed&quot;</p>
<dd>Not documented</p>
<dt>&quot;quorum&quot;</p>
<dd>Not documented</p>
<dt>&quot;raw&quot;</p>
<dd>Not documented</p>
<dt>&quot;rbd&quot;</p>
<dd>Not documented</p>
<dt>&quot;replication&quot;</p>
<dd>Not documented <code>If:</code> <tt>&quot;defined(CONFIG_REPLICATION)&quot;</tt></p>
<dt>&quot;sheepdog&quot;</p>
<dd>Not documented</p>
<dt>&quot;ssh&quot;</p>
<dd>Not documented</p>
<dt>&quot;vdi&quot;</p>
<dd>Not documented</p>
<dt>&quot;vhdx&quot;</p>
<dd>Not documented</p>
<dt>&quot;vmdk&quot;</p>
<dd>Not documented</p>
<dt>&quot;vpc&quot;</p>
<dd>Not documented</p>
<dt>&quot;vvfat&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsFile</code> (Object) Driver specific block device options for the file backend. <code>Members:</code></p>
<dl>
<dt>&quot;filename: string&quot;</p>
<dd>path to the image file</p>
<dt>&quot;pr-manager: string&quot; (optional)</p>
<dd>the id for the object that will handle persistent reservations for this device (default: none, forward the commands via <font SIZE="-1">SG_IO</font>; since 2.11)</p>
<dt>&quot;aio: BlockdevAioOptions&quot; (optional)</p>
<dd><font SIZE="-1">AIO</font> backend (default: threads) (since: 2.8)</p>
<dt>&quot;locking: OnOffAuto&quot; (optional)</p>
<dd>whether to enable file locking. If set to &#8216;auto&#8217;, only enable when Open File Descriptor (<font SIZE="-1">OFD</font>) locking <font SIZE="-1">API</font> is available (default: auto, since 2.10)</p>
<dt>&quot;drop-cache: boolean&quot; (optional)</p>
<dd>invalidate page cache during live migration. This prevents stale data on the migration destination with cache.direct=off. Currently only supported on Linux hosts. (default: on, since: 4.0) <code>If:</code> <tt>&quot;defined(CONFIG_LINUX)&quot;</tt></p>
<dt>&quot;x-check-cache-dropped: boolean&quot; (optional)</p>
<dd>whether to check that page cache was dropped on live migration. May cause noticeable delays if the image file is large, do not use in production. (default: off) (since: 3.0)</dl>
<p> <code>Features:</code></p>
<dl>
<dt>&quot;dynamic-auto-read-only&quot;</p>
<dd>If present, enabled auto-read-only means that the driver will open the image read-only at first, dynamically reopen the image file read-write when the first writer is attached to the node and reopen read-only when the last writer is detached. This allows giving <font SIZE="-1">QEMU</font> write permissions only on demand when an operation actually needs write access.</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsNull</code> (Object) Driver specific block device options for the null backend. <code>Members:</code></p>
<dl>
<dt>&quot;size: int&quot; (optional)</p>
<dd>size of the device in bytes.</p>
<dt>&quot;latency-ns: int&quot; (optional)</p>
<dd>emulated latency (in nanoseconds) in processing requests. Default to zero which completes requests immediately. (Since 2.4)</p>
<dt>&quot;read-zeroes: boolean&quot; (optional)</p>
<dd>if true, reads from the device produce zeroes; if false, the buffer is left unchanged. (default: false; since: 4.1)</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsNVMe</code> (Object) Driver specific block device options for the NVMe backend. <code>Members:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>controller address of the NVMe device.</p>
<dt>&quot;namespace: int&quot;</p>
<dd>namespace number of the device, starting from 1.</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevOptionsVVFAT</code> (Object) Driver specific block device options for the vvfat protocol. <code>Members:</code></p>
<dl>
<dt>&quot;dir: string&quot;</p>
<dd>directory to be exported as <font SIZE="-1">FAT</font> image</p>
<dt>&quot;fat-type: int&quot; (optional)</p>
<dd><font SIZE="-1">FAT</font> type: 12, 16 or 32</p>
<dt>&quot;floppy: boolean&quot; (optional)</p>
<dd>whether to export a floppy image (true) or partitioned hard disk (false; default)</p>
<dt>&quot;label: string&quot; (optional)</p>
<dd>set the volume label, limited to 11 bytes. <font SIZE="-1">FAT16</font> and <font SIZE="-1">FAT32</font> traditionally have some restrictions on labels, which are ignored by most operating systems. Defaults to &#8220;<font SIZE="-1">QEMU VVFAT&#8221;.</font> (since 2.4)</p>
<dt>&quot;rw: boolean&quot; (optional)</p>
<dd>whether to allow write operations (default: false)</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsGenericFormat</code> (Object) Driver specific block device options for image format that have no option besides their data source. <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>reference to or definition of the data source block device</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsLUKS</code> (Object) Driver specific block device options for <font SIZE="-1">LUKS.</font> <code>Members:</code></p>
<dl>
<dt>&quot;key-secret: string&quot; (optional)</p>
<dd>the <font SIZE="-1">ID</font> of a QCryptoSecret object providing the decryption key (since 2.6). Mandatory except when doing a metadata-only probe of the image.</p>
<dt>The members of &quot;BlockdevOptionsGenericFormat&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsGenericCOWFormat</code> (Object) Driver specific block device options for image format that have no option besides their data source and an optional backing file. <code>Members:</code></p>
<dl>
<dt>&quot;backing: BlockdevRefOrNull&quot; (optional)</p>
<dd>reference to or definition of the backing file block device, null disables the backing file entirely. Defaults to the backing file stored the image file.</p>
<dt>The members of &quot;BlockdevOptionsGenericFormat&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.9 <code>Qcow2OverlapCheckMode</code> (Enum) General overlap check modes. <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>Do not perform any checks</p>
<dt>&quot;constant&quot;</p>
<dd>Perform only checks which can be done in constant time and without reading anything from disk</p>
<dt>&quot;cached&quot;</p>
<dd>Perform only checks which can be done without reading anything from disk</p>
<dt>&quot;all&quot;</p>
<dd>Perform all available overlap checks</dl>
<p> <code>Since:</code> 2.9 <code>Qcow2OverlapCheckFlags</code> (Object) Structure of flags for each metadata structure. Setting a field to &#8216;true&#8217; makes qemu guard that structure against unintended overwriting. The default value is chosen according to the template given. <code>Members:</code></p>
<dl>
<dt>&quot;template: Qcow2OverlapCheckMode&quot; (optional)</p>
<dd>Specifies a template mode which can be adjusted using the other flags, defaults to &#8216;cached&#8217;</p>
<dt>&quot;bitmap-directory: boolean&quot; (optional)</p>
<dd>since 3.0</p>
<dt>&quot;main-header: boolean&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;active-l1: boolean&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;active-l2: boolean&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;refcount-table: boolean&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;refcount-block: boolean&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;snapshot-table: boolean&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;inactive-l1: boolean&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;inactive-l2: boolean&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.9 <code>Qcow2OverlapChecks</code> (Alternate) Specifies which metadata structures should be guarded against unintended overwriting. <code>Members:</code></p>
<dl>
<dt>&quot;flags: Qcow2OverlapCheckFlags&quot;</p>
<dd>set of flags for separate specification of each metadata structure type</p>
<dt>&quot;mode: Qcow2OverlapCheckMode&quot;</p>
<dd>named mode which chooses a specific set of flags</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevQcowEncryptionFormat</code> (Enum) <code>Values:</code></p>
<dl>
<dt>&quot;aes&quot;</p>
<dd>AES-CBC with plain64 initialization vectors</dl>
<p> <code>Since:</code> 2.10 <code>BlockdevQcowEncryption</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;format: BlockdevQcowEncryptionFormat&quot;</p>
<dd>Not documented</p>
<dt>The members of &quot;QCryptoBlockOptionsQCow&quot; when &quot;format&quot; is &quot;aes&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.10 <code>BlockdevOptionsQcow</code> (Object) Driver specific block device options for qcow. <code>Members:</code></p>
<dl>
<dt>&quot;encrypt: BlockdevQcowEncryption&quot; (optional)</p>
<dd>Image decryption options. Mandatory for encrypted images, except when doing a metadata-only probe of the image.</p>
<dt>The members of &quot;BlockdevOptionsGenericCOWFormat&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.10 <code>BlockdevQcow2EncryptionFormat</code> (Enum) <code>Values:</code></p>
<dl>
<dt>&quot;aes&quot;</p>
<dd>AES-CBC with plain64 initialization vectors</p>
<dt>&quot;luks&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.10 <code>BlockdevQcow2Encryption</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;format: BlockdevQcow2EncryptionFormat&quot;</p>
<dd>Not documented</p>
<dt>The members of &quot;QCryptoBlockOptionsQCow&quot; when &quot;format&quot; is &quot;aes&quot;</p>
<dd>
<dt>The members of &quot;QCryptoBlockOptionsLUKS&quot; when &quot;format&quot; is &quot;luks&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.10 <code>BlockdevOptionsQcow2</code> (Object) Driver specific block device options for qcow2. <code>Members:</code></p>
<dl>
<dt>&quot;lazy-refcounts: boolean&quot; (optional)</p>
<dd>whether to enable the lazy refcounts feature (default is taken from the image file)</p>
<dt>&quot;pass-discard-request: boolean&quot; (optional)</p>
<dd>whether discard requests to the qcow2 device should be forwarded to the data source</p>
<dt>&quot;pass-discard-snapshot: boolean&quot; (optional)</p>
<dd>whether discard requests for the data source should be issued when a snapshot operation (e.g. deleting a snapshot) frees clusters in the qcow2 file</p>
<dt>&quot;pass-discard-other: boolean&quot; (optional)</p>
<dd>whether discard requests for the data source should be issued on other occasions where a cluster gets freed</p>
<dt>&quot;overlap-check: Qcow2OverlapChecks&quot; (optional)</p>
<dd>which overlap checks to perform for writes to the image, defaults to &#8216;cached&#8217; (since 2.2)</p>
<dt>&quot;cache-size: int&quot; (optional)</p>
<dd>the maximum total size of the L2 table and refcount block caches in bytes (since 2.2)</p>
<dt>&quot;l2-cache-size: int&quot; (optional)</p>
<dd>the maximum size of the L2 table cache in bytes (since 2.2)</p>
<dt>&quot;l2-cache-entry-size: int&quot; (optional)</p>
<dd>the size of each entry in the L2 cache in bytes. It must be a power of two between 512 and the cluster size. The default value is the cluster size (since 2.12)</p>
<dt>&quot;refcount-cache-size: int&quot; (optional)</p>
<dd>the maximum size of the refcount block cache in bytes (since 2.2)</p>
<dt>&quot;cache-clean-interval: int&quot; (optional)</p>
<dd>clean unused entries in the L2 and refcount caches. The interval is in seconds. The default value is 600 on supporting platforms, and 0 on other platforms. 0 disables this feature. (since 2.5)</p>
<dt>&quot;encrypt: BlockdevQcow2Encryption&quot; (optional)</p>
<dd>Image decryption options. Mandatory for encrypted images, except when doing a metadata-only probe of the image. (since 2.10)</p>
<dt>&quot;data-file: BlockdevRef&quot; (optional)</p>
<dd>reference to or definition of the external data file. This may only be specified for images that require an external data file. If it is not specified for such an image, the data file name is loaded from the image file. (since 4.0)</p>
<dt>The members of &quot;BlockdevOptionsGenericCOWFormat&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.9 <code>SshHostKeyCheckMode</code> (Enum) <tt>&quot;none&quot;</tt> Don&#8217;t check the host key at all <tt>&quot;hash&quot;</tt> Compare the host key with a given hash <tt>&quot;known_hosts&quot;</tt> Check the host key against the known_hosts file <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>Not documented</p>
<dt>&quot;hash&quot;</p>
<dd>Not documented</p>
<dt>&quot;known_hosts&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>SshHostKeyCheckHashType</code> (Enum) <tt>&quot;md5&quot;</tt> The given hash is an md5 hash <tt>&quot;sha1&quot;</tt> The given hash is an sha1 hash <code>Values:</code></p>
<dl>
<dt>&quot;md5&quot;</p>
<dd>Not documented</p>
<dt>&quot;sha1&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>SshHostKeyHash</code> (Object) <tt>&quot;type&quot;</tt> The hash algorithm used for the hash <tt>&quot;hash&quot;</tt> The expected hash value <code>Members:</code></p>
<dl>
<dt>&quot;type: SshHostKeyCheckHashType&quot;</p>
<dd>Not documented</p>
<dt>&quot;hash: string&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>SshHostKeyCheck</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;mode: SshHostKeyCheckMode&quot;</p>
<dd>Not documented</p>
<dt>The members of &quot;SshHostKeyHash&quot; when &quot;mode&quot; is &quot;hash&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.12 <code>BlockdevOptionsSsh</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;server: InetSocketAddress&quot;</p>
<dd>host address</p>
<dt>&quot;path: string&quot;</p>
<dd>path to the image on the host</p>
<dt>&quot;user: string&quot; (optional)</p>
<dd>user as which to connect, defaults to current local user name</p>
<dt>&quot;host-key-check: SshHostKeyCheck&quot; (optional)</p>
<dd>Defines how and what to check the host key against (default: known_hosts)</dl>
<p> <code>Since:</code> 2.9 <code>BlkdebugEvent</code> (Enum) Trigger events supported by blkdebug. <code>Values:</code></p>
<dl>
<dt>&quot;l1_shrink_write_table&quot;</p>
<dd>write zeros to the l1 table to shrink image. (since 2.11)</p>
<dt>&quot;l1_shrink_free_l2_clusters&quot;</p>
<dd>discard the l2 tables. (since 2.11)</p>
<dt>&quot;cor_write&quot;</p>
<dd>a write due to copy-on-read (since 2.11)</p>
<dt>&quot;cluster_alloc_space&quot;</p>
<dd>an allocation of file space for a cluster (since 4.1)</p>
<dt>&quot;none&quot;</p>
<dd>triggers once at creation of the blkdebug node (since 4.1)</p>
<dt>&quot;l1_update&quot;</p>
<dd>Not documented</p>
<dt>&quot;l1_grow_alloc_table&quot;</p>
<dd>Not documented</p>
<dt>&quot;l1_grow_write_table&quot;</p>
<dd>Not documented</p>
<dt>&quot;l1_grow_activate_table&quot;</p>
<dd>Not documented</p>
<dt>&quot;l2_load&quot;</p>
<dd>Not documented</p>
<dt>&quot;l2_update&quot;</p>
<dd>Not documented</p>
<dt>&quot;l2_update_compressed&quot;</p>
<dd>Not documented</p>
<dt>&quot;l2_alloc_cow_read&quot;</p>
<dd>Not documented</p>
<dt>&quot;l2_alloc_write&quot;</p>
<dd>Not documented</p>
<dt>&quot;read_aio&quot;</p>
<dd>Not documented</p>
<dt>&quot;read_backing_aio&quot;</p>
<dd>Not documented</p>
<dt>&quot;read_compressed&quot;</p>
<dd>Not documented</p>
<dt>&quot;write_aio&quot;</p>
<dd>Not documented</p>
<dt>&quot;write_compressed&quot;</p>
<dd>Not documented</p>
<dt>&quot;vmstate_load&quot;</p>
<dd>Not documented</p>
<dt>&quot;vmstate_save&quot;</p>
<dd>Not documented</p>
<dt>&quot;cow_read&quot;</p>
<dd>Not documented</p>
<dt>&quot;cow_write&quot;</p>
<dd>Not documented</p>
<dt>&quot;reftable_load&quot;</p>
<dd>Not documented</p>
<dt>&quot;reftable_grow&quot;</p>
<dd>Not documented</p>
<dt>&quot;reftable_update&quot;</p>
<dd>Not documented</p>
<dt>&quot;refblock_load&quot;</p>
<dd>Not documented</p>
<dt>&quot;refblock_update&quot;</p>
<dd>Not documented</p>
<dt>&quot;refblock_update_part&quot;</p>
<dd>Not documented</p>
<dt>&quot;refblock_alloc&quot;</p>
<dd>Not documented</p>
<dt>&quot;refblock_alloc_hookup&quot;</p>
<dd>Not documented</p>
<dt>&quot;refblock_alloc_write&quot;</p>
<dd>Not documented</p>
<dt>&quot;refblock_alloc_write_blocks&quot;</p>
<dd>Not documented</p>
<dt>&quot;refblock_alloc_write_table&quot;</p>
<dd>Not documented</p>
<dt>&quot;refblock_alloc_switch_table&quot;</p>
<dd>Not documented</p>
<dt>&quot;cluster_alloc&quot;</p>
<dd>Not documented</p>
<dt>&quot;cluster_alloc_bytes&quot;</p>
<dd>Not documented</p>
<dt>&quot;cluster_free&quot;</p>
<dd>Not documented</p>
<dt>&quot;flush_to_os&quot;</p>
<dd>Not documented</p>
<dt>&quot;flush_to_disk&quot;</p>
<dd>Not documented</p>
<dt>&quot;pwritev_rmw_head&quot;</p>
<dd>Not documented</p>
<dt>&quot;pwritev_rmw_after_head&quot;</p>
<dd>Not documented</p>
<dt>&quot;pwritev_rmw_tail&quot;</p>
<dd>Not documented</p>
<dt>&quot;pwritev_rmw_after_tail&quot;</p>
<dd>Not documented</p>
<dt>&quot;pwritev&quot;</p>
<dd>Not documented</p>
<dt>&quot;pwritev_zero&quot;</p>
<dd>Not documented</p>
<dt>&quot;pwritev_done&quot;</p>
<dd>Not documented</p>
<dt>&quot;empty_image_prepare&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.9 <code>BlkdebugIOType</code> (Enum) Kinds of I/O that blkdebug can inject errors in. <code>Values:</code></p>
<dl>
<dt>&quot;read&quot;</p>
<dd>.<code>bdrv_co_preadv()</code></p>
<dt>&quot;write&quot;</p>
<dd>.<code>bdrv_co_pwritev()</code></p>
<dt>&quot;write-zeroes&quot;</p>
<dd>.<code>bdrv_co_pwrite_zeroes()</code></p>
<dt>&quot;discard&quot;</p>
<dd>.<code>bdrv_co_pdiscard()</code></p>
<dt>&quot;flush&quot;</p>
<dd>.<code>bdrv_co_flush_to_disk()</code></p>
<dt>&quot;block-status&quot;</p>
<dd>.<code>bdrv_co_block_status()</code></dl>
<p> <code>Since:</code> 4.1 <code>BlkdebugInjectErrorOptions</code> (Object) Describes a single error injection for blkdebug. <code>Members:</code></p>
<dl>
<dt>&quot;event: BlkdebugEvent&quot;</p>
<dd>trigger event</p>
<dt>&quot;state: int&quot; (optional)</p>
<dd>the state identifier blkdebug needs to be in to actually trigger the event; defaults to &#8220;any&#8221;</p>
<dt>&quot;iotype: BlkdebugIOType&quot; (optional)</p>
<dd>the type of I/O operations on which this error should be injected; defaults to &#8220;all read, write, write-zeroes, discard, and flush operations&#8221; (since: 4.1)</p>
<dt>&quot;errno: int&quot; (optional)</p>
<dd>error identifier (errno) to be returned; defaults to <font SIZE="-1">EIO</font></p>
<dt>&quot;sector: int&quot; (optional)</p>
<dd>specifies the sector index which has to be affected in order to actually trigger the event; defaults to &#8220;any sector&#8221;</p>
<dt>&quot;once: boolean&quot; (optional)</p>
<dd>disables further events after this one has been triggered; defaults to false</p>
<dt>&quot;immediately: boolean&quot; (optional)</p>
<dd>fail immediately; defaults to false</dl>
<p> <code>Since:</code> 2.9 <code>BlkdebugSetStateOptions</code> (Object) Describes a single state-change event for blkdebug. <code>Members:</code></p>
<dl>
<dt>&quot;event: BlkdebugEvent&quot;</p>
<dd>trigger event</p>
<dt>&quot;state: int&quot; (optional)</p>
<dd>the current state identifier blkdebug needs to be in; defaults to &#8220;any&#8221;</p>
<dt>&quot;new_state: int&quot;</p>
<dd>the state identifier blkdebug is supposed to assume if this event is triggered</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsBlkdebug</code> (Object) Driver specific block device options for blkdebug. <code>Members:</code></p>
<dl>
<dt>&quot;image: BlockdevRef&quot;</p>
<dd>underlying raw block device (or image file)</p>
<dt>&quot;config: string&quot; (optional)</p>
<dd>filename of the configuration file</p>
<dt>&quot;align: int&quot; (optional)</p>
<dd>required alignment for requests in bytes, must be positive power of 2, or 0 for default</p>
<dt>&quot;max-transfer: int&quot; (optional)</p>
<dd>maximum size for I/O transfers in bytes, must be positive multiple of <tt>&quot;align&quot;</tt> and of the underlying file&#8217;s request alignment (but need not be a power of 2), or 0 for default (since 2.10)</p>
<dt>&quot;opt-write-zero: int&quot; (optional)</p>
<dd>preferred alignment for write zero requests in bytes, must be positive multiple of <tt>&quot;align&quot;</tt> and of the underlying file&#8217;s request alignment (but need not be a power of 2), or 0 for default (since 2.10)</p>
<dt>&quot;max-write-zero: int&quot; (optional)</p>
<dd>maximum size for write zero requests in bytes, must be positive multiple of <tt>&quot;align&quot;</tt>, of <tt>&quot;opt-write-zero&quot;</tt>, and of the underlying file&#8217;s request alignment (but need not be a power of 2), or 0 for default (since 2.10)</p>
<dt>&quot;opt-discard: int&quot; (optional)</p>
<dd>preferred alignment for discard requests in bytes, must be positive multiple of <tt>&quot;align&quot;</tt> and of the underlying file&#8217;s request alignment (but need not be a power of 2), or 0 for default (since 2.10)</p>
<dt>&quot;max-discard: int&quot; (optional)</p>
<dd>maximum size for discard requests in bytes, must be positive multiple of <tt>&quot;align&quot;</tt>, of <tt>&quot;opt-discard&quot;</tt>, and of the underlying file&#8217;s request alignment (but need not be a power of 2), or 0 for default (since 2.10)</p>
<dt>&quot;inject-error: array of BlkdebugInjectErrorOptions&quot; (optional)</p>
<dd>array of error injection descriptions</p>
<dt>&quot;set-state: array of BlkdebugSetStateOptions&quot; (optional)</p>
<dd>array of state-change descriptions</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsBlklogwrites</code> (Object) Driver specific block device options for blklogwrites. <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>block device</p>
<dt>&quot;log: BlockdevRef&quot;</p>
<dd>block device used to log writes to <tt>&quot;file&quot;</tt></p>
<dt>&quot;log-sector-size: int&quot; (optional)</p>
<dd>sector size used in logging writes to <tt>&quot;file&quot;</tt>, determines granularity of offsets and sizes of writes (default: 512)</p>
<dt>&quot;log-append: boolean&quot; (optional)</p>
<dd>append to an existing log (default: false)</p>
<dt>&quot;log-super-update-interval: int&quot; (optional)</p>
<dd>interval of write requests after which the log super block is updated to disk (default: 4096)</dl>
<p> <code>Since:</code> 3.0 <code>BlockdevOptionsBlkverify</code> (Object) Driver specific block device options for blkverify. <code>Members:</code></p>
<dl>
<dt>&quot;test: BlockdevRef&quot;</p>
<dd>block device to be tested</p>
<dt>&quot;raw: BlockdevRef&quot;</p>
<dd>raw image used for verification</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsBlkreplay</code> (Object) Driver specific block device options for blkreplay. <code>Members:</code></p>
<dl>
<dt>&quot;image: BlockdevRef&quot;</p>
<dd>disk image which should be controlled with blkreplay</dl>
<p> <code>Since:</code> 4.2 <code>QuorumReadPattern</code> (Enum) An enumeration of quorum read patterns. <code>Values:</code></p>
<dl>
<dt>&quot;quorum&quot;</p>
<dd>read all the children and do a quorum vote on reads</p>
<dt>&quot;fifo&quot;</p>
<dd>read only from the first child that has not failed</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsQuorum</code> (Object) Driver specific block device options for Quorum <code>Members:</code></p>
<dl>
<dt>&quot;blkverify: boolean&quot; (optional)</p>
<dd>true if the driver must print content mismatch set to false by default</p>
<dt>&quot;children: array of BlockdevRef&quot;</p>
<dd>the children block devices to use</p>
<dt>&quot;vote-threshold: int&quot;</p>
<dd>the vote limit under which a read will fail</p>
<dt>&quot;rewrite-corrupted: boolean&quot; (optional)</p>
<dd>rewrite corrupted data when quorum is reached (Since 2.1)</p>
<dt>&quot;read-pattern: QuorumReadPattern&quot; (optional)</p>
<dd>choose read pattern and set to quorum by default (Since 2.2)</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsGluster</code> (Object) Driver specific block device options for Gluster <code>Members:</code></p>
<dl>
<dt>&quot;volume: string&quot;</p>
<dd>name of gluster volume where <font SIZE="-1">VM</font> image resides</p>
<dt>&quot;path: string&quot;</p>
<dd>absolute path to image file in gluster volume</p>
<dt>&quot;server: array of SocketAddress&quot;</p>
<dd>gluster servers description</p>
<dt>&quot;debug: int&quot; (optional)</p>
<dd>libgfapi log level (default &#8216;4&#8217; which is Error) (Since 2.8)</p>
<dt>&quot;logfile: string&quot; (optional)</p>
<dd>libgfapi log file (default /dev/stderr) (Since 2.8)</dl>
<p> <code>Since:</code> 2.9 <code>IscsiTransport</code> (Enum) An enumeration of libiscsi transport types <code>Values:</code></p>
<dl>
<dt>&quot;tcp&quot;</p>
<dd>Not documented</p>
<dt>&quot;iser&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.9 <code>IscsiHeaderDigest</code> (Enum) An enumeration of header digests supported by libiscsi <code>Values:</code></p>
<dl>
<dt>&quot;crc32c&quot;</p>
<dd>Not documented</p>
<dt>&quot;none&quot;</p>
<dd>Not documented</p>
<dt>&quot;crc32c-none&quot;</p>
<dd>Not documented</p>
<dt>&quot;none-crc32c&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsIscsi</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;transport: IscsiTransport&quot;</p>
<dd>The iscsi transport type</p>
<dt>&quot;portal: string&quot;</p>
<dd>The address of the iscsi portal</p>
<dt>&quot;target: string&quot;</p>
<dd>The target iqn name</p>
<dt>&quot;lun: int&quot; (optional)</p>
<dd><font SIZE="-1">LUN</font> to connect to. Defaults to 0.</p>
<dt>&quot;user: string&quot; (optional)</p>
<dd>User name to log in with. If omitted, no <font SIZE="-1">CHAP</font> authentication is performed.</p>
<dt>&quot;password-secret: string&quot; (optional)</p>
<dd>The <font SIZE="-1">ID</font> of a QCryptoSecret object providing the password for the login. This option is required if <tt>&quot;user&quot;</tt> is specified.</p>
<dt>&quot;initiator-name: string&quot; (optional)</p>
<dd>The iqn name we want to identify to the target as. If this option is not specified, an initiator name is generated automatically.</p>
<dt>&quot;header-digest: IscsiHeaderDigest&quot; (optional)</p>
<dd>The desired header digest. Defaults to none-crc32c.</p>
<dt>&quot;timeout: int&quot; (optional)</p>
<dd>Timeout in seconds after which a request will timeout. 0 means no timeout and is the default.</dl>
<p> Driver specific block device options for iscsi <code>Since:</code> 2.9 <code>RbdAuthMode</code> (Enum) <code>Values:</code></p>
<dl>
<dt>&quot;cephx&quot;</p>
<dd>Not documented</p>
<dt>&quot;none&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 3.0 <code>BlockdevOptionsRbd</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;pool: string&quot;</p>
<dd>Ceph pool name.</p>
<dt>&quot;image: string&quot;</p>
<dd>Image name in the Ceph pool.</p>
<dt>&quot;conf: string&quot; (optional)</p>
<dd>path to Ceph configuration file. Values in the configuration file will be overridden by options specified via <font SIZE="-1">QAPI.</font></p>
<dt>&quot;snapshot: string&quot; (optional)</p>
<dd>Ceph snapshot name.</p>
<dt>&quot;user: string&quot; (optional)</p>
<dd>Ceph id name.</p>
<dt>&quot;auth-client-required: array of RbdAuthMode&quot; (optional)</p>
<dd>Acceptable authentication modes. This maps to Ceph configuration option &#8220;auth_client_required&#8221;. (Since 3.0)</p>
<dt>&quot;key-secret: string&quot; (optional)</p>
<dd><font SIZE="-1">ID</font> of a QCryptoSecret object providing a key for cephx authentication. This maps to Ceph configuration option &#8220;key&#8221;. (Since 3.0)</p>
<dt>&quot;server: array of InetSocketAddressBase&quot; (optional)</p>
<dd>Monitor host address and port. This maps to the &#8220;mon_host&#8221; Ceph option.</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsSheepdog</code> (Object) Driver specific block device options for sheepdog <code>Members:</code></p>
<dl>
<dt>&quot;vdi: string&quot;</p>
<dd>Virtual disk image name</p>
<dt>&quot;server: SocketAddress&quot;</p>
<dd>The Sheepdog server to connect to</p>
<dt>&quot;snap-id: int&quot; (optional)</p>
<dd>Snapshot <font SIZE="-1">ID</font></p>
<dt>&quot;tag: string&quot; (optional)</p>
<dd>Snapshot tag name</dl>
<p> Only one of <tt>&quot;snap-id&quot;</tt> and <tt>&quot;tag&quot;</tt> may be present. <code>Since:</code> 2.9 <code>ReplicationMode</code> (Enum) An enumeration of replication modes. <code>Values:</code></p>
<dl>
<dt>&quot;primary&quot;</p>
<dd>Primary mode, the vm&#8217;s state will be sent to secondary <font SIZE="-1">QEMU.</font></p>
<dt>&quot;secondary&quot;</p>
<dd>Secondary mode, receive the vm&#8217;s state from primary <font SIZE="-1">QEMU.</font></dl>
<p> <code>Since:</code> 2.9 <code>If:</code> <tt>&quot;defined(CONFIG_REPLICATION)&quot;</tt> <code>BlockdevOptionsReplication</code> (Object) Driver specific block device options for replication <code>Members:</code></p>
<dl>
<dt>&quot;mode: ReplicationMode&quot;</p>
<dd>the replication mode</p>
<dt>&quot;top-id: string&quot; (optional)</p>
<dd>In secondary mode, node name or device <font SIZE="-1">ID</font> of the root node who owns the replication node chain. Must not be given in primary mode.</p>
<dt>The members of &quot;BlockdevOptionsGenericFormat&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.9 <code>If:</code> <tt>&quot;defined(CONFIG_REPLICATION)&quot;</tt> <code>NFSTransport</code> (Enum) An enumeration of <font SIZE="-1">NFS</font> transport types <code>Values:</code></p>
<dl>
<dt>&quot;inet&quot;</p>
<dd><font SIZE="-1">TCP</font> transport</dl>
<p> <code>Since:</code> 2.9 <code>NFSServer</code> (Object) Captures the address of the socket <code>Members:</code></p>
<dl>
<dt>&quot;type: NFSTransport&quot;</p>
<dd>transport type used for <font SIZE="-1">NFS</font> (only <font SIZE="-1">TCP</font> supported)</p>
<dt>&quot;host: string&quot;</p>
<dd>host address for <font SIZE="-1">NFS</font> server</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsNfs</code> (Object) Driver specific block device option for <font SIZE="-1">NFS</font> <code>Members:</code></p>
<dl>
<dt>&quot;server: NFSServer&quot;</p>
<dd>host address</p>
<dt>&quot;path: string&quot;</p>
<dd>path of the image on the host</p>
<dt>&quot;user: int&quot; (optional)</p>
<dd><font SIZE="-1">UID</font> value to use when talking to the server (defaults to 65534 on Windows and <code>getuid()</code> on unix)</p>
<dt>&quot;group: int&quot; (optional)</p>
<dd><font SIZE="-1">GID</font> value to use when talking to the server (defaults to 65534 on Windows and <code>getgid()</code> in unix)</p>
<dt>&quot;tcp-syn-count: int&quot; (optional)</p>
<dd>number of SYNs during the session establishment (defaults to libnfs default)</p>
<dt>&quot;readahead-size: int&quot; (optional)</p>
<dd>set the readahead size in bytes (defaults to libnfs default)</p>
<dt>&quot;page-cache-size: int&quot; (optional)</p>
<dd>set the pagecache size in bytes (defaults to libnfs default)</p>
<dt>&quot;debug: int&quot; (optional)</p>
<dd>set the <font SIZE="-1">NFS</font> debug level (max 2) (defaults to libnfs default)</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsCurlBase</code> (Object) Driver specific block device options shared by all protocols supported by the curl backend. <code>Members:</code></p>
<dl>
<dt>&quot;url: string&quot;</p>
<dd><font SIZE="-1">URL</font> of the image file</p>
<dt>&quot;readahead: int&quot; (optional)</p>
<dd>Size of the read-ahead cache; must be a multiple of 512 (defaults to 256 kB)</p>
<dt>&quot;timeout: int&quot; (optional)</p>
<dd>Timeout for connections, in seconds (defaults to 5)</p>
<dt>&quot;username: string&quot; (optional)</p>
<dd>Username for authentication (defaults to none)</p>
<dt>&quot;password-secret: string&quot; (optional)</p>
<dd><font SIZE="-1">ID</font> of a QCryptoSecret object providing a password for authentication (defaults to no password)</p>
<dt>&quot;proxy-username: string&quot; (optional)</p>
<dd>Username for proxy authentication (defaults to none)</p>
<dt>&quot;proxy-password-secret: string&quot; (optional)</p>
<dd><font SIZE="-1">ID</font> of a QCryptoSecret object providing a password for proxy authentication (defaults to no password)</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsCurlHttp</code> (Object) Driver specific block device options for <font SIZE="-1">HTTP</font> connections over the curl backend. URLs must start with &#8220;<a rel="nofollow" href="http://''.">http://&#8221;.</a> Members :</p>
<p>    &quot;cookie: string&quot;(optional)</p>
<p>        List of cookies to set;<br />
format is<br />
&#8220;name1 = content1;<br />
name2 = content2;&#8221; as explained by<br />
CURLOPT_COOKIE(3). Defaults to no cookies.<br />
&quot;cookie-secret: string&quot; (optional)</p>
<p>ID of a QCryptoSecret object providing the cookie data in a<br />
secure way. See &quot;cookie&quot; for the format. (since 2.10)<br />
The members of &quot;BlockdevOptionsCurlBase&quot; <code>Since:</code> 2.9 <code>BlockdevOptionsCurlHttps</code> (Object) Driver specific block device options for <font SIZE="-1">HTTPS</font> connections over the curl backend. URLs must start with &#8220;<a rel="nofollow" href="https://''.">https://&#8221;.</a> Members :</p>
<p>    &quot;cookie: string&quot;(optional)</p>
<p>        List of cookies to set;<br />
format is<br />
&#8220;name1 = content1;<br />
name2 = content2;&#8221; as explained by<br />
CURLOPT_COOKIE(3). Defaults to no cookies.<br />
&quot;sslverify: boolean&quot; (optional)</p>
<p>Whether to verify the SSL certificate&#8217;s validity (defaults to<br />
true)<br />
&quot;cookie-secret: string&quot; (optional)</p>
<p>ID of a QCryptoSecret object providing the cookie data in a<br />
secure way. See &quot;cookie&quot; for the format. (since 2.10)<br />
The members of &quot;BlockdevOptionsCurlBase&quot; <code>Since:</code> 2.9 <code>BlockdevOptionsCurlFtp</code> (Object) Driver specific block device options for <font SIZE="-1">FTP</font> connections over the curl backend. URLs must start with &#8220;<a href="ftp://''.">ftp://&#8221;.</a> <code>Members:</code></p>
<dl>
<dt>The members of &quot;BlockdevOptionsCurlBase&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsCurlFtps</code> (Object) Driver specific block device options for <font SIZE="-1">FTPS</font> connections over the curl backend. URLs must start with &#8220;<a href="ftps://''.">ftps://&#8221;.</a> <code>Members:</code></p>
<dl>
<dt>&quot;sslverify: boolean&quot; (optional)</p>
<dd>Whether to verify the <font SIZE="-1">SSL</font> certificate&#8217;s validity (defaults to true)</p>
<dt>The members of &quot;BlockdevOptionsCurlBase&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsNbd</code> (Object) Driver specific block device options for <font SIZE="-1">NBD.</font> <code>Members:</code></p>
<dl>
<dt>&quot;server: SocketAddress&quot;</p>
<dd><font SIZE="-1">NBD</font> server address</p>
<dt>&quot;export: string&quot; (optional)</p>
<dd>export name</p>
<dt>&quot;tls-creds: string&quot; (optional)</p>
<dd><font SIZE="-1">TLS</font> credentials <font SIZE="-1">ID</font></p>
<dt>&quot;x-dirty-bitmap: string&quot; (optional)</p>
<dd>A &#8220;qemu:dirty-bitmap:NAME&#8221; string to query in place of traditional &#8220;base:allocation&#8221; block status (see <font SIZE="-1">NBD_OPT_LIST_META_CONTEXT</font> in the <font SIZE="-1">NBD</font> protocol) (since 3.0)</p>
<dt>&quot;reconnect-delay: int&quot; (optional)</p>
<dd>On an unexpected disconnect, the nbd client tries to connect again until succeeding or encountering a serious error. During the first <tt>&quot;reconnect-delay&quot;</tt> seconds, all requests are paused and will be rerun on a successful reconnect. After that time, any delayed requests and all future requests before a successful reconnect will immediately fail. Default 0 (Since 4.2)</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsRaw</code> (Object) Driver specific block device options for the raw driver. <code>Members:</code></p>
<dl>
<dt>&quot;offset: int&quot; (optional)</p>
<dd>position where the block device starts</p>
<dt>&quot;size: int&quot; (optional)</p>
<dd>the assumed size of the device</p>
<dt>The members of &quot;BlockdevOptionsGenericFormat&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.9 <code>BlockdevOptionsVxHS</code> (Object) Driver specific block device options for VxHS <code>Members:</code></p>
<dl>
<dt>&quot;vdisk-id: string&quot;</p>
<dd><font SIZE="-1">UUID</font> of VxHS volume</p>
<dt>&quot;server: InetSocketAddressBase&quot;</p>
<dd>vxhs server <font SIZE="-1">IP,</font> port</p>
<dt>&quot;tls-creds: string&quot; (optional)</p>
<dd><font SIZE="-1">TLS</font> credentials <font SIZE="-1">ID</font></dl>
<p> <code>Since:</code> 2.10 <code>BlockdevOptionsThrottle</code> (Object) Driver specific block device options for the throttle driver <code>Members:</code></p>
<dl>
<dt>&quot;throttle-group: string&quot;</p>
<dd>the name of the throttle-group object to use. It must already exist.</p>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>reference to or definition of the data source block device</dl>
<p> <code>Since:</code> 2.11 <code>BlockdevOptions</code> (Object) Options for creating a block device. Many options are available for all block devices, independent of the block driver: Members:</p>
<p>&quot;driver: BlockdevDriver&quot;</p>
<p>block driver name<br />
&quot;node-name: string&quot; (optional)</p>
<p>the node name of the new node (Since 2.0).<br />
This option is required on the top level of blockdev-add.<br />
Valid node names start with an alphabetic character and may<br />
contain only alphanumeric characters, &#8216;-&#8216;, &#8216;.&#8217; and &#8216;_&#8217;. Their<br />
maximum length is 31 characters.<br />
&quot;discard: BlockdevDiscardOptions&quot; (optional)</p>
<p>discard-related options (default: ignore)<br />
&quot;cache: BlockdevCacheOptions&quot; (optional)</p>
<p>cache-related options<br />
&quot;read-only: boolean&quot; (optional)</p>
<p>whether the block device should be read-only (default: false).<br />
Note that some block drivers support only read-only access,<br />
either generally or in certain configurations. In this case,<br />
the default value does not work and the option must be<br />
specified explicitly.<br />
&quot;auto-read-only: boolean&quot; (optional)</p>
<p>if true and &quot;read-only&quot; is false, QEMU may automatically<br />
decide not to open the image read-write as requested, but<br />
fall back to read-only instead (and switch between the modes<br />
later), e.g. depending on whether the image file is writable<br />
or whether a writing user is attached to the node<br />
(default: false, since 3.1)<br />
&quot;detect-zeroes: BlockdevDetectZeroesOptions&quot; (optional)</p>
<p>detect and optimize zero writes (Since 2.1)<br />
(default: off)<br />
&quot;force-share: boolean&quot; (optional)</p>
<p>force share all permission on added nodes.<br />
Requires read-only=true. (Since 2.10)<br />
The members of &quot;BlockdevOptionsBlkdebug&quot; when &quot;driver&quot; is &quot;blkdebug&quot;</p>
<p>The members of &quot;BlockdevOptionsBlklogwrites&quot; when &quot;driver&quot; is &quot;blklogwrites&quot;</p>
<p>The members of &quot;BlockdevOptionsBlkverify&quot; when &quot;driver&quot; is &quot;blkverify&quot;</p>
<p>The members of &quot;BlockdevOptionsBlkreplay&quot; when &quot;driver&quot; is &quot;blkreplay&quot;</p>
<p>The members of &quot;BlockdevOptionsGenericFormat&quot; when &quot;driver&quot; is &quot;bochs&quot;</p>
<p>The members of &quot;BlockdevOptionsGenericFormat&quot; when &quot;driver&quot; is &quot;cloop&quot;</p>
<p>The members of &quot;BlockdevOptionsGenericFormat&quot; when &quot;driver&quot; is &quot;copy-on-read&quot;</p>
<p>The members of &quot;BlockdevOptionsGenericFormat&quot; when &quot;driver&quot; is &quot;dmg&quot;</p>
<p>The members of &quot;BlockdevOptionsFile&quot; when &quot;driver&quot; is &quot;file&quot;</p>
<p>The members of &quot;BlockdevOptionsCurlFtp&quot; when &quot;driver&quot; is &quot;ftp&quot;</p>
<p>The members of &quot;BlockdevOptionsCurlFtps&quot; when &quot;driver&quot; is &quot;ftps&quot;</p>
<p>The members of &quot;BlockdevOptionsGluster&quot; when &quot;driver&quot; is &quot;gluster&quot;</p>
<p>The members of &quot;BlockdevOptionsFile&quot; when &quot;driver&quot; is &quot;host_cdrom&quot;</p>
<p>The members of &quot;BlockdevOptionsFile&quot; when &quot;driver&quot; is &quot;host_device&quot;</p>
<p>The members of &quot;BlockdevOptionsCurlHttp&quot; when &quot;driver&quot; is &quot;http&quot;</p>
<p>The members of &quot;BlockdevOptionsCurlHttps&quot; when &quot;driver&quot; is &quot;https&quot;</p>
<p>The members of &quot;BlockdevOptionsIscsi&quot; when &quot;driver&quot; is &quot;iscsi&quot;</p>
<p>The members of &quot;BlockdevOptionsLUKS&quot; when &quot;driver&quot; is &quot;luks&quot;</p>
<p>The members of &quot;BlockdevOptionsNbd&quot; when &quot;driver&quot; is &quot;nbd&quot;</p>
<p>The members of &quot;BlockdevOptionsNfs&quot; when &quot;driver&quot; is &quot;nfs&quot;</p>
<p>The members of &quot;BlockdevOptionsNull&quot; when &quot;driver&quot; is &quot;null-aio&quot;</p>
<p>The members of &quot;BlockdevOptionsNull&quot; when &quot;driver&quot; is &quot;null-co&quot;</p>
<p>The members of &quot;BlockdevOptionsNVMe&quot; when &quot;driver&quot; is &quot;nvme&quot;</p>
<p>The members of &quot;BlockdevOptionsGenericFormat&quot; when &quot;driver&quot; is &quot;parallels&quot;</p>
<p>The members of &quot;BlockdevOptionsQcow2&quot; when &quot;driver&quot; is &quot;qcow2&quot;</p>
<p>The members of &quot;BlockdevOptionsQcow&quot; when &quot;driver&quot; is &quot;qcow&quot;</p>
<p>The members of &quot;BlockdevOptionsGenericCOWFormat&quot; when &quot;driver&quot; is &quot;qed&quot;</p>
<p>The members of &quot;BlockdevOptionsQuorum&quot; when &quot;driver&quot; is &quot;quorum&quot;</p>
<p>The members of &quot;BlockdevOptionsRaw&quot; when &quot;driver&quot; is &quot;raw&quot;</p>
<p>The members of &quot;BlockdevOptionsRbd&quot; when &quot;driver&quot; is &quot;rbd&quot;</p>
<p>The members of &quot;BlockdevOptionsReplication&quot; when &quot;driver&quot; is &quot;replication&quot; (If: &quot;defined(CONFIG_REPLICATION)&quot;)</p>
<p>The members of &quot;BlockdevOptionsSheepdog&quot; when &quot;driver&quot; is &quot;sheepdog&quot;</p>
<p>The members of &quot;BlockdevOptionsSsh&quot; when &quot;driver&quot; is &quot;ssh&quot;</p>
<p>The members of &quot;BlockdevOptionsThrottle&quot; when &quot;driver&quot; is &quot;throttle&quot;</p>
<p>The members of &quot;BlockdevOptionsGenericFormat&quot; when &quot;driver&quot; is &quot;vdi&quot;</p>
<p>The members of &quot;BlockdevOptionsGenericFormat&quot; when &quot;driver&quot; is &quot;vhdx&quot;</p>
<p>The members of &quot;BlockdevOptionsGenericCOWFormat&quot; when &quot;driver&quot; is &quot;vmdk&quot;</p>
<p>The members of &quot;BlockdevOptionsGenericFormat&quot; when &quot;driver&quot; is &quot;vpc&quot;</p>
<p>The members of &quot;BlockdevOptionsVVFAT&quot; when &quot;driver&quot; is &quot;vvfat&quot;</p>
<p>The members of &quot;BlockdevOptionsVxHS&quot; when &quot;driver&quot; is &quot;vxhs&quot; Remaining options are determined by the block driver. <code>Since:</code> 2.9 <code>BlockdevRef</code> (Alternate) Reference to a block device. <code>Members:</code></p>
<dl>
<dt>&quot;definition: BlockdevOptions&quot;</p>
<dd>defines a new block device inline</p>
<dt>&quot;reference: string&quot;</p>
<dd>references the <font SIZE="-1">ID</font> of an existing block device</dl>
<p> <code>Since:</code> 2.9 <code>BlockdevRefOrNull</code> (Alternate) Reference to a block device. <code>Members:</code></p>
<dl>
<dt>&quot;definition: BlockdevOptions&quot;</p>
<dd>defines a new block device inline</p>
<dt>&quot;reference: string&quot;</p>
<dd>references the <font SIZE="-1">ID</font> of an existing block device. An empty string means that no block device should be referenced. Deprecated; use null instead.</p>
<dt>&quot;null: null&quot;</p>
<dd>No block device should be referenced (since 2.10)</dl>
<p> <code>Since:</code> 2.9 <code>blockdev-add</code> (Command) Creates a new block device. If the <tt>&quot;id&quot;</tt> option is given at the top level, a BlockBackend will be created; otherwise, <tt>&quot;node-name&quot;</tt> is mandatory at the top level and no BlockBackend will be created. <code>Arguments:</code> the members of <tt>&quot;BlockdevOptions&quot;</tt> <code>Since:</code> 2.9 <code>Example:</code> 1.<br />
        -&gt;{&quot;execute&quot; : &quot;blockdev-add&quot;,<br />
           &quot;arguments&quot; : {<br />
               &quot;driver&quot; : &quot;qcow2&quot;,<br />
               &quot;node-name&quot; : &quot;test1&quot;,<br />
               &quot;file&quot; : {<br />
                   &quot;driver&quot; : &quot;file&quot;,<br />
                   &quot;filename&quot; : &quot;test.qcow2&quot;<br />
               }<br />
           }} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
}</p>
<p>2.<br />
        -&gt;{&quot;execute&quot; : &quot;blockdev-add&quot;,<br />
           &quot;arguments&quot; : {<br />
               &quot;driver&quot; : &quot;qcow2&quot;,<br />
               &quot;node-name&quot; : &quot;node0&quot;,<br />
               &quot;discard&quot; : &quot;unmap&quot;,<br />
               &quot;cache&quot; : {<br />
                   &quot;direct&quot; : true<br />
               },<br />
               &quot;file&quot; : {<br />
                   &quot;driver&quot; : &quot;file&quot;,<br />
                   &quot;filename&quot; : &quot;/tmp/test.qcow2&quot;<br />
               },<br />
               &quot;backing&quot; : {<br />
                   &quot;driver&quot; : &quot;raw&quot;,<br />
                   &quot;file&quot; : {<br />
                       &quot;driver&quot; : &quot;file&quot;,<br />
                       &quot;filename&quot; : &quot;/dev/fdset/4&quot;<br />
                   }<br />
               }<br />
           }}</p>
<p>    &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>x-blockdev-reopen</code> (Command) Reopens a block device using the given set of options. Any option not specified will be reset to its default value regardless of its previous status. If an option cannot be changed or a particular driver does not support reopening then the command will return an error. The top-level <tt>&quot;node-name&quot;</tt> option (from BlockdevOptions) must be specified and is used to select the block device to be reopened. Other <tt>&quot;node-name&quot;</tt> options must be either omitted or set to the current name of the appropriate node. This command won&#8217;t change any node name and any attempt to do it will result in an error. In the case of options that refer to child nodes, the behavior of this command depends on the value: 1) A set of options (BlockdevOptions): the child is reopened with the specified set of options. 2) A reference to the current child: the child is reopened using its existing set of options. 3) A reference to a different node: the current child is replaced with the specified one. 4) <font SIZE="-1">NULL:</font> the current child (if any) is detached. Options (1) and (2) are supported in all cases, but at the moment only <tt>&quot;backing&quot;</tt> allows replacing or detaching an existing child. Unlike with blockdev-add, the <tt>&quot;backing&quot;</tt> option must always be present unless the node being reopened does not have a backing file and its image does not have a default backing file name as part of its metadata. <code>Arguments:</code> the members of <tt>&quot;BlockdevOptions&quot;</tt> <code>Since:</code> 4.0 <code>blockdev-del</code> (Command) Deletes a block device that has been added using blockdev-add. The command will fail if the node is attached to a device or is otherwise being used. <code>Arguments:</code></p>
<dl>
<dt>&quot;node-name: string&quot;</p>
<dd>Name of the graph node to delete.</dl>
<p> <code>Since:</code> 2.9 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-add&quot;,<br />
   &quot;arguments&quot; : {<br />
       &quot;driver&quot; : &quot;qcow2&quot;,<br />
       &quot;node-name&quot; : &quot;node0&quot;,<br />
       &quot;file&quot; : {<br />
           &quot;driver&quot; : &quot;file&quot;,<br />
           &quot;filename&quot; : &quot;test.qcow2&quot;<br />
       }<br />
   }} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
    }</p>
<p>        -&gt; {&quot;execute&quot; : &quot;blockdev-del&quot;,<br />
            &quot;arguments&quot; : {&quot;node-name&quot; : &quot;node0&quot;}} &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
    } <code>BlockdevCreateOptionsFile</code> (Object) Driver specific image creation options for file. <tt>&quot;filename&quot;</tt> Filename for the new image file <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;preallocation&quot;</tt> Preallocation mode for the new image (default: off; allowed values: off, falloc (if defined <font SIZE="-1">CONFIG_POSIX_FALLOCATE</font>), full (if defined <font SIZE="-1">CONFIG_POSIX</font>)) <tt>&quot;nocow&quot;</tt> Turn off copy-on-write (valid only on btrfs; default: off) <code>Members:</code></p>
<dl>
<dt>&quot;filename: string&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;preallocation: PreallocMode&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;nocow: boolean&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsGluster</code> (Object) Driver specific image creation options for gluster. <tt>&quot;location&quot;</tt> Where to store the new image file <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;preallocation&quot;</tt> Preallocation mode for the new image (default: off; allowed values: off, falloc (if defined <font SIZE="-1">CONFIG_GLUSTERFS_FALLOCATE</font>), full (if defined <font SIZE="-1">CONFIG_GLUSTERFS_ZEROFILL</font>)) <code>Members:</code></p>
<dl>
<dt>&quot;location: BlockdevOptionsGluster&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;preallocation: PreallocMode&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsLUKS</code> (Object) Driver specific image creation options for <font SIZE="-1">LUKS.</font> <tt>&quot;file&quot;</tt> Node to create the image format on <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;preallocation&quot;</tt> Preallocation mode for the new image (since: 4.2) (default: off; allowed values: off, metadata, falloc, full) <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;preallocation: PreallocMode&quot; (optional)</p>
<dd>Not documented</p>
<dt>The members of &quot;QCryptoBlockCreateOptionsLUKS&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsNfs</code> (Object) Driver specific image creation options for <font SIZE="-1">NFS.</font> <tt>&quot;location&quot;</tt> Where to store the new image file <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <code>Members:</code></p>
<dl>
<dt>&quot;location: BlockdevOptionsNfs&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsParallels</code> (Object) Driver specific image creation options for parallels. <tt>&quot;file&quot;</tt> Node to create the image format on <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;cluster-size&quot;</tt> Cluster size in bytes (default: 1 <font SIZE="-1">MB</font>) <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;cluster-size: int&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsQcow</code> (Object) Driver specific image creation options for qcow. <tt>&quot;file&quot;</tt> Node to create the image format on <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;backing-file&quot;</tt> File name of the backing file if a backing file should be used <tt>&quot;encrypt&quot;</tt> Encryption options if the image should be encrypted <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;backing-file: string&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;encrypt: QCryptoBlockCreateOptions&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevQcow2Version</code> (Enum) <code>Values:</code></p>
<dl>
<dt>&quot;v2&quot;</p>
<dd>The original <font SIZE="-1">QCOW2</font> format as introduced in qemu 0.10 (version 2)</p>
<dt>&quot;v3&quot;</p>
<dd>The extended <font SIZE="-1">QCOW2</font> format as introduced in qemu 1.1 (version 3)</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsQcow2</code> (Object) Driver specific image creation options for qcow2. <tt>&quot;file&quot;</tt> Node to create the image format on <tt>&quot;data-file&quot;</tt> Node to use as an external data file in which all guest data is stored so that only metadata remains in the qcow2 file (since: 4.0) <tt>&quot;data-file-raw&quot;</tt> True if the external data file must stay valid as a standalone (read-only) raw image without looking at qcow2 metadata (default: false; since: 4.0) <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;version&quot;</tt> Compatibility level (default: v3) <tt>&quot;backing-file&quot;</tt> File name of the backing file if a backing file should be used <tt>&quot;backing-fmt&quot;</tt> Name of the block driver to use for the backing file <tt>&quot;encrypt&quot;</tt> Encryption options if the image should be encrypted <tt>&quot;cluster-size&quot;</tt> qcow2 cluster size in bytes (default: 65536) <tt>&quot;preallocation&quot;</tt> Preallocation mode for the new image (default: off; allowed values: off, falloc, full, metadata) <tt>&quot;lazy-refcounts&quot;</tt> True if refcounts may be updated lazily (default: off) <tt>&quot;refcount-bits&quot;</tt> Width of reference counts in bits (default: 16) <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>Not documented</p>
<dt>&quot;data-file: BlockdevRef&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;data-file-raw: boolean&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;version: BlockdevQcow2Version&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;backing-file: string&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;backing-fmt: BlockdevDriver&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;encrypt: QCryptoBlockCreateOptions&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;cluster-size: int&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;preallocation: PreallocMode&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;lazy-refcounts: boolean&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;refcount-bits: int&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsQed</code> (Object) Driver specific image creation options for qed. <tt>&quot;file&quot;</tt> Node to create the image format on <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;backing-file&quot;</tt> File name of the backing file if a backing file should be used <tt>&quot;backing-fmt&quot;</tt> Name of the block driver to use for the backing file <tt>&quot;cluster-size&quot;</tt> Cluster size in bytes (default: 65536) <tt>&quot;table-size&quot;</tt> L1/L2 table size (in clusters) <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;backing-file: string&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;backing-fmt: BlockdevDriver&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;cluster-size: int&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;table-size: int&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsRbd</code> (Object) Driver specific image creation options for rbd/Ceph. <tt>&quot;location&quot;</tt> Where to store the new image file. This location cannot point to a snapshot. <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;cluster-size&quot;</tt> <font SIZE="-1">RBD</font> object size <code>Members:</code></p>
<dl>
<dt>&quot;location: BlockdevOptionsRbd&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;cluster-size: int&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevVmdkSubformat</code> (Enum) Subformat options for <font SIZE="-1">VMDK</font> images <code>Values:</code></p>
<dl>
<dt>&quot;monolithicSparse&quot;</p>
<dd>Single file image with sparse cluster allocation</p>
<dt>&quot;monolithicFlat&quot;</p>
<dd>Single flat data image and a descriptor file</p>
<dt>&quot;twoGbMaxExtentSparse&quot;</p>
<dd>Data is split into 2GB (per virtual <font SIZE="-1">LBA</font>) sparse extent files, in addition to a descriptor file</p>
<dt>&quot;twoGbMaxExtentFlat&quot;</p>
<dd>Data is split into 2GB (per virtual <font SIZE="-1">LBA</font>) flat extent files, in addition to a descriptor file</p>
<dt>&quot;streamOptimized&quot;</p>
<dd>Single file image sparse cluster allocation, optimized for streaming over network.</dl>
<p> <code>Since:</code> 4.0 <code>BlockdevVmdkAdapterType</code> (Enum) Adapter type info for <font SIZE="-1">VMDK</font> images <code>Values:</code></p>
<dl>
<dt>&quot;ide&quot;</p>
<dd>Not documented</p>
<dt>&quot;buslogic&quot;</p>
<dd>Not documented</p>
<dt>&quot;lsilogic&quot;</p>
<dd>Not documented</p>
<dt>&quot;legacyESX&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 4.0 <code>BlockdevCreateOptionsVmdk</code> (Object) Driver specific image creation options for <font SIZE="-1">VMDK.</font> <tt>&quot;file&quot;</tt> Where to store the new image file. This refers to the image file for monolithcSparse and streamOptimized format, or the descriptor file for other formats. <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;extents&quot;</tt> Where to store the data extents. Required for monolithcFlat, twoGbMaxExtentSparse and twoGbMaxExtentFlat formats. For monolithicFlat, only one entry is required; for twoGbMaxExtent* formats, the number of entries required is calculated as extent_number = virtual_size / 2GB. Providing more extents than will be used is an error. <tt>&quot;subformat&quot;</tt> The subformat of the <font SIZE="-1">VMDK</font> image. Default: &#8220;monolithicSparse&#8221;. <tt>&quot;backing-file&quot;</tt> The path of backing file. Default: no backing file is used. <tt>&quot;adapter-type&quot;</tt> The adapter type used to fill in the descriptor. Default: ide. <tt>&quot;hwversion&quot;</tt> Hardware version. The meaningful options are &#8220;4&#8221; or &#8220;6&#8221;. Default: &#8220;4&#8221;. <tt>&quot;zeroed-grain&quot;</tt> Whether to enable zeroed-grain feature for sparse subformats. Default: false. <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;extents: array of BlockdevRef&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;subformat: BlockdevVmdkSubformat&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;backing-file: string&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;adapter-type: BlockdevVmdkAdapterType&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;hwversion: string&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;zeroed-grain: boolean&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 4.0 <code>SheepdogRedundancyType</code> (Enum) <tt>&quot;full&quot;</tt> Create a fully replicated vdi with x copies <tt>&quot;erasure-coded&quot;</tt> Create an erasure coded vdi with x data strips and y parity strips <code>Values:</code></p>
<dl>
<dt>&quot;full&quot;</p>
<dd>Not documented</p>
<dt>&quot;erasure-coded&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>SheepdogRedundancyFull</code> (Object) <tt>&quot;copies&quot;</tt> Number of copies to use (between 1 and 31) <code>Members:</code></p>
<dl>
<dt>&quot;copies: int&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>SheepdogRedundancyErasureCoded</code> (Object) <tt>&quot;data-strips&quot;</tt> Number of data strips to use (one of {2,4,8,16}) <tt>&quot;parity-strips&quot;</tt> Number of parity strips to use (between 1 and 15) <code>Members:</code></p>
<dl>
<dt>&quot;data-strips: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;parity-strips: int&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>SheepdogRedundancy</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;type: SheepdogRedundancyType&quot;</p>
<dd>Not documented</p>
<dt>The members of &quot;SheepdogRedundancyFull&quot; when &quot;type&quot; is &quot;full&quot;</p>
<dd>
<dt>The members of &quot;SheepdogRedundancyErasureCoded&quot; when &quot;type&quot; is &quot;erasure-coded&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsSheepdog</code> (Object) Driver specific image creation options for Sheepdog. <tt>&quot;location&quot;</tt> Where to store the new image file <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;backing-file&quot;</tt> File name of a base image <tt>&quot;preallocation&quot;</tt> Preallocation mode for the new image (default: off; allowed values: off, full) <tt>&quot;redundancy&quot;</tt> Redundancy of the image <tt>&quot;object-size&quot;</tt> Object size of the image <code>Members:</code></p>
<dl>
<dt>&quot;location: BlockdevOptionsSheepdog&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;backing-file: string&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;preallocation: PreallocMode&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;redundancy: SheepdogRedundancy&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;object-size: int&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsSsh</code> (Object) Driver specific image creation options for <font SIZE="-1">SSH.</font> <tt>&quot;location&quot;</tt> Where to store the new image file <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <code>Members:</code></p>
<dl>
<dt>&quot;location: BlockdevOptionsSsh&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsVdi</code> (Object) Driver specific image creation options for <font SIZE="-1">VDI.</font> <tt>&quot;file&quot;</tt> Node to create the image format on <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;preallocation&quot;</tt> Preallocation mode for the new image (default: off; allowed values: off, metadata) <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;preallocation: PreallocMode&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevVhdxSubformat</code> (Enum) <code>Values:</code></p>
<dl>
<dt>&quot;dynamic&quot;</p>
<dd>Growing image file</p>
<dt>&quot;fixed&quot;</p>
<dd>Preallocated fixed-size image file</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsVhdx</code> (Object) Driver specific image creation options for vhdx. <tt>&quot;file&quot;</tt> Node to create the image format on <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;log-size&quot;</tt> Log size in bytes, must be a multiple of 1 <font SIZE="-1">MB</font> (default: 1 <font SIZE="-1">MB</font>) <tt>&quot;block-size&quot;</tt> Block size in bytes, must be a multiple of 1 <font SIZE="-1">MB</font> and not larger than 256 <font SIZE="-1">MB</font> (default: automatically choose a block size depending on the image size) <tt>&quot;subformat&quot;</tt> vhdx subformat (default: dynamic) <tt>&quot;block-state-zero&quot;</tt> Force use of payload blocks of type &#8216;<font SIZE="-1">ZERO</font>&#8216;. Non-standard, but default. Do not set to &#8216;off&#8217; when using &#8216;qemu-img convert&#8217; with subformat=dynamic. <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;log-size: int&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;block-size: int&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;subformat: BlockdevVhdxSubformat&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;block-state-zero: boolean&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevVpcSubformat</code> (Enum) <code>Values:</code></p>
<dl>
<dt>&quot;dynamic&quot;</p>
<dd>Growing image file</p>
<dt>&quot;fixed&quot;</p>
<dd>Preallocated fixed-size image file</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptionsVpc</code> (Object) Driver specific image creation options for vpc (<font SIZE="-1">VHD</font>). <tt>&quot;file&quot;</tt> Node to create the image format on <tt>&quot;size&quot;</tt> Size of the virtual disk in bytes <tt>&quot;subformat&quot;</tt> vhdx subformat (default: dynamic) <tt>&quot;force-size&quot;</tt> Force use of the exact byte size instead of rounding to the next size that can be represented in <font SIZE="-1">CHS</font> geometry (default: false) <code>Members:</code></p>
<dl>
<dt>&quot;file: BlockdevRef&quot;</p>
<dd>Not documented</p>
<dt>&quot;size: int&quot;</p>
<dd>Not documented</p>
<dt>&quot;subformat: BlockdevVpcSubformat&quot; (optional)</p>
<dd>Not documented</p>
<dt>&quot;force-size: boolean&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>BlockdevCreateOptions</code> (Object) Options for creating an image format on a given node. <tt>&quot;driver&quot;</tt> block driver to create the image format <code>Members:</code></p>
<dl>
<dt>&quot;driver: BlockdevDriver&quot;</p>
<dd>Not documented</p>
<dt>The members of &quot;BlockdevCreateOptionsFile&quot; when &quot;driver&quot; is &quot;file&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsGluster&quot; when &quot;driver&quot; is &quot;gluster&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsLUKS&quot; when &quot;driver&quot; is &quot;luks&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsNfs&quot; when &quot;driver&quot; is &quot;nfs&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsParallels&quot; when &quot;driver&quot; is &quot;parallels&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsQcow&quot; when &quot;driver&quot; is &quot;qcow&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsQcow2&quot; when &quot;driver&quot; is &quot;qcow2&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsQed&quot; when &quot;driver&quot; is &quot;qed&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsRbd&quot; when &quot;driver&quot; is &quot;rbd&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsSheepdog&quot; when &quot;driver&quot; is &quot;sheepdog&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsSsh&quot; when &quot;driver&quot; is &quot;ssh&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsVdi&quot; when &quot;driver&quot; is &quot;vdi&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsVhdx&quot; when &quot;driver&quot; is &quot;vhdx&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsVmdk&quot; when &quot;driver&quot; is &quot;vmdk&quot;</p>
<dd>
<dt>The members of &quot;BlockdevCreateOptionsVpc&quot; when &quot;driver&quot; is &quot;vpc&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.12 <code>blockdev-create</code> (Command) Starts a job to create an image format on a given node. The job is automatically finalized, but a manual job-dismiss is required. <code>Arguments:</code></p>
<dl>
<dt>&quot;job-id: string&quot;</p>
<dd>Identifier for the newly created job.</p>
<dt>&quot;options: BlockdevCreateOptions&quot;</p>
<dd>Options for the image creation.</dl>
<p> <code>Since:</code> 3.0 <code>blockdev-open-tray</code> (Command) Opens a block device&#8217;s tray. If there is a block driver state tree inserted as a medium, it will become inaccessible to the guest (but it will remain associated to the block device, so closing the tray will make it accessible again). If the tray was already open before, this will be a no-op. Once the tray opens, a <font SIZE="-1">DEVICE_TRAY_MOVED</font> event is emitted. There are cases in which no such event will be generated, these include:</p>
<dl>
<dt>&#8211;</p>
<dd>if the guest has locked the tray, <tt>&quot;force&quot;</tt> is false and the guest does not respond to the eject request</p>
<dt>&#8211;</p>
<dd>if the BlockBackend denoted by <tt>&quot;device&quot;</tt> does not have a guest device attached to it</p>
<dt>&#8211;</p>
<dd>if the guest device does not have an actual tray</dl>
<p> <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>Block device name (deprecated, use <tt>&quot;id&quot;</tt> instead)</p>
<dt>&quot;id: string&quot; (optional)</p>
<dd>The name or <font SIZE="-1">QOM</font> path of the guest device (since: 2.8)</p>
<dt>&quot;force: boolean&quot; (optional)</p>
<dd>if false (the default), an eject request will be sent to the guest if it has locked the tray (and the tray will not be opened immediately); if true, the tray will be opened regardless of whether it is locked</dl>
<p> <code>Since:</code> 2.5 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-open-tray&quot;,<br />
   &quot;arguments&quot; : {&quot;id&quot; : &quot;ide0-1-0&quot;}}</p>
<p>    &lt; -{&quot;timestamp&quot; : {&quot;seconds&quot; : 1418751016,<br />
                       &quot;microseconds&quot; : 716996},<br />
        &quot;event&quot; : &quot;DEVICE_TRAY_MOVED&quot;,<br />
        &quot;data&quot; : {&quot;device&quot; : &quot;ide1-cd0&quot;,<br />
                  &quot;id&quot; : &quot;ide0-1-0&quot;,<br />
                  &quot;tray-open&quot; : true}}</p>
<p>    &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>blockdev-close-tray</code> (Command) Closes a block device&#8217;s tray. If there is a block driver state tree associated with the block device (which is currently ejected), that tree will be loaded as the medium. If the tray was already closed before, this will be a no-op. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>Block device name (deprecated, use <tt>&quot;id&quot;</tt> instead)</p>
<dt>&quot;id: string&quot; (optional)</p>
<dd>The name or <font SIZE="-1">QOM</font> path of the guest device (since: 2.8)</dl>
<p> <code>Since:</code> 2.5 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-close-tray&quot;,<br />
   &quot;arguments&quot; : {&quot;id&quot; : &quot;ide0-1-0&quot;}}</p>
<p>    &lt; -{&quot;timestamp&quot; : {&quot;seconds&quot; : 1418751345,<br />
                       &quot;microseconds&quot; : 272147},<br />
        &quot;event&quot; : &quot;DEVICE_TRAY_MOVED&quot;,<br />
        &quot;data&quot; : {&quot;device&quot; : &quot;ide1-cd0&quot;,<br />
                  &quot;id&quot; : &quot;ide0-1-0&quot;,<br />
                  &quot;tray-open&quot; : false}}</p>
<p>    &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>blockdev-remove-medium</code> (Command) Removes a medium (a block driver state tree) from a block device. That block device&#8217;s tray must currently be open (unless there is no attached guest device). If the tray is open and there is no medium inserted, this will be a no-op. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The name or <font SIZE="-1">QOM</font> path of the guest device</dl>
<p> <code>Since:</code> 2.12 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-remove-medium&quot;,<br />
   &quot;arguments&quot; : {&quot;id&quot; : &quot;ide0-1-0&quot;}}</p>
<p>    &lt; &#8211;<br />
{<br />
    &quot;error&quot;:<br />
    {<br />
        &quot;class&quot; : &quot;GenericError&quot;,<br />
                  &quot;desc&quot; : &quot;Tray of device &#8216;ide0-1-0&#8217; is not open&quot;<br />
    }<br />
    }</p>
<p>        -&gt; {&quot;execute&quot; : &quot;blockdev-open-tray&quot;,<br />
            &quot;arguments&quot; : {&quot;id&quot; : &quot;ide0-1-0&quot;}}</p>
<p>        &lt; -{&quot;timestamp&quot; : {&quot;seconds&quot; : 1418751627,<br />
                           &quot;microseconds&quot; : 549958},<br />
            &quot;event&quot; : &quot;DEVICE_TRAY_MOVED&quot;,<br />
            &quot;data&quot; : {&quot;device&quot; : &quot;ide1-cd0&quot;,<br />
                      &quot;id&quot; : &quot;ide0-1-0&quot;,<br />
                      &quot;tray-open&quot; : true}}</p>
<p>        &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
        }</p>
<p>            -&gt; {&quot;execute&quot; : &quot;blockdev-remove-medium&quot;,<br />
                &quot;arguments&quot; : {&quot;id&quot; : &quot;ide0-1-0&quot;}}</p>
<p>            &lt; &#8211;<br />
        {<br />
            &quot;return&quot;:<br />
            {<br />
            }<br />
        } <code>blockdev-insert-medium</code> (Command) Inserts a medium (a block driver state tree) into a block device. That block device&#8217;s tray must currently be open (unless there is no attached guest device) and there must be no medium inserted already. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The name or <font SIZE="-1">QOM</font> path of the guest device</p>
<dt>&quot;node-name: string&quot;</p>
<dd>name of a node in the block driver state graph</dl>
<p> <code>Since:</code> 2.12 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-add&quot;,<br />
   &quot;arguments&quot; : {<br />
       &quot;node-name&quot; : &quot;node0&quot;,<br />
       &quot;driver&quot; : &quot;raw&quot;,<br />
       &quot;file&quot; : {&quot;driver&quot; : &quot;file&quot;,<br />
                 &quot;filename&quot; : &quot;fedora.iso&quot;}<br />
   }} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
    }</p>
<p>        -&gt; {&quot;execute&quot; : &quot;blockdev-insert-medium&quot;,<br />
            &quot;arguments&quot; : {&quot;id&quot; : &quot;ide0-1-0&quot;,<br />
                           &quot;node-name&quot; : &quot;node0&quot;}}</p>
<p>        &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
    } <code>BlockdevChangeReadOnlyMode</code> (Enum) Specifies the new read-only mode of a block device subject to the <tt>&quot;blockdev-change-medium&quot;</tt> command. <code>Values:</code></p>
<dl>
<dt>&quot;retain&quot;</p>
<dd>Retains the current read-only mode</p>
<dt>&quot;read-only&quot;</p>
<dd>Makes the device read-only</p>
<dt>&quot;read-write&quot;</p>
<dd>Makes the device writable</dl>
<p> <code>Since:</code> 2.3 <code>blockdev-change-medium</code> (Command) Changes the medium inserted into a block device by ejecting the current medium and loading a new image file which is inserted as the new medium (this command combines blockdev-open-tray, blockdev-remove-medium, blockdev-insert-medium and blockdev-close-tray). <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>Block device name (deprecated, use <tt>&quot;id&quot;</tt> instead)</p>
<dt>&quot;id: string&quot; (optional)</p>
<dd>The name or <font SIZE="-1">QOM</font> path of the guest device (since: 2.8)</p>
<dt>&quot;filename: string&quot;</p>
<dd>filename of the new image to be loaded</p>
<dt>&quot;format: string&quot; (optional)</p>
<dd>format to open the new image with (defaults to the probed format)</p>
<dt>&quot;read-only-mode: BlockdevChangeReadOnlyMode&quot; (optional)</p>
<dd>change the read-only mode of the device; defaults to &#8216;retain&#8217;</dl>
<p> <code>Since:</code> 2.5 <code>Examples:</code> 1. Change a removable medium</p>
<p>        -&gt;{&quot;execute&quot; : &quot;blockdev-change-medium&quot;,<br />
           &quot;arguments&quot; : {&quot;id&quot; : &quot;ide0-1-0&quot;,<br />
                          &quot;filename&quot; : &quot;/srv/images/Fedora-12-x86_64-DVD.iso&quot;,<br />
                          &quot;format&quot; : &quot;raw&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
}</p>
<p>2. Load a read &#8211; only medium into a writable drive</p>
<p>                     -&gt;{&quot;execute&quot; : &quot;blockdev-change-medium&quot;,<br />
                        &quot;arguments&quot; : {&quot;id&quot; : &quot;floppyA&quot;,<br />
                                       &quot;filename&quot; : &quot;/srv/images/ro.img&quot;,<br />
                                       &quot;format&quot; : &quot;raw&quot;,<br />
                                       &quot;read-only-mode&quot; : &quot;retain&quot;}}</p>
<p>    &lt; &#8211;<br />
{<br />
    &quot;error&quot;:<br />
    {<br />
        &quot;class&quot; : &quot;GenericError&quot;,<br />
                  &quot;desc&quot; : &quot;Could not open &#8216;/srv/images/ro.img&#8217;: Permission denied&quot;<br />
    }<br />
    }</p>
<p>        -&gt; {&quot;execute&quot; : &quot;blockdev-change-medium&quot;,<br />
            &quot;arguments&quot; : {&quot;id&quot; : &quot;floppyA&quot;,<br />
                           &quot;filename&quot; : &quot;/srv/images/ro.img&quot;,<br />
                           &quot;format&quot; : &quot;raw&quot;,<br />
                           &quot;read-only-mode&quot; : &quot;read-only&quot;}}</p>
<p>        &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
    } <code>BlockErrorAction</code> (Enum) An enumeration of action that has been taken when a <font SIZE="-1">DISK I/O</font> occurs <code>Values:</code></p>
<dl>
<dt>&quot;ignore&quot;</p>
<dd>error has been ignored</p>
<dt>&quot;report&quot;</p>
<dd>error has been reported to the device</p>
<dt>&quot;stop&quot;</p>
<dd>error caused <font SIZE="-1">VM</font> to be stopped</dl>
<p> <code>Since:</code> 2.1 <font SIZE="-1"><code>BLOCK_IMAGE_CORRUPTED</code></font> (Event) Emitted when a disk image is being marked corrupt. The image can be identified by its device or node name. The &#8216;device&#8217; field is always present for compatibility reasons, but it can be empty (&quot;&quot;) if the image does not have a device name associated. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>device name. This is always present for compatibility reasons, but it can be empty (&quot;&quot;) if the image does not have a device name associated.</p>
<dt>&quot;node-name: string&quot; (optional)</p>
<dd>node name (Since: 2.4)</p>
<dt>&quot;msg: string&quot;</p>
<dd>informative message for human consumption, such as the kind of corruption being detected. It should not be parsed by machine as it is not guaranteed to be stable</p>
<dt>&quot;offset: int&quot; (optional)</p>
<dd>if the corruption resulted from an image access, this is the host&#8217;s access offset into the image</p>
<dt>&quot;size: int&quot; (optional)</p>
<dd>if the corruption resulted from an image access, this is the access size</p>
<dt>&quot;fatal: boolean&quot;</p>
<dd>if set, the image is marked corrupt and therefore unusable after this event and must be repaired (Since 2.2; before, every <font SIZE="-1">BLOCK_IMAGE_CORRUPTED</font> event was fatal)</dl>
<p> <code>Note:</code> If action is &#8220;stop&#8221;, a <font SIZE="-1">STOP</font> event will eventually follow the <font SIZE="-1">BLOCK_IO_ERROR</font> event. <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;BLOCK_IMAGE_CORRUPTED&quot;,
 &quot;data&quot;: { &quot;device&quot;: &quot;ide0-hd0&quot;, &quot;node-name&quot;: &quot;node0&quot;,
 &quot;msg&quot;: &quot;Prevented active L1 table overwrite&quot;, &quot;offset&quot;: 196608,
 &quot;size&quot;: 65536 },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1378126126, &quot;microseconds&quot;: 966463 } }</pre>
<p><code>Since:</code> 1.7 <font SIZE="-1"><code>BLOCK_IO_ERROR</code></font> (Event) Emitted when a disk I/O error occurs <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>device name. This is always present for compatibility reasons, but it can be empty (&quot;&quot;) if the image does not have a device name associated.</p>
<dt>&quot;node-name: string&quot; (optional)</p>
<dd>node name. Note that errors may be reported for the root node that is directly attached to a guest device rather than for the node where the error occurred. The node name is not present if the drive is empty. (Since: 2.8)</p>
<dt>&quot;operation: IoOperationType&quot;</p>
<dd>I/O operation</p>
<dt>&quot;action: BlockErrorAction&quot;</p>
<dd>action that has been taken</p>
<dt>&quot;nospace: boolean&quot; (optional)</p>
<dd>true if I/O error was caused due to a no-space condition. This key is only present if query-block&#8217;s io-status is present, please see query-block documentation for more information (since: 2.2)</p>
<dt>&quot;reason: string&quot;</p>
<dd>human readable string describing the error cause. (This field is a debugging aid for humans, it should not be parsed by applications) (since: 2.2)</dl>
<p> <code>Note:</code> If action is &#8220;stop&#8221;, a <font SIZE="-1">STOP</font> event will eventually follow the <font SIZE="-1">BLOCK_IO_ERROR</font> event <code>Since:</code> 0.13.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;BLOCK_IO_ERROR&quot;,
 &quot;data&quot;: { &quot;device&quot;: &quot;ide0-hd1&quot;,
 &quot;node-name&quot;: &quot;#block212&quot;,
 &quot;operation&quot;: &quot;write&quot;,
 &quot;action&quot;: &quot;stop&quot; },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1265044230, &quot;microseconds&quot;: 450486 } }</pre>
<p><font SIZE="-1"><code>BLOCK_JOB_COMPLETED</code></font> (Event) Emitted when a block job has completed <code>Arguments:</code></p>
<dl>
<dt>&quot;type: JobType&quot;</p>
<dd>job type</p>
<dt>&quot;device: string&quot;</p>
<dd>The job identifier. Originally the device name but other values are allowed since <font SIZE="-1">QEMU 2.7</font></p>
<dt>&quot;len: int&quot;</p>
<dd>maximum progress value</p>
<dt>&quot;offset: int&quot;</p>
<dd>current progress value. On success this is equal to len. On failure this is less than len</p>
<dt>&quot;speed: int&quot;</p>
<dd>rate limit, bytes per second</p>
<dt>&quot;error: string&quot; (optional)</p>
<dd>error message. Only present on failure. This field contains a human-readable error message. There are no semantics other than that streaming has failed and clients should not try to interpret the error string</dl>
<p> <code>Since:</code> 1.1 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;BLOCK_JOB_COMPLETED&quot;,
 &quot;data&quot;: { &quot;type&quot;: &quot;stream&quot;, &quot;device&quot;: &quot;virtio-disk0&quot;,
 &quot;len&quot;: 10737418240, &quot;offset&quot;: 10737418240,
 &quot;speed&quot;: 0 },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1267061043, &quot;microseconds&quot;: 959568 } }</pre>
<p><font SIZE="-1"><code>BLOCK_JOB_CANCELLED</code></font> (Event) Emitted when a block job has been cancelled <code>Arguments:</code></p>
<dl>
<dt>&quot;type: JobType&quot;</p>
<dd>job type</p>
<dt>&quot;device: string&quot;</p>
<dd>The job identifier. Originally the device name but other values are allowed since <font SIZE="-1">QEMU 2.7</font></p>
<dt>&quot;len: int&quot;</p>
<dd>maximum progress value</p>
<dt>&quot;offset: int&quot;</p>
<dd>current progress value. On success this is equal to len. On failure this is less than len</p>
<dt>&quot;speed: int&quot;</p>
<dd>rate limit, bytes per second</dl>
<p> <code>Since:</code> 1.1 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;BLOCK_JOB_CANCELLED&quot;,
 &quot;data&quot;: { &quot;type&quot;: &quot;stream&quot;, &quot;device&quot;: &quot;virtio-disk0&quot;,
 &quot;len&quot;: 10737418240, &quot;offset&quot;: 134217728,
 &quot;speed&quot;: 0 },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1267061043, &quot;microseconds&quot;: 959568 } }</pre>
<p><font SIZE="-1"><code>BLOCK_JOB_ERROR</code></font> (Event) Emitted when a block job encounters an error <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>The job identifier. Originally the device name but other values are allowed since <font SIZE="-1">QEMU 2.7</font></p>
<dt>&quot;operation: IoOperationType&quot;</p>
<dd>I/O operation</p>
<dt>&quot;action: BlockErrorAction&quot;</p>
<dd>action that has been taken</dl>
<p> <code>Since:</code> 1.3 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;BLOCK_JOB_ERROR&quot;,
 &quot;data&quot;: { &quot;device&quot;: &quot;ide0-hd1&quot;,
 &quot;operation&quot;: &quot;write&quot;,
 &quot;action&quot;: &quot;stop&quot; },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1265044230, &quot;microseconds&quot;: 450486 } }</pre>
<p><font SIZE="-1"><code>BLOCK_JOB_READY</code></font> (Event) Emitted when a block job is ready to complete <code>Arguments:</code></p>
<dl>
<dt>&quot;type: JobType&quot;</p>
<dd>job type</p>
<dt>&quot;device: string&quot;</p>
<dd>The job identifier. Originally the device name but other values are allowed since <font SIZE="-1">QEMU 2.7</font></p>
<dt>&quot;len: int&quot;</p>
<dd>maximum progress value</p>
<dt>&quot;offset: int&quot;</p>
<dd>current progress value. On success this is equal to len. On failure this is less than len</p>
<dt>&quot;speed: int&quot;</p>
<dd>rate limit, bytes per second</dl>
<p> <code>Note:</code> The &#8220;ready to complete&#8221; status is always reset by a <tt>&quot;BLOCK_JOB_ERROR&quot;</tt> event <code>Since:</code> 1.3 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;BLOCK_JOB_READY&quot;,
 &quot;data&quot;: { &quot;device&quot;: &quot;drive0&quot;, &quot;type&quot;: &quot;mirror&quot;, &quot;speed&quot;: 0,
 &quot;len&quot;: 2097152, &quot;offset&quot;: 2097152 }
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1265044230, &quot;microseconds&quot;: 450486 } }</pre>
<p><font SIZE="-1"><code>BLOCK_JOB_PENDING</code></font> (Event) Emitted when a block job is awaiting explicit authorization to finalize graph changes via <tt>&quot;block-job-finalize&quot;</tt>. If this job is part of a transaction, it will not emit this event until the transaction has converged first. <code>Arguments:</code></p>
<dl>
<dt>&quot;type: JobType&quot;</p>
<dd>job type</p>
<dt>&quot;id: string&quot;</p>
<dd>The job identifier.</dl>
<p> <code>Since:</code> 2.12 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;BLOCK_JOB_WAITING&quot;,
 &quot;data&quot;: { &quot;device&quot;: &quot;drive0&quot;, &quot;type&quot;: &quot;mirror&quot; },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1265044230, &quot;microseconds&quot;: 450486 } }</pre>
<p><code>PreallocMode</code> (Enum) Preallocation mode of <font SIZE="-1">QEMU</font> image file <code>Values:</code></p>
<dl>
<dt>&quot;off&quot;</p>
<dd>no preallocation</p>
<dt>&quot;metadata&quot;</p>
<dd>preallocate only for metadata</p>
<dt>&quot;falloc&quot;</p>
<dd>like <tt>&quot;full&quot;</tt> preallocation but allocate disk space by <code>posix_fallocate()</code> rather than writing data.</p>
<dt>&quot;full&quot;</p>
<dd>preallocate all data by writing it to the device to ensure disk space is really available. This data may or may not be zero, depending on the image format and storage. <tt>&quot;full&quot;</tt> preallocation also sets up metadata correctly.</dl>
<p> <code>Since:</code> 2.2 <font SIZE="-1"><code>BLOCK_WRITE_THRESHOLD</code></font> (Event) Emitted when writes on block device reaches or exceeds the configured write threshold. For thin-provisioned devices, this means the device should be extended to avoid pausing for disk exhaustion. The event is one shot. Once triggered, it needs to be re-registered with another block-set-write-threshold command. <code>Arguments:</code></p>
<dl>
<dt>&quot;node-name: string&quot;</p>
<dd>graph node name on which the threshold was exceeded.</p>
<dt>&quot;amount-exceeded: int&quot;</p>
<dd>amount of data which exceeded the threshold, in bytes.</p>
<dt>&quot;write-threshold: int&quot;</p>
<dd>last configured threshold, in bytes.</dl>
<p> <code>Since:</code> 2.3 <code>block-set-write-threshold</code> (Command) Change the write threshold for a block drive. An event will be delivered if a write to this block drive crosses the configured threshold. The threshold is an offset, thus must be non-negative. Default is no write threshold. Setting the threshold to zero disables it. This is useful to transparently resize thin-provisioned drives without the guest <font SIZE="-1">OS</font> noticing. <code>Arguments:</code></p>
<dl>
<dt>&quot;node-name: string&quot;</p>
<dd>graph node name on which the threshold must be set.</p>
<dt>&quot;write-threshold: int&quot;</p>
<dd>configured threshold for the block device, bytes. Use 0 to disable the threshold.</dl>
<p> <code>Since:</code> 2.3 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;block-set-write-threshold&quot;,<br />
   &quot;arguments&quot; : {&quot;node-name&quot; : &quot;mydev&quot;,<br />
                  &quot;write-threshold&quot; : 17179869184}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>x-blockdev-change</code> (Command) Dynamically reconfigure the block driver state graph. It can be used to add, remove, insert or replace a graph node. Currently only the Quorum driver implements this feature to add or remove its child. This is useful to fix a broken quorum child. If <tt>&quot;node&quot;</tt> is specified, it will be inserted under <tt>&quot;parent&quot;</tt>. <tt>&quot;child&quot;</tt> may not be specified in this case. If both <tt>&quot;parent&quot;</tt> and <tt>&quot;child&quot;</tt> are specified but <tt>&quot;node&quot;</tt> is not, <tt>&quot;child&quot;</tt> will be detached from <tt>&quot;parent&quot;</tt>. <code>Arguments:</code></p>
<dl>
<dt>&quot;parent: string&quot;</p>
<dd>the id or name of the parent node.</p>
<dt>&quot;child: string&quot; (optional)</p>
<dd>the name of a child under the given parent node.</p>
<dt>&quot;node: string&quot; (optional)</p>
<dd>the name of the node that will be added.</dl>
<p> <code>Note:</code> this command is experimental, and its <font SIZE="-1">API</font> is not stable. It does not support all kinds of operations, all kinds of children, nor all block drivers. <font SIZE="-1">FIXME</font> Removing children from a quorum node means introducing gaps in the child indices. This cannot be represented in the &#8216;children&#8217; list of BlockdevOptionsQuorum, as returned by .<code>bdrv_refresh_filename()</code>. Warning: The data in a new quorum child <font SIZE="-1">MUST</font> be consistent with that of the rest of the array. <code>Since:</code> 2.7 <code>Example:</code> 1. Add a new node to a quorum<br />
        -&gt;{&quot;execute&quot; : &quot;blockdev-add&quot;,<br />
           &quot;arguments&quot; : {<br />
               &quot;driver&quot; : &quot;raw&quot;,<br />
               &quot;node-name&quot; : &quot;new_node&quot;,<br />
               &quot;file&quot; : {&quot;driver&quot; : &quot;file&quot;,<br />
                         &quot;filename&quot; : &quot;test.raw&quot;}<br />
           }} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
    }<br />
        -&gt; {&quot;execute&quot; : &quot;x-blockdev-change&quot;,<br />
            &quot;arguments&quot; : {&quot;parent&quot; : &quot;disk1&quot;,<br />
                           &quot;node&quot; : &quot;new_node&quot;}} &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
    }</p>
<p>2. Delete a quorum&#8217;s node<br />
        -&gt;{&quot;execute&quot; : &quot;x-blockdev-change&quot;,<br />
           &quot;arguments&quot; : {&quot;parent&quot; : &quot;disk1&quot;,<br />
                          &quot;child&quot; : &quot;children.1&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>x-blockdev-set-iothread</code> (Command) Move <tt>&quot;node&quot;</tt> and its children into the <tt>&quot;iothread&quot;</tt>. If <tt>&quot;iothread&quot;</tt> is null then move <tt>&quot;node&quot;</tt> and its children into the main loop. The node must not be attached to a BlockBackend. <code>Arguments:</code></p>
<dl>
<dt>&quot;node-name: string&quot;</p>
<dd>the name of the block driver node</p>
<dt>&quot;iothread: StrOrNull&quot;</p>
<dd>the name of the IOThread object or null for the main loop</p>
<dt>&quot;force: boolean&quot; (optional)</p>
<dd>true if the node and its children should be moved when a BlockBackend is already attached</dl>
<p> <code>Note:</code> this command is experimental and intended for test cases that need control over IOThreads only. <code>Since:</code> 2.12 <code>Example:</code> 1. Move a node into an IOThread<br />
        -&gt;{&quot;execute&quot; : &quot;x-blockdev-set-iothread&quot;,<br />
           &quot;arguments&quot; : {&quot;node-name&quot; : &quot;disk1&quot;,<br />
                          &quot;iothread&quot; : &quot;iothread0&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
}</p>
<p>2. Move a node into the main loop<br />
        -&gt;{&quot;execute&quot; : &quot;x-blockdev-set-iothread&quot;,<br />
           &quot;arguments&quot; : {&quot;node-name&quot; : &quot;disk1&quot;,<br />
                          &quot;iothread&quot; : null}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <i>Additional block stuff (</i><font SIZE="-1"><i>VM</i></font><i> related)</i> <code>BiosAtaTranslation</code> (Enum) Policy that <font SIZE="-1">BIOS</font> should use to interpret cylinder/head/sector addresses. Note that Bochs <font SIZE="-1">BIOS</font> and SeaBIOS will not actually translate logical <font SIZE="-1">CHS</font> to physical; instead, they will use logical block addressing. <code>Values:</code></p>
<dl>
<dt>&quot;auto&quot;</p>
<dd>If cylinder/heads/sizes are passed, choose between none and <font SIZE="-1">LBA</font> depending on the size of the disk. If they are not passed, choose none if <font SIZE="-1">QEMU</font> can guess that the disk had 16 or fewer heads, large if <font SIZE="-1">QEMU</font> can guess that the disk had 131072 or fewer tracks across all heads (i.e. cylinders*heads&lt;131072), otherwise <font SIZE="-1">LBA.</font></p>
<dt>&quot;none&quot;</p>
<dd>The physical disk geometry is equal to the logical geometry.</p>
<dt>&quot;lba&quot;</p>
<dd>Assume 63 sectors per track and one of 16, 32, 64, 128 or 255 heads (if fewer than 255 are enough to cover the whole disk with 1024 cylinders/head). The number of cylinders/head is then computed based on the number of sectors and heads.</p>
<dt>&quot;large&quot;</p>
<dd>The number of cylinders per head is scaled down to 1024 by correspondingly scaling up the number of heads.</p>
<dt>&quot;rechs&quot;</p>
<dd>Same as <tt>&quot;large&quot;</tt>, but first convert a 16-head geometry to 15-head, by proportionally scaling up the number of cylinders/head.</dl>
<p> <code>Since:</code> 2.0 <code>FloppyDriveType</code> (Enum) Type of Floppy drive to be emulated by the Floppy Disk Controller. <code>Values:</code></p>
<dl>
<dt>144</p>
<dd>1.44MB 3.5&quot; drive</p>
<dt>288</p>
<dd>2.88MB 3.5&quot; drive</p>
<dt>120</p>
<dd>1.2MB 5.25&quot; drive</p>
<dt>&quot;none&quot;</p>
<dd>No drive connected</p>
<dt>&quot;auto&quot;</p>
<dd>Automatically determined by inserted media at boot</dl>
<p> <code>Since:</code> 2.6 <code>BlockdevSnapshotInternal</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>the device name or node-name of a root node to generate the snapshot from</p>
<dt>&quot;name: string&quot;</p>
<dd>the name of the internal snapshot to be created</dl>
<p> <code>Notes:</code> In transaction, if <tt>&quot;name&quot;</tt> is empty, or any snapshot matching <tt>&quot;name&quot;</tt> exists, the operation will fail. Only some image formats support it, for example, qcow2, rbd, and sheepdog. <code>Since:</code> 1.7 <code>PRManagerInfo</code> (Object) Information about a persistent reservation manager <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>the identifier of the persistent reservation manager</p>
<dt>&quot;connected: boolean&quot;</p>
<dd>true if the persistent reservation manager is connected to the underlying storage or helper</dl>
<p> <code>Since:</code> 3.0 <code>query-pr-managers</code> (Command) Returns a list of information about each persistent reservation manager. <code>Returns:</code> a list of <tt>&quot;PRManagerInfo&quot;</tt> for each persistent reservation manager <code>Since:</code> 3.0 <code>blockdev-snapshot-internal-sync</code> (Command) Synchronously take an internal snapshot of a block device, when the format of the image used supports it. If the name is an empty string, or a snapshot with name already exists, the operation will fail. For the arguments, see the documentation of BlockdevSnapshotInternal. <code>Returns:</code> nothing on success If <tt>&quot;device&quot;</tt> is not a valid block device, GenericError If any snapshot matching <tt>&quot;name&quot;</tt> exists, or <tt>&quot;name&quot;</tt> is empty, GenericError If the format of the image used does not support it, BlockFormatFeatureNotSupported <code>Since:</code> 1.7 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-snapshot-internal-sync&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;ide-hd0&quot;,<br />
                  &quot;name&quot; : &quot;snapshot0&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>blockdev-snapshot-delete-internal-sync</code> (Command) Synchronously delete an internal snapshot of a block device, when the format of the image used support it. The snapshot is identified by name or id or both. One of the name or id is required. Return SnapshotInfo for the successfully deleted snapshot. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>the device name or node-name of a root node to delete the snapshot from</p>
<dt>&quot;id: string&quot; (optional)</p>
<dd>optional the snapshot&#8217;s <font SIZE="-1">ID</font> to be deleted</p>
<dt>&quot;name: string&quot; (optional)</p>
<dd>optional the snapshot&#8217;s name to be deleted</dl>
<p> <code>Returns:</code> SnapshotInfo on success If <tt>&quot;device&quot;</tt> is not a valid block device, GenericError If snapshot not found, GenericError If the format of the image used does not support it, BlockFormatFeatureNotSupported If <tt>&quot;id&quot;</tt> and <tt>&quot;name&quot;</tt> are both not specified, GenericError <code>Since:</code> 1.7 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;blockdev-snapshot-delete-internal-sync&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;ide-hd0&quot;,<br />
                  &quot;name&quot; : &quot;snapshot0&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;id&quot; : &quot;1&quot;,<br />
               &quot;name&quot; : &quot;snapshot0&quot;,<br />
                        &quot;vm-state-size&quot; : 0,<br />
                        &quot;date-sec&quot; : 1000012,<br />
                        &quot;date-nsec&quot; : 10,<br />
                        &quot;vm-clock-sec&quot; : 100,<br />
                        &quot;vm-clock-nsec&quot; : 20<br />
    }<br />
} <code>eject</code> (Command) Ejects a device from a removable drive. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>Block device name (deprecated, use <tt>&quot;id&quot;</tt> instead)</p>
<dt>&quot;id: string&quot; (optional)</p>
<dd>The name or <font SIZE="-1">QOM</font> path of the guest device (since: 2.8)</p>
<dt>&quot;force: boolean&quot; (optional)</p>
<dd>If true, eject regardless of whether the drive is locked. If not specified, the default value is false.</dl>
<p> <code>Returns:</code> Nothing on success If <tt>&quot;device&quot;</tt> is not a valid block device, DeviceNotFound <code>Notes:</code> Ejecting a device with no media results in success <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;eject&quot;, &quot;arguments&quot; : {&quot;id&quot; : &quot;ide1-0-1&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>nbd-server-start</code> (Command) Start an <font SIZE="-1">NBD</font> server listening on the given host and port. Block devices can then be exported using <tt>&quot;nbd-server-add&quot;</tt>. The <font SIZE="-1">NBD</font> server will present them as named exports; for example, another <font SIZE="-1">QEMU</font> instance could refer to them as &#8220;nbd:HOST:PORT:exportname=NAME&#8221;. <code>Arguments:</code></p>
<dl>
<dt>&quot;addr: SocketAddressLegacy&quot;</p>
<dd>Address on which to listen.</p>
<dt>&quot;tls-creds: string&quot; (optional)</p>
<dd><font SIZE="-1">ID</font> of the <font SIZE="-1">TLS</font> credentials object (since 2.6).</p>
<dt>&quot;tls-authz: string&quot; (optional)</p>
<dd><font SIZE="-1">ID</font> of the QAuthZ authorization object used to validate the client&#8217;s x509 distinguished name. This object is is only resolved at time of use, so can be deleted and recreated on the fly while the <font SIZE="-1">NBD</font> server is active. If missing, it will default to denying access (since 4.0).</dl>
<p> <code>Returns:</code> error if the server is already running. <code>Since:</code> 1.3.0 <code>nbd-server-add</code> (Command) Export a block node to <font SIZE="-1">QEMU</font>&#8216;s embedded <font SIZE="-1">NBD</font> server. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>The device name or node name of the node to be exported</p>
<dt>&quot;name: string&quot; (optional)</p>
<dd>Export name. If unspecified, the <tt>&quot;device&quot;</tt> parameter is used as the export name. (Since 2.12)</p>
<dt>&quot;writable: boolean&quot; (optional)</p>
<dd>Whether clients should be able to write to the device via the <font SIZE="-1">NBD</font> connection (default false).</p>
<dt>&quot;bitmap: string&quot; (optional)</p>
<dd>Also export the dirty bitmap reachable from <tt>&quot;device&quot;</tt>, so the <font SIZE="-1">NBD</font> client can use <font SIZE="-1">NBD_OPT_SET_META_CONTEXT</font> with &#8220;qemu:dirty-bitmap:NAME&#8221; to inspect the bitmap. (since 4.0)</dl>
<p> <code>Returns:</code> error if the server is not running, or export with the same name already exists. <code>Since:</code> 1.3.0 <code>NbdServerRemoveMode</code> (Enum) Mode for removing an <font SIZE="-1">NBD</font> export. <code>Values:</code></p>
<dl>
<dt>&quot;safe&quot;</p>
<dd>Remove export if there are no existing connections, fail otherwise.</p>
<dt>&quot;hard&quot;</p>
<dd>Drop all connections immediately and remove export.</dl>
<p> Potential additional modes to be added in the future: hide: Just hide export from new clients, leave existing connections as is. Remove export after all clients are disconnected. soft: Hide export from new clients, answer with <font SIZE="-1">ESHUTDOWN</font> for all further requests from existing clients. <code>Since:</code> 2.12 <code>nbd-server-remove</code> (Command) Remove <font SIZE="-1">NBD</font> export by name. <code>Arguments:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>Export name.</p>
<dt>&quot;mode: NbdServerRemoveMode&quot; (optional)</p>
<dd>Mode of command operation. See <tt>&quot;NbdServerRemoveMode&quot;</tt> description. Default is &#8216;safe&#8217;.</dl>
<p> <code>Returns:</code> error if</p>
<dl>
<dt>&#8211;</p>
<dd>the server is not running</p>
<dt>&#8211;</p>
<dd>export is not found</p>
<dt>&#8211;</p>
<dd>mode is &#8216;safe&#8217; and there are existing connections</dl>
<p> <code>Since:</code> 2.12 <code>nbd-server-stop</code> (Command) Stop <font SIZE="-1">QEMU</font>&#8216;s embedded <font SIZE="-1">NBD</font> server, and unregister all devices previously added via <tt>&quot;nbd-server-add&quot;</tt>. <code>Since:</code> 1.3.0 <font SIZE="-1"><code>DEVICE_TRAY_MOVED</code></font> (Event) Emitted whenever the tray of a removable device is moved by the guest or by <font SIZE="-1">HMP/QMP</font> commands <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>Block device name. This is always present for compatibility reasons, but it can be empty (&quot;&quot;) if the image does not have a device name associated.</p>
<dt>&quot;id: string&quot;</p>
<dd>The name or <font SIZE="-1">QOM</font> path of the guest device (since 2.8)</p>
<dt>&quot;tray-open: boolean&quot;</p>
<dd>true if the tray has been opened or false if it has been closed</dl>
<p> <code>Since:</code> 1.1 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;DEVICE_TRAY_MOVED&quot;,
 &quot;data&quot;: { &quot;device&quot;: &quot;ide1-cd0&quot;,
 &quot;id&quot;: &quot;/machine/unattached/device[22]&quot;,
 &quot;tray-open&quot;: true
 },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1265044230, &quot;microseconds&quot;: 450486 } }</pre>
<p><font SIZE="-1"><code>PR_MANAGER_STATUS_CHANGED</code></font> (Event) Emitted whenever the connected status of a persistent reservation manager changes. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The id of the <font SIZE="-1">PR</font> manager object</p>
<dt>&quot;connected: boolean&quot;</p>
<dd>true if the <font SIZE="-1">PR</font> manager is connected to a backend</dl>
<p> <code>Since:</code> 3.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;PR_MANAGER_STATUS_CHANGED&quot;,
 &quot;data&quot;: { &quot;id&quot;: &quot;pr-helper0&quot;,
 &quot;connected&quot;: true
 },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1519840375, &quot;microseconds&quot;: 450486 } }</pre>
<p><code>QuorumOpType</code> (Enum) An enumeration of the quorum operation types <code>Values:</code></p>
<dl>
<dt>&quot;read&quot;</p>
<dd>read operation</p>
<dt>&quot;write&quot;</p>
<dd>write operation</p>
<dt>&quot;flush&quot;</p>
<dd>flush operation</dl>
<p> <code>Since:</code> 2.6 <font SIZE="-1"><code>QUORUM_FAILURE</code></font> (Event) Emitted by the Quorum block driver if it fails to establish a quorum <code>Arguments:</code></p>
<dl>
<dt>&quot;reference: string&quot;</p>
<dd>device name if defined else node name</p>
<dt>&quot;sector-num: int&quot;</p>
<dd>number of the first sector of the failed read operation</p>
<dt>&quot;sectors-count: int&quot;</p>
<dd>failed read operation sector count</dl>
<p> <code>Note:</code> This event is rate-limited. <code>Since:</code> 2.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;QUORUM_FAILURE&quot;,
 &quot;data&quot;: { &quot;reference&quot;: &quot;usr1&quot;, &quot;sector-num&quot;: 345435, &quot;sectors-count&quot;: 5 },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1344522075, &quot;microseconds&quot;: 745528 } }</pre>
<p><font SIZE="-1"><code>QUORUM_REPORT_BAD</code></font> (Event) Emitted to report a corruption of a Quorum file <code>Arguments:</code></p>
<dl>
<dt>&quot;type: QuorumOpType&quot;</p>
<dd>quorum operation type (Since 2.6)</p>
<dt>&quot;error: string&quot; (optional)</p>
<dd>error message. Only present on failure. This field contains a human-readable error message. There are no semantics other than that the block layer reported an error and clients should not try to interpret the error string.</p>
<dt>&quot;node-name: string&quot;</p>
<dd>the graph node name of the block driver state</p>
<dt>&quot;sector-num: int&quot;</p>
<dd>number of the first sector of the failed read operation</p>
<dt>&quot;sectors-count: int&quot;</p>
<dd>failed read operation sector count</dl>
<p> <code>Note:</code> This event is rate-limited. <code>Since:</code> 2.0 <code>Example:</code> </p>
<pre> 1. Read operation
 
 { &quot;event&quot;: &quot;QUORUM_REPORT_BAD&quot;,
 &quot;data&quot;: { &quot;node-name&quot;: &quot;node0&quot;, &quot;sector-num&quot;: 345435, &quot;sectors-count&quot;: 5,
 &quot;type&quot;: &quot;read&quot; },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1344522075, &quot;microseconds&quot;: 745528 } }
 
 2. Flush operation
 
 { &quot;event&quot;: &quot;QUORUM_REPORT_BAD&quot;,
 &quot;data&quot;: { &quot;node-name&quot;: &quot;node0&quot;, &quot;sector-num&quot;: 0, &quot;sectors-count&quot;: 2097120,
 &quot;type&quot;: &quot;flush&quot;, &quot;error&quot;: &quot;Broken pipe&quot; },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1456406829, &quot;microseconds&quot;: 291763 } }</pre>
<h3>Character devices</h3>
<p><code>ChardevInfo</code> (Object) Information about a character device. <code>Members:</code></p>
<dl>
<dt>&quot;label: string&quot;</p>
<dd>the label of the character device</p>
<dt>&quot;filename: string&quot;</p>
<dd>the filename of the character device</p>
<dt>&quot;frontend-open: boolean&quot;</p>
<dd>shows whether the frontend device attached to this backend (eg. with the chardev=&#8230; option) is in open or closed state (since 2.1)</dl>
<p> <code>Notes:</code> <tt>&quot;filename&quot;</tt> is encoded using the <font SIZE="-1">QEMU</font> command line character device encoding. See the <font SIZE="-1">QEMU</font> man page for details. <code>Since:</code> 0.14.0 <code>query-chardev</code> (Command) Returns information about current character devices. <code>Returns:</code> a list of <tt>&quot;ChardevInfo&quot;</tt> <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-chardev&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;label&quot; : &quot;charchannel0&quot;,<br />
            &quot;filename&quot; : &quot;unix:/var/lib/libvirt/qemu/seabios.rhel6.agent,server&quot;,<br />
            &quot;frontend-open&quot; : false<br />
        },<br />
        {<br />
            &quot;label&quot; : &quot;charmonitor&quot;,<br />
            &quot;filename&quot; : &quot;unix:/var/lib/libvirt/qemu/seabios.rhel6.monitor,server&quot;,<br />
            &quot;frontend-open&quot; : true<br />
        },<br />
        {<br />
            &quot;label&quot; : &quot;charserial0&quot;,<br />
            &quot;filename&quot; : &quot;pty:/dev/pts/2&quot;,<br />
            &quot;frontend-open&quot; : true<br />
        }<br />
    ]<br />
} <code>ChardevBackendInfo</code> (Object) Information about a character device backend <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>The backend name</dl>
<p> <code>Since:</code> 2.0 <code>query-chardev-backends</code> (Command) Returns information about character device backends. <code>Returns:</code> a list of <tt>&quot;ChardevBackendInfo&quot;</tt> <code>Since:</code> 2.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-chardev-backends&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;name&quot; : &quot;udp&quot;<br />
        },<br />
        {<br />
            &quot;name&quot; : &quot;tcp&quot;<br />
        },<br />
        {<br />
            &quot;name&quot; : &quot;unix&quot;<br />
        },<br />
        {<br />
            &quot;name&quot; : &quot;spiceport&quot;<br />
        }<br />
    ]<br />
} <code>DataFormat</code> (Enum) An enumeration of data format. <code>Values:</code></p>
<dl>
<dt>&quot;utf8&quot;</p>
<dd>Data is a <font SIZE="-1">UTF-8</font> string (<font SIZE="-1">RFC 3629</font>)</p>
<dt>&quot;base64&quot;</p>
<dd>Data is Base64 encoded binary (<font SIZE="-1">RFC 3548</font>)</dl>
<p> <code>Since:</code> 1.4 <code>ringbuf-write</code> (Command) Write to a ring buffer character device. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>the ring buffer character device name</p>
<dt>&quot;data: string&quot;</p>
<dd>data to write</p>
<dt>&quot;format: DataFormat&quot; (optional)</p>
<dd>data encoding (default &#8216;utf8&#8217;).</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>base64: data must be base64 encoded text. Its binary decoding gets written.</p>
<dt>&#8211;</p>
<dd>utf8: data&#8217;s <font SIZE="-1">UTF-8</font> encoding is written</p>
<dt>&#8211;</p>
<dd>data itself is always Unicode regardless of format, like any other string.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 1.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;ringbuf-write&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;foo&quot;,<br />
                  &quot;data&quot; : &quot;abcdefgh&quot;,<br />
                  &quot;format&quot; : &quot;utf8&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>ringbuf-read</code> (Command) Read from a ring buffer character device. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>the ring buffer character device name</p>
<dt>&quot;size: int&quot;</p>
<dd>how many bytes to read at most</p>
<dt>&quot;format: DataFormat&quot; (optional)</p>
<dd>data encoding (default &#8216;utf8&#8217;).</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>base64: the data read is returned in base64 encoding.</p>
<dt>&#8211;</p>
<dd>utf8: the data read is interpreted as <font SIZE="-1">UTF-8.</font> Bug: can screw up when the buffer contains invalid <font SIZE="-1">UTF-8</font> sequences, <font SIZE="-1">NUL</font> characters, after the ring buffer lost data, and when reading stops because the size limit is reached.</p>
<dt>&#8211;</p>
<dd>The return value is always Unicode regardless of format, like any other string.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<p> <code>Returns:</code> data read from the device <code>Since:</code> 1.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;ringbuf-read&quot;,<br />
   &quot;arguments&quot; : {&quot;device&quot; : &quot;foo&quot;,<br />
                  &quot;size&quot; : 1000,<br />
                  &quot;format&quot; : &quot;utf8&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : &quot;abcdefgh&quot;<br />
} <code>ChardevCommon</code> (Object) Configuration shared across all chardev backends <code>Members:</code></p>
<dl>
<dt>&quot;logfile: string&quot; (optional)</p>
<dd>The name of a logfile to save output</p>
<dt>&quot;logappend: boolean&quot; (optional)</p>
<dd>true to append instead of truncate (default to false to truncate)</dl>
<p> <code>Since:</code> 2.6 <code>ChardevFile</code> (Object) Configuration info for file chardevs. <code>Members:</code></p>
<dl>
<dt>&quot;in: string&quot; (optional)</p>
<dd>The name of the input file</p>
<dt>&quot;out: string&quot;</p>
<dd>The name of the output file</p>
<dt>&quot;append: boolean&quot; (optional)</p>
<dd>Open the file in append mode (default false to truncate) (Since 2.6)</p>
<dt>The members of &quot;ChardevCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.4 <code>ChardevHostdev</code> (Object) Configuration info for device and pipe chardevs. <code>Members:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>The name of the special file for the device, i.e. /dev/ttyS0 on Unix or <font SIZE="-1">COM1:</font> on Windows</p>
<dt>The members of &quot;ChardevCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.4 <code>ChardevSocket</code> (Object) Configuration info for (stream) socket chardevs. Members:</p>
<p>&quot;addr: SocketAddressLegacy&quot;</p>
<p>socket address to listen on (server=true)<br />
or connect to (server=false)<br />
&quot;tls-creds: string&quot; (optional)</p>
<p>the ID of the TLS credentials object (since 2.6)<br />
&quot;tls-authz: string&quot; (optional)</p>
<p>the ID of the QAuthZ authorization object against which<br />
the client&#8217;s x509 distinguished name will be validated. This<br />
object is only resolved at time of use, so can be deleted<br />
and recreated on the fly while the chardev server is active.<br />
If missing, it will default to denying access (since 4.0)<br />
&quot;server: boolean&quot; (optional)</p>
<p>create server socket (default: true)<br />
&quot;wait: boolean&quot; (optional)</p>
<p>wait for incoming connection on server<br />
sockets (default: false).<br />
&quot;nodelay: boolean&quot; (optional)</p>
<p>set TCP_NODELAY socket option (default: false)<br />
&quot;telnet: boolean&quot; (optional)</p>
<p>enable telnet protocol on server<br />
sockets (default: false)<br />
&quot;tn3270: boolean&quot; (optional)</p>
<p>enable tn3270 protocol on server<br />
sockets (default: false) (Since: 2.10)<br />
&quot;websocket: boolean&quot; (optional)</p>
<p>enable websocket protocol on server<br />
sockets (default: false) (Since: 3.1)<br />
&quot;reconnect: int&quot; (optional)</p>
<p>For a client socket, if a socket is disconnected,<br />
then attempt a reconnect after the given number of seconds.<br />
Setting this to zero disables this function. (default: 0)<br />
(Since: 2.2)<br />
The members of &quot;ChardevCommon&quot; <code>Since:</code> 1.4 <code>ChardevUdp</code> (Object) Configuration info for datagram socket chardevs. <code>Members:</code></p>
<dl>
<dt>&quot;remote: SocketAddressLegacy&quot;</p>
<dd>remote address</p>
<dt>&quot;local: SocketAddressLegacy&quot; (optional)</p>
<dd>local address</p>
<dt>The members of &quot;ChardevCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.5 <code>ChardevMux</code> (Object) Configuration info for mux chardevs. <code>Members:</code></p>
<dl>
<dt>&quot;chardev: string&quot;</p>
<dd>name of the base chardev.</p>
<dt>The members of &quot;ChardevCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.5 <code>ChardevStdio</code> (Object) Configuration info for stdio chardevs. <code>Members:</code></p>
<dl>
<dt>&quot;signal: boolean&quot; (optional)</p>
<dd>Allow signals (such as <font SIZE="-1">SIGINT</font> triggered by ^C) be delivered to qemu. Default: true in -nographic mode, false otherwise.</p>
<dt>The members of &quot;ChardevCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.5 <code>ChardevSpiceChannel</code> (Object) Configuration info for spice vm channel chardevs. <code>Members:</code></p>
<dl>
<dt>&quot;type: string&quot;</p>
<dd>kind of channel (for example vdagent).</p>
<dt>The members of &quot;ChardevCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.5 <code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <code>ChardevSpicePort</code> (Object) Configuration info for spice port chardevs. <code>Members:</code></p>
<dl>
<dt>&quot;fqdn: string&quot;</p>
<dd>name of the channel (see docs/spice-port-fqdn.txt)</p>
<dt>The members of &quot;ChardevCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.5 <code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <code>ChardevVC</code> (Object) Configuration info for virtual console chardevs. <code>Members:</code></p>
<dl>
<dt>&quot;width: int&quot; (optional)</p>
<dd>console width, in pixels</p>
<dt>&quot;height: int&quot; (optional)</p>
<dd>console height, in pixels</p>
<dt>&quot;cols: int&quot; (optional)</p>
<dd>console width, in chars</p>
<dt>&quot;rows: int&quot; (optional)</p>
<dd>console height, in chars</p>
<dt>The members of &quot;ChardevCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.5 <code>ChardevRingbuf</code> (Object) Configuration info for ring buffer chardevs. <code>Members:</code></p>
<dl>
<dt>&quot;size: int&quot; (optional)</p>
<dd>ring buffer size, must be power of two, default is 65536</p>
<dt>The members of &quot;ChardevCommon&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.5 <code>ChardevBackend</code> (Object) Configuration info for the new chardev backend. <code>Members:</code></p>
<dl>
<dt>&quot;type&quot;</p>
<dd>One of &#8220;file&#8221;, &#8220;serial&#8221;, &#8220;parallel&#8221;, &#8220;pipe&#8221;, &#8220;socket&#8221;, &#8220;udp&#8221;, &#8220;pty&#8221;, &#8220;null&#8221;, &#8220;mux&#8221;, &#8220;msmouse&#8221;, &#8220;wctablet&#8221;, &#8220;braille&#8221;, &#8220;testdev&#8221;, &#8220;stdio&#8221;, &#8220;console&#8221;, &#8220;spicevmc&#8221;, &#8220;spiceport&#8221;, &#8220;vc&#8221;, &#8220;ringbuf&#8221;, &#8220;memory&#8221;</p>
<dt>&quot;data: ChardevFile&quot; when &quot;type&quot; is &quot;file&quot;</p>
<dd>
<dt>&quot;data: ChardevHostdev&quot; when &quot;type&quot; is &quot;serial&quot;</p>
<dd>
<dt>&quot;data: ChardevHostdev&quot; when &quot;type&quot; is &quot;parallel&quot;</p>
<dd>
<dt>&quot;data: ChardevHostdev&quot; when &quot;type&quot; is &quot;pipe&quot;</p>
<dd>
<dt>&quot;data: ChardevSocket&quot; when &quot;type&quot; is &quot;socket&quot;</p>
<dd>
<dt>&quot;data: ChardevUdp&quot; when &quot;type&quot; is &quot;udp&quot;</p>
<dd>
<dt>&quot;data: ChardevCommon&quot; when &quot;type&quot; is &quot;pty&quot;</p>
<dd>
<dt>&quot;data: ChardevCommon&quot; when &quot;type&quot; is &quot;null&quot;</p>
<dd>
<dt>&quot;data: ChardevMux&quot; when &quot;type&quot; is &quot;mux&quot;</p>
<dd>
<dt>&quot;data: ChardevCommon&quot; when &quot;type&quot; is &quot;msmouse&quot;</p>
<dd>
<dt>&quot;data: ChardevCommon&quot; when &quot;type&quot; is &quot;wctablet&quot;</p>
<dd>
<dt>&quot;data: ChardevCommon&quot; when &quot;type&quot; is &quot;braille&quot;</p>
<dd>
<dt>&quot;data: ChardevCommon&quot; when &quot;type&quot; is &quot;testdev&quot;</p>
<dd>
<dt>&quot;data: ChardevStdio&quot; when &quot;type&quot; is &quot;stdio&quot;</p>
<dd>
<dt>&quot;data: ChardevCommon&quot; when &quot;type&quot; is &quot;console&quot;</p>
<dd>
<dt>&quot;data: ChardevSpiceChannel&quot; when &quot;type&quot; is &quot;spicevmc&quot; (<code>If:</code> &quot;defined(CONFIG_SPICE)&quot;)</p>
<dd>
<dt>&quot;data: ChardevSpicePort&quot; when &quot;type&quot; is &quot;spiceport&quot; (<code>If:</code> &quot;defined(CONFIG_SPICE)&quot;)</p>
<dd>
<dt>&quot;data: ChardevVC&quot; when &quot;type&quot; is &quot;vc&quot;</p>
<dd>
<dt>&quot;data: ChardevRingbuf&quot; when &quot;type&quot; is &quot;ringbuf&quot;</p>
<dd>
<dt>&quot;data: ChardevRingbuf&quot; when &quot;type&quot; is &quot;memory&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.4 (testdev since 2.2, wctablet since 2.9) <code>ChardevReturn</code> (Object) Return info about the chardev backend just created. <code>Members:</code></p>
<dl>
<dt>&quot;pty: string&quot; (optional)</p>
<dd>name of the slave pseudoterminal device, present if and only if a chardev of type &#8216;pty&#8217; was created</dl>
<p> <code>Since:</code> 1.4 <code>chardev-add</code> (Command) Add a character device backend <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>the chardev&#8217;s <font SIZE="-1">ID,</font> must be unique</p>
<dt>&quot;backend: ChardevBackend&quot;</p>
<dd>backend type and parameters</dl>
<p> <code>Returns:</code> ChardevReturn. <code>Since:</code> 1.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;chardev-add&quot;,<br />
   &quot;arguments&quot; : {&quot;id&quot; : &quot;foo&quot;,<br />
                  &quot;backend&quot; : {&quot;type&quot; : &quot;null&quot;, &quot;data&quot; : {}}}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
    }</p>
<p>        -&gt; {&quot;execute&quot; : &quot;chardev-add&quot;,<br />
            &quot;arguments&quot; : {&quot;id&quot; : &quot;bar&quot;,<br />
                           &quot;backend&quot; : {&quot;type&quot; : &quot;file&quot;,<br />
                                        &quot;data&quot; : {&quot;out&quot; : &quot;/tmp/bar.log&quot;}}}} &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
        }</p>
<p>            -&gt; {&quot;execute&quot; : &quot;chardev-add&quot;,<br />
                &quot;arguments&quot; : {&quot;id&quot; : &quot;baz&quot;,<br />
                               &quot;backend&quot; : {&quot;type&quot; : &quot;pty&quot;, &quot;data&quot; : {}}}} &lt; &#8211;<br />
        {<br />
            &quot;return&quot;:<br />
            {<br />
                &quot;pty&quot; : &quot;/dev/pty/42&quot;<br />
            }<br />
        } <code>chardev-change</code> (Command) Change a character device backend <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>the chardev&#8217;s <font SIZE="-1">ID,</font> must exist</p>
<dt>&quot;backend: ChardevBackend&quot;</p>
<dd>new backend type and parameters</dl>
<p> <code>Returns:</code> ChardevReturn. <code>Since:</code> 2.10 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;chardev-change&quot;,<br />
   &quot;arguments&quot; : {&quot;id&quot; : &quot;baz&quot;,<br />
                  &quot;backend&quot; : {&quot;type&quot; : &quot;pty&quot;, &quot;data&quot; : {}}}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;pty&quot; : &quot;/dev/pty/42&quot;<br />
    }<br />
    }</p>
<p>        -&gt; {&quot;execute&quot; : &quot;chardev-change&quot;,<br />
            &quot;arguments&quot; : {<br />
                &quot;id&quot; : &quot;charchannel2&quot;,<br />
                &quot;backend&quot; : {<br />
                    &quot;type&quot; : &quot;socket&quot;,<br />
                    &quot;data&quot; : {<br />
                        &quot;addr&quot; : {<br />
                            &quot;type&quot; : &quot;unix&quot;,<br />
                            &quot;data&quot; : {<br />
                                &quot;path&quot; : &quot;/tmp/charchannel2.socket&quot;<br />
                            }<br />
                        },<br />
                        &quot;server&quot; : true,<br />
                        &quot;wait&quot; : false<br />
                    }<br />
                }<br />
            }} &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
    } <code>chardev-remove</code> (Command) Remove a character device backend <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>the chardev&#8217;s <font SIZE="-1">ID,</font> must exist and not be in use</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 1.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;chardev-remove&quot;, &quot;arguments&quot; : {&quot;id&quot; : &quot;foo&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>chardev-send-break</code> (Command) Send a break to a character device <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>the chardev&#8217;s <font SIZE="-1">ID,</font> must exist</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 2.10 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;chardev-send-break&quot;, &quot;arguments&quot; : {&quot;id&quot; : &quot;foo&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <font SIZE="-1"><code>VSERPORT_CHANGE</code></font> (Event) Emitted when the guest opens or closes a virtio-serial port. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>device identifier of the virtio-serial port</p>
<dt>&quot;open: boolean&quot;</p>
<dd>true if the guest has opened the virtio-serial port</dl>
<p> <code>Since:</code> 2.1 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;VSERPORT_CHANGE&quot;,
 &quot;data&quot;: { &quot;id&quot;: &quot;channel0&quot;, &quot;open&quot;: true },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1401385907, &quot;microseconds&quot;: 422329 } }</pre>
<h3>Dump guest memory</h3>
<p><code>DumpGuestMemoryFormat</code> (Enum) An enumeration of guest-memory-dump&#8217;s format. <code>Values:</code></p>
<dl>
<dt>&quot;elf&quot;</p>
<dd>elf format</p>
<dt>&quot;kdump-zlib&quot;</p>
<dd>kdump-compressed format with zlib-compressed</p>
<dt>&quot;kdump-lzo&quot;</p>
<dd>kdump-compressed format with lzo-compressed</p>
<dt>&quot;kdump-snappy&quot;</p>
<dd>kdump-compressed format with snappy-compressed</p>
<dt>&quot;win-dmp&quot;</p>
<dd>Windows full crashdump format, can be used instead of <font SIZE="-1">ELF</font> converting (since 2.13)</dl>
<p> <code>Since:</code> 2.0 <code>dump-guest-memory</code> (Command) Dump guest&#8217;s memory to vmcore. It is a synchronous operation that can take very long depending on the amount of guest memory. <code>Arguments:</code></p>
<dl>
<dt>&quot;paging: boolean&quot;</p>
<dd>if true, do paging to get guest&#8217;s memory mapping. This allows using gdb to process the core file. <font SIZE="-1">IMPORTANT:</font> this option can make <font SIZE="-1">QEMU</font> allocate several gigabytes of <font SIZE="-1">RAM.</font> This can happen for a large guest, or a malicious guest pretending to be large. Also, paging=true has the following limitations:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>The guest may be in a catastrophic state or can have corrupted memory, which cannot be trusted</p>
<dt>2.</p>
<dd>The guest can be in real-mode even if paging is enabled. For example, the guest uses <font SIZE="-1">ACPI</font> to sleep, and <font SIZE="-1">ACPI</font> sleep state goes in real-mode</p>
<dt>3.</p>
<dd>Currently only supported on i386 and x86_64.</dl>
</dl>
<dl>
<dd></dl>
<dt>&quot;protocol: string&quot;</p>
<dd>the filename or file descriptor of the vmcore. The supported protocols are:</p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>file: the protocol starts with &#8220;file:&#8221;, and the following string is the file&#8217;s path.</p>
<dt>2.</p>
<dd>fd: the protocol starts with &#8220;fd:&#8221;, and the following string is the fd&#8217;s name.</dl>
</dl>
<dl>
<dd></dl>
<dt>&quot;detach: boolean&quot; (optional)</p>
<dd>if true, <font SIZE="-1">QMP</font> will return immediately rather than waiting for the dump to finish. The user can track progress using &#8220;query-dump&#8221;. (since 2.6).</p>
<dt>&quot;begin: int&quot; (optional)</p>
<dd>if specified, the starting physical address.</p>
<dt>&quot;length: int&quot; (optional)</p>
<dd>if specified, the memory size, in bytes. If you don&#8217;t want to dump all guest&#8217;s memory, please specify the start <tt>&quot;begin&quot;</tt> and <tt>&quot;length&quot;</tt></p>
<dt>&quot;format: DumpGuestMemoryFormat&quot; (optional)</p>
<dd>if specified, the format of guest memory dump. But non-elf format is conflict with paging and filter, ie. <tt>&quot;paging&quot;</tt>, <tt>&quot;begin&quot;</tt> and <tt>&quot;length&quot;</tt> is not allowed to be specified with non-elf <tt>&quot;format&quot;</tt> at the same time (since 2.0)</dl>
<p> <code>Note:</code> All boolean arguments default to false <code>Returns:</code> nothing on success <code>Since:</code> 1.2 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;dump-guest-memory&quot;,<br />
   &quot;arguments&quot; : {&quot;protocol&quot; : &quot;fd:dump&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>DumpStatus</code> (Enum) Describe the status of a long-running background guest memory dump. <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>no dump-guest-memory has started yet.</p>
<dt>&quot;active&quot;</p>
<dd>there is one dump running in background.</p>
<dt>&quot;completed&quot;</p>
<dd>the last dump has finished successfully.</p>
<dt>&quot;failed&quot;</p>
<dd>the last dump has failed.</dl>
<p> <code>Since:</code> 2.6 <code>DumpQueryResult</code> (Object) The result format for &#8216;query-dump&#8217;. <code>Members:</code></p>
<dl>
<dt>&quot;status: DumpStatus&quot;</p>
<dd>enum of <tt>&quot;DumpStatus&quot;</tt>, which shows current dump status</p>
<dt>&quot;completed: int&quot;</p>
<dd>bytes written in latest dump (uncompressed)</p>
<dt>&quot;total: int&quot;</p>
<dd>total bytes to be written in latest dump (uncompressed)</dl>
<p> <code>Since:</code> 2.6 <code>query-dump</code> (Command) Query latest dump status. <code>Returns:</code> A <tt>&quot;DumpStatus&quot;</tt> object showing the dump status. <code>Since:</code> 2.6 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-dump&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;status&quot; : &quot;active&quot;, &quot;completed&quot; : 1024000, &quot;total&quot; : 2048000<br />
    }<br />
} <font SIZE="-1"><code>DUMP_COMPLETED</code></font> (Event) Emitted when background dump has completed <code>Arguments:</code></p>
<dl>
<dt>&quot;result: DumpQueryResult&quot;</p>
<dd>final dump status</p>
<dt>&quot;error: string&quot; (optional)</p>
<dd>human-readable error string that provides hint on why dump failed. Only presents on failure. The user should not try to interpret the error string.</dl>
<p> <code>Since:</code> 2.6 <code>Example:</code> { &quot;event&quot;: &quot;DUMP_COMPLETED&quot;,<br />
    &quot;data&quot;: {&quot;result&quot;: {&quot;total&quot;: 1090650112, &quot;status&quot;: &quot;completed&quot;,<br />
            &quot;completed&quot;: 1090650112} } } <code>DumpGuestMemoryCapability</code> (Object) A list of the available formats for dump-guest-memory <code>Members:</code></p>
<dl>
<dt>&quot;formats: array of DumpGuestMemoryFormat&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.0 <code>query-dump-guest-memory-capability</code> (Command) Returns the available formats for dump-guest-memory <code>Returns:</code> A <tt>&quot;DumpGuestMemoryCapability&quot;</tt> object listing available formats for dump-guest-memory <code>Since:</code> 2.0 <code>Example:</code> </p>
<pre> -&gt; { &quot;execute&quot;: &quot;query-dump-guest-memory-capability&quot; }
 &lt;- { &quot;return&quot;: { &quot;formats&quot;:
 [&quot;elf&quot;, &quot;kdump-zlib&quot;, &quot;kdump-lzo&quot;, &quot;kdump-snappy&quot;] }</pre>
<h3>Net devices</h3>
<p><code>set_link</code> (Command) Sets the link status of a virtual network adapter. <code>Arguments:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>the device name of the virtual network adapter</p>
<dt>&quot;up: boolean&quot;</p>
<dd>true to set the link status to be up</dl>
<p> <code>Returns:</code> Nothing on success If <tt>&quot;name&quot;</tt> is not a valid network device, DeviceNotFound <code>Since:</code> 0.14.0 <code>Notes:</code> Not all network adapters support setting link status. This command will succeed even if the network adapter does not support link status notification. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;set_link&quot;,<br />
   &quot;arguments&quot; : {&quot;name&quot; : &quot;e1000.0&quot;, &quot;up&quot; : false}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>netdev_add</code> (Command) Add a network backend. <code>Arguments:</code></p>
<dl>
<dt>&quot;type: string&quot;</p>
<dd>the type of network backend. Possible values are listed in NetClientDriver (excluding &#8216;none&#8217; and &#8216;nic&#8217;)</p>
<dt>&quot;id: string&quot;</p>
<dd>the name of the new network backend</dl>
<p> Additional arguments depend on the type. <font SIZE="-1"><code>TODO:</code></font> This command effectively bypasses <font SIZE="-1">QAPI</font> completely due to its &#8220;additional arguments&#8221; business. It shouldn&#8217;t have been added to the schema in this form. It should be qapified properly, or replaced by a properly qapified command. <code>Since:</code> 0.14.0 <code>Returns:</code> Nothing on success If <tt>&quot;type&quot;</tt> is not a valid network backend, DeviceNotFound <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;netdev_add&quot;,<br />
   &quot;arguments&quot; : {&quot;type&quot; : &quot;user&quot;, &quot;id&quot; : &quot;netdev1&quot;, &quot;dnssearch&quot; : &quot;example.org&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>netdev_del</code> (Command) Remove a network backend. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>the name of the network backend to remove</dl>
<p> <code>Returns:</code> Nothing on success If <tt>&quot;id&quot;</tt> is not a valid network backend, DeviceNotFound <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;netdev_del&quot;, &quot;arguments&quot; : {&quot;id&quot; : &quot;netdev1&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>NetLegacyNicOptions</code> (Object) Create a new Network Interface Card. <code>Members:</code></p>
<dl>
<dt>&quot;netdev: string&quot; (optional)</p>
<dd>id of -netdev to connect to</p>
<dt>&quot;macaddr: string&quot; (optional)</p>
<dd><font SIZE="-1">MAC</font> address</p>
<dt>&quot;model: string&quot; (optional)</p>
<dd>device model (e1000, rtl8139, virtio etc.)</p>
<dt>&quot;addr: string&quot; (optional)</p>
<dd><font SIZE="-1">PCI</font> device address</p>
<dt>&quot;vectors: int&quot; (optional)</p>
<dd>number of MSI-x vectors, 0 to disable MSI-X</dl>
<p> <code>Since:</code> 1.2 <code>NetdevUserOptions</code> (Object) Use the user mode network stack which requires no administrator privilege to run. <code>Members:</code></p>
<dl>
<dt>&quot;hostname: string&quot; (optional)</p>
<dd>client hostname reported by the builtin <font SIZE="-1">DHCP</font> server</p>
<dt>&quot;restrict: boolean&quot; (optional)</p>
<dd>isolate the guest from the host</p>
<dt>&quot;ipv4: boolean&quot; (optional)</p>
<dd>whether to support IPv4, default true for enabled (since 2.6)</p>
<dt>&quot;ipv6: boolean&quot; (optional)</p>
<dd>whether to support IPv6, default true for enabled (since 2.6)</p>
<dt>&quot;ip: string&quot; (optional)</p>
<dd>legacy parameter, use net= instead</p>
<dt>&quot;net: string&quot; (optional)</p>
<dd><font SIZE="-1">IP</font> network address that the guest will see, in the form addr[/netmask] The netmask is optional, and can be either in the form a.b.c.d or as a number of valid top-most bits. Default is 10.0.2.0/24.</p>
<dt>&quot;host: string&quot; (optional)</p>
<dd>guest-visible address of the host</p>
<dt>&quot;tftp: string&quot; (optional)</p>
<dd>root directory of the built-in <font SIZE="-1">TFTP</font> server</p>
<dt>&quot;bootfile: string&quot; (optional)</p>
<dd><font SIZE="-1">BOOTP</font> filename, for use with tftp=</p>
<dt>&quot;dhcpstart: string&quot; (optional)</p>
<dd>the first of the 16 IPs the built-in <font SIZE="-1">DHCP</font> server can assign</p>
<dt>&quot;dns: string&quot; (optional)</p>
<dd>guest-visible address of the virtual nameserver</p>
<dt>&quot;dnssearch: array of String&quot; (optional)</p>
<dd>list of <font SIZE="-1">DNS</font> suffixes to search, passed as <font SIZE="-1">DHCP</font> option to the guest</p>
<dt>&quot;domainname: string&quot; (optional)</p>
<dd>guest-visible domain name of the virtual nameserver (since 3.0)</p>
<dt>&quot;ipv6-prefix: string&quot; (optional)</p>
<dd>IPv6 network prefix (default is fec0::) (since 2.6). The network prefix is given in the usual hexadecimal IPv6 address notation.</p>
<dt>&quot;ipv6-prefixlen: int&quot; (optional)</p>
<dd>IPv6 network prefix length (default is 64) (since 2.6)</p>
<dt>&quot;ipv6-host: string&quot; (optional)</p>
<dd>guest-visible IPv6 address of the host (since 2.6)</p>
<dt>&quot;ipv6-dns: string&quot; (optional)</p>
<dd>guest-visible IPv6 address of the virtual nameserver (since 2.6)</p>
<dt>&quot;smb: string&quot; (optional)</p>
<dd>root directory of the built-in <font SIZE="-1">SMB</font> server</p>
<dt>&quot;smbserver: string&quot; (optional)</p>
<dd><font SIZE="-1">IP</font> address of the built-in <font SIZE="-1">SMB</font> server</p>
<dt>&quot;hostfwd: array of String&quot; (optional)</p>
<dd>redirect incoming <font SIZE="-1">TCP</font> or <font SIZE="-1">UDP</font> host connections to guest endpoints</p>
<dt>&quot;guestfwd: array of String&quot; (optional)</p>
<dd>forward guest <font SIZE="-1">TCP</font> connections</p>
<dt>&quot;tftp-server-name: string&quot; (optional)</p>
<dd><font SIZE="-1">RFC2132 &#8220;TFTP</font> server name&#8221; string (Since 3.1)</dl>
<p> <code>Since:</code> 1.2 <code>NetdevTapOptions</code> (Object) Used to configure a host <font SIZE="-1">TAP</font> network interface backend. <code>Members:</code></p>
<dl>
<dt>&quot;ifname: string&quot; (optional)</p>
<dd>interface name</p>
<dt>&quot;fd: string&quot; (optional)</p>
<dd>file descriptor of an already opened tap</p>
<dt>&quot;fds: string&quot; (optional)</p>
<dd>multiple file descriptors of already opened multiqueue capable tap</p>
<dt>&quot;script: string&quot; (optional)</p>
<dd>script to initialize the interface</p>
<dt>&quot;downscript: string&quot; (optional)</p>
<dd>script to shut down the interface</p>
<dt>&quot;br: string&quot; (optional)</p>
<dd>bridge name (since 2.8)</p>
<dt>&quot;helper: string&quot; (optional)</p>
<dd>command to execute to configure bridge</p>
<dt>&quot;sndbuf: int&quot; (optional)</p>
<dd>send buffer limit. Understands [TGMKkb] suffixes.</p>
<dt>&quot;vnet_hdr: boolean&quot; (optional)</p>
<dd>enable the <font SIZE="-1">IFF_VNET_HDR</font> flag on the tap interface</p>
<dt>&quot;vhost: boolean&quot; (optional)</p>
<dd>enable vhost-net network accelerator</p>
<dt>&quot;vhostfd: string&quot; (optional)</p>
<dd>file descriptor of an already opened vhost net device</p>
<dt>&quot;vhostfds: string&quot; (optional)</p>
<dd>file descriptors of multiple already opened vhost net devices</p>
<dt>&quot;vhostforce: boolean&quot; (optional)</p>
<dd>vhost on for non-MSIX virtio guests</p>
<dt>&quot;queues: int&quot; (optional)</p>
<dd>number of queues to be created for multiqueue capable tap</p>
<dt>&quot;poll-us: int&quot; (optional)</p>
<dd>maximum number of microseconds that could be spent on busy polling for tap (since 2.7)</dl>
<p> <code>Since:</code> 1.2 <code>NetdevSocketOptions</code> (Object) Socket netdevs are used to establish a network connection to another <font SIZE="-1">QEMU</font> virtual machine via a <font SIZE="-1">TCP</font> socket. <code>Members:</code></p>
<dl>
<dt>&quot;fd: string&quot; (optional)</p>
<dd>file descriptor of an already opened socket</p>
<dt>&quot;listen: string&quot; (optional)</p>
<dd>port number, and optional hostname, to listen on</p>
<dt>&quot;connect: string&quot; (optional)</p>
<dd>port number, and optional hostname, to connect to</p>
<dt>&quot;mcast: string&quot; (optional)</p>
<dd><font SIZE="-1">UDP</font> multicast address and port number</p>
<dt>&quot;localaddr: string&quot; (optional)</p>
<dd>source address and port for multicast and udp packets</p>
<dt>&quot;udp: string&quot; (optional)</p>
<dd><font SIZE="-1">UDP</font> unicast address and port number</dl>
<p> <code>Since:</code> 1.2 <code>NetdevL2TPv3Options</code> (Object) Configure an Ethernet over L2TPv3 tunnel. <code>Members:</code></p>
<dl>
<dt>&quot;src: string&quot;</p>
<dd>source address</p>
<dt>&quot;dst: string&quot;</p>
<dd>destination address</p>
<dt>&quot;srcport: string&quot; (optional)</p>
<dd>source port &#8211; mandatory for udp, optional for ip</p>
<dt>&quot;dstport: string&quot; (optional)</p>
<dd>destination port &#8211; mandatory for udp, optional for ip</p>
<dt>&quot;ipv6: boolean&quot; (optional)</p>
<dd>force the use of ipv6</p>
<dt>&quot;udp: boolean&quot; (optional)</p>
<dd>use the udp version of l2tpv3 encapsulation</p>
<dt>&quot;cookie64: boolean&quot; (optional)</p>
<dd>use 64 bit coookies</p>
<dt>&quot;counter: boolean&quot; (optional)</p>
<dd>have sequence counter</p>
<dt>&quot;pincounter: boolean&quot; (optional)</p>
<dd>pin sequence counter to zero &#8211; workaround for buggy implementations or networks with packet reorder</p>
<dt>&quot;txcookie: int&quot; (optional)</p>
<dd>32 or 64 bit transmit cookie</p>
<dt>&quot;rxcookie: int&quot; (optional)</p>
<dd>32 or 64 bit receive cookie</p>
<dt>&quot;txsession: int&quot;</p>
<dd>32 bit transmit session</p>
<dt>&quot;rxsession: int&quot; (optional)</p>
<dd>32 bit receive session &#8211; if not specified set to the same value as transmit</p>
<dt>&quot;offset: int&quot; (optional)</p>
<dd>additional offset &#8211; allows the insertion of additional application-specific data before the packet payload</dl>
<p> <code>Since:</code> 2.1 <code>NetdevVdeOptions</code> (Object) Connect to a vde switch running on the host. <code>Members:</code></p>
<dl>
<dt>&quot;sock: string&quot; (optional)</p>
<dd>socket path</p>
<dt>&quot;port: int&quot; (optional)</p>
<dd>port number</p>
<dt>&quot;group: string&quot; (optional)</p>
<dd>group owner of socket</p>
<dt>&quot;mode: int&quot; (optional)</p>
<dd>permissions for socket</dl>
<p> <code>Since:</code> 1.2 <code>NetdevBridgeOptions</code> (Object) Connect a host <font SIZE="-1">TAP</font> network interface to a host bridge device. <code>Members:</code></p>
<dl>
<dt>&quot;br: string&quot; (optional)</p>
<dd>bridge name</p>
<dt>&quot;helper: string&quot; (optional)</p>
<dd>command to execute to configure bridge</dl>
<p> <code>Since:</code> 1.2 <code>NetdevHubPortOptions</code> (Object) Connect two or more net clients through a software hub. <code>Members:</code></p>
<dl>
<dt>&quot;hubid: int&quot;</p>
<dd>hub identifier number</p>
<dt>&quot;netdev: string&quot; (optional)</p>
<dd>used to connect hub to a netdev instead of a device (since 2.12)</dl>
<p> <code>Since:</code> 1.2 <code>NetdevNetmapOptions</code> (Object) Connect a client to a netmap-enabled <font SIZE="-1">NIC</font> or to a <font SIZE="-1">VALE</font> switch port <code>Members:</code></p>
<dl>
<dt>&quot;ifname: string&quot;</p>
<dd>Either the name of an existing network interface supported by netmap, or the name of a <font SIZE="-1">VALE</font> port (created on the fly). A <font SIZE="-1">VALE</font> port name is in the form &#8216;valeXXX:YYY&#8217;, where <font SIZE="-1">XXX</font> and <font SIZE="-1">YYY</font> are non-negative integers. <font SIZE="-1">XXX</font> identifies a switch and <font SIZE="-1">YYY</font> identifies a port of the switch. <font SIZE="-1">VALE</font> ports having the same <font SIZE="-1">XXX</font> are therefore connected to the same switch.</p>
<dt>&quot;devname: string&quot; (optional)</p>
<dd>path of the netmap device (default: &#8216;/dev/netmap&#8217;).</dl>
<p> <code>Since:</code> 2.0 <code>NetdevVhostUserOptions</code> (Object) Vhost-user network backend <code>Members:</code></p>
<dl>
<dt>&quot;chardev: string&quot;</p>
<dd>name of a unix socket chardev</p>
<dt>&quot;vhostforce: boolean&quot; (optional)</p>
<dd>vhost on for non-MSIX virtio guests (default: false).</p>
<dt>&quot;queues: int&quot; (optional)</p>
<dd>number of queues to be created for multiqueue vhost-user (default: 1) (Since 2.5)</dl>
<p> <code>Since:</code> 2.1 <code>NetClientDriver</code> (Enum) Available netdev drivers. <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>Not documented</p>
<dt>&quot;nic&quot;</p>
<dd>Not documented</p>
<dt>&quot;user&quot;</p>
<dd>Not documented</p>
<dt>&quot;tap&quot;</p>
<dd>Not documented</p>
<dt>&quot;l2tpv3&quot;</p>
<dd>Not documented</p>
<dt>&quot;socket&quot;</p>
<dd>Not documented</p>
<dt>&quot;vde&quot;</p>
<dd>Not documented</p>
<dt>&quot;bridge&quot;</p>
<dd>Not documented</p>
<dt>&quot;hubport&quot;</p>
<dd>Not documented</p>
<dt>&quot;netmap&quot;</p>
<dd>Not documented</p>
<dt>&quot;vhost-user&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.7 &#8216;dump&#8217;: dropped in 2.12 <code>Netdev</code> (Object) Captures the configuration of a network device. <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>identifier for monitor commands.</p>
<dt>&quot;type: NetClientDriver&quot;</p>
<dd>Specify the driver used for interpreting remaining arguments.</p>
<dt>The members of &quot;NetLegacyNicOptions&quot; when &quot;type&quot; is &quot;nic&quot;</p>
<dd>
<dt>The members of &quot;NetdevUserOptions&quot; when &quot;type&quot; is &quot;user&quot;</p>
<dd>
<dt>The members of &quot;NetdevTapOptions&quot; when &quot;type&quot; is &quot;tap&quot;</p>
<dd>
<dt>The members of &quot;NetdevL2TPv3Options&quot; when &quot;type&quot; is &quot;l2tpv3&quot;</p>
<dd>
<dt>The members of &quot;NetdevSocketOptions&quot; when &quot;type&quot; is &quot;socket&quot;</p>
<dd>
<dt>The members of &quot;NetdevVdeOptions&quot; when &quot;type&quot; is &quot;vde&quot;</p>
<dd>
<dt>The members of &quot;NetdevBridgeOptions&quot; when &quot;type&quot; is &quot;bridge&quot;</p>
<dd>
<dt>The members of &quot;NetdevHubPortOptions&quot; when &quot;type&quot; is &quot;hubport&quot;</p>
<dd>
<dt>The members of &quot;NetdevNetmapOptions&quot; when &quot;type&quot; is &quot;netmap&quot;</p>
<dd>
<dt>The members of &quot;NetdevVhostUserOptions&quot; when &quot;type&quot; is &quot;vhost-user&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.2 &#8216;l2tpv3&#8217; &#8211; since 2.1 <code>NetLegacy</code> (Object) Captures the configuration of a network device; legacy. <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot; (optional)</p>
<dd>identifier for monitor commands</p>
<dt>&quot;name: string&quot; (optional)</p>
<dd>identifier for monitor commands, ignored if <tt>&quot;id&quot;</tt> is present</p>
<dt>&quot;opts: NetLegacyOptions&quot;</p>
<dd>device type specific properties (legacy)</dl>
<p> <code>Since:</code> 1.2 &#8216;vlan&#8217;: dropped in 3.0 <code>NetLegacyOptionsType</code> (Enum) <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>Not documented</p>
<dt>&quot;nic&quot;</p>
<dd>Not documented</p>
<dt>&quot;user&quot;</p>
<dd>Not documented</p>
<dt>&quot;tap&quot;</p>
<dd>Not documented</p>
<dt>&quot;l2tpv3&quot;</p>
<dd>Not documented</p>
<dt>&quot;socket&quot;</p>
<dd>Not documented</p>
<dt>&quot;vde&quot;</p>
<dd>Not documented</p>
<dt>&quot;bridge&quot;</p>
<dd>Not documented</p>
<dt>&quot;netmap&quot;</p>
<dd>Not documented</p>
<dt>&quot;vhost-user&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 1.2 <code>NetLegacyOptions</code> (Object) Like Netdev, but for use only by the legacy command line options <code>Members:</code></p>
<dl>
<dt>&quot;type: NetLegacyOptionsType&quot;</p>
<dd>Not documented</p>
<dt>The members of &quot;NetLegacyNicOptions&quot; when &quot;type&quot; is &quot;nic&quot;</p>
<dd>
<dt>The members of &quot;NetdevUserOptions&quot; when &quot;type&quot; is &quot;user&quot;</p>
<dd>
<dt>The members of &quot;NetdevTapOptions&quot; when &quot;type&quot; is &quot;tap&quot;</p>
<dd>
<dt>The members of &quot;NetdevL2TPv3Options&quot; when &quot;type&quot; is &quot;l2tpv3&quot;</p>
<dd>
<dt>The members of &quot;NetdevSocketOptions&quot; when &quot;type&quot; is &quot;socket&quot;</p>
<dd>
<dt>The members of &quot;NetdevVdeOptions&quot; when &quot;type&quot; is &quot;vde&quot;</p>
<dd>
<dt>The members of &quot;NetdevBridgeOptions&quot; when &quot;type&quot; is &quot;bridge&quot;</p>
<dd>
<dt>The members of &quot;NetdevNetmapOptions&quot; when &quot;type&quot; is &quot;netmap&quot;</p>
<dd>
<dt>The members of &quot;NetdevVhostUserOptions&quot; when &quot;type&quot; is &quot;vhost-user&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.2 <code>NetFilterDirection</code> (Enum) Indicates whether a netfilter is attached to a netdev&#8217;s transmit queue or receive queue or both. <code>Values:</code></p>
<dl>
<dt>&quot;all&quot;</p>
<dd>the filter is attached both to the receive and the transmit queue of the netdev (default).</p>
<dt>&quot;rx&quot;</p>
<dd>the filter is attached to the receive queue of the netdev, where it will receive packets sent to the netdev.</p>
<dt>&quot;tx&quot;</p>
<dd>the filter is attached to the transmit queue of the netdev, where it will receive packets sent by the netdev.</dl>
<p> <code>Since:</code> 2.5 <code>RxState</code> (Enum) Packets receiving state <code>Values:</code></p>
<dl>
<dt>&quot;normal&quot;</p>
<dd>filter assigned packets according to the mac-table</p>
<dt>&quot;none&quot;</p>
<dd>don&#8217;t receive any assigned packet</p>
<dt>&quot;all&quot;</p>
<dd>receive all assigned packets</dl>
<p> <code>Since:</code> 1.6 <code>RxFilterInfo</code> (Object) Rx-filter information for a <font SIZE="-1">NIC.</font> <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>net client name</p>
<dt>&quot;promiscuous: boolean&quot;</p>
<dd>whether promiscuous mode is enabled</p>
<dt>&quot;multicast: RxState&quot;</p>
<dd>multicast receive state</p>
<dt>&quot;unicast: RxState&quot;</p>
<dd>unicast receive state</p>
<dt>&quot;vlan: RxState&quot;</p>
<dd>vlan receive state (Since 2.0)</p>
<dt>&quot;broadcast-allowed: boolean&quot;</p>
<dd>whether to receive broadcast</p>
<dt>&quot;multicast-overflow: boolean&quot;</p>
<dd>multicast table is overflowed or not</p>
<dt>&quot;unicast-overflow: boolean&quot;</p>
<dd>unicast table is overflowed or not</p>
<dt>&quot;main-mac: string&quot;</p>
<dd>the main macaddr string</p>
<dt>&quot;vlan-table: array of int&quot;</p>
<dd>a list of active vlan id</p>
<dt>&quot;unicast-table: array of string&quot;</p>
<dd>a list of unicast macaddr string</p>
<dt>&quot;multicast-table: array of string&quot;</p>
<dd>a list of multicast macaddr string</dl>
<p> <code>Since:</code> 1.6 <code>query-rx-filter</code> (Command) Return rx-filter information for all NICs (or for the given <font SIZE="-1">NIC</font>). <code>Arguments:</code></p>
<dl>
<dt>&quot;name: string&quot; (optional)</p>
<dd>net client name</dl>
<p> <code>Returns:</code> list of <tt>&quot;RxFilterInfo&quot;</tt> for all NICs (or for the given <font SIZE="-1">NIC</font>). Returns an error if the given <tt>&quot;name&quot;</tt> doesn&#8217;t exist, or given <font SIZE="-1">NIC</font> doesn&#8217;t support rx-filter querying, or given net client isn&#8217;t a <font SIZE="-1">NIC.</font> <code>Since:</code> 1.6 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-rx-filter&quot;, &quot;arguments&quot; : {&quot;name&quot; : &quot;vnet0&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;promiscuous&quot; : true,<br />
            &quot;name&quot; : &quot;vnet0&quot;,<br />
            &quot;main-mac&quot; : &quot;52:54:00:12:34:56&quot;,<br />
            &quot;unicast&quot; : &quot;normal&quot;,<br />
            &quot;vlan&quot; : &quot;normal&quot;,<br />
            &quot;vlan-table&quot; : [<br />
                4,<br />
                0<br />
            ],<br />
            &quot;unicast-table&quot; : [<br />
            ],<br />
            &quot;multicast&quot; : &quot;normal&quot;,<br />
            &quot;multicast-overflow&quot; : false,<br />
            &quot;unicast-overflow&quot; : false,<br />
            &quot;multicast-table&quot; : [<br />
                &quot;01:00:5e:00:00:01&quot;,<br />
                &quot;33:33:00:00:00:01&quot;,<br />
                &quot;33:33:ff:12:34:56&quot;<br />
            ],<br />
            &quot;broadcast-allowed&quot; : false<br />
        }<br />
    ]<br />
} <font SIZE="-1"><code>NIC_RX_FILTER_CHANGED</code></font> (Event) Emitted once until the &#8216;query-rx-filter&#8217; command is executed, the first event will always be emitted <code>Arguments:</code></p>
<dl>
<dt>&quot;name: string&quot; (optional)</p>
<dd>net client name</p>
<dt>&quot;path: string&quot;</p>
<dd>device path</dl>
<p> <code>Since:</code> 1.6 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;NIC_RX_FILTER_CHANGED&quot;,
 &quot;data&quot;: { &quot;name&quot;: &quot;vnet0&quot;,
 &quot;path&quot;: &quot;/machine/peripheral/vnet0/virtio-backend&quot; },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1368697518, &quot;microseconds&quot;: 326866 } }
 }</pre>
<p><code>AnnounceParameters</code> (Object) Parameters for self-announce timers <code>Members:</code></p>
<dl>
<dt>&quot;initial: int&quot;</p>
<dd>Initial delay (in ms) before sending the first <font SIZE="-1">GARP/RARP</font> announcement</p>
<dt>&quot;max: int&quot;</p>
<dd>Maximum delay (in ms) between <font SIZE="-1">GARP/RARP</font> announcement packets</p>
<dt>&quot;rounds: int&quot;</p>
<dd>Number of self-announcement attempts</p>
<dt>&quot;step: int&quot;</p>
<dd>Delay increase (in ms) after each self-announcement attempt</p>
<dt>&quot;interfaces: array of string&quot; (optional)</p>
<dd>An optional list of interface names, which restricts the announcement to the listed interfaces. (Since 4.1)</p>
<dt>&quot;id: string&quot; (optional)</p>
<dd>A name to be used to identify an instance of announce-timers and to allow it to modified later. Not for use as part of the migration parameters. (Since 4.1)</dl>
<p> <code>Since:</code> 4.0 <code>announce-self</code> (Command) Trigger generation of broadcast <font SIZE="-1">RARP</font> frames to update network switches. This can be useful when network bonds fail-over the active slave. <code>Arguments:</code> the members of <tt>&quot;AnnounceParameters&quot;</tt> <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;announce-self&quot;,<br />
   &quot;arguments&quot; : {<br />
       &quot;initial&quot; : 50,<br />
       &quot;max&quot; : 550,<br />
       &quot;rounds&quot; : 10,<br />
       &quot;step&quot; : 50,<br />
       &quot;interfaces&quot; : [ &quot;vn2&quot;, &quot;vn3&quot; ],<br />
       &quot;id&quot; : &quot;bob&quot;<br />
   }} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>Since:</code> 4.0 <font SIZE="-1"><code>FAILOVER_NEGOTIATED</code></font> (Event) Emitted when <font SIZE="-1">VIRTIO_NET_F_STANDBY</font> was enabled during feature negotiation. Failover primary devices which were hidden (not hotplugged when requested) before will now be hotplugged by the virtio-net standby device. device-id: <font SIZE="-1">QEMU</font> device id of the unplugged device <code>Arguments:</code></p>
<dl>
<dt>&quot;device-id: string&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 4.2 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;FAILOVER_NEGOTIATED&quot;,
 &quot;data&quot;: &quot;net1&quot; }</pre>
<h3><font SIZE="-1">RDMA</font> device</h3>
<p><font SIZE="-1"><code>RDMA_GID_STATUS_CHANGED</code></font> (Event) Emitted when guest driver adds/deletes <font SIZE="-1">GID</font> to/from device <code>Arguments:</code></p>
<dl>
<dt>&quot;netdev: string&quot;</p>
<dd>RoCE Network Device name</p>
<dt>&quot;gid-status: boolean&quot;</p>
<dd>Add or delete indication</p>
<dt>&quot;subnet-prefix: int&quot;</p>
<dd>Subnet Prefix</p>
<dt>&quot;interface-id: int&quot;</p>
<dd>Not documented</dl>
<p> <tt>&quot;interface-id&quot;</tt> : Interface <font SIZE="-1">ID</font> <code>Since:</code> 4.0 <code>Example:</code> </p>
<pre> &lt;- {&quot;timestamp&quot;: {&quot;seconds&quot;: 1541579657, &quot;microseconds&quot;: 986760},
 &quot;event&quot;: &quot;RDMA_GID_STATUS_CHANGED&quot;,
 &quot;data&quot;:
 {&quot;netdev&quot;: &quot;bridge0&quot;,
 &quot;interface-id&quot;: 15880512517475447892,
 &quot;gid-status&quot;: true,
 &quot;subnet-prefix&quot;: 33022}}</pre>
<h3>Rocker switch device</h3>
<p><code>RockerSwitch</code> (Object) Rocker switch information. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>switch name</p>
<dt>&quot;id: int&quot;</p>
<dd>switch <font SIZE="-1">ID</font></p>
<dt>&quot;ports: int&quot;</p>
<dd>number of front-panel ports</dl>
<p> <code>Since:</code> 2.4 <code>query-rocker</code> (Command) Return rocker switch information. <code>Arguments:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>Not documented</dl>
<p> <code>Returns:</code> <tt>&quot;Rocker&quot;</tt> information <code>Since:</code> 2.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-rocker&quot;, &quot;arguments&quot; : {&quot;name&quot; : &quot;sw1&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;name&quot; : &quot;sw1&quot;, &quot;ports&quot; : 2, &quot;id&quot; : 1327446905938<br />
    }<br />
} <code>RockerPortDuplex</code> (Enum) An eumeration of port duplex states. <code>Values:</code></p>
<dl>
<dt>&quot;half&quot;</p>
<dd>half duplex</p>
<dt>&quot;full&quot;</p>
<dd>full duplex</dl>
<p> <code>Since:</code> 2.4 <code>RockerPortAutoneg</code> (Enum) An eumeration of port autoneg states. <code>Values:</code></p>
<dl>
<dt>&quot;off&quot;</p>
<dd>autoneg is off</p>
<dt>&quot;on&quot;</p>
<dd>autoneg is on</dl>
<p> <code>Since:</code> 2.4 <code>RockerPort</code> (Object) Rocker switch port information. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>port name</p>
<dt>&quot;enabled: boolean&quot;</p>
<dd>port is enabled for I/O</p>
<dt>&quot;link-up: boolean&quot;</p>
<dd>physical link is <font SIZE="-1">UP</font> on port</p>
<dt>&quot;speed: int&quot;</p>
<dd>port link speed in Mbps</p>
<dt>&quot;duplex: RockerPortDuplex&quot;</p>
<dd>port link duplex</p>
<dt>&quot;autoneg: RockerPortAutoneg&quot;</p>
<dd>port link autoneg</dl>
<p> <code>Since:</code> 2.4 <code>query-rocker-ports</code> (Command) Return rocker switch port information. <code>Arguments:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>Not documented</dl>
<p> <code>Returns:</code> a list of <tt>&quot;RockerPort&quot;</tt> information <code>Since:</code> 2.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-rocker-ports&quot;, &quot;arguments&quot; : {&quot;name&quot; : &quot;sw1&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [ {&quot;duplex&quot; : &quot;full&quot;, &quot;enabled&quot; : true, &quot;name&quot; : &quot;sw1.1&quot;, &quot;autoneg&quot; : &quot;off&quot;, &quot;link-up&quot; : true, &quot;speed&quot; : 10000},<br />
                 {&quot;duplex&quot; : &quot;full&quot;, &quot;enabled&quot; : true, &quot;name&quot; : &quot;sw1.2&quot;, &quot;autoneg&quot; : &quot;off&quot;, &quot;link-up&quot; : true, &quot;speed&quot; : 10000} ]<br />
} <code>RockerOfDpaFlowKey</code> (Object) Rocker switch OF-DPA flow key <code>Members:</code></p>
<dl>
<dt>&quot;priority: int&quot;</p>
<dd>key priority, 0 being lowest priority</p>
<dt>&quot;tbl-id: int&quot;</p>
<dd>flow table <font SIZE="-1">ID</font></p>
<dt>&quot;in-pport: int&quot; (optional)</p>
<dd>physical input port</p>
<dt>&quot;tunnel-id: int&quot; (optional)</p>
<dd>tunnel <font SIZE="-1">ID</font></p>
<dt>&quot;vlan-id: int&quot; (optional)</p>
<dd><font SIZE="-1">VLAN ID</font></p>
<dt>&quot;eth-type: int&quot; (optional)</p>
<dd>Ethernet header type</p>
<dt>&quot;eth-src: string&quot; (optional)</p>
<dd>Ethernet header source <font SIZE="-1">MAC</font> address</p>
<dt>&quot;eth-dst: string&quot; (optional)</p>
<dd>Ethernet header destination <font SIZE="-1">MAC</font> address</p>
<dt>&quot;ip-proto: int&quot; (optional)</p>
<dd><font SIZE="-1">IP</font> Header protocol field</p>
<dt>&quot;ip-tos: int&quot; (optional)</p>
<dd><font SIZE="-1">IP</font> header <font SIZE="-1">TOS</font> field</p>
<dt>&quot;ip-dst: string&quot; (optional)</p>
<dd><font SIZE="-1">IP</font> header destination address</dl>
<p> <code>Note:</code> optional members may or may not appear in the flow key depending if they&#8217;re relevant to the flow key. <code>Since:</code> 2.4 <code>RockerOfDpaFlowMask</code> (Object) Rocker switch OF-DPA flow mask <code>Members:</code></p>
<dl>
<dt>&quot;in-pport: int&quot; (optional)</p>
<dd>physical input port</p>
<dt>&quot;tunnel-id: int&quot; (optional)</p>
<dd>tunnel <font SIZE="-1">ID</font></p>
<dt>&quot;vlan-id: int&quot; (optional)</p>
<dd><font SIZE="-1">VLAN ID</font></p>
<dt>&quot;eth-src: string&quot; (optional)</p>
<dd>Ethernet header source <font SIZE="-1">MAC</font> address</p>
<dt>&quot;eth-dst: string&quot; (optional)</p>
<dd>Ethernet header destination <font SIZE="-1">MAC</font> address</p>
<dt>&quot;ip-proto: int&quot; (optional)</p>
<dd><font SIZE="-1">IP</font> Header protocol field</p>
<dt>&quot;ip-tos: int&quot; (optional)</p>
<dd><font SIZE="-1">IP</font> header <font SIZE="-1">TOS</font> field</dl>
<p> <code>Note:</code> optional members may or may not appear in the flow mask depending if they&#8217;re relevant to the flow mask. <code>Since:</code> 2.4 <code>RockerOfDpaFlowAction</code> (Object) Rocker switch OF-DPA flow action <code>Members:</code></p>
<dl>
<dt>&quot;goto-tbl: int&quot; (optional)</p>
<dd>next table <font SIZE="-1">ID</font></p>
<dt>&quot;group-id: int&quot; (optional)</p>
<dd>group <font SIZE="-1">ID</font></p>
<dt>&quot;tunnel-lport: int&quot; (optional)</p>
<dd>tunnel logical port <font SIZE="-1">ID</font></p>
<dt>&quot;vlan-id: int&quot; (optional)</p>
<dd><font SIZE="-1">VLAN ID</font></p>
<dt>&quot;new-vlan-id: int&quot; (optional)</p>
<dd>new <font SIZE="-1">VLAN ID</font></p>
<dt>&quot;out-pport: int&quot; (optional)</p>
<dd>physical output port</dl>
<p> <code>Note:</code> optional members may or may not appear in the flow action depending if they&#8217;re relevant to the flow action. <code>Since:</code> 2.4 <code>RockerOfDpaFlow</code> (Object) Rocker switch OF-DPA flow <code>Members:</code></p>
<dl>
<dt>&quot;cookie: int&quot;</p>
<dd>flow unique cookie <font SIZE="-1">ID</font></p>
<dt>&quot;hits: int&quot;</p>
<dd>count of matches (hits) on flow</p>
<dt>&quot;key: RockerOfDpaFlowKey&quot;</p>
<dd>flow key</p>
<dt>&quot;mask: RockerOfDpaFlowMask&quot;</p>
<dd>flow mask</p>
<dt>&quot;action: RockerOfDpaFlowAction&quot;</p>
<dd>flow action</dl>
<p> <code>Since:</code> 2.4 <code>query-rocker-of-dpa-flows</code> (Command) Return rocker OF-DPA flow information. <code>Arguments:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>switch name</p>
<dt>&quot;tbl-id: int&quot; (optional)</p>
<dd>flow table <font SIZE="-1">ID.</font> If tbl-id is not specified, returns flow information for all tables.</dl>
<p> <code>Returns:</code> rocker OF-DPA flow information <code>Since:</code> 2.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-rocker-of-dpa-flows&quot;,<br />
   &quot;arguments&quot; : {&quot;name&quot; : &quot;sw1&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {&quot;key&quot; : {&quot;in-pport&quot; : 0, &quot;priority&quot; : 1, &quot;tbl-id&quot; : 0},<br />
         &quot;hits&quot; : 138,<br />
         &quot;cookie&quot; : 0,<br />
         &quot;action&quot; : {&quot;goto-tbl&quot; : 10},<br />
         &quot;mask&quot; : {&quot;in-pport&quot; : 4294901760}},<br />
        {&#8230; more&#8230;},<br />
    ]<br />
} <code>RockerOfDpaGroup</code> (Object) Rocker switch OF-DPA group <code>Members:</code></p>
<dl>
<dt>&quot;id: int&quot;</p>
<dd>group unique <font SIZE="-1">ID</font></p>
<dt>&quot;type: int&quot;</p>
<dd>group type</p>
<dt>&quot;vlan-id: int&quot; (optional)</p>
<dd><font SIZE="-1">VLAN ID</font></p>
<dt>&quot;pport: int&quot; (optional)</p>
<dd>physical port number</p>
<dt>&quot;index: int&quot; (optional)</p>
<dd>group index, unique with group type</p>
<dt>&quot;out-pport: int&quot; (optional)</p>
<dd>output physical port number</p>
<dt>&quot;group-id: int&quot; (optional)</p>
<dd>next group <font SIZE="-1">ID</font></p>
<dt>&quot;set-vlan-id: int&quot; (optional)</p>
<dd><font SIZE="-1">VLAN ID</font> to set</p>
<dt>&quot;pop-vlan: int&quot; (optional)</p>
<dd>pop <font SIZE="-1">VLAN</font> headr from packet</p>
<dt>&quot;group-ids: array of int&quot; (optional)</p>
<dd>list of next group IDs</p>
<dt>&quot;set-eth-src: string&quot; (optional)</p>
<dd>set source <font SIZE="-1">MAC</font> address in Ethernet header</p>
<dt>&quot;set-eth-dst: string&quot; (optional)</p>
<dd>set destination <font SIZE="-1">MAC</font> address in Ethernet header</p>
<dt>&quot;ttl-check: int&quot; (optional)</p>
<dd>perform <font SIZE="-1">TTL</font> check</dl>
<p> <code>Note:</code> optional members may or may not appear in the group depending if they&#8217;re relevant to the group type. <code>Since:</code> 2.4 <code>query-rocker-of-dpa-groups</code> (Command) Return rocker OF-DPA group information. <code>Arguments:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>switch name</p>
<dt>&quot;type: int&quot; (optional)</p>
<dd>group type. If type is not specified, returns group information for all group types.</dl>
<p> <code>Returns:</code> rocker OF-DPA group information <code>Since:</code> 2.4 <code>Example:</code> </p>
<pre> -&gt; { &quot;execute&quot;: &quot;query-rocker-of-dpa-groups&quot;,
 &quot;arguments&quot;: { &quot;name&quot;: &quot;sw1&quot; } }
 &lt;- { &quot;return&quot;: [ {&quot;type&quot;: 0, &quot;out-pport&quot;: 2,
 &quot;pport&quot;: 2, &quot;vlan-id&quot;: 3841,
 &quot;pop-vlan&quot;: 1, &quot;id&quot;: 251723778},
 {&quot;type&quot;: 0, &quot;out-pport&quot;: 0,
 &quot;pport&quot;: 0, &quot;vlan-id&quot;: 3841,
 &quot;pop-vlan&quot;: 1, &quot;id&quot;: 251723776},
 {&quot;type&quot;: 0, &quot;out-pport&quot;: 1,
 &quot;pport&quot;: 1, &quot;vlan-id&quot;: 3840,
 &quot;pop-vlan&quot;: 1, &quot;id&quot;: 251658241},
 {&quot;type&quot;: 0, &quot;out-pport&quot;: 0,
 &quot;pport&quot;: 0, &quot;vlan-id&quot;: 3840,
 &quot;pop-vlan&quot;: 1, &quot;id&quot;: 251658240}
 ]}</pre>
<h3><font SIZE="-1">TPM</font> (trusted platform module) devices</h3>
<p><code>TpmModel</code> (Enum) An enumeration of <font SIZE="-1">TPM</font> models <code>Values:</code></p>
<dl>
<dt>&quot;tpm-tis&quot;</p>
<dd><font SIZE="-1">TPM TIS</font> model</p>
<dt>&quot;tpm-crb&quot;</p>
<dd><font SIZE="-1">TPM CRB</font> model (since 2.12)</dl>
<p> <code>Since:</code> 1.5 <code>query-tpm-models</code> (Command) Return a list of supported <font SIZE="-1">TPM</font> models <code>Returns:</code> a list of TpmModel <code>Since:</code> 1.5 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-tpm-models&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [ &quot;tpm-tis&quot;, &quot;tpm-crb&quot; ]<br />
} <code>TpmType</code> (Enum) An enumeration of <font SIZE="-1">TPM</font> types <code>Values:</code></p>
<dl>
<dt>&quot;passthrough&quot;</p>
<dd><font SIZE="-1">TPM</font> passthrough type</p>
<dt>&quot;emulator&quot;</p>
<dd>Software Emulator <font SIZE="-1">TPM</font> type Since: 2.11</dl>
<p> <code>Since:</code> 1.5 <code>query-tpm-types</code> (Command) Return a list of supported <font SIZE="-1">TPM</font> types <code>Returns:</code> a list of TpmType <code>Since:</code> 1.5 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-tpm-types&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [ &quot;passthrough&quot;, &quot;emulator&quot; ]<br />
} <code>TPMPassthroughOptions</code> (Object) Information about the <font SIZE="-1">TPM</font> passthrough type <code>Members:</code></p>
<dl>
<dt>&quot;path: string&quot; (optional)</p>
<dd>string describing the path used for accessing the <font SIZE="-1">TPM</font> device</p>
<dt>&quot;cancel-path: string&quot; (optional)</p>
<dd>string showing the <font SIZE="-1">TPM</font>&#8216;s sysfs cancel file for cancellation of <font SIZE="-1">TPM</font> commands while they are executing</dl>
<p> <code>Since:</code> 1.5 <code>TPMEmulatorOptions</code> (Object) Information about the <font SIZE="-1">TPM</font> emulator type <code>Members:</code></p>
<dl>
<dt>&quot;chardev: string&quot;</p>
<dd>Name of a unix socket chardev</dl>
<p> <code>Since:</code> 2.11 <code>TpmTypeOptions</code> (Object) A union referencing different <font SIZE="-1">TPM</font> backend types&#8217; configuration options <code>Members:</code></p>
<dl>
<dt>&quot;type&quot;</p>
<dd>&#8216;passthrough&#8217; The configuration options for the <font SIZE="-1">TPM</font> passthrough type &#8217;emulator&#8217; The configuration options for <font SIZE="-1">TPM</font> emulator backend type</p>
<dt>&quot;data: TPMPassthroughOptions&quot; when &quot;type&quot; is &quot;passthrough&quot;</p>
<dd>
<dt>&quot;data: TPMEmulatorOptions&quot; when &quot;type&quot; is &quot;emulator&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.5 <code>TPMInfo</code> (Object) Information about the <font SIZE="-1">TPM</font> <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>The Id of the <font SIZE="-1">TPM</font></p>
<dt>&quot;model: TpmModel&quot;</p>
<dd>The <font SIZE="-1">TPM</font> frontend model</p>
<dt>&quot;options: TpmTypeOptions&quot;</p>
<dd>The <font SIZE="-1">TPM</font> (backend) type configuration options</dl>
<p> <code>Since:</code> 1.5 <code>query-tpm</code> (Command) Return information about the <font SIZE="-1">TPM</font> device <code>Returns:</code> <tt>&quot;TPMInfo&quot;</tt> on success <code>Since:</code> 1.5 <code>Example:</code> </p>
<pre> -&gt; { &quot;execute&quot;: &quot;query-tpm&quot; }
 &lt;- { &quot;return&quot;:
 [
 { &quot;model&quot;: &quot;tpm-tis&quot;,
 &quot;options&quot;:
 { &quot;type&quot;: &quot;passthrough&quot;,
 &quot;data&quot;:
 { &quot;cancel-path&quot;: &quot;/sys/class/misc/tpm0/device/cancel&quot;,
 &quot;path&quot;: &quot;/dev/tpm0&quot;
 }
 },
 &quot;id&quot;: &quot;tpm0&quot;
 }
 ]
 }</pre>
<h3>Remote desktop</h3>
<p><code>set_password</code> (Command) Sets the password of a remote display session. <code>Arguments:</code></p>
<dl>
<dt>&quot;protocol: string&quot;</p>
<dd>`vnc&#8217; to modify the <font SIZE="-1">VNC</font> server password `spice&#8217; to modify the Spice server password</p>
<dt>&quot;password: string&quot;</p>
<dd>the new password</p>
<dt>&quot;connected: string&quot; (optional)</p>
<dd>how to handle existing clients when changing the password. If nothing is specified, defaults to `keep&#8217; `fail&#8217; to fail the command if clients are connected `disconnect&#8217; to disconnect existing clients `keep&#8217; to maintain existing clients</dl>
<p> <code>Returns:</code> Nothing on success If Spice is not enabled, DeviceNotFound <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;set_password&quot;, &quot;arguments&quot; : {&quot;protocol&quot; : &quot;vnc&quot;,<br />
                                              &quot;password&quot; : &quot;secret&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>expire_password</code> (Command) Expire the password of a remote display server. <code>Arguments:</code></p>
<dl>
<dt>&quot;protocol: string&quot;</p>
<dd>the name of the remote display protocol `vnc&#8217; or `spice&#8217;</p>
<dt>&quot;time: string&quot;</p>
<dd>when to expire the password. `now&#8217; to expire the password immediately `never&#8217; to cancel password expiration `+INT&#8217; where <font SIZE="-1">INT</font> is the number of seconds from now (integer) `<font SIZE="-1">INT</font>&#8216; where <font SIZE="-1">INT</font> is the absolute time in seconds</dl>
<p> <code>Returns:</code> Nothing on success If <tt>&quot;protocol&quot;</tt> is `spice&#8217; and Spice is not active, DeviceNotFound <code>Since:</code> 0.14.0 <code>Notes:</code> Time is relative to the server and currently there is no way to coordinate server time with client time. It is not recommended to use the absolute time version of the <tt>&quot;time&quot;</tt> parameter unless you&#8217;re sure you are on the same machine as the <font SIZE="-1">QEMU</font> instance. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;expire_password&quot;, &quot;arguments&quot; : {&quot;protocol&quot; : &quot;vnc&quot;,<br />
                                                 &quot;time&quot; : &quot;+60&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>screendump</code> (Command) Write a <font SIZE="-1">PPM</font> of the <font SIZE="-1">VGA</font> screen to a file. <code>Arguments:</code></p>
<dl>
<dt>&quot;filename: string&quot;</p>
<dd>the path of a new <font SIZE="-1">PPM</font> file to store the image</p>
<dt>&quot;device: string&quot; (optional)</p>
<dd><font SIZE="-1">ID</font> of the display device that should be dumped. If this parameter is missing, the primary display will be used. (Since 2.12)</p>
<dt>&quot;head: int&quot; (optional)</p>
<dd>head to use in case the device supports multiple heads. If this parameter is missing, head #0 will be used. Also note that the head can only be specified in conjunction with the device <font SIZE="-1">ID.</font> (Since 2.12)</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;screendump&quot;,<br />
   &quot;arguments&quot; : {&quot;filename&quot; : &quot;/tmp/image&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <i>Spice</i> <code>SpiceBasicInfo</code> (Object) The basic information for <font SIZE="-1">SPICE</font> network connection <code>Members:</code></p>
<dl>
<dt>&quot;host: string&quot;</p>
<dd><font SIZE="-1">IP</font> address</p>
<dt>&quot;port: string&quot;</p>
<dd>port number</p>
<dt>&quot;family: NetworkAddressFamily&quot;</p>
<dd>address family</dl>
<p> <code>Since:</code> 2.1 <code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <code>SpiceServerInfo</code> (Object) Information about a <font SIZE="-1">SPICE</font> server <code>Members:</code></p>
<dl>
<dt>&quot;auth: string&quot; (optional)</p>
<dd>authentication method</p>
<dt>The members of &quot;SpiceBasicInfo&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.1 <code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <code>SpiceChannel</code> (Object) Information about a <font SIZE="-1">SPICE</font> client channel. <code>Members:</code></p>
<dl>
<dt>&quot;connection-id: int&quot;</p>
<dd><font SIZE="-1">SPICE</font> connection id number. All channels with the same id belong to the same <font SIZE="-1">SPICE</font> session.</p>
<dt>&quot;channel-type: int&quot;</p>
<dd><font SIZE="-1">SPICE</font> channel type number. &#8220;1&#8221; is the main control channel, filter for this one if you want to track spice sessions only</p>
<dt>&quot;channel-id: int&quot;</p>
<dd><font SIZE="-1">SPICE</font> channel <font SIZE="-1">ID</font> number. Usually &#8220;0&#8221;, might be different when multiple channels of the same type exist, such as multiple display channels in a multihead setup</p>
<dt>&quot;tls: boolean&quot;</p>
<dd>true if the channel is encrypted, false otherwise.</p>
<dt>The members of &quot;SpiceBasicInfo&quot;</p>
<dd></dl>
<p> <code>Since:</code> 0.14.0 <code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <code>SpiceQueryMouseMode</code> (Enum) An enumeration of Spice mouse states. <code>Values:</code></p>
<dl>
<dt>&quot;client&quot;</p>
<dd>Mouse cursor position is determined by the client.</p>
<dt>&quot;server&quot;</p>
<dd>Mouse cursor position is determined by the server.</p>
<dt>&quot;unknown&quot;</p>
<dd>No information is available about mouse mode used by the spice server.</dl>
<p> <code>Note:</code> spice/enums.h has a SpiceMouseMode already, hence the name. <code>Since:</code> 1.1 <code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <code>SpiceInfo</code> (Object) Information about the <font SIZE="-1">SPICE</font> session. <code>Members:</code></p>
<dl>
<dt>&quot;enabled: boolean&quot;</p>
<dd>true if the <font SIZE="-1">SPICE</font> server is enabled, false otherwise</p>
<dt>&quot;migrated: boolean&quot;</p>
<dd>true if the last guest migration completed and spice migration had completed as well. false otherwise. (since 1.4)</p>
<dt>&quot;host: string&quot; (optional)</p>
<dd>The hostname the <font SIZE="-1">SPICE</font> server is bound to. This depends on the name resolution on the host and may be an <font SIZE="-1">IP</font> address.</p>
<dt>&quot;port: int&quot; (optional)</p>
<dd>The <font SIZE="-1">SPICE</font> server&#8217;s port number.</p>
<dt>&quot;compiled-version: string&quot; (optional)</p>
<dd><font SIZE="-1">SPICE</font> server version.</p>
<dt>&quot;tls-port: int&quot; (optional)</p>
<dd>The <font SIZE="-1">SPICE</font> server&#8217;s <font SIZE="-1">TLS</font> port number.</p>
<dt>&quot;auth: string&quot; (optional)</p>
<dd>the current authentication type used by the server &#8216;none&#8217; if no authentication is being used &#8216;spice&#8217; uses <font SIZE="-1">SASL</font> or direct <font SIZE="-1">TLS</font> authentication, depending on command line options</p>
<dt>&quot;mouse-mode: SpiceQueryMouseMode&quot;</p>
<dd>The mode in which the mouse cursor is displayed currently. Can be determined by the client or the server, or unknown if spice server doesn&#8217;t provide this information. (since: 1.1)</p>
<dt>&quot;channels: array of SpiceChannel&quot; (optional)</p>
<dd>a list of <tt>&quot;SpiceChannel&quot;</tt> for each active spice channel</dl>
<p> <code>Since:</code> 0.14.0 <code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <code>query-spice</code> (Command) Returns information about the current <font SIZE="-1">SPICE</font> server <code>Returns:</code> <tt>&quot;SpiceInfo&quot;</tt> <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-spice&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;enabled&quot; : true,<br />
                    &quot;auth&quot; : &quot;spice&quot;,<br />
                             &quot;port&quot; : 5920,<br />
                             &quot;tls-port&quot; : 5921,<br />
                             &quot;host&quot; : &quot;0.0.0.0&quot;,<br />
                                      &quot;channels&quot; : [<br />
                                          {<br />
                                              &quot;port&quot; : &quot;54924&quot;,<br />
                                              &quot;family&quot; : &quot;ipv4&quot;,<br />
                                              &quot;channel-type&quot; : 1,<br />
                                              &quot;connection-id&quot; : 1804289383,<br />
                                              &quot;host&quot; : &quot;127.0.0.1&quot;,<br />
                                              &quot;channel-id&quot; : 0,<br />
                                              &quot;tls&quot; : true<br />
                                          },<br />
                                          {<br />
                                              &quot;port&quot; : &quot;36710&quot;,<br />
                                              &quot;family&quot; : &quot;ipv4&quot;,<br />
                                              &quot;channel-type&quot; : 4,<br />
                                              &quot;connection-id&quot; : 1804289383,<br />
                                              &quot;host&quot; : &quot;127.0.0.1&quot;,<br />
                                              &quot;channel-id&quot; : 0,<br />
                                              &quot;tls&quot; : false<br />
                                          },<br />
                                          [&#8230; more channels follow&#8230;]<br />
                                      ]<br />
    }<br />
} <code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <font SIZE="-1"><code>SPICE_CONNECTED</code></font> (Event) Emitted when a <font SIZE="-1">SPICE</font> client establishes a connection <code>Arguments:</code></p>
<dl>
<dt>&quot;server: SpiceBasicInfo&quot;</p>
<dd>server information</p>
<dt>&quot;client: SpiceBasicInfo&quot;</p>
<dd>client information</dl>
<p> <code>Since:</code> 0.14.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;timestamp&quot;: {&quot;seconds&quot;: 1290688046, &quot;microseconds&quot;: 388707},
 &quot;event&quot;: &quot;SPICE_CONNECTED&quot;,
 &quot;data&quot;: {
 &quot;server&quot;: { &quot;port&quot;: &quot;5920&quot;, &quot;family&quot;: &quot;ipv4&quot;, &quot;host&quot;: &quot;127.0.0.1&quot;},
 &quot;client&quot;: {&quot;port&quot;: &quot;52873&quot;, &quot;family&quot;: &quot;ipv4&quot;, &quot;host&quot;: &quot;127.0.0.1&quot;}
 }}</pre>
<p><code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <font SIZE="-1"><code>SPICE_INITIALIZED</code></font> (Event) Emitted after initial handshake and authentication takes place (if any) and the <font SIZE="-1">SPICE</font> channel is up and running <code>Arguments:</code></p>
<dl>
<dt>&quot;server: SpiceServerInfo&quot;</p>
<dd>server information</p>
<dt>&quot;client: SpiceChannel&quot;</p>
<dd>client information</dl>
<p> <code>Since:</code> 0.14.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;timestamp&quot;: {&quot;seconds&quot;: 1290688046, &quot;microseconds&quot;: 417172},
 &quot;event&quot;: &quot;SPICE_INITIALIZED&quot;,
 &quot;data&quot;: {&quot;server&quot;: {&quot;auth&quot;: &quot;spice&quot;, &quot;port&quot;: &quot;5921&quot;,
 &quot;family&quot;: &quot;ipv4&quot;, &quot;host&quot;: &quot;127.0.0.1&quot;},
 &quot;client&quot;: {&quot;port&quot;: &quot;49004&quot;, &quot;family&quot;: &quot;ipv4&quot;, &quot;channel-type&quot;: 3,
 &quot;connection-id&quot;: 1804289383, &quot;host&quot;: &quot;127.0.0.1&quot;,
 &quot;channel-id&quot;: 0, &quot;tls&quot;: true}
 }}</pre>
<p><code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <font SIZE="-1"><code>SPICE_DISCONNECTED</code></font> (Event) Emitted when the <font SIZE="-1">SPICE</font> connection is closed <code>Arguments:</code></p>
<dl>
<dt>&quot;server: SpiceBasicInfo&quot;</p>
<dd>server information</p>
<dt>&quot;client: SpiceBasicInfo&quot;</p>
<dd>client information</dl>
<p> <code>Since:</code> 0.14.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;timestamp&quot;: {&quot;seconds&quot;: 1290688046, &quot;microseconds&quot;: 388707},
 &quot;event&quot;: &quot;SPICE_DISCONNECTED&quot;,
 &quot;data&quot;: {
 &quot;server&quot;: { &quot;port&quot;: &quot;5920&quot;, &quot;family&quot;: &quot;ipv4&quot;, &quot;host&quot;: &quot;127.0.0.1&quot;},
 &quot;client&quot;: {&quot;port&quot;: &quot;52873&quot;, &quot;family&quot;: &quot;ipv4&quot;, &quot;host&quot;: &quot;127.0.0.1&quot;}
 }}</pre>
<p><code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <font SIZE="-1"><code>SPICE_MIGRATE_COMPLETED</code></font> (Event) Emitted when <font SIZE="-1">SPICE</font> migration has completed <code>Since:</code> 1.3 <code>Example:</code> </p>
<pre> &lt;- { &quot;timestamp&quot;: {&quot;seconds&quot;: 1290688046, &quot;microseconds&quot;: 417172},
 &quot;event&quot;: &quot;SPICE_MIGRATE_COMPLETED&quot; }</pre>
<p><code>If:</code> <tt>&quot;defined(CONFIG_SPICE)&quot;</tt> <i></i><font SIZE="-1"><i>VNC</i></font><i></i> <code>VncBasicInfo</code> (Object) The basic information for vnc network connection <code>Members:</code></p>
<dl>
<dt>&quot;host: string&quot;</p>
<dd><font SIZE="-1">IP</font> address</p>
<dt>&quot;service: string&quot;</p>
<dd>The service name of the vnc port. This may depend on the host system&#8217;s service database so symbolic names should not be relied on.</p>
<dt>&quot;family: NetworkAddressFamily&quot;</p>
<dd>address family</p>
<dt>&quot;websocket: boolean&quot;</p>
<dd>true in case the socket is a websocket (since 2.3).</dl>
<p> <code>Since:</code> 2.1 <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <code>VncServerInfo</code> (Object) The network connection information for server <code>Members:</code></p>
<dl>
<dt>&quot;auth: string&quot; (optional)</p>
<dd>authentication method used for the plain (non-websocket) <font SIZE="-1">VNC</font> server</p>
<dt>The members of &quot;VncBasicInfo&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.1 <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <code>VncClientInfo</code> (Object) Information about a connected <font SIZE="-1">VNC</font> client. <code>Members:</code></p>
<dl>
<dt>&quot;x509_dname: string&quot; (optional)</p>
<dd>If x509 authentication is in use, the Distinguished Name of the client.</p>
<dt>&quot;sasl_username: string&quot; (optional)</p>
<dd>If <font SIZE="-1">SASL</font> authentication is in use, the <font SIZE="-1">SASL</font> username used for authentication.</p>
<dt>The members of &quot;VncBasicInfo&quot;</p>
<dd></dl>
<p> <code>Since:</code> 0.14.0 <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <code>VncInfo</code> (Object) Information about the <font SIZE="-1">VNC</font> session. <code>Members:</code></p>
<dl>
<dt>&quot;enabled: boolean&quot;</p>
<dd>true if the <font SIZE="-1">VNC</font> server is enabled, false otherwise</p>
<dt>&quot;host: string&quot; (optional)</p>
<dd>The hostname the <font SIZE="-1">VNC</font> server is bound to. This depends on the name resolution on the host and may be an <font SIZE="-1">IP</font> address.</p>
<dt>&quot;family: NetworkAddressFamily&quot; (optional)</p>
<dd>&#8216;ipv6&#8217; if the host is listening for IPv6 connections &#8216;ipv4&#8217; if the host is listening for IPv4 connections &#8216;unix&#8217; if the host is listening on a unix domain socket &#8216;unknown&#8217; otherwise</p>
<dt>&quot;service: string&quot; (optional)</p>
<dd>The service name of the server&#8217;s port. This may depends on the host system&#8217;s service database so symbolic names should not be relied on.</p>
<dt>&quot;auth: string&quot; (optional)</p>
<dd>the current authentication type used by the server &#8216;none&#8217; if no authentication is being used &#8216;vnc&#8217; if <font SIZE="-1">VNC</font> authentication is being used &#8216;vencrypt+plain&#8217; if VEncrypt is used with plain text authentication &#8216;vencrypt+tls+none&#8217; if VEncrypt is used with <font SIZE="-1">TLS</font> and no authentication &#8216;vencrypt+tls+vnc&#8217; if VEncrypt is used with <font SIZE="-1">TLS</font> and <font SIZE="-1">VNC</font> authentication &#8216;vencrypt+tls+plain&#8217; if VEncrypt is used with <font SIZE="-1">TLS</font> and plain text auth &#8216;vencrypt+x509+none&#8217; if VEncrypt is used with x509 and no auth &#8216;vencrypt+x509+vnc&#8217; if VEncrypt is used with x509 and <font SIZE="-1">VNC</font> auth &#8216;vencrypt+x509+plain&#8217; if VEncrypt is used with x509 and plain text auth &#8216;vencrypt+tls+sasl&#8217; if VEncrypt is used with <font SIZE="-1">TLS</font> and <font SIZE="-1">SASL</font> auth &#8216;vencrypt+x509+sasl&#8217; if VEncrypt is used with x509 and <font SIZE="-1">SASL</font> auth</p>
<dt>&quot;clients: array of VncClientInfo&quot; (optional)</p>
<dd>a list of <tt>&quot;VncClientInfo&quot;</tt> of all currently connected clients</dl>
<p> <code>Since:</code> 0.14.0 <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <code>VncPrimaryAuth</code> (Enum) vnc primary authentication method. <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>Not documented</p>
<dt>&quot;vnc&quot;</p>
<dd>Not documented</p>
<dt>&quot;ra2&quot;</p>
<dd>Not documented</p>
<dt>&quot;ra2ne&quot;</p>
<dd>Not documented</p>
<dt>&quot;tight&quot;</p>
<dd>Not documented</p>
<dt>&quot;ultra&quot;</p>
<dd>Not documented</p>
<dt>&quot;tls&quot;</p>
<dd>Not documented</p>
<dt>&quot;vencrypt&quot;</p>
<dd>Not documented</p>
<dt>&quot;sasl&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.3 <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <code>VncVencryptSubAuth</code> (Enum) vnc sub authentication method with vencrypt. <code>Values:</code></p>
<dl>
<dt>&quot;plain&quot;</p>
<dd>Not documented</p>
<dt>&quot;tls-none&quot;</p>
<dd>Not documented</p>
<dt>&quot;x509-none&quot;</p>
<dd>Not documented</p>
<dt>&quot;tls-vnc&quot;</p>
<dd>Not documented</p>
<dt>&quot;x509-vnc&quot;</p>
<dd>Not documented</p>
<dt>&quot;tls-plain&quot;</p>
<dd>Not documented</p>
<dt>&quot;x509-plain&quot;</p>
<dd>Not documented</p>
<dt>&quot;tls-sasl&quot;</p>
<dd>Not documented</p>
<dt>&quot;x509-sasl&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.3 <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <code>VncServerInfo2</code> (Object) The network connection information for server <code>Members:</code></p>
<dl>
<dt>&quot;auth: VncPrimaryAuth&quot;</p>
<dd>The current authentication type used by the servers</p>
<dt>&quot;vencrypt: VncVencryptSubAuth&quot; (optional)</p>
<dd>The vencrypt sub authentication type used by the servers, only specified in case auth == vencrypt.</p>
<dt>The members of &quot;VncBasicInfo&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.9 <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <code>VncInfo2</code> (Object) Information about a vnc server <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>vnc server name.</p>
<dt>&quot;server: array of VncServerInfo2&quot;</p>
<dd>A list of <tt>&quot;VncBasincInfo&quot;</tt> describing all listening sockets. The list can be empty (in case the vnc server is disabled). It also may have multiple entries: normal + websocket, possibly also ipv4 + ipv6 in the future.</p>
<dt>&quot;clients: array of VncClientInfo&quot;</p>
<dd>A list of <tt>&quot;VncClientInfo&quot;</tt> of all currently connected clients. The list can be empty, for obvious reasons.</p>
<dt>&quot;auth: VncPrimaryAuth&quot;</p>
<dd>The current authentication type used by the non-websockets servers</p>
<dt>&quot;vencrypt: VncVencryptSubAuth&quot; (optional)</p>
<dd>The vencrypt authentication type used by the servers, only specified in case auth == vencrypt.</p>
<dt>&quot;display: string&quot; (optional)</p>
<dd>The display device the vnc server is linked to.</dl>
<p> <code>Since:</code> 2.3 <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <code>query-vnc</code> (Command) Returns information about the current <font SIZE="-1">VNC</font> server <code>Returns:</code> <tt>&quot;VncInfo&quot;</tt> <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-vnc&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;enabled&quot; : true,<br />
                    &quot;host&quot; : &quot;0.0.0.0&quot;,<br />
                             &quot;service&quot; : &quot;50402&quot;,<br />
                                         &quot;auth&quot; : &quot;vnc&quot;,<br />
                                                  &quot;family&quot; : &quot;ipv4&quot;,<br />
                                                             &quot;clients&quot; : [<br />
                                                                 {<br />
                                                                     &quot;host&quot; : &quot;127.0.0.1&quot;,<br />
                                                                     &quot;service&quot; : &quot;50401&quot;,<br />
                                                                     &quot;family&quot; : &quot;ipv4&quot;<br />
                                                                 }<br />
                                                             ]<br />
    }<br />
} <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <code>query-vnc-servers</code> (Command) Returns a list of vnc servers. The list can be empty. <code>Returns:</code> a list of <tt>&quot;VncInfo2&quot;</tt> <code>Since:</code> 2.3 <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <code>change-vnc-password</code> (Command) Change the <font SIZE="-1">VNC</font> server password. <code>Arguments:</code></p>
<dl>
<dt>&quot;password: string&quot;</p>
<dd>the new password to use with <font SIZE="-1">VNC</font> authentication</dl>
<p> <code>Since:</code> 1.1 <code>Notes:</code> An empty password in this command will set the password to the empty string. Existing clients are unaffected by executing this command. <code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <font SIZE="-1"><code>VNC_CONNECTED</code></font> (Event) Emitted when a <font SIZE="-1">VNC</font> client establishes a connection <code>Arguments:</code></p>
<dl>
<dt>&quot;server: VncServerInfo&quot;</p>
<dd>server information</p>
<dt>&quot;client: VncBasicInfo&quot;</p>
<dd>client information</dl>
<p> <code>Note:</code> This event is emitted before any authentication takes place, thus the authentication <font SIZE="-1">ID</font> is not provided <code>Since:</code> 0.13.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;VNC_CONNECTED&quot;,
 &quot;data&quot;: {
 &quot;server&quot;: { &quot;auth&quot;: &quot;sasl&quot;, &quot;family&quot;: &quot;ipv4&quot;,
 &quot;service&quot;: &quot;5901&quot;, &quot;host&quot;: &quot;0.0.0.0&quot; },
 &quot;client&quot;: { &quot;family&quot;: &quot;ipv4&quot;, &quot;service&quot;: &quot;58425&quot;,
 &quot;host&quot;: &quot;127.0.0.1&quot; } },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1262976601, &quot;microseconds&quot;: 975795 } }</pre>
<p><code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <font SIZE="-1"><code>VNC_INITIALIZED</code></font> (Event) Emitted after authentication takes place (if any) and the <font SIZE="-1">VNC</font> session is made active <code>Arguments:</code></p>
<dl>
<dt>&quot;server: VncServerInfo&quot;</p>
<dd>server information</p>
<dt>&quot;client: VncClientInfo&quot;</p>
<dd>client information</dl>
<p> <code>Since:</code> 0.13.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;VNC_INITIALIZED&quot;,
 &quot;data&quot;: {
 &quot;server&quot;: { &quot;auth&quot;: &quot;sasl&quot;, &quot;family&quot;: &quot;ipv4&quot;,
 &quot;service&quot;: &quot;5901&quot;, &quot;host&quot;: &quot;0.0.0.0&quot;},
 &quot;client&quot;: { &quot;family&quot;: &quot;ipv4&quot;, &quot;service&quot;: &quot;46089&quot;,
 &quot;host&quot;: &quot;127.0.0.1&quot;, &quot;sasl_username&quot;: &quot;luiz&quot; } },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1263475302, &quot;microseconds&quot;: 150772 } }</pre>
<p><code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt> <font SIZE="-1"><code>VNC_DISCONNECTED</code></font> (Event) Emitted when the connection is closed <code>Arguments:</code></p>
<dl>
<dt>&quot;server: VncServerInfo&quot;</p>
<dd>server information</p>
<dt>&quot;client: VncClientInfo&quot;</p>
<dd>client information</dl>
<p> <code>Since:</code> 0.13.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;VNC_DISCONNECTED&quot;,
 &quot;data&quot;: {
 &quot;server&quot;: { &quot;auth&quot;: &quot;sasl&quot;, &quot;family&quot;: &quot;ipv4&quot;,
 &quot;service&quot;: &quot;5901&quot;, &quot;host&quot;: &quot;0.0.0.0&quot; },
 &quot;client&quot;: { &quot;family&quot;: &quot;ipv4&quot;, &quot;service&quot;: &quot;58425&quot;,
 &quot;host&quot;: &quot;127.0.0.1&quot;, &quot;sasl_username&quot;: &quot;luiz&quot; } },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1262976601, &quot;microseconds&quot;: 975795 } }</pre>
<p><code>If:</code> <tt>&quot;defined(CONFIG_VNC)&quot;</tt></p>
<h3>Input</h3>
<p><code>MouseInfo</code> (Object) Information about a mouse device. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>the name of the mouse device</p>
<dt>&quot;index: int&quot;</p>
<dd>the index of the mouse device</p>
<dt>&quot;current: boolean&quot;</p>
<dd>true if this device is currently receiving mouse events</p>
<dt>&quot;absolute: boolean&quot;</p>
<dd>true if this device supports absolute coordinates as input</dl>
<p> <code>Since:</code> 0.14.0 <code>query-mice</code> (Command) Returns information about each active mouse device <code>Returns:</code> a list of <tt>&quot;MouseInfo&quot;</tt> for each device <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-mice&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;name&quot; : &quot;QEMU Microsoft Mouse&quot;,<br />
            &quot;index&quot; : 0,<br />
            &quot;current&quot; : false,<br />
            &quot;absolute&quot; : false<br />
        },<br />
        {<br />
            &quot;name&quot; : &quot;QEMU PS/2 Mouse&quot;,<br />
            &quot;index&quot; : 1,<br />
            &quot;current&quot; : true,<br />
            &quot;absolute&quot; : true<br />
        }<br />
    ]<br />
} <code>QKeyCode</code> (Enum) An enumeration of key name. This is used by the <tt>&quot;send-key&quot;</tt> command. <code>Values:</code></p>
<dl>
<dt>&quot;unmapped&quot;</p>
<dd>since 2.0</p>
<dt>&quot;pause&quot;</p>
<dd>since 2.0</p>
<dt>&quot;ro&quot;</p>
<dd>since 2.4</p>
<dt>&quot;kp_comma&quot;</p>
<dd>since 2.4</p>
<dt>&quot;kp_equals&quot;</p>
<dd>since 2.6</p>
<dt>&quot;power&quot;</p>
<dd>since 2.6</p>
<dt>&quot;hiragana&quot;</p>
<dd>since 2.9</p>
<dt>&quot;henkan&quot;</p>
<dd>since 2.9</p>
<dt>&quot;yen&quot;</p>
<dd>since 2.9</p>
<dt>&quot;sleep&quot;</p>
<dd>since 2.10</p>
<dt>&quot;wake&quot;</p>
<dd>since 2.10</p>
<dt>&quot;audionext&quot;</p>
<dd>since 2.10</p>
<dt>&quot;audioprev&quot;</p>
<dd>since 2.10</p>
<dt>&quot;audiostop&quot;</p>
<dd>since 2.10</p>
<dt>&quot;audioplay&quot;</p>
<dd>since 2.10</p>
<dt>&quot;audiomute&quot;</p>
<dd>since 2.10</p>
<dt>&quot;volumeup&quot;</p>
<dd>since 2.10</p>
<dt>&quot;volumedown&quot;</p>
<dd>since 2.10</p>
<dt>&quot;mediaselect&quot;</p>
<dd>since 2.10</p>
<dt>&quot;mail&quot;</p>
<dd>since 2.10</p>
<dt>&quot;calculator&quot;</p>
<dd>since 2.10</p>
<dt>&quot;computer&quot;</p>
<dd>since 2.10</p>
<dt>&quot;ac_home&quot;</p>
<dd>since 2.10</p>
<dt>&quot;ac_back&quot;</p>
<dd>since 2.10</p>
<dt>&quot;ac_forward&quot;</p>
<dd>since 2.10</p>
<dt>&quot;ac_refresh&quot;</p>
<dd>since 2.10</p>
<dt>&quot;ac_bookmarks&quot;</p>
<dd>since 2.10 altgr, altgr_r: dropped in 2.10</p>
<dt>&quot;muhenkan&quot;</p>
<dd>since 2.12</p>
<dt>&quot;katakanahiragana&quot;</p>
<dd>since 2.12</p>
<dt>&quot;shift&quot;</p>
<dd>Not documented</p>
<dt>&quot;shift_r&quot;</p>
<dd>Not documented</p>
<dt>&quot;alt&quot;</p>
<dd>Not documented</p>
<dt>&quot;alt_r&quot;</p>
<dd>Not documented</p>
<dt>&quot;ctrl&quot;</p>
<dd>Not documented</p>
<dt>&quot;ctrl_r&quot;</p>
<dd>Not documented</p>
<dt>&quot;menu&quot;</p>
<dd>Not documented</p>
<dt>&quot;esc&quot;</p>
<dd>Not documented</p>
<dt>1</p>
<dd>Not documented</p>
<dt>2</p>
<dd>Not documented</p>
<dt>3</p>
<dd>Not documented</p>
<dt>4</p>
<dd>Not documented</p>
<dt>5</p>
<dd>Not documented</p>
<dt>6</p>
<dd>Not documented</p>
<dt>7</p>
<dd>Not documented</p>
<dt>8</p>
<dd>Not documented</p>
<dt>9</p>
<dd>Not documented</p>
<dt>0</p>
<dd>Not documented</p>
<dt>&quot;minus&quot;</p>
<dd>Not documented</p>
<dt>&quot;equal&quot;</p>
<dd>Not documented</p>
<dt>&quot;backspace&quot;</p>
<dd>Not documented</p>
<dt>&quot;tab&quot;</p>
<dd>Not documented</p>
<dt>&quot;q&quot;</p>
<dd>Not documented</p>
<dt>&quot;w&quot;</p>
<dd>Not documented</p>
<dt>&quot;e&quot;</p>
<dd>Not documented</p>
<dt>&quot;r&quot;</p>
<dd>Not documented</p>
<dt>&quot;t&quot;</p>
<dd>Not documented</p>
<dt>&quot;y&quot;</p>
<dd>Not documented</p>
<dt>&quot;u&quot;</p>
<dd>Not documented</p>
<dt>&quot;i&quot;</p>
<dd>Not documented</p>
<dt>&quot;o&quot;</p>
<dd>Not documented</p>
<dt>&quot;p&quot;</p>
<dd>Not documented</p>
<dt>&quot;bracket_left&quot;</p>
<dd>Not documented</p>
<dt>&quot;bracket_right&quot;</p>
<dd>Not documented</p>
<dt>&quot;ret&quot;</p>
<dd>Not documented</p>
<dt>&quot;a&quot;</p>
<dd>Not documented</p>
<dt>&quot;s&quot;</p>
<dd>Not documented</p>
<dt>&quot;d&quot;</p>
<dd>Not documented</p>
<dt>&quot;f&quot;</p>
<dd>Not documented</p>
<dt>&quot;g&quot;</p>
<dd>Not documented</p>
<dt>&quot;h&quot;</p>
<dd>Not documented</p>
<dt>&quot;j&quot;</p>
<dd>Not documented</p>
<dt>&quot;k&quot;</p>
<dd>Not documented</p>
<dt>&quot;l&quot;</p>
<dd>Not documented</p>
<dt>&quot;semicolon&quot;</p>
<dd>Not documented</p>
<dt>&quot;apostrophe&quot;</p>
<dd>Not documented</p>
<dt>&quot;grave_accent&quot;</p>
<dd>Not documented</p>
<dt>&quot;backslash&quot;</p>
<dd>Not documented</p>
<dt>&quot;z&quot;</p>
<dd>Not documented</p>
<dt>&quot;x&quot;</p>
<dd>Not documented</p>
<dt>&quot;c&quot;</p>
<dd>Not documented</p>
<dt>&quot;v&quot;</p>
<dd>Not documented</p>
<dt>&quot;b&quot;</p>
<dd>Not documented</p>
<dt>&quot;n&quot;</p>
<dd>Not documented</p>
<dt>&quot;m&quot;</p>
<dd>Not documented</p>
<dt>&quot;comma&quot;</p>
<dd>Not documented</p>
<dt>&quot;dot&quot;</p>
<dd>Not documented</p>
<dt>&quot;slash&quot;</p>
<dd>Not documented</p>
<dt>&quot;asterisk&quot;</p>
<dd>Not documented</p>
<dt>&quot;spc&quot;</p>
<dd>Not documented</p>
<dt>&quot;caps_lock&quot;</p>
<dd>Not documented</p>
<dt>&quot;f1&quot;</p>
<dd>Not documented</p>
<dt>&quot;f2&quot;</p>
<dd>Not documented</p>
<dt>&quot;f3&quot;</p>
<dd>Not documented</p>
<dt>&quot;f4&quot;</p>
<dd>Not documented</p>
<dt>&quot;f5&quot;</p>
<dd>Not documented</p>
<dt>&quot;f6&quot;</p>
<dd>Not documented</p>
<dt>&quot;f7&quot;</p>
<dd>Not documented</p>
<dt>&quot;f8&quot;</p>
<dd>Not documented</p>
<dt>&quot;f9&quot;</p>
<dd>Not documented</p>
<dt>&quot;f10&quot;</p>
<dd>Not documented</p>
<dt>&quot;num_lock&quot;</p>
<dd>Not documented</p>
<dt>&quot;scroll_lock&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_divide&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_multiply&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_subtract&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_add&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_enter&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_decimal&quot;</p>
<dd>Not documented</p>
<dt>&quot;sysrq&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_0&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_1&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_2&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_3&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_4&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_5&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_6&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_7&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_8&quot;</p>
<dd>Not documented</p>
<dt>&quot;kp_9&quot;</p>
<dd>Not documented</p>
<dt>&quot;less&quot;</p>
<dd>Not documented</p>
<dt>&quot;f11&quot;</p>
<dd>Not documented</p>
<dt>&quot;f12&quot;</p>
<dd>Not documented</p>
<dt>&quot;print&quot;</p>
<dd>Not documented</p>
<dt>&quot;home&quot;</p>
<dd>Not documented</p>
<dt>&quot;pgup&quot;</p>
<dd>Not documented</p>
<dt>&quot;pgdn&quot;</p>
<dd>Not documented</p>
<dt>&quot;end&quot;</p>
<dd>Not documented</p>
<dt>&quot;left&quot;</p>
<dd>Not documented</p>
<dt>&quot;up&quot;</p>
<dd>Not documented</p>
<dt>&quot;down&quot;</p>
<dd>Not documented</p>
<dt>&quot;right&quot;</p>
<dd>Not documented</p>
<dt>&quot;insert&quot;</p>
<dd>Not documented</p>
<dt>&quot;delete&quot;</p>
<dd>Not documented</p>
<dt>&quot;stop&quot;</p>
<dd>Not documented</p>
<dt>&quot;again&quot;</p>
<dd>Not documented</p>
<dt>&quot;props&quot;</p>
<dd>Not documented</p>
<dt>&quot;undo&quot;</p>
<dd>Not documented</p>
<dt>&quot;front&quot;</p>
<dd>Not documented</p>
<dt>&quot;copy&quot;</p>
<dd>Not documented</p>
<dt>&quot;open&quot;</p>
<dd>Not documented</p>
<dt>&quot;paste&quot;</p>
<dd>Not documented</p>
<dt>&quot;find&quot;</p>
<dd>Not documented</p>
<dt>&quot;cut&quot;</p>
<dd>Not documented</p>
<dt>&quot;lf&quot;</p>
<dd>Not documented</p>
<dt>&quot;help&quot;</p>
<dd>Not documented</p>
<dt>&quot;meta_l&quot;</p>
<dd>Not documented</p>
<dt>&quot;meta_r&quot;</p>
<dd>Not documented</p>
<dt>&quot;compose&quot;</p>
<dd>Not documented</dl>
<p> &#8216;sysrq&#8217; was mistakenly added to hack around the fact that the ps2 driver was not generating correct scancodes sequences when &#8216;alt+print&#8217; was pressed. This flaw is now fixed and the &#8216;sysrq&#8217; key serves no further purpose. Any further use of &#8216;sysrq&#8217; will be transparently changed to &#8216;print&#8217;, so they are effectively synonyms. <code>Since:</code> 1.3.0 <code>KeyValue</code> (Object) Represents a keyboard key. <code>Members:</code></p>
<dl>
<dt>&quot;type&quot;</p>
<dd>One of &#8220;number&#8221;, &#8220;qcode&#8221;</p>
<dt>&quot;data: int&quot; when &quot;type&quot; is &quot;number&quot;</p>
<dd>
<dt>&quot;data: QKeyCode&quot; when &quot;type&quot; is &quot;qcode&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.3.0 <code>send-key</code> (Command) Send keys to guest. <code>Arguments:</code></p>
<dl>
<dt>&quot;keys: array of KeyValue&quot;</p>
<dd>An array of <tt>&quot;KeyValue&quot;</tt> elements. All <tt>&quot;KeyValues&quot;</tt> in this array are simultaneously sent to the guest. A <tt>&quot;KeyValue&quot;</tt>.number value is sent directly to the guest, while <tt>&quot;KeyValue&quot;</tt>.qcode must be a valid <tt>&quot;QKeyCode&quot;</tt> value</p>
<dt>&quot;hold-time: int&quot; (optional)</p>
<dd>time to delay key up events, milliseconds. Defaults to 100</dl>
<p> <code>Returns:</code> Nothing on success If key is unknown or redundant, InvalidParameter <code>Since:</code> 1.3.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;send-key&quot;,<br />
   &quot;arguments&quot; : {&quot;keys&quot; : [ {&quot;type&quot; : &quot;qcode&quot;, &quot;data&quot; : &quot;ctrl&quot;},<br />
                             {&quot;type&quot; : &quot;qcode&quot;, &quot;data&quot; : &quot;alt&quot;},<br />
                             {&quot;type&quot; : &quot;qcode&quot;, &quot;data&quot; : &quot;delete&quot;} ]}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>InputButton</code> (Enum) Button of a pointer input device (mouse, tablet). <code>Values:</code></p>
<dl>
<dt>&quot;side&quot;</p>
<dd>front side button of a 5-button mouse (since 2.9)</p>
<dt>&quot;extra&quot;</p>
<dd>rear side button of a 5-button mouse (since 2.9)</p>
<dt>&quot;left&quot;</p>
<dd>Not documented</p>
<dt>&quot;middle&quot;</p>
<dd>Not documented</p>
<dt>&quot;right&quot;</p>
<dd>Not documented</p>
<dt>&quot;wheel-up&quot;</p>
<dd>Not documented</p>
<dt>&quot;wheel-down&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.0 <code>InputAxis</code> (Enum) Position axis of a pointer input device (mouse, tablet). <code>Values:</code></p>
<dl>
<dt>&quot;x&quot;</p>
<dd>Not documented</p>
<dt>&quot;y&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.0 <code>InputKeyEvent</code> (Object) Keyboard input event. <code>Members:</code></p>
<dl>
<dt>&quot;key: KeyValue&quot;</p>
<dd>Which key this event is for.</p>
<dt>&quot;down: boolean&quot;</p>
<dd>True for key-down and false for key-up events.</dl>
<p> <code>Since:</code> 2.0 <code>InputBtnEvent</code> (Object) Pointer button input event. <code>Members:</code></p>
<dl>
<dt>&quot;button: InputButton&quot;</p>
<dd>Which button this event is for.</p>
<dt>&quot;down: boolean&quot;</p>
<dd>True for key-down and false for key-up events.</dl>
<p> <code>Since:</code> 2.0 <code>InputMoveEvent</code> (Object) Pointer motion input event. <code>Members:</code></p>
<dl>
<dt>&quot;axis: InputAxis&quot;</p>
<dd>Which axis is referenced by <tt>&quot;value&quot;</tt>.</p>
<dt>&quot;value: int&quot;</p>
<dd>Pointer position. For absolute coordinates the valid range is 0 -&gt; 0x7ffff</dl>
<p> <code>Since:</code> 2.0 <code>InputEvent</code> (Object) Input event union. <code>Members:</code></p>
<dl>
<dt>&quot;type&quot;</p>
<dd>the input type, one of:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>&#8216;key&#8217;: Input event of Keyboard</p>
<dt>&#8211;</p>
<dd>&#8216;btn&#8217;: Input event of pointer buttons</p>
<dt>&#8211;</p>
<dd>&#8216;rel&#8217;: Input event of relative pointer motion</p>
<dt>&#8211;</p>
<dd>&#8216;abs&#8217;: Input event of absolute pointer motion</dl>
</dl>
<dl>
<dd></dl>
<dt>&quot;data: InputKeyEvent&quot; when &quot;type&quot; is &quot;key&quot;</p>
<dd>
<dt>&quot;data: InputBtnEvent&quot; when &quot;type&quot; is &quot;btn&quot;</p>
<dd>
<dt>&quot;data: InputMoveEvent&quot; when &quot;type&quot; is &quot;rel&quot;</p>
<dd>
<dt>&quot;data: InputMoveEvent&quot; when &quot;type&quot; is &quot;abs&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.0 <code>input-send-event</code> (Command) Send input event(s) to guest. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>display device to send event(s) to.</p>
<dt>&quot;head: int&quot; (optional)</p>
<dd>head to send event(s) to, in case the display device supports multiple scanouts.</p>
<dt>&quot;events: array of InputEvent&quot;</p>
<dd>List of InputEvent union.</dl>
<p> <code>Returns:</code> Nothing on success. The <tt>&quot;device&quot;</tt> and <tt>&quot;head&quot;</tt> parameters can be used to send the input event to specific input devices in case (a) multiple input devices of the same kind are added to the virtual machine and (b) you have configured input routing (see docs/multiseat.txt) for those input devices. The parameters work exactly like the device and head properties of input devices. If <tt>&quot;device&quot;</tt> is missing, only devices that have no input routing config are admissible. If <tt>&quot;device&quot;</tt> is specified, both input devices with and without input routing config are admissible, but devices with input routing config take precedence. <code>Since:</code> 2.6 <code>Note:</code> The consoles are visible in the qom tree, under /backend/console[$index]. They have a device link and head property, so it is possible to map which console belongs to which device and display. <code>Example:</code> 1. Press left mouse button.</p>
<p>        -&gt;{&quot;execute&quot; : &quot;input-send-event&quot;,<br />
           &quot;arguments&quot; : {&quot;device&quot; : &quot;video0&quot;,<br />
                          &quot;events&quot; : [ {&quot;type&quot; : &quot;btn&quot;,<br />
                                        &quot;data&quot; : {&quot;down&quot; : true, &quot;button&quot; : &quot;left&quot;}} ]}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
    }</p>
<p>        -&gt; {&quot;execute&quot; : &quot;input-send-event&quot;,<br />
            &quot;arguments&quot; : {&quot;device&quot; : &quot;video0&quot;,<br />
                           &quot;events&quot; : [ {&quot;type&quot; : &quot;btn&quot;,<br />
                                         &quot;data&quot; : {&quot;down&quot; : false, &quot;button&quot; : &quot;left&quot;}} ]}} &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
    }</p>
<p>2. Press ctrl &#8211; alt &#8211; del.</p>
<p>                          -&gt;{&quot;execute&quot; : &quot;input-send-event&quot;,<br />
                             &quot;arguments&quot; : {&quot;events&quot; : [<br />
                                 {&quot;type&quot; : &quot;key&quot;, &quot;data&quot; : {&quot;down&quot; : true,<br />
                                                            &quot;key&quot; : {&quot;type&quot; : &quot;qcode&quot;, &quot;data&quot; : &quot;ctrl&quot;}}},<br />
                                 {&quot;type&quot; : &quot;key&quot;, &quot;data&quot; : {&quot;down&quot; : true,<br />
                                                            &quot;key&quot; : {&quot;type&quot; : &quot;qcode&quot;, &quot;data&quot; : &quot;alt&quot;}}},<br />
                                 {&quot;type&quot; : &quot;key&quot;, &quot;data&quot; : {&quot;down&quot; : true,<br />
                                                            &quot;key&quot; : {&quot;type&quot; : &quot;qcode&quot;, &quot;data&quot; : &quot;delete&quot;}}}<br />
                             ]}} &lt;<br />
    &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
}</p>
<p>3. Move mouse pointer to absolute coordinates(20000, 400).</p>
<p>        -&gt;{&quot;execute&quot; : &quot;input-send-event&quot;,<br />
           &quot;arguments&quot; : {&quot;events&quot; : [<br />
               {&quot;type&quot; : &quot;abs&quot;, &quot;data&quot; : {&quot;axis&quot; : &quot;x&quot;, &quot;value&quot; : 20000}},<br />
               {&quot;type&quot; : &quot;abs&quot;, &quot;data&quot; : {&quot;axis&quot; : &quot;y&quot;, &quot;value&quot; : 400}}<br />
           ]}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>GrabToggleKeys</code> (Enum) Keys to toggle input-linux between host and guest. <code>Values:</code></p>
<dl>
<dt>&quot;ctrl-ctrl&quot;</p>
<dd>Not documented</p>
<dt>&quot;alt-alt&quot;</p>
<dd>Not documented</p>
<dt>&quot;shift-shift&quot;</p>
<dd>Not documented</p>
<dt>&quot;meta-meta&quot;</p>
<dd>Not documented</p>
<dt>&quot;scrolllock&quot;</p>
<dd>Not documented</p>
<dt>&quot;ctrl-scrolllock&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 4.0 <code>DisplayGTK</code> (Object) <font SIZE="-1">GTK</font> display options. <code>Members:</code></p>
<dl>
<dt>&quot;grab-on-hover: boolean&quot; (optional)</p>
<dd>Grab keyboard input on mouse hover.</p>
<dt>&quot;zoom-to-fit: boolean&quot; (optional)</p>
<dd>Zoom guest display to fit into the host window. When turned off the host window will be resized instead. In case the display device can notify the guest on window resizes (virtio-gpu) this will default to &#8220;on&#8221;, assuming the guest will resize the display to match the window size then. Otherwise it defaults to &#8220;off&#8221;. Since 3.1</dl>
<p> <code>Since:</code> 2.12 <code>DisplayEGLHeadless</code> (Object) <font SIZE="-1">EGL</font> headless display options. <code>Members:</code></p>
<dl>
<dt>&quot;rendernode: string&quot; (optional)</p>
<dd>Which <font SIZE="-1">DRM</font> render node should be used. Default is the first available node on the host.</dl>
<p> <code>Since:</code> 3.1 <code>DisplayGLMode</code> (Enum) Display OpenGL mode. <code>Values:</code></p>
<dl>
<dt>&quot;off&quot;</p>
<dd>Disable OpenGL (default).</p>
<dt>&quot;on&quot;</p>
<dd>Use OpenGL, pick context type automatically. Would better be named &#8216;auto&#8217; but is called &#8216;on&#8217; for backward compatibility with bool type.</p>
<dt>&quot;core&quot;</p>
<dd>Use OpenGL with Core (desktop) Context.</p>
<dt>&quot;es&quot;</p>
<dd>Use OpenGL with <font SIZE="-1">ES</font> (embedded systems) Context.</dl>
<p> <code>Since:</code> 3.0 <code>DisplayCurses</code> (Object) Curses display options. <code>Members:</code></p>
<dl>
<dt>&quot;charset: string&quot; (optional)</p>
<dd>Font charset used by guest (default: <font SIZE="-1">CP437</font>).</dl>
<p> <code>Since:</code> 4.0 <code>DisplayType</code> (Enum) Display (user interface) type. <code>Values:</code></p>
<dl>
<dt>&quot;default&quot;</p>
<dd>The default user interface, selecting from the first available of gtk, sdl, cocoa, and vnc.</p>
<dt>&quot;none&quot;</p>
<dd>No user interface or video output display. The guest will still see an emulated graphics card, but its output will not be displayed to the <font SIZE="-1">QEMU</font> user.</p>
<dt>&quot;gtk&quot;</p>
<dd>The <font SIZE="-1">GTK</font> user interface.</p>
<dt>&quot;sdl&quot;</p>
<dd>The <font SIZE="-1">SDL</font> user interface.</p>
<dt>&quot;egl-headless&quot;</p>
<dd>No user interface, offload <font SIZE="-1">GL</font> operations to a local <font SIZE="-1">DRI</font> device. Graphical display need to be paired with <font SIZE="-1">VNC</font> or Spice. (Since 3.1)</p>
<dt>&quot;curses&quot;</p>
<dd>Display video output via curses. For graphics device models which support a text mode, <font SIZE="-1">QEMU</font> can display this output using a curses/ncurses interface. Nothing is displayed when the graphics device is in graphical mode or if the graphics device does not support a text mode. Generally only the <font SIZE="-1">VGA</font> device models support text mode.</p>
<dt>&quot;cocoa&quot;</p>
<dd>The Cocoa user interface.</p>
<dt>&quot;spice-app&quot;</p>
<dd>Set up a Spice server and run the default associated application to connect to it. The server will redirect the serial console and <font SIZE="-1">QEMU</font> monitors. (Since 4.0)</dl>
<p> <code>Since:</code> 2.12 <code>DisplayOptions</code> (Object) Display (user interface) options. <code>Members:</code></p>
<dl>
<dt>&quot;type: DisplayType&quot;</p>
<dd>Which DisplayType qemu should use.</p>
<dt>&quot;full-screen: boolean&quot; (optional)</p>
<dd>Start user interface in fullscreen mode (default: off).</p>
<dt>&quot;window-close: boolean&quot; (optional)</p>
<dd>Allow to quit qemu with window close button (default: on).</p>
<dt>&quot;gl: DisplayGLMode&quot; (optional)</p>
<dd>Enable OpenGL support (default: off).</p>
<dt>The members of &quot;DisplayGTK&quot; when &quot;type&quot; is &quot;gtk&quot;</p>
<dd>
<dt>The members of &quot;DisplayCurses&quot; when &quot;type&quot; is &quot;curses&quot;</p>
<dd>
<dt>The members of &quot;DisplayEGLHeadless&quot; when &quot;type&quot; is &quot;egl-headless&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.12 <code>query-display-options</code> (Command) Returns information about display configuration <code>Returns:</code> <tt>&quot;DisplayOptions&quot;</tt> <code>Since:</code> 3.1 <code>QAuthZListPolicy</code> (Enum) The authorization policy result <code>Values:</code></p>
<dl>
<dt>&quot;deny&quot;</p>
<dd>deny access</p>
<dt>&quot;allow&quot;</p>
<dd>allow access</dl>
<p> <code>Since:</code> 4.0 <code>QAuthZListFormat</code> (Enum) The authorization policy match format <code>Values:</code></p>
<dl>
<dt>&quot;exact&quot;</p>
<dd>an exact string match</p>
<dt>&quot;glob&quot;</p>
<dd>string with ? and * shell wildcard support</dl>
<p> <code>Since:</code> 4.0 <code>QAuthZListRule</code> (Object) A single authorization rule. <code>Members:</code></p>
<dl>
<dt>&quot;match: string&quot;</p>
<dd>a string or glob to match against a user identity</p>
<dt>&quot;policy: QAuthZListPolicy&quot;</p>
<dd>the result to return if <tt>&quot;match&quot;</tt> evaluates to true</p>
<dt>&quot;format: QAuthZListFormat&quot; (optional)</p>
<dd>the format of the <tt>&quot;match&quot;</tt> rule (default &#8216;exact&#8217;)</dl>
<p> <code>Since:</code> 4.0 <code>QAuthZListRuleListHack</code> (Object) Not exposed via <font SIZE="-1">QMP</font>; hack to generate QAuthZListRuleList for use internally by the code. <code>Members:</code></p>
<dl>
<dt>&quot;unused: array of QAuthZListRule&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 4.0</p>
<h3>Migration</h3>
<p><code>MigrationStats</code> (Object) Detailed migration status. <code>Members:</code></p>
<dl>
<dt>&quot;transferred: int&quot;</p>
<dd>amount of bytes already transferred to the target <font SIZE="-1">VM</font></p>
<dt>&quot;remaining: int&quot;</p>
<dd>amount of bytes remaining to be transferred to the target <font SIZE="-1">VM</font></p>
<dt>&quot;total: int&quot;</p>
<dd>total amount of bytes involved in the migration process</p>
<dt>&quot;duplicate: int&quot;</p>
<dd>number of duplicate (zero) pages (since 1.2)</p>
<dt>&quot;skipped: int&quot;</p>
<dd>number of skipped zero pages (since 1.5)</p>
<dt>&quot;normal: int&quot;</p>
<dd>number of normal pages (since 1.2)</p>
<dt>&quot;normal-bytes: int&quot;</p>
<dd>number of normal bytes sent (since 1.2)</p>
<dt>&quot;dirty-pages-rate: int&quot;</p>
<dd>number of pages dirtied by second by the guest (since 1.3)</p>
<dt>&quot;mbps: number&quot;</p>
<dd>throughput in megabits/sec. (since 1.6)</p>
<dt>&quot;dirty-sync-count: int&quot;</p>
<dd>number of times that dirty ram was synchronized (since 2.1)</p>
<dt>&quot;postcopy-requests: int&quot;</p>
<dd>The number of page requests received from the destination (since 2.7)</p>
<dt>&quot;page-size: int&quot;</p>
<dd>The number of bytes per page for the various page-based statistics (since 2.10)</p>
<dt>&quot;multifd-bytes: int&quot;</p>
<dd>The number of bytes sent through multifd (since 3.0)</p>
<dt>&quot;pages-per-second: int&quot;</p>
<dd>the number of memory pages transferred per second (Since 4.0)</dl>
<p> <code>Since:</code> 0.14.0 <code>XBZRLECacheStats</code> (Object) Detailed <font SIZE="-1">XBZRLE</font> migration cache statistics <code>Members:</code></p>
<dl>
<dt>&quot;cache-size: int&quot;</p>
<dd><font SIZE="-1">XBZRLE</font> cache size</p>
<dt>&quot;bytes: int&quot;</p>
<dd>amount of bytes already transferred to the target <font SIZE="-1">VM</font></p>
<dt>&quot;pages: int&quot;</p>
<dd>amount of pages transferred to the target <font SIZE="-1">VM</font></p>
<dt>&quot;cache-miss: int&quot;</p>
<dd>number of cache miss</p>
<dt>&quot;cache-miss-rate: number&quot;</p>
<dd>rate of cache miss (since 2.1)</p>
<dt>&quot;overflow: int&quot;</p>
<dd>number of overflows</dl>
<p> <code>Since:</code> 1.2 <code>CompressionStats</code> (Object) Detailed migration compression statistics <code>Members:</code></p>
<dl>
<dt>&quot;pages: int&quot;</p>
<dd>amount of pages compressed and transferred to the target <font SIZE="-1">VM</font></p>
<dt>&quot;busy: int&quot;</p>
<dd>count of times that no free thread was available to compress data</p>
<dt>&quot;busy-rate: number&quot;</p>
<dd>rate of thread busy</p>
<dt>&quot;compressed-size: int&quot;</p>
<dd>amount of bytes after compression</p>
<dt>&quot;compression-rate: number&quot;</p>
<dd>rate of compressed size</dl>
<p> <code>Since:</code> 3.1 <code>MigrationStatus</code> (Enum) An enumeration of migration status. <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>no migration has ever happened.</p>
<dt>&quot;setup&quot;</p>
<dd>migration process has been initiated.</p>
<dt>&quot;cancelling&quot;</p>
<dd>in the process of cancelling migration.</p>
<dt>&quot;cancelled&quot;</p>
<dd>cancelling migration is finished.</p>
<dt>&quot;active&quot;</p>
<dd>in the process of doing migration.</p>
<dt>&quot;postcopy-active&quot;</p>
<dd>like active, but now in postcopy mode. (since 2.5)</p>
<dt>&quot;postcopy-paused&quot;</p>
<dd>during postcopy but paused. (since 3.0)</p>
<dt>&quot;postcopy-recover&quot;</p>
<dd>trying to recover from a paused postcopy. (since 3.0)</p>
<dt>&quot;completed&quot;</p>
<dd>migration is finished.</p>
<dt>&quot;failed&quot;</p>
<dd>some error occurred during migration process.</p>
<dt>&quot;colo&quot;</p>
<dd><font SIZE="-1">VM</font> is in the process of fault tolerance, <font SIZE="-1">VM</font> can not get into this state unless colo capability is enabled for migration. (since 2.8)</p>
<dt>&quot;pre-switchover&quot;</p>
<dd>Paused before device serialisation. (since 2.11)</p>
<dt>&quot;device&quot;</p>
<dd>During device serialisation when pause-before-switchover is enabled (since 2.11)</p>
<dt>&quot;wait-unplug&quot;</p>
<dd>wait for device unplug request by guest <font SIZE="-1">OS</font> to be completed. (since 4.2)</dl>
<p> <code>Since:</code> 2.3 <code>MigrationInfo</code> (Object) Information about current migration process. <code>Members:</code></p>
<dl>
<dt>&quot;status: MigrationStatus&quot; (optional)</p>
<dd><tt>&quot;MigrationStatus&quot;</tt> describing the current migration status. If this field is not returned, no migration process has been initiated</p>
<dt>&quot;ram: MigrationStats&quot; (optional)</p>
<dd><tt>&quot;MigrationStats&quot;</tt> containing detailed migration status, only returned if status is &#8216;active&#8217; or &#8216;completed'(since 1.2)</p>
<dt>&quot;disk: MigrationStats&quot; (optional)</p>
<dd><tt>&quot;MigrationStats&quot;</tt> containing detailed disk migration status, only returned if status is &#8216;active&#8217; and it is a block migration</p>
<dt>&quot;xbzrle-cache: XBZRLECacheStats&quot; (optional)</p>
<dd><tt>&quot;XBZRLECacheStats&quot;</tt> containing detailed <font SIZE="-1">XBZRLE</font> migration statistics, only returned if <font SIZE="-1">XBZRLE</font> feature is on and status is &#8216;active&#8217; or &#8216;completed&#8217; (since 1.2)</p>
<dt>&quot;total-time: int&quot; (optional)</p>
<dd>total amount of milliseconds since migration started. If migration has ended, it returns the total migration time. (since 1.2)</p>
<dt>&quot;downtime: int&quot; (optional)</p>
<dd>only present when migration finishes correctly total downtime in milliseconds for the guest. (since 1.3)</p>
<dt>&quot;expected-downtime: int&quot; (optional)</p>
<dd>only present while migration is active expected downtime in milliseconds for the guest in last walk of the dirty bitmap. (since 1.3)</p>
<dt>&quot;setup-time: int&quot; (optional)</p>
<dd>amount of setup time in milliseconds <i>before</i> the iterations begin but <i>after</i> the <font SIZE="-1">QMP</font> command is issued. This is designed to provide an accounting of any activities (such as <font SIZE="-1">RDMA</font> pinning) which may be expensive, but do not actually occur during the iterative migration rounds themselves. (since 1.6)</p>
<dt>&quot;cpu-throttle-percentage: int&quot; (optional)</p>
<dd>percentage of time guest cpus are being throttled during auto-converge. This is only present when auto-converge has started throttling guest cpus. (Since 2.7)</p>
<dt>&quot;error-desc: string&quot; (optional)</p>
<dd>the human readable error description string, when <tt>&quot;status&quot;</tt> is &#8216;failed&#8217;. Clients should not attempt to parse the error strings. (Since 2.7)</p>
<dt>&quot;postcopy-blocktime: int&quot; (optional)</p>
<dd>total time when all vCPU were blocked during postcopy live migration. This is only present when the postcopy-blocktime migration capability is enabled. (Since 3.0)</p>
<dt>&quot;postcopy-vcpu-blocktime: array of int&quot; (optional)</p>
<dd>list of the postcopy blocktime per vCPU. This is only present when the postcopy-blocktime migration capability is enabled. (Since 3.0)</p>
<dt>&quot;compression: CompressionStats&quot; (optional)</p>
<dd>migration compression statistics, only returned if compression feature is on and status is &#8216;active&#8217; or &#8216;completed&#8217; (Since 3.1)</p>
<dt>&quot;socket-address: array of SocketAddress&quot; (optional)</p>
<dd>Only used for tcp, to know what the real port is (Since 4.0)</dl>
<p> <code>Since:</code> 0.14.0 <code>query-migrate</code> (Command) Returns information about current migration process. If migration is active there will be another json-object with <font SIZE="-1">RAM</font> migration status and if block migration is active another one with block migration status. <code>Returns:</code> <tt>&quot;MigrationInfo&quot;</tt> <code>Since:</code> 0.14.0 <code>Example:</code> 1. Before the first migration</p>
<p>        -&gt;{&quot;execute&quot; : &quot;query-migrate&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
}</p>
<p>2. Migration is done and has succeeded</p>
<p>        -&gt;{&quot;execute&quot; : &quot;query-migrate&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;status&quot; : &quot;completed&quot;,<br />
                   &quot;total-time&quot; : 12345,<br />
                   &quot;setup-time&quot; : 12345,<br />
                   &quot;downtime&quot; : 12345,<br />
                   &quot;ram&quot;:<br />
        {<br />
            &quot;transferred&quot; : 123,<br />
                &quot;remaining&quot; : 123,<br />
                &quot;total&quot; : 246,<br />
                &quot;duplicate&quot; : 123,<br />
                &quot;normal&quot; : 123,<br />
                &quot;normal-bytes&quot; : 123456,<br />
                &quot;dirty-sync-count&quot; : 15<br />
        }<br />
    }<br />
}</p>
<p>3. Migration is done and has failed</p>
<p>        -&gt;{&quot;execute&quot; : &quot;query-migrate&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;status&quot; : &quot;failed&quot;<br />
    }<br />
}</p>
<p>4. Migration is being performed and is not a block migration :</p>
<p>        -&gt;{&quot;execute&quot; : &quot;query-migrate&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;status&quot; : &quot;active&quot;,<br />
                   &quot;total-time&quot; : 12345,<br />
                   &quot;setup-time&quot; : 12345,<br />
                   &quot;expected-downtime&quot; : 12345,<br />
                   &quot;ram&quot;:<br />
        {<br />
            &quot;transferred&quot; : 123,<br />
                &quot;remaining&quot; : 123,<br />
                &quot;total&quot; : 246,<br />
                &quot;duplicate&quot; : 123,<br />
                &quot;normal&quot; : 123,<br />
                &quot;normal-bytes&quot; : 123456,<br />
                &quot;dirty-sync-count&quot; : 15<br />
        }<br />
    }<br />
}</p>
<p>5. Migration is being performed and is a block migration :</p>
<p>        -&gt;{&quot;execute&quot; : &quot;query-migrate&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;status&quot; : &quot;active&quot;,<br />
                   &quot;total-time&quot; : 12345,<br />
                   &quot;setup-time&quot; : 12345,<br />
                   &quot;expected-downtime&quot; : 12345,<br />
                   &quot;ram&quot; : {<br />
                       &quot;total&quot; : 1057024,<br />
                       &quot;remaining&quot; : 1053304,<br />
                       &quot;transferred&quot; : 3720,<br />
                       &quot;duplicate&quot; : 123,<br />
                       &quot;normal&quot; : 123,<br />
                       &quot;normal-bytes&quot; : 123456,<br />
                       &quot;dirty-sync-count&quot; : 15<br />
                   },<br />
                           &quot;disk&quot;:<br />
        {<br />
            &quot;total&quot; : 20971520,<br />
                &quot;remaining&quot; : 20880384,<br />
                &quot;transferred&quot; : 91136<br />
        }<br />
    }<br />
}</p>
<p>6. Migration is being performed and XBZRLE is active :</p>
<p>        -&gt;{&quot;execute&quot; : &quot;query-migrate&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;status&quot; : &quot;active&quot;,<br />
                   &quot;total-time&quot; : 12345,<br />
                   &quot;setup-time&quot; : 12345,<br />
                   &quot;expected-downtime&quot; : 12345,<br />
                   &quot;ram&quot; : {<br />
                       &quot;total&quot; : 1057024,<br />
                       &quot;remaining&quot; : 1053304,<br />
                       &quot;transferred&quot; : 3720,<br />
                       &quot;duplicate&quot; : 10,<br />
                       &quot;normal&quot; : 3333,<br />
                       &quot;normal-bytes&quot; : 3412992,<br />
                       &quot;dirty-sync-count&quot; : 15<br />
                   },<br />
                           &quot;xbzrle-cache&quot;:<br />
        {<br />
            &quot;cache-size&quot; : 67108864,<br />
                &quot;bytes&quot; : 20971520,<br />
                &quot;pages&quot; : 2444343,<br />
                &quot;cache-miss&quot; : 2244,<br />
                &quot;cache-miss-rate&quot; : 0.123,<br />
                &quot;overflow&quot; : 34434<br />
        }<br />
    }<br />
} <code>MigrationCapability</code> (Enum) Migration capabilities enumeration <code>Values:</code></p>
<dl>
<dt>&quot;xbzrle&quot;</p>
<dd>Migration supports xbzrle (Xor Based Zero Run Length Encoding). This feature allows us to minimize migration traffic for certain work loads, by sending compressed difference of the pages</p>
<dt>&quot;rdma-pin-all&quot;</p>
<dd>Controls whether or not the entire <font SIZE="-1">VM</font> memory footprint is <code>mlock()</code>&#8216;d on demand or all at once. Refer to docs/rdma.txt for usage. Disabled by default. (since 2.0)</p>
<dt>&quot;zero-blocks&quot;</p>
<dd>During storage migration encode blocks of zeroes efficiently. This essentially saves 1MB of zeroes per block on the wire. Enabling requires source and target <font SIZE="-1">VM</font> to support this feature. To enable it is sufficient to enable the capability on the source <font SIZE="-1">VM.</font> The feature is disabled by default. (since 1.6)</p>
<dt>&quot;compress&quot;</p>
<dd>Use multiple compression threads to accelerate live migration. This feature can help to reduce the migration traffic, by sending compressed pages. Please note that if compress and xbzrle are both on, compress only takes effect in the ram bulk stage, after that, it will be disabled and only xbzrle takes effect, this can help to minimize migration traffic. The feature is disabled by default. (since 2.4 )</p>
<dt>&quot;events&quot;</p>
<dd>generate events for each migration state change (since 2.4 )</p>
<dt>&quot;auto-converge&quot;</p>
<dd>If enabled, <font SIZE="-1">QEMU</font> will automatically throttle down the guest to speed up convergence of <font SIZE="-1">RAM</font> migration. (since 1.6)</p>
<dt>&quot;postcopy-ram&quot;</p>
<dd>Start executing on the migration target before all of <font SIZE="-1">RAM</font> has been migrated, pulling the remaining pages along as needed. The capacity must have the same setting on both source and target or migration will not even start. <font SIZE="-1">NOTE:</font> If the migration fails during postcopy the <font SIZE="-1">VM</font> will fail. (since 2.6)</p>
<dt>&quot;x-colo&quot;</p>
<dd>If enabled, migration will never end, and the state of the <font SIZE="-1">VM</font> on the primary side will be migrated continuously to the <font SIZE="-1">VM</font> on secondary side, this process is called COarse-Grain LOck Stepping (<font SIZE="-1">COLO</font>) for Non-stop Service. (since 2.8)</p>
<dt>&quot;release-ram&quot;</p>
<dd>if enabled, qemu will free the migrated ram pages on the source during postcopy-ram migration. (since 2.9)</p>
<dt>&quot;block&quot;</p>
<dd>If enabled, <font SIZE="-1">QEMU</font> will also migrate the contents of all block devices. Default is disabled. A possible alternative uses mirror jobs to a builtin <font SIZE="-1">NBD</font> server on the destination, which offers more flexibility. (Since 2.10)</p>
<dt>&quot;return-path&quot;</p>
<dd>If enabled, migration will use the return path even for precopy. (since 2.10)</p>
<dt>&quot;pause-before-switchover&quot;</p>
<dd>Pause outgoing migration before serialising device state and before disabling block <font SIZE="-1">IO</font> (since 2.11)</p>
<dt>&quot;multifd&quot;</p>
<dd>Use more than one fd for migration (since 4.0)</p>
<dt>&quot;dirty-bitmaps&quot;</p>
<dd>If enabled, <font SIZE="-1">QEMU</font> will migrate named dirty bitmaps. (since 2.12)</p>
<dt>&quot;postcopy-blocktime&quot;</p>
<dd>Calculate downtime for postcopy live migration (since 3.0)</p>
<dt>&quot;late-block-activate&quot;</p>
<dd>If enabled, the destination will not activate block devices (and thus take locks) immediately at the end of migration. (since 3.0)</p>
<dt>&quot;x-ignore-shared&quot;</p>
<dd>If enabled, <font SIZE="-1">QEMU</font> will not migrate shared memory (since 4.0)</p>
<dt>&quot;validate-uuid&quot;</p>
<dd>Send the <font SIZE="-1">UUID</font> of the source to allow the destination to ensure it is the same. (since 4.2)</dl>
<p> <code>Since:</code> 1.2 <code>MigrationCapabilityStatus</code> (Object) Migration capability information <code>Members:</code></p>
<dl>
<dt>&quot;capability: MigrationCapability&quot;</p>
<dd>capability enum</p>
<dt>&quot;state: boolean&quot;</p>
<dd>capability state bool</dl>
<p> <code>Since:</code> 1.2 <code>migrate-set-capabilities</code> (Command) Enable/Disable the following migration capabilities (like xbzrle) <code>Arguments:</code></p>
<dl>
<dt>&quot;capabilities: array of MigrationCapabilityStatus&quot;</p>
<dd>json array of capability modifications to make</dl>
<p> <code>Since:</code> 1.2 <code>Example:</code> </p>
<pre> -&gt; { &quot;execute&quot;: &quot;migrate-set-capabilities&quot; , &quot;arguments&quot;:
 { &quot;capabilities&quot;: [ { &quot;capability&quot;: &quot;xbzrle&quot;, &quot;state&quot;: true } ] } }</pre>
<p><code>query-migrate-capabilities</code> (Command) Returns information about the current migration capabilities status <code>Returns:</code> <tt>&quot;MigrationCapabilitiesStatus&quot;</tt> <code>Since:</code> 1.2 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-migrate-capabilities&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {&quot;state&quot; : false, &quot;capability&quot; : &quot;xbzrle&quot;},<br />
        {&quot;state&quot; : false, &quot;capability&quot; : &quot;rdma-pin-all&quot;},<br />
        {&quot;state&quot; : false, &quot;capability&quot; : &quot;auto-converge&quot;},<br />
        {&quot;state&quot; : false, &quot;capability&quot; : &quot;zero-blocks&quot;},<br />
        {&quot;state&quot; : false, &quot;capability&quot; : &quot;compress&quot;},<br />
        {&quot;state&quot; : true, &quot;capability&quot; : &quot;events&quot;},<br />
        {&quot;state&quot; : false, &quot;capability&quot; : &quot;postcopy-ram&quot;},<br />
        {&quot;state&quot; : false, &quot;capability&quot; : &quot;x-colo&quot;}<br />
    ]<br />
} <code>MigrationParameter</code> (Enum) Migration parameters enumeration <code>Values:</code></p>
<dl>
<dt>&quot;announce-initial&quot;</p>
<dd>Initial delay (in milliseconds) before sending the first announce (Since 4.0)</p>
<dt>&quot;announce-max&quot;</p>
<dd>Maximum delay (in milliseconds) between packets in the announcement (Since 4.0)</p>
<dt>&quot;announce-rounds&quot;</p>
<dd>Number of self-announce packets sent after migration (Since 4.0)</p>
<dt>&quot;announce-step&quot;</p>
<dd>Increase in delay (in milliseconds) between subsequent packets in the announcement (Since 4.0)</p>
<dt>&quot;compress-level&quot;</p>
<dd>Set the compression level to be used in live migration, the compression level is an integer between 0 and 9, where 0 means no compression, 1 means the best compression speed, and 9 means best compression ratio which will consume more <font SIZE="-1">CPU.</font></p>
<dt>&quot;compress-threads&quot;</p>
<dd>Set compression thread count to be used in live migration, the compression thread count is an integer between 1 and 255.</p>
<dt>&quot;compress-wait-thread&quot;</p>
<dd>Controls behavior when all compression threads are currently busy. If true (default), wait for a free compression thread to become available; otherwise, send the page uncompressed. (Since 3.1)</p>
<dt>&quot;decompress-threads&quot;</p>
<dd>Set decompression thread count to be used in live migration, the decompression thread count is an integer between 1 and 255. Usually, decompression is at least 4 times as fast as compression, so set the decompress-threads to the number about 1/4 of compress-threads is adequate.</p>
<dt>&quot;cpu-throttle-initial&quot;</p>
<dd>Initial percentage of time guest cpus are throttled when migration auto-converge is activated. The default value is 20. (Since 2.7)</p>
<dt>&quot;cpu-throttle-increment&quot;</p>
<dd>throttle percentage increase each time auto-converge detects that migration is not making progress. The default value is 10. (Since 2.7)</p>
<dt>&quot;tls-creds&quot;</p>
<dd><font SIZE="-1">ID</font> of the &#8216;tls-creds&#8217; object that provides credentials for establishing a <font SIZE="-1">TLS</font> connection over the migration data channel. On the outgoing side of the migration, the credentials must be for a &#8216;client&#8217; endpoint, while for the incoming side the credentials must be for a &#8216;server&#8217; endpoint. Setting this will enable <font SIZE="-1">TLS</font> for all migrations. The default is unset, resulting in unsecured migration at the <font SIZE="-1">QEMU</font> level. (Since 2.7)</p>
<dt>&quot;tls-hostname&quot;</p>
<dd>hostname of the target host for the migration. This is required when using x509 based <font SIZE="-1">TLS</font> credentials and the migration <font SIZE="-1">URI</font> does not already include a hostname. For example if using fd: or exec: based migration, the hostname must be provided so that the server&#8217;s x509 certificate identity can be validated. (Since 2.7)</p>
<dt>&quot;tls-authz&quot;</p>
<dd><font SIZE="-1">ID</font> of the &#8216;authz&#8217; object subclass that provides access control checking of the <font SIZE="-1">TLS</font> x509 certificate distinguished name. This object is only resolved at time of use, so can be deleted and recreated on the fly while the migration server is active. If missing, it will default to denying access (Since 4.0)</p>
<dt>&quot;max-bandwidth&quot;</p>
<dd>to set maximum speed for migration. maximum speed in bytes per second. (Since 2.8)</p>
<dt>&quot;downtime-limit&quot;</p>
<dd>set maximum tolerated downtime for migration. maximum downtime in milliseconds (Since 2.8)</p>
<dt>&quot;x-checkpoint-delay&quot;</p>
<dd>The delay time (in ms) between two <font SIZE="-1">COLO</font> checkpoints in periodic mode. (Since 2.8)</p>
<dt>&quot;block-incremental&quot;</p>
<dd>Affects how much storage is migrated when the block migration capability is enabled. When false, the entire storage backing chain is migrated into a flattened image at the destination; when true, only the active qcow2 layer is migrated and the destination must already have access to the same backing chain as was used on the source. (since 2.10)</p>
<dt>&quot;multifd-channels&quot;</p>
<dd>Number of channels used to migrate data in parallel. This is the same number that the number of sockets used for migration. The default value is 2 (since 4.0)</p>
<dt>&quot;xbzrle-cache-size&quot;</p>
<dd>cache size to be used by <font SIZE="-1">XBZRLE</font> migration. It needs to be a multiple of the target page size and a power of 2 (Since 2.11)</p>
<dt>&quot;max-postcopy-bandwidth&quot;</p>
<dd>Background transfer bandwidth during postcopy. Defaults to 0 (unlimited). In bytes per second. (Since 3.0)</p>
<dt>&quot;max-cpu-throttle&quot;</p>
<dd>maximum cpu throttle percentage. Defaults to 99. (Since 3.1)</dl>
<p> <code>Since:</code> 2.4 <code>MigrateSetParameters</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;announce-initial: int&quot; (optional)</p>
<dd>Initial delay (in milliseconds) before sending the first announce (Since 4.0)</p>
<dt>&quot;announce-max: int&quot; (optional)</p>
<dd>Maximum delay (in milliseconds) between packets in the announcement (Since 4.0)</p>
<dt>&quot;announce-rounds: int&quot; (optional)</p>
<dd>Number of self-announce packets sent after migration (Since 4.0)</p>
<dt>&quot;announce-step: int&quot; (optional)</p>
<dd>Increase in delay (in milliseconds) between subsequent packets in the announcement (Since 4.0)</p>
<dt>&quot;compress-level: int&quot; (optional)</p>
<dd>compression level</p>
<dt>&quot;compress-threads: int&quot; (optional)</p>
<dd>compression thread count</p>
<dt>&quot;compress-wait-thread: boolean&quot; (optional)</p>
<dd>Controls behavior when all compression threads are currently busy. If true (default), wait for a free compression thread to become available; otherwise, send the page uncompressed. (Since 3.1)</p>
<dt>&quot;decompress-threads: int&quot; (optional)</p>
<dd>decompression thread count</p>
<dt>&quot;cpu-throttle-initial: int&quot; (optional)</p>
<dd>Initial percentage of time guest cpus are throttled when migration auto-converge is activated. The default value is 20. (Since 2.7)</p>
<dt>&quot;cpu-throttle-increment: int&quot; (optional)</p>
<dd>throttle percentage increase each time auto-converge detects that migration is not making progress. The default value is 10. (Since 2.7)</p>
<dt>&quot;tls-creds: StrOrNull&quot; (optional)</p>
<dd><font SIZE="-1">ID</font> of the &#8216;tls-creds&#8217; object that provides credentials for establishing a <font SIZE="-1">TLS</font> connection over the migration data channel. On the outgoing side of the migration, the credentials must be for a &#8216;client&#8217; endpoint, while for the incoming side the credentials must be for a &#8216;server&#8217; endpoint. Setting this to a non-empty string enables <font SIZE="-1">TLS</font> for all migrations. An empty string means that <font SIZE="-1">QEMU</font> will use plain text mode for migration, rather than <font SIZE="-1">TLS</font> (Since 2.9) Previously (since 2.7), this was reported by omitting tls-creds instead.</p>
<dt>&quot;tls-hostname: StrOrNull&quot; (optional)</p>
<dd>hostname of the target host for the migration. This is required when using x509 based <font SIZE="-1">TLS</font> credentials and the migration <font SIZE="-1">URI</font> does not already include a hostname. For example if using fd: or exec: based migration, the hostname must be provided so that the server&#8217;s x509 certificate identity can be validated. (Since 2.7) An empty string means that <font SIZE="-1">QEMU</font> will use the hostname associated with the migration <font SIZE="-1">URI,</font> if any. (Since 2.9) Previously (since 2.7), this was reported by omitting tls-hostname instead.</p>
<dt>&quot;max-bandwidth: int&quot; (optional)</p>
<dd>to set maximum speed for migration. maximum speed in bytes per second. (Since 2.8)</p>
<dt>&quot;downtime-limit: int&quot; (optional)</p>
<dd>set maximum tolerated downtime for migration. maximum downtime in milliseconds (Since 2.8)</p>
<dt>&quot;x-checkpoint-delay: int&quot; (optional)</p>
<dd>the delay time between two <font SIZE="-1">COLO</font> checkpoints. (Since 2.8)</p>
<dt>&quot;block-incremental: boolean&quot; (optional)</p>
<dd>Affects how much storage is migrated when the block migration capability is enabled. When false, the entire storage backing chain is migrated into a flattened image at the destination; when true, only the active qcow2 layer is migrated and the destination must already have access to the same backing chain as was used on the source. (since 2.10)</p>
<dt>&quot;multifd-channels: int&quot; (optional)</p>
<dd>Number of channels used to migrate data in parallel. This is the same number that the number of sockets used for migration. The default value is 2 (since 4.0)</p>
<dt>&quot;xbzrle-cache-size: int&quot; (optional)</p>
<dd>cache size to be used by <font SIZE="-1">XBZRLE</font> migration. It needs to be a multiple of the target page size and a power of 2 (Since 2.11)</p>
<dt>&quot;max-postcopy-bandwidth: int&quot; (optional)</p>
<dd>Background transfer bandwidth during postcopy. Defaults to 0 (unlimited). In bytes per second. (Since 3.0)</p>
<dt>&quot;max-cpu-throttle: int&quot; (optional)</p>
<dd>maximum cpu throttle percentage. The default value is 99. (Since 3.1)</p>
<dt>&quot;tls-authz: StrOrNull&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.4 <code>migrate-set-parameters</code> (Command) Set various migration parameters. <code>Arguments:</code> the members of <tt>&quot;MigrateSetParameters&quot;</tt> <code>Since:</code> 2.4 <code>Example:</code> </p>
<pre> -&gt; { &quot;execute&quot;: &quot;migrate-set-parameters&quot; ,
 &quot;arguments&quot;: { &quot;compress-level&quot;: 1 } }</pre>
<p><code>MigrationParameters</code> (Object) The optional members aren&#8217;t actually optional. <code>Members:</code></p>
<dl>
<dt>&quot;announce-initial: int&quot; (optional)</p>
<dd>Initial delay (in milliseconds) before sending the first announce (Since 4.0)</p>
<dt>&quot;announce-max: int&quot; (optional)</p>
<dd>Maximum delay (in milliseconds) between packets in the announcement (Since 4.0)</p>
<dt>&quot;announce-rounds: int&quot; (optional)</p>
<dd>Number of self-announce packets sent after migration (Since 4.0)</p>
<dt>&quot;announce-step: int&quot; (optional)</p>
<dd>Increase in delay (in milliseconds) between subsequent packets in the announcement (Since 4.0)</p>
<dt>&quot;compress-level: int&quot; (optional)</p>
<dd>compression level</p>
<dt>&quot;compress-threads: int&quot; (optional)</p>
<dd>compression thread count</p>
<dt>&quot;compress-wait-thread: boolean&quot; (optional)</p>
<dd>Controls behavior when all compression threads are currently busy. If true (default), wait for a free compression thread to become available; otherwise, send the page uncompressed. (Since 3.1)</p>
<dt>&quot;decompress-threads: int&quot; (optional)</p>
<dd>decompression thread count</p>
<dt>&quot;cpu-throttle-initial: int&quot; (optional)</p>
<dd>Initial percentage of time guest cpus are throttled when migration auto-converge is activated. (Since 2.7)</p>
<dt>&quot;cpu-throttle-increment: int&quot; (optional)</p>
<dd>throttle percentage increase each time auto-converge detects that migration is not making progress. (Since 2.7)</p>
<dt>&quot;tls-creds: string&quot; (optional)</p>
<dd><font SIZE="-1">ID</font> of the &#8216;tls-creds&#8217; object that provides credentials for establishing a <font SIZE="-1">TLS</font> connection over the migration data channel. On the outgoing side of the migration, the credentials must be for a &#8216;client&#8217; endpoint, while for the incoming side the credentials must be for a &#8216;server&#8217; endpoint. An empty string means that <font SIZE="-1">QEMU</font> will use plain text mode for migration, rather than <font SIZE="-1">TLS</font> (Since 2.7) Note: 2.8 reports this by omitting tls-creds instead.</p>
<dt>&quot;tls-hostname: string&quot; (optional)</p>
<dd>hostname of the target host for the migration. This is required when using x509 based <font SIZE="-1">TLS</font> credentials and the migration <font SIZE="-1">URI</font> does not already include a hostname. For example if using fd: or exec: based migration, the hostname must be provided so that the server&#8217;s x509 certificate identity can be validated. (Since 2.7) An empty string means that <font SIZE="-1">QEMU</font> will use the hostname associated with the migration <font SIZE="-1">URI,</font> if any. (Since 2.9) Note: 2.8 reports this by omitting tls-hostname instead.</p>
<dt>&quot;tls-authz: string&quot; (optional)</p>
<dd><font SIZE="-1">ID</font> of the &#8216;authz&#8217; object subclass that provides access control checking of the <font SIZE="-1">TLS</font> x509 certificate distinguished name. (Since 4.0)</p>
<dt>&quot;max-bandwidth: int&quot; (optional)</p>
<dd>to set maximum speed for migration. maximum speed in bytes per second. (Since 2.8)</p>
<dt>&quot;downtime-limit: int&quot; (optional)</p>
<dd>set maximum tolerated downtime for migration. maximum downtime in milliseconds (Since 2.8)</p>
<dt>&quot;x-checkpoint-delay: int&quot; (optional)</p>
<dd>the delay time between two <font SIZE="-1">COLO</font> checkpoints. (Since 2.8)</p>
<dt>&quot;block-incremental: boolean&quot; (optional)</p>
<dd>Affects how much storage is migrated when the block migration capability is enabled. When false, the entire storage backing chain is migrated into a flattened image at the destination; when true, only the active qcow2 layer is migrated and the destination must already have access to the same backing chain as was used on the source. (since 2.10)</p>
<dt>&quot;multifd-channels: int&quot; (optional)</p>
<dd>Number of channels used to migrate data in parallel. This is the same number that the number of sockets used for migration. The default value is 2 (since 4.0)</p>
<dt>&quot;xbzrle-cache-size: int&quot; (optional)</p>
<dd>cache size to be used by <font SIZE="-1">XBZRLE</font> migration. It needs to be a multiple of the target page size and a power of 2 (Since 2.11)</p>
<dt>&quot;max-postcopy-bandwidth: int&quot; (optional)</p>
<dd>Background transfer bandwidth during postcopy. Defaults to 0 (unlimited). In bytes per second. (Since 3.0)</p>
<dt>&quot;max-cpu-throttle: int&quot; (optional)</p>
<dd>maximum cpu throttle percentage. Defaults to 99. (Since 3.1)</dl>
<p> <code>Since:</code> 2.4 <code>query-migrate-parameters</code> (Command) Returns information about the current migration parameters <code>Returns:</code> <tt>&quot;MigrationParameters&quot;</tt> <code>Since:</code> 2.4 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-migrate-parameters&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;decompress-threads&quot; : 2,<br />
            &quot;cpu-throttle-increment&quot; : 10,<br />
            &quot;compress-threads&quot; : 8,<br />
            &quot;compress-level&quot; : 1,<br />
            &quot;cpu-throttle-initial&quot; : 20,<br />
            &quot;max-bandwidth&quot; : 33554432,<br />
            &quot;downtime-limit&quot; : 300<br />
    }<br />
} <code>client_migrate_info</code> (Command) Set migration information for remote display. This makes the server ask the client to automatically reconnect using the new parameters once migration finished successfully. Only implemented for <font SIZE="-1">SPICE.</font> <code>Arguments:</code></p>
<dl>
<dt>&quot;protocol: string&quot;</p>
<dd>must be &#8220;spice&#8221;</p>
<dt>&quot;hostname: string&quot;</p>
<dd>migration target hostname</p>
<dt>&quot;port: int&quot; (optional)</p>
<dd>spice tcp port for plaintext channels</p>
<dt>&quot;tls-port: int&quot; (optional)</p>
<dd>spice tcp port for tls-secured channels</p>
<dt>&quot;cert-subject: string&quot; (optional)</p>
<dd>server certificate subject</dl>
<p> <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;client_migrate_info&quot;,<br />
   &quot;arguments&quot; : {&quot;protocol&quot; : &quot;spice&quot;,<br />
                  &quot;hostname&quot; : &quot;virt42.lab.kraxel.org&quot;,<br />
                  &quot;port&quot; : 1234}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>migrate-start-postcopy</code> (Command) Followup to a migration command to switch the migration to postcopy mode. The postcopy-ram capability must be set on both source and destination before the original migration command. <code>Since:</code> 2.5 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;migrate-start-postcopy&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <font SIZE="-1"><code>MIGRATION</code></font> (Event) Emitted when a migration event happens <code>Arguments:</code></p>
<dl>
<dt>&quot;status: MigrationStatus&quot;</p>
<dd><tt>&quot;MigrationStatus&quot;</tt> describing the current migration status.</dl>
<p> <code>Since:</code> 2.4 <code>Example:</code> </p>
<pre> &lt;- {&quot;timestamp&quot;: {&quot;seconds&quot;: 1432121972, &quot;microseconds&quot;: 744001},
 &quot;event&quot;: &quot;MIGRATION&quot;,
 &quot;data&quot;: {&quot;status&quot;: &quot;completed&quot;} }</pre>
<p><font SIZE="-1"><code>MIGRATION_PASS</code></font> (Event) Emitted from the source side of a migration at the start of each pass (when it syncs the dirty bitmap) <code>Arguments:</code></p>
<dl>
<dt>&quot;pass: int&quot;</p>
<dd>An incrementing count (starting at 1 on the first pass)</dl>
<p> <code>Since:</code> 2.6 <code>Example:</code> { &quot;timestamp&quot;: {&quot;seconds&quot;: 1449669631, &quot;microseconds&quot;: 239225},<br />
    &quot;event&quot;: &quot;MIGRATION_PASS&quot;, &quot;data&quot;: {&quot;pass&quot;: 2} } <code>COLOMessage</code> (Enum) The message transmission between Primary side and Secondary side. <code>Values:</code></p>
<dl>
<dt>&quot;checkpoint-ready&quot;</p>
<dd>Secondary <font SIZE="-1">VM</font> (<font SIZE="-1">SVM</font>) is ready for checkpointing</p>
<dt>&quot;checkpoint-request&quot;</p>
<dd>Primary <font SIZE="-1">VM</font> (<font SIZE="-1">PVM</font>) tells <font SIZE="-1">SVM</font> to prepare for checkpointing</p>
<dt>&quot;checkpoint-reply&quot;</p>
<dd><font SIZE="-1">SVM</font> gets <font SIZE="-1">PVM</font>&#8216;s checkpoint request</p>
<dt>&quot;vmstate-send&quot;</p>
<dd><font SIZE="-1">VM</font>&#8216;s state will be sent by <font SIZE="-1">PVM.</font></p>
<dt>&quot;vmstate-size&quot;</p>
<dd>The total size of VMstate.</p>
<dt>&quot;vmstate-received&quot;</p>
<dd><font SIZE="-1">VM</font>&#8216;s state has been received by <font SIZE="-1">SVM.</font></p>
<dt>&quot;vmstate-loaded&quot;</p>
<dd><font SIZE="-1">VM</font>&#8216;s state has been loaded by <font SIZE="-1">SVM.</font></dl>
<p> <code>Since:</code> 2.8 <code>COLOMode</code> (Enum) The <font SIZE="-1">COLO</font> current mode. <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd><font SIZE="-1">COLO</font> is disabled.</p>
<dt>&quot;primary&quot;</p>
<dd><font SIZE="-1">COLO</font> node in primary side.</p>
<dt>&quot;secondary&quot;</p>
<dd><font SIZE="-1">COLO</font> node in slave side.</dl>
<p> <code>Since:</code> 2.8 <code>FailoverStatus</code> (Enum) An enumeration of <font SIZE="-1">COLO</font> failover status <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>no failover has ever happened</p>
<dt>&quot;require&quot;</p>
<dd>got failover requirement but not handled</p>
<dt>&quot;active&quot;</p>
<dd>in the process of doing failover</p>
<dt>&quot;completed&quot;</p>
<dd>finish the process of failover</p>
<dt>&quot;relaunch&quot;</p>
<dd>restart the failover process, from &#8216;none&#8217; -&gt; &#8216;completed&#8217; (Since 2.9)</dl>
<p> <code>Since:</code> 2.8 <font SIZE="-1"><code>COLO_EXIT</code></font> (Event) Emitted when <font SIZE="-1">VM</font> finishes <font SIZE="-1">COLO</font> mode due to some errors happening or at the request of users. <code>Arguments:</code></p>
<dl>
<dt>&quot;mode: COLOMode&quot;</p>
<dd>report <font SIZE="-1">COLO</font> mode when <font SIZE="-1">COLO</font> exited.</p>
<dt>&quot;reason: COLOExitReason&quot;</p>
<dd>describes the reason for the <font SIZE="-1">COLO</font> exit.</dl>
<p> <code>Since:</code> 3.1 <code>Example:</code> </p>
<pre> &lt;- { &quot;timestamp&quot;: {&quot;seconds&quot;: 2032141960, &quot;microseconds&quot;: 417172},
 &quot;event&quot;: &quot;COLO_EXIT&quot;, &quot;data&quot;: {&quot;mode&quot;: &quot;primary&quot;, &quot;reason&quot;: &quot;request&quot; } }</pre>
<p><code>COLOExitReason</code> (Enum) The reason for a <font SIZE="-1">COLO</font> exit. <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>failover has never happened. This state does not occur in the <font SIZE="-1">COLO_EXIT</font> event, and is only visible in the result of query-colo-status.</p>
<dt>&quot;request&quot;</p>
<dd><font SIZE="-1">COLO</font> exit is due to an external request.</p>
<dt>&quot;error&quot;</p>
<dd><font SIZE="-1">COLO</font> exit is due to an internal error.</p>
<dt>&quot;processing&quot;</p>
<dd><font SIZE="-1">COLO</font> is currently handling a failover (since 4.0).</dl>
<p> <code>Since:</code> 3.1 <code>x-colo-lost-heartbeat</code> (Command) Tell qemu that heartbeat is lost, request it to do takeover procedures. If this command is sent to the <font SIZE="-1">PVM,</font> the Primary side will exit <font SIZE="-1">COLO</font> mode. If sent to the Secondary, the Secondary side will run failover work, then takes over server operation to become the service <font SIZE="-1">VM.</font> <code>Since:</code> 2.8 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;x-colo-lost-heartbeat&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>migrate_cancel</code> (Command) Cancel the current executing migration process. <code>Returns:</code> nothing on success <code>Notes:</code> This command succeeds even if there is no migration process running. <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;migrate_cancel&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>migrate-continue</code> (Command) Continue migration when it&#8217;s in a paused state. <code>Arguments:</code></p>
<dl>
<dt>&quot;state: MigrationStatus&quot;</p>
<dd>The state the migration is currently expected to be in</dl>
<p> <code>Returns:</code> nothing on success <code>Since:</code> 2.11 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;migrate-continue&quot;, &quot;arguments&quot; : {&quot;state&quot; : &quot;pre-switchover&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>migrate_set_downtime</code> (Command) Set maximum tolerated downtime for migration. <code>Arguments:</code></p>
<dl>
<dt>&quot;value: number&quot;</p>
<dd>maximum downtime in seconds</dl>
<p> <code>Returns:</code> nothing on success <code>Notes:</code> This command is deprecated in favor of &#8216;migrate-set-parameters&#8217; <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;migrate_set_downtime&quot;, &quot;arguments&quot; : {&quot;value&quot; : 0.1}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>migrate_set_speed</code> (Command) Set maximum speed for migration. <code>Arguments:</code></p>
<dl>
<dt>&quot;value: int&quot;</p>
<dd>maximum speed in bytes per second.</dl>
<p> <code>Returns:</code> nothing on success <code>Notes:</code> This command is deprecated in favor of &#8216;migrate-set-parameters&#8217; <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;migrate_set_speed&quot;, &quot;arguments&quot; : {&quot;value&quot; : 1024}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>migrate-set-cache-size</code> (Command) Set cache size to be used by <font SIZE="-1">XBZRLE</font> migration <code>Arguments:</code></p>
<dl>
<dt>&quot;value: int&quot;</p>
<dd>cache size in bytes</dl>
<p> The size will be rounded down to the nearest power of 2. The cache size can be modified before and during ongoing migration <code>Returns:</code> nothing on success <code>Notes:</code> This command is deprecated in favor of &#8216;migrate-set-parameters&#8217; <code>Since:</code> 1.2 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;migrate-set-cache-size&quot;,<br />
   &quot;arguments&quot; : {&quot;value&quot; : 536870912}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>query-migrate-cache-size</code> (Command) Query migration <font SIZE="-1">XBZRLE</font> cache size <code>Returns:</code> <font SIZE="-1">XBZRLE</font> cache size in bytes <code>Notes:</code> This command is deprecated in favor of &#8216;query-migrate-parameters&#8217; <code>Since:</code> 1.2 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-migrate-cache-size&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : 67108864<br />
} <code>migrate</code> (Command) Migrates the current running guest to another Virtual Machine. <code>Arguments:</code></p>
<dl>
<dt>&quot;uri: string&quot;</p>
<dd>the Uniform Resource Identifier of the destination <font SIZE="-1">VM</font></p>
<dt>&quot;blk: boolean&quot; (optional)</p>
<dd>do block migration (full disk copy)</p>
<dt>&quot;inc: boolean&quot; (optional)</p>
<dd>incremental disk copy migration</p>
<dt>&quot;detach: boolean&quot; (optional)</p>
<dd>this argument exists only for compatibility reasons and is ignored by <font SIZE="-1">QEMU</font></p>
<dt>&quot;resume: boolean&quot; (optional)</p>
<dd>resume one paused migration, default &#8220;off&#8221;. (since 3.0)</dl>
<p> <code>Returns:</code> nothing on success <code>Since:</code> 0.14.0 <code>Notes:</code></p>
<dl>
<dt>1.</p>
<dd>The &#8216;query-migrate&#8217; command should be used to check migration&#8217;s progress and final result (this information is provided by the &#8216;status&#8217; member)</p>
<dt>2.</p>
<dd>All boolean arguments default to false</p>
<dt>3.</p>
<dd>The user Monitor&#8217;s &#8220;detach&#8221; argument is invalid in <font SIZE="-1">QMP</font> and should not be used</dl>
<p> <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;migrate&quot;, &quot;arguments&quot; : {&quot;uri&quot; : &quot;tcp:0:4446&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>migrate-incoming</code> (Command) Start an incoming migration, the qemu must have been started with -incoming defer <code>Arguments:</code></p>
<dl>
<dt>&quot;uri: string&quot;</p>
<dd>The Uniform Resource Identifier identifying the source or address to listen on</dl>
<p> <code>Returns:</code> nothing on success <code>Since:</code> 2.3 <code>Notes:</code></p>
<dl>
<dt>1.</p>
<dd>It&#8217;s a bad idea to use a string for the uri, but it needs to stay compatible with -incoming and the format of the uri is already exposed above libvirt.</p>
<dt>2.</p>
<dd><font SIZE="-1">QEMU</font> must be started with -incoming defer to allow migrate-incoming to be used.</p>
<dt>3.</p>
<dd>The uri format is the same as for -incoming</dl>
<p> <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;migrate-incoming&quot;,<br />
   &quot;arguments&quot; : {&quot;uri&quot; : &quot;tcp::4446&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>xen-save-devices-state</code> (Command) Save the state of all devices to file. The <font SIZE="-1">RAM</font> and the block devices of the <font SIZE="-1">VM</font> are not saved by this command. <code>Arguments:</code></p>
<dl>
<dt>&quot;filename: string&quot;</p>
<dd>the file to save the state of the devices to as binary data. See xen-save-devices-state.txt for a description of the binary format.</p>
<dt>&quot;live: boolean&quot; (optional)</p>
<dd>Optional argument to ask <font SIZE="-1">QEMU</font> to treat this command as part of a live migration. Default to true. (since 2.11)</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 1.1 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;xen-save-devices-state&quot;,<br />
   &quot;arguments&quot; : {&quot;filename&quot; : &quot;/tmp/save&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>xen-set-replication</code> (Command) Enable or disable replication. <code>Arguments:</code></p>
<dl>
<dt>&quot;enable: boolean&quot;</p>
<dd>true to enable, false to disable.</p>
<dt>&quot;primary: boolean&quot;</p>
<dd>true for primary or false for secondary.</p>
<dt>&quot;failover: boolean&quot; (optional)</p>
<dd>true to do failover, false to stop. but cannot be specified if &#8216;enable&#8217; is true. default value is false.</dl>
<p> <code>Returns:</code> nothing. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;xen-set-replication&quot;,<br />
   &quot;arguments&quot; : {&quot;enable&quot; : true, &quot;primary&quot; : false}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>Since:</code> 2.9 <code>If:</code> <tt>&quot;defined(CONFIG_REPLICATION)&quot;</tt> <code>ReplicationStatus</code> (Object) The result format for &#8216;query-xen-replication-status&#8217;. <code>Members:</code></p>
<dl>
<dt>&quot;error: boolean&quot;</p>
<dd>true if an error happened, false if replication is normal.</p>
<dt>&quot;desc: string&quot; (optional)</p>
<dd>the human readable error description string, when <tt>&quot;error&quot;</tt> is &#8216;true&#8217;.</dl>
<p> <code>Since:</code> 2.9 <code>If:</code> <tt>&quot;defined(CONFIG_REPLICATION)&quot;</tt> <code>query-xen-replication-status</code> (Command) Query replication status while the vm is running. <code>Returns:</code> A <tt>&quot;ReplicationResult&quot;</tt> object showing the status. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-xen-replication-status&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;error&quot; : false<br />
    }<br />
} <code>Since:</code> 2.9 <code>If:</code> <tt>&quot;defined(CONFIG_REPLICATION)&quot;</tt> <code>xen-colo-do-checkpoint</code> (Command) Xen uses this command to notify replication to trigger a checkpoint. <code>Returns:</code> nothing. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;xen-colo-do-checkpoint&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>Since:</code> 2.9 <code>If:</code> <tt>&quot;defined(CONFIG_REPLICATION)&quot;</tt> <code>COLOStatus</code> (Object) The result format for &#8216;query-colo-status&#8217;. <code>Members:</code></p>
<dl>
<dt>&quot;mode: COLOMode&quot;</p>
<dd><font SIZE="-1">COLO</font> running mode. If <font SIZE="-1">COLO</font> is running, this field will return &#8216;primary&#8217; or &#8216;secondary&#8217;.</p>
<dt>&quot;last-mode: COLOMode&quot;</p>
<dd><font SIZE="-1">COLO</font> last running mode. If <font SIZE="-1">COLO</font> is running, this field will return same like mode field, after failover we can use this field to get last colo mode. (since 4.0)</p>
<dt>&quot;reason: COLOExitReason&quot;</p>
<dd>describes the reason for the <font SIZE="-1">COLO</font> exit.</dl>
<p> <code>Since:</code> 3.1 <code>query-colo-status</code> (Command) Query <font SIZE="-1">COLO</font> status while the vm is running. <code>Returns:</code> A <tt>&quot;COLOStatus&quot;</tt> object showing the status. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-colo-status&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;mode&quot; : &quot;primary&quot;, &quot;reason&quot; : &quot;request&quot;<br />
    }<br />
} <code>Since:</code> 3.1 <code>migrate-recover</code> (Command) Provide a recovery migration stream <font SIZE="-1">URI.</font> <code>Arguments:</code></p>
<dl>
<dt>&quot;uri: string&quot;</p>
<dd>the <font SIZE="-1">URI</font> to be used for the recovery of migration stream.</dl>
<p> <code>Returns:</code> nothing. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;migrate-recover&quot;,<br />
   &quot;arguments&quot; : {&quot;uri&quot; : &quot;tcp:192.168.1.200:12345&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>Since:</code> 3.0 <code>migrate-pause</code> (Command) Pause a migration. Currently it only supports postcopy. <code>Returns:</code> nothing. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;migrate-pause&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>Since:</code> 3.0 <font SIZE="-1"><code>UNPLUG_PRIMARY</code></font> (Event) Emitted from source side of a migration when migration state is <font SIZE="-1">WAIT_UNPLUG.</font> Device was unplugged by guest operating system. Device resources in <font SIZE="-1">QEMU</font> are kept on standby to be able to re-plug it in case of migration failure. <code>Arguments:</code></p>
<dl>
<dt>&quot;device-id: string&quot;</p>
<dd><font SIZE="-1">QEMU</font> device id of the unplugged device</dl>
<p> <code>Since:</code> 4.2 <code>Example:</code> </p>
<pre> {&quot;event&quot;: &quot;UNPLUG_PRIMARY&quot;, &quot;data&quot;: {&quot;device-id&quot;: &quot;hostdev0&quot;} }</pre>
<h3>Transactions</h3>
<p><code>Abort</code> (Object) This action can be used to test transaction failure. <code>Since:</code> 1.6 <code>ActionCompletionMode</code> (Enum) An enumeration of Transactional completion modes. <code>Values:</code></p>
<dl>
<dt>&quot;individual&quot;</p>
<dd>Do not attempt to cancel any other Actions if any Actions fail after the Transaction request succeeds. All Actions that can complete successfully will do so without waiting on others. This is the default.</p>
<dt>&quot;grouped&quot;</p>
<dd>If any Action fails after the Transaction succeeds, cancel all Actions. Actions do not complete until all Actions are ready to complete. May be rejected by Actions that do not support this completion mode.</dl>
<p> <code>Since:</code> 2.5 <code>TransactionAction</code> (Object) A discriminated record of operations that can be performed with <tt>&quot;transaction&quot;</tt>. Action <tt>&quot;type&quot;</tt> can be:</p>
<dl>
<dt>&#8211;</p>
<dd><tt>&quot;abort&quot;</tt>: since 1.6</p>
<dt>&#8211;</p>
<dd><tt>&quot;block-dirty-bitmap-add&quot;</tt>: since 2.5</p>
<dt>&#8211;</p>
<dd><tt>&quot;block-dirty-bitmap-remove&quot;</tt>: since 4.2</p>
<dt>&#8211;</p>
<dd><tt>&quot;block-dirty-bitmap-clear&quot;</tt>: since 2.5</p>
<dt>&#8211;</p>
<dd><tt>&quot;block-dirty-bitmap-enable&quot;</tt>: since 4.0</p>
<dt>&#8211;</p>
<dd><tt>&quot;block-dirty-bitmap-disable&quot;</tt>: since 4.0</p>
<dt>&#8211;</p>
<dd><tt>&quot;block-dirty-bitmap-merge&quot;</tt>: since 4.0</p>
<dt>&#8211;</p>
<dd><tt>&quot;blockdev-backup&quot;</tt>: since 2.3</p>
<dt>&#8211;</p>
<dd><tt>&quot;blockdev-snapshot&quot;</tt>: since 2.5</p>
<dt>&#8211;</p>
<dd><tt>&quot;blockdev-snapshot-internal-sync&quot;</tt>: since 1.7</p>
<dt>&#8211;</p>
<dd><tt>&quot;blockdev-snapshot-sync&quot;</tt>: since 1.1</p>
<dt>&#8211;</p>
<dd><tt>&quot;drive-backup&quot;</tt>: since 1.6</dl>
<p> <code>Members:</code></p>
<dl>
<dt>&quot;type&quot;</p>
<dd>One of &#8220;abort&#8221;, &#8220;block-dirty-bitmap-add&#8221;, &#8220;block-dirty-bitmap-remove&#8221;, &#8220;block-dirty-bitmap-clear&#8221;, &#8220;block-dirty-bitmap-enable&#8221;, &#8220;block-dirty-bitmap-disable&#8221;, &#8220;block-dirty-bitmap-merge&#8221;, &#8220;blockdev-backup&#8221;, &#8220;blockdev-snapshot&#8221;, &#8220;blockdev-snapshot-internal-sync&#8221;, &#8220;blockdev-snapshot-sync&#8221;, &#8220;drive-backup&#8221;</p>
<dt>&quot;data: Abort&quot; when &quot;type&quot; is &quot;abort&quot;</p>
<dd>
<dt>&quot;data: BlockDirtyBitmapAdd&quot; when &quot;type&quot; is &quot;block-dirty-bitmap-add&quot;</p>
<dd>
<dt>&quot;data: BlockDirtyBitmap&quot; when &quot;type&quot; is &quot;block-dirty-bitmap-remove&quot;</p>
<dd>
<dt>&quot;data: BlockDirtyBitmap&quot; when &quot;type&quot; is &quot;block-dirty-bitmap-clear&quot;</p>
<dd>
<dt>&quot;data: BlockDirtyBitmap&quot; when &quot;type&quot; is &quot;block-dirty-bitmap-enable&quot;</p>
<dd>
<dt>&quot;data: BlockDirtyBitmap&quot; when &quot;type&quot; is &quot;block-dirty-bitmap-disable&quot;</p>
<dd>
<dt>&quot;data: BlockDirtyBitmapMerge&quot; when &quot;type&quot; is &quot;block-dirty-bitmap-merge&quot;</p>
<dd>
<dt>&quot;data: BlockdevBackup&quot; when &quot;type&quot; is &quot;blockdev-backup&quot;</p>
<dd>
<dt>&quot;data: BlockdevSnapshot&quot; when &quot;type&quot; is &quot;blockdev-snapshot&quot;</p>
<dd>
<dt>&quot;data: BlockdevSnapshotInternal&quot; when &quot;type&quot; is &quot;blockdev-snapshot-internal-sync&quot;</p>
<dd>
<dt>&quot;data: BlockdevSnapshotSync&quot; when &quot;type&quot; is &quot;blockdev-snapshot-sync&quot;</p>
<dd>
<dt>&quot;data: DriveBackup&quot; when &quot;type&quot; is &quot;drive-backup&quot;</p>
<dd></dl>
<p> <code>Since:</code> 1.1 <code>TransactionProperties</code> (Object) Optional arguments to modify the behavior of a Transaction. <code>Members:</code></p>
<dl>
<dt>&quot;completion-mode: ActionCompletionMode&quot; (optional)</p>
<dd>Controls how jobs launched asynchronously by Actions will complete or fail as a group. See <tt>&quot;ActionCompletionMode&quot;</tt> for details.</dl>
<p> <code>Since:</code> 2.5 <code>transaction</code> (Command) Executes a number of transactionable <font SIZE="-1">QMP</font> commands atomically. If any operation fails, then the entire set of actions will be abandoned and the appropriate error returned. For external snapshots, the dictionary contains the device, the file to use for the new snapshot, and the format. The default format, if not specified, is qcow2. Each new snapshot defaults to being created by <font SIZE="-1">QEMU</font> (wiping any contents if the file already exists), but it is also possible to reuse an externally-created file. In the latter case, you should ensure that the new image file has the same contents as the current one; <font SIZE="-1">QEMU</font> cannot perform any meaningful check. Typically this is achieved by using the current image file as the backing file for the new image. On failure, the original disks pre-snapshot attempt will be used. For internal snapshots, the dictionary contains the device and the snapshot&#8217;s name. If an internal snapshot matching name already exists, the request will be rejected. Only some image formats support it, for example, qcow2, rbd, and sheepdog. On failure, qemu will try delete the newly created internal snapshot in the transaction. When an I/O error occurs during deletion, the user needs to fix it later with qemu-img or other command. <code>Arguments:</code></p>
<dl>
<dt>&quot;actions: array of TransactionAction&quot;</p>
<dd>List of <tt>&quot;TransactionAction&quot;</tt>; information needed for the respective operations.</p>
<dt>&quot;properties: TransactionProperties&quot; (optional)</p>
<dd>structure of additional options to control the execution of the transaction. See <tt>&quot;TransactionProperties&quot;</tt> for additional detail.</dl>
<p> <code>Returns:</code> nothing on success Errors depend on the operations of the transaction <code>Note:</code> The transaction aborts on the first failure. Therefore, there will be information on only one failed operation returned in an error condition, and subsequent actions will not have been attempted. <code>Since:</code> 1.1 <code>Example:</code> </p>
<pre> -&gt; { &quot;execute&quot;: &quot;transaction&quot;,
 &quot;arguments&quot;: { &quot;actions&quot;: [
 { &quot;type&quot;: &quot;blockdev-snapshot-sync&quot;, &quot;data&quot; : { &quot;device&quot;: &quot;ide-hd0&quot;,
 &quot;snapshot-file&quot;: &quot;/some/place/my-image&quot;,
 &quot;format&quot;: &quot;qcow2&quot; } },
 { &quot;type&quot;: &quot;blockdev-snapshot-sync&quot;, &quot;data&quot; : { &quot;node-name&quot;: &quot;myfile&quot;,
 &quot;snapshot-file&quot;: &quot;/some/place/my-image2&quot;,
 &quot;snapshot-node-name&quot;: &quot;node3432&quot;,
 &quot;mode&quot;: &quot;existing&quot;,
 &quot;format&quot;: &quot;qcow2&quot; } },
 { &quot;type&quot;: &quot;blockdev-snapshot-sync&quot;, &quot;data&quot; : { &quot;device&quot;: &quot;ide-hd1&quot;,
 &quot;snapshot-file&quot;: &quot;/some/place/my-image2&quot;,
 &quot;mode&quot;: &quot;existing&quot;,
 &quot;format&quot;: &quot;qcow2&quot; } },
 { &quot;type&quot;: &quot;blockdev-snapshot-internal-sync&quot;, &quot;data&quot; : {
 &quot;device&quot;: &quot;ide-hd2&quot;,
 &quot;name&quot;: &quot;snapshot0&quot; } } ] } }
 &lt;- { &quot;return&quot;: {} }</pre>
<h3>Tracing</h3>
<p><code>TraceEventState</code> (Enum) State of a tracing event. <code>Values:</code></p>
<dl>
<dt>&quot;unavailable&quot;</p>
<dd>The event is statically disabled.</p>
<dt>&quot;disabled&quot;</p>
<dd>The event is dynamically disabled.</p>
<dt>&quot;enabled&quot;</p>
<dd>The event is dynamically enabled.</dl>
<p> <code>Since:</code> 2.2 <code>TraceEventInfo</code> (Object) Information of a tracing event. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>Event name.</p>
<dt>&quot;state: TraceEventState&quot;</p>
<dd>Tracing state.</p>
<dt>&quot;vcpu: boolean&quot;</p>
<dd>Whether this is a per-vCPU event (since 2.7).</dl>
<p> An event is per-vCPU if it has the &#8220;vcpu&#8221; property in the &#8220;trace-events&#8221; files. <code>Since:</code> 2.2 <code>trace-event-get-state</code> (Command) Query the state of events. <code>Arguments:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>Event name pattern (case-sensitive glob).</p>
<dt>&quot;vcpu: int&quot; (optional)</p>
<dd>The vCPU to query (any by default; since 2.7).</dl>
<p> <code>Returns:</code> a list of <tt>&quot;TraceEventInfo&quot;</tt> for the matching events An event is returned if:</p>
<dl>
<dt>&#8211;</p>
<dd>its name matches the <tt>&quot;name&quot;</tt> pattern, and</p>
<dt>&#8211;</p>
<dd>if <tt>&quot;vcpu&quot;</tt> is given, the event has the &#8220;vcpu&#8221; property.</dl>
<p> Therefore, if <tt>&quot;vcpu&quot;</tt> is given, the operation will only match per-vCPU events, returning their state on the specified vCPU. Special case: if <tt>&quot;name&quot;</tt> is an exact match, <tt>&quot;vcpu&quot;</tt> is given and the event does not have the &#8220;vcpu&#8221; property, an error is returned. <code>Since:</code> 2.2 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;trace-event-get-state&quot;,<br />
   &quot;arguments&quot; : {&quot;name&quot; : &quot;qemu_memalign&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [ {&quot;name&quot; : &quot;qemu_memalign&quot;, &quot;state&quot; : &quot;disabled&quot;} ]<br />
} <code>trace-event-set-state</code> (Command) Set the dynamic tracing state of events. <code>Arguments:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>Event name pattern (case-sensitive glob).</p>
<dt>&quot;enable: boolean&quot;</p>
<dd>Whether to enable tracing.</p>
<dt>&quot;ignore-unavailable: boolean&quot; (optional)</p>
<dd>Do not match unavailable events with <tt>&quot;name&quot;</tt>.</p>
<dt>&quot;vcpu: int&quot; (optional)</p>
<dd>The vCPU to act upon (all by default; since 2.7).</dl>
<p> An event&#8217;s state is modified if:</p>
<dl>
<dt>&#8211;</p>
<dd>its name matches the <tt>&quot;name&quot;</tt> pattern, and</p>
<dt>&#8211;</p>
<dd>if <tt>&quot;vcpu&quot;</tt> is given, the event has the &#8220;vcpu&#8221; property.</dl>
<p> Therefore, if <tt>&quot;vcpu&quot;</tt> is given, the operation will only match per-vCPU events, setting their state on the specified vCPU. Special case: if <tt>&quot;name&quot;</tt> is an exact match, <tt>&quot;vcpu&quot;</tt> is given and the event does not have the &#8220;vcpu&#8221; property, an error is returned. <code>Since:</code> 2.2 <code>Example:</code> </p>
<pre> -&gt; { &quot;execute&quot;: &quot;trace-event-set-state&quot;,
 &quot;arguments&quot;: { &quot;name&quot;: &quot;qemu_memalign&quot;, &quot;enable&quot;: &quot;true&quot; } }
 &lt;- { &quot;return&quot;: {} }</pre>
<h3><font SIZE="-1">QMP</font> introspection</h3>
<p><code>query-qmp-schema</code> (Command) Command query-qmp-schema exposes the <font SIZE="-1">QMP</font> wire <font SIZE="-1">ABI</font> as an array of SchemaInfo. This lets <font SIZE="-1">QMP</font> clients figure out what commands and events are available in this <font SIZE="-1">QEMU,</font> and their parameters and results. However, the SchemaInfo can&#8217;t reflect all the rules and restrictions that apply to <font SIZE="-1">QMP.</font> It&#8217;s interface introspection (figuring out what&#8217;s there), not interface specification. The specification is in the <font SIZE="-1">QAPI</font> schema. Furthermore, while we strive to keep the <font SIZE="-1">QMP</font> wire format backwards-compatible across qemu versions, the introspection output is not guaranteed to have the same stability. For example, one version of qemu may list an object member as an optional non-variant, while another lists the same member only through the object&#8217;s variants; or the type of a member may change from a generic string into a specific enum or from one specific type into an alternate that includes the original type alongside something else. <code>Returns:</code> array of <tt>&quot;SchemaInfo&quot;</tt>, where each element describes an entity in the <font SIZE="-1">ABI:</font> command, event, type, &#8230; The order of the various SchemaInfo is unspecified; however, all names are guaranteed to be unique (no name will be duplicated with different meta-types). <code>Note:</code> the <font SIZE="-1">QAPI</font> schema is also used to help define <code>internal</code> interfaces, by defining <font SIZE="-1">QAPI</font> types. These are not part of the <font SIZE="-1">QMP</font> wire <font SIZE="-1">ABI,</font> and therefore not returned by this command. <code>Since:</code> 2.5 <code>SchemaMetaType</code> (Enum) This is a <tt>&quot;SchemaInfo&quot;</tt>&#8216;s meta type, i.e. the kind of entity it describes. <code>Values:</code></p>
<dl>
<dt>&quot;builtin&quot;</p>
<dd>a predefined type such as &#8216;int&#8217; or &#8216;bool&#8217;.</p>
<dt>&quot;enum&quot;</p>
<dd>an enumeration type</p>
<dt>&quot;array&quot;</p>
<dd>an array type</p>
<dt>&quot;object&quot;</p>
<dd>an object type (struct or union)</p>
<dt>&quot;alternate&quot;</p>
<dd>an alternate type</p>
<dt>&quot;command&quot;</p>
<dd>a <font SIZE="-1">QMP</font> command</p>
<dt>&quot;event&quot;</p>
<dd>a <font SIZE="-1">QMP</font> event</dl>
<p> <code>Since:</code> 2.5 <code>SchemaInfo</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>the entity&#8217;s name, inherited from <tt>&quot;base&quot;</tt>. The SchemaInfo is always referenced by this name. Commands and events have the name defined in the <font SIZE="-1">QAPI</font> schema. Unlike command and event names, type names are not part of the wire <font SIZE="-1">ABI.</font> Consequently, type names are meaningless strings here, although they are still guaranteed unique regardless of <tt>&quot;meta-type&quot;</tt>.</p>
<dt>&quot;meta-type: SchemaMetaType&quot;</p>
<dd>the entity&#8217;s meta type, inherited from <tt>&quot;base&quot;</tt>.</p>
<dt>The members of &quot;SchemaInfoBuiltin&quot; when &quot;meta-type&quot; is &quot;builtin&quot;</p>
<dd>
<dt>The members of &quot;SchemaInfoEnum&quot; when &quot;meta-type&quot; is &quot;enum&quot;</p>
<dd>
<dt>The members of &quot;SchemaInfoArray&quot; when &quot;meta-type&quot; is &quot;array&quot;</p>
<dd>
<dt>The members of &quot;SchemaInfoObject&quot; when &quot;meta-type&quot; is &quot;object&quot;</p>
<dd>
<dt>The members of &quot;SchemaInfoAlternate&quot; when &quot;meta-type&quot; is &quot;alternate&quot;</p>
<dd>
<dt>The members of &quot;SchemaInfoCommand&quot; when &quot;meta-type&quot; is &quot;command&quot;</p>
<dd>
<dt>The members of &quot;SchemaInfoEvent&quot; when &quot;meta-type&quot; is &quot;event&quot;</p>
<dd></dl>
<p> Additional members depend on the value of <tt>&quot;meta-type&quot;</tt>. <code>Since:</code> 2.5 <code>SchemaInfoBuiltin</code> (Object) Additional SchemaInfo members for meta-type &#8216;builtin&#8217;. <code>Members:</code></p>
<dl>
<dt>&quot;json-type: JSONType&quot;</p>
<dd>the <font SIZE="-1">JSON</font> type used for this type on the wire.</dl>
<p> <code>Since:</code> 2.5 <code>JSONType</code> (Enum) The four primitive and two structured types according to <font SIZE="-1">RFC 8259</font> section 1, plus &#8216;int&#8217; (split off &#8216;number&#8217;), plus the obvious top type &#8216;value&#8217;. <code>Values:</code></p>
<dl>
<dt>&quot;string&quot;</p>
<dd>Not documented</p>
<dt>&quot;number&quot;</p>
<dd>Not documented</p>
<dt>&quot;int&quot;</p>
<dd>Not documented</p>
<dt>&quot;boolean&quot;</p>
<dd>Not documented</p>
<dt>&quot;null&quot;</p>
<dd>Not documented</p>
<dt>&quot;object&quot;</p>
<dd>Not documented</p>
<dt>&quot;array&quot;</p>
<dd>Not documented</p>
<dt>&quot;value&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.5 <code>SchemaInfoEnum</code> (Object) Additional SchemaInfo members for meta-type &#8216;enum&#8217;. <code>Members:</code></p>
<dl>
<dt>&quot;values: array of string&quot;</p>
<dd>the enumeration type&#8217;s values, in no particular order.</dl>
<p> Values of this type are <font SIZE="-1">JSON</font> string on the wire. <code>Since:</code> 2.5 <code>SchemaInfoArray</code> (Object) Additional SchemaInfo members for meta-type &#8216;array&#8217;. <code>Members:</code></p>
<dl>
<dt>&quot;element-type: string&quot;</p>
<dd>the array type&#8217;s element type.</dl>
<p> Values of this type are <font SIZE="-1">JSON</font> array on the wire. <code>Since:</code> 2.5 <code>SchemaInfoObject</code> (Object) Additional SchemaInfo members for meta-type &#8216;object&#8217;. <code>Members:</code></p>
<dl>
<dt>&quot;members: array of SchemaInfoObjectMember&quot;</p>
<dd>the object type&#8217;s (non-variant) members, in no particular order.</p>
<dt>&quot;tag: string&quot; (optional)</p>
<dd>the name of the member serving as type tag. An element of <tt>&quot;members&quot;</tt> with this name must exist.</p>
<dt>&quot;variants: array of SchemaInfoObjectVariant&quot; (optional)</p>
<dd>variant members, i.e. additional members that depend on the type tag&#8217;s value. Present exactly when <tt>&quot;tag&quot;</tt> is present. The variants are in no particular order, and may even differ from the order of the values of the enum type of the <tt>&quot;tag&quot;</tt>.</p>
<dt>&quot;features: array of string&quot; (optional)</p>
<dd>names of features associated with the type, in no particular order. (since: 4.1)</dl>
<p> Values of this type are <font SIZE="-1">JSON</font> object on the wire. <code>Since:</code> 2.5 <code>SchemaInfoObjectMember</code> (Object) An object member. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>the member&#8217;s name, as defined in the <font SIZE="-1">QAPI</font> schema.</p>
<dt>&quot;type: string&quot;</p>
<dd>the name of the member&#8217;s type.</p>
<dt>&quot;default: value&quot; (optional)</p>
<dd>default when used as command parameter. If absent, the parameter is mandatory. If present, the value must be null. The parameter is optional, and behavior when it&#8217;s missing is not specified here. Future extension: if present and non-null, the parameter is optional, and defaults to this value.</dl>
<p> <code>Since:</code> 2.5 <code>SchemaInfoObjectVariant</code> (Object) The variant members for a value of the type tag. <code>Members:</code></p>
<dl>
<dt>&quot;case: string&quot;</p>
<dd>a value of the type tag.</p>
<dt>&quot;type: string&quot;</p>
<dd>the name of the object type that provides the variant members when the type tag has value <tt>&quot;case&quot;</tt>.</dl>
<p> <code>Since:</code> 2.5 <code>SchemaInfoAlternate</code> (Object) Additional SchemaInfo members for meta-type &#8216;alternate&#8217;. <code>Members:</code></p>
<dl>
<dt>&quot;members: array of SchemaInfoAlternateMember&quot;</p>
<dd>the alternate type&#8217;s members, in no particular order. The members&#8217; wire encoding is distinct, see docs/devel/qapi-code-gen.txt section Alternate types.</dl>
<p> On the wire, this can be any of the members. <code>Since:</code> 2.5 <code>SchemaInfoAlternateMember</code> (Object) An alternate member. <code>Members:</code></p>
<dl>
<dt>&quot;type: string&quot;</p>
<dd>the name of the member&#8217;s type.</dl>
<p> <code>Since:</code> 2.5 <code>SchemaInfoCommand</code> (Object) Additional SchemaInfo members for meta-type &#8216;command&#8217;. <code>Members:</code></p>
<dl>
<dt>&quot;arg-type: string&quot;</p>
<dd>the name of the object type that provides the command&#8217;s parameters.</p>
<dt>&quot;ret-type: string&quot;</p>
<dd>the name of the command&#8217;s result type.</p>
<dt>&quot;allow-oob: boolean&quot; (optional)</p>
<dd>whether the command allows out-of-band execution, defaults to false (Since: 2.12)</p>
<dt>&quot;features: array of string&quot; (optional)</p>
<dd>names of features associated with the command, in no particular order. (since 4.2)</dl>
<p> <font SIZE="-1"><code>TODO:</code></font> <tt>&quot;success-response&quot;</tt> (currently irrelevant, because it&#8217;s <font SIZE="-1">QGA,</font> not <font SIZE="-1">QMP</font>) <code>Since:</code> 2.5 <code>SchemaInfoEvent</code> (Object) Additional SchemaInfo members for meta-type &#8216;event&#8217;. <code>Members:</code></p>
<dl>
<dt>&quot;arg-type: string&quot;</p>
<dd>the name of the object type that provides the event&#8217;s parameters.</dl>
<p> <code>Since:</code> 2.5</p>
<h3><font SIZE="-1">QEMU</font> Object Model (<font SIZE="-1">QOM</font>)</h3>
<p><code>ObjectPropertyInfo</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>the name of the property</p>
<dt>&quot;type: string&quot;</p>
<dd>the type of the property. This will typically come in one of four forms: 1) A primitive type such as &#8216;u8&#8217;, &#8216;u16&#8217;, &#8216;bool&#8217;, &#8216;str&#8217;, or &#8216;double&#8217;. These types are mapped to the appropriate <font SIZE="-1">JSON</font> type. 2) A child type in the form &#8216;child&lt;subtype&gt;&#8217; where subtype is a qdev device type name. Child properties create the composition tree. 3) A link type in the form &#8216;link&lt;subtype&gt;&#8217; where subtype is a qdev device type name. Link properties form the device model graph.</p>
<dt>&quot;description: string&quot; (optional)</p>
<dd>if specified, the description of the property.</dl>
<p> <code>Since:</code> 1.2 <code>qom-list</code> (Command) This command will list any properties of a object given a path in the object model. <code>Arguments:</code></p>
<dl>
<dt>&quot;path: string&quot;</p>
<dd>the path within the object model. See <tt>&quot;qom-get&quot;</tt> for a description of this parameter.</dl>
<p> <code>Returns:</code> a list of <tt>&quot;ObjectPropertyInfo&quot;</tt> that describe the properties of the object. <code>Since:</code> 1.2 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;qom-list&quot;,<br />
   &quot;arguments&quot; : {&quot;path&quot; : &quot;/chardevs&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [ {&quot;name&quot; : &quot;type&quot;, &quot;type&quot; : &quot;string&quot;},<br />
                 {&quot;name&quot; : &quot;parallel0&quot;, &quot;type&quot; : &quot;child&lt;chardev-vc&gt;&quot;},<br />
                 {&quot;name&quot; : &quot;serial0&quot;, &quot;type&quot; : &quot;child&lt;chardev-vc&gt;&quot;},<br />
                 {&quot;name&quot; : &quot;mon0&quot;, &quot;type&quot; : &quot;child&lt;chardev-stdio&gt;&quot;} ]<br />
} <code>qom-get</code> (Command) This command will get a property from a object model path and return the value. <code>Arguments:</code></p>
<dl>
<dt>&quot;path: string&quot;</p>
<dd>The path within the object model. There are two forms of supported paths&#8212;absolute and partial paths. Absolute paths are derived from the root object and can follow child&lt;&gt; or link&lt;&gt; properties. Since they can follow link&lt;&gt; properties, they can be arbitrarily long. Absolute paths look like absolute filenames and are prefixed with a leading slash. Partial paths look like relative filenames. They do not begin with a prefix. The matching rules for partial paths are subtle but designed to make specifying objects easy. At each level of the composition tree, the partial path is matched as an absolute path. The first match is not returned. At least two matches are searched for. A successful result is only returned if only one match is found. If more than one match is found, a flag is return to indicate that the match was ambiguous.</p>
<dt>&quot;property: string&quot;</p>
<dd>The property name to read</dl>
<p> <code>Returns:</code> The property value. The type depends on the property type. child&lt;&gt; and link&lt;&gt; properties are returned as #str pathnames. All integer property types (u8, u16, etc) are returned as #int. <code>Since:</code> 1.2 <code>Example:</code> 1. Use absolute path</p>
<p>        -&gt;{&quot;execute&quot; : &quot;qom-get&quot;,<br />
           &quot;arguments&quot; : {&quot;path&quot; : &quot;/machine/unattached/device[0]&quot;,<br />
                          &quot;property&quot; : &quot;hotplugged&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : false<br />
}</p>
<p>2. Use partial path</p>
<p>        -&gt;{&quot;execute&quot; : &quot;qom-get&quot;,<br />
           &quot;arguments&quot; : {&quot;path&quot; : &quot;unattached/sysbus&quot;,<br />
                          &quot;property&quot; : &quot;type&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : &quot;System&quot;<br />
} <code>qom-set</code> (Command) This command will set a property from a object model path. <code>Arguments:</code></p>
<dl>
<dt>&quot;path: string&quot;</p>
<dd>see <tt>&quot;qom-get&quot;</tt> for a description of this parameter</p>
<dt>&quot;property: string&quot;</p>
<dd>the property name to set</p>
<dt>&quot;value: value&quot;</p>
<dd>a value who&#8217;s type is appropriate for the property type. See <tt>&quot;qom-get&quot;</tt> for a description of type mapping.</dl>
<p> <code>Since:</code> 1.2 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;qom-set&quot;,<br />
   &quot;arguments&quot; : {&quot;path&quot; : &quot;/machine&quot;,<br />
                  &quot;property&quot; : &quot;graphics&quot;,<br />
                  &quot;value&quot; : false}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>ObjectTypeInfo</code> (Object) This structure describes a search result from <tt>&quot;qom-list-types&quot;</tt> <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>the type name found in the search</p>
<dt>&quot;abstract: boolean&quot; (optional)</p>
<dd>the type is abstract and can&#8217;t be directly instantiated. Omitted if false. (since 2.10)</p>
<dt>&quot;parent: string&quot; (optional)</p>
<dd>Name of parent type, if any (since 2.10)</dl>
<p> <code>Since:</code> 1.1 <code>qom-list-types</code> (Command) This command will return a list of types given search parameters <code>Arguments:</code></p>
<dl>
<dt>&quot;implements: string&quot; (optional)</p>
<dd>if specified, only return types that implement this type name</p>
<dt>&quot;abstract: boolean&quot; (optional)</p>
<dd>if true, include abstract types in the results</dl>
<p> <code>Returns:</code> a list of <tt>&quot;ObjectTypeInfo&quot;</tt> or an empty list if no results are found <code>Since:</code> 1.1 <code>qom-list-properties</code> (Command) List properties associated with a <font SIZE="-1">QOM</font> object. <code>Arguments:</code></p>
<dl>
<dt>&quot;typename: string&quot;</p>
<dd>the type name of an object</dl>
<p> <code>Note:</code> objects can create properties at runtime, for example to describe links between different devices and/or objects. These properties are not included in the output of this command. <code>Returns:</code> a list of ObjectPropertyInfo describing object properties <code>Since:</code> 2.12 <code>object-add</code> (Command) Create a <font SIZE="-1">QOM</font> object. <code>Arguments:</code></p>
<dl>
<dt>&quot;qom-type: string&quot;</p>
<dd>the class name for the object to be created</p>
<dt>&quot;id: string&quot;</p>
<dd>the name of the new object</p>
<dt>&quot;props: value&quot; (optional)</p>
<dd>a dictionary of properties to be passed to the backend</dl>
<p> <code>Returns:</code> Nothing on success Error if <tt>&quot;qom-type&quot;</tt> is not a valid class name <code>Since:</code> 2.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;object-add&quot;,<br />
   &quot;arguments&quot; : {&quot;qom-type&quot; : &quot;rng-random&quot;, &quot;id&quot; : &quot;rng1&quot;, &quot;props&quot; : {&quot;filename&quot; : &quot;/dev/hwrng&quot;}}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>object-del</code> (Command) Remove a <font SIZE="-1">QOM</font> object. <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>the name of the <font SIZE="-1">QOM</font> object to remove</dl>
<p> <code>Returns:</code> Nothing on success Error if <tt>&quot;id&quot;</tt> is not a valid id for a <font SIZE="-1">QOM</font> object <code>Since:</code> 2.0 <code>Example:</code> </p>
<pre> -&gt; { &quot;execute&quot;: &quot;object-del&quot;, &quot;arguments&quot;: { &quot;id&quot;: &quot;rng1&quot; } }
 &lt;- { &quot;return&quot;: {} }</pre>
<h3>Device infrastructure (qdev)</h3>
<p><code>device-list-properties</code> (Command) List properties associated with a device. <code>Arguments:</code></p>
<dl>
<dt>&quot;typename: string&quot;</p>
<dd>the type name of a device</dl>
<p> <code>Returns:</code> a list of ObjectPropertyInfo describing a devices properties <code>Note:</code> objects can create properties at runtime, for example to describe links between different devices and/or objects. These properties are not included in the output of this command. <code>Since:</code> 1.2 <code>device_add</code> (Command) <code>Arguments:</code></p>
<dl>
<dt>&quot;driver: string&quot;</p>
<dd>the name of the new device&#8217;s driver</p>
<dt>&quot;bus: string&quot; (optional)</p>
<dd>the device&#8217;s parent bus (device tree path)</p>
<dt>&quot;id: string&quot; (optional)</p>
<dd>the device&#8217;s <font SIZE="-1">ID,</font> must be unique</dl>
<p> Additional arguments depend on the type. Add a device. <code>Notes:</code></p>
<dl>
<dt>1.</p>
<dd>For detailed information about this command, please refer to the &#8216;docs/qdev-device-use.txt&#8217; file.</p>
<dt>2.</p>
<dd>It&#8217;s possible to list device properties by running <font SIZE="-1">QEMU</font> with the &#8220;-device <font SIZE="-1">DEVICE</font>,help&#8221; command-line argument, where <font SIZE="-1">DEVICE</font> is the device&#8217;s name</dl>
<p> <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;device_add&quot;,<br />
   &quot;arguments&quot; : {&quot;driver&quot; : &quot;e1000&quot;, &quot;id&quot; : &quot;net1&quot;, &quot;bus&quot; : &quot;pci.0&quot;, &quot;mac&quot; : &quot;52:54:00:12:34:56&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <font SIZE="-1"><code>TODO:</code></font> This command effectively bypasses <font SIZE="-1">QAPI</font> completely due to its &#8220;additional arguments&#8221; business. It shouldn&#8217;t have been added to the schema in this form. It should be qapified properly, or replaced by a properly qapified command. <code>Since:</code> 0.13 <code>device_del</code> (Command) Remove a device from a guest <code>Arguments:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>the device&#8217;s <font SIZE="-1">ID</font> or <font SIZE="-1">QOM</font> path</dl>
<p> <code>Returns:</code> Nothing on success If <tt>&quot;id&quot;</tt> is not a valid device, DeviceNotFound <code>Notes:</code> When this command completes, the device may not be removed from the guest. Hot removal is an operation that requires guest cooperation. This command merely requests that the guest begin the hot removal process. Completion of the device removal process is signaled with a <font SIZE="-1">DEVICE_DELETED</font> event. Guest reset will automatically complete removal for all devices. <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;device_del&quot;,<br />
   &quot;arguments&quot; : {&quot;id&quot; : &quot;net1&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
    }</p>
<p>        -&gt; {&quot;execute&quot; : &quot;device_del&quot;,<br />
            &quot;arguments&quot; : {&quot;id&quot; : &quot;/machine/peripheral-anon/device[0]&quot;}} &lt; &#8211;<br />
    {<br />
        &quot;return&quot;:<br />
        {<br />
        }<br />
    } <font SIZE="-1"><code>DEVICE_DELETED</code></font> (Event) Emitted whenever the device removal completion is acknowledged by the guest. At this point, it&#8217;s safe to reuse the specified device <font SIZE="-1">ID.</font> Device removal can be initiated by the guest or by <font SIZE="-1">HMP/QMP</font> commands. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>device name</p>
<dt>&quot;path: string&quot;</p>
<dd>device path</dl>
<p> <code>Since:</code> 1.5 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;DEVICE_DELETED&quot;,
 &quot;data&quot;: { &quot;device&quot;: &quot;virtio-net-pci-0&quot;,
 &quot;path&quot;: &quot;/machine/peripheral/virtio-net-pci-0&quot; },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1265044230, &quot;microseconds&quot;: 450486 } }</pre>
<h3>Machines</h3>
<p><code>SysEmuTarget</code> (Enum) The comprehensive enumeration of <font SIZE="-1">QEMU</font> system emulation (&#8220;softmmu&#8221;) targets. Run &#8220;./configure &#8211;help&#8221; in the project root directory, and look for the *-softmmu targets near the &#8220;&#8211;target-list&#8221; option. The individual target constants are not documented here, for the time being. <code>Values:</code></p>
<dl>
<dt>&quot;aarch64&quot;</p>
<dd>Not documented</p>
<dt>&quot;alpha&quot;</p>
<dd>Not documented</p>
<dt>&quot;arm&quot;</p>
<dd>Not documented</p>
<dt>&quot;cris&quot;</p>
<dd>Not documented</p>
<dt>&quot;hppa&quot;</p>
<dd>Not documented</p>
<dt>&quot;i386&quot;</p>
<dd>Not documented</p>
<dt>&quot;lm32&quot;</p>
<dd>Not documented</p>
<dt>&quot;m68k&quot;</p>
<dd>Not documented</p>
<dt>&quot;microblaze&quot;</p>
<dd>Not documented</p>
<dt>&quot;microblazeel&quot;</p>
<dd>Not documented</p>
<dt>&quot;mips&quot;</p>
<dd>Not documented</p>
<dt>&quot;mips64&quot;</p>
<dd>Not documented</p>
<dt>&quot;mips64el&quot;</p>
<dd>Not documented</p>
<dt>&quot;mipsel&quot;</p>
<dd>Not documented</p>
<dt>&quot;moxie&quot;</p>
<dd>Not documented</p>
<dt>&quot;nios2&quot;</p>
<dd>Not documented</p>
<dt>&quot;or1k&quot;</p>
<dd>Not documented</p>
<dt>&quot;ppc&quot;</p>
<dd>Not documented</p>
<dt>&quot;ppc64&quot;</p>
<dd>Not documented</p>
<dt>&quot;riscv32&quot;</p>
<dd>Not documented</p>
<dt>&quot;riscv64&quot;</p>
<dd>Not documented</p>
<dt>&quot;s390x&quot;</p>
<dd>Not documented</p>
<dt>&quot;sh4&quot;</p>
<dd>Not documented</p>
<dt>&quot;sh4eb&quot;</p>
<dd>Not documented</p>
<dt>&quot;sparc&quot;</p>
<dd>Not documented</p>
<dt>&quot;sparc64&quot;</p>
<dd>Not documented</p>
<dt>&quot;tricore&quot;</p>
<dd>Not documented</p>
<dt>&quot;unicore32&quot;</p>
<dd>Not documented</p>
<dt>&quot;x86_64&quot;</p>
<dd>Not documented</p>
<dt>&quot;xtensa&quot;</p>
<dd>Not documented</p>
<dt>&quot;xtensaeb&quot;</p>
<dd>Not documented</dl>
<p> <code>Notes:</code> The resulting <font SIZE="-1">QMP</font> strings can be appended to the &#8220;qemu-system-&#8221; prefix to produce the corresponding <font SIZE="-1">QEMU</font> executable name. This is true even for &#8220;qemu-system-x86_64&#8221;. ppcemb: dropped in 3.1 <code>Since:</code> 3.0 <code>CpuInfoArch</code> (Enum) An enumeration of cpu types that enable additional information during <tt>&quot;query-cpus&quot;</tt> and <tt>&quot;query-cpus-fast&quot;</tt>. <code>Values:</code></p>
<dl>
<dt>&quot;s390&quot;</p>
<dd>since 2.12</p>
<dt>&quot;riscv&quot;</p>
<dd>since 2.12</p>
<dt>&quot;x86&quot;</p>
<dd>Not documented</p>
<dt>&quot;sparc&quot;</p>
<dd>Not documented</p>
<dt>&quot;ppc&quot;</p>
<dd>Not documented</p>
<dt>&quot;mips&quot;</p>
<dd>Not documented</p>
<dt>&quot;tricore&quot;</p>
<dd>Not documented</p>
<dt>&quot;other&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.6 <code>CpuInfo</code> (Object) Information about a virtual <font SIZE="-1">CPU</font> <code>Members:</code></p>
<dl>
<dt>&quot;CPU: int&quot;</p>
<dd>the index of the virtual <font SIZE="-1">CPU</font></p>
<dt>&quot;current: boolean&quot;</p>
<dd>this only exists for backwards compatibility and should be ignored</p>
<dt>&quot;halted: boolean&quot;</p>
<dd>true if the virtual <font SIZE="-1">CPU</font> is in the halt state. Halt usually refers to a processor specific low power mode.</p>
<dt>&quot;qom_path: string&quot;</p>
<dd>path to the <font SIZE="-1">CPU</font> object in the <font SIZE="-1">QOM</font> tree (since 2.4)</p>
<dt>&quot;thread_id: int&quot;</p>
<dd><font SIZE="-1">ID</font> of the underlying host thread</p>
<dt>&quot;props: CpuInstanceProperties&quot; (optional)</p>
<dd>properties describing to which node/socket/core/thread virtual <font SIZE="-1">CPU</font> belongs to, provided if supported by board (since 2.10)</p>
<dt>&quot;arch: CpuInfoArch&quot;</p>
<dd>architecture of the cpu, which determines which additional fields will be listed (since 2.6)</p>
<dt>The members of &quot;CpuInfoX86&quot; when &quot;arch&quot; is &quot;x86&quot;</p>
<dd>
<dt>The members of &quot;CpuInfoSPARC&quot; when &quot;arch&quot; is &quot;sparc&quot;</p>
<dd>
<dt>The members of &quot;CpuInfoPPC&quot; when &quot;arch&quot; is &quot;ppc&quot;</p>
<dd>
<dt>The members of &quot;CpuInfoMIPS&quot; when &quot;arch&quot; is &quot;mips&quot;</p>
<dd>
<dt>The members of &quot;CpuInfoTricore&quot; when &quot;arch&quot; is &quot;tricore&quot;</p>
<dd>
<dt>The members of &quot;CpuInfoS390&quot; when &quot;arch&quot; is &quot;s390&quot;</p>
<dd>
<dt>The members of &quot;CpuInfoRISCV&quot; when &quot;arch&quot; is &quot;riscv&quot;</p>
<dd></dl>
<p> <code>Since:</code> 0.14.0 <code>Notes:</code> <tt>&quot;halted&quot;</tt> is a transient state that changes frequently. By the time the data is sent to the client, the guest may no longer be halted. <code>CpuInfoX86</code> (Object) Additional information about a virtual i386 or x86_64 <font SIZE="-1">CPU</font> <code>Members:</code></p>
<dl>
<dt>&quot;pc: int&quot;</p>
<dd>the 64-bit instruction pointer</dl>
<p> <code>Since:</code> 2.6 <code>CpuInfoSPARC</code> (Object) Additional information about a virtual <font SIZE="-1">SPARC CPU</font> <code>Members:</code></p>
<dl>
<dt>&quot;pc: int&quot;</p>
<dd>the <font SIZE="-1">PC</font> component of the instruction pointer</p>
<dt>&quot;npc: int&quot;</p>
<dd>the <font SIZE="-1">NPC</font> component of the instruction pointer</dl>
<p> <code>Since:</code> 2.6 <code>CpuInfoPPC</code> (Object) Additional information about a virtual <font SIZE="-1">PPC CPU</font> <code>Members:</code></p>
<dl>
<dt>&quot;nip: int&quot;</p>
<dd>the instruction pointer</dl>
<p> <code>Since:</code> 2.6 <code>CpuInfoMIPS</code> (Object) Additional information about a virtual <font SIZE="-1">MIPS CPU</font> <code>Members:</code></p>
<dl>
<dt>&quot;PC: int&quot;</p>
<dd>the instruction pointer</dl>
<p> <code>Since:</code> 2.6 <code>CpuInfoTricore</code> (Object) Additional information about a virtual Tricore <font SIZE="-1">CPU</font> <code>Members:</code></p>
<dl>
<dt>&quot;PC: int&quot;</p>
<dd>the instruction pointer</dl>
<p> <code>Since:</code> 2.6 <code>CpuInfoRISCV</code> (Object) Additional information about a virtual <font SIZE="-1">RISCV CPU</font> <code>Members:</code></p>
<dl>
<dt>&quot;pc: int&quot;</p>
<dd>the instruction pointer</dl>
<p> Since 2.12 <code>CpuS390State</code> (Enum) An enumeration of cpu states that can be assumed by a virtual S390 <font SIZE="-1">CPU</font> <code>Values:</code></p>
<dl>
<dt>&quot;uninitialized&quot;</p>
<dd>Not documented</p>
<dt>&quot;stopped&quot;</p>
<dd>Not documented</p>
<dt>&quot;check-stop&quot;</p>
<dd>Not documented</p>
<dt>&quot;operating&quot;</p>
<dd>Not documented</p>
<dt>&quot;load&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.12 <code>CpuInfoS390</code> (Object) Additional information about a virtual S390 <font SIZE="-1">CPU</font> <code>Members:</code></p>
<dl>
<dt>&quot;cpu-state: CpuS390State&quot;</p>
<dd>the virtual <font SIZE="-1">CPU</font>&#8216;s state</dl>
<p> <code>Since:</code> 2.12 <code>query-cpus</code> (Command) Returns a list of information about each virtual <font SIZE="-1">CPU.</font> This command causes vCPU threads to exit to userspace, which causes a small interruption to guest <font SIZE="-1">CPU</font> execution. This will have a negative impact on realtime guests and other latency sensitive guest workloads. It is recommended to use <tt>&quot;query-cpus-fast&quot;</tt> instead of this command to avoid the vCPU interruption. <code>Returns:</code> a list of <tt>&quot;CpuInfo&quot;</tt> for each virtual <font SIZE="-1">CPU</font> <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-cpus&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;CPU&quot; : 0,<br />
            &quot;current&quot; : true,<br />
            &quot;halted&quot; : false,<br />
            &quot;qom_path&quot; : &quot;/machine/unattached/device[0]&quot;,<br />
            &quot;arch&quot; : &quot;x86&quot;,<br />
            &quot;pc&quot; : 3227107138,<br />
            &quot;thread_id&quot; : 3134<br />
        },<br />
        {<br />
            &quot;CPU&quot; : 1,<br />
            &quot;current&quot; : false,<br />
            &quot;halted&quot; : true,<br />
            &quot;qom_path&quot; : &quot;/machine/unattached/device[2]&quot;,<br />
            &quot;arch&quot; : &quot;x86&quot;,<br />
            &quot;pc&quot; : 7108165,<br />
            &quot;thread_id&quot; : 3135<br />
        }<br />
    ]<br />
} <code>Notes:</code> This interface is deprecated (since 2.12.0), and it is strongly recommended that you avoid using it. Use <tt>&quot;query-cpus-fast&quot;</tt> to obtain information about virtual CPUs. <code>CpuInfoFast</code> (Object) Information about a virtual <font SIZE="-1">CPU</font> <code>Members:</code></p>
<dl>
<dt>&quot;cpu-index: int&quot;</p>
<dd>index of the virtual <font SIZE="-1">CPU</font></p>
<dt>&quot;qom-path: string&quot;</p>
<dd>path to the <font SIZE="-1">CPU</font> object in the <font SIZE="-1">QOM</font> tree</p>
<dt>&quot;thread-id: int&quot;</p>
<dd><font SIZE="-1">ID</font> of the underlying host thread</p>
<dt>&quot;props: CpuInstanceProperties&quot; (optional)</p>
<dd>properties describing to which node/socket/core/thread virtual <font SIZE="-1">CPU</font> belongs to, provided if supported by board</p>
<dt>&quot;arch: CpuInfoArch&quot;</p>
<dd>base architecture of the cpu; deprecated since 3.0.0 in favor of <tt>&quot;target&quot;</tt></p>
<dt>&quot;target: SysEmuTarget&quot;</p>
<dd>the <font SIZE="-1">QEMU</font> system emulation target, which determines which additional fields will be listed (since 3.0)</p>
<dt>The members of &quot;CpuInfoS390&quot; when &quot;target&quot; is &quot;s390x&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.12 <code>query-cpus-fast</code> (Command) Returns information about all virtual CPUs. This command does not incur a performance penalty and should be used in production instead of query-cpus. <code>Returns:</code> list of <tt>&quot;CpuInfoFast&quot;</tt> <code>Since:</code> 2.12 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-cpus-fast&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;thread-id&quot; : 25627,<br />
            &quot;props&quot; : {<br />
                &quot;core-id&quot; : 0,<br />
                &quot;thread-id&quot; : 0,<br />
                &quot;socket-id&quot; : 0<br />
            },<br />
            &quot;qom-path&quot; : &quot;/machine/unattached/device[0]&quot;,<br />
            &quot;arch&quot; : &quot;x86&quot;,<br />
            &quot;target&quot; : &quot;x86_64&quot;,<br />
            &quot;cpu-index&quot; : 0<br />
        },<br />
        {<br />
            &quot;thread-id&quot; : 25628,<br />
            &quot;props&quot; : {<br />
                &quot;core-id&quot; : 0,<br />
                &quot;thread-id&quot; : 0,<br />
                &quot;socket-id&quot; : 1<br />
            },<br />
            &quot;qom-path&quot; : &quot;/machine/unattached/device[2]&quot;,<br />
            &quot;arch&quot; : &quot;x86&quot;,<br />
            &quot;target&quot; : &quot;x86_64&quot;,<br />
            &quot;cpu-index&quot; : 1<br />
        }<br />
    ]<br />
} <code>cpu-add</code> (Command) Adds <font SIZE="-1">CPU</font> with specified <font SIZE="-1">ID.</font> <code>Arguments:</code></p>
<dl>
<dt>&quot;id: int&quot;</p>
<dd><font SIZE="-1">ID</font> of <font SIZE="-1">CPU</font> to be created, valid values [0..max_cpus)</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 1.5 <code>Note:</code> This command is deprecated. The `device_add` command should be used instead. See the `query-hotpluggable-cpus` command for details. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;cpu-add&quot;, &quot;arguments&quot; : {&quot;id&quot; : 2}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>MachineInfo</code> (Object) Information describing a machine. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>the name of the machine</p>
<dt>&quot;alias: string&quot; (optional)</p>
<dd>an alias for the machine name</p>
<dt>&quot;is-default: boolean&quot; (optional)</p>
<dd>whether the machine is default</p>
<dt>&quot;cpu-max: int&quot;</p>
<dd>maximum number of CPUs supported by the machine type (since 1.5.0)</p>
<dt>&quot;hotpluggable-cpus: boolean&quot;</p>
<dd>cpu hotplug via -device is supported (since 2.7.0)</p>
<dt>&quot;numa-mem-supported: boolean&quot;</p>
<dd>true if &#8216;-numa node,mem&#8217; option is supported by the machine type and false otherwise (since 4.1)</p>
<dt>&quot;deprecated: boolean&quot;</p>
<dd>if true, the machine type is deprecated and may be removed in future versions of <font SIZE="-1">QEMU</font> according to the <font SIZE="-1">QEMU</font> deprecation policy (since 4.1.0)</p>
<dt>&quot;default-cpu-type: string&quot; (optional)</p>
<dd>default <font SIZE="-1">CPU</font> model typename if none is requested via the -cpu argument. (since 4.2)</dl>
<p> <code>Since:</code> 1.2.0 <code>query-machines</code> (Command) Return a list of supported machines <code>Returns:</code> a list of MachineInfo <code>Since:</code> 1.2.0 <code>CurrentMachineParams</code> (Object) Information describing the running machine parameters. <code>Members:</code></p>
<dl>
<dt>&quot;wakeup-suspend-support: boolean&quot;</p>
<dd>true if the machine supports wake up from suspend</dl>
<p> <code>Since:</code> 4.0 <code>query-current-machine</code> (Command) Return information on the current virtual machine. <code>Returns:</code> CurrentMachineParams <code>Since:</code> 4.0 <code>TargetInfo</code> (Object) Information describing the <font SIZE="-1">QEMU</font> target. <code>Members:</code></p>
<dl>
<dt>&quot;arch: SysEmuTarget&quot;</p>
<dd>the target architecture</dl>
<p> <code>Since:</code> 1.2.0 <code>query-target</code> (Command) Return information about the target for this <font SIZE="-1">QEMU</font> <code>Returns:</code> TargetInfo <code>Since:</code> 1.2.0 <code>NumaOptionsType</code> (Enum) <code>Values:</code></p>
<dl>
<dt>&quot;node&quot;</p>
<dd><font SIZE="-1">NUMA</font> nodes configuration</p>
<dt>&quot;dist&quot;</p>
<dd><font SIZE="-1">NUMA</font> distance configuration (since 2.10)</p>
<dt>&quot;cpu&quot;</p>
<dd>property based <font SIZE="-1">CPU</font>(s) to node mapping (Since: 2.10)</dl>
<p> <code>Since:</code> 2.1 <code>NumaOptions</code> (Object) A discriminated record of <font SIZE="-1">NUMA</font> options. (for OptsVisitor) <code>Members:</code></p>
<dl>
<dt>&quot;type: NumaOptionsType&quot;</p>
<dd>Not documented</p>
<dt>The members of &quot;NumaNodeOptions&quot; when &quot;type&quot; is &quot;node&quot;</p>
<dd>
<dt>The members of &quot;NumaDistOptions&quot; when &quot;type&quot; is &quot;dist&quot;</p>
<dd>
<dt>The members of &quot;NumaCpuOptions&quot; when &quot;type&quot; is &quot;cpu&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.1 <code>NumaNodeOptions</code> (Object) Create a guest <font SIZE="-1">NUMA</font> node. (for OptsVisitor) <code>Members:</code></p>
<dl>
<dt>&quot;nodeid: int&quot; (optional)</p>
<dd><font SIZE="-1">NUMA</font> node <font SIZE="-1">ID</font> (increase by 1 from 0 if omitted)</p>
<dt>&quot;cpus: array of int&quot; (optional)</p>
<dd>VCPUs belonging to this node (assign <font SIZE="-1">VCPUS</font> round-robin if omitted)</p>
<dt>&quot;mem: int&quot; (optional)</p>
<dd>memory size of this node; mutually exclusive with <tt>&quot;memdev&quot;</tt>. Equally divide total memory among nodes if both <tt>&quot;mem&quot;</tt> and <tt>&quot;memdev&quot;</tt> are omitted.</p>
<dt>&quot;memdev: string&quot; (optional)</p>
<dd>memory backend object. If specified for one node, it must be specified for all nodes.</dl>
<p> <code>Since:</code> 2.1 <code>NumaDistOptions</code> (Object) Set the distance between 2 <font SIZE="-1">NUMA</font> nodes. <code>Members:</code></p>
<dl>
<dt>&quot;src: int&quot;</p>
<dd>source <font SIZE="-1">NUMA</font> node.</p>
<dt>&quot;dst: int&quot;</p>
<dd>destination <font SIZE="-1">NUMA</font> node.</p>
<dt>&quot;val: int&quot;</p>
<dd><font SIZE="-1">NUMA</font> distance from source node to destination node. When a node is unreachable from another node, set the distance between them to 255.</dl>
<p> <code>Since:</code> 2.10 <code>X86CPURegister32</code> (Enum) A X86 32-bit register <code>Values:</code></p>
<dl>
<dt>&quot;EAX&quot;</p>
<dd>Not documented</p>
<dt>&quot;EBX&quot;</p>
<dd>Not documented</p>
<dt>&quot;ECX&quot;</p>
<dd>Not documented</p>
<dt>&quot;EDX&quot;</p>
<dd>Not documented</p>
<dt>&quot;ESP&quot;</p>
<dd>Not documented</p>
<dt>&quot;EBP&quot;</p>
<dd>Not documented</p>
<dt>&quot;ESI&quot;</p>
<dd>Not documented</p>
<dt>&quot;EDI&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 1.5 <code>X86CPUFeatureWordInfo</code> (Object) Information about a X86 <font SIZE="-1">CPU</font> feature word <code>Members:</code></p>
<dl>
<dt>&quot;cpuid-input-eax: int&quot;</p>
<dd>Input <font SIZE="-1">EAX</font> value for <font SIZE="-1">CPUID</font> instruction for that feature word</p>
<dt>&quot;cpuid-input-ecx: int&quot; (optional)</p>
<dd>Input <font SIZE="-1">ECX</font> value for <font SIZE="-1">CPUID</font> instruction for that feature word</p>
<dt>&quot;cpuid-register: X86CPURegister32&quot;</p>
<dd>Output register containing the feature bits</p>
<dt>&quot;features: int&quot;</p>
<dd>value of output register, containing the feature bits</dl>
<p> <code>Since:</code> 1.5 <code>DummyForceArrays</code> (Object) Not used by <font SIZE="-1">QMP</font>; hack to let us use X86CPUFeatureWordInfoList internally <code>Members:</code></p>
<dl>
<dt>&quot;unused: array of X86CPUFeatureWordInfo&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 2.5 <code>NumaCpuOptions</code> (Object) Option &#8220;-numa cpu&#8221; overrides default cpu to node mapping. It accepts the same set of cpu properties as returned by query-hotpluggable-cpus[].props, where node-id could be used to override default node mapping. <code>Members:</code></p>
<dl>
<dt>The members of &quot;CpuInstanceProperties&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.10 <code>HostMemPolicy</code> (Enum) Host memory policy types <code>Values:</code></p>
<dl>
<dt>&quot;default&quot;</p>
<dd>restore default policy, remove any nondefault policy</p>
<dt>&quot;preferred&quot;</p>
<dd>set the preferred host nodes for allocation</p>
<dt>&quot;bind&quot;</p>
<dd>a strict policy that restricts memory allocation to the host nodes specified</p>
<dt>&quot;interleave&quot;</p>
<dd>memory allocations are interleaved across the set of host nodes specified</dl>
<p> <code>Since:</code> 2.1 <code>Memdev</code> (Object) Information about memory backend <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot; (optional)</p>
<dd>backend&#8217;s <font SIZE="-1">ID</font> if backend has &#8216;id&#8217; property (since 2.9)</p>
<dt>&quot;size: int&quot;</p>
<dd>memory backend size</p>
<dt>&quot;merge: boolean&quot;</p>
<dd>enables or disables memory merge support</p>
<dt>&quot;dump: boolean&quot;</p>
<dd>includes memory backend&#8217;s memory in a core dump or not</p>
<dt>&quot;prealloc: boolean&quot;</p>
<dd>enables or disables memory preallocation</p>
<dt>&quot;host-nodes: array of int&quot;</p>
<dd>host nodes for its memory policy</p>
<dt>&quot;policy: HostMemPolicy&quot;</p>
<dd>memory policy of memory backend</dl>
<p> <code>Since:</code> 2.1 <code>query-memdev</code> (Command) Returns information for all memory backends. <code>Returns:</code> a list of <tt>&quot;Memdev&quot;</tt>. <code>Since:</code> 2.1 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-memdev&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;id&quot; : &quot;mem1&quot;,<br />
            &quot;size&quot; : 536870912,<br />
            &quot;merge&quot; : false,<br />
            &quot;dump&quot; : true,<br />
            &quot;prealloc&quot; : false,<br />
            &quot;host-nodes&quot; : [ 0, 1 ],<br />
            &quot;policy&quot; : &quot;bind&quot;<br />
        },<br />
        {<br />
            &quot;size&quot; : 536870912,<br />
            &quot;merge&quot; : false,<br />
            &quot;dump&quot; : true,<br />
            &quot;prealloc&quot; : true,<br />
            &quot;host-nodes&quot; : [ 2, 3 ],<br />
            &quot;policy&quot; : &quot;preferred&quot;<br />
        }<br />
    ]<br />
} <code>CpuInstanceProperties</code> (Object) List of properties to be used for hotplugging a <font SIZE="-1">CPU</font> instance, it should be passed by management with device_add command when a <font SIZE="-1">CPU</font> is being hotplugged. <code>Members:</code></p>
<dl>
<dt>&quot;node-id: int&quot; (optional)</p>
<dd><font SIZE="-1">NUMA</font> node <font SIZE="-1">ID</font> the <font SIZE="-1">CPU</font> belongs to</p>
<dt>&quot;socket-id: int&quot; (optional)</p>
<dd>socket number within node/board the <font SIZE="-1">CPU</font> belongs to</p>
<dt>&quot;die-id: int&quot; (optional)</p>
<dd>die number within node/board the <font SIZE="-1">CPU</font> belongs to (Since 4.1)</p>
<dt>&quot;core-id: int&quot; (optional)</p>
<dd>core number within die the <font SIZE="-1">CPU</font> belongs to# <tt>&quot;thread-id&quot;</tt>: thread number within core the <font SIZE="-1">CPU</font> belongs to</p>
<dt>&quot;thread-id: int&quot; (optional)</p>
<dd>Not documented</dl>
<p> <code>Note:</code> currently there are 5 properties that could be present but management should be prepared to pass through other properties with device_add command to allow for future interface extension. This also requires the filed names to be kept in sync with the properties passed to -device/device_add. <code>Since:</code> 2.7 <code>HotpluggableCPU</code> (Object) <code>Members:</code></p>
<dl>
<dt>&quot;type: string&quot;</p>
<dd><font SIZE="-1">CPU</font> object type for usage with device_add command</p>
<dt>&quot;props: CpuInstanceProperties&quot;</p>
<dd>list of properties to be used for hotplugging <font SIZE="-1">CPU</font></p>
<dt>&quot;vcpus-count: int&quot;</p>
<dd>number of logical <font SIZE="-1">VCPU</font> threads <tt>&quot;HotpluggableCPU&quot;</tt> provides</p>
<dt>&quot;qom-path: string&quot; (optional)</p>
<dd>link to existing <font SIZE="-1">CPU</font> object if <font SIZE="-1">CPU</font> is present or omitted if <font SIZE="-1">CPU</font> is not present.</dl>
<p> <code>Since:</code> 2.7 <code>query-hotpluggable-cpus</code> (Command) <font SIZE="-1"><code>TODO:</code></font> Better documentation; currently there is none. <code>Returns:</code> a list of HotpluggableCPU objects. <code>Since:</code> 2.7 <code>Example:</code> </p>
<pre> For pseries machine type started with -smp 2,cores=2,maxcpus=4 -cpu POWER8:
 
 -&gt; { &quot;execute&quot;: &quot;query-hotpluggable-cpus&quot; }
 &lt;- {&quot;return&quot;: [
 { &quot;props&quot;: { &quot;core&quot;: 8 }, &quot;type&quot;: &quot;POWER8-spapr-cpu-core&quot;,
 &quot;vcpus-count&quot;: 1 },
 { &quot;props&quot;: { &quot;core&quot;: 0 }, &quot;type&quot;: &quot;POWER8-spapr-cpu-core&quot;,
 &quot;vcpus-count&quot;: 1, &quot;qom-path&quot;: &quot;/machine/unattached/device[0]&quot;}
 ]}'
 
 For pc machine type started with -smp 1,maxcpus=2:
 
 -&gt; { &quot;execute&quot;: &quot;query-hotpluggable-cpus&quot; }
 &lt;- {&quot;return&quot;: [
 {
 &quot;type&quot;: &quot;qemu64-x86_64-cpu&quot;, &quot;vcpus-count&quot;: 1,
 &quot;props&quot;: {&quot;core-id&quot;: 0, &quot;socket-id&quot;: 1, &quot;thread-id&quot;: 0}
 },
 {
 &quot;qom-path&quot;: &quot;/machine/unattached/device[0]&quot;,
 &quot;type&quot;: &quot;qemu64-x86_64-cpu&quot;, &quot;vcpus-count&quot;: 1,
 &quot;props&quot;: {&quot;core-id&quot;: 0, &quot;socket-id&quot;: 0, &quot;thread-id&quot;: 0}
 }
 ]}
 
 For s390x-virtio-ccw machine type started with -smp 1,maxcpus=2 -cpu qemu
 (Since: 2.11):
 
 -&gt; { &quot;execute&quot;: &quot;query-hotpluggable-cpus&quot; }
 &lt;- {&quot;return&quot;: [
 {
 &quot;type&quot;: &quot;qemu-s390x-cpu&quot;, &quot;vcpus-count&quot;: 1,
 &quot;props&quot;: { &quot;core-id&quot;: 1 }
 },
 {
 &quot;qom-path&quot;: &quot;/machine/unattached/device[0]&quot;,
 &quot;type&quot;: &quot;qemu-s390x-cpu&quot;, &quot;vcpus-count&quot;: 1,
 &quot;props&quot;: { &quot;core-id&quot;: 0 }
 }
 ]}</pre>
<p><code>set-numa-node</code> (Command) Runtime equivalent of &#8216;-numa&#8217; <font SIZE="-1">CLI</font> option, available at preconfigure stage to configure numa mapping before initializing machine. Since 3.0 <code>Arguments:</code> the members of <tt>&quot;NumaOptions&quot;</tt> <code>CpuModelInfo</code> (Object) Virtual <font SIZE="-1">CPU</font> model. A <font SIZE="-1">CPU</font> model consists of the name of a <font SIZE="-1">CPU</font> definition, to which delta changes are applied (e.g. features added/removed). Most magic values that an architecture might require should be hidden behind the name. However, if required, architectures can expose relevant properties. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>the name of the <font SIZE="-1">CPU</font> definition the model is based on</p>
<dt>&quot;props: value&quot; (optional)</p>
<dd>a dictionary of <font SIZE="-1">QOM</font> properties to be applied</dl>
<p> <code>Since:</code> 2.8.0 <code>CpuModelExpansionType</code> (Enum) An enumeration of <font SIZE="-1">CPU</font> model expansion types. <code>Values:</code></p>
<dl>
<dt>&quot;static&quot;</p>
<dd>Expand to a static <font SIZE="-1">CPU</font> model, a combination of a static base model name and property delta changes. As the static base model will never change, the expanded <font SIZE="-1">CPU</font> model will be the same, independent of <font SIZE="-1">QEMU</font> version, machine type, machine options, and accelerator options. Therefore, the resulting model can be used by tooling without having to specify a compatibility machine &#8211; e.g. when displaying the &#8220;host&#8221; model. The <tt>&quot;static&quot;</tt> <font SIZE="-1">CPU</font> models are migration-safe.</p>
<dt>&quot;full&quot;</p>
<dd>Expand all properties. The produced model is not guaranteed to be migration-safe, but allows tooling to get an insight and work with model details.</dl>
<p> <code>Note:</code> When a non-migration-safe <font SIZE="-1">CPU</font> model is expanded in static mode, some features enabled by the <font SIZE="-1">CPU</font> model may be omitted, because they can&#8217;t be implemented by a static <font SIZE="-1">CPU</font> model definition (e.g. cache info passthrough and <font SIZE="-1">PMU</font> passthrough in x86). If you need an accurate representation of the features enabled by a non-migration-safe <font SIZE="-1">CPU</font> model, use <tt>&quot;full&quot;</tt>. If you need a static representation that will keep <font SIZE="-1">ABI</font> compatibility even when changing <font SIZE="-1">QEMU</font> version or machine-type, use <tt>&quot;static&quot;</tt> (but keep in mind that some features may be omitted). <code>Since:</code> 2.8.0 <code>CpuModelCompareResult</code> (Enum) An enumeration of <font SIZE="-1">CPU</font> model comparison results. The result is usually calculated using e.g. <font SIZE="-1">CPU</font> features or <font SIZE="-1">CPU</font> generations. <code>Values:</code></p>
<dl>
<dt>&quot;incompatible&quot;</p>
<dd>If model A is incompatible to model B, model A is not guaranteed to run where model B runs and the other way around.</p>
<dt>&quot;identical&quot;</p>
<dd>If model A is identical to model B, model A is guaranteed to run where model B runs and the other way around.</p>
<dt>&quot;superset&quot;</p>
<dd>If model A is a superset of model B, model B is guaranteed to run where model A runs. There are no guarantees about the other way.</p>
<dt>&quot;subset&quot;</p>
<dd>If model A is a subset of model B, model A is guaranteed to run where model B runs. There are no guarantees about the other way.</dl>
<p> <code>Since:</code> 2.8.0 <code>CpuModelBaselineInfo</code> (Object) The result of a <font SIZE="-1">CPU</font> model baseline. <code>Members:</code></p>
<dl>
<dt>&quot;model: CpuModelInfo&quot;</p>
<dd>the baselined CpuModelInfo.</dl>
<p> <code>Since:</code> 2.8.0 <code>If:</code> <tt>&quot;defined(TARGET_S390X)&quot;</tt> <code>CpuModelCompareInfo</code> (Object) The result of a <font SIZE="-1">CPU</font> model comparison. <code>Members:</code></p>
<dl>
<dt>&quot;result: CpuModelCompareResult&quot;</p>
<dd>The result of the compare operation.</p>
<dt>&quot;responsible-properties: array of string&quot;</p>
<dd>List of properties that led to the comparison result not being identical.</dl>
<p> <tt>&quot;responsible-properties&quot;</tt> is a list of <font SIZE="-1">QOM</font> property names that led to both CPUs not being detected as identical. For identical models, this list is empty. If a <font SIZE="-1">QOM</font> property is read-only, that means there&#8217;s no known way to make the <font SIZE="-1">CPU</font> models identical. If the special property name &#8220;type&#8221; is included, the models are by definition not identical and cannot be made identical. <code>Since:</code> 2.8.0 <code>If:</code> <tt>&quot;defined(TARGET_S390X)&quot;</tt> <code>query-cpu-model-comparison</code> (Command) Compares two <font SIZE="-1">CPU</font> models, returning how they compare in a specific configuration. The results indicates how both models compare regarding runnability. This result can be used by tooling to make decisions if a certain <font SIZE="-1">CPU</font> model will run in a certain configuration or if a compatible <font SIZE="-1">CPU</font> model has to be created by baselining. Usually, a <font SIZE="-1">CPU</font> model is compared against the maximum possible <font SIZE="-1">CPU</font> model of a certain configuration (e.g. the &#8220;host&#8221; model for <font SIZE="-1">KVM</font>). If that <font SIZE="-1">CPU</font> model is identical or a subset, it will run in that configuration. The result returned by this command may be affected by:</p>
<dl>
<dt>&bull;</p>
<dd><font SIZE="-1">QEMU</font> version: <font SIZE="-1">CPU</font> models may look different depending on the <font SIZE="-1">QEMU</font> version. (Except for <font SIZE="-1">CPU</font> models reported as &#8220;static&#8221; in query-cpu-definitions.)</p>
<dt>&bull;</p>
<dd>machine-type: <font SIZE="-1">CPU</font> model may look different depending on the machine-type. (Except for <font SIZE="-1">CPU</font> models reported as &#8220;static&#8221; in query-cpu-definitions.)</p>
<dt>&bull;</p>
<dd>machine options (including accelerator): in some architectures, <font SIZE="-1">CPU</font> models may look different depending on machine and accelerator options. (Except for <font SIZE="-1">CPU</font> models reported as &#8220;static&#8221; in query-cpu-definitions.)</p>
<dt>&bull;</p>
<dd>&#8220;-cpu&#8221; arguments and global properties: arguments to the -cpu option and global properties may affect expansion of <font SIZE="-1">CPU</font> models. Using query-cpu-model-expansion while using these is not advised.</dl>
<p> Some architectures may not support comparing <font SIZE="-1">CPU</font> models. s390x supports comparing <font SIZE="-1">CPU</font> models. <code>Arguments:</code></p>
<dl>
<dt>&quot;modela: CpuModelInfo&quot;</p>
<dd>Not documented</p>
<dt>&quot;modelb: CpuModelInfo&quot;</p>
<dd>Not documented</dl>
<p> <code>Returns:</code> a CpuModelBaselineInfo. Returns an error if comparing <font SIZE="-1">CPU</font> models is not supported, if a model cannot be used, if a model contains an unknown cpu definition name, unknown properties or properties with wrong types. <code>Note:</code> this command isn&#8217;t specific to s390x, but is only implemented on this architecture currently. <code>Since:</code> 2.8.0 <code>If:</code> <tt>&quot;defined(TARGET_S390X)&quot;</tt> <code>query-cpu-model-baseline</code> (Command) Baseline two <font SIZE="-1">CPU</font> models, creating a compatible third model. The created model will always be a static, migration-safe <font SIZE="-1">CPU</font> model (see &#8220;static&#8221; <font SIZE="-1">CPU</font> model expansion for details). This interface can be used by tooling to create a compatible <font SIZE="-1">CPU</font> model out two <font SIZE="-1">CPU</font> models. The created <font SIZE="-1">CPU</font> model will be identical to or a subset of both <font SIZE="-1">CPU</font> models when comparing them. Therefore, the created <font SIZE="-1">CPU</font> model is guaranteed to run where the given <font SIZE="-1">CPU</font> models run. The result returned by this command may be affected by:</p>
<dl>
<dt>&bull;</p>
<dd><font SIZE="-1">QEMU</font> version: <font SIZE="-1">CPU</font> models may look different depending on the <font SIZE="-1">QEMU</font> version. (Except for <font SIZE="-1">CPU</font> models reported as &#8220;static&#8221; in query-cpu-definitions.)</p>
<dt>&bull;</p>
<dd>machine-type: <font SIZE="-1">CPU</font> model may look different depending on the machine-type. (Except for <font SIZE="-1">CPU</font> models reported as &#8220;static&#8221; in query-cpu-definitions.)</p>
<dt>&bull;</p>
<dd>machine options (including accelerator): in some architectures, <font SIZE="-1">CPU</font> models may look different depending on machine and accelerator options. (Except for <font SIZE="-1">CPU</font> models reported as &#8220;static&#8221; in query-cpu-definitions.)</p>
<dt>&bull;</p>
<dd>&#8220;-cpu&#8221; arguments and global properties: arguments to the -cpu option and global properties may affect expansion of <font SIZE="-1">CPU</font> models. Using query-cpu-model-expansion while using these is not advised.</dl>
<p> Some architectures may not support baselining <font SIZE="-1">CPU</font> models. s390x supports baselining <font SIZE="-1">CPU</font> models. <code>Arguments:</code></p>
<dl>
<dt>&quot;modela: CpuModelInfo&quot;</p>
<dd>Not documented</p>
<dt>&quot;modelb: CpuModelInfo&quot;</p>
<dd>Not documented</dl>
<p> <code>Returns:</code> a CpuModelBaselineInfo. Returns an error if baselining <font SIZE="-1">CPU</font> models is not supported, if a model cannot be used, if a model contains an unknown cpu definition name, unknown properties or properties with wrong types. <code>Note:</code> this command isn&#8217;t specific to s390x, but is only implemented on this architecture currently. <code>Since:</code> 2.8.0 <code>If:</code> <tt>&quot;defined(TARGET_S390X)&quot;</tt> <code>CpuModelExpansionInfo</code> (Object) The result of a cpu model expansion. <code>Members:</code></p>
<dl>
<dt>&quot;model: CpuModelInfo&quot;</p>
<dd>the expanded CpuModelInfo.</dl>
<p> <code>Since:</code> 2.8.0 <code>If:</code> <tt>&quot;defined(TARGET_S390X) || defined(TARGET_I386) || defined(TARGET_ARM)&quot;</tt> <code>query-cpu-model-expansion</code> (Command) Expands a given <font SIZE="-1">CPU</font> model (or a combination of <font SIZE="-1">CPU</font> model + additional options) to different granularities, allowing tooling to get an understanding what a specific <font SIZE="-1">CPU</font> model looks like in <font SIZE="-1">QEMU</font> under a certain configuration. This interface can be used to query the &#8220;host&#8221; <font SIZE="-1">CPU</font> model. The data returned by this command may be affected by:</p>
<dl>
<dt>&bull;</p>
<dd><font SIZE="-1">QEMU</font> version: <font SIZE="-1">CPU</font> models may look different depending on the <font SIZE="-1">QEMU</font> version. (Except for <font SIZE="-1">CPU</font> models reported as &#8220;static&#8221; in query-cpu-definitions.)</p>
<dt>&bull;</p>
<dd>machine-type: <font SIZE="-1">CPU</font> model may look different depending on the machine-type. (Except for <font SIZE="-1">CPU</font> models reported as &#8220;static&#8221; in query-cpu-definitions.)</p>
<dt>&bull;</p>
<dd>machine options (including accelerator): in some architectures, <font SIZE="-1">CPU</font> models may look different depending on machine and accelerator options. (Except for <font SIZE="-1">CPU</font> models reported as &#8220;static&#8221; in query-cpu-definitions.)</p>
<dt>&bull;</p>
<dd>&#8220;-cpu&#8221; arguments and global properties: arguments to the -cpu option and global properties may affect expansion of <font SIZE="-1">CPU</font> models. Using query-cpu-model-expansion while using these is not advised.</dl>
<p> Some architectures may not support all expansion types. s390x supports &#8220;full&#8221; and &#8220;static&#8221;. Arm only supports &#8220;full&#8221;. <code>Arguments:</code></p>
<dl>
<dt>&quot;type: CpuModelExpansionType&quot;</p>
<dd>Not documented</p>
<dt>&quot;model: CpuModelInfo&quot;</p>
<dd>Not documented</dl>
<p> <code>Returns:</code> a CpuModelExpansionInfo. Returns an error if expanding <font SIZE="-1">CPU</font> models is not supported, if the model cannot be expanded, if the model contains an unknown <font SIZE="-1">CPU</font> definition name, unknown properties or properties with a wrong type. Also returns an error if an expansion type is not supported. <code>Since:</code> 2.8.0 <code>If:</code> <tt>&quot;defined(TARGET_S390X) || defined(TARGET_I386) || defined(TARGET_ARM)&quot;</tt> <code>CpuDefinitionInfo</code> (Object) Virtual <font SIZE="-1">CPU</font> definition. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>the name of the <font SIZE="-1">CPU</font> definition</p>
<dt>&quot;migration-safe: boolean&quot; (optional)</p>
<dd>whether a <font SIZE="-1">CPU</font> definition can be safely used for migration in combination with a <font SIZE="-1">QEMU</font> compatibility machine when migrating between different <font SIZE="-1">QEMU</font> versions and between hosts with different sets of (hardware or software) capabilities. If not provided, information is not available and callers should not assume the <font SIZE="-1">CPU</font> definition to be migration-safe. (since 2.8)</p>
<dt>&quot;static: boolean&quot;</p>
<dd>whether a <font SIZE="-1">CPU</font> definition is static and will not change depending on <font SIZE="-1">QEMU</font> version, machine type, machine options and accelerator options. A static model is always migration-safe. (since 2.8)</p>
<dt>&quot;unavailable-features: array of string&quot; (optional)</p>
<dd>List of properties that prevent the <font SIZE="-1">CPU</font> model from running in the current host. (since 2.8)</p>
<dt>&quot;typename: string&quot;</p>
<dd>Type name that can be used as argument to <tt>&quot;device-list-properties&quot;</tt>, to introspect properties configurable using -cpu or -global. (since 2.9)</p>
<dt>&quot;alias-of: string&quot; (optional)</p>
<dd>Name of <font SIZE="-1">CPU</font> model this model is an alias for. The target of the <font SIZE="-1">CPU</font> model alias may change depending on the machine type. Management software is supposed to translate <font SIZE="-1">CPU</font> model aliases in the <font SIZE="-1">VM</font> configuration, because aliases may stop being migration-safe in the future (since 4.1)</dl>
<p> <tt>&quot;unavailable-features&quot;</tt> is a list of <font SIZE="-1">QOM</font> property names that represent <font SIZE="-1">CPU</font> model attributes that prevent the <font SIZE="-1">CPU</font> from running. If the <font SIZE="-1">QOM</font> property is read-only, that means there&#8217;s no known way to make the <font SIZE="-1">CPU</font> model run in the current host. Implementations that choose not to provide specific information return the property name &#8220;type&#8221;. If the property is read-write, it means that it <font SIZE="-1">MAY</font> be possible to run the <font SIZE="-1">CPU</font> model in the current host if that property is changed. Management software can use it as hints to suggest or choose an alternative for the user, or just to generate meaningful error messages explaining why the <font SIZE="-1">CPU</font> model can&#8217;t be used. If <tt>&quot;unavailable-features&quot;</tt> is an empty list, the <font SIZE="-1">CPU</font> model is runnable using the current host and machine-type. If <tt>&quot;unavailable-features&quot;</tt> is not present, runnability information for the <font SIZE="-1">CPU</font> is not available. <code>Since:</code> 1.2.0 <code>If:</code> <tt>&quot;defined(TARGET_PPC) || defined(TARGET_ARM) || defined(TARGET_I386) || defined(TARGET_S390X) || defined(TARGET_MIPS)&quot;</tt> <code>query-cpu-definitions</code> (Command) Return a list of supported virtual <font SIZE="-1">CPU</font> definitions <code>Returns:</code> a list of CpuDefInfo <code>Since:</code> 1.2.0 <code>If:</code> <tt>&quot;defined(TARGET_PPC) || defined(TARGET_ARM) || defined(TARGET_I386) || defined(TARGET_S390X) || defined(TARGET_MIPS)&quot;</tt></p>
<h3>Miscellanea</h3>
<p><code>qmp_capabilities</code> (Command) Enable <font SIZE="-1">QMP</font> capabilities. Arguments: <code>Arguments:</code></p>
<dl>
<dt>&quot;enable: array of QMPCapability&quot; (optional)</p>
<dd>An optional list of QMPCapability values to enable. The client must not enable any capability that is not mentioned in the <font SIZE="-1">QMP</font> greeting message. If the field is not provided, it means no <font SIZE="-1">QMP</font> capabilities will be enabled. (since 2.12)</dl>
<p> <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;qmp_capabilities&quot;,<br />
   &quot;arguments&quot; : {&quot;enable&quot; : [&quot;oob&quot;]}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>Notes:</code> This command is valid exactly when first connecting: it must be issued before any other command will be accepted, and will fail once the monitor is accepting other commands. (see qemu docs/interop/qmp-spec.txt) The <font SIZE="-1">QMP</font> client needs to explicitly enable <font SIZE="-1">QMP</font> capabilities, otherwise all the <font SIZE="-1">QMP</font> capabilities will be turned off by default. <code>Since:</code> 0.13 <code>QMPCapability</code> (Enum) Enumeration of capabilities to be advertised during initial client connection, used for agreeing on particular <font SIZE="-1">QMP</font> extension behaviors. <code>Values:</code></p>
<dl>
<dt>&quot;oob&quot;</p>
<dd><font SIZE="-1">QMP</font> ability to support out-of-band requests. (Please refer to qmp-spec.txt for more information on <font SIZE="-1">OOB</font>)</dl>
<p> <code>Since:</code> 2.12 <code>VersionTriple</code> (Object) A three-part version number. <code>Members:</code></p>
<dl>
<dt>&quot;major: int&quot;</p>
<dd>The major version number.</p>
<dt>&quot;minor: int&quot;</p>
<dd>The minor version number.</p>
<dt>&quot;micro: int&quot;</p>
<dd>The micro version number.</dl>
<p> <code>Since:</code> 2.4 <code>VersionInfo</code> (Object) A description of <font SIZE="-1">QEMU</font>&#8216;s version. <code>Members:</code></p>
<dl>
<dt>&quot;qemu: VersionTriple&quot;</p>
<dd>The version of <font SIZE="-1">QEMU.</font> By current convention, a micro version of 50 signifies a development branch. A micro version greater than or equal to 90 signifies a release candidate for the next minor version. A micro version of less than 50 signifies a stable release.</p>
<dt>&quot;package: string&quot;</p>
<dd><font SIZE="-1">QEMU</font> will always set this field to an empty string. Downstream versions of <font SIZE="-1">QEMU</font> should set this to a non-empty string. The exact format depends on the downstream however it highly recommended that a unique name is used.</dl>
<p> <code>Since:</code> 0.14.0 <code>query-version</code> (Command) Returns the current version of <font SIZE="-1">QEMU.</font> <code>Returns:</code> A <tt>&quot;VersionInfo&quot;</tt> object describing the current version of <font SIZE="-1">QEMU.</font> <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-version&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;qemu&quot; : {<br />
            &quot;major&quot; : 0,<br />
            &quot;minor&quot; : 11,<br />
            &quot;micro&quot; : 5<br />
        },<br />
                 &quot;package&quot; : &quot;&quot;<br />
    }<br />
} <code>CommandInfo</code> (Object) Information about a <font SIZE="-1">QMP</font> command <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>The command name</dl>
<p> <code>Since:</code> 0.14.0 <code>query-commands</code> (Command) Return a list of supported <font SIZE="-1">QMP</font> commands by this server <code>Returns:</code> A list of <tt>&quot;CommandInfo&quot;</tt> for all supported commands <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-commands&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;name&quot; : &quot;query-balloon&quot;<br />
        },<br />
        {<br />
            &quot;name&quot; : &quot;system_powerdown&quot;<br />
        }<br />
    ]<br />
} <code>Note:</code> This example has been shortened as the real response is too long. <code>LostTickPolicy</code> (Enum) Policy for handling lost ticks in timer devices. <code>Values:</code></p>
<dl>
<dt>&quot;discard&quot;</p>
<dd>throw away the missed tick(s) and continue with future injection normally. Guest time may be delayed, unless the <font SIZE="-1">OS</font> has explicit handling of lost ticks</p>
<dt>&quot;delay&quot;</p>
<dd>continue to deliver ticks at the normal rate. Guest time will be delayed due to the late tick</p>
<dt>&quot;slew&quot;</p>
<dd>deliver ticks at a higher rate to catch up with the missed tick. The guest time should not be delayed once catchup is complete.</dl>
<p> <code>Since:</code> 2.0 <code>add_client</code> (Command) Allow client connections for <font SIZE="-1">VNC,</font> Spice and socket based character devices to be passed in to <font SIZE="-1">QEMU</font> via <font SIZE="-1">SCM_RIGHTS.</font> <code>Arguments:</code></p>
<dl>
<dt>&quot;protocol: string&quot;</p>
<dd>protocol name. Valid names are &#8220;vnc&#8221;, &#8220;spice&#8221; or the name of a character device (eg. from -chardev id=XXXX)</p>
<dt>&quot;fdname: string&quot;</p>
<dd>file descriptor name previously passed via &#8216;getfd&#8217; command</p>
<dt>&quot;skipauth: boolean&quot; (optional)</p>
<dd>whether to skip authentication. Only applies to &#8220;vnc&#8221; and &#8220;spice&#8221; protocols</p>
<dt>&quot;tls: boolean&quot; (optional)</p>
<dd>whether to perform <font SIZE="-1">TLS.</font> Only applies to the &#8220;spice&#8221; protocol</dl>
<p> <code>Returns:</code> nothing on success. <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;add_client&quot;, &quot;arguments&quot; : {&quot;protocol&quot; : &quot;vnc&quot;,<br />
                                            &quot;fdname&quot; : &quot;myclient&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>NameInfo</code> (Object) Guest name information. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot; (optional)</p>
<dd>The name of the guest</dl>
<p> <code>Since:</code> 0.14.0 <code>query-name</code> (Command) Return the name information of a guest. <code>Returns:</code> <tt>&quot;NameInfo&quot;</tt> of the guest <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-name&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;name&quot; : &quot;qemu-name&quot;<br />
    }<br />
} <code>KvmInfo</code> (Object) Information about support for <font SIZE="-1">KVM</font> acceleration <code>Members:</code></p>
<dl>
<dt>&quot;enabled: boolean&quot;</p>
<dd>true if <font SIZE="-1">KVM</font> acceleration is active</p>
<dt>&quot;present: boolean&quot;</p>
<dd>true if <font SIZE="-1">KVM</font> acceleration is built into this executable</dl>
<p> <code>Since:</code> 0.14.0 <code>query-kvm</code> (Command) Returns information about <font SIZE="-1">KVM</font> acceleration <code>Returns:</code> <tt>&quot;KvmInfo&quot;</tt> <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-kvm&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;enabled&quot; : true, &quot;present&quot; : true<br />
    }<br />
} <code>UuidInfo</code> (Object) Guest <font SIZE="-1">UUID</font> information (Universally Unique Identifier). <code>Members:</code></p>
<dl>
<dt>&quot;UUID: string&quot;</p>
<dd>the <font SIZE="-1">UUID</font> of the guest</dl>
<p> <code>Since:</code> 0.14.0 <code>Notes:</code> If no <font SIZE="-1">UUID</font> was specified for the guest, a null <font SIZE="-1">UUID</font> is returned. <code>query-uuid</code> (Command) Query the guest <font SIZE="-1">UUID</font> information. <code>Returns:</code> The <tt>&quot;UuidInfo&quot;</tt> for the guest <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-uuid&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;UUID&quot; : &quot;550e8400-e29b-41d4-a716-446655440000&quot;<br />
    }<br />
} <code>EventInfo</code> (Object) Information about a <font SIZE="-1">QMP</font> event <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>The event name</dl>
<p> <code>Since:</code> 1.2.0 <code>query-events</code> (Command) Return information on <font SIZE="-1">QMP</font> events. <code>Returns:</code> A list of <tt>&quot;EventInfo&quot;</tt>. <code>Since:</code> 1.2.0 <code>Note:</code> This command is deprecated, because its output doesn&#8217;t reflect compile-time configuration. Use query-qmp-schema instead. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-events&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;name&quot; : &quot;SHUTDOWN&quot;<br />
        },<br />
        {<br />
            &quot;name&quot; : &quot;RESET&quot;<br />
        }<br />
    ]<br />
} <code>Note:</code> This example has been shortened as the real response is too long. <code>IOThreadInfo</code> (Object) Information about an iothread <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>the identifier of the iothread</p>
<dt>&quot;thread-id: int&quot;</p>
<dd><font SIZE="-1">ID</font> of the underlying host thread</p>
<dt>&quot;poll-max-ns: int&quot;</p>
<dd>maximum polling time in ns, 0 means polling is disabled (since 2.9)</p>
<dt>&quot;poll-grow: int&quot;</p>
<dd>how many ns will be added to polling time, 0 means that it&#8217;s not configured (since 2.9)</p>
<dt>&quot;poll-shrink: int&quot;</p>
<dd>how many ns will be removed from polling time, 0 means that it&#8217;s not configured (since 2.9)</dl>
<p> <code>Since:</code> 2.0 <code>query-iothreads</code> (Command) Returns a list of information about each iothread. <code>Note:</code> this list excludes the <font SIZE="-1">QEMU</font> main loop thread, which is not declared using the -object iothread command-line option. It is always the main thread of the process. <code>Returns:</code> a list of <tt>&quot;IOThreadInfo&quot;</tt> for each iothread <code>Since:</code> 2.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-iothreads&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;id&quot; : &quot;iothread0&quot;,<br />
            &quot;thread-id&quot; : 3134<br />
        },<br />
        {<br />
            &quot;id&quot; : &quot;iothread1&quot;,<br />
            &quot;thread-id&quot; : 3135<br />
        }<br />
    ]<br />
} <code>BalloonInfo</code> (Object) Information about the guest balloon device. <code>Members:</code></p>
<dl>
<dt>&quot;actual: int&quot;</p>
<dd>the number of bytes the balloon currently contains</dl>
<p> <code>Since:</code> 0.14.0 <code>query-balloon</code> (Command) Return information about the balloon device. <code>Returns:</code> <tt>&quot;BalloonInfo&quot;</tt> on success If the balloon driver is enabled but not functional because the <font SIZE="-1">KVM</font> kernel module cannot support it, KvmMissingCap If no balloon device is present, DeviceNotActive <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-balloon&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;actual&quot; : 1073741824,<br />
    }<br />
} <font SIZE="-1"><code>BALLOON_CHANGE</code></font> (Event) Emitted when the guest changes the actual <font SIZE="-1">BALLOON</font> level. This value is equivalent to the <tt>&quot;actual&quot;</tt> field return by the &#8216;query-balloon&#8217; command <code>Arguments:</code></p>
<dl>
<dt>&quot;actual: int&quot;</p>
<dd>actual level of the guest memory balloon in bytes</dl>
<p> <code>Note:</code> this event is rate-limited. <code>Since:</code> 1.2 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;BALLOON_CHANGE&quot;,
 &quot;data&quot;: { &quot;actual&quot;: 944766976 },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1267020223, &quot;microseconds&quot;: 435656 } }</pre>
<p><code>PciMemoryRange</code> (Object) A <font SIZE="-1">PCI</font> device memory region <code>Members:</code></p>
<dl>
<dt>&quot;base: int&quot;</p>
<dd>the starting address (guest physical)</p>
<dt>&quot;limit: int&quot;</p>
<dd>the ending address (guest physical)</dl>
<p> <code>Since:</code> 0.14.0 <code>PciMemoryRegion</code> (Object) Information about a <font SIZE="-1">PCI</font> device I/O region. <code>Members:</code></p>
<dl>
<dt>&quot;bar: int&quot;</p>
<dd>the index of the Base Address Register for this region</p>
<dt>&quot;type: string&quot;</p>
<dd>&#8216;io&#8217; if the region is a <font SIZE="-1">PIO</font> region &#8216;memory&#8217; if the region is a <font SIZE="-1">MMIO</font> region</p>
<dt>&quot;size: int&quot;</p>
<dd>memory size</p>
<dt>&quot;prefetch: boolean&quot; (optional)</p>
<dd>if <tt>&quot;type&quot;</tt> is &#8216;memory&#8217;, true if the memory is prefetchable</p>
<dt>&quot;mem_type_64: boolean&quot; (optional)</p>
<dd>if <tt>&quot;type&quot;</tt> is &#8216;memory&#8217;, true if the <font SIZE="-1">BAR</font> is 64-bit</p>
<dt>&quot;address: int&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 0.14.0 <code>PciBusInfo</code> (Object) Information about a bus of a <font SIZE="-1">PCI</font> Bridge device <code>Members:</code></p>
<dl>
<dt>&quot;number: int&quot;</p>
<dd>primary bus interface number. This should be the number of the bus the device resides on.</p>
<dt>&quot;secondary: int&quot;</p>
<dd>secondary bus interface number. This is the number of the main bus for the bridge</p>
<dt>&quot;subordinate: int&quot;</p>
<dd>This is the highest number bus that resides below the bridge.</p>
<dt>&quot;io_range: PciMemoryRange&quot;</p>
<dd>The <font SIZE="-1">PIO</font> range for all devices on this bridge</p>
<dt>&quot;memory_range: PciMemoryRange&quot;</p>
<dd>The <font SIZE="-1">MMIO</font> range for all devices on this bridge</p>
<dt>&quot;prefetchable_range: PciMemoryRange&quot;</p>
<dd>The range of prefetchable <font SIZE="-1">MMIO</font> for all devices on this bridge</dl>
<p> <code>Since:</code> 2.4 <code>PciBridgeInfo</code> (Object) Information about a <font SIZE="-1">PCI</font> Bridge device <code>Members:</code></p>
<dl>
<dt>&quot;bus: PciBusInfo&quot;</p>
<dd>information about the bus the device resides on</p>
<dt>&quot;devices: array of PciDeviceInfo&quot; (optional)</p>
<dd>a list of <tt>&quot;PciDeviceInfo&quot;</tt> for each device on this bridge</dl>
<p> <code>Since:</code> 0.14.0 <code>PciDeviceClass</code> (Object) Information about the Class of a <font SIZE="-1">PCI</font> device <code>Members:</code></p>
<dl>
<dt>&quot;desc: string&quot; (optional)</p>
<dd>a string description of the device&#8217;s class</p>
<dt>&quot;class: int&quot;</p>
<dd>the class code of the device</dl>
<p> <code>Since:</code> 2.4 <code>PciDeviceId</code> (Object) Information about the Id of a <font SIZE="-1">PCI</font> device <code>Members:</code></p>
<dl>
<dt>&quot;device: int&quot;</p>
<dd>the <font SIZE="-1">PCI</font> device id</p>
<dt>&quot;vendor: int&quot;</p>
<dd>the <font SIZE="-1">PCI</font> vendor id</p>
<dt>&quot;subsystem: int&quot; (optional)</p>
<dd>the <font SIZE="-1">PCI</font> subsystem id (since 3.1)</p>
<dt>&quot;subsystem-vendor: int&quot; (optional)</p>
<dd>the <font SIZE="-1">PCI</font> subsystem vendor id (since 3.1)</dl>
<p> <code>Since:</code> 2.4 <code>PciDeviceInfo</code> (Object) Information about a <font SIZE="-1">PCI</font> device <code>Members:</code></p>
<dl>
<dt>&quot;bus: int&quot;</p>
<dd>the bus number of the device</p>
<dt>&quot;slot: int&quot;</p>
<dd>the slot the device is located in</p>
<dt>&quot;function: int&quot;</p>
<dd>the function of the slot used by the device</p>
<dt>&quot;class_info: PciDeviceClass&quot;</p>
<dd>the class of the device</p>
<dt>&quot;id: PciDeviceId&quot;</p>
<dd>the <font SIZE="-1">PCI</font> device id</p>
<dt>&quot;irq: int&quot; (optional)</p>
<dd>if an <font SIZE="-1">IRQ</font> is assigned to the device, the <font SIZE="-1">IRQ</font> number</p>
<dt>&quot;qdev_id: string&quot;</p>
<dd>the device name of the <font SIZE="-1">PCI</font> device</p>
<dt>&quot;pci_bridge: PciBridgeInfo&quot; (optional)</p>
<dd>if the device is a <font SIZE="-1">PCI</font> bridge, the bridge information</p>
<dt>&quot;regions: array of PciMemoryRegion&quot;</p>
<dd>a list of the <font SIZE="-1">PCI I/O</font> regions associated with the device</dl>
<p> <code>Notes:</code> the contents of <tt>&quot;class_info&quot;</tt>.desc are not stable and should only be treated as informational. <code>Since:</code> 0.14.0 <code>PciInfo</code> (Object) Information about a <font SIZE="-1">PCI</font> bus <code>Members:</code></p>
<dl>
<dt>&quot;bus: int&quot;</p>
<dd>the bus index</p>
<dt>&quot;devices: array of PciDeviceInfo&quot;</p>
<dd>a list of devices on this bus</dl>
<p> <code>Since:</code> 0.14.0 <code>query-pci</code> (Command) Return information about the <font SIZE="-1">PCI</font> bus topology of the guest. <code>Returns:</code> a list of <tt>&quot;PciInfo&quot;</tt> for each <font SIZE="-1">PCI</font> bus. Each bus is represented by a json-object, which has a key with a json-array of all <font SIZE="-1">PCI</font> devices attached to it. Each device is represented by a json-object. <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-pci&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;bus&quot; : 0,<br />
            &quot;devices&quot; : [<br />
                {<br />
                    &quot;bus&quot; : 0,<br />
                    &quot;qdev_id&quot; : &quot;&quot;,<br />
                    &quot;slot&quot; : 0,<br />
                    &quot;class_info&quot; : {<br />
                        &quot;class&quot; : 1536,<br />
                        &quot;desc&quot; : &quot;Host bridge&quot;<br />
                    },<br />
                    &quot;id&quot; : {<br />
                        &quot;device&quot; : 32902,<br />
                        &quot;vendor&quot; : 4663<br />
                    },<br />
                    &quot;function&quot; : 0,<br />
                    &quot;regions&quot; : [<br />
                    ]<br />
                },<br />
                {<br />
                    &quot;bus&quot; : 0,<br />
                    &quot;qdev_id&quot; : &quot;&quot;,<br />
                    &quot;slot&quot; : 1,<br />
                    &quot;class_info&quot; : {<br />
                        &quot;class&quot; : 1537,<br />
                        &quot;desc&quot; : &quot;ISA bridge&quot;<br />
                    },<br />
                    &quot;id&quot; : {<br />
                        &quot;device&quot; : 32902,<br />
                        &quot;vendor&quot; : 28672<br />
                    },<br />
                    &quot;function&quot; : 0,<br />
                    &quot;regions&quot; : [<br />
                    ]<br />
                },<br />
                {<br />
                    &quot;bus&quot; : 0,<br />
                    &quot;qdev_id&quot; : &quot;&quot;,<br />
                    &quot;slot&quot; : 1,<br />
                    &quot;class_info&quot; : {<br />
                        &quot;class&quot; : 257,<br />
                        &quot;desc&quot; : &quot;IDE controller&quot;<br />
                    },<br />
                    &quot;id&quot; : {<br />
                        &quot;device&quot; : 32902,<br />
                        &quot;vendor&quot; : 28688<br />
                    },<br />
                    &quot;function&quot; : 1,<br />
                    &quot;regions&quot; : [<br />
                        {<br />
                            &quot;bar&quot; : 4,<br />
                            &quot;size&quot; : 16,<br />
                            &quot;address&quot; : 49152,<br />
                            &quot;type&quot; : &quot;io&quot;<br />
                        }<br />
                    ]<br />
                },<br />
                {<br />
                    &quot;bus&quot; : 0,<br />
                    &quot;qdev_id&quot; : &quot;&quot;,<br />
                    &quot;slot&quot; : 2,<br />
                    &quot;class_info&quot; : {<br />
                        &quot;class&quot; : 768,<br />
                        &quot;desc&quot; : &quot;VGA controller&quot;<br />
                    },<br />
                    &quot;id&quot; : {<br />
                        &quot;device&quot; : 4115,<br />
                        &quot;vendor&quot; : 184<br />
                    },<br />
                    &quot;function&quot; : 0,<br />
                    &quot;regions&quot; : [<br />
                        {<br />
                            &quot;prefetch&quot; : true,<br />
                            &quot;mem_type_64&quot; : false,<br />
                            &quot;bar&quot; : 0,<br />
                            &quot;size&quot; : 33554432,<br />
                            &quot;address&quot; : 4026531840,<br />
                            &quot;type&quot; : &quot;memory&quot;<br />
                        },<br />
                        {<br />
                            &quot;prefetch&quot; : false,<br />
                            &quot;mem_type_64&quot; : false,<br />
                            &quot;bar&quot; : 1,<br />
                            &quot;size&quot; : 4096,<br />
                            &quot;address&quot; : 4060086272,<br />
                            &quot;type&quot; : &quot;memory&quot;<br />
                        },<br />
                        {<br />
                            &quot;prefetch&quot; : false,<br />
                            &quot;mem_type_64&quot; : false,<br />
                            &quot;bar&quot; : 6,<br />
                            &quot;size&quot; : 65536,<br />
                            &quot;address&quot; : -1,<br />
                            &quot;type&quot; : &quot;memory&quot;<br />
                        }<br />
                    ]<br />
                },<br />
                {<br />
                    &quot;bus&quot; : 0,<br />
                    &quot;qdev_id&quot; : &quot;&quot;,<br />
                    &quot;irq&quot; : 11,<br />
                    &quot;slot&quot; : 4,<br />
                    &quot;class_info&quot; : {<br />
                        &quot;class&quot; : 1280,<br />
                        &quot;desc&quot; : &quot;RAM controller&quot;<br />
                    },<br />
                    &quot;id&quot; : {<br />
                        &quot;device&quot; : 6900,<br />
                        &quot;vendor&quot; : 4098<br />
                    },<br />
                    &quot;function&quot; : 0,<br />
                    &quot;regions&quot; : [<br />
                        {<br />
                            &quot;bar&quot; : 0,<br />
                            &quot;size&quot; : 32,<br />
                            &quot;address&quot; : 49280,<br />
                            &quot;type&quot; : &quot;io&quot;<br />
                        }<br />
                    ]<br />
                }<br />
            ]<br />
        }<br />
    ]<br />
} <code>Note:</code> This example has been shortened as the real response is too long. <code>quit</code> (Command) This command will cause the <font SIZE="-1">QEMU</font> process to exit gracefully. While every attempt is made to send the <font SIZE="-1">QMP</font> response before terminating, this is not guaranteed. When using this interface, a premature <font SIZE="-1">EOF</font> would not be unexpected. <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;quit&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>stop</code> (Command) Stop all guest <font SIZE="-1">VCPU</font> execution. <code>Since:</code> 0.14.0 <code>Notes:</code> This function will succeed even if the guest is already in the stopped state. In &#8220;inmigrate&#8221; state, it will ensure that the guest remains paused once migration finishes, as if the -S option was passed on the command line. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;stop&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>system_reset</code> (Command) Performs a hard reset of a guest. <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;system_reset&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>system_powerdown</code> (Command) Requests that a guest perform a powerdown operation. <code>Since:</code> 0.14.0 <code>Notes:</code> A guest may or may not respond to this command. This command returning does not indicate that a guest has accepted the request or that it has shut down. Many guests will respond to this command by prompting the user in some way. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;system_powerdown&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>memsave</code> (Command) Save a portion of guest memory to a file. <code>Arguments:</code></p>
<dl>
<dt>&quot;val: int&quot;</p>
<dd>the virtual address of the guest to start from</p>
<dt>&quot;size: int&quot;</p>
<dd>the size of memory region to save</p>
<dt>&quot;filename: string&quot;</p>
<dd>the file to save the memory to as binary data</p>
<dt>&quot;cpu-index: int&quot; (optional)</p>
<dd>the index of the virtual <font SIZE="-1">CPU</font> to use for translating the virtual address (defaults to <font SIZE="-1">CPU 0</font>)</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 0.14.0 <code>Notes:</code> Errors were not reliably returned until 1.1 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;memsave&quot;,<br />
   &quot;arguments&quot; : {&quot;val&quot; : 10,<br />
                  &quot;size&quot; : 100,<br />
                  &quot;filename&quot; : &quot;/tmp/virtual-mem-dump&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>pmemsave</code> (Command) Save a portion of guest physical memory to a file. <code>Arguments:</code></p>
<dl>
<dt>&quot;val: int&quot;</p>
<dd>the physical address of the guest to start from</p>
<dt>&quot;size: int&quot;</p>
<dd>the size of memory region to save</p>
<dt>&quot;filename: string&quot;</p>
<dd>the file to save the memory to as binary data</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 0.14.0 <code>Notes:</code> Errors were not reliably returned until 1.1 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;pmemsave&quot;,<br />
   &quot;arguments&quot; : {&quot;val&quot; : 10,<br />
                  &quot;size&quot; : 100,<br />
                  &quot;filename&quot; : &quot;/tmp/physical-mem-dump&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>cont</code> (Command) Resume guest <font SIZE="-1">VCPU</font> execution. <code>Since:</code> 0.14.0 <code>Returns:</code> If successful, nothing <code>Notes:</code> This command will succeed if the guest is currently running. It will also succeed if the guest is in the &#8220;inmigrate&#8221; state; in this case, the effect of the command is to make sure the guest starts once migration finishes, removing the effect of the -S command line option if it was passed. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;cont&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>x-exit-preconfig</code> (Command) Exit from &#8220;preconfig&#8221; state This command makes <font SIZE="-1">QEMU</font> exit the preconfig state and proceed with <font SIZE="-1">VM</font> initialization using configuration data provided on the command line and via the <font SIZE="-1">QMP</font> monitor during the preconfig state. The command is only available during the preconfig state (i.e. when the &#8211;preconfig command line option was in use). Since 3.0 <code>Returns:</code> nothing <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;x-exit-preconfig&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>system_wakeup</code> (Command) Wake up guest from suspend. If the guest has wake-up from suspend support enabled (wakeup-suspend-support flag from query-current-machine), wake-up guest from suspend if the guest is in <font SIZE="-1">SUSPENDED</font> state. Return an error otherwise. <code>Since:</code> 1.1 <code>Returns:</code> nothing. <code>Note:</code> prior to 4.0, this command does nothing in case the guest isn&#8217;t suspended. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;system_wakeup&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>inject-nmi</code> (Command) Injects a Non-Maskable Interrupt into the default <font SIZE="-1">CPU</font> (x86/s390) or all CPUs (ppc64). The command fails when the guest doesn&#8217;t support injecting. <code>Returns:</code> If successful, nothing <code>Since:</code> 0.14.0 <code>Note:</code> prior to 2.1, this command was only supported for x86 and s390 VMs <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;inject-nmi&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>balloon</code> (Command) Request the balloon driver to change its balloon size. <code>Arguments:</code></p>
<dl>
<dt>&quot;value: int&quot;</p>
<dd>the target size of the balloon in bytes</dl>
<p> <code>Returns:</code> Nothing on success If the balloon driver is enabled but not functional because the <font SIZE="-1">KVM</font> kernel module cannot support it, KvmMissingCap If no balloon device is present, DeviceNotActive <code>Notes:</code> This command just issues a request to the guest. When it returns, the balloon size may not have changed. A guest can change the balloon size independent of this command. <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;balloon&quot;, &quot;arguments&quot; : {&quot;value&quot; : 536870912}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>human-monitor-command</code> (Command) Execute a command on the human monitor and return the output. <code>Arguments:</code></p>
<dl>
<dt>&quot;command-line: string&quot;</p>
<dd>the command to execute in the human monitor</p>
<dt>&quot;cpu-index: int&quot; (optional)</p>
<dd>The <font SIZE="-1">CPU</font> to use for commands that require an implicit <font SIZE="-1">CPU</font></dl>
<p> <code>Features:</code></p>
<dl>
<dt>&quot;savevm-monitor-nodes&quot;</p>
<dd>If present, <font SIZE="-1">HMP</font> command savevm only snapshots monitor-owned nodes if they have no parents. This allows the use of &#8216;savevm&#8217; with -blockdev. (since 4.2)</dl>
<p> <code>Returns:</code> the output of the command as a string <code>Since:</code> 0.14.0 <code>Notes:</code> This command only exists as a stop-gap. Its use is highly discouraged. The semantics of this command are not guaranteed: this means that command names, arguments and responses can change or be removed at <font SIZE="-1">ANY</font> time. Applications that rely on long term stability guarantees should <font SIZE="-1">NOT</font> use this command. Known limitations:</p>
<dl>
<dt>&bull;</p>
<dd>This command is stateless, this means that commands that depend on state information (such as getfd) might not work</p>
<dt>&bull;</p>
<dd>Commands that prompt the user for data don&#8217;t currently work</dl>
<p> <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;human-monitor-command&quot;,<br />
   &quot;arguments&quot; : {&quot;command-line&quot; : &quot;info kvm&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : &quot;kvm support: enabled
&quot;<br />
} <code>change</code> (Command) This command is multiple commands multiplexed together. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>This is normally the name of a block device but it may also be &#8216;vnc&#8217;. when it&#8217;s &#8216;vnc&#8217;, then sub command depends on <tt>&quot;target&quot;</tt></p>
<dt>&quot;target: string&quot;</p>
<dd>If <tt>&quot;device&quot;</tt> is a block device, then this is the new filename. If <tt>&quot;device&quot;</tt> is &#8216;vnc&#8217;, then if the value &#8216;password&#8217; selects the vnc change password command. Otherwise, this specifies a new server <font SIZE="-1">URI</font> address to listen to for <font SIZE="-1">VNC</font> connections.</p>
<dt>&quot;arg: string&quot; (optional)</p>
<dd>If <tt>&quot;device&quot;</tt> is a block device, then this is an optional format to open the device with. If <tt>&quot;device&quot;</tt> is &#8216;vnc&#8217; and <tt>&quot;target&quot;</tt> is &#8216;password&#8217;, this is the new <font SIZE="-1">VNC</font> password to set. See change-vnc-password for additional notes.</dl>
<p> <code>Returns:</code> Nothing on success. If <tt>&quot;device&quot;</tt> is not a valid block device, DeviceNotFound <code>Notes:</code> This interface is deprecated, and it is strongly recommended that you avoid using it. For changing block devices, use blockdev-change-medium; for changing <font SIZE="-1">VNC</font> parameters, use change-vnc-password. <code>Since:</code> 0.14.0 <code>Example:</code> 1. Change a removable medium</p>
<p>        -&gt;{&quot;execute&quot; : &quot;change&quot;,<br />
           &quot;arguments&quot; : {&quot;device&quot; : &quot;ide1-cd0&quot;,<br />
                          &quot;target&quot; : &quot;/srv/images/Fedora-12-x86_64-DVD.iso&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
}</p>
<p>2. Change VNC password</p>
<p>        -&gt;{&quot;execute&quot; : &quot;change&quot;,<br />
           &quot;arguments&quot; : {&quot;device&quot; : &quot;vnc&quot;, &quot;target&quot; : &quot;password&quot;, &quot;arg&quot; : &quot;foobar1&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>xen-set-global-dirty-log</code> (Command) Enable or disable the global dirty log mode. <code>Arguments:</code></p>
<dl>
<dt>&quot;enable: boolean&quot;</p>
<dd>true to enable, false to disable.</dl>
<p> <code>Returns:</code> nothing <code>Since:</code> 1.3 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;xen-set-global-dirty-log&quot;,<br />
   &quot;arguments&quot; : {&quot;enable&quot; : true}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>getfd</code> (Command) Receive a file descriptor via <font SIZE="-1">SCM</font> rights and assign it a name <code>Arguments:</code></p>
<dl>
<dt>&quot;fdname: string&quot;</p>
<dd>file descriptor name</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 0.14.0 <code>Notes:</code> If <tt>&quot;fdname&quot;</tt> already exists, the file descriptor assigned to it will be closed and replaced by the received file descriptor. The &#8216;closefd&#8217; command can be used to explicitly close the file descriptor when it is no longer needed. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;getfd&quot;, &quot;arguments&quot; : {&quot;fdname&quot; : &quot;fd1&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>closefd</code> (Command) Close a file descriptor previously passed via <font SIZE="-1">SCM</font> rights <code>Arguments:</code></p>
<dl>
<dt>&quot;fdname: string&quot;</p>
<dd>file descriptor name</dl>
<p> <code>Returns:</code> Nothing on success <code>Since:</code> 0.14.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;closefd&quot;, &quot;arguments&quot; : {&quot;fdname&quot; : &quot;fd1&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>MemoryInfo</code> (Object) Actual memory information in bytes. <code>Members:</code></p>
<dl>
<dt>&quot;base-memory: int&quot;</p>
<dd>size of &#8220;base&#8221; memory specified with command line option -m.</p>
<dt>&quot;plugged-memory: int&quot; (optional)</p>
<dd>size of memory that can be hot-unplugged. This field is omitted if target doesn&#8217;t support memory hotplug (i.e. <font SIZE="-1">CONFIG_MEM_DEVICE</font> not defined at build time).</dl>
<p> <code>Since:</code> 2.11.0 <code>query-memory-size-summary</code> (Command) Return the amount of initially allocated and present hotpluggable (if enabled) memory in bytes. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-memory-size-summary&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;base-memory&quot; : 4294967296, &quot;plugged-memory&quot; : 0<br />
    }<br />
} <code>Since:</code> 2.11.0 <code>AddfdInfo</code> (Object) Information about a file descriptor that was added to an fd set. <code>Members:</code></p>
<dl>
<dt>&quot;fdset-id: int&quot;</p>
<dd>The <font SIZE="-1">ID</font> of the fd set that <tt>&quot;fd&quot;</tt> was added to.</p>
<dt>&quot;fd: int&quot;</p>
<dd>The file descriptor that was received via <font SIZE="-1">SCM</font> rights and added to the fd set.</dl>
<p> <code>Since:</code> 1.2.0 <code>add-fd</code> (Command) Add a file descriptor, that was passed via <font SIZE="-1">SCM</font> rights, to an fd set. <code>Arguments:</code></p>
<dl>
<dt>&quot;fdset-id: int&quot; (optional)</p>
<dd>The <font SIZE="-1">ID</font> of the fd set to add the file descriptor to.</p>
<dt>&quot;opaque: string&quot; (optional)</p>
<dd>A free-form string that can be used to describe the fd.</dl>
<p> <code>Returns:</code> <tt>&quot;AddfdInfo&quot;</tt> on success If file descriptor was not received, FdNotSupplied If <tt>&quot;fdset-id&quot;</tt> is a negative value, InvalidParameterValue <code>Notes:</code> The list of fd sets is shared by all monitor connections. If <tt>&quot;fdset-id&quot;</tt> is not specified, a new fd set will be created. <code>Since:</code> 1.2.0 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;add-fd&quot;, &quot;arguments&quot; : {&quot;fdset-id&quot; : 1}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;fdset-id&quot; : 1, &quot;fd&quot; : 3<br />
    }<br />
} <code>remove-fd</code> (Command) Remove a file descriptor from an fd set. <code>Arguments:</code></p>
<dl>
<dt>&quot;fdset-id: int&quot;</p>
<dd>The <font SIZE="-1">ID</font> of the fd set that the file descriptor belongs to.</p>
<dt>&quot;fd: int&quot; (optional)</p>
<dd>The file descriptor that is to be removed.</dl>
<p> <code>Returns:</code> Nothing on success If <tt>&quot;fdset-id&quot;</tt> or <tt>&quot;fd&quot;</tt> is not found, FdNotFound <code>Since:</code> 1.2.0 <code>Notes:</code> The list of fd sets is shared by all monitor connections. If <tt>&quot;fd&quot;</tt> is not specified, all file descriptors in <tt>&quot;fdset-id&quot;</tt> will be removed. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;remove-fd&quot;, &quot;arguments&quot; : {&quot;fdset-id&quot; : 1, &quot;fd&quot; : 3}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>FdsetFdInfo</code> (Object) Information about a file descriptor that belongs to an fd set. <code>Members:</code></p>
<dl>
<dt>&quot;fd: int&quot;</p>
<dd>The file descriptor value.</p>
<dt>&quot;opaque: string&quot; (optional)</p>
<dd>A free-form string that can be used to describe the fd.</dl>
<p> <code>Since:</code> 1.2.0 <code>FdsetInfo</code> (Object) Information about an fd set. <code>Members:</code></p>
<dl>
<dt>&quot;fdset-id: int&quot;</p>
<dd>The <font SIZE="-1">ID</font> of the fd set.</p>
<dt>&quot;fds: array of FdsetFdInfo&quot;</p>
<dd>A list of file descriptors that belong to this fd set.</dl>
<p> <code>Since:</code> 1.2.0 <code>query-fdsets</code> (Command) Return information describing all fd sets. <code>Returns:</code> A list of <tt>&quot;FdsetInfo&quot;</tt> <code>Since:</code> 1.2.0 <code>Note:</code> The list of fd sets is shared by all monitor connections. <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-fdsets&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;fds&quot; : [<br />
                {<br />
                    &quot;fd&quot; : 30,<br />
                    &quot;opaque&quot; : &quot;rdonly:/path/to/file&quot;<br />
                },<br />
                {<br />
                    &quot;fd&quot; : 24,<br />
                    &quot;opaque&quot; : &quot;rdwr:/path/to/file&quot;<br />
                }<br />
            ],<br />
            &quot;fdset-id&quot; : 1<br />
        },<br />
        {<br />
            &quot;fds&quot; : [<br />
                {<br />
                    &quot;fd&quot; : 28<br />
                },<br />
                {<br />
                    &quot;fd&quot; : 29<br />
                }<br />
            ],<br />
            &quot;fdset-id&quot; : 0<br />
        }<br />
    ]<br />
} <code>AcpiTableOptions</code> (Object) Specify an <font SIZE="-1">ACPI</font> table on the command line to load. At most one of <tt>&quot;file&quot;</tt> and <tt>&quot;data&quot;</tt> can be specified. The list of files specified by any one of them is loaded and concatenated in order. If both are omitted, <tt>&quot;data&quot;</tt> is implied. Other fields / optargs can be used to override fields of the generic <font SIZE="-1">ACPI</font> table header; refer to the <font SIZE="-1">ACPI</font> specification 5.0, section 5.2.6 System Description Table Header. If a header field is not overridden, then the corresponding value from the concatenated blob is used (in case of <tt>&quot;file&quot;</tt>), or it is filled in with a hard-coded value (in case of <tt>&quot;data&quot;</tt>). String fields are copied into the matching <font SIZE="-1">ACPI</font> member from lowest address upwards, and silently truncated / NUL-padded to length. <code>Members:</code></p>
<dl>
<dt>&quot;sig: string&quot; (optional)</p>
<dd>table signature / identifier (4 bytes)</p>
<dt>&quot;rev: int&quot; (optional)</p>
<dd>table revision number (dependent on signature, 1 byte)</p>
<dt>&quot;oem_id: string&quot; (optional)</p>
<dd><font SIZE="-1">OEM</font> identifier (6 bytes)</p>
<dt>&quot;oem_table_id: string&quot; (optional)</p>
<dd><font SIZE="-1">OEM</font> table identifier (8 bytes)</p>
<dt>&quot;oem_rev: int&quot; (optional)</p>
<dd>OEM-supplied revision number (4 bytes)</p>
<dt>&quot;asl_compiler_id: string&quot; (optional)</p>
<dd>identifier of the utility that created the table (4 bytes)</p>
<dt>&quot;asl_compiler_rev: int&quot; (optional)</p>
<dd>revision number of the utility that created the table (4 bytes)</p>
<dt>&quot;file: string&quot; (optional)</p>
<dd>colon (:) separated list of pathnames to load and concatenate as table data. The resultant binary blob is expected to have an <font SIZE="-1">ACPI</font> table header. At least one file is required. This field excludes <tt>&quot;data&quot;</tt>.</p>
<dt>&quot;data: string&quot; (optional)</p>
<dd>colon (:) separated list of pathnames to load and concatenate as table data. The resultant binary blob must not have an <font SIZE="-1">ACPI</font> table header. At least one file is required. This field excludes <tt>&quot;file&quot;</tt>.</dl>
<p> <code>Since:</code> 1.5 <code>CommandLineParameterType</code> (Enum) Possible types for an option parameter. <code>Values:</code></p>
<dl>
<dt>&quot;string&quot;</p>
<dd>accepts a character string</p>
<dt>&quot;boolean&quot;</p>
<dd>accepts &#8220;on&#8221; or &#8220;off&#8221;</p>
<dt>&quot;number&quot;</p>
<dd>accepts a number</p>
<dt>&quot;size&quot;</p>
<dd>accepts a number followed by an optional suffix (K)ilo, (M)ega, (G)iga, (T)era</dl>
<p> <code>Since:</code> 1.5 <code>CommandLineParameterInfo</code> (Object) Details about a single parameter of a command line option. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot;</p>
<dd>parameter name</p>
<dt>&quot;type: CommandLineParameterType&quot;</p>
<dd>parameter <tt>&quot;CommandLineParameterType&quot;</tt></p>
<dt>&quot;help: string&quot; (optional)</p>
<dd>human readable text string, not suitable for parsing.</p>
<dt>&quot;default: string&quot; (optional)</p>
<dd>default value string (since 2.1)</dl>
<p> <code>Since:</code> 1.5 <code>CommandLineOptionInfo</code> (Object) Details about a command line option, including its list of parameter details <code>Members:</code></p>
<dl>
<dt>&quot;option: string&quot;</p>
<dd>option name</p>
<dt>&quot;parameters: array of CommandLineParameterInfo&quot;</p>
<dd>an array of <tt>&quot;CommandLineParameterInfo&quot;</tt></dl>
<p> <code>Since:</code> 1.5 <code>query-command-line-options</code> (Command) Query command line option schema. <code>Arguments:</code></p>
<dl>
<dt>&quot;option: string&quot; (optional)</p>
<dd>option name</dl>
<p> <code>Returns:</code> list of <tt>&quot;CommandLineOptionInfo&quot;</tt> for all options (or for the given <tt>&quot;option&quot;</tt>). Returns an error if the given <tt>&quot;option&quot;</tt> doesn&#8217;t exist. <code>Since:</code> 1.5 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-command-line-options&quot;,<br />
   &quot;arguments&quot; : {&quot;option&quot; : &quot;option-rom&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [<br />
        {<br />
            &quot;parameters&quot; : [<br />
                {<br />
                    &quot;name&quot; : &quot;romfile&quot;,<br />
                    &quot;type&quot; : &quot;string&quot;<br />
                },<br />
                {<br />
                    &quot;name&quot; : &quot;bootindex&quot;,<br />
                    &quot;type&quot; : &quot;number&quot;<br />
                }<br />
            ],<br />
            &quot;option&quot; : &quot;option-rom&quot;<br />
        }<br />
    ]<br />
} <code>PCDIMMDeviceInfo</code> (Object) PCDIMMDevice state information <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot; (optional)</p>
<dd>device&#8217;s <font SIZE="-1">ID</font></p>
<dt>&quot;addr: int&quot;</p>
<dd>physical address, where device is mapped</p>
<dt>&quot;size: int&quot;</p>
<dd>size of memory that the device provides</p>
<dt>&quot;slot: int&quot;</p>
<dd>slot number at which device is plugged in</p>
<dt>&quot;node: int&quot;</p>
<dd><font SIZE="-1">NUMA</font> node number where device is plugged in</p>
<dt>&quot;memdev: string&quot;</p>
<dd>memory backend linked with device</p>
<dt>&quot;hotplugged: boolean&quot;</p>
<dd>true if device was hotplugged</p>
<dt>&quot;hotpluggable: boolean&quot;</p>
<dd>true if device if could be added/removed while machine is running</dl>
<p> <code>Since:</code> 2.1 <code>VirtioPMEMDeviceInfo</code> (Object) VirtioPMEM state information <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot; (optional)</p>
<dd>device&#8217;s <font SIZE="-1">ID</font></p>
<dt>&quot;memaddr: int&quot;</p>
<dd>physical address in memory, where device is mapped</p>
<dt>&quot;size: int&quot;</p>
<dd>size of memory that the device provides</p>
<dt>&quot;memdev: string&quot;</p>
<dd>memory backend linked with device</dl>
<p> <code>Since:</code> 4.1 <code>MemoryDeviceInfo</code> (Object) Union containing information about a memory device nvdimm is included since 2.12. virtio-pmem is included since 4.1. <code>Members:</code></p>
<dl>
<dt>&quot;type&quot;</p>
<dd>One of &#8220;dimm&#8221;, &#8220;nvdimm&#8221;, &#8220;virtio-pmem&#8221;</p>
<dt>&quot;data: PCDIMMDeviceInfo&quot; when &quot;type&quot; is &quot;dimm&quot;</p>
<dd>
<dt>&quot;data: PCDIMMDeviceInfo&quot; when &quot;type&quot; is &quot;nvdimm&quot;</p>
<dd>
<dt>&quot;data: VirtioPMEMDeviceInfo&quot; when &quot;type&quot; is &quot;virtio-pmem&quot;</p>
<dd></dl>
<p> <code>Since:</code> 2.1 <code>query-memory-devices</code> (Command) Lists available memory devices and their state <code>Since:</code> 2.1 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-memory-devices&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [ {&quot;data&quot; :<br />
                      {&quot;addr&quot; : 5368709120,<br />
                       &quot;hotpluggable&quot; : true,<br />
                       &quot;hotplugged&quot; : true,<br />
                       &quot;id&quot; : &quot;d1&quot;,<br />
                       &quot;memdev&quot; : &quot;/objects/memX&quot;,<br />
                       &quot;node&quot; : 0,<br />
                       &quot;size&quot; : 1073741824,<br />
                       &quot;slot&quot; : 0},<br />
                  &quot;type&quot; : &quot;dimm&quot;} ]<br />
} <font SIZE="-1"><code>MEM_UNPLUG_ERROR</code></font> (Event) Emitted when memory hot unplug error occurs. <code>Arguments:</code></p>
<dl>
<dt>&quot;device: string&quot;</p>
<dd>device name</p>
<dt>&quot;msg: string&quot;</p>
<dd>Informative message</dl>
<p> <code>Since:</code> 2.4 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;MEM_UNPLUG_ERROR&quot;
 &quot;data&quot;: { &quot;device&quot;: &quot;dimm1&quot;,
 &quot;msg&quot;: &quot;acpi: device unplug for unsupported device&quot;
 },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1265044230, &quot;microseconds&quot;: 450486 } }</pre>
<p><code>ACPISlotType</code> (Enum) <code>Values:</code></p>
<dl>
<dt>&quot;DIMM&quot;</p>
<dd>memory slot</p>
<dt>&quot;CPU&quot;</p>
<dd>logical <font SIZE="-1">CPU</font> slot (since 2.7)</dl>
<p> <code>ACPIOSTInfo</code> (Object) <font SIZE="-1">OSPM</font> Status Indication for a device For description of possible values of <tt>&quot;source&quot;</tt> and <tt>&quot;status&quot;</tt> fields see &#8220;_OST (<font SIZE="-1">OSPM</font> Status Indication)&#8221; chapter of <font SIZE="-1">ACPI5.0</font> spec. <code>Members:</code></p>
<dl>
<dt>&quot;device: string&quot; (optional)</p>
<dd>device <font SIZE="-1">ID</font> associated with slot</p>
<dt>&quot;slot: string&quot;</p>
<dd>slot <font SIZE="-1">ID,</font> unique per slot of a given <tt>&quot;slot-type&quot;</tt></p>
<dt>&quot;slot-type: ACPISlotType&quot;</p>
<dd>type of the slot</p>
<dt>&quot;source: int&quot;</p>
<dd>an integer containing the source event</p>
<dt>&quot;status: int&quot;</p>
<dd>an integer containing the status code</dl>
<p> <code>Since:</code> 2.1 <code>query-acpi-ospm-status</code> (Command) Return a list of ACPIOSTInfo for devices that support status reporting via <font SIZE="-1">ACPI _OST</font> method. <code>Since:</code> 2.1 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-acpi-ospm-status&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot; : [ {&quot;device&quot; : &quot;d1&quot;, &quot;slot&quot; : &quot;0&quot;, &quot;slot-type&quot; : &quot;DIMM&quot;, &quot;source&quot; : 1, &quot;status&quot; : 0},<br />
                 {&quot;slot&quot; : &quot;1&quot;, &quot;slot-type&quot; : &quot;DIMM&quot;, &quot;source&quot; : 0, &quot;status&quot; : 0},<br />
                 {&quot;slot&quot; : &quot;2&quot;, &quot;slot-type&quot; : &quot;DIMM&quot;, &quot;source&quot; : 0, &quot;status&quot; : 0},<br />
                 {&quot;slot&quot; : &quot;3&quot;, &quot;slot-type&quot; : &quot;DIMM&quot;, &quot;source&quot; : 0, &quot;status&quot; : 0} ]<br />
} <font SIZE="-1"><code>ACPI_DEVICE_OST</code></font> (Event) Emitted when guest executes <font SIZE="-1">ACPI _OST</font> method. <code>Arguments:</code></p>
<dl>
<dt>&quot;info: ACPIOSTInfo&quot;</p>
<dd><font SIZE="-1">OSPM</font> Status Indication</dl>
<p> <code>Since:</code> 2.1 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;ACPI_DEVICE_OST&quot;,
 &quot;data&quot;: { &quot;device&quot;: &quot;d1&quot;, &quot;slot&quot;: &quot;0&quot;,
 &quot;slot-type&quot;: &quot;DIMM&quot;, &quot;source&quot;: 1, &quot;status&quot;: 0 } }</pre>
<p><code>ReplayMode</code> (Enum) Mode of the replay subsystem. <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>normal execution mode. Replay or record are not enabled.</p>
<dt>&quot;record&quot;</p>
<dd>record mode. All non-deterministic data is written into the replay log.</p>
<dt>&quot;play&quot;</p>
<dd>replay mode. Non-deterministic data required for system execution is read from the log.</dl>
<p> <code>Since:</code> 2.5 <code>xen-load-devices-state</code> (Command) Load the state of all devices from file. The <font SIZE="-1">RAM</font> and the block devices of the <font SIZE="-1">VM</font> are not loaded by this command. <code>Arguments:</code></p>
<dl>
<dt>&quot;filename: string&quot;</p>
<dd>the file to load the state of the devices from as binary data. See xen-save-devices-state.txt for a description of the binary format.</dl>
<p> <code>Since:</code> 2.7 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;xen-load-devices-state&quot;,<br />
   &quot;arguments&quot; : {&quot;filename&quot; : &quot;/tmp/resume&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>GuidInfo</code> (Object) <font SIZE="-1">GUID</font> information. <code>Members:</code></p>
<dl>
<dt>&quot;guid: string&quot;</p>
<dd>the globally unique identifier</dl>
<p> <code>Since:</code> 2.9 <code>query-vm-generation-id</code> (Command) Show Virtual Machine Generation <font SIZE="-1">ID</font> <code>Since:</code> 2.9 <font SIZE="-1"><code>RTC_CHANGE</code></font> (Event) Emitted when the guest changes the <font SIZE="-1">RTC</font> time. <code>Arguments:</code></p>
<dl>
<dt>&quot;offset: int&quot;</p>
<dd>offset between base <font SIZE="-1">RTC</font> clock (as specified by -rtc base), and new <font SIZE="-1">RTC</font> clock value</dl>
<p> <code>Note:</code> This event is rate-limited. <code>Since:</code> 0.13.0 <code>Example:</code> </p>
<pre> &lt;- { &quot;event&quot;: &quot;RTC_CHANGE&quot;,
 &quot;data&quot;: { &quot;offset&quot;: 78 },
 &quot;timestamp&quot;: { &quot;seconds&quot;: 1267020223, &quot;microseconds&quot;: 435656 } }</pre>
<p><code>If:</code> <tt>&quot;defined(TARGET_ALPHA) || defined(TARGET_ARM) || defined(TARGET_HPPA) || defined(TARGET_I386) || defined(TARGET_MIPS) || defined(TARGET_MIPS64) || defined(TARGET_MOXIE) || defined(TARGET_PPC) || defined(TARGET_PPC64) || defined(TARGET_S390X) || defined(TARGET_SH4) || defined(TARGET_SPARC)&quot;</tt> <code>rtc-reset-reinjection</code> (Command) This command will reset the <font SIZE="-1">RTC</font> interrupt reinjection backlog. Can be used if another mechanism to synchronize guest time is in effect, for example <font SIZE="-1">QEMU</font> guest agent&#8217;s guest-set-time command. <code>Since:</code> 2.1 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;rtc-reset-reinjection&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>If:</code> <tt>&quot;defined(TARGET_I386)&quot;</tt> <code>SevState</code> (Enum) An enumeration of <font SIZE="-1">SEV</font> state information used during <tt>&quot;query-sev&quot;</tt>. <code>Values:</code></p>
<dl>
<dt>&quot;uninit&quot;</p>
<dd>The guest is uninitialized.</p>
<dt>&quot;launch-update&quot;</p>
<dd>The guest is currently being launched; plaintext data and register state is being imported.</p>
<dt>&quot;launch-secret&quot;</p>
<dd>The guest is currently being launched; ciphertext data is being imported.</p>
<dt>&quot;running&quot;</p>
<dd>The guest is fully launched or migrated in.</p>
<dt>&quot;send-update&quot;</p>
<dd>The guest is currently being migrated out to another machine.</p>
<dt>&quot;receive-update&quot;</p>
<dd>The guest is currently being migrated from another machine.</dl>
<p> <code>Since:</code> 2.12 <code>If:</code> <tt>&quot;defined(TARGET_I386)&quot;</tt> <code>SevInfo</code> (Object) Information about Secure Encrypted Virtualization (<font SIZE="-1">SEV</font>) support <code>Members:</code></p>
<dl>
<dt>&quot;enabled: boolean&quot;</p>
<dd>true if <font SIZE="-1">SEV</font> is active</p>
<dt>&quot;api-major: int&quot;</p>
<dd><font SIZE="-1">SEV API</font> major version</p>
<dt>&quot;api-minor: int&quot;</p>
<dd><font SIZE="-1">SEV API</font> minor version</p>
<dt>&quot;build-id: int&quot;</p>
<dd><font SIZE="-1">SEV FW</font> build id</p>
<dt>&quot;policy: int&quot;</p>
<dd><font SIZE="-1">SEV</font> policy value</p>
<dt>&quot;state: SevState&quot;</p>
<dd><font SIZE="-1">SEV</font> guest state</p>
<dt>&quot;handle: int&quot;</p>
<dd><font SIZE="-1">SEV</font> firmware handle</dl>
<p> <code>Since:</code> 2.12 <code>If:</code> <tt>&quot;defined(TARGET_I386)&quot;</tt> <code>query-sev</code> (Command) Returns information about <font SIZE="-1">SEV</font> <code>Returns:</code> <tt>&quot;SevInfo&quot;</tt> <code>Since:</code> 2.12 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-sev&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;enabled&quot; : true, &quot;api-major&quot; : 0, &quot;api-minor&quot; : 0, &quot;build-id&quot; : 0, &quot;policy&quot; : 0, &quot;state&quot; : &quot;running&quot;, &quot;handle&quot; : 1<br />
    }<br />
} <code>If:</code> <tt>&quot;defined(TARGET_I386)&quot;</tt> <code>SevLaunchMeasureInfo</code> (Object) <font SIZE="-1">SEV</font> Guest Launch measurement information <code>Members:</code></p>
<dl>
<dt>&quot;data: string&quot;</p>
<dd>the measurement value encoded in base64</dl>
<p> <code>Since:</code> 2.12 <code>If:</code> <tt>&quot;defined(TARGET_I386)&quot;</tt> <code>query-sev-launch-measure</code> (Command) Query the <font SIZE="-1">SEV</font> guest launch information. <code>Returns:</code> The <tt>&quot;SevLaunchMeasureInfo&quot;</tt> for the guest <code>Since:</code> 2.12 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-sev-launch-measure&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;data&quot; : &quot;4l8LXeNlSPUDlXPJG5966/8%YZ&quot;<br />
    }<br />
} <code>If:</code> <tt>&quot;defined(TARGET_I386)&quot;</tt> <code>SevCapability</code> (Object) The struct describes capability for a Secure Encrypted Virtualization feature. <code>Members:</code></p>
<dl>
<dt>&quot;pdh: string&quot;</p>
<dd>Platform Diffie-Hellman key (base64 encoded)</p>
<dt>&quot;cert-chain: string&quot;</p>
<dd><font SIZE="-1">PDH</font> certificate chain (base64 encoded)</p>
<dt>&quot;cbitpos: int&quot;</p>
<dd>C-bit location in page table entry</p>
<dt>&quot;reduced-phys-bits: int&quot;</p>
<dd>Number of physical Address bit reduction when <font SIZE="-1">SEV</font> is enabled</dl>
<p> <code>Since:</code> 2.12 <code>If:</code> <tt>&quot;defined(TARGET_I386)&quot;</tt> <code>query-sev-capabilities</code> (Command) This command is used to get the <font SIZE="-1">SEV</font> capabilities, and is supported on <font SIZE="-1">AMD X86</font> platforms only. <code>Returns:</code> SevCapability objects. <code>Since:</code> 2.12 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;query-sev-capabilities&quot;} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
        &quot;pdh&quot; : &quot;8CCDD8DDD&quot;, &quot;cert-chain&quot; : &quot;888CCCDDDEE&quot;, &quot;cbitpos&quot; : 47, &quot;reduced-phys-bits&quot; : 5<br />
    }<br />
} <code>If:</code> <tt>&quot;defined(TARGET_I386)&quot;</tt> <code>dump-skeys</code> (Command) Dump guest&#8217;s storage keys <code>Arguments:</code></p>
<dl>
<dt>&quot;filename: string&quot;</p>
<dd>the path to the file to dump to</dl>
<p> This command is only supported on s390 architecture. <code>Since:</code> 2.5 <code>Example:</code> -&gt;{&quot;execute&quot; : &quot;dump-skeys&quot;,<br />
   &quot;arguments&quot; : {&quot;filename&quot; : &quot;/tmp/skeys&quot;}} &lt; &#8211;<br />
{<br />
    &quot;return&quot;:<br />
    {<br />
    }<br />
} <code>If:</code> <tt>&quot;defined(TARGET_S390X)&quot;</tt> <code>GICCapability</code> (Object) The struct describes capability for a specific <font SIZE="-1">GIC</font> (Generic Interrupt Controller) version. These bits are not only decided by <font SIZE="-1">QEMU/KVM</font> software version, but also decided by the hardware that the program is running upon. <code>Members:</code></p>
<dl>
<dt>&quot;version: int&quot;</p>
<dd>version of <font SIZE="-1">GIC</font> to be described. Currently, only 2 and 3 are supported.</p>
<dt>&quot;emulated: boolean&quot;</p>
<dd>whether current QEMU/hardware supports emulated <font SIZE="-1">GIC</font> device in user space.</p>
<dt>&quot;kernel: boolean&quot;</p>
<dd>whether current QEMU/hardware supports hardware accelerated <font SIZE="-1">GIC</font> device in kernel.</dl>
<p> <code>Since:</code> 2.6 <code>If:</code> <tt>&quot;defined(TARGET_ARM)&quot;</tt> <code>query-gic-capabilities</code> (Command) This command is ARM-only. It will return a list of GICCapability objects that describe its capability bits. <code>Returns:</code> a list of GICCapability objects. <code>Since:</code> 2.6 <code>Example:</code> </p>
<pre><code>-&gt;{&quot;execute&quot; : &quot;query-gic-capabilities&quot;} &lt; -
{
    &quot;return&quot; : [ {&quot;version&quot; : 2, &quot;emulated&quot; : true, &quot;kernel&quot; : false},
                 {&quot;version&quot; : 3, &quot;emulated&quot; : false, &quot;kernel&quot; : true} ]
}</code></pre>
<p> <code>If:</code> <tt>&quot;defined(TARGET_ARM)&quot;</tt> <code>AudiodevPerDirectionOptions</code> (Object) General audio backend options that are used for both playback and recording. <code>Members:</code></p>
<dl>
<dt>&quot;mixing-engine: boolean&quot; (optional)</p>
<dd>use <font SIZE="-1">QEMU</font>&#8216;s mixing engine to mix all streams inside <font SIZE="-1">QEMU</font> and convert audio formats when not supported by the backend. When set to off, fixed-settings must be also off (default on, since 4.2)</p>
<dt>&quot;fixed-settings: boolean&quot; (optional)</p>
<dd>use fixed settings for host input/output. When off, frequency, channels and format must not be specified (default true)</p>
<dt>&quot;frequency: int&quot; (optional)</p>
<dd>frequency to use when using fixed settings (default 44100)</p>
<dt>&quot;channels: int&quot; (optional)</p>
<dd>number of channels when using fixed settings (default 2)</p>
<dt>&quot;voices: int&quot; (optional)</p>
<dd>number of voices to use (default 1)</p>
<dt>&quot;format: AudioFormat&quot; (optional)</p>
<dd>sample format to use when using fixed settings (default s16)</p>
<dt>&quot;buffer-length: int&quot; (optional)</p>
<dd>the buffer length in microseconds</dl>
<p> <code>Since:</code> 4.0 <code>AudiodevGenericOptions</code> (Object) Generic driver-specific options. <code>Members:</code></p>
<dl>
<dt>&quot;in: AudiodevPerDirectionOptions&quot; (optional)</p>
<dd>options of the capture stream</p>
<dt>&quot;out: AudiodevPerDirectionOptions&quot; (optional)</p>
<dd>options of the playback stream</dl>
<p> <code>Since:</code> 4.0 <code>AudiodevAlsaPerDirectionOptions</code> (Object) Options of the <font SIZE="-1">ALSA</font> backend that are used for both playback and recording. <code>Members:</code></p>
<dl>
<dt>&quot;dev: string&quot; (optional)</p>
<dd>the name of the <font SIZE="-1">ALSA</font> device to use (default &#8216;default&#8217;)</p>
<dt>&quot;period-length: int&quot; (optional)</p>
<dd>the period length in microseconds</p>
<dt>&quot;try-poll: boolean&quot; (optional)</p>
<dd>attempt to use poll mode, falling back to non-polling access on failure (default true)</p>
<dt>The members of &quot;AudiodevPerDirectionOptions&quot;</p>
<dd></dl>
<p> <code>Since:</code> 4.0 <code>AudiodevAlsaOptions</code> (Object) Options of the <font SIZE="-1">ALSA</font> audio backend. <code>Members:</code></p>
<dl>
<dt>&quot;in: AudiodevAlsaPerDirectionOptions&quot; (optional)</p>
<dd>options of the capture stream</p>
<dt>&quot;out: AudiodevAlsaPerDirectionOptions&quot; (optional)</p>
<dd>options of the playback stream</p>
<dt>&quot;threshold: int&quot; (optional)</p>
<dd>set the threshold (in microseconds) when playback starts</dl>
<p> <code>Since:</code> 4.0 <code>AudiodevCoreaudioPerDirectionOptions</code> (Object) Options of the Core Audio backend that are used for both playback and recording. <code>Members:</code></p>
<dl>
<dt>&quot;buffer-count: int&quot; (optional)</p>
<dd>number of buffers</p>
<dt>The members of &quot;AudiodevPerDirectionOptions&quot;</p>
<dd></dl>
<p> <code>Since:</code> 4.0 <code>AudiodevCoreaudioOptions</code> (Object) Options of the coreaudio audio backend. <code>Members:</code></p>
<dl>
<dt>&quot;in: AudiodevCoreaudioPerDirectionOptions&quot; (optional)</p>
<dd>options of the capture stream</p>
<dt>&quot;out: AudiodevCoreaudioPerDirectionOptions&quot; (optional)</p>
<dd>options of the playback stream</dl>
<p> <code>Since:</code> 4.0 <code>AudiodevDsoundOptions</code> (Object) Options of the DirectSound audio backend. <code>Members:</code></p>
<dl>
<dt>&quot;in: AudiodevPerDirectionOptions&quot; (optional)</p>
<dd>options of the capture stream</p>
<dt>&quot;out: AudiodevPerDirectionOptions&quot; (optional)</p>
<dd>options of the playback stream</p>
<dt>&quot;latency: int&quot; (optional)</p>
<dd>add extra latency to playback in microseconds (default 10000)</dl>
<p> <code>Since:</code> 4.0 <code>AudiodevOssPerDirectionOptions</code> (Object) Options of the <font SIZE="-1">OSS</font> backend that are used for both playback and recording. <code>Members:</code></p>
<dl>
<dt>&quot;dev: string&quot; (optional)</p>
<dd>file name of the <font SIZE="-1">OSS</font> device (default &#8216;/dev/dsp&#8217;)</p>
<dt>&quot;buffer-count: int&quot; (optional)</p>
<dd>number of buffers</p>
<dt>&quot;try-poll: boolean&quot; (optional)</p>
<dd>attempt to use poll mode, falling back to non-polling access on failure (default true)</p>
<dt>The members of &quot;AudiodevPerDirectionOptions&quot;</p>
<dd></dl>
<p> <code>Since:</code> 4.0 <code>AudiodevOssOptions</code> (Object) Options of the <font SIZE="-1">OSS</font> audio backend. <code>Members:</code></p>
<dl>
<dt>&quot;in: AudiodevOssPerDirectionOptions&quot; (optional)</p>
<dd>options of the capture stream</p>
<dt>&quot;out: AudiodevOssPerDirectionOptions&quot; (optional)</p>
<dd>options of the playback stream</p>
<dt>&quot;try-mmap: boolean&quot; (optional)</p>
<dd>try using memory-mapped access, falling back to non-memory-mapped access on failure (default true)</p>
<dt>&quot;exclusive: boolean&quot; (optional)</p>
<dd>open device in exclusive mode (vmix won&#8217;t work) (default false)</p>
<dt>&quot;dsp-policy: int&quot; (optional)</p>
<dd>set the timing policy of the device (between 0 and 10, where smaller number means smaller latency but higher <font SIZE="-1">CPU</font> usage) or -1 to use fragment mode (option ignored on some platforms) (default 5)</dl>
<p> <code>Since:</code> 4.0 <code>AudiodevPaPerDirectionOptions</code> (Object) Options of the Pulseaudio backend that are used for both playback and recording. <code>Members:</code></p>
<dl>
<dt>&quot;name: string&quot; (optional)</p>
<dd>name of the sink/source to use</p>
<dt>&quot;stream-name: string&quot; (optional)</p>
<dd>name of the PulseAudio stream created by qemu. Can be used to identify the stream in PulseAudio when you create multiple PulseAudio devices or run multiple qemu instances (default: audiodev&#8217;s id, since 4.2)</p>
<dt>&quot;latency: int&quot; (optional)</p>
<dd>latency you want PulseAudio to achieve in microseconds (default 15000)</p>
<dt>The members of &quot;AudiodevPerDirectionOptions&quot;</p>
<dd></dl>
<p> <code>Since:</code> 4.0 <code>AudiodevPaOptions</code> (Object) Options of the PulseAudio audio backend. <code>Members:</code></p>
<dl>
<dt>&quot;in: AudiodevPaPerDirectionOptions&quot; (optional)</p>
<dd>options of the capture stream</p>
<dt>&quot;out: AudiodevPaPerDirectionOptions&quot; (optional)</p>
<dd>options of the playback stream</p>
<dt>&quot;server: string&quot; (optional)</p>
<dd>PulseAudio server address (default: let PulseAudio choose)</dl>
<p> <code>Since:</code> 4.0 <code>AudiodevWavOptions</code> (Object) Options of the wav audio backend. <code>Members:</code></p>
<dl>
<dt>&quot;in: AudiodevPerDirectionOptions&quot; (optional)</p>
<dd>options of the capture stream</p>
<dt>&quot;out: AudiodevPerDirectionOptions&quot; (optional)</p>
<dd>options of the playback stream</p>
<dt>&quot;path: string&quot; (optional)</p>
<dd>name of the wav file to record (default &#8216;qemu.wav&#8217;)</dl>
<p> <code>Since:</code> 4.0 <code>AudioFormat</code> (Enum) An enumeration of possible audio formats. <code>Values:</code></p>
<dl>
<dt>&quot;u8&quot;</p>
<dd>Not documented</p>
<dt>&quot;s8&quot;</p>
<dd>Not documented</p>
<dt>&quot;u16&quot;</p>
<dd>Not documented</p>
<dt>&quot;s16&quot;</p>
<dd>Not documented</p>
<dt>&quot;u32&quot;</p>
<dd>Not documented</p>
<dt>&quot;s32&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 4.0 <code>AudiodevDriver</code> (Enum) An enumeration of possible audio backend drivers. <code>Values:</code></p>
<dl>
<dt>&quot;none&quot;</p>
<dd>Not documented</p>
<dt>&quot;alsa&quot;</p>
<dd>Not documented</p>
<dt>&quot;coreaudio&quot;</p>
<dd>Not documented</p>
<dt>&quot;dsound&quot;</p>
<dd>Not documented</p>
<dt>&quot;oss&quot;</p>
<dd>Not documented</p>
<dt>&quot;pa&quot;</p>
<dd>Not documented</p>
<dt>&quot;sdl&quot;</p>
<dd>Not documented</p>
<dt>&quot;spice&quot;</p>
<dd>Not documented</p>
<dt>&quot;wav&quot;</p>
<dd>Not documented</dl>
<p> <code>Since:</code> 4.0 <code>Audiodev</code> (Object) Options of an audio backend. <code>Members:</code></p>
<dl>
<dt>&quot;id: string&quot;</p>
<dd>identifier of the backend</p>
<dt>&quot;driver: AudiodevDriver&quot;</p>
<dd>the backend driver to use</p>
<dt>&quot;timer-period: int&quot; (optional)</p>
<dd>timer period (in microseconds, 0: use lowest possible)</p>
<dt>The members of &quot;AudiodevGenericOptions&quot; when &quot;driver&quot; is &quot;none&quot;</p>
<dd>
<dt>The members of &quot;AudiodevAlsaOptions&quot; when &quot;driver&quot; is &quot;alsa&quot;</p>
<dd>
<dt>The members of &quot;AudiodevCoreaudioOptions&quot; when &quot;driver&quot; is &quot;coreaudio&quot;</p>
<dd>
<dt>The members of &quot;AudiodevDsoundOptions&quot; when &quot;driver&quot; is &quot;dsound&quot;</p>
<dd>
<dt>The members of &quot;AudiodevOssOptions&quot; when &quot;driver&quot; is &quot;oss&quot;</p>
<dd>
<dt>The members of &quot;AudiodevPaOptions&quot; when &quot;driver&quot; is &quot;pa&quot;</p>
<dd>
<dt>The members of &quot;AudiodevGenericOptions&quot; when &quot;driver&quot; is &quot;sdl&quot;</p>
<dd>
<dt>The members of &quot;AudiodevGenericOptions&quot; when &quot;driver&quot; is &quot;spice&quot;</p>
<dd>
<dt>The members of &quot;AudiodevWavOptions&quot; when &quot;driver&quot; is &quot;wav&quot;</p>
<dd></dl>
<p> <code>Since:</code> 4.0 </p>
