---
title: "sysfs_streq(9)"
name: "sysfs_streq"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sysfs_streq/"
description: "sysfs_streq – return true if strings are equal, modulo trailing newline"
---

<p>sysfs_streq &#8211; return true if strings are equal, modulo trailing newline</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool sysfs_streq(const char&nbsp;<wbr>*&nbsp;<wbr></code><i>s1</i><code>, const char&nbsp;<wbr>*&nbsp;<wbr></code><i>s2</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>s1</i></p>
<dl>
<dd>
<dd>one string</dl>
<p> <i>s2</i></p>
<dl>
<dd>another string</dl>
<h2>Description</h2>
<p>This routine returns true iff two strings are equal, treating both NUL and newline-then-NUL as equivalent string terminations. It&#8217;s geared for use with sysfs input strings, which generally terminate with newlines but are compared against values without newlines.</p>
<h2>Copyright</h2>
