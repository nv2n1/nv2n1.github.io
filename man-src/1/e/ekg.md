---
title: "ekg(1)"
name: "ekg"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ekg/"
description: "ekg – A Gadu-Gadu compatible client."
---

<h2>NAME</h2>
<p> ekg &#8211; A Gadu-Gadu compatible client.</p>
<h2>SYNOPSIS</h2>
<p> <code>ekg [</code> <code>options</code> <code>]</code> <code>[</code> <code>commands</code> <code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ekg</code> is an experimental Gadu-Gadu client. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h&nbsp;<wbr>[&#8211;help]</code></p>
<dd> Shows command line options.</p>
<dt><code>-u username&nbsp;<wbr>[&#8211;user username]</code></p>
<dd> Starts ekg with other By default config files are stored in ~/.gg/ (if there is a non-empty $CONFIG_DIR environment variable, ~/$CONFIG_DIR/gg/ is used instead); this option gives ability to create subdirectories structure with other setups.</p>
<dt><code>-t theme&nbsp;<wbr>[&#8211;theme theme]</code></p>
<dd> Loads theme from the specified file.</p>
<dt><code>-c file&nbsp;<wbr>[&#8211;control-pipe file]</code></p>
<dd> Creates a named pipe that can be used to control the client.</p>
<dt><code>-n&nbsp;<wbr>[&#8211;no-auto]</code></p>
<dd> Don&#8217;t connect automagically. After starting program won&#8217;t automatically connect to the gg servers.</p>
<dt><code>-N&nbsp;<wbr>[&#8211;no-global-config]</code></p>
<dd> Don&#8217;t load global configuration file (i.e. /etc/ekg.conf) after user&#8217;s one.</p>
<dt><code>-a&nbsp;<wbr>[&#8211;away[=description]]</code></p>
<dd> After connecting sets the status to &quot;away&quot;.</p>
<dt><code>-b&nbsp;<wbr>[&#8211;back[=description]]</code></p>
<dd> After connecting sets the status to &quot;back&quot;.</p>
<dt><code>-i&nbsp;<wbr>[&#8211;invisible[=description]]</code></p>
<dd> After connecting sets the status to &quot;invisible&quot;.</p>
<dt><code>-p&nbsp;<wbr>[&#8211;private]</code></p>
<dd> After connecting change to &quot;private mode&quot;.</p>
<dt><code>-v&nbsp;<wbr>[&#8211;version]</code></p>
<dd> Prints the client and libgadu library version.</p>
<dt><code>-f name&nbsp;<wbr>[&#8211;frontend name]</code></p>
<dd> Selects given user interface. </p>
</dl>
<h2>Index</h2>
