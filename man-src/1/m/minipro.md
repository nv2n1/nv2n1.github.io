---
title: "minipro(1)"
name: "minipro"
section: "1"
letter: "m"
url: "/docs/linux/man/1-minipro/"
description: "minipro – flash various chips with Minipro TL866XX series of programmers from autoelectric.cn."
---

<h2>NAME</h2>
<p> minipro &#8211; flash various chips with Minipro TL866XX series of programmers from autoelectric.cn.</p>
<h2>SYNOPSIS</h2>
<p> <code>minipro</code> [-p<code> device]</code> [-c<code> code|data|config]</code> [-r|-w<code> filename]</code> [-e]<code>[-u]</code>[-P]<code>[-i|-I]</code> </p>
<p> <code>miniprohex</code> [-p<code> device]</code> [-c<code> code|data|config]</code> [-r|-w<code> filename]</code> [-e]<code>[-u]</code>[-P]<code>[-i|-I]</code> </p>
<p> If <code>-c</code> is omitted and <code>-r</code> is specified then the code, data (if applicable) and config (if applicable) are getting read in filename.$ext, filename.eeprom.$ext and filename.config.txt correspondingly. If <code>-c</code> is omitted and <code>-w</code> is specified then <code>-c code</code> is getting enforced. </p>
<p> The <code>-i</code> and <code>-I</code> options enable use of ICSP port for TL866A models. The former enables the voltage supply on the Vcc pin of the ICSP port while the latter leaves it off. </p>
<h2>DESCRIPTION</h2>
<p> <i>minipro</i> is an opensource tool that aims to create a complete cross-platform replacement for proprietary utility from autoelectric.cn. Currently it&#8217;s supporting more than 13000 of target devices &#8211; including AVRs, PICs as well as a huge number of other microcontrollers and various BIOSes. </p>
<h2>Index</h2>
