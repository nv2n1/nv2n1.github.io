---
title: "kf(1)"
name: "kf"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kf/"
description: "kf – securely forward tickets"
---

<h2 class="name">NAME</h2>
<p> <code>kf</code> &#8211; securely forward tickets </p>
<h2>SYNOPSIS</h2>
<p> [-<code>p </code><i>port</i> &#8211;<code>-port = </code><i>port</i> ] [-<code>l </code><i>login</i> &#8211;<code>-login = </code><i>login</i> ] [-<code>c </code><i>ccache</i> &#8211;<code>-ccache = </code><i>ccache</i> ] [-<code>F | -forwardable</code> ] [-<code>G | -no-forwardable</code> ] [-<code>h | -help</code> ] [-<code>-version</code> ] <i>host &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The program forwards tickets to a remote host through an authenticated and encrypted stream. Options supported are:</p>
<dl>
<dt> &#8211;<code>p </code><i>port</i> &#8211;<code>-port = </code><i>port</i></dt>
<dd>
</dd><dd>port to connect to</dd>
<dt> &#8211;<code>l </code><i>login</i> &#8211;<code>-login = </code><i>login</i></dt>
<dd>
</dd><dd>remote login name</dd>
<dt> &#8211;<code>c </code><i>ccache</i> &#8211;<code>-ccache = </code><i>ccache</i></dt>
<dd>
</dd><dd>remote cred cache</dd>
<dt><code>-F , -forwardable</code></dt>
<dd> forward forwardable credentials</dd>
<dt><code>-G , -no-forwardable</code></dt>
<dd> do not forward forwardable credentials</dd>
<dt><code>-h , -help</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd></dd></dl>
<p> is useful when you do not want to enter your password on a remote host but want to have your tickets one for example AFS. </p>
<p> In order for to work you will need to acquire your initial ticket with forwardable flag, i.e. <code>kinit &#8211;forwardable</code> </p>
<p> <code>telnet</code> is able to forward tickets by itself.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kinit/">kinit</a>(1), <a href="/docs/linux/man/1-telnet/">telnet</a>(1), <a href="/docs/linux/man/8-kfd/">kfd</a>(8) </p>
<h2>Index</h2>
