---
title: "jackrec(1)"
name: "jackrec"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jackrec/"
description: "jackrec – JACK toolkit client for recording audio"
---

<h2>NAME</h2>
<p> jackrec &#8211; JACK toolkit client for recording audio</p>
<h2>SYNOPSIS</h2>
<p> <code>jackrec</code> -f filename -d seconds [ -b bitdepth ] port1 [ port2 &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>jackrec is a basic, but useful, audio recorder that will record</code> audio from 1 or more JACK ports to a file on disk. The file format is always RIFF/WAV, with samples stored as signed integers. The sample bit depth can be selected using the <i>-b</i> option. The file will have as many channels as there are ports specified on the command line &#8211; each channel will contain the data recorded from one port. The user should generally specify the duration (in seconds) using the <i>-d</i> option. If not specified, jackrec will record until terminated by a signal (eg. from Ctrl-c). </p>
<p> This application is not intended to be a heavy duty audio recorder, and originated as an example client to show how to handle threading and disk I/O in a JACK client. However, it is a useful, simple recorder and is included in the JACK toolkit as a result. </p>
<h2>Index</h2>
