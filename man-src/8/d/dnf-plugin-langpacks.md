---
title: "dnf-plugin-langpacks(8)"
name: "dnf-plugin-langpacks"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnf-plugin-langpacks/"
description: "dnf.langpacks.plugin – DNF langpacks plugin"
---

<p>dnf.langpacks.plugin &#8211; DNF langpacks plugin</p>
<h2>Synopsis</h2>
<p><code>dnf</code> [command] [package &#8230;]</p>
<h2>Description</h2>
<p><code>dnf-langpacks</code> is a plugin for dnf to install language packs. This plugin provides various commands. <i>commands</i> available are:<br />
 <i></i><code> * langavailable [language1] [language2] [&#8230;]</code><br />
This command allows user to find if language support is available for the given input languages.<br />
 <i></i><code> * langinfo [language1] [language2] [&#8230;]</code><br />
This command will show the user what packages will get installed by a given input languages.<br />
 <i></i><code> * langlist</code><br />
This command will show the user what languages are already installed(enabled)&nbsp;<wbr>on the system.<br />
 <i></i><code> * langinstall [language1] [language2] [&#8230;]</code><br />
This command will install the given input languages. If no input language is given then this<br />
command will try to add any missing language packages for all enabled languages on the system.<br />
 <i></i><code> * langremove [language1] [language2] [&#8230;]</code><br />
This command will remove the given input languages.<br />
 This plugin also provide option to enable additional languages. Just add locale code to langpacks_locale config item in /etc/dnf/plugins/langpacks.conf </p>
<h2>Examples</h2>
<p><code>To check if langpacks are available for language codes de, hi and language names Japanese and Portuguese&nbsp;<wbr>(Brazil).</code><br />
dnf langavailable de&nbsp;<wbr>&quot;Japanese&quot;&nbsp;<wbr>hi&nbsp;<wbr>&quot;Portuguese&nbsp;<wbr>(Brazil)&quot;<br />
<code>To check what packages will get installed for language codes de, hi and language names Japanese and Portuguese&nbsp;<wbr>(Brazil).</code><br />
dnf langinfo de&nbsp;<wbr>&quot;Japanese&quot;&nbsp;<wbr>hi&nbsp;<wbr>&quot;Portuguese&nbsp;<wbr>(Brazil)&quot;<br />
<code>To check what languages are already installed on your system.</code><br />
dnf langlist<br />
<code>To install the languages for language codes de, hi and language names Japanese and Portuguese&nbsp;<wbr>(Brazil).</code><br />
dnf langinstall de&nbsp;<wbr>&quot;Japanese&quot;&nbsp;<wbr>hi&nbsp;<wbr>&quot;Portuguese&nbsp;<wbr>(Brazil)&quot;<br />
<code>To remove the languages for language codes de, hi and language names Japanese and Portuguese&nbsp;<wbr>(Brazil).</code><br />
dnf langremove de&nbsp;<wbr>&quot;Japanese&quot;&nbsp;<wbr>hi&nbsp;<wbr>&quot;Portuguese&nbsp;<wbr>(Brazil)&quot; </p>
<h2>Notes</h2>
<p>These commands accept language codes or language names or mix of them as a input.<br />
General usage for end users is like this:<br />
1)&nbsp;<wbr>Use langavailable command to see if required language support is available.<br />
2)&nbsp;<wbr>Use langinfo command to know what packages will get installed.<br />
3)&nbsp;<wbr>Use langlist to know if you have required language already installed or not.<br />
4)&nbsp;<wbr>Use langinstall to install any new available language.<br />
5)&nbsp;<wbr>Or Use langremove to remove any installed language. </p>
<h2>Author</h2>
<p>Parag Nemade</p>
<h2>See Also</h2>
<pre><i>dnf (8)</i></pre>
<h2>Bugs</h2>
<p>Please report any bugs in Red Hat bugzilla, <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora">https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora</a> </p>
