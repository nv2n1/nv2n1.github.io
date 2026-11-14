---
title: "yum-langpacks(8)"
name: "yum-langpacks"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yum-langpacks/"
description: "yum-langpacks – Plugin for yum"
---

<p>yum-langpacks &#8211; Plugin for yum</p>
<h2>Synopsis</h2>
<p><code>yum</code> [command] [package &#8230;]</p>
<h2>Description</h2>
<p><code>yum-langpacks</code> is a plugin for yum to install language packs. This plugin allows user various commands. <i>command</i> is one of:<br />
 <i></i> * langavailable [language1] [language2] [&#8230;]<br />
 <i></i> * langinfo [language1] [language2] [&#8230;]<br />
 <i></i> * langinstall [language1] [language2] [&#8230;]<br />
 <i></i> * langlist [language1] [language2] [&#8230;]<br />
 <i></i> * langremove [language1] [language2] [&#8230;] </p>
<dl>
<dt><code>langavailable</code></p>
<dd>This command allows user to find if language support is available for the given input languages.</p>
<dd>
<dt><code>langinfo</code></p>
<dd>This command allows user to check which packages will get installed when the given input language support is installed.</p>
<dd>
<dt><code>langinstall</code></p>
<dd>This command allows user to install language packs for the given input languages.</p>
<dd>
<dt><code>langlist</code></p>
<dd>This command prints list of the installed languages.</p>
<dd>
<dt><code>langremove</code></p>
<dd>This command allows user to remove the installed language packs for a given input languages. </p>
<h2>Examples</h2>
<p><code>To check what packages get installed for language codes es_ES, hi_IN and language names Japanese and Portuguese&nbsp;<wbr>(Brazil).</code><br />
yum langinfo es_ES&nbsp;<wbr>&quot;Japanese&quot;&nbsp;<wbr>hi_IN&nbsp;<wbr>&quot;Portuguese&nbsp;<wbr>(Brazil)&quot; </p>
<h2>Notes</h2>
<p>These commands accept language codes or language names or mix of them as a input. </p>
<h2>See Also</h2>
<pre><i>yum (8)</i></pre>
<h2>Bugs</h2>
<p>Please report any bugs in Red Hat bugzilla, <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora">https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora</a> </p>
