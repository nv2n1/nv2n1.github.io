---
title: "mrtg-contrib(1)"
name: "mrtg-contrib"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-contrib/"
description: "mrtg-contrib – Contribution Guidelines for MRTG"
---

<h2 class="name">NAME</h2>
<p> mrtg-contrib &#8211; Contribution Guidelines for MRTG </p>
<h2>DESCRIPTION</h2>
<p> If you have written an extension to mrtg or created a bug fix, please consider contributing it to the project. As I get quite a number of contributions every week, here are a few guidelines which explain how to contribute so that I can use the contribution without too much additional work.</p>
<h3>Translations</h3>
<p> <font SIZE="-1">MRTG</font> messages have been translated to a number of languages but there are still many which have not been covered yet. If you want to add yours, go into the <i>mrtg-2.17.4/translate</i> directory and follow the instructions given in the <i></i><font SIZE="-1"><i>README</i></font><i></i> file.</p>
<h3>Patches</h3>
<p> When you have created your modification or extension to mrtg and want to submit it to me, please crate a patch for the files which you have modified. Do not send entire files unless they are new. </p>
<p> To create a patch, get hold of a copy of <font SIZE="-1">GNU</font> diff (Many Unix systems will have this installed already. In the <font SIZE="-1">NT</font> world you might want to get <a rel="nofollow" href="http://sources.redhat.com/cygwin/">http://sources.redhat.com/cygwin/</a> to get all the nice <font SIZE="-1">GNU</font> tools available.) and type </p>
<pre>
 diff --unified --ignore-space-change old-file new-file &gt; simple.patch
</pre>
<p> or if you have modified several files do </p>
<pre><code>
diff-- recursive-- unified-- ignore - space - change old - dir / new - dir / &gt; long.patch
</code></pre>
<h3>Documentation</h3>
<p> All documentation of mrtg is done with the perl <font SIZE="-1"><code>POD</code></font> system. If you want to learn about it, type </p>
<pre>
 perldoc perlpod
</pre>
<p> and read the instructions. If you have bugfixes or additions to the existing documents, make sure you modify the <font SIZE="-1"><code>POD</code></font> files and not the html or txt versions. </p>
<p> I take documentation very seriously. Whenever you create a new feature for mrtg which you want to get included in the official release, your patch must also contain modifications for the relevant <code>pod</code> file in the <i>doc</i> tree or for the documentation sections of <i>cfgmaker</i> and <i>indexmaker</i>.</p>
<h2>ADDRESS</h2>
<p> Send your patches, translations and contributions to Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
