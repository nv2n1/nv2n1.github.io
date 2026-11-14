---
title: "ffado-bridgeco-downloader(1)"
name: "ffado-bridgeco-downloader"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffado-bridgeco-downloader/"
description: "ffado-bridgeco-downloader – firmware download application for BridgeCo devices"
---

<h2>NAME</h2>
<p> ffado-bridgeco-downloader &#8211; firmware download application for BridgeCo devices</p>
<h2>SYNOPSIS</h2>
<p> <code>ffado-bridgeco-downloader [OPTION&#8230;] OPERATION</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ffado-bridgeco-downloader</code> permits firmware updates to be made to BridgeCo (aka BeBoB) devices under Linux. <i>OPERATION</i> describes the action to be carried out. An <i>OPERATION</i> is introduced with the GUID of the device to operate on. This is followed by one of the following keywords and any arguments required by that keyword.</p>
<dl>
<dt><code>display</code></p>
<dd> Display information about the interface</p>
<dt><code>setguid NEW_GUID</code></p>
<dd> Set the device&#8217;s GUID to <i>NEW_GUID</i></p>
<dt><code>firmware FILE</code></p>
<dd> Download the firmware file <i>FILE</i> to the device.</p>
<dt><code>cne FILE</code></p>
<dd> Download the CnE file <i>FILE</i> to the device.</p>
<dt><code>bcd FILE</code></p>
<dd> Parse the BeBoB BCD file <i>FILE</i> and display information about the contents. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, &#8211;help, &#8211;usage</code></p>
<dd> Display brief usage information and exit</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show the program version and exit</p>
<dt><code>-p, &#8211;port=NUM</code></p>
<dd> Specify use of IEEE1394 port <i>NUM</i></p>
<dt><code>-v, &#8211;verbose=LEVEL</code></p>
<dd> Produce verbose output. The higher the <i>LEVEL</i> the more verbose the messages. The some verbose messages may only be available of FFADO was compiled with debugging enabled.</p>
<dt><code>-b, &#8211;noboot</code></p>
<dd> Do not start the bootloader. Use this if the bootloader is already running.</p>
<dt><code>-f, &#8211;force</code></p>
<dd> Force firmware download in the event the program doesn&#8217;t think it&#8217;s a good idea. Use with caution.</p>
<dt><code>-m, &#8211;magic=MAGIC</code></p>
<dd> A magic number you have to obtain before this program will work. Specifying it on the command line means that you accept the risks which come with this tool. The magic number can be obtained in the source code. </p>
</dl>
<h2>NOTES</h2>
<p> Manipulating firmware can cause your device to stop working. The FFADO project accepts no responsibility if this occurs as a result of using this tool. </p>
<h2>Index</h2>
