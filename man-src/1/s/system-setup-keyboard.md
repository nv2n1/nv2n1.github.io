---
title: "system-setup-keyboard(1)"
name: "system-setup-keyboard"
section: "1"
letter: "s"
url: "/docs/linux/man/1-system-setup-keyboard/"
description: "system-setup-keyboard – xorg.conf keyboard layout daemon"
---

<h2>NAME</h2>
<p> system-setup-keyboard &#8211; xorg.conf keyboard layout daemon</p>
<h2>SYNOPSIS</h2>
<pre>
system-setup-keyboard
</pre>
<h2>DESCRIPTION</h2>
<p> system-setup-keyboard is a daemon that monitors /etc/sysconfig/keyboard and writes out an xorg.conf.d snippet based on this file&#8217;s contents. Whenever the file is updated, system-setup-keyboard writes out the matching XKB configuration for the selected layout. This configuration applies to all keyboards but may be overwritten by other xorg.conf.d snippets or entries in the xorg.conf configuration file. </p>
<p> system-setup-keyboard is started on entering runlevel 5 by upstart or before starting prefdm by systemd depending on the used init system.</p>
<h2>KEYBOARD LAYOUTS</h2>
<p> The following conversion table is used to convert from the system keyboard layout to the XKB rules, model, layout and options. </p>
<table>
<tr VALIGN=top>
<td>Layout</td>
<td>XKB layout</td>
<td>model</td>
<td>variant</td>
<td>options
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>sr-cy</code></td>
<td>rs</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sv-latin1</code></td>
<td>se</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>cf</code></td>
<td>ca(fr)</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fr_CH-latin1</code></td>
<td>ch</td>
<td>pc105</td>
<td>fr</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fr-latin9</code></td>
<td>fr</td>
<td>pc105</td>
<td>latin9</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>dev</code></td>
<td>dev,us</td>
<td>pc105</td>
<td></td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>sk-qwerty</code></td>
<td>sk</td>
<td>pc105</td>
<td></td>
<td> qwerty
</td>
</tr>
<tr VALIGN=top>
<td><code>et</code></td>
<td>ee</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ar-qwerty-digits</code></td>
<td>ara,us</td>
<td>pc105</td>
<td>qwerty_digits</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>ar-azerty</code></td>
<td>ara,us</td>
<td>pc105</td>
<td>azerty</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>ie</code></td>
<td>ie</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ro-cedilla</code></td>
<td>ro</td>
<td>pc105</td>
<td>cedilla</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>es</code></td>
<td>es</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pl2</code></td>
<td>pl</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>cz-lat2</code></td>
<td>cz</td>
<td>pc105</td>
<td>qwerty</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ru</code></td>
<td>ru,us</td>
<td>pc105</td>
<td></td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>dvorak</code></td>
<td>us</td>
<td>pc105</td>
<td>dvorak</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>bg_bds-utf8</code></td>
<td>bg,us</td>
<td>pc105</td>
<td></td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>no</code></td>
<td>no</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>de-latin1-nodeadkeys</code></td>
<td>de</td>
<td>pc105</td>
<td>nodeadkeys</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ben</code></td>
<td>in,us</td>
<td>pc105</td>
<td>ben</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>ar-azerty-digits</code></td>
<td>ara,us</td>
<td>pc105</td>
<td>azerty_digits</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>ar-qwerty</code></td>
<td>ara,us</td>
<td>pc105</td>
<td>qwerty</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>tj</code></td>
<td>tj</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ro-std-cedilla</code></td>
<td>ro</td>
<td>pc105</td>
<td>std_cedilla</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>pt-latin1</code></td>
<td>pt</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>us-acentos</code></td>
<td>us</td>
<td>pc105</td>
<td>intl</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ro</code></td>
<td>ro</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>br-abnt2</code></td>
<td>br</td>
<td>abnt2</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ar-digits</code></td>
<td>ara,us</td>
<td>pc105</td>
<td>digits</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>cz-us-qwertz</code></td>
<td>cz,us</td>
<td>pc105</td>
<td></td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>it-ibm</code></td>
<td>it</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>bg_pho-utf8</code></td>
<td>bg,us</td>
<td>pc105</td>
<td>,phonetic</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>fr-pc</code></td>
<td>fr</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>dk</code></td>
<td>dk</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>be-latin1</code></td>
<td>be</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sg-latin1</code></td>
<td>ch</td>
<td>pc105</td>
<td>de_nodeadkeys</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fr-latin1</code></td>
<td>fr</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ua-utf</code></td>
<td>ua,us</td>
<td>pc105</td>
<td></td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>tml-uni</code></td>
<td>in,us</td>
<td>pc105</td>
<td>tam_TAB</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>it</code></td>
<td>it</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fr</code></td>
<td>fr</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>dk-latin1</code></td>
<td>dk</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fr_CH</code></td>
<td>ch</td>
<td>pc105</td>
<td>fr</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fi</code></td>
<td>fi</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sr-latin</code></td>
<td>rs</td>
<td>pc105</td>
<td>latin</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>hu</code></td>
<td>hu</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>it2</code></td>
<td>it</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>fi-latin1</code></td>
<td>fi</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ben-probhat</code></td>
<td>in,us</td>
<td>pc105</td>
<td>ben_probhat</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>croat</code></td>
<td>hr</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>jp106</code></td>
<td>jp</td>
<td>jp106</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>hu101</code></td>
<td>hu</td>
<td>pc105</td>
<td>qwerty</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>slovene</code></td>
<td>si</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>tml-inscript</code></td>
<td>in,us</td>
<td>pc105</td>
<td>tam</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>de-latin1</code></td>
<td>de</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ro-std</code></td>
<td>ro</td>
<td>pc105</td>
<td>std</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>ko</code></td>
<td>kr</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>us</code></td>
<td>us</td>
<td>pc105+inet</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>la-latin1</code></td>
<td>latam</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>gur</code></td>
<td>gur,us</td>
<td>pc105</td>
<td></td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>de</code></td>
<td>de</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>is-latin1</code></td>
<td>is</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>uk</code></td>
<td>gb</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>guj</code></td>
<td>in,us</td>
<td>pc105</td>
<td>guj</td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>trq</code></td>
<td>tr</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>mk-utf</code></td>
<td>mkd,us</td>
<td>pc105</td>
<td></td>
<td> grp:shifts_toggle,grp_led:scroll
</td>
</tr>
<tr VALIGN=top>
<td><code>nl</code></td>
<td>nl</td>
<td>pc105</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>sg</code></td>
<td>ch</td>
<td>pc105</td>
<td>de_nodeadkeys</td>
<td>
</td>
</tr>
</table>
<h2>FILES</h2>
<p> /etc/X11/xorg.conf.d/00-system-setup-keyboard.conf<br />
 /etc/init/system-setup-keyboard.conf<br />
 /lib/systemd/system/system-setup-keyboard.service</p>
<h2>AUTHORS</h2>
<p> Adel Gadllah &lt;adel.gadllah [at] gmail.com&gt;<br />
 Peter Hutterer &lt;peter.hutterer [at] redhat.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-xorg-conf/">xorg.conf</a>(5) </p>
<h2>Index</h2>
