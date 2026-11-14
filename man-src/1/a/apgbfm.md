---
title: "apgbfm(1)"
name: "apgbfm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apgbfm/"
description: "apgbfm – APG Bloom filter management program"
---

<h2 class="name">NAME</h2>
<p> apgbfm &#8211; APG Bloom filter management program</p>
<h2>SYNOPSIS</h2>
<p> <code>apgbfm</code> <code>-f</code> <i>filter</i> <code>-n</code> <code>numofwords</code> [<code>-q</code>] [<code>-s</code>]<br />
 <code>apgbfm</code> <code>-f</code> <i>filter</i> <code>-d</code> <i>dictfile</i> [<code>-q</code>] [<code>-s</code>]<br />
 <code>apgbfm</code> <code>-f</code> <i>filter</i> <code>-a</code> <code>word</code> [<code>-q</code>]<br />
 <code>apgbfm</code> <code>-f</code> <i>filter</i> <code>-A</code> <i>dictfile</i> [<code>-q</code>]<br />
 <code>apgbfm</code> <code>-f</code> <i>filter</i> <code>-c</code> <code>word</code> [<code>-q</code>]<br />
 <code>apgbfm</code> <code>-f</code> <i>filter</i> <code>-C</code> <i>dictfile</i> [<code>-q</code>]<br />
 <code>apgbfm</code> <code>-i</code> <i>filter</i><br />
 <code>apgbfm</code> [<code>-v</code>] [<code>-h</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>apgbfm</code> is used to manage Bloom filter that is used to restrict password generation in <code>APG</code> pasword generation software. Usage of the Bloom filter allows to speed up password check for large dictionaries and has some other benefits. </p>
<p> The idea to use Bloom filter for that purpose is came from the description of the <code>OPUS</code> project <code>OPUS: Preventing Weak Password Choices</code> <i>Purdue Technical Report CSD-TR 92-028</i> writen by <i>Eugene H. Spafford</i>. </p>
<p> You can obtain this article from:<br />
 <i><a rel="nofollow" href="http://www.cerias.purdue.edu/homes/spaf/tech-reps/9128.ps">http://www.cerias.purdue.edu/homes/spaf/tech-reps/9128.ps</a></i><br />
 It has very nice description of Bloom filter and it&#8217;s advantages for password checking systems. </p>
<p> In simple words, <code>apgbfm</code> generates <i>n</i> hash values for every word and sets corresponding bits in filter file to 1. To check the word <code>apgbfm</code> generates the same hash functions for that word and if all <i>n</i> corresponding bits in filter file are set to 1 then it suppose that word exists in dicionary. <code>apgbfm</code> uses <code>SHA-1</code> as a hash function. </p>
<p> <code>apgbfm</code> can be used as standalone utility, not only with <code>apg</code>, or <code>apgd</code>. </p>
<dl>
<dt><code>WARNING !!!</code></p>
<dd> Filter file format can be changed in the future. I&#8217;ll try to make file formats compatible but i can not guaranty this.</p>
<dt><code>WARNING !!!</code></p>
<dd> <code>apgbfm</code> may slow down your computer during filter creation.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f </code><i>filter</i></p>
<dd> use <i>filter</i> as the name for Bloom filter filename.</p>
<dt><code>-i </code><i>filter</i></p>
<dd> print information about <i>filter</i>.</p>
<dt><code>-n numofwords</code></p>
<dd> create new empty filter for <code>numofwords</code> number of words. Useful when you want to fill filter dynamicaly.</p>
<dt><code>-d </code><i>dictfile</i></p>
<dd> create new filter from <i>dictfile</i>. It may take a lot of time to generate filter from a big dictionary. In that dictionary you may place words (one per line) that should not appear as generated passwords. For example: user names common words, etc. You even can use one of the dictionaries that come with <i>dictionary password crackers</i>. This check is case sensitive. For example, if you want to reject word &#8216;root&#8217;, you should insert in <i>dictfile</i> words: root, Root, RoOt, &#8230; , ROOT. To indicate that program is working <code>apgbfm</code> prints dot for every 100 words added in dictionary.</p>
<dt><code>-a word</code></p>
<dd> add <code>word</code> to the filter.</p>
<dt><code>-A </code><i>dictfile</i></p>
<dd> add all words from <i>dictfile</i> to the filter. To indicate that program is working <code>apgbfm</code> prints dot for every 100 words added in dictionary.</p>
<dt><code>-c word</code></p>
<dd> check <code>word</code> for appearance in the filter.</p>
<dt><code>-C </code><i>dictfile</i></p>
<dd> check every word from <i>dictfile</i> for appearance in the filter.</p>
<dt><code>-q</code></p>
<dd> quiet mode.</p>
<dt><code>-s</code></p>
<dd> create new filter in case-insensitive mode.</p>
<dt><code>-v</code></p>
<dd> print version information.</p>
<dt><code>-h</code></p>
<dd> print help information.</dl>
<h2>EXIT CODE</h2>
<p> On successful completion of its task, <code>apgbfm</code> will complete with exit code 0. An exit code of -1 indicates an error occurred. Textual errors are written to the standard error stream.</p>
<h2>FILES</h2>
<p> <code>None.</code></p>
<h2>BUGS</h2>
<p> <code>None.</code> If you&#8217;ve found one, please send bug description to the author. </p>
<p> This man page is Alpha too.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apg/">apg</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Adel I. Mirzazhanov, &lt;a-del [at] iname.com&gt;<br />
 Project home page: <a rel="nofollow" href="http://www.adel.nursat.kz/apg/">http://www.adel.nursat.kz/apg/</a> </p>
<h2>Index</h2>
