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
<dt><i>outfile</i></p>
<dd>The key map information is stored in the file named <i>outfile</i>. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/xrdp/km-XXXXXXXX.ini</i></p>
<dd>Files containing the keyboard mapping for language <i>XXXXXXXX</i>, which is a 8 digit hexadecimal number identifying the country and language code.</p>
<dl>
<dd>
<dl>
<dt><code>00000405</code></p>
<dd>cs Czech</p>
<dt><code>00000407</code></p>
<dd>de German</p>
<dt><code>00000409</code></p>
<dd>en-us US English</p>
<dt><code>0000040c</code></p>
<dd>fr French</p>
<dt><code>00000410</code></p>
<dd>it Italian</p>
<dt><code>00000416</code></p>
<dd>br Portuguese (Brazil)</p>
<dt><code>00000419</code></p>
<dd>ru Russian</p>
<dt><code>0000041d</code></p>
<dd>se Swedish</p>
<dt><code>00000809</code></p>
<dd>en-uk UK English</dl>
</dl>
</dl>
<h2>Authors</h2>
<p>Jay Sorg &lt;jsorg71 [at] users.sourceforge.net&gt;<br />
 Simone Fedele &lt;ilsimo [at] users.sourceforge.net&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-xrdp/">xrdp</a></code>(8), <code><a href="/docs/linux/man/1-setxkbmap/">setxkbmap</a></code>(1), <code><a href="/docs/linux/man/7-unicode/">unicode</a></code>(7), for more info on <code>xrdp</code> see <a rel="nofollow" href="http://www.xrdp.org/">http://www.xrdp.org/</a> </p>
