---
title: "dmesg(1)"
name: "dmesg"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dmesg/"
description: "dmesg – print or control the kernel ring buffer"
---

<h2 class="name">NAME</h2>
<p> dmesg &#8211; print or control the kernel ring buffer </p>
<h2>SYNOPSIS</h2>
<p> <code>dmesg</code> [options] </p>
<p> <code>dmesg</code> <code>&#8211;clear</code> </p>
<p> <code>dmesg</code> <code>&#8211;read-clear</code> [options] </p>
<p> <code>dmesg</code> <code>&#8211;console-level</code> <i>level</i> </p>
<p> <code>dmesg</code> <code>&#8211;console-on</code> </p>
<p> <code>dmesg</code> <code>&#8211;console-off</code></p>
<h2>DESCRIPTION</h2>
<p> <code>dmesg</code> is used to examine or control the kernel ring buffer. </p>
<p> The default action is to display all messages from the kernel ring buffer.</p>
<h2>OPTIONS</h2>
<p> The <code>&#8211;clear</code>, <code>&#8211;read-clear</code>, <code>&#8211;console-on</code>, <code>&#8211;console-off</code>, and <code>&#8211;console-level</code> options are mutually exclusive. </p>
<p> <code>-C</code>, <code>&#8211;clear</code></p>
<dl>
<dt>
<dd> Clear the ring buffer.</dl>
<p> <code>-c</code>, <code>&#8211;read-clear</code></p>
<dl>
<dt>
<dd> Clear the ring buffer after first printing its contents.</dl>
<p> <code>-D</code>, <code>&#8211;console-off</code></p>
<dl>
<dt>
<dd> Disable the printing of messages to the console.</dl>
<p> <code>-d</code>, <code>&#8211;show-delta</code></p>
<dl>
<dt>
<dd> Display the timestamp and the time delta spent between messages. If used together with <code>&#8211;notime</code> then only the time delta without the timestamp is printed.</dl>
<p> <code>-E</code>, <code>&#8211;console-on</code></p>
<dl>
<dt>
<dd> Enable printing messages to the console.</dl>
<p> <code>-e</code>, <code>&#8211;reltime</code></p>
<dl>
<dt>
<dd> Display the local time and the delta in human-readable format. Be aware that conversion to the local time could be inaccurate (see <code>-T</code> for more details).</dl>
<p> <code>-F</code>, <code>&#8211;file</code> <i>file</i></p>
<dl>
<dt>
<dd> Read the syslog messages from the given <i>file</i>. Note that <code>-F</code> does not support messages in kmsg format. The old syslog format is supported only.</dl>
<p> <code>-f</code>, <code>&#8211;facility</code> <i>list</i></p>
<dl>
<dt>
<dd> Restrict output to the given (comma-separated) <i>list</i> of facilities. For example: </p>
<p> <code>dmesg &#8211;facility=daemon</code> </p>
<p> will print messages from system daemons only. For all supported facilities see the <code>&#8211;help</code> output.</dl>
<p> <code>-H</code>, <code>&#8211;human</code></p>
<dl>
<dt>
<dd> Enable human-readable output. See also <code>&#8211;color</code>, <code>&#8211;reltime</code> and <code>&#8211;nopager</code>.</dl>
<p> <code>-k</code>, <code>&#8211;kernel</code></p>
<dl>
<dt>
<dd> Print kernel messages.</dl>
<p> <code>-L</code>, <code>&#8211;color</code>[=<i>when</i>]</p>
<dl>
<dt>
<dd> Colorize the output. The optional argument <i>when</i> can be <code>auto</code>, <code>never</code> or <code>always</code>. If the <i>when</i> argument is omitted, it defaults to <code>auto</code>. The colors can be disabled; for the current built-in default see the <code>&#8211;help</code> output. See also the <code>COLORS</code> section below.</dl>
<p> <code>-l</code>, <code>&#8211;level</code> <i>list</i></p>
<dl>
<dt>
<dd> Restrict output to the given (comma-separated) <i>list</i> of levels. For example: </p>
<p> <code>dmesg &#8211;level=err,warn</code> </p>
<p> will print error and warning messages only. For all supported levels see the <code>&#8211;help</code> output.</dl>
<p> <code>-n</code>, <code>&#8211;console-level</code> <i>level</i></p>
<dl>
<dt>
<dd> Set the <i>level</i> at which printing of messages is done to the console. The <i>level</i> is a level number or abbreviation of the level name. For all supported levels see the <code>&#8211;help</code> output. </p>
<p> For example, <code>-n 1</code> or <code>-n emerg</code> prevents all messages, except emergency (panic) messages, from appearing on the console. All levels of messages are still written to <i>/proc/kmsg</i>, so <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) can still be used to control exactly where kernel messages appear. When the <code>-n</code> option is used, <code>dmesg</code> will <i>not</i> print or clear the kernel ring buffer.</dl>
<p> <code>&#8211;noescape</code></p>
<dl>
<dt>
<dd> The unprintable and potentially unsafe characters (e.g., broken multi-byte sequences, terminal controlling chars, etc.) are escaped in format 
