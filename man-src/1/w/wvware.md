---
title: "wvware(1)"
name: "wvware"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wvware/"
description: "wvWare – convert msword documents"
---

<p>wvWare &#8211; convert msword documents</p>
<h2>Synopsis</h2>
<p><code>wvWare [-c charset] [&#8211;charset charset] [-p password] [&#8211;password password] [-x config.xml] [&#8211;config config.xml] [-d dir] [&#8211;dir dir] filename</code> </p>
<h2>Description</h2>
<p><i>wvWare converts word documents into other formats</i> such as PS,PDF,HTML,LaTeX,DVI,ABW</p>
<h3>Options</h3>
<dl COMPACT>
<dt><i>-c charset, &#8211;charset charset</i></p>
<dd>word 97 documents are stored in one of two formats, either in 8 bit windows codepages or in 16 bit unicode. The unicode can be converted easily into utf-8, and the codepages are promoted to unicode and converted from there, except for the western european codepage which is always converted to iso-5589-15 if possible. This is the default behaviour. While it is possible to convert into other formats or to force a conversion to a particular format, it is not recomended as you don&#8217;t get a guarantee that the output will be correct. For instance, if you convert an english document into koi8-r encoding then it will be wrong, but if you are sure then you can override the default output format. The charsets that are available depend on your system: systems using the gnu libc 2 and above can convert to just about anything; systems that at, wv configure time, prove to be inadequate for charset conversion use wv&#8217;s internal conversion formats which are a small subset of the possible conversions, namely: utf-8 iso-5589-15 koi8-r tis-620</p>
<dt><i>-p password, &#8211;password password</i></p>
<dd>Due to heroic work done by a great team of workers, the wv library can decrypt password protected word 97 and older versions of word documents given the correct password.</p>
<dt><i>-d dir, &#8211;dir dir</i></p>
<dd>If dir is used then any created graphics will be placed in this directory. The default is the directory in which the word document resides.</p>
<dt><i>-x config.xml, &#8211;config config.xml</i></p>
<dd>Use this to give the location of the config file. If not used, the config file is searched for by first checking the current directory, and then by looking in the install location (/usr/local/lib/wv/wvHtml.xml by default)</dl>
<h2>More Information</h2>
<p><a rel="nofollow" href="http://wvware.sourceforge.net">http://wvware.sourceforge.net</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-wvabw/">wvAbw</a>(1),</code> <code><a href="/docs/linux/man/1-wvhtml/">wvHtml</a>(1),</code> <code><a href="/docs/linux/man/1-wvlatex/">wvLatex</a>(1),</code> <code><a href="/docs/linux/man/1-wvcleanlatex/">wvCleanLatex</a>(1),</code> <code><a href="/docs/linux/man/1-wvps/">wvPS</a>(1),</code> <code><a href="/docs/linux/man/1-wvdvi/">wvDVI</a>(1),</code> <code><a href="/docs/linux/man/1-wvpdf/">wvPDF</a>(1),</code> <code><a href="/docs/linux/man/1-wvrtf/">wvRTF</a>(1),</code> <code><a href="/docs/linux/man/1-wvtext/">wvText</a>(1),</code> <code><a href="/docs/linux/man/1-wvwml/">wvWml</a>(1),</code> <code><a href="/docs/linux/man/1-wvmime/">wvMime</a>(1),</code> <code><a href="/docs/linux/man/1-catdoc/">catdoc</a>(1),</code> <code><a href="/docs/linux/man/1-word2x/">word2x</a>(1)</code></p>
<h2>Author</h2>
<p>&nbsp;<wbr>Dom Lachowicz&nbsp;<wbr>(current author and maintainer)&nbsp;<wbr><br />
&nbsp;<wbr>Caolan McNamara&nbsp;<wbr>(original author)<br />
&nbsp;<wbr>WEB:&nbsp;<wbr><a rel="nofollow" href="http://wvware.sourceforge.net">http://wvware.sourceforge.net</a><br />
&nbsp;<wbr>MAIL: cinamod [at] hotmail.com</p>
