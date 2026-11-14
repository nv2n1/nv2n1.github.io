---
title: "wimlib-imagex-join(1)"
name: "wimlib-imagex-join"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-join/"
description: "wimlib-imagex-join – Join split WIMs into a standalone one-part WIM"
---

<h2>NAME</h2>
<p> wimlib-imagex-join &#8211; Join split WIMs into a standalone one-part WIM</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex join</code> [<i>OPTION</i>&#8230;] <i>OUT_WIMFILE</i> <i>SPLIT_WIM_PART</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Joins the <i>SPLIT_WIM_PARTs</i> into a standalone one-part WIM <i>OUT_WIMFILE</i>. This command is also available as simply <code>wimjoin</code> if the appropriate hard link or batch file has been installed. </p>
<p> All parts of the split WIM must be specified. You probably want to do so using a shell wildcard. </p>
<p> <code>wimlib-imagex join</code> can join both non-pipable and pipable split WIMs.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;check</code></p>
<dd> When reading each <i>SPLIT_WIM_PART</i>, verify its integrity if the integrity table is present; additionally, when writing <i>OUT_WIMFILE</i>, write an integrity table. If this option is not specified, an integrity table will be included in <i>OUT_WIMFILE</i> if and only if one was present in the first part of the split WIM.</dl>
<h2>EXAMPLES</h2>
<p> Join a split WIM, with the parts named `windows*.swm&#8217; where the * is anything (usually the number of the part, except for the first part which may have no number), and write the joined WIM to the file `windows.wim&#8217;.</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex join windows.wim windows*.swm</dl>
<h2>NOTES</h2>
<p> <code>wimlib-imagex join</code> is roughly equivalent to:</p>
<dl>
<dt>
<dd>
<p> <code>wimlib-imagex export</code> <i>SWM_PART_1</i> &#8211;ref=&quot;<i>SWM_GLOB</i>&quot; all <i>OUT_WIMFILE</i></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-export/">wimlib-imagex-export</a></code>(1) </p>
<h2>Index</h2>
