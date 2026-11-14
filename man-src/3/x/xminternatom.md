---
title: "xminternatom(3)"
name: "xminternatom"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xminternatom/"
description: "XmInternAtom — A macro that returns an atom for a given name"
---

<p><code>XmInternAtom</code> &#8212; A macro that returns an atom for a given name</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/AtomMgr.h&gt;
<code>Atom XmInternAtom</code>(
<code>Display * display</code>,
<code>String name</code>,
<code>Boolean only_if_exists</code>);</pre>
<h2>Description</h2>
<p><code>XmInternAtom</code> returns an atom for a given name. The returned atom remains defined even after the client&#8217;s connection closes. The returned atom becomes undefined when the last connection to the X server closes.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server</p>
<dt><i>name</i></p>
<dd>Specifies the name associated with the atom you want returned. The value of <i>name</i> is case dependent.</p>
<dt><i>only_if_exists</i></p>
<dd>Specifies a Boolean value. If False, the atom is created even if it does not exist. (If it does not exist, the returned atom will be <code>None</code>.) If True, the atom is created only if it exists.</dl>
<h2>Return</h2>
<p>Returns an atom.</p>
