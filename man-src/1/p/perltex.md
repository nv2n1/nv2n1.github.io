---
title: "perltex(1)"
name: "perltex"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perltex/"
description: "perltex – enable LaTeX macros to be defined in terms of Perl code"
---

<h2 class="name">NAME</h2>
<p> perltex &#8211; enable LaTeX macros to be defined in terms of Perl code </p>
<h2>SYNOPSIS</h2>
<p> perltex [<code>&#8211;help</code>] [<code>&#8211;latex</code>=<i>program</i>] [<code>&#8212;</code>[<code>no</code>]<code>safe</code>] [<code>&#8211;permit</code>=<i>feature</i>] [<code>&#8211;makesty</code>] [<i>latex options</i>]</p>
<h2>DESCRIPTION</h2>
<p> LaTeX &#8212; through the underlying TeX typesetting system &#8212; produces beautifully typeset documents but has a macro language that is difficult to program. In particular, support for complex string manipulation is largely lacking. Perl is a popular general-purpose programming language whose forte is string manipulation. However, it has no typesetting capabilities whatsoever. </p>
<p> Clearly, Perl&#8217;s programmability could complement LaTeX&#8217;s typesetting strengths. <code>perltex</code> is the tool that enables a symbiosis between the two systems. All a user needs to do is compile a LaTeX document using <code>perltex</code> instead of <code>latex</code>. (<code>perltex</code> is actually a wrapper for <code>latex</code>, so no <code>latex</code> functionality is lost.) If the document includes a <tt>&quot;
