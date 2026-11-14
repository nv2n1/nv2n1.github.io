---
title: "perl584delta(1)"
name: "perl584delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl584delta/"
description: "perl584delta – what is new for perl v5.8.4"
---

<h2 class="name">NAME</h2>
<p> perl584delta &#8211; what is new for perl v5.8.4 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.3 release and the 5.8.4 release.</p>
<h2>Incompatible Changes</h2>
<p> Many minor bugs have been fixed. Scripts which happen to rely on previously erroneous behaviour will consider these fixes as incompatible changes :-) You are advised to perform sufficient acceptance testing on this release to satisfy yourself that this does not affect you, before putting this release into production. </p>
<p> The diagnostic output of Carp has been changed slightly, to add a space after the comma between arguments. This makes it much easier for tools such as web browsers to wrap it, but might confuse any automatic tools which perform detailed parsing of Carp output. </p>
<p> The internal dump output has been improved, so that non-printable characters such as newline and backspace are output in <tt>&quot;
