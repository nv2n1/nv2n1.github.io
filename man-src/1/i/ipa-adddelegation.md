---
title: "ipa-adddelegation(1)"
name: "ipa-adddelegation"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-adddelegation/"
description: "ipa-adddelegation – Add a delegation"
---

<h2>NAME</h2>
<p> ipa-adddelegation &#8211; Add a delegation </p>
<h2>SYNOPSIS</h2>
<p> ipa-adddelegation [<i>OPTION</i>]&#8230; <i>name</i> </p>
<h2>DESCRIPTION</h2>
<p> Adds a delegation named <i>name</i>. </p>
<p> A delegation is used to grant write access to certain attributes from one group to another. </p>
<p> For example, a secretary group may be granted write access to modify the phone attribute of all users in a manager&#8217;s group.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;attributes</code>=<i>ATTRIBUTES</i></p>
<dd> A comma-separated list of the SM]attributes that may be written by the source group.</p>
<dt><code>-l</code></p>
<dd> Provide a list of common attribute names. This is not an exhaustive list.</p>
<dt><code>-s</code>, <code>&#8211;source</code>=<i>SOURCE</i></p>
<dd> The name of the group that is being granted write permission.</p>
<dt><code>-t</code>, <code>&#8211;target</code>=<i>TARGET</i></p>
<dd> The name of the group that will be written to.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display the XML-RPC request and response for more verbose debugging output</dl>
<p> All arguments except -v/&#8211;verbose are mandatory.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>ipa-adddelegation -a telephonenumber,facsimiletelephonenumber,mobile -s secretaries -t everyone phones</p>
<dd>
<p> Create a delegation named <code>phones</code> that will let anyone in the <i>secretaries</i> group edit the phone numbers of anyone in the group <i>everyone</i>.</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the delegation was added successfully </p>
<p> 1 if an error occurred </p>
<p> 2 if no not exactly one matching source group was found (0 or more than one) </p>
<p> 3 if no not exactly one matching target group was found (0 or more than one </p>
<h2>Index</h2>
