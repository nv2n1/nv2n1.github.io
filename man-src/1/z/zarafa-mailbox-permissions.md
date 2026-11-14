---
title: "zarafa-mailbox-permissions(1)"
name: "zarafa-mailbox-permissions"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-mailbox-permissions/"
description: "zarafa-mailbox-permissions – Manage mailbox delegate permissions."
---

<h2 class="name">NAME</h2>
<p> zarafa-mailbox-permissions &#8211; Manage mailbox delegate permissions. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-mailbox-permissions</code> <i>ACTION</i> [<i>MAILBOXES</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>This script can be used to show delegate permissions and settings for users. The Zarafa server must be running for <code>zarafa-mailbox-permissions</code> to work. </p>
<p> You can show delegates and permissions information, and add or update delegate permissions on a mailbox.</p>
<h2>ACTIONS</h2>
<p> zarafa-mailbox-permissions needs an action command with the appropriate options. Valid actions are: </p>
<p> <code>&#8211;update-delegate</code> <i>username</i></p>
<dl>
<dt>
<dd> Add or update delegate information for <i>username</i> on specified <i>mailboxes</i>.</dl>
<p> <code>&#8211;remove-all-permissions</code></p>
<dl>
<dt>
<dd> Removes all delegates and explicit permissions on folders from one or more <i>mailboxes</i>.</dl>
<p> <code>&#8211;list-permissions</code></p>
<dl>
<dt>
<dd> Show all delegates and folder permissions of one or more <i>mailbox</i>.</dl>
<p> <code>&#8211;list-permissions-per-folder</code></p>
<dl>
<dt>
<dd> Show delegates and folder containing explicit permissions of one or more <i>mailbox</i>.</dl>
<h2>OPTIONS</h2>
<p> The options used by actions are as follows: </p>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Perform the action on all available users in the zarafa-server.</dl>
<p> <code>-h</code>, <code>&#8211;host</code> <i>URL</i></p>
<dl>
<dt>
<dd> Use URL to connect to the zarafa-server. Default is <i>file:///var/run/zarafa</i>.</dl>
<p> <code>-s</code>, <code>&#8211;sslkey-file</code> <i>FILENAME</i></p>
<dl>
<dt>
<dd> Use this file as the SSL private key to connect to the zarafa-server. Default is no SSL key.</dl>
<p> <code>-p</code>, <code>&#8211;sslkey-pass</code> <i>PASSWORD</i></p>
<dl>
<dt>
<dd> Use this password as the SSL private key password. Default is no SSL key password.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Currently unused, but may be used in the future for more information.</dl>
<p> <code>&#8211;calendar</code> <i>[none|readonly|secretary|owner]</i></p>
<dl>
<dt>
<dd> When updating a delegate, set these permissions on the default calendar folder of the given <i>mailboxes</i>. Select one of the permission preset to set on the folder.</dl>
<p> <code>&#8211;tasks</code> <i>[none|readonly|secretary|owner]</i></p>
<dl>
<dt>
<dd> When updating a delegate, set these permissions on the default tasks folder of the given <i>mailboxes</i>. Select one of the permission preset to set on the folder.</dl>
<p> <code>&#8211;inbox</code> <i>[none|readonly|secretary|owner]</i></p>
<dl>
<dt>
<dd> When updating a delegate, set these permissions on the default inbox folder of the given <i>mailboxes</i>. Select one of the permission preset to set on the folder.</dl>
<p> <code>&#8211;notes</code> <i>[none|readonly|secretary|owner]</i></p>
<dl>
<dt>
<dd> When updating a delegate, set these permissions on the default notes folder of the given <i>mailboxes</i>. Select one of the permission preset to set on the folder.</dl>
<p> <code>&#8211;journal</code> <i>[none|readonly|secretary|owner]</i></p>
<dl>
<dt>
<dd> When updating a delegate, set these permissions on the default journal folder of the given <i>mailboxes</i>. Select one of the permission preset to set on the folder.</dl>
<p> <code>&#8211;store</code> <i>[denied|norights|readonly|secretary|owner|fullcontrol]</i></p>
<dl>
<dt>
<dd> When updating a delegate, set these permissions on the store of the given <i>mailboxes</i>. All folders in the store inherit these permissions unless explicitly overwritten. Select one of the permission preset to set on the store.</dl>
<p> <code>&#8211;see-private</code> <i>[no|yes]</i></p>
<dl>
<dt>
<dd> When updating a delegate, allow the delegate to see private marked items of the given <i>mailboxes</i>.</dl>
<p> <code>&#8211;sendcopy</code> <i>[no|yes]</i></p>
<dl>
<dt>
<dd> When updating a delegate, mark the delegate to receive a copy of meeting requests in their inbox for the given <i>mailboxes</i>.</dl>
<p> <code>&#8211;send-only-to-delegators</code> <i>[no|yes]</i></p>
<dl>
<dt>
<dd> When updating a delegate, and <code>&#8211;sendcopy</code> is used, let the delegates receive meeting requests only, and not the owner of the given <i>mailboxes</i>.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show a help text of the program and some usage examples.</dl>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1)<code><a href="/docs/linux/man/5-zarafa-server-cfg/">zarafa-server.cfg</a></code>(5) </p>
<h2>Index</h2>
