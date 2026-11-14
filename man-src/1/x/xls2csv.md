---
title: "xls2csv(1)"
name: "xls2csv"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xls2csv/"
description: "xls2csv – reads MS-Excel file and puts its content as comma-separated data on standard output"
---

<h2>NAME</h2>
<p> xls2csv &#8211; reads MS-Excel file and puts its content as comma-separated data on standard output</p>
<h2>SYNOPSIS</h2>
<p> <code>xls2csv </code>[<code>-xlV</code>] [<code>-f</code> <i> format </i>] [<code>-b</code> <i> string </i>] [<code>-s</code> <i> charset </i>] [<code>-d</code> <i> charset </i>] [-q <i> number </i>] [<code>-c</code> <i> char</i>] <i>files</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>xls2csv </code> reads MS-Excel spreadsheet and dumps its content as comma-separated values to stdout. Numbers are printed without delimiters, strings are enclosed in the double quotes. Double-quotes inside string are doubled.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-x</code></p>
<dd> print unknown Unicode chars as 
