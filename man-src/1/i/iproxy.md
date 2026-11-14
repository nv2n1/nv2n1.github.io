---
title: "iproxy(1)"
name: "iproxy"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iproxy/"
description: "iproxy – proxy that enables tcp service access to iPhone/iPod"
---

<h2 class="name">NAME</h2>
<p> iproxy &#8211; proxy that enables tcp service access to iPhone/iPod </p>
<h2>SYNOPSIS</h2>
<p> <code>iproxy </code> [LOCAL_TCP_PORT] [DEVICE_TCP_PORT] </p>
<h2>DESCRIPTION</h2>
<p> iproxy allows you to forward localhost ports to the device&#8212;allows SSH over USB on jailbroken devices, or allowing access the lockdown daemon (and then to all of the file access, sync, notification and backup services running on the device). </p>
<p> Example :<br />
&nbsp;<wbr>./iproxy 2222 22&nbsp;<wbr>&amp;<br />
&nbsp;<wbr>ssh -p 2222 root [at] localhost </p>
<h2>AUTHORS</h2>
<p> Nikias Bassen &lt;nikias [at] gmx.li&gt; </p>
<p> Paul Sladen &lt;libiphone [at] paul.sladen.org&gt; </p>
<p> Man page written to conform with Debian by Julien Lavergne. </p>
<h2>Index</h2>
