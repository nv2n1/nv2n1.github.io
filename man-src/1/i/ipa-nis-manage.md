---
title: "ipa-nis-manage(1)"
name: "ipa-nis-manage"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-nis-manage/"
description: "ipa-nis-manage – Enables or disables the NIS listener plugin"
---

<h2>NAME</h2>
<p> ipa-nis-manage &#8211; Enables or disables the NIS listener plugin</p>
<h2>SYNOPSIS</h2>
<p> ipa-nis-manage [options] &lt;enable|disable|status&gt;</p>
<h2>DESCRIPTION</h2>
<p> Run the command with the <code>enable</code> option to enable the NIS plugin. </p>
<p> Run the command with the <code>disable</code> option to disable the NIS plugin. </p>
<p> Run the command with the <code>status</code> option to read status of the NIS plugin. Return code 0 indicates enabled plugin, return code 4 indicates disabled plugin. </p>
<p> In all cases the user will be prompted to provide the Directory Manager&#8217;s password unless option <code>-y</code> is used. </p>
<p> Directory Server will need to be restarted after the NIS listener plugin has been enabled. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Enable debug logging when more verbose output is needed</p>
<dt><code>-y</code> <i>file</i></p>
<dd> File containing the Directory Manager password</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<p> 2 if the plugin is already in the required status (enabled or disabled) </p>
<p> 3 if RPC services cannot be enabled. </p>
<p> 4 if status command detected plugin in disabled state. </p>
<h2>Index</h2>
