---
title: "intel_infoframes(1)"
name: "intel_infoframes"
section: "1"
letter: "i"
url: "/docs/linux/man/1-intel_infoframes/"
description: "intel_infoframes – View and change HDMI InfoFrames"
---

<h2>NAME</h2>
<p> intel_infoframes &#8211; View and change HDMI InfoFrames</p>
<h2>SYNOPSIS</h2>
<p> <code>intel_infoframes</code></p>
<h2>DESCRIPTION</h2>
<p> <code>intel_infoframes</code> is a tool to view and change the HDMI InfoFrames sent by the GPU. Its main purpose is to be used as a debugging tool. In some cases (e.g., when changing modes) the Kernel will undo the changes made by this tool. </p>
<p> Descriptions of the InfoFrame fields can be found on the HDMI and CEA-861 specifications. </p>
<p> Use the <code>-h</code> or <code>&#8211;help</code> options to learn how to use the command</p>
<h2>LIMITATIONS</h2>
<p> Not all HDMI monitors respect the InfoFrames sent to them. Only GEN 4 or newer hardware is supported yet.</p>
<h2>SEE ALSO</h2>
<p> HDMI specification, CEA-861 specification. </p>
<h2>Index</h2>
