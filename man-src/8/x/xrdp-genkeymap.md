---
title: "xrdp-genkeymap(8)"
name: "xrdp-genkeymap"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xrdp-genkeymap/"
description: "xrdp-genkeymap – key map generator for XRDP"
---

<p><code>xrdp-genkeymap</code> &#8211; key map generator for XRDP</p>
<h2>Syntax</h2>
<p><code>xrdp-genkeymap</code> <i>file</i></p>
<h2>Description</h2>
<p><code>xrdp-genkeymap</code> extracts the key map used by the currently running X session to generated a mapping from Remote Desktop Protocol (RDP) key codes to X keysyms and Unicode code points. </p>
<h2>Options</h2>
<dl>
<dt><i>outfile</i></dt>
<dd>The key map information is stored in the file named <i>outfile</i>. </dd>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/xrdp/km-XXXXXXXX.ini</i></dt>
<dd>Files containing the keyboard mapping for language <i>XXXXXXXX</i>, which is a 8 digit hexadecimal number identifying the country and language code.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>00000405</code></dt>
<dd>cs Czech</dd>
<dt><code>00000407</code></dt>
<dd>de German</dd>
<dt><code>00000409</code></dt>
<dd>en-us US English</dd>
<dt><code>0000040c</code></dt>
<dd>fr French</dd>
<dt><code>00000410</code></dt>
<dd>it Italian</dd>
<dt><code>00000416</code></dt>
<dd>br Portuguese (Brazil)</dd>
<dt><code>00000419</code></dt>
<dd>ru Russian</dd>
<dt><code>0000041d</code></dt>
<dd>se Swedish</dd>
<dt><code>00000809</code></dt>
<dd>en-uk UK English</dd></dl>
</dl>
</dl>
<h2>Authors</h2>
<p>Jay Sorg &lt;jsorg71 [at] users.sourceforge.net&gt;<br/>
 Simone Fedele &lt;ilsimo [at] users.sourceforge.net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8), <code><a href="/docs/linux/man/1-setxkbmap/">setxkbmap</a></code>(1), <code><a href="/docs/linux/man/7-unicode/">unicode</a></code>(7), for more info on <code>xrdp</code> see <a rel="nofollow" href="http://www.xrdp.org/">http://www.xrdp.org/</a> </p>
