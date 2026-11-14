---
title: "pgpewrap(1)"
name: "pgpewrap"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pgpewrap/"
description: "pgpewrap – Mutt command line munging tool"
---

<h2>NAME</h2>
<p> pgpewrap &#8211; Mutt command line munging tool </p>
<h2>SYNTAX</h2>
<p> <code>pgpewrap</code> [ <code>flags</code> ] &#8212; <code>prefix</code> [ <code>recipients</code> ] </p>
<h2>DESCRIPTION</h2>
<p> This is a little C program which does some command line munging: The first argument is a command to be executed. When <code>pgpewrap</code> encounters a &quot;&#8211;&quot; (dash-dash) argument, it will interpret the next argument as a prefix which is put in front of all following arguments. </p>
<h2>EXAMPLE</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>pgpewrap pgpe file &#8212; -r a b c </p>
<p> will execute: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>pgpe file -r a -r b -r c </p>
<p> This script is needed with PGP 5 and with GPG, since their command line interfaces can&#8217;t be properly served by mutt&#8217;s format mechanism. </p>
<h2>Index</h2>
