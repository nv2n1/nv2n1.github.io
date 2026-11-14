---
title: "fedpkg-copr(1)"
name: "fedpkg-copr"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fedpkg-copr/"
---

<h2 class="name">NAME</h2>
 

 fedpkg-copr - COPR dist-git client based on fedpkg 

<h2>SYNOPSIS</h2>

 

 fedpkg-copr [ global_options ] command [ command_options ] [ command_arguments ] 

 fedpkg-copr help 

 fedpkg-copr command --help

<h2>DESCRIPTION</h2>

 

 This tool enables you to interact with COPR dist-git repository. Except it doesn't because COPR dist-git repos are currently closed. Currently, this tool only serves as srpm &quot;fetch&quot; tool for copr-backend service, so that it can build the srpms. 

 There are two differences in COPR dist-git when compared to Fedora dist-git: 

<dl>
<dt>
<dd> &bull; COPR repo URLs take form of /&lt;username&gt;/&lt;projectname&gt;/&lt;packagename&gt;.git</dl>
 

<dl>
<dt>
<dd> &bull; Other than just default branches are supported: mga6, cauldron, and custom</dl>

<h2>AUTHORS</h2>

 

 Michal Novotny &lt;clime [at] redhat.com&gt; 

<h2>Index</h2>


