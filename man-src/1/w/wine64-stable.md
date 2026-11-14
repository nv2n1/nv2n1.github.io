---
title: "wine64-stable(1)"
name: "wine64-stable"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wine64-stable/"
description: "wine – run Windows programs on Unix"
---

<h2 class="name">NAME</h2>
<p> wine &#8211; run Windows programs on Unix </p>
<h2>SYNOPSIS</h2>
<p> <code>wine</code> <i>program </i>[<i>arguments</i>]<br />
 <code>wine &#8211;help</code><br />
 <code>wine &#8211;version</code> </p>
<p> For instructions on passing arguments to Windows programs, please see the <code>PROGRAM/ARGUMENTS</code> section of the man page.</p>
<h2>DESCRIPTION</h2>
<p> <code>wine</code> loads and runs the given program, which can be a DOS, Windows 3.x, Win32 or Win64 executable (on 64-bit systems). </p>
<p> For debugging wine, use <code>winedbg</code> instead. </p>
<p> For running CUI executables (Windows console programs), use <code>wineconsole</code> instead of <code>wine</code>. This will display the output in a separate window. Not using <code>wineconsole</code> for CUI programs will only provide very limited console support, and your program might not function properly. </p>
<p> When invoked with <code>&#8211;help</code> or <code>&#8211;version</code> as the only argument, <code>wine</code> will simply print a small help message or its version respectively and exit.</p>
<h2>PROGRAM/ARGUMENTS</h2>
<p> The program name may be specified in DOS format (<i>C:\WINDOWS\SOL.EXE</i>) or in Unix format (<i>/msdos/windows/sol.exe</i>). You may pass arguments to the program being executed by adding them to the end of the command line invoking <code>wine</code> (such as: <i>wine notepad C:\TEMP\README.TXT</i>). Note that you need to &#8216;\&#8217; escape special characters (and spaces) when invoking Wine via a shell, e.g. </p>
<p> wine C:\Program\ Files\MyPrg\test.exe </p>
<p> It can also be one of the Windows executables shipped with Wine, in which case specifying the full path is not mandatory, e.g. <i>wine explorer</i> or <i>wine notepad</i>. </p>
<h2>ENVIRONMENT</h2>
<p> <code>wine</code> makes the environment variables of the shell from which it is started accessible to the Windows/DOS processes started. So use the appropriate syntax for your shell to enter environment variables you need.</p>
<dl>
<dt><code>WINEPREFIX</code></p>
<dd> If set, the contents of this variable is taken as the name of the directory where Wine stores its data (the default is <i>$HOME/.wine</i>). This directory is also used to identify the socket which is used to communicate with the <code>wineserver</code>. All <code>wine</code> processes using the same <code>wineserver</code> (i.e.: same user) share certain things like registry, shared memory, and config file. By setting <code>WINEPREFIX</code> to different values for different <code>wine</code> processes, it is possible to run a number of truly independent <code>wine</code> processes.</p>
<dt><code>WINESERVER</code></p>
<dd> Specifies the path and name of the <code>wineserver</code> binary. If not set, Wine will try to load <i>/usr/lib/wine/wineserver</i>, and if this doesn&#8217;t exist it will then look for a file named &quot;wineserver&quot; in the path and in a few other likely locations.</p>
<dt><code>WINELOADER</code></p>
<dd> Specifies the path and name of the <code>wine</code> binary to use to launch new Windows processes. If not set, Wine will try to load <i>/usr/lib/wine/wine</i>, and if this doesn&#8217;t exist it will then look for a file named &quot;wine&quot; in the path and in a few other likely locations.</p>
<dt><code>WINEDEBUG</code></p>
<dd> Turns debugging messages on or off. The syntax of the variable is of the form [<i>class</i>][<code>+</code>|<code>&#8211;</code>]<i>channel</i>[,[<i>class2</i>][<code>+</code>|<code>&#8211;</code>]<i>channel2</i>]</p>
<dl>
<dt>
<dd>
<p> <i>class</i> is optional and can be one of the following: <code>err</code>, <code>warn</code>, <code>fixme</code>, or <code>trace</code>. If <i>class</i> is not specified, all debugging messages for the specified channel are turned on. Each channel will print messages about a particular component of Wine. The following character can be either <code>+</code> or <code>&#8211;</code> to switch the specified channel on or off respectively. If there is no <i>class</i> part before it, a leading <code>+</code> can be omitted. Note that spaces are not allowed anywhere in the string. </p>
<p> Examples:</p>
<dl>
<dt>WINEDEBUG=warn+all</p>
<dd> will turn on all warning messages (recommended for debugging). </p>
<dt>WINEDEBUG=warn+dll,+heap</p>
<dd> will turn on DLL warning messages and all heap messages. </p>
<dt>WINEDEBUG=fixme-all,warn+cursor,+relay</p>
<dd> will turn off all FIXME messages, turn on cursor warning messages, and turn on all relay messages (API calls). </p>
<dt>WINEDEBUG=relay</p>
<dd> will turn on all relay messages. For more control on including or excluding functions and dlls from the relay trace, look into the <code>HKEY_CURRENT_USER\Software\Wine\Debug</code> registry key.</dl>
<p> For more information on debugging messages, see the <i>Running Wine</i> chapter of the Wine User Guide.</dl>
<dt><code>WINEDLLPATH</code></p>
<dd> Specifies the path(s) in which to search for builtin dlls and Winelib applications. This is a list of directories separated by &quot;:&quot;. In addition to any directory specified in <code>WINEDLLPATH</code>, Wine will also look in <i>/usr/lib/x86_64-linux-gnu/wine</i>.</p>
<dt><code>WINEDLLOVERRIDES</code></p>
<dd> Defines the override type and load order of dlls used in the loading process for any dll. There are currently two types of libraries that can be loaded into a process address space: native windows dlls (<i>native</i>) and Wine internal dlls (<i>builtin</i>). The type may be abbreviated with the first letter of the type (<i>n</i> or <i>b</i>). The library may also be disabled (&#8221;). Each sequence of orders must be separated by commas.</p>
<dl>
<dt>
<dd>
<p> Each dll may have its own specific load order. The load order determines which version of the dll is attempted to be loaded into the address space. If the first fails, then the next is tried and so on. Multiple libraries with the same load order can be separated with commas. It is also possible to use specify different loadorders for different libraries by separating the entries by &quot;;&quot;. </p>
<p> The load order for a 16-bit dll is always defined by the load order of the 32-bit dll that contains it (which can be identified by looking at the symbolic link of the 16-bit .dll.so file). For instance if <i>ole32.dll</i> is configured as builtin, <i>storage.dll</i> will be loaded as builtin too, since the 32-bit <i>ole32.dll</i> contains the 16-bit <i>storage.dll</i>. </p>
<p> Examples:</p>
<dl>
<dt>WINEDLLOVERRIDES=&quot;comdlg32,shell32=n,b&quot;</p>
<dd>
 Try to load comdlg32 and shell32 as native windows dll first and try the builtin version if the native load fails.</p>
<dt>WINEDLLOVERRIDES=&quot;comdlg32,shell32=n;c:\foo\bar\baz=b&quot;</p>
<dd>
 Try to load the libraries comdlg32 and shell32 as native windows dlls. Furthermore, if an application request to load <i>c:ooaraz.dll</i> load the builtin library <i>baz</i>.</p>
<dt>WINEDLLOVERRIDES=&quot;comdlg32=b,n;shell32=b;comctl32=n;oleaut32=&quot;</p>
<dd>
 Try to load comdlg32 as builtin first and try the native version if the builtin load fails; load shell32 always as builtin and comctl32 always as native; oleaut32 will be disabled.</dl>
</dl>
<dt><code>WINEPATH</code></p>
<dd> Specifies additional path(s) to be prepended to the default Windows <code>PATH</code> environment variable. This is a list of Windows-style directories separated by &quot;;&quot;.</p>
<dl>
<dt>
<dd>
<p> For a permanent alternative, edit (create if needed) the <code>PATH</code> value under the <code>HKEY_CURRENT_USER\Environment</code> registry key.</dl>
<dt><code>WINEARCH</code></p>
<dd> Specifies the Windows architecture to support. It can be set either to <code>win32</code> (support only 32-bit applications), or to <code>win64</code> (support both 64-bit applications and 32-bit ones in WoW64 mode).<br />
 The architecture supported by a given Wine prefix is set at prefix creation time and cannot be changed afterwards. When running with an existing prefix, Wine will refuse to start if <code>WINEARCH</code> doesn&#8217;t match the prefix architecture.</p>
<dt><code>DISPLAY</code></p>
<dd> Specifies the X11 display to use.</p>
<dt>OSS sound driver configuration variables:</p>
<dd>
<dt><code>AUDIODEV</code></p>
<dd> Set the device for audio input / output. Default <i>/dev/dsp</i>.</p>
<dt><code>MIXERDEV</code></p>
<dd> Set the device for mixer controls. Default <i>/dev/mixer</i>.</p>
<dt><code>MIDIDEV</code></p>
<dd> Set the MIDI (sequencer) device. Default <i>/dev/sequencer</i>.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/lib/wine/wine</i></p>
<dd> The Wine program loader.</p>
<dt><i>/usr/lib/wine/wineconsole</i></p>
<dd> The Wine program loader for CUI (console) applications.</p>
<dt><i>/usr/lib/wine/wineserver</i></p>
<dd> The Wine server</p>
<dt><i>/usr/lib/wine/winedbg</i></p>
<dd> The Wine debugger</p>
<dt><i>/usr/lib/x86_64-linux-gnu/wine</i></p>
<dd> Directory containing Wine shared libraries</p>
<dt><i>$WINEPREFIX/dosdevices</i></p>
<dd> Directory containing the DOS device mappings. Each file in that directory is a symlink to the Unix device file implementing a given device. For instance, if COM1 is mapped to <i>/dev/ttyS0</i> you&#8217;d have a symlink of the form <i>$WINEPREFIX/dosdevices/com1</i> -&gt; <i>/dev/ttyS0</i>.<br />
 DOS drives are also specified with symlinks; for instance if drive D: corresponds to the CDROM mounted at <i>/mnt/cdrom</i>, you&#8217;d have a symlink <i>$WINEPREFIX/dosdevices/d:</i> -&gt; <i>/mnt/cdrom</i>. The Unix device corresponding to a DOS drive can be specified the same way, except with &#8216;::&#8217; instead of &#8216;:&#8217;. So for the previous example, if the CDROM device is mounted from <i>/dev/hdc</i>, the corresponding symlink would be <i>$WINEPREFIX/dosdevices/d::</i> -&gt; <i>/dev/hdc</i>.</dl>
<h2>AUTHORS</h2>
<p> Wine is available thanks to the work of many developers. For a listing of the authors, please see the file <i>AUTHORS</i> in the top-level directory of the source distribution.</p>
<h2>COPYRIGHT</h2>
<p> Wine can be distributed under the terms of the LGPL license. A copy of the license is in the file <i>COPYING.LIB</i> in the top-level directory of the source distribution.</p>
<h2>BUGS</h2>
<p> A status report on many applications is available from the <code>Wine Application Database</code> Please add entries to this list for applications you currently run, if necessary. </p>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AVAILABILITY</h2>
<p> The most recent public version of <code>wine</code> is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wineserver/">wineserver</a></code>(1), <code><a href="/docs/linux/man/1-winedbg/">winedbg</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
<h2>Index</h2>
