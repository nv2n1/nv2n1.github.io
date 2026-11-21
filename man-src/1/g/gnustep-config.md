---

title: "gnustep-config(1)"
name: "gnustep-config"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnustep-config/"
description: "gnustep-config – prints information about the current gnustep installation."
---

<p> gnustep-config &#8211; prints information about the current gnustep installation.</p>
<h2>SYNOPSIS</h2>
<p> <code>gnustep-config</code> [ <code>&#8211;variable=</code><i>variable</i> |<code>&#8211;objc-flags</code>|<code>&#8211;objc-libs</code>|<code>&#8211;base-libs</code>|<code>&#8211;gui-libs</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gnustep-config</code> can print information about the currently installed GNUstep system. It can output dependend on the options used the different flags used for compilation, but also the different internal variables used by the make system.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;variable=</code><i>variable</i></dt>
<dd> prints the value of the specified variable. Possible variables are:</dd>
<dl>
<dl>
<dl>
<dt>
</dt><dd>GNUSTEP_MAKEFILES</dd>
<dt>
</dt><dd>GNUSTEP_USER_DIR</dd>
<dt>
</dt><dd>GNUSTEP_USER_DEFAULTS_DIR</dd>
<dt>
</dt><dd>GNUSTEP_HOST</dd>
<dt>
</dt><dd>GNUSTEP_HOST_CPU</dd>
<dt>
</dt><dd>GNUSTEP_HOST_VENDOR</dd>
<dt>
</dt><dd>GNUSTEP_HOST_OS</dd>
<dt>
</dt><dd>GNUSTEP_IS_FLATTENED</dd>
<dt>
</dt><dd>GNUSTEP_xxx_APPS</dd>
<dt>
</dt><dd>GNUSTEP_xxx_TOOLS</dd>
<dt>
</dt><dd>GNUSTEP_xxx_LIBRARY</dd>
<dt>
</dt><dd>GNUSTEP_xxx_HEADERS</dd>
<dt>
</dt><dd>GNUSTEP_xxx_LIBRARIES</dd>
<dt>
</dt><dd>GNUSTEP_xxx_DOC</dd>
<dt>
</dt><dd>GNUSTEP_xxx_DOC_MAN</dd>
<dt>
</dt><dd>GNUSTEP_xxx_DOC_INFO</dd></dl>
</dl>
<p> where &#8216;xxx&#8217; could be any of &#8216;SYSTEM&#8217;, &#8216;NETWORK&#8217;, &#8216;LOCAL&#8217; and &#8216;USER&#8217;.</dl>
<dt><code>&#8211;objc-flags</code></dt>
<dd> prints all the flags required to compile an ObjC file </dd>
<dt><code>&#8211;objc-libs</code></dt>
<dd>
&nbsp;<wbr>prints all the flags required to link a pure ObjC program&nbsp;<wbr>(no foundation/gui) </dd>
<dt><code>&#8211;base-libs</code></dt>
<dd> prints all the flags required to link a command-line ObjC program (no gui) </dd>
<dt><code>&#8211;gui-libs</code></dt>
<dd> prints all the flags required to link a GUI ObjC program</dd></dl>
<h2>BUGS</h2>
<p> None known</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-gnustep/">GNUstep</a>(7)</p>
<h2>HISTORY</h2>
<p> Work on <code>gnustep-config</code> started in 2007 by Nicola Pero &lt;nicola.pero [at] meta-innovation.com&gt;</p>
<h2>AUTHORS</h2>
<p> This man page was written by Dennis Leeuw &lt;dleeuw [at] made-it.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2007 Free Software Foundation, Inc. </p>
<p> Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. </p>
