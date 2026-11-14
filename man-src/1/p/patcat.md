---
title: "patcat(1)"
name: "patcat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-patcat/"
description: "patcat – combine two GUS patches into one stereo extended GUS patch"
---

<h2>NAME</h2>
<p> patcat &#8211; combine two GUS patches into one stereo extended GUS patch </p>
<h2>SYNOPSIS</h2>
<p> <code>patcat left.pat right.pat</code> </p>
<h2>DESCRIPTION</h2>
<p> Patcat combines two ordinary monophonic GUS patches to make an extended GUS patch that has two channels. The left channel is from the first of the two patch files that were combined, and the right channel is from the second. The new extended GUS patch file that is created is named the same as the name of the left patch file but with &quot;-stereo&quot; appended. </p>
<p> Two monophonic extended GUS patches can also be combined, provided their velocity layers match up. </p>
<h2>OPTIONS</h2>
<p> There are no options. </p>
<h2>AUTHORS</h2>
<p> Greg Lee &lt;greg [at] ling.lll.hawaii.edu&gt;<br />
 Based on code from Hannu Savolainen </p>
<h2>Index</h2>
