---
title: "mgettydefs(4)"
name: "mgettydefs"
section: "4"
letter: "m"
url: "/docs/linux/man/4-mgettydefs/"
description: "mgettydefs – speed and terminal settings used by mgetty"
---

<p>mgettydefs &#8211; speed and terminal settings used by mgetty</p>
<h2>Description</h2>
<p>The <code>/etc/gettydefs</code> file contains information used by <i><a href="/docs/linux/man/1-mgetty/">mgetty</a></i>(1) to set up the speed and terminal settings for a line. It also supplies information on what the <i>login</i> prompt should look like. Many versions of UNIX have a version of <i><a href="/docs/linux/man/1-getty/">getty</a></i>(1) that also reads <code>/etc/gettydefs</code>. Both <i>mgetty</i> and <i>getty</i> expect similar formats in <code>/etc/gettydefs</code> except that, when used by <i>mgetty</i>, extended functionality is available. Even so, the additional functions are simply ignored by standard <i>getty</i>, so they can co-exist using the same file. Note, however, that <i>mgetty</i> can be compiled to use a file different from <code>/etc/gettydefs </code> if your <i>getty</i> gets upset about the extensions. This manual page documents <code>/etc/gettydefs</code> and describes the extended functionality available when used by <i><a href="/docs/linux/man/1-mgetty/">mgetty</a></i>(1). This document will refer to <i><a href="/docs/linux/man/1-getty/">getty</a></i>(1) except where <i>mgetty</i>&#8216;s behaviour is different. Each entry in <code>/etc/gettydefs</code> has the following format:</p>
<dl>
<dd>label# initial-flags # final-flags # login-prompt #next-label</dl>
<p> Each entry is followed by a blank line. The login prompt field can contain quoted characters which will be converted to other values. The sequences and their substitutions are:</p>
<dl>
<dt><code>
</code></p>
<dd>newline</p>
<dt><code></code></p>
<dd>carriage return</p>
<dt><code>\g</code></p>
<dd>beep</p>
<dt><code></code></p>
<dd>backspace</p>
<dt><code></code></p>
<dd>vertical tab (VT)</p>
<dt><code></code></p>
<dd>formfeed</p>
<dt><code>	</code></p>
<dd>tab</p>
<dt><code>\L</code></p>
<dd>portname</p>
<dt><code>\C</code></p>
<dd>time in <i><a href="/docs/linux/man/3-ctime/">ctime</a></i>(3) format.</p>
<dt><code>\N</code></p>
<dd>number of users currently logged in</p>
<dt><code>
