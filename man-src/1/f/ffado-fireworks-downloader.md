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
<dt><code>list</code></dt>
<dd> List devices on the firewire bus.</dd>
<dt><code>display</code></dt>
<dd> Display information about a device and its firmware.</dd>
<dt><code>upload FILE</code></dt>
<dd> Upload the firmware contained in <i>FILE</i> to the device</dd>
<dt><code>download FILE START_ADDR LEN</code></dt>
<dd> Download the flash contents from the device. <i>LEN</i> bytes will be downloaded starting at <i>START_ADDR</i> and written to the file <i>FILE</i></dd>
<dt><code>verify FILE</code></dt>
<dd> Verify that the firmware contained in the device corresponds to the one in <i>FILE</i></dd>
<dt><code>session_display</code></dt>
<dd> Show information about the session on the device.</dd>
<dt><code>session_info FILE</code></dt>
<dd> Show information about the device session stored in <i>FILE</i></dd>
<dt><code>session_download FILE</code></dt>
<dd> Download the session content from the device into <i>FILE</i></dd>
<dt><code>session_upload FILE</code></dt>
<dd> Upload the session from <i>FILE</i> to the device. </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display brief usage information and exit</dd>
<dt><code>-p, &#8211;port=NUM</code></dt>
<dd> Specify use of IEEE1394 port <i>NUM</i></dd>
<dt><code>-v, &#8211;verbose=LEVEL</code></dt>
<dd> Produce verbose output. The higher the <i>LEVEL</i> the more verbose the messages. The some verbose messages may only be available of FFADO was compiled with debugging enabled.</dd>
<dt><code>-g, &#8211;guid=GUID</code></dt>
<dd> Specify the GUID of the device to interact with. If this is not specified an attempt will be made to automatically detect a suitable device.</dd>
<dt><code>-m, &#8211;magic=MAGIC</code></dt>
<dd> A magic number you have to obtain before this program will work. Specifying it on the command line means that you accept the risks which come with this tool. The magic number can be obtained in the source code. </dd>
</dl>
<h2>NOTES</h2>
<p> Manipulating firmware can cause your device to stop working. The FFADO project accepts no responsibility if this occurs as a result of using this tool. </p>
<h2>Index</h2>
