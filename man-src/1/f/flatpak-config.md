---
title: "flatpak-config(1)"
name: "flatpak-config"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flatpak-config/"
description: "flatpak-config – Manage configuration"
---

<h2 class="name">NAME</h2>
<p> flatpak-config &#8211; Manage configuration </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flatpak config</code> [OPTION&#8230;]</p>
<dt> <code>flatpak config</code> [OPTION&#8230;] &#8211;set KEY VALUE</p>
<dt> <code>flatpak config</code> [OPTION&#8230;] &#8211;unset|&#8211;get KEY</dl>
<h2>DESCRIPTION</h2>
<dd>The flatpak config command shows or modifies the configuration of a flatpak installation. The following keys are supported: </p>
<p> <i>languages</i></p>
<dl>
<dt>
<dd> The languages that are included when installing Locale extensions. The value is a semicolon-separated list of two-letter language codes, or one of the special values * or all. If this key is unset, flatpak defaults to including the <i>extra-languages</i> key and the current locale.</dl>
<p> <i>extra-languages</i></p>
<dl>
<dt>
<dd> This key is used when languages is not set, and it defines extra locale extensions on top of the system configured languages. The value is a semicolon-separated list of locale identifiers (language, optional locale, optional codeset, optional modifier) as documented by <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) (for example, en;en_DK;zh_HK.big5hkscs;uz_UZ.utf8 [at] cyrillic).</dl>
<p> For configuration of individual remotes, see <code><a href="/docs/linux/man/1-flatpak-remote-modify/">flatpak-remote-modify</a></code>(1). For configuration of individual applications, see <code><a href="/docs/linux/man/1-flatpak-override/">flatpak-override</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help options and exit.</dl>
<p> <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Print all keys and their values.</dl>
<p> <code>&#8211;set</code></p>
<dl>
<dt>
<dd> Set key KEY to VALUE.</dl>
<p> <code>&#8211;unset</code></p>
<dl>
<dt>
<dd> Unset key KEY.</dl>
<p> <code>&#8211;get</code></p>
<dl>
<dt>
<dd> Print value of KEY.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dt>
<dd> Configure per-user installation.</dl>
<p> <code>&#8211;system</code></p>
<dl>
<dt>
<dd> Configure system-wide installation.</dl>
<p> <code>&#8211;installation=NAME</code></p>
<dl>
<dt>
<dd> Configure the system-wide installation specified by NAME among those defined in /etc/flatpak/installations.d/. Using <code>&#8211;installation=default</code> is equivalent to using <code>&#8211;system</code>.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print debug information during command processing.</dl>
<p> <code>&#8211;ostree-verbose</code></p>
<dl>
<dt>
<dd> Print OSTree debug information during command processing.</dl>
<h2>EXAMPLES</h2>
<p> <code>$ flatpak config &#8211;set languages &quot;sv;en;fi&quot;</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flatpak/">flatpak</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-remote-modify/">flatpak-remote-modify</a></code>(1), <code><a href="/docs/linux/man/1-flatpak-override/">flatpak-override</a></code>(1) </p>
<h2>Index</h2>
