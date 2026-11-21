---

title: "ipa-modgroup(1)"
name: "ipa-modgroup"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-modgroup/"
description: "ipa-modgroup – Modify a group"
---

<p> ipa-modgroup &#8211; Modify a group</p>
<h2>SYNOPSIS</h2>
<p> ipa-modgroup [<i>OPTION</i>]&#8230; <i>group</i> </p>
<h2>DESCRIPTION</h2>
<p> Updates the members or description of <i>group</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;add</code>=<i>user1,user2,&#8230;usern</i></dt>
<dd> Add one or more users to the group</dd>
<dt><code>-d</code>, <code>&#8211;description</code>=<i>description</i></dt>
<dd> Modify the description of the group</dd>
<dt><code>-e</code>, <code>&#8211;groupdel</code>=<i>group1,group2,&#8230;groupn</i></dt>
<dd> Remove one or more groups from the group</dd>
<dt><code>-g</code>, <code>&#8211;groupadd</code>=<i>group1,group2,&#8230;groupn</i></dt>
<dd> Add one or more groups to the group</dd>
<dt><code>-r</code>, <code>&#8211;remove</code>=<i>user1,user2,&#8230;usern</i></dt>
<dd> Remove one or more users from the group</dd>
<dt><code>&#8211;addattr</code> <i>attr=value</i></dt>
<dd> Add a new attribute, or value to an existing attribute</dd>
<dt><code>&#8211;delattr</code> <i>attr=value</i></dt>
<dd> Remove an attribute and all values</dd>
<dt><code>&#8211;setattr</code> <i>attr=value</i></dt>
<dd> Set an attribute to a new value, removing all old ones</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Display the XML-RPC request and response for more verbose debugging output.</dd></dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
