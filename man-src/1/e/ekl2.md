---

title: "ekl2(1)"
name: "ekl2"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ekl2/"
description: "ekl2 – EKG history viewer."
---

<p> ekl2 &#8211; EKG history viewer.</p>
<h2>SYNTAX</h2>
<p> <code>ekl2 [</code> <code>OPTIONS</code> <code>] [</code> <code>SOURCE</code> <code>]</code></p>
<h2>SUMMARY</h2>
<p> <code>ekl2</code> This program prints the conversation history file as created by ekg.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d&nbsp;<wbr>+format &#8211;date&nbsp;<wbr>+format&nbsp;<wbr></code></dt>
<dd> Sets format of displayed date (see <a href="/docs/linux/man/1-date/">date</a>(1))</dd>
<dt><code>&#8211;location</code></dt>
<dd> Sets log files&#8217; location (~/.gg/history by default)</dd>
<dt><code>-h &#8211;help&nbsp;<wbr></code></dt>
<dd> Prints help message.</dd>
<dt><code>-L &#8211;List&nbsp;<wbr></code></dt>
<dd> Prints the list of available log files. (from ~/.gg/history)</dd>
<dt><code>-l &#8211;sessions&nbsp;<wbr>[+num]&nbsp;<wbr>[+off]</code></dt>
<dd> Prints the list of sessions in given log file. <code>num&nbsp;<wbr></code> is the number of session to display. <code>off&nbsp;<wbr></code> is the offset between conversations, in minutes (60 by default).</dd>
<dt><code>-n &#8211;nocolor&nbsp;<wbr></code></dt>
<dd> No colors.</dd>
<dt><code>-sh &#8211;short&nbsp;<wbr></code></dt>
<dd> simplified form.</dd>
<dt><code>-v &#8211;version&nbsp;<wbr></code></dt>
<dd> Prints script version.</dd>
<dt><code>SOURCE&nbsp;<wbr></code></dt>
<dd> gg number, nickname or logfile name.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ekg/">ekg</a></code>(1). </p>
