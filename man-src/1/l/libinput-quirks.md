---
title: "libinput-quirks(1)"
name: "libinput-quirks"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libinput-quirks/"
description: "libinput-quirks – quirk debug helper for libinput"
---

<h2 class="name">NAME</h2>
<p> libinput-quirks &#8211; quirk debug helper for libinput </p>
<h2>SYNOPSIS</h2>
<p> <code>libinput quirks list [&#8211;data-dir /path/to/dir] [&#8211;verbose] </code><i>/dev/input/event0</i> </p>
<p> <code>libinput quirks validate [&#8211;data-dir /path/to/dir] [&#8211;verbose]</code> </p>
<p> <code>libinput quirks &#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>libinput quirks</code> tool interacts with libinput&#8217;s quirks database. </p>
<p> When invoked as <code>libinput quirks list,</code> the tool lists all quirks applied to the given device. </p>
<p> When invoked as <code>libinput quirks validate,</code> the tool checks for parsing errors in the quirks files and fails if a parsing error is encountered. </p>
<p> This is a debugging tool only, its output and behavior may change at any time. Do not rely on the output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;data-dir </code><i>/path/to/dir</i></p>
<dd> Use the given directory as data directory for quirks files. When omitted, the default directories are used.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help</p>
<dt><code>&#8211;verbose</code></p>
<dd> Use verbose output, useful for debugging.</dl>
<h2>LIBINPUT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-libinput/">libinput</a>(1)</code> suite </p>
<h2>Index</h2>
