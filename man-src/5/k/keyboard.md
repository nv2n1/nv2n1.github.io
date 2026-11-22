---
title: "keyboard(5)"
name: "keyboard"
section: "5"
letter: "k"
url: "/docs/linux/man/5-keyboard/"
description: "keyboard – keyboard configuration file"
---

<p>keyboard &#8211; keyboard configuration file</p>
<h2>Description</h2>
<p>The <code>keyboard</code> file describes the properties of the keyboard. It is read by <code><a href="/docs/linux/man/1-setupcon/">setupcon</a></code>(1) in order to configure the keyboard on the console. In Debian systems the default keyboard layout is described in <i>/etc/default/keyboard</i> and it is shared between X and the console. The specification of the keyboard layout in the <code>keyboard</code> file is based on the XKB options XkbModel, XkbLayout, XkbVariant and XkbOptions. Unfortunately, there is little documentation how to use them. Description of all possible values for these options can be found in the file <i>xorg.lst</i>. You might want to read &#8220;The XKB Configuration Guide&#8221; by Kamil Toman and Ivan U. Pascal:</p>
<dl>
<dd><a rel="nofollow" href="http://www.xfree86.org/current/XKB-Config.html">http://www.xfree86.org/current/XKB-Config.html</a></dd></dl>
<p> Other possible readings are:</p>
<dl>
<dd><a rel="nofollow" href="https://wiki.archlinux.org/index.php/X_KeyBoard_extension">https://wiki.archlinux.org/index.php/X_KeyBoard_extension</a><br/>
 <a rel="nofollow" href="http://pascal.tsu.ru/en/xkb/">http://pascal.tsu.ru/en/xkb/</a><br/>
 <a rel="nofollow" href="http://www.charvolant.org/~doug/xkb/">http://www.charvolant.org/~doug/xkb/</a></dd></dl>
<p> The complete XKB-specification can be found on</p>
<dl>
<dd><a rel="nofollow" href="http://xfree86.org/current/XKBproto.pdf">http://xfree86.org/current/XKBproto.pdf</a></dd></dl>
<p> The file <code>keyboard</code> consists of variable settings in POSIX format:</p>
<dl>
<dd><i>VARIABLE</i>=<i>VALUE</i></dd></dl>
<p> Only one assignment is allowed per line. Comments (starting with &#8216;#&#8217;) are also allowed. </p>
<h2>Options</h2>
<p>The following variables can be set. </p>
<dl>
<dt><code>XKBMODEL</code></dt>
<dd>Specifies the XKB keyboard model name. Default: <code>pc105</code> on most platforms. </dd>
<dt><code>XKBLAYOUT</code></dt>
<dd>Specifies the XKB keyboard layout name. This is usually the country or language type of the keyboard. Default: <code>us</code> on most platforms </dd>
<dt><code>XKBVARIANT</code></dt>
<dd>Specifies the XKB keyboard variant components. These can be used to further specify the keyboard layout details. Default: not set. </dd>
<dt><code>XKBOPTIONS</code></dt>
<dd>Specifies the XKB keyboard option components. Options usually relate to the behavior of the special keys (&lt;Shift&gt;, &lt;Control&gt;, &lt;Alt&gt;, &lt;CapsLock&gt;, etc.) Default: not set. </dd>
<dt><code>BACKSPACE</code></dt>
<dd>Determines the behavior of &lt;BackSpace&gt; and &lt;Delete&gt; keys on the console. Allowed values: <code>bs,</code> del <code>and</code> guess. In most cases you can specify <code>guess</code> here, in which case the current terminal settings and the kernel of your operating system will be used to determine the correct value. Value <code>bs</code> specifies VT100-conformant behavior: &lt;BackSpace&gt; will generate <code>^H</code> (ASCII BS) and &lt;Delete&gt; will generate <code>^?</code> (ASCII DEL). Value <code>del</code> specifies VT220-conformant behavior: &lt;BackSpace&gt; will generate <code>^?</code> (ASCII DEL) and &lt;Delete&gt; will generate a special function sequence. </dd>
<dt><code>KMAP</code></dt>
<dd>Usually this variable will be unset but if you don&#8217;t want to use a XKB layout on the console, you can specify an alternative keymap here. Specify a file that is suitable as input for <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1) on Linux or for <code>kbdcontrol</code>(1) on FreeBSD. </dd>
</dl>
<h2>Files</h2>
<p>The standard location of the <code>keyboard</code> file is <i>/etc/default/keyboard</i>. Description of all available keyboard models, layouts, variants and options is available in <i>/usr/share/X11/xkb/rules/xorg.lst</i>. In most cases, in <i>/usr/share/keymaps/</i> or <i>/usr/share/syscons/keymaps/</i> you will find several keymaps that can be used with the variable <code>KMAP</code>.</p>
<h2>Notes</h2>
<p>In Debian systems, changes in <i>/etc/default/keyboard</i> do not become immediately visible to X. You should either reboot the system, or use </p>
<pre>udevadm trigger --subsystem-match=input --action=change</pre>
<p>In order to activate the changes on the console, run <code><a href="/docs/linux/man/1-setupcon/">setupcon</a></code>(1)<code>.</code> </p>
<h2>Bugs</h2>
<p>When a triple-layout is used on the console, i.e. a layout with three XKB groups, then the group toggling happens in the following way: Group1 -&gt; Group2 -&gt; Group1 -&gt; Group3. On FreeBSD triple- and quadruple-layouts are not supported on the console (only the first and the second layout are taken into account). The option <code>grp:shifts_toggle</code> is not supported on the console. </p>
<h2>Examples</h2>
<p>The following configuration will give you the standard US QWERTY layout (<code>us</code>). The key &lt;Menu&gt; will act as a compose key (<code>compose:menu</code>) and &lt;CapsLock&gt; will act as third control key (<code>ctrl:nocaps</code>). </p>
<pre>XKBLAYOUT=us
XKBVARIANT=
XKBOPTIONS=compose:menu,ctrl:nocaps</pre>
<p>In the following configuration the right &lt;Alt&gt; key (<code>grp:toggle</code>) will toggle between US QWERTY layout (<code>us</code>) and Greek (<code>gr</code>) layout. The option <code>grp_led:scroll</code> is ignored on the console but in X in means to use the ScrollLock keyboard led as indicator for the current layout (US or Greek). </p>
<pre>XKBLAYOUT=us,gr
XKBVARIANT=
XKBOPTIONS=grp:toggle,grp_led:scroll</pre>
<p>In the following configuration the &lt;Control&gt;+&lt;Shift&gt; key combination will toggle (<code>grp:ctrl_shift_toggle</code>) between French keyboard (<code>fr</code>) without dead keys (<code>nodeadkeys</code>) and British (<code>gb</code>) &#8220;Dvorak&#8221; (<code>dvorak</code>) keyboard. The right &lt;Win&gt; key will be a compose-key (<code>compose:rwin</code>) and the right &lt;Alt&gt; key will function as AltGr (<code>lv3:lalt_switch</code>). </p>
<pre>XKBLAYOUT=fr,gb
XKBVARIANT=nodeadkeys,dvorak
XKBOPTIONS=grp:ctrl_shift_toggle,compose:rwin,lv3:ralt_switch</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-setupcon/">setupcon</a></code>(1), <code><a href="/docs/linux/man/1-ckbcomp/">ckbcomp</a></code>(1), <code><a href="/docs/linux/man/5-console-setup/">console-setup</a></code>(5), <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), <code>kbdcontrol</code>(1) </p>
