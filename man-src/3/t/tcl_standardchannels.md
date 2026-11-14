---
title: "tcl_standardchannels(3)"
name: "tcl_standardchannels"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_standardchannels/"
description: "Tcl_StandardChannels – How the Tcl library deals with the standard channels"
---

<p>Tcl_StandardChannels &#8211; How the Tcl library deals with the standard channels </p>
<h2>Description</h2>
<p>This page explains the initialization and use of standard channels in the Tcl library. </p>
<p> The term <i>standard channels</i> comes out of the Unix world and refers to the three channels automatically opened by the OS for each new application. They are <code>stdin</code>, <code>stdout</code> and <code>stderr</code>. The first is the standard input an application can read from, the other two refer to writable channels, one for regular output and the other for error messages. </p>
<p> Tcl generalizes this concept in a cross-platform way and exposes standard channels to the script level.</p>
<h3>Application Programming Interfaces</h3>
<p>The public API procedures dealing directly with standard channels are <code>Tcl_GetStdChannel</code> and <code>Tcl_SetStdChannel</code>. Additional public APIs to consider are <code>Tcl_RegisterChannel</code>, <code>Tcl_CreateChannel</code> and <code>Tcl_GetChannel</code>.</p>
<h2>Initialization Of Tcl Standard Channels</h2>
<p>Standard channels are initialized by the Tcl library in three cases: when explicitly requested, when implicitly required before returning channel information, or when implicitly required during registration of a new channel. </p>
<p> These cases differ in how they handle unavailable platform- specific standard channels. (A channel is not &#8220;available&#8221; if it could not be successfully opened; for example, in a Tcl application run as a Windows NT service.)</p>
<dl COMPACT>
<dt>1)</p>
<dd>A single standard channel is initialized when it is explicitly specified in a call to <code>Tcl_SetStdChannel</code>. The states of the other standard channels are unaffected.</p>
<dl COMPACT>
<dd>Missing platform-specific standard channels do not matter here. This approach is not available at the script level.</dl>
<dt>2)</p>
<dd>All uninitialized standard channels are initialized to platform-specific default values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>(a)</p>
<dd>when open channels are listed with <code>Tcl_GetChannelNames</code> (or the <code>file channels</code> script command), or</p>
<dt>(b)</p>
<dd>when information about any standard channel is requested with a call to <code>Tcl_GetStdChannel</code>, or with a call to <code>Tcl_GetChannel</code> which specifies one of the standard names (<code>stdin</code>, <code>stdout</code> and <code>stderr</code>).</dl>
<p> In case of missing platform-specific standard channels, the Tcl standard channels are considered as initialized and then immediately closed. This means that the first three Tcl channels then opened by the application are designated as the Tcl standard channels.</dl>
<dt>3)</p>
<dd>All uninitialized standard channels are initialized to platform-specific default values when a user-requested channel is registered with <code>Tcl_RegisterChannel</code>.</dl>
<p> In case of unavailable platform-specific standard channels the channel whose creation caused the initialization of the Tcl standard channels is made a normal channel. The next three Tcl channels opened by the application are designated as the Tcl standard channels. In other words, of the first four Tcl channels opened by the application the second to fourth are designated as the Tcl standard channels.</p>
<h2>Re-Initialization Of Tcl Standard Channels</h2>
<p>Once a Tcl standard channel is initialized through one of the methods above, closing this Tcl standard channel will cause the next call to <code>Tcl_CreateChannel</code> to make the new channel the new standard channel, too. If more than one Tcl standard channel was closed <code>Tcl_CreateChannel</code> will fill the empty slots in the order <code>stdin</code>, <code>stdout</code> and <code>stderr</code>. </p>
<p> <code>Tcl_CreateChannel</code> will not try to reinitialize an empty slot if that slot was not initialized before. It is this behavior which enables an application to employ method 1 of initialization, i.e. to create and designate their own Tcl standard channels.</p>
<h2>Shell-Specific Details</h2>
<h3>tclsh</h3>
<p>The Tcl shell (or rather the function <code>Tcl_Main</code>, which forms the core of the shell&#8217;s implementation) uses method 2 to initialize the standard channels.</p>
<h3>wish</h3>
<p>The windowing shell (or rather the function <code>Tk_MainEx</code>, which forms the core of the shell&#8217;s implementation) uses method 1 to initialize the standard channels (See <code>Tk_InitConsoleChannels</code>) on non-Unix platforms. On Unix platforms, <code>Tk_MainEx</code> implicitly uses method 2 to initialize the standard channels.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_createchannel/">Tcl_CreateChannel</a>(3), <a href="/docs/linux/man/3-tcl_registerchannel/">Tcl_RegisterChannel</a>(3), <a href="/docs/linux/man/3-tcl_getchannel/">Tcl_GetChannel</a>(3), <a href="/docs/linux/man/3-tcl_getstdchannel/">Tcl_GetStdChannel</a>(3), <a href="/docs/linux/man/3-tcl_setstdchannel/">Tcl_SetStdChannel</a>(3), <a href="/docs/linux/man/3-tk_initconsolechannels/">Tk_InitConsoleChannels</a>(3), <a href="/docs/linux/man/1-tclsh/">tclsh</a>(1), <a href="/docs/linux/man/1-wish/">wish</a>(1), <a href="/docs/linux/man/3-tcl_main/">Tcl_Main</a>(3), <a href="/docs/linux/man/3-tk_mainex/">Tk_MainEx</a>(3)</p>
<h2>Keywords</h2>
<p>standard channels</p>
