---
title: "ps2frag(1)"
name: "ps2frag"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ps2frag/"
description: "ps2frag – obsolete shell script for the PSfrag system."
---

<h2 class="name">NAME</h2>
<p> ps2frag &#8211; obsolete shell script for the PSfrag system. </p>
<h2>IMPORTANT NOTICE</h2>
<p> The new PSfrag system no longer requires the ps2frag script; instead, it handles the processing entirely within TeX/LaTeX and DVIPS. I&#8217;m sure you will agree that never needing to run ps2frag again is a nice convenience! </p>
<p> However, there are two significant differences in the way this new version of PSfrag works. Please make yourself aware of them: </p>
<p> 1) XDvi is no longer able to determine where your PSfrag replacements should go, so instead it lines them up in a vertical list to the left of the figure. This allows you to confirm that they have been typeset properly, at least. However, to confirm that PSfrag <code>positions </code> your replacements properly, you will have to view the PostScript version of your file with a viewer like GhostView, or print it out. This seems to be the only disadvantage to the elimination of the pre-processing step. </p>
<p> 2) If you embed &#8216;	ex&#8217; commands inside your figures, you now need to explicitly _tell_ PSfrag to process these commands. To do so, use 
