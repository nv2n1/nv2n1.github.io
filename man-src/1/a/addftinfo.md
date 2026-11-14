---
title: "addftinfo(1)"
name: "addftinfo"
section: "1"
letter: "a"
url: "/docs/linux/man/1-addftinfo/"
description: "addftinfo – add information to troff font files for use with groff"
---

<h2 class="name">NAME</h2>
<p> addftinfo &#8211; add information to troff font files for use with groff </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-asc-height </code><i>n</i> ] [ <code>-body-depth </code><i>n</i> ] [ <code>-body-height </code><i>n</i> ] [ <code>-cap-height </code><i>n</i> ] [ <code>-comma-depth </code><i>n</i> ] [ <code>-desc-depth </code><i>n</i> ] [ <code>-fig-height </code><i>n</i> ] [ <code>-x-height </code><i>n</i> ] <i>res</i> <i>unitwidth</i> <i>font</i> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>addftinfo</code> reads a troff font file and adds some additional font-metric information that is used by the groff system. The font file with the information added is written on the standard output. The information added is guessed using some parametric information about the font and assumptions about the traditional troff names for characters. The main information added is the heights and depths of characters. The <i>res</i> and <i>unitwidth</i> arguments should be the same as the corresponding parameters in the DESC file; <i>font</i> is the name of the file describing the font; if <i>font</i> ends with <code>I</code> the font will be assumed to be italic.</p>
<h2>OPTIONS</h2>
<p> <code>-v</code> prints the version number. </p>
<p> All other options change one of the parameters that are used to derive the heights and depths. Like the existing quantities in the font file, each <i>value</i> is in inches/<i>res</i> for a font whose point size is <i>unitwidth</i>. <i>param-option</i> must be one of:</p>
<dl>
<dt><code>-x-height</code></p>
<dd> The height of lowercase letters without ascenders such as x.</p>
<dt><code>-fig-height</code></p>
<dd> The height of figures (digits).</p>
<dt><code>-asc-height</code></p>
<dd> The height of characters with ascenders, such as b, d or l.</p>
<dt><code>-body-height</code></p>
<dd> The height of characters such as parentheses.</p>
<dt><code>-cap-height</code></p>
<dd> The height of uppercase letters such as A.</p>
<dt><code>-comma-depth</code></p>
<dd> The depth of a comma.</p>
<dt><code>-desc-depth</code></p>
<dd> The depth of characters with descenders, such as p, q, or y.</p>
<dt><code>-body-depth</code></p>
<dd> The depth of characters such as parentheses.</dl>
<p> <code>addftinfo</code> makes no attempt to use the specified parameters to guess the unspecified parameters. If a parameter is not specified the default will be used. The defaults are chosen to have the reasonable values for a Times font.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5), <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7) </p>
<p> You can view a man page <i>name</i><code>(</code><i>n</i><code>)</code> with</p>
<dl>
<dt>
<dd> <code>man</code><i> n name</i></dl>
<p> in text mode and with</p>
<dl>
<dt>
<dd> <code>groffer</code><i> n name</i></dl>
<p> in graphical mode (PDF, etc.). </p>
<h2>Index</h2>
