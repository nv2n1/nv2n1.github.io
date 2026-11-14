---
title: "elektra-keyname(3)"
name: "elektra-keyname"
section: "3"
letter: "e"
url: "/docs/linux/man/3-elektra-keyname/"
description: "Key :: Name Manipulation Methods –"
---

<h2 class="name">NAME</h2>
<p> Key :: Name Manipulation Methods &#8211; </p>
<p> Methods to do various operations on Key names.</p>
<h3>Functions</h3>
<p> const char * <code>keyName</code> (const Key *key) </p>
<p> ssize_t <code>keyGetNameSize</code> (const Key *key) </p>
<p> ssize_t <code>keyGetName</code> (const Key *key, char *returnedName, size_t maxSize) </p>
<p> ssize_t <code>keySetName</code> (Key *key, const char *newName) </p>
<p> ssize_t <code>keyGetFullNameSize</code> (const Key *key) </p>
<p> ssize_t <code>keyGetFullName</code> (const Key *key, char *returnedName, size_t maxSize) </p>
<p> const char * <code>keyBaseName</code> (const Key *key) </p>
<p> ssize_t <code>keyGetBaseNameSize</code> (const Key *key) </p>
<p> ssize_t <code>keyGetBaseName</code> (const Key *key, char *returned, size_t maxSize) </p>
<p> ssize_t <code>keyAddBaseName</code> (Key *key, const char *baseName) </p>
<p> ssize_t <code>keySetBaseName</code> (Key *key, const char *baseName) </p>
<p> const char * <code>keyOwner</code> (const Key *key) </p>
<p> ssize_t <code>keyGetOwnerSize</code> (const Key *key) </p>
<p> ssize_t <code>keyGetOwner</code> (const Key *key, char *returned, size_t maxSize) </p>
<p> ssize_t <code>keySetOwner</code> (Key *key, const char *owner) </p>
<h2>Detailed Description</h2>
<p> Methods to do various operations on Key names. </p>
<p> To use them: </p>
<pre><code>
#include &lt;kdb.h&gt;
</code></pre>
<p> These functions make it easier for c programmers to work with key names. Everything here can also be done with keySetName, described in key. </p>
<p> <code>Rules for Key Names</code>.RS 4 </p>
<p> When using Elektra to store your application&#8217;s configuration and state, please keep in mind the following rules:</p>
<dl>
<dt>*</p>
<dd> You are not allowed to create keys right under system or user.</p>
<dt>*</p>
<dd> You are not allowed to create folder keys right under system or user. They are reserved for very essential OS subsystems.</p>
<dt>*</p>
<dd> The keys for your application, called say <i>MyApp</i>, should be created under system/sw/MyApp and/or user/sw/MyApp.</p>
<dt>*</p>
<dd> It is suggested to make your application look for default keys under system/sw/MyApp/current and/or user/sw/MyApp/current. This way, from a sysadmin perspective, it will be possible to copy the system/sw/MyApp/current tree to something like system/sw/MyApp/old, and keep system clean and organized.</p>
<dt>*</p>
<dd> 
