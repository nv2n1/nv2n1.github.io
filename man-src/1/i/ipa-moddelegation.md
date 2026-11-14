---
title: "ipa-moddelegation(1)"
name: "ipa-moddelegation"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-moddelegation/"
description: "ipa-moddelegation – Modify an existing delegation"
---

<h2>NAME</h2>
<p> ipa-moddelegation &#8211; Modify an existing delegation </p>
<h2>SYNOPSIS</h2>
<p> ipa-moddelegation [<i>OPTION</i>]&#8230; <i>name</i> </p>
<h2>DESCRIPTION</h2>
<p> Modifies an existing delegation named <i>name</i>. </p>
<p> A delegation is used to grant access to certain attributes from one group to another.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;attributes</code>=<i>ATTRIBUTES</i></p>
<dd> A comma-separated list of the the SM]attributes that may be written by the source group. This list of attributes replaces the list in the existing delegation.</p>
<dt><code>-s</code>, <code>&#8211;source</code>=<i>SOURCE</i></p>
<dd> The name of the group that is being granted write permission.</p>
<dt><code>-t</code>, <code>&#8211;target</code>=<i>TARGET</i></p>
<dd> The name of the group that will be written to.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display the XML-RPC request and response for more verbose debugging output.</dl>
<p> At least one of -a, -s or -t is required.</p>
<h2>EXIT STATUS</h2>
<p> 0 if the delegation was updated successfully </p>
<p> 1 if an error occurred </p>
<p> 2 if no matching delegation was found </p>
<h2>Index</h2>
