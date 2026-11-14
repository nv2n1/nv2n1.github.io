---
title: "autosp(1)"
name: "autosp"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autosp/"
description: "autosp – preprocessor to generate note-spacing commands for MusiXTeX scores"
---

<h2 class="name">NAME</h2>
<p> autosp &#8211; preprocessor to generate note-spacing commands for MusiXTeX scores</p>
<h2>SYNOPSIS</h2>
<p> <code>autosp </code> [<code>-v | &#8211;version | -h | &#8211;help</code>] </p>
<p> <code>autosp</code> [<code>-d | &#8211;dotted</code>] [<code>-l | &#8211;log</code>] <i>infile</i>[.aspc] [<i>outfile</i>[<i></i>.tex]] </p>
<h2>DESCRIPTION</h2>
<p> This program makes it easier to create MusiXTeX scores by converting (non-standard) commands of the form notes &#8230; n into one or more conventional note-spacing commands (
otes \Notes \NOtes &#8230;), determined by the actual note values, with \sk spacing commands inserted as necessary. The coding for an entire measure can be entered one part at a time, without concern for note-spacing changes within the part or spacing requirements of other parts. </p>
<p> For example, if applied to </p>
<pre>
    notes\qa J\qa K&amp;
