---
title: "jack_bufsize(1)"
name: "jack_bufsize"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack_bufsize/"
description: "jack_bufsize – JACK toolkit client to change the JACK buffer size"
---

<h2>NAME</h2>
<p> jack_bufsize &#8211; JACK toolkit client to change the JACK buffer size</p>
<h2>SYNOPSIS</h2>
<p> <code>jack_bufsize bufsize</code></p>
<h2>DESCRIPTION</h2>
<p> <code>jack_bufsize</code> jack_bufsize sets the size of the buffer (frames per period) used in JACK. This change happens on-line (the JACK server and its clients do not need to be restarted).<br />
 When invoked without arguments, it prints the current bufsize, and exits. </p>
<h2>Index</h2>
