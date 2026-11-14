---
title: "secret-tool(1)"
name: "secret-tool"
section: "1"
letter: "s"
url: "/docs/linux/man/1-secret-tool/"
description: "secret-tool – Store and retrieve passwords"
---

<h2 class="name">NAME</h2>
<p> secret-tool &#8211; Store and retrieve passwords </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>secret-tool store </code><code>&#8211;label=&#8217;Label&#8217;</code><code>{attribute}</code><code>{value}</code><code> &#8230;</code></p>
<dt> <code>secret-tool lookup </code><code>{attribute}</code><code>{value}</code><code> &#8230;</code></p>
<dt> <code>secret-tool clear </code><code>{attribute}</code><code>{value}</code><code> &#8230;</code></p>
<dt> <code>secret-tool search </code><code>[&#8211;all]</code><code>{attribute}</code><code>{value}</code><code> &#8230;</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>secret-tool</code></p>
<dd>is a command line tool that can be used to store and retrieve passwords. </p>
<p> Each password is stored in an item. Items are uniquely identified by a set of attribute keys and values. When storing a password you must specify unique pairs of attributes names and values, and when looking up a password you provide the same attribute name and value pairs.</p>
<h2>STORE</h2>
<p> To store a password run <code>secret-tool</code> with the store argument. You must also specify a label for the passward with the &#8211;label argument. This label will be displayed in the password manager. </p>
<p> Make sure to pass a unique set of attributes names and values when storing a password. If the attributes match an already existing item, it will be updated instead of creating a new item. </p>
<p> If invoked from a terminal or tty, then the password to store will be prompted for and only one line will be accepted. </p>
<p> A password to store can also be piped in via stdin. The password will be the contents of stdin until EOF. If you provide a newline via stdin it will be stored as part of the password.</p>
<h2>LOOKUP</h2>
<p> To lookup a password run <code>secret-tool</code> with the lookup argument. Specify the same same attribute names and value pairs that you passed when storing the password. </p>
<p> If multiple items match the attribute provided, then the first password that is already unlocked will be returned. If necessary an item will be unlocked. </p>
<p> When printing the password to a terminal or tty, an extra newline will be added after the password.</p>
<h2>CLEAR</h2>
<p> To remove a password run <code>secret-tool</code> with the clear argument. Specify the same attirbute name and value pairs that you passed when storing the password. </p>
<p> All unlocked items that match the attributes will be removed.</p>
<h2>SEARCH</h2>
<p> This command searches for and prints details on matching items in secret service. Specify the same attribute and value pairs that you passed in when storing the password. You can use the following options: </p>
<p> <code>&#8211;all</code></p>
<dl>
<dt>
<dd> Return all matching results, rather than just the one of the matches. Without this option, the first unlocked match returned from the service will be printed.</dl>
<p> <code>&#8211;unlock</code></p>
<dl>
<dt>
<dd> Unlock items that are locked and then print out their details. Without this option, locked items are skipped.</dl>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Storing, retrieving, and clearing a password</code> </p>
<dl>
<dt>
<dd>
<pre>
$ secret-tool store --label='My password' key1 value1 key2 value2
Password: My password
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
$ secret-tool lookup key1 value1 key2 value2
My password
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
$ secret-tool clear key1 value1 key2 value2
</pre>
</dl>
<h2>Index</h2>
