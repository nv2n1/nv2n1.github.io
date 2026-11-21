---

title: "ieee1284_close(3)"
name: "ieee1284_close"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ieee1284_close/"
description: "ieee1284_close – close an open port"
---

<p> ieee1284_close &#8211; close an open port </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ieee1284.h&gt;
</code></pre>
<dl>
<dt> <code>int ieee1284_close(struct parport&nbsp;<wbr>*</code><i>port</i><code>);</code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>To close an open port and free any resources associated with it, call <code>ieee1284_close</code>.</dd>
<h2>RETURN VALUE</h2>
<p> <code>E1284_OK</code></p>
<dl>
<dt>
</dt><dd> The port is now closed.</dd></dl>
<p> <code>E1284_INVALIDPORT</code></p>
<dl>
<dt>
</dt><dd> The <i>port</i> parameter is invalid (perhaps it is not open, for instance).</dd></dl>
<p> <code>E1284_SYS</code></p>
<dl>
<dt>
</dt><dd> There was a problem at the operating system level. The global variable <i>errno</i> has been set appropriately.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>ieee1284_open</code>(3)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2003 Tim Waugh </p>
