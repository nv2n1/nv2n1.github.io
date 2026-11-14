---
title: "amorad(8)"
name: "amorad"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amorad/"
description: "amorad – Amora (A Remote Mobile Assistant) daemon"
---

<p>amorad &#8211; Amora (A Remote Mobile Assistant) daemon</p>
<h2>Synopsis</h2>
<p>amorad [options] </p>
<h2>Description</h2>
<p>Amora is an application that enables you to control your PC desktop using a cellphone. It uses bluetooth to send mouse and keyboard events to the graphical session. With it you can control your slides in OpenOffice.org, movies or any other application. Amora also has a screenshot feature, where you can see a thumbnail in the cellphone screen of the currently focused window in your desktop. </p>
<p> The server (amorad) is written in C using Xlib and XTest to send events for X session and the POSIX socket API for I/O. It must be started by the user, inside a valid X session.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Help (usage) message </p>
<dt><code>-l</code></p>
<dd>Set a specific path for the log file </p>
<dt><code>-v</code></p>
<dd>Show program version and exit
</dl>
<h2>Amora Client</h2>
<p>In order to use amora, you need a mobile phone with amora-client installed and running. The current client is implemented in Python for S60 (Nokia cellphones).</p>
<h2>Bugs</h2>
<p>See the current bugs and open new ones in the project website. </p>
<h2>Credits</h2>
<p>Author: Adenilson Cavalcanti da Silva </p>
<p> Contributions from: Ademar de Souza Reis Jr., Alexis Younes, Thiago Marcos Santos, Wilson Prata and others;</p>
<h2>See Also</h2>
<p><code><a rel="nofollow" href="http://code.google.com/p/amora/">http://code.google.com/p/amora/</a></code> </p>
