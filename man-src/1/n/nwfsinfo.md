---
title: "nwfsinfo(1)"
name: "nwfsinfo"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nwfsinfo/"
description: "nwfsinfo – Print some information about the file server"
---

<h2>NAME</h2>
<p> nwfsinfo &#8211; Print some information about the file server</p>
<h2>SYNOPSIS</h2>
<p> <code>nwfsinfo</code> [<code>-h</code>] [<code>-S</code> <i>server</i>] [<code>-t</code>] [<code>-i</code>] [<code>-d</code>] [<code>-e</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>nwfsinfo</code> prints some of the information the NetWare servers present without logging in. The options control what is printed. You should try the different options to find out what is printed when. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> With -h nwfsinfo prints a little help text.</dl>
<p> <code>-S</code> <i>server</i></p>
<dl>
<dt>
<dd> is the name of the server you want to know something about.</dl>
<p> <code>-t</code></p>
<dl>
<dt>
<dd> Print what the file server believes to be the current time.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Print the so-called file server description strings.</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> Print the extended file server information such as NetWare version, maximum connections an others.</dl>
<p> <code>-e</code></p>
<dl>
<dt>
<dd> List informations about NCP extensions loaded on server.</dl>
<h2>BUGS</h2>
<p> Description strings contain garbage on some Netware versions. </p>
<h2>AUTHOR</h2>
<p> This utility was originally written by Volker Lendecke. </p>
<h2>Index</h2>
