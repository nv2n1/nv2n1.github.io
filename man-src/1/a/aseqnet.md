---
title: "aseqnet(1)"
name: "aseqnet"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aseqnet/"
description: "aseqnet – ALSA sequencer connectors over network"
---

<h2 class="name">NAME</h2>
<p> aseqnet &#8211; ALSA sequencer connectors over network</p>
<h2>SYNOPSIS</h2>
<p> <code>aseqnet</code> [remotehost] </p>
<h2>DESCRIPTION</h2>
<p> <code>aseqnet</code> is an ALSA sequencer client which sends and receives event packets over network. Suppose two hosts connected by network, <i>hostA</i> as a server and <i>hostB</i> as a client. The ALSA sequencer system must be running on both hosts. For creating the server port, run the following on hostA:</p>
<dl>
<dt>
<dd> hostA% aseqnet<br />
 sequencer opened: 128:0</dl>
<p> Then a user client 128 with port 0 was opened on hostA. (The client number may vary.) For creating the (network-)client port, run <code>aseqnet</code> with the hostname of the server:</p>
<dl>
<dt>
<dd> hostB% aseqnet hostA<br />
 sequencer opened: 132:0</dl>
<p> Now all events sent to hostA:128:0 are transferred to hostB:132:0, and vice versa. </p>
<p> The ports created by <code>aseqnet</code> can be connected arbitrary to other sequencer ports via <code><a href="/docs/linux/man/1-aconnect/">aconnect</a>(1).</code> For example, to connect hostB:132:0 to a MIDI output device 65:0:</p>
<dl>
<dt>
<dd> hostB% aconnect 132:0 65:0</dl>
<p> Then events to hostA:128:0 will be delivered to hostB:65:0. The following command plays MIDI on <i>hostB.</i></p>
<dl>
<dt>
<dd> hostA% pmidi -p 128:0 foo.mid</dl>
<p> The multiple clients may exist simultaneously. If <i>hostC</i> is connected as a client to hostA, events from from hostA are sent to all connected network clients, i.e. hostB and hostC. However, only one connection is allowed from a client to a server. </p>
<p> To disconnect network, stop all clients before server by ctrl-C or sending signal to them. The server will automatically quit. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p port</code></p>
<dd> Specify the TCP port number or TCP service name.</p>
<dt><code>-s addr</code></p>
<dd> Subscribe to the given address for read automatically.</p>
<dt><code>-d addr</code></p>
<dd> Subscribe to the given address for write automatically.</p>
<dt><code>-n name</code></p>
<dd> Specify the midi name of the process.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-aconnect/">aconnect</a>(1), <a href="/docs/linux/man/1-pmidi/">pmidi</a>(1) </p>
<h2>AUTHOR</h2>
<p> Takashi Iwai &lt;tiwai [at] suse.de&gt;. </p>
<h2>Index</h2>
