---
title: "kbd(4)"
name: "kbd"
section: "4"
letter: "k"
url: "/docs/linux/man/4-kbd/"
description: "kbd – Keyboard input driver"
---

<p>kbd &#8211; Keyboard input driver</p>
<h2>Synopsis</h2>
<pre><code>Section &#34;InputDevice&#34;</code>
<code> Identifier &#34;</code><i>idevname</i><code>&#34;</code>
<code> Driver &#34;kbd&#34;</code>
&nbsp;<wbr>&nbsp;<wbr>...
<code>EndSection</code></pre>
<h2>Description</h2>
<p><code>kbd </code> is an Xorg input driver for keyboards. The driver supports the standard OS-provided keyboard interface, but these are currently only available to this driver module for Linux, BSD, and Solaris. This driver is the replacement for the built-in <code>keyboard</code> driver formerly included in Xorg. </p>
<p> The <code>kbd</code> driver functions as a keyboard input device.</p>
<h2>Configuration Details</h2>
<p>Depending on the X server version in use, input device options may be set in either a xorg.conf file, an xorg.conf.d snippet, or in the configuration files read by the Hardware Abstraction Layer (HAL) daemon, <a href="/docs/linux/man/1-hald/">hald</a>(1). </p>
<p> Please refer to <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) for general configuration details and for options that can be used with all input drivers. This section only covers configuration details specific to this driver. </p>
<p> The following driver <code>Options</code> are supported:</p>
<dl>
<dt><code>Option &#34;Device&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specify the keyboard device. Default: the OS&#8217;s default console keyboard input source. Property: &quot;Device Node&quot; (read-only).</p>
<dt><code>Option &#34;Protocol&#34; &#34;</code><i>string</i><code>&#34;</code></p>
<dd>Specify the keyboard protocol. Valid protocol types include:</dl>
<dl>
<dd>Standard, Xqueue.</dl>
<dl>
<dd>Not all protocols are supported on all platforms. Default: &quot;Standard&quot;.</dl>
<dl>
<dt><code>Option &#34;XLeds&#34; &#34;</code><i>ledlist</i><code>&#34;</code></p>
<dd>makes the keyboard LEDs specified in <i>ledlist</i> available for client use instead of their traditional function (Scroll Lock, Caps Lock and Num Lock). The numbers in the list are in the range 1 to 3. Default: empty list.</p>
<dt><code>Option &#34;XkbRules&#34; &#34;</code><i>rules</i><code>&#34;</code></p>
<dd>specifies which XKB rules file to use for interpreting the <code>XkbModel</code>, <code>XkbLayout</code>, <code>XkbVariant</code>, and <code>XkbOptions</code> settings. Default: &quot;base&quot; for most platforms. If you use the &quot;base&quot; value then you can find listing of all valid values for these four options in the <i>/usr/share/X11/xkb/rules/base.lst</i> file.</p>
<dt><code>Option &#34;XkbModel&#34; &#34;</code><i>modelname</i><code>&#34;</code></p>
<dd>specifies the XKB keyboard model name. Default: &quot;pc105&quot; for most platforms.</p>
<dt><code>Option &#34;XkbLayout&#34; &#34;</code><i>layoutname</i><code>&#34;</code></p>
<dd>specifies the XKB keyboard layout name. This is usually the country or language type of the keyboard. Default: &quot;us&quot; for most platforms.</p>
<dt><code>Option &#34;XkbVariant&#34; &#34;</code><i>variants</i><code>&#34;</code></p>
<dd>specifies the XKB keyboard variant components. These can be used to enhance the keyboard layout details. Default: not set.</p>
<dt><code>Option &#34;XkbOptions&#34; &#34;</code><i>options</i><code>&#34;</code></p>
<dd>specifies the XKB keyboard option components. These can be used to enhance the keyboard behaviour. Default: not set.</dl>
<p> For a list of available XKB options, see <code><a href="/docs/linux/man/7-xkeyboard-config/">xkeyboard-config</a>(7).</code></p>
<h2>Example</h2>
<p>The following xorg.conf fragment ensures that user will be able to switch between <i>us</i> and <i>sk</i> layouts by pressing the &quot;menu&quot; key. The scroll lock LED shows which layout is currently active. </p>
<p> The <code>XkbVariant</code> option defines which variants of the two layouts should be used. In case of the <i>us</i> layout its default variant is used. In case of the <i>sk</i> layout its <i>qwerty</i> variant is used. </p>
<pre><dl><dt><dd>Section &#34;InputDevice&#34;
<dl><dt><dd>Identifier &quot;Generic Keyboard&quot;
Driver &quot;kbd&quot;
Option &quot;CoreKeyboard&quot;
Option &quot;XkbRules&quot; &quot;base&quot;
Option &quot;XkbModel&quot; &quot;pc105&quot;
Option &quot;XkbLayout&quot; &quot;us,sk&quot;
Option &quot;XkbVariant&quot; &quot;,qwerty&quot;
Option &quot;XkbOptions&quot; &quot;grp:menu_toggle,grp_led:scroll&quot;
</dl>
EndSection
</dl></pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xorg/">Xorg</a>(1), <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5), <a href="/docs/linux/man/1-xserver/">Xserver</a>(1), <a href="/docs/linux/man/7-x/">X</a>(7). <a href="/docs/linux/man/7-hal/">hal</a>(7), <a href="/docs/linux/man/8-hald/">hald</a>(8), <a href="/docs/linux/man/5-fdi/">fdi</a>(5). <a href="/docs/linux/man/7-xkeyboard-config/">xkeyboard-config</a>(7). </p>
