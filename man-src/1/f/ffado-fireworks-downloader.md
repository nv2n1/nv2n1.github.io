---
title: "ffado-fireworks-downloader(1)"
name: "ffado-fireworks-downloader"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffado-fireworks-downloader/"
description: "ffado-fireworks-downloader – firmware download application for Echo Fireworks devices"
---

<h2>NAME</h2>
<p> ffado-fireworks-downloader &#8211; firmware download application for Echo Fireworks devices</p>
<h2>SYNOPSIS</h2>
<p> <code>ffado-fireworks-downloader [OPTION&#8230;] OPERATION</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ffado-bridgeco-downloader</code> permits firmware updates to be made to Echo Fireworks devices under Linux. <i>OPERATION</i> describes the action to be carried out. An <i>OPERATION</i> comprises one of the following keywords and any arguments required by that keyword.</p>
<dl>
<dt><code>list</code></p>
<dd> List devices on the firewire bus.</p>
<dt><code>display</code></p>
<dd> Display information about a device and its firmware.</p>
<dt><code>upload FILE</code></p>
<dd> Upload the firmware contained in <i>FILE</i> to the device</p>
<dt><code>download FILE START_ADDR LEN</code></p>
<dd> Download the flash contents from the device. <i>LEN</i> bytes will be downloaded starting at <i>START_ADDR</i> and written to the file <i>FILE</i></p>
<dt><code>verify FILE</code></p>
<dd> Verify that the firmware contained in the device corresponds to the one in <i>FILE</i></p>
<dt><code>session_display</code></p>
<dd> Show information about the session on the device.</p>
<dt><code>session_info FILE</code></p>
<dd> Show information about the device session stored in <i>FILE</i></p>
<dt><code>session_download FILE</code></p>
<dd> Download the session content from the device into <i>FILE</i></p>
<dt><code>session_upload FILE</code></p>
<dd> Upload the session from <i>FILE</i> to the device. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display brief usage information and exit</p>
<dt><code>-p, &#8211;port=NUM</code></p>
<dd> Specify use of IEEE1394 port <i>NUM</i></p>
<dt><code>-v, &#8211;verbose=LEVEL</code></p>
<dd> Produce verbose output. The higher the <i>LEVEL</i> the more verbose the messages. The some verbose messages may only be available of FFADO was compiled with debugging enabled.</p>
<dt><code>-g, &#8211;guid=GUID</code></p>
<dd> Specify the GUID of the device to interact with. If this is not specified an attempt will be made to automatically detect a suitable device.</p>
<dt><code>-m, &#8211;magic=MAGIC</code></p>
<dd> A magic number you have to obtain before this program will work. Specifying it on the command line means that you accept the risks which come with this tool. The magic number can be obtained in the source code. </p>
</dl>
<h2>NOTES</h2>
<p> Manipulating firmware can cause your device to stop working. The FFADO project accepts no responsibility if this occurs as a result of using this tool. </p>
<h2>Index</h2>
