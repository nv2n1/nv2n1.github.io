---
title: "bjavaloader(1)"
name: "bjavaloader"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bjavaloader/"
description: "bjavaloader – Barry Project’s program to manage BlackBerry applications"
---

<h2 class="name">NAME</h2>
<p> <code>bjavaloader</code> &#8211; Barry Project&#8217;s program to manage BlackBerry applications </p>
<h2>SYNOPSIS</h2>
<p> <code>bjavaloader [-h][-p pin][-P pass][-v]</code></p>
<dl>
<dt><code>bjavaloader dir [-s]</code></p>
<dd>
<dt><code>bjavaloader deviceinfo</code></p>
<dd>
<dt><code>bjavaloader load &lt;.codfile&gt;</code></p>
<dd>
<dt><code>bjavaloader save &lt;module_name&gt;</code></p>
<dd>
<dt><code>bjavaloader wipe [-a | -i]</code></p>
<dd>
<dt><code>bjavaloader erase [-f] &lt;module_name&gt;</code></p>
<dd>
<dt><code>bjavaloader eventlog</code></p>
<dd>
<dt><code>bjavaloader cleareventlog</code></p>
<dd>
<dt><code>bjavaloader logstacktraces</code></p>
<dd>
<dt><code>bjavaloader screenshot &lt;.bmp file&gt;</code></p>
<dd>
<dt><code>bjavaloader settime [yyyy-mm-dd HH:MM:SS]</code></p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> <code>bjavaloader</code> is a tool for loading, listing, and deleting applications on a BlackBerry device. It has a few other features as well, not pertaining to application management. The command syntax is intentionally similar to the Windows program &#8216;javaloader.exe&#8217; provided by Research In Motion, in order to make it easy to use the same build scripts on Linux and Windows.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Used with the &#8216;wipe&#8217; command to only wipe the applications.</p>
<dt><code>-i</code></p>
<dd> Used with the &#8216;wipe&#8217; command to only wipe the filesystem.</p>
<dt><code>-f</code></p>
<dd> Used with the &#8216;erase&#8217; command to force the erasure of an application that is currently in use in the device. Experimental.</p>
<dt><code>-h</code></p>
<dd> Display a command help summary.</p>
<dt><code>-s</code></p>
<dd> When using the &#8216;dir&#8217; command, list the submodules as well.</p>
<dt><code>-p pin</code></p>
<dd> Specifies the PIN number of the device with which you wish to communicate, when multiple devices are connected.</p>
<dt><code>-P password</code></p>
<dd> A simplistic method to specify the device password.</p>
<dt><code>-v</code></p>
<dd> Verbose debug output. This enables dumping of USB bus scanning, as well as the protocol packets used during communication. </p>
</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>dir [-s]</code></p>
<dd> Fetch a list of all applications and display them on stdout. When used with the -s option, submodules are included, and can take a long time to display.</p>
<dt><code>deviceinfo</code></p>
<dd> Provides information on the handheld.</p>
<dt><code>load &lt;.cod filename&gt; &#8230;</code></p>
<dd> Loads one or more COD application files into the device.</p>
<dt><code>save &lt;module name&gt; &#8230;</code></p>
<dd> Retrieves modules from the handheld and writes them to .cod files with the same name as the module. Note that this will overwrite any existing .cod file in the current directory.</p>
<dt><code>wipe [-a | -i]</code></p>
<dd> Wipes the handheld, removing all data such as messages, contacts, etc. and/or all .cod files, including OS .cod files. By default, with no options specified, both applications and data are wiped. Use the switches to specify only applications or data.</p>
<dt><code>erase [-f] &lt;module name&gt; &#8230;</code></p>
<dd> Delete the specified application module(s). The module name can be determined using the &#8216;dir&#8217; command. When used with the -f option, the module is erased even if in use, and the device will be reset.</p>
<dt><code>eventlog</code></p>
<dd> Retrives the handheld event log and prints it on stdout.</p>
<dt><code>cleareventlog</code></p>
<dd> Clears the handheld event log.</p>
<dt><code>logstacktraces</code></p>
<dd> Dumps the stack traces for all threads into the event log, which can then be viewed with the &#8216;eventlog&#8217; command.</p>
<dt><code>screenshot &lt;.bmp filename&gt;</code></p>
<dd> Capture current screen image and save in BMP format.</p>
<dt><code>settime [yyyy-mm-dd HH:MM:SS]</code></p>
<dd> Sets the time on the handheld to the current time, or the specified time. If time is given as an argument, the current system timezone is assumed. </p>
</dl>
<h2>AUTHOR</h2>
<p> <code>bjavaloader</code> was initially written for the Barry project by Nicolas Vivien, with additional contributions from others over time. This manual page was written by Chris Frey.</p>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="http://www.netdirect.ca/software/packages/barry">http://www.netdirect.ca/software/packages/barry</a> </p>
<h2>Index</h2>
