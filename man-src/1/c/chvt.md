---

title: "chvt(1)"
name: "chvt"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chvt/"
description: "chvt – change foreground virtual terminal"
---

<p> <code>chvt</code> [<i>,option/</i>&#8230;] <i>N</i></p>
<p> The command <code>chvt</code> <i>N</i> makes <i>/dev/ttyN</i> the foreground terminal. (The corresponding screen is created if it did not exist yet. To get rid of unused VTs, use <code><a href="/docs/linux/man/1-deallocvt/">deallocvt</a></code>(1).) The key combination (Ctrl-)LeftAlt-F<i>N</i> (with <i>N</i> in the range 1-12) usually has a similar effect.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-V, &#8211;version</i></dt>
<dd> print program version and exit.</dd>
<dt><i>-h, &#8211;help</i></dt>
<dd> show this text and exit. </dd>
</dl>
