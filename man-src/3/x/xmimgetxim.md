---
title: "xmimgetxim(3)"
name: "xmimgetxim"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmimgetxim/"
description: "XmImGetXIM — An input manager function that retrieves the input method associated with a specified widget"
---

<p><code>XmImGetXIM</code> &#8212; An input manager function that retrieves the input method associated with a specified widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/XmIm.h&gt;
<code>XIM XmImGetXIM</code>(
<code>Widget widget</code>);</pre>
<h2>Description</h2>
<p><code>XmImGetXIM</code> retrieves the XIM data structure representing the input method that the input manager has opened for the specified widget. If an input method has not been opened by a previous call to <code>XmImRegister</code>, the first time this routine is called it opens an input method using the <code>XmNinputMethod</code> resource for the VendorShell. If the <code>XmNinputMethod</code> is NULL, an input method is opened using the current locale. If it cannot open an input method, the function returns NULL.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of a widget registered with the input manager</dl>
<h2>Return</h2>
<p>Returns the input method for the current locale associated with the specified widget&#8217;s input manager; otherwise, returns NULL. The application is responsible for freeing the returned XIM by calling <code>XmImCloseXIM</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmimclosexim/">XmImCloseXIM</a></code>(3), <code><a href="/docs/linux/man/3-xmimgetxim/">XmImGetXIM</a></code>(3), <code><a href="/docs/linux/man/3-xmimmblookupstring/">XmImMbLookupString</a></code>(3), and <code><a href="/docs/linux/man/3-xmimregister/">XmImRegister</a></code>(3).</p>
