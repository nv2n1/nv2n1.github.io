---
title: "exo-preferred-applications(1)"
name: "exo-preferred-applications"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exo-preferred-applications/"
description: "exo-preferred-applications – Select preferred applications for Xfce desktop environment"
---

<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
</dt><dd> exo-helper-1 [OPTION?]</dd></dl>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options</dd>
<dt><code>&#8211;help-gtk</code></dt>
<dd> Show GTK+ Options</dd></dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version information and exit</dd>
<dt><code>-c</code>, <code>&#8211;configure</code></dt>
<dd> Open the Preferred Applications</dd></dl>
<p> configuration dialog</p>
<dl>
<dt><code>-s</code>, <code>&#8211;socket-id</code>=<i>,SOCKET/</i> ID</dt>
<dd> Settings manager socket</dd>
<dt><code>-l</code>, <code>&#8211;launch</code>=<i>,TYPE/</i> [PARAMETER]</dt>
<dd> Launch the default helper of TYPE with the optional PARAMETER, where TYPE is one of the following values.</dd>
<dt><code>-q</code>, <code>&#8211;query</code>=<i>,TYPE/</i> [PARAMETER]</dt>
<dd> Query the default helper of TYPE, where TYPE is one of the following values.</dd>
<dt><code>&#8211;display</code>=<i>,DISPLAY/</i></dt>
<dd> X display to use</dd></dl>
<p> The following TYPEs are supported for the <code>&#8211;launch</code> and <code>&#8211;query</code> commands:</p>
<dl>
<dt>WebBrowser</dt>
<dd> &#8211; The preferred Web Browser.</dd>
<dt>MailReader</dt>
<dd> &#8211; The preferred Mail Reader.</dd>
<dt>FileManager</dt>
<dd> &#8211; The preferred File Manager.</dd>
<dt>
</dt><dd> TerminalEmulator &#8211; The preferred Terminal Emulator. </dd>
</dl>
