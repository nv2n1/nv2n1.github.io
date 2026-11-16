---
title: "ofxdump(1)"
name: "ofxdump"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ofxdump/"
description: "ofxdump – Dump content of OFX files as human-readable text"
---

<h2>NAME</h2>
<p> ofxdump &#8211; Dump content of OFX files as human-readable text</p>
<h2>SYNOPSIS</h2>
<p> <code>ofxdump</code> [<i>OPTIONS</i>]&#8230; [<i>FILES</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> ofxdump 0.9.9 </p>
<p> ofxdump prints to stdout, in human readable form, everything the library understands about a particular file or response, and sends errors to stderr. To know exactly what the library understands about of a particular ofx response file, just call ofxdump on that file.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version and exit</dd>
<dt><code>-f</code>, <code>&#8211;import-format</code>=<i>STRING</i></dt>
<dd> Force the file format of the file(s) specified (default=`AUTODETECT&#8217;)</dd>
<dt><code>&#8211;list-import-formats</code></dt>
<dd> List available import file formats &#8216;import-format&#8217; command</dd>
<dt><code>&#8211;msg_parser</code></dt>
<dd> Output file parsing messages (default=off)</dd>
<dt><code>&#8211;msg_debug</code></dt>
<dd> Output messages meant for debuging (default=off)</dd>
<dt><code>&#8211;msg_warning</code></dt>
<dd> Output warning messages about abnormal conditions and unknown constructs (default=on)</dd>
<dt><code>&#8211;msg_error</code></dt>
<dd> Output error messages (default=on)</dd>
<dt><code>&#8211;msg_info</code></dt>
<dd> Output informational messages about the progress of the library (default=on)</dd>
<dt><code>&#8211;msg_status</code></dt>
<dd> Output status messages (default=on) </dd>
</dl>
<h2>Index</h2>
