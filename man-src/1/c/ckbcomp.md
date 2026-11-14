---
title: "ckbcomp(1)"
name: "ckbcomp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ckbcomp/"
description: "ckbcomp – compile a XKB keyboard description to a keymap suitable for loadkeys or kbdcontrol"
---

<h2 class="name">NAME</h2>
<p> ckbcomp &#8211; compile a XKB keyboard description to a keymap suitable for loadkeys or kbdcontrol</p>
<h2>SYNOPSIS</h2>
<p> <code>ckbcomp</code> [<i>OPTION</i>&#8230;]&nbsp;[<i>XKBLAYOUT</i>&nbsp;[<i>XKBVARIANT</i>&nbsp;[<i>XKBOPTIONS</i>]&#8230;]] </p>
<h2>DESCRIPTION</h2>
<p> The <code>ckbcomp</code> keymap compiler converts a description of an XKB keyboard layout into a console keymap that can be read directly by <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) or <code><a href="/docs/linux/man/1-kbdcontrol/">kbdcontrol</a></code>(1). </p>
<p> On its standard output <code>ckbcomp</code> dumps the generated keyboard definition. The most important difference between the arguments of <code><a href="/docs/linux/man/1-setxkbmap/">setxkbmap</a></code>(1) and the arguments of <code>ckbcomp</code> is the additional parameter <i>-charmap</i> when non-Unicode keyboard map is wanted. Without <i>-charmap</i> <code>ckbcomp</code> will generate Unicode keyboard. </p>
<h2>OPTIONS</h2>
<h3>General options</h3>
<dl>
<dt><code>-?</code>,<code>-help</code></p>
<dd> Print a usage message and exit.</p>
<dt><code>-charmap&nbsp;</code><i>charmap</i></p>
<dd> The encoding to use for the output keymap. There should be an character mapping table defining this encoding in <i>/usr/share/consoletrans</i>. Definitions of the following charmaps are provided: <code>ARMSCII-8</code>, <code>CP1251</code>, <code>CP1255</code>, <code>CP1256</code>, <code>GEORGIAN-ACADEMY</code>, <code>GEORGIAN-PS</code>, <code>IBM1133</code>, <code>ISIRI-3342</code>, <code>ISO-8859-1</code>, <code>ISO-8859-2</code>, <code>ISO-8859-3</code>, <code>ISO-8859-4</code>, <code>ISO-8859-5</code>, <code>ISO-8859-6</code>, <code>ISO-8859-7</code>, <code>ISO-8859-8</code>, <code>ISO-8859-9</code>, <code>ISO-8859-10</code>, <code>ISO-8859-11</code>, <code>ISO-8859-13</code>, <code>ISO-8859-14</code>, <code>ISO-8859-15</code>, <code>ISO-8859-16</code>, <code>KOI8-R</code>, <code>KOI8-U</code>, <code>TIS-620</code> and <code>VISCII</code>. </p>
<dt><code>-I</code><i>dir</i></p>
<dd> Look in the top-level directory <i>dir</i> for files included by the keymap description. This option may be used multiple times. If a file can not be found in any of the specified directories, it will be searched also in some other standard locations, such as <i>/etc/console-setup/ckb</i>, <i>/usr/share/X11/xkb</i> and <i>/etc/X11/xkb</i> </p>
<dt><code>-v&nbsp;</code><i>level</i></p>
<dd> Set level of detail for listing. The argument <i>level</i> must be a number from 1 to 10.</p>
<dt><code>-compact</code></p>
<dd> Generate a compact keymap with at most two xkb groups and two levels in each or only one xkb-group and up to four levels.</p>
<dt><code>-freebsd</code></p>
<dd> Generate a keymap for FreeBSD.</p>
<dt><code>-backspace&nbsp;</code>[<code>bs</code>|<code>del</code>]</p>
<dd> Specifies the behaviour of the <font SIZE="-1">&lt;BackSpace&gt;</font> and <font SIZE="-1">&lt;Delete&gt;</font> keys. Value <code>bs</code> specifies VT100-conformant behaviour: <font SIZE="-1">&lt;BackSpace&gt;</font> will generate <code>^H</code> <font SIZE="-1">(ASCII BS)</font> and <font SIZE="-1">&lt;Delete&gt;</font> will generate <code>^?</code> <font SIZE="-1">(ASCII DEL).</font> Value <code>del</code> specifies VT220-conformant behavior: <font SIZE="-1">&lt;BackSpace&gt;</font> will generate <code>^?</code> <font SIZE="-1">(ASCII DEL)</font> and <font SIZE="-1">&lt;Delete&gt;</font> will generate a special function sequence. </p>
</dl>
<h3>XKB Keyboard Description</h3>
<p> The keyboard layout, variant and options components can be also specified directly on the command line. See the synopsis of the command.</p>
<dl>
<dt><code>-symbols&nbsp;</code><i>name</i></p>
<dd> Specifies the symbols component name of the XKB keyboard description.</p>
<dt><code>-keycodes&nbsp;</code><i>name</i></p>
<dd> Specifies the keycodes component name of the XKB keyboard description.</p>
<dt><code>-rules&nbsp;</code><i>name</i></p>
<dd> The name of the rules file to use.</p>
<dt><code>-model&nbsp;</code><i>name</i></p>
<dd> Specifies the keyboard model used to choose the component names.</p>
<dt><code>-layout&nbsp;</code><i>name</i></p>
<dd> Specifies the layout used to choose the component names.</p>
<dt><code>-variant&nbsp;</code><i>name</i></p>
<dd> Specifies the layout variant used to choose the component names.</p>
<dt><code>-option&nbsp;</code><i>name</i></p>
<dd> Adds an option used to choose component names. </p>
</dl>
<h2>FILES</h2>
<p> <i>/usr/share/consoletrans</i><br />
 <i>/etc/console-setup/ckb</i><br />
 <i>/usr/share/X11/xkb</i><br />
 <i>/etc/X11/xkb</i> </p>
<h2>NOTES</h2>
<p> If the option <i>-freebsd</i> is used together with <i>-backspace del</i>, then the key <font SIZE="-1">&lt;Delete&gt;</font> will generate the special code <code>fkey70</code>. It is your responsibility to assign the appropriate sequence to this special code by using the following command: </p>
<pre>
kbdcontrol -f 70 &quot;`printf '[3~'`&quot;
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-keyboard/">keyboard</a></code>(5), <code><a href="/docs/linux/man/1-setxkbmap/">setxkbmap</a></code>(1) </p>
<h2>Index</h2>
