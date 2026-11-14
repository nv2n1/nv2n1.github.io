---
title: "espdiff(1)"
name: "espdiff"
section: "1"
letter: "e"
url: "/docs/linux/man/1-espdiff/"
description: "espdiff – apply the appropriate transformation to a set of patches"
---

<h2 class="name">NAME</h2>
<p> espdiff &#8211; apply the appropriate transformation to a set of patches </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>espdiff</code> [&#8211;deep-brainwave-mode] [&#8211;recurse] [&#8211;compare] [<i>file</i>&#8230;]</p>
<dt> <code>espdiff</code> {[&#8211;help] | [&#8211;version]}</dl>
<h2>DESCRIPTION</h2>
<p> <code>espdiff</code></p>
<dd>applies the appropriate transformation to a patch or set of patches, depending on what you intend to accomplish. </p>
<p> The input patches must be &#8220;clean&#8221;: in other words they must apply without fuzz or offsets in whichever order they are meant to be applied. The exception is if you intend <code>espdiff</code> to clean them for you (good luck). </p>
<p> You may find it useful to cross your fingers while the program performs its task, or to screw your eyes tight shut while imagining it doing the right thing.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;deep-brainwave-mode</code></p>
<dl>
<dt>
<dd> Probes your brain deeply in a manner that takes longer, but produces better extra sensory results.</dl>
<p> <code>&#8211;recurse</code></p>
<dl>
<dt>
<dd> Recurses neural pathways throughout all parts of the brain, in some cases determining code changes you might make far off in the future. You may feel a gentle tickling sensation when using this option.</dl>
<p> <code>&#8211;compare</code></p>
<dl>
<dt>
<dd> Allows the program to scan the current directory examining existing patches to determine areas of code you are likely to change again, and concentrating on these areas more closely.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of espdiff.</dl>
<h2>LIMITATIONS</h2>
<p> Do not use this program while sleep-walking, or before your first cup of coffee. </p>
<p> There are some cases in which it is not possible to determine what the intention of the user is. In these cases, you should construct the output you desire using an editor, and send the input files together with the desired output file to Tim Waugh &lt;twaugh [at] redhat.com&gt; asking for a new diff tool.</p>
<h2>AUTHORS</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Package maintainer</dl>
<p> <code>Mike Harris</code> &lt;mharris [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Conceptual designer</dl>
<h2>Index</h2>
