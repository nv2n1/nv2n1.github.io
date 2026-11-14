---
title: "pcsc_scan(1)"
name: "pcsc_scan"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcsc_scan/"
description: "pcsc_scan – regularly scans every PC/SC readers connected to the host"
---

<h2 class="name">NAME</h2>
<p> pcsc_scan &#8211; regularly scans every PC/SC readers connected to the host </p>
<h2>SYNOPSIS</h2>
<p> <code>pcsc_scan [</code><i>options</i><code>]</code></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>pcsc_scan</code> command. </p>
<p> <code>pcsc_scan</code> is a program that regularly scans every PC/SC readers connected to the host </p>
<p> The normal way to exit the program is to use Control-C. </p>
<p> When <code>pcsc_scan</code> is started it asks <code>pcscd</code> the list of available smart card readers. The list is printed. A sequence number is printed before each reader. </p>
<p> Example:<br />
&nbsp;<wbr>PC/SC device scanner<br />
&nbsp;<wbr>V 1.1.0&nbsp;<wbr>(c)&nbsp;<wbr>2001-2002, Ludovic Rousseau<br />
&nbsp;<wbr>PC/SC lite version: 1.1.1<br />
&nbsp;<wbr>0: GemPC410 0 0<br />
&nbsp;<wbr>1: GemPC430 0 0 </p>
<p> When a card is inserted in any reader some information is printed:</p>
<dl>
<dt>date and time:</p>
<dd> Thu Jun 13 18:56:14 2002</p>
<dt>reader name:</p>
<dd> Reader 0 (GemPC410 0 0)</p>
<dt>card state and occured event:</p>
<dd> Card state: State has changed, Card inserted,</p>
<dt>ATR in case of card insertion:</p>
<dd> ATR: 3B 82 00 86 1E</p>
<dt>print an ATR analysis if the <code>ATR_analysis</code> command is available:</p>
<dd>
&nbsp;<wbr>ATR: 3B 82 00 86 1E<br />
&nbsp;<wbr>+&nbsp;<wbr>TS&nbsp;<wbr>=&nbsp;<wbr>3B &#8211;&gt;&nbsp;<wbr>Direct Convention<br />
&nbsp;<wbr>+&nbsp;<wbr>T0&nbsp;<wbr>=&nbsp;<wbr>82,&nbsp;<wbr><a href="/docs/linux/man/1-y/">Y</a>(1): 1000, K: 2&nbsp;<wbr>(historical bytes)<br />
<a href="/docs/linux/man/1-td/">TD</a>(1)&nbsp;<wbr>=&nbsp;<wbr>00 &#8211;&gt;&nbsp;<wbr>Y(i+1)&nbsp;<wbr>=&nbsp;<wbr>0000, Protocol T&nbsp;<wbr>=&nbsp;<wbr>0<br />
&nbsp;<wbr>&#8212;&#8211;<br />
&nbsp;<wbr>+&nbsp;<wbr>Historical bytes: 86 1E</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> print help</p>
<dt><code>-V</code></p>
<dd> print version number</p>
<dt><code>-n</code></p>
<dd> do not print ATR analysis</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-pcscd/">pcscd</a></code>(8), <code><a href="/docs/linux/man/1-atr_analysis/">ATR_analysis</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Ludovic Rousseau &lt;ludovic.rousseau [at] free.fr&gt; </p>
<h2>Index</h2>
