---

title: "ipa-managed-entries(1)"
name: "ipa-managed-entries"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-managed-entries/"
description: "ipa-managed-entries – Enables or disables the schema Managed Entry plugins"
---

<p> ipa-managed-entries &#8211; Enables or disables the schema Managed Entry plugins</p>
<h2>SYNOPSIS</h2>
<p> ipa-managed-entries [options] &lt;enable|disable|status&gt;</p>
<h2>DESCRIPTION</h2>
<p> Run the command with the <code>enable</code> option to enable the Managed Entry plugin. </p>
<p> Run the command with the <code>disable</code> option to disable the Managed Entry plugin. </p>
<p> Run the command with the <code>status</code> to determine the current status of the Managed Entry plugin. </p>
<p> In all cases the user will be prompted to provide the Directory Manager&#8217;s password unless option <code>-p</code> is used. </p>
<p> Directory Server will need to be restarted after the Managed Entry plugin has been enabled. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show a help message and exit</dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> Enable debug logging when more verbose output is needed</dd>
<dt><code>-e</code>, <code>&#8211;entry</code></dt>
<dd> DN for the Managed Entry Definition</dd>
<dt><code>-l</code>, <code>&#8211;list</code></dt>
<dd> List available Managed Entries</dd>
<dt><code>-p</code> <i>DM_PASSWORD</i>, <code>&#8211;password</code>=<i>DM_PASSWORD</i></dt>
<dd> The Directory Manager password to use for authentication</dd></dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<p> 2 if the plugin is already in the required status (enabled or disabled) </p>
