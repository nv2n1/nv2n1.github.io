---
title: "ipa-moduser(1)"
name: "ipa-moduser"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-moduser/"
description: "ipa-moduser – Modify a user"
---

<h2>NAME</h2>
<p> ipa-moduser &#8211; Modify a user</p>
<h2>SYNOPSIS</h2>
<p> ipa-moduser [<i>OPTION</i>]&#8230; <i>name</i> </p>
<h2>DESCRIPTION</h2>
<p> Updates the user <i>name</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;activate</code></dt>
<dd> Activate a user that was previously inactivated</dd>
<dt><code>-c</code>, <code>&#8211;gecos</code>=<i>GECOS</i></dt>
<dd> Set the gecos field of the user. This is traditionally the user&#8217;s full name.</dd>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>directory</i></dt>
<dd> Set user&#8217;s home directory</dd>
<dt><code>-f</code>, <code>&#8211;firstname</code>=<i>NAME</i></dt>
<dd> Set user&#8217;s first name</dd>
<dt><code>-l</code>, <code>&#8211;lastname</code>=<i>NAME</i></dt>
<dd> Set user&#8217;s last name</dd>
<dt><code>-s</code>, <code>&#8211;shell</code>=<i>shell</i></dt>
<dd> Set user&#8217;s login shell</dd>
<dt><code>&#8211;addattr</code> <i>attr=value</i></dt>
<dd> Add a new attribute, or value to an existing attribute</dd>
<dt><code>&#8211;delattr</code> <i>attr=value</i></dt>
<dd> Remove an attribute and all values</dd>
<dt><code>&#8211;setattr</code> <i>attr=value</i></dt>
<dd> Set an attribute to a new value, removing all old ones</dd></dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
