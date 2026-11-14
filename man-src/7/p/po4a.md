---
title: "po4a(7)"
name: "po4a"
section: "7"
letter: "p"
url: "/docs/linux/man/7-po4a/"
description: "po4a – framework to translate documentation and other materials"
---

<p>po4a &#8211; framework to translate documentation and other materials</p>
<h2>Introduction</h2>
<p>The po4a (<font SIZE="-1">PO</font> for anything) project goal is to ease translations (and more interestingly, the maintenance of translations) using gettext tools on areas where they were not expected like documentation.</p>
<h2>Table of content</h2>
<p>This document is organized as follow:</p>
<dl>
<dt>1 Why should I use po4a? What is it good for?</p>
<dd>This introducing chapter explains the motivation of the project and its philosophy. You should read it first if you are in the process of evaluating po4a for your own translations.</p>
<dt>2 How to use po4a?</p>
<dd>This chapter is a sort of reference manual, trying to answer the users&#8217; questions and to give you a better understanding of the whole process. This introduces how to do things with po4a and serve as an introduction to the documentation of the specific tools.</p>
<dl>
<dd>
<dl>
<dt><font SIZE="-1">HOWTO</font> begin a new translation?</p>
<dd>
<dt><font SIZE="-1">HOWTO</font> change the translation back to a documentation file?</p>
<dd>
<dt><font SIZE="-1">HOWTO</font> update a po4a translation?</p>
<dd>
<dt><font SIZE="-1">HOWTO</font> convert a pre-existing translation to po4a?</p>
<dd>
<dt><font SIZE="-1">HOWTO</font> add extra text to translations (like translator&#8217;s name)?</p>
<dd>
<dt><font SIZE="-1">HOWTO</font> do all this in one program invocation?</p>
<dd>
<dt><font SIZE="-1">HOWTO</font> customize po4a?</p>
<dd></dl>
</dl>
<dl>
<dd></dl>
<dt>3 How does it work?</p>
<dd>This chapter gives you a brief overview of the po4a internals, so that you may feel more confident to help us maintaining and improving it. It may also help you understanding why it does not do what you expected, and how to solve your problems.</p>
<dt>4 <font SIZE="-1">FAQ</font></p>
<dd>This chapter groups the Frequently Asked Questions. In fact, most of the questions for now could be formulated that way: &#8220;Why is it designed this way, and not that one?&#8221; If you think po4a isn&#8217;t the right answer to documentation translation, you should consider reading this section. If it does not answer your question, please contact us on the &lt;po4a-devel [at] lists.alioth.debian.org&gt; mailing list. We love feedback.</p>
<dt>5 Specific notes about modules</p>
<dd>This chapter presents the specificities of each module from the translator and original author&#8217;s point of view. Read this to learn the syntax you will encounter when translating stuff in this module, or the rules you should follow in your original document to make translators&#8217; life easier. </p>
<p> Actually, this section is not really part of this document. Instead, it is placed in each module&#8217;s documentation. This helps ensuring that the information is up to date by keeping the documentation and the code together.</dl>
<h2>Why should I use po4a? What it is good for?</h2>
<p>I like the idea of open-source software, making it possible for everybody to access software and its source code. But being French, I&#8217;m well aware that the licensing is not the only restriction to the openness of software: non-translated free software is useless for non-English speakers, and we still have some work to make it available to really everybody out there. </p>
<p> The perception of this situation by the open-source actors did dramatically improve recently. We, as translators, won the first battle and convinced everybody of the translations&#8217; importance. But unfortunately, it was the easy part. Now, we have to do the job and actually translate all this stuff. </p>
<p> Actually, open-source software themselves benefit of a rather decent level of translation, thanks to the wonderful gettext tool suite. It is able to extract the strings to translate from the program, present a uniform format to translators, and then use the result of their works at run time to display translated messages to the user. </p>
<p> But the situation is rather different when it comes to documentation. Too often, the translated documentation is not visible enough (not distributed as a part of the program), only partial, or not up to date. This last situation is by far the worst possible one. Outdated translation can reveal worse than no translation at all to the users by describing old program behavior which are not in use anymore.</p>
<h3>The problem to solve</h3>
<p>Translating documentation is not very difficult in itself. Texts are far longer than the messages of the program and thus take longer to be achieved, but no technical skill is really needed to do so. The difficult part comes when you have to maintain your work. Detecting which parts did change and need to be updated is very difficult, error-prone and highly unpleasant. I guess that this explains why so much translated documentation out there are outdated.</p>
<h3>The po4a answers</h3>
<p>So, the whole point of po4a is to make the documentation translation <i>maintainable</i>. The idea is to reuse the gettext methodology to this new field. Like in gettext, texts are extracted from their original locations in order to be presented in a uniform format to the translators. The classical gettext tools help them updating their works when a new release of the original comes out. But to the difference of the classical gettext model, the translations are then re-injected in the structure of the original document so that they can be processed and distributed just like the English version. </p>
<p> Thanks to this, discovering which parts of the document were changed and need an update becomes very easy. Another good point is that the tools will make almost all the work when the structure of the original document gets fundamentally reorganized and when some chapters are moved around, merged or split. By extracting the text to translate from the document structure, it also keeps you away from the text formatting complexity and reduces your chances to get a broken document (even if it does not completely prevent you to do so). </p>
<p> Please also see the <font SIZE="-1"><code>FAQ</code></font> below in this document for a more complete list of the advantages and disadvantages of this approach.</p>
<h3>Supported formats</h3>
<p>Currently, this approach has been successfully implemented to several kinds of text formatting formats: </p>
<p> <i>man</i> </p>
<p> The good old manual pages&#8217; format, used by so much programs out there. The po4a support is very welcome here since this format is somewhat difficult to use and not really friendly to the newbies. The <i><a href="//www.systutorials.com/docs/linux/man/3pm-Locale::Po4a::Man/">Locale::Po4a::Man</a></i>(3pm) module also supports the mdoc format, used by the <font SIZE="-1">BSD</font> man pages (they are also quite common on Linux). </p>
<p> <i>pod</i> </p>
<p> This is the Perl Online Documentation format. The language and extensions themselves are documented that way, as well as most of the existing Perl scripts. It makes easy to keep the documentation close to the actual code by embedding them both in the same file. It makes programmer life easier, but unfortunately, not the translator one. </p>
<p> <i>sgml</i> </p>
<p> Even if somewhat superseded by <font SIZE="-1">XML</font> nowadays, this format is still used rather often for documents which are more than a few screens long. It allows you to make complete books. Updating the translation of so long documents can reveal to be a real nightmare. <code>diff</code> reveals often useless when the original text was re-indented after update. Fortunately, po4a can help you in that process. </p>
<p> Currently, only the DebianDoc and DocBook <font SIZE="-1">DTD</font> are supported, but adding support to a new one is really easy. It is even possible to use po4a on an unknown <font SIZE="-1">SGML DTD</font> without changing the code by providing the needed information on the command line. See <i><a href="//www.systutorials.com/docs/linux/man/3pm-Locale::Po4a::Sgml/">Locale::Po4a::Sgml</a></i>(3pm) for details. </p>
<p> <i>TeX / LaTeX</i> </p>
<p> The LaTeX format is a major documentation format used in the Free Software world and for publications. The <i><a href="//www.systutorials.com/docs/linux/man/3pm-Locale::Po4a::LaTeX/">Locale::Po4a::LaTeX</a></i>(3pm) module was tested with the Python documentation, a book and some presentations. </p>
<p> <i>texinfo</i> </p>
<p> All the <font SIZE="-1">GNU</font> documentation is written in this format (that&#8217;s even one of the requirement to become an official <font SIZE="-1">GNU</font> project). The support for <i><a href="//www.systutorials.com/docs/linux/man/3pm-Locale::Po4a::Texinfo/">Locale::Po4a::Texinfo</a></i>(3pm) in po4a is still at the beginning. Please report bugs and feature requests. </p>
<p> <i>xml</i> </p>
<p> The <font SIZE="-1">XML</font> format is a base format for many documentation formats. </p>
<p> Currently, the DocBook <font SIZE="-1">DTD</font> is supported by po4a. See <i><a href="//www.systutorials.com/docs/linux/man/3pm-Locale::Po4a::Docbook/">Locale::Po4a::Docbook</a></i>(3pm) for details. </p>
<p> <i>others</i> </p>
<p> Po4a can also handle some more rare or specialized formats, such as the documentation of compilation options for the 2.4.x kernels or the diagrams produced by the dia tool. Adding a new one is often very easy and the main task is to come up with a parser of your target format. See <i><a href="//www.systutorials.com/docs/linux/man/3pm-Locale::Po4a::TransTractor/">Locale::Po4a::TransTractor</a></i>(3pm) for more information about this.</p>
<h3>Unsupported formats</h3>
<p>Unfortunately, po4a still lacks support for several documentation formats. </p>
<p> There is a whole bunch of other formats we would like to support in po4a, and not only documentation ones. Indeed, we aim at plugging all &#8220;market holes&#8221; left by the classical gettext tools. It encompass package descriptions (deb and rpm), package installation scripts questions, package changelogs, and all specialized file formats used by the programs such as game scenarios or wine resource files.</p>
<h2>How to use po4a?</h2>
<p>This chapter is a sort of reference manual, trying to answer the users&#8217; questions and to give you a better understanding of the whole process. This introduces how to do things with po4a and serve as an introduction to the documentation of the specific tools.</p>
<h3>Graphical overview</h3>
<p>The following schema gives an overview of the process of translating documentation using po4a. Do not be afraid by its apparent complexity, it comes from the fact that the <i>whole</i> process is represented here. Once you converted your project to po4a, only the right part of the graphic is relevant. </p>
<p> Note that <i>master.doc</i> is taken as an example for the documentation to be translated and <i>translation.doc</i> is the corresponding translated text. The suffix could be <i>.pod</i>, <i>.xml</i>, or <i>.sgml</i> depending on its format. Each part of the picture will be detailed in the next sections. </p>
<pre> master.doc
 |
 V
 +&lt;-----&lt;----+&lt;-----&lt;-----&lt;--------+-------&gt;--------&gt;-------+
 : | | :
{translation} | { update of master.doc } :
 : | | :
 XX.doc | V V
(optional) | master.doc -&gt;--------&gt;------&gt;+
 : | (new) |
 V V | |
 [po4a-gettextize] doc.XX.po---&gt;+ | |
 | (old) | | |
 | ^ V V |
 | | [po4a-updatepo] |
 V | | V
 translation.pot ^ V |
 | | doc.XX.po |
 | | (fuzzy) |
 { translation } | | |
 | ^ V V
 | | {manual editing} |
 | | | |
 V | V V
 doc.XX.po ---&gt;----&gt;+&lt;---&lt;---- doc.XX.po addendum master.doc
 (initial) (up-to-date) (optional) (up-to-date) 
 : | | |
 : V | |
 +-----&gt;-----&gt;-----&gt;------&gt; + | |
 | | |
 V V V
 +------&gt;-----+------&lt;------+
 |
 V
 [po4a-translate]
 |
 V
 XX.doc
 (up-to-date)</pre>
<p>On the left part, the conversion of a translation not using po4a to this system is shown. On the top of the right part, the action of the original author is depicted (updating the documentation). The middle of the right part is where the automatic actions of po4a are depicted. The new material are extracted, and compared against the exiting translation. Parts which didn&#8217;t change are found, and previous translation is used. Parts which where partially modified are also connected to the previous translation, but with a specific marker indicating that the translation must be updated. The bottom of the figure shows how a formatted document is built. </p>
<p> Actually, as a translator, the only manual operation you have to do is the part marked {manual editing}. Yeah, I&#8217;m sorry, but po4a helps you translate. It does not translate anything for you&#8230;</p>
<h3><font SIZE="-1">HOWTO</font> begin a new translation?</h3>
<p>This section presents the needed steps required to begin a new translation with po4a. The refinements involved in converting an existing project to this system are detailed in the relevant section. </p>
<p> To begin a new translation using po4a, you have to do the following steps:</p>
<dl>
<dt>&#8211;</p>
<dd>Extract the text which have to be translated from the original &lt;<i>master.doc</i>&gt; document into a new translation template &lt;<i>translation.pot</i>&gt; file (the gettext format). For that, use the <code>po4a-gettextize</code> program this way: </p>
<pre> $ po4a-gettextize -f &lt;format&gt; -m &lt;master.doc&gt; -p &lt;translation.pot&gt;</pre>
<p>&lt;<i>format</i>&gt; is naturally the format used in the <i>master.doc</i> document. As expected, the output goes into <i>translation.pot</i>. Please refer to <i><a href="/docs/linux/man/1-po4a-gettextize/">po4a-gettextize</a></i>(1) for more details about the existing options.</p>
<dt>&#8211;</p>
<dd>Actually translate what should be translated. For that, you have to rename the <font SIZE="-1">POT</font> file for example to <i>doc.XX.po</i> (where <i></i><font SIZE="-1"><i>XX</i></font><i></i> is the <font SIZE="-1">ISO639</font> code of the language you are translating to, e.g. <code>fr</code> for French), and edit the resulting file. It is often a good idea to not name the file <i></i><font SIZE="-1"><i>XX</i></font><i>.po</i> to avoid confusion with the translation of the program messages, but this your call. Don&#8217;t forget to update the <font SIZE="-1">PO</font> file headers, they are important. </p>
<p> The actual translation can be done using the Emacs&#8217; or Vi&#8217;s <font SIZE="-1">PO</font> mode, Lokalize (<font SIZE="-1">KDE</font> based), Gtranslator (<font SIZE="-1">GNOME</font> based) or whichever program you prefer to use for them (e.g. Virtaal). </p>
<p> If you wish to learn more about this, you definitively need to refer to the gettext documentation, available in the <code>gettext-doc</code> package.</dl>
<h3><font SIZE="-1">HOWTO</font> change the translation back to a documentation file?</h3>
<p>Once you&#8217;re done with the translation, you want to get the translated documentation and distribute it to users along with the original one. For that, use the <i><a href="/docs/linux/man/1-po4a-translate/">po4a-translate</a></i>(1) program like that (where <i></i><font SIZE="-1"><i>XX</i></font><i></i> is the language code): </p>
<pre> $ po4a-translate -f &lt;format&gt; -m &lt;master.doc&gt; -p &lt;doc.XX.po&gt; -l &lt;XX.doc&gt;</pre>
<p>As before, &lt;<i>format</i>&gt; is the format used in the <i>master.doc</i> document. But this time, the <font SIZE="-1">PO</font> file provided with the <code>-p</code> flag is part of the input. This is your translation. The output goes into <i></i><font SIZE="-1"><i>XX</i></font><i>.doc</i>. </p>
<p> Please refer to <i><a href="/docs/linux/man/1-po4a-translate/">po4a-translate</a></i>(1) for more details.</p>
<h3><font SIZE="-1">HOWTO</font> update a po4a translation?</h3>
<p>To update your translation when the original <i>master.doc</i> file has changed, use the <i><a href="/docs/linux/man/1-po4a-updatepo/">po4a-updatepo</a></i>(1) program like that: </p>
<pre> $ po4a-updatepo -f &lt;format&gt; -m &lt;new_master.doc&gt; -p &lt;old_doc.XX.po&gt;</pre>
<p>(Please refer to <i><a href="/docs/linux/man/1-po4a-updatepo/">po4a-updatepo</a></i>(1) for more details) </p>
<p> Naturally, the new paragraph in the document won&#8217;t get magically translated in the <font SIZE="-1">PO</font> file with this operation, and you&#8217;ll need to update the <font SIZE="-1">PO</font> file manually. Likewise, you may have to rework the translation for paragraphs which were modified a bit. To make sure you won&#8217;t miss any of them, they are marked as &#8220;fuzzy&#8221; during the process and you have to remove this marker before the translation can be used by <code>po4a-translate</code>. As for the initial translation, the best is to use your favorite <font SIZE="-1">PO</font> editor here. </p>
<p> Once your <font SIZE="-1">PO</font> file is up-to-date again, without any untranslated or fuzzy string left, you can generate a translated documentation file, as explained in the previous section.</p>
<h3><font SIZE="-1">HOWTO</font> convert a pre-existing translation to po4a?</h3>
<p>Often, you used to translate manually the document happily until a major reorganization of the original <i>master.doc</i> document happened. Then, after some unpleasant tries with <code>diff</code> or similar tools, you want to convert to po4a. But of course, you don&#8217;t want to loose your existing translation in the process. Don&#8217;t worry, this case is also handled by po4a tools and is called gettextization. </p>
<p> The key here is to have the same structure in the translated document and in the original one so that the tools can match the content accordingly. </p>
<p> If you are lucky (i.e., if the structures of both documents perfectly match), it will work seamlessly and you will be set in a few seconds. Otherwise, you may understand why this process has such an ugly name, and you&#8217;d better be prepared to some grunt work here. In any case, remember that it is the price to pay to get the comfort of po4a afterward. And the good point is that you have to do so only once. </p>
<p> I cannot emphasis this too much. In order to ease the process, it is thus important that you find the exact version which were used to do the translation. The best situation is when you noted down the <font SIZE="-1">VCS</font> revision used for the translation and you didn&#8217;t modify it in the translation process, so that you can use it. </p>
<p> It won&#8217;t work well when you use the updated original text with the old translation. It remains possible, but is harder and really should be avoided if possible. In fact, I guess that if you fail to find the original text again, the best solution is to find someone to do the gettextization for you (but, please, not me ;). </p>
<p> Maybe I&#8217;m too dramatic here. Even when things go wrong, it remains ways faster than translating everything again. I was able to gettextize the existing French translation of the Perl documentation in one day, even though things <code>did</code> went wrong. That was more than two megabytes of text, and a new translation would have lasted months or more. </p>
<p> Let me explain the basis of the procedure first and I will come back on hints to achieve it when the process goes wrong. To ease comprehension, let&#8217;s use above example once again. </p>
<p> Once you have the old <i>master.doc</i> again which matches with the translation <i></i><font SIZE="-1"><i>XX</i></font><i>.doc</i>, the gettextization can be done directly to the <font SIZE="-1">PO</font> file <i>doc.XX.po</i> without manual translation of <i>translation.pot</i> file: </p>
<pre> $ po4a-gettextize -f &lt;format&gt; -m &lt;old_master.doc&gt; -l &lt;XX.doc&gt; -p &lt;doc.XX.po&gt;</pre>
<p>When you&#8217;re lucky, that&#8217;s it. You converted your old translation to po4a and can begin with the updating task right away. Just follow the procedure explained a few section ago to synchronize your <font SIZE="-1">PO</font> file with the newest original document, and update the translation accordingly. </p>
<p> Please note that even when things seem to work properly, there is still room for errors in this process. The point is that po4a is unable to understand the text to make sure that the translation match the original. That&#8217;s why all strings are marked as &#8220;fuzzy&#8221; in the process. You should check each of them carefully before removing those markers. </p>
<p> Often the document structures don&#8217;t match exactly, preventing <code>po4a-gettextize</code> from doing its job properly. At that point, the whole game is about editing the files to get their damn structures matching. </p>
<p> It may help to read the section <code>Gettextization: how does it work?</code> below. Understanding the internal process will help you to make this work. The good point is that <code>po4a-gettextize</code> is rather verbose about what went wrong when it happens. First, it pinpoints where in the documents the structures&#8217; discrepancies are. You will learn the strings that don&#8217;t match, their positions in the text, and the type of each of them. Moreover, the <font SIZE="-1">PO</font> file generated so far will be dumped to <i>gettextization.failed.po</i>.</p>
<dl>
<dt>&#8211;</p>
<dd>Remove all extra parts of the translations, such as the section in which you give the translator name and thank every people who contributed to the translation. Addenda, which are described in the next section, will allow you to re-add them afterward.</p>
<dt>&#8211;</p>
<dd>Do not hesitate to edit both the original and the translation. The most important thing is to get the <font SIZE="-1">PO</font> file. You will be able to update it afterward. That being said, editing the translation should be preferred when both are possible since it makes things easier when the gettextization is done.</p>
<dt>&#8211;</p>
<dd>If needed, kill some parts of the original if they happen to not be translated. When synchronizing the <font SIZE="-1">PO</font> with the document afterward, they will come back from themselves.</p>
<dt>&#8211;</p>
<dd>If you changed the structure a bit (to merge two paragraphs, or split another one), undo those changes. If there are issues in the original, you should inform the original author. Fixing them in your translation only fixes them for a part of the community. And moreover, it&#8217;s impossible when using po4a ;)</p>
<dt>&#8211;</p>
<dd>Sometimes, the paragraph content does match, but their types don&#8217;t. Fixing it is rather format-dependant. In <font SIZE="-1">POD</font> and man, it often comes from the fact that one of the two contains a line beginning with a white space where the other doesn&#8217;t. In those formats, such paragraph cannot be wrapped and thus become a different type. Just remove the space and you are fine. It may also be a typo in the tag name. </p>
<p> Likewise, two paragraphs may get merged together in <font SIZE="-1">POD</font> when the separating line contains some spaces, or when there is no empty line before the =item line and the content of the item.</p>
<dt>&#8211;</p>
<dd>Sometimes, there is a desynchronization between the files, and the translation is attached to the wrong original paragraph. It is the sign that the real problem was before in the files. Check <i>gettextization.failed.po</i> to see when the desynchronization begins, and fix it there.</p>
<dt>&#8211;</p>
<dd>Sometimes, you get the strong feeling that po4a ate some parts of the text, either the original or the translation. <i>gettextization.failed.po</i> indicates that both of them where gently matching, and then the gettextization fails because it tried to match one paragraph with the one after (or before) the right one, as if the right one disappeared. Curse po4a as I did when it first happened to me. Generously. </p>
<p> This unfortunate situation happens when the same paragraph is repeated over the document. In that case, no new entry is created in the <font SIZE="-1">PO</font> file, but a new reference is added to the existing one instead. </p>
<p> So, when the same paragraph appears twice in the original but both are not translated in the exact same way each time, you will get the feeling that a paragraph of the original disappeared. Just kill the new translation. If you prefer to kill the first translation instead when it was actually better, remove the second one from where it is and put it in place of the first one. </p>
<p> In the contrary, if two similar but different paragraphs were translated in the exact same way, you will get the feeling that a paragraph of the translation disappeared. A solution is to add a stupid string to the original paragraph (such as &#8220;I&#8217;m different&#8221;). Don&#8217;t be afraid, those things will disappear during the synchronization, and when the added text is short enough, gettext will match your translation to the existing text (marking it as fuzzy, but you don&#8217;t really care since all strings are fuzzy after gettextization).</dl>
<p> Hopefully, those tips will help you making your gettextization work and obtain your precious <font SIZE="-1">PO</font> file. You are now ready to synchronize your file and begin your translation. Please note that on large text, it may happen that the first synchronization takes a long time. </p>
<p> For example, the first <code>po4a-updatepo</code> of the Perl documentation&#8217;s French translation (5.5 Mb <font SIZE="-1">PO</font> file) took about two days full on a 1Ghz G5 computer. Yes, 48 hours. But the subsequent ones only take a dozen of seconds on my old laptop. This is because the first time, most of the msgid of the <font SIZE="-1">PO</font> file don&#8217;t match any of the <font SIZE="-1">POT</font> file ones. This forces gettext to search for the closest one using a costly string proximity algorithm.</p>
<h3><font SIZE="-1">HOWTO</font> add extra text to translations (like translator&#8217;s name)?</h3>
<p>Because of the gettext approach, doing this becomes more difficult in po4a than it was when simply editing a new file along the original one. But it remains possible, thanks to the so-called <code>addenda</code>. </p>
<p> It may help the comprehension to consider addenda as a sort of patches applied to the localized document after processing. They are rather different from the usual patches (they have only one line of context, which can embed Perl regular expression, and they can only add new text without removing any), but the functionalities are the same. </p>
<p> Their goal is to allow the translator to add extra content to the document which is not translated from the original document. The most common usage is to add a section about the translation itself, listing contributors and explaining how to report bug against the translation. </p>
<p> An addendum must be provided as a separate file. The first line constitutes a header indicating where in the produced document they should be placed. The rest of the addendum file will be added verbatim at the determined position of the resulting document. </p>
<p> The header has a pretty rigid syntax: It must begin with the string <font SIZE="-1"><code>PO4A-HEADER:</code></font>, followed by a semi-colon (<code>;</code>) separated list of <i>key</i><code>=</code><i>value</i> fields. White spaces <font SIZE="-1">ARE</font> important. Note that you cannot use the semi-colon char (<code>;</code>) in the value, and that quoting it doesn&#8217;t help. </p>
<p> Again, it sounds scary, but the examples given below should help you to find how to write the header line you need. To illustrate the discussion, assume we want to add a section called &#8220;About this translation&#8221; after the &#8220;About this document&#8221; one. </p>
<p> Here are the possible header keys:</p>
<dl>
<dt><code>position</code> (mandatory)</p>
<dd>a regexp. The addendum will be placed near the line matching this regexp. Note that we&#8217;re speaking about the translated document here, not the original. If more than a line match this expression (or none), the addition will fail. It is indeed better to report an error than inserting the addendum at the wrong location. </p>
<p> This line is called <i>position point</i> in the following. The point where the addendum is added is called <i>insertion point</i>. Those two points are near one from another, but not equal. For example, if you want to insert a new section, it is easier to put the <i>position point</i> on the title of the preceding section and explain po4a where the section ends (remember that <i>position point</i> is given by a regexp which should match a unique line). </p>
<p> The localization of the <i>insertion point</i> with regard to the <i>position point</i> is controlled by the <code>mode</code>, <code>beginboundary</code> and <code>endboundary</code> fields, as explained below. </p>
<p> In our case, we would have: </p>
<pre> position=&lt;title&gt;About this document&lt;/title&gt;</pre>
<dt><code>mode</code> (mandatory)</p>
<dd>It can be either the string <code>before</code> or <code>after</code>, specifying the position of the addendum, relative to the <i>position point</i>. </p>
<p> Since we want the new section to be placed below the one we are matching, we have: </p>
<pre> mode=after</pre>
<dt><code>beginboundary</code> (used only when <code>mode=after</code>, and mandatory in that case)</p>
<dd>
<dt><code>endboundary</code> (idem)</p>
<dd>regexp matching the end of the section after which the addendum goes. </p>
<p> When <code>mode=after</code>, the <i>insertion point</i> is after the <i>position point</i>, but not directly after! It is placed at the end of the section beginning at the <i>position point</i>, i.e., after or before the line matched by the <i>???</i><code>boundary</code> argument, depending on whether you used <code>beginboundary</code> or <code>endboundary</code>. </p>
<p> In our case, we can choose to indicate the end of the section we match by adding: </p>
<pre> endboundary=&lt;/section&gt;</pre>
<p>or to indicate the beginning of the next section by indicating: </p>
<pre> beginboundary=&lt;section&gt;</pre>
<p>In both case, our addendum will be placed after the <code>&lt;/section&gt;</code> and before the <code>&lt;section&gt;</code>. The first one is better since it will work even if the document gets reorganized. </p>
<p> Both forms exist because documentation formats are different. In some of them, there is a way to mark the end of a section (just like the <code>&lt;/section&gt;</code> we just used), while some other don&#8217;t explicitly mark the end of section (like in man). In the former case, you want to make a <i>boundary</i> matching the <i>end of a section</i>, so that the <i>insertion point</i> comes after it. In the latter case, you want to make a <i>boundary</i> matching the <i>beginning of the next section</i>, so that the <i>insertion point</i> comes just before it.</dl>
<p> This can seem obscure, but hopefully, the next examples will enlighten you.</p>
<dl>
<dt> To sum up the example we used so far, in order to add a section called &quot;About this translation&quot; after the &quot;About this document&quot; one in a <font SIZE="-1">SGML</font> document, you can use either of those header lines:</p>
<dd>
<pre> PO4A-HEADER: mode=after; position=About this document; endboundary=&lt;/section&gt;
 PO4A-HEADER: mode=after; position=About this document; beginboundary=&lt;section&gt;</pre>
<dt> If you want to add something after the following nroff section:</p>
<dd>
<pre> .SH &quot;AUTHORS&quot;</pre>
<p>you should put a <code>position</code> matching this line, and a <code>beginboundary</code> matching the beginning of the next section (i.e., <code>^\.SH</code>). The addendum will then be added <code>after</code> the <i>position point</i> and immediately <code>before</code> the first line matching the <code>beginboundary</code>. That is to say: </p>
<pre> PO4A-HEADER:mode=after;position=AUTHORS;beginboundary=\.SH</pre>
<dt> If you want to add something into a section (like after &quot;Copyright Big Dude&quot;) instead of adding a whole section, give a <code>position</code> matching this line, and give a <code>beginboundary</code> matching any line.</p>
<dd>
<pre> PO4A-HEADER:mode=after;position=Copyright Big Dude, 2004;beginboundary=^</pre>
<dt>If you want to add something at the end of the document, give a <code>position</code> matching any line of your document (but only one line. Po4a won&#8217;t proceed if it&#8217;s not unique), and give an <code>endboundary</code> matching nothing. Don&#8217;t use simple strings here like <code>&quot;</code><font SIZE="-1"><code>EOF&quot;</code></font>, but prefer those which have less chance to be in your document.</p>
<dd>
<pre> PO4A-HEADER:mode=after;position=&lt;title&gt;About&lt;/title&gt;;beginboundary=FakePo4aBoundary</pre>
</dl>
<p> In any case, remember that these are regexp. For example, if you want to match the end of a nroff section ending with the line </p>
<pre> .fi</pre>
<p>don&#8217;t use <code>.fi</code> as <code>endboundary</code>, because it will match with &#8220;the[ fi]le&#8221;, which is obviously not what you expect. The correct <code>endboundary</code> in that case is: <code>^\.fi$</code>. </p>
<p> If the addendum doesn&#8217;t go where you expected, try to pass the <code>-vv</code> argument to the tools, so that they explain you what they do while placing the addendum. </p>
<p> <i>More detailed example</i> </p>
<p> Original document (<font SIZE="-1">POD</font> formatted): </p>
<pre> |=head1 NAME
 |
 |dummy - a dummy program
 |
 |=head1 AUTHOR
 |
 |me</pre>
<p>Then, the following addendum will ensure that a section (in French) about the translator is added at the end of the file. (in French, &#8220;<font SIZE="-1">TRADUCTEUR&#8221;</font> means &#8220;<font SIZE="-1">TRANSLATOR&#8221;,</font> and &#8220;moi&#8221; means &#8220;me&#8221;) </p>
<pre> |PO4A-HEADER:mode=after;position=AUTEUR;beginboundary=^=head
 |
 |=head1 TRADUCTEUR
 |
 |moi</pre>
<p>In order to put your addendum before the <font SIZE="-1">AUTHOR,</font> use the following header: </p>
<pre> PO4A-HEADER:mode=after;position=NOM;beginboundary=^=head1</pre>
<p>This works because the next line matching the <code>beginboundary</code> /^=head1/ after the section &#8220;<font SIZE="-1">NAME&#8221; </font>(translated to &#8220;<font SIZE="-1">NOM&#8221;</font> in French), is the one declaring the authors. So, the addendum will be put between both sections.</p>
<h3><font SIZE="-1">HOWTO</font> do all this in one program invocation?</h3>
<p>The use of po4a proved to be a bit error prone for the users since you have to call two different programs in the right order (<code>po4a-updatepo</code> and then <code>po4a-translate</code>), each of them needing more than 3 arguments. Moreover, it was difficult with this system to use only one <font SIZE="-1">PO</font> file for all your documents when more than one format was used. </p>
<p> The <i><a href="/docs/linux/man/1-po4a/">po4a</a></i>(1) program was designed to solve those difficulties. Once your project is converted to the system, you write a simple configuration file explaining where your translation files are (<font SIZE="-1">PO</font> and <font SIZE="-1">POT</font>), where the original documents are, their formats and where their translations should be placed. </p>
<p> Then, calling <i><a href="/docs/linux/man/1-po4a/">po4a</a></i>(1) on this file ensures that the <font SIZE="-1">PO</font> files are synchronized against the original document, and that the translated document are generated properly. Of course, you will want to call this program twice: once before editing the <font SIZE="-1">PO</font> file to update them and once afterward to get a completely updated translated document. But you only need to remember one command line.</p>
<h3><font SIZE="-1">HOWTO</font> customize po4a?</h3>
<p>po4a modules have options (specified with the <code>-o</code> option) that can be used to change the module behavior. </p>
<p> It is also possible to customize a module or new / derivative / modified modules by putting a module in <i>lib/Locale/Po4a/</i>, and adding <i>lib</i> to the paths specified by the <font SIZE="-1">PERLLIB</font> or <font SIZE="-1">PERL5LIB</font> environment. For example: </p>
<pre> PERLLIB=$PWD/lib po4a --previous po4a/po4a.cfg</pre>
<p>Note: the actual name of the lib directory is not important.</p>
<h2>How does it work?</h2>
<p>This chapter gives you a brief overview of the po4a internals, so that you may feel more confident to help us maintaining and improving it. It may also help you understanding why it does not do what you expected, and how to solve your problems.</p>
<h3>What&#8217;s the big picture here?</h3>
<p>The po4a architecture is object oriented (in Perl. Isn&#8217;t that neat?). The common ancestor to all parser classes is called TransTractor. This strange name comes from the fact that it is at the same time in charge of translating document and extracting strings. </p>
<p> More formally, it takes a document to translate plus a <font SIZE="-1">PO</font> file containing the translations to use as input while producing two separate outputs: Another <font SIZE="-1">PO</font> file (resulting of the extraction of translatable strings from the input document), and a translated document (with the same structure than the input one, but with all translatable strings replaced with content of the input <font SIZE="-1">PO</font>). Here is a graphical representation of this: </p>
<pre> Input document --\ /---&gt; Output document
 \ TransTractor:: / (translated)
 +--&gt;-- parse() --------+
 / \
 Input PO --------/ \---&gt; Output PO
 (extracted)</pre>
<p>This little bone is the core of all the po4a architecture. If you omit the input <font SIZE="-1">PO</font> and the output document, you get <code>po4a-gettextize</code>. If you provide both input and disregard the output <font SIZE="-1">PO,</font> you get <code>po4a-translate</code>. </p>
<p> <i>TransTractor::parse()</i> is a virtual function implemented by each module. Here is a little example to show you how it works. It parses a list of paragraphs, each of them beginning with <code>&lt;p&gt;</code>. </p>
<pre> 1 sub parse {
 2 PARAGRAPH: while (1) {
 3 $my ($paragraph,$pararef,$line,$lref)=(&quot;&quot;,&quot;&quot;,&quot;&quot;,&quot;&quot;);
 4 $my $first=1;
 5 while (($line,$lref)=$document-&gt;shiftline() &amp;&amp; defined($line)) {
 6 if ($line =~ m/&lt;p&gt;/ &amp;&amp; !$first--; ) {
 7 $document-&gt;unshiftline($line,$lref);
 8
 9 $paragraph =~ s/^&lt;p&gt;//s;
 10 $document-&gt;pushline(&quot;&lt;p&gt;&quot;.$document-&gt;translate($paragraph,$pararef));
 11
 12 next PARAGRAPH;
 13 } else {
 14 $paragraph .= $line;
 15 $pararef = $lref unless(length($pararef));
 16 }
 17 }
 18 return; # Did not got a defined line? End of input file.
 19 }
 20 }</pre>
<p>On line 6, we encounter <code>&lt;p&gt;</code> for the second time. That&#8217;s the signal of the next paragraph. We should thus put the just obtained line back into the original document (line 7) and push the paragraph built so far into the outputs. After removing the leading <code>&lt;p&gt;</code> of it on line 9, we push the concatenation of this tag with the translation of the rest of the paragraph. </p>
<p> This <i>translate()</i> function is very cool. It pushes its argument into the output <font SIZE="-1">PO</font> file (extraction) and returns its translation as found in the input <font SIZE="-1">PO</font> file (translation). Since it&#8217;s used as part of the argument of <i>pushline()</i>, this translation lands into the output document. </p>
<p> Isn&#8217;t that cool? It is possible to build a complete po4a module in less than 20 lines when the format is simple enough&#8230; </p>
<p> You can learn more about this in <i><a href="//www.systutorials.com/docs/linux/man/3pm-Locale::Po4a::TransTractor/">Locale::Po4a::TransTractor</a></i>(3pm).</p>
<h3>Gettextization: how does it work?</h3>
<p>The idea here is to take the original document and its translation, and to say that the Nth extracted string from the translation is the translation of the Nth extracted string from the original. In order to work, both files must share exactly the same structure. For example, if the files have the following structure, it is very unlikely that the 4th string in translation (of type &#8216;chapter&#8217;) is the translation of the 4th string in original (of type &#8216;paragraph&#8217;). </p>
<pre> Original Translation
 chapter chapter
 paragraph paragraph
 paragraph paragraph
 paragraph chapter
 chapter paragraph
 paragraph paragraph</pre>
<p>For that, po4a parsers are used on both the original and the translation files to extract <font SIZE="-1">PO</font> files, and then a third <font SIZE="-1">PO</font> file is built from them taking strings from the second as translation of strings from the first. In order to check that the strings we put together are actually the translations of each other, document parsers in po4a should put information about the syntactical type of extracted strings in the document (all existing ones do so, yours should also). Then, this information is used to make sure that both documents have the same syntax. In the previous example, it would allow us to detect that string 4 is a paragraph in one case, and a chapter title in another case and to report the problem. </p>
<p> In theory, it would be possible to detect the problem, and resynchronize the files afterward (just like <code>diff</code> does). But what we should do of the few strings before desynchronizations is not clear, and it would produce bad results some times. That&#8217;s why the current implementation don&#8217;t try to resynchronize anything and verbosely fail when something goes wrong, requiring manual modification of files to fix the problem. </p>
<p> Even with these precautions, things can go wrong very easily here. That&#8217;s why all translations guessed this way are marked fuzzy to make sure that the translator reviews and checks them.</p>
<h3>Addendum: How does it work?</h3>
<p>Well, that&#8217;s pretty easy here. The translated document is not written directly to disk, but kept in memory until all the addenda are applied. The algorithms involved here are rather straightforward. We look for a line matching the position regexp, and insert the addendum before it if we&#8217;re in <code>mode=before</code>. If not, we search for the next line matching the boundary and insert the addendum after this line if it&#8217;s an <code>endboundary</code> or before this line if it&#8217;s a <code>beginboundary</code>.</p>
<h2>Faq</h2>
<p>This chapter groups the Frequently Asked Questions. In fact, most of the questions for now could be formulated that way: &#8220;Why is it designed this way, and not that one?&#8221; If you think po4a isn&#8217;t the right answer to documentation translation, you should consider reading this section. If it does not answer your question, please contact us on the &lt;po4a-devel [at] lists.alioth.debian.org&gt; mailing list. We love feedback.</p>
<h3>Why to translate each paragraph separately?</h3>
<p>Yes, in po4a, each paragraph is translated separately (in fact, each module decides this, but all existing modules do so, and yours should also). There are two main advantages to this approach:</p>
<dl>
<dt>&bull;</p>
<dd>When the technical parts of the document are hidden from the scene, the translator can&#8217;t mess with them. The fewer markers we present to the translator the less error he can do.</p>
<dt>&bull;</p>
<dd>Cutting the document helps in isolating the changes to the original document. When the original is modified, finding what parts of the translation need to be updated is eased by this process.</dl>
<p> Even with these advantages, some people don&#8217;t like the idea of translating each paragraph separately. Here are some of the answers I can give to their fear:</p>
<dl>
<dt>&bull;</p>
<dd>This approach proved successfully in the <font SIZE="-1">KDE</font> project and allows people there to produce the biggest corpus of translated and up to date documentation I know.</p>
<dt>&bull;</p>
<dd>The translators can still use the context to translate, since the strings in the <font SIZE="-1">PO</font> file are in the same order than in the original document. Translating sequentially is thus rather comparable whether you use po4a or not. And in any case, the best way to get the context remains to convert the document to a printable format since the text formatting ones are not really readable, <font SIZE="-1">IMHO. </font></p>
<dt>&bull;</p>
<dd>This approach is the one used by professional translators. I agree, that they have somewhat different goals than open-source translators. The maintenance is for example often less critical to them since the content changes rarely.</dl>
<h3>Why not to split on sentence level (or smaller)?</h3>
<p>Professional translator tools sometimes split the document at the sentence level in order to maximize the reusability of previous translations and speed up their process. The problem is that the same sentence may have several translations, depending on the context. </p>
<p> Paragraphs are by definition longer than sentences. It will hopefully ensure that having the same paragraph in two documents will have the same meaning (and translation), regardless of the context in each case. </p>
<p> Splitting on smaller parts than the sentence would be <code>very bad</code>. It would be a bit long to explain why here, but interested reader can refer to the <i><a href="//www.systutorials.com/docs/linux/man/3pm-Locale::Maketext::TPJ13/">Locale::Maketext::TPJ13</a></i>(3pm) man page (which comes with the Perl documentation), for example. To make short, each language has its specific syntactic rules, and there is no way to build sentences by aggregating parts of sentences working for all existing languages (or even for the 5 of the 10 most spoken ones, or even less).</p>
<h3>Why not put the original as comment along with translation (or other way around)?</h3>
<p>At the first glance, gettext doesn&#8217;t seem to be adapted to all kind of translations. For example, it didn&#8217;t seemed adapted to debconf, the interface all Debian packages use for their interaction with the user during installation. In that case, the texts to translate were pretty short (a dozen lines for each package), and it was difficult to put the translation in a specialized file since it has to be available before the package installation. </p>
<p> That&#8217;s why the debconf developer decided to implement another solution, where translations are placed in the same file than the original. This is rather appealing. One would even want to do this for <font SIZE="-1">XML,</font> for example. It would look like that: </p>
<pre> &lt;section&gt;
 &lt;title lang=&quot;en&quot;&gt;My title&lt;/title&gt;
 &lt;title lang=&quot;fr&quot;&gt;Mon titre&lt;/title&gt;
 &lt;para&gt;
 &lt;text lang=&quot;en&quot;&gt;My text.&lt;/text&gt;
 &lt;text lang=&quot;fr&quot;&gt;Mon texte.&lt;/text&gt;
 &lt;/para&gt;
 &lt;/section&gt;</pre>
<p>But it was so problematic that a PO-based approach is now used. Only the original can be edited in the file, and the translations must take place in <font SIZE="-1">PO</font> files extracted from the master template (and placed back at package compilation time). The old system was deprecated because of several issues:</p>
<dl>
<dt>&bull;</p>
<dd>maintenance problems </p>
<p> If several translators provide a patch at the same time, it gets hard to merge them together. </p>
<p> How will you detect changes to the original, which need to be applied to the translations? In order to use diff, you have to note which version of the original you translated. I.e., you need a <font SIZE="-1">PO</font> file in your file ;)</p>
<dt>&bull;</p>
<dd>encoding problems </p>
<p> This solution is viable when only European languages are involved, but the introduction of Korean, Russian and/or Arab really complicate the picture. <font SIZE="-1">UTF</font> could be a solution, but there are still some problems with it. </p>
<p> Moreover, such problems are hard to detect (i.e., only Korean readers will detect that the encoding of Korean is broken [because of the Russian translator])</dl>
<p> gettext solves all those problems together.</p>
<h3>But gettext wasn&#8217;t designed for that use!</h3>
<p>That&#8217;s true, but until now nobody came with a better solution. The only known alternative is manual translation, with all the maintenance issues.</p>
<h3>What about the other translation tools for documentation using gettext?</h3>
<p>As far as I know, there are only two of them:</p>
<dl>
<dt><code>poxml</code></p>
<dd>This is the tool developed by <font SIZE="-1">KDE</font> people to handle DocBook <font SIZE="-1">XML. AFAIK,</font> it was the first program to extract strings to translate from documentation to <font SIZE="-1">PO</font> files, and inject them back after translation. </p>
<p> It can only handle <font SIZE="-1">XML,</font> and only a particular <font SIZE="-1">DTD. I</font>&#8216;m quite unhappy with the handling of lists, which end in one big msgid. When the list become big, the chunk becomes harder to shallow.</p>
<dt><code>po-debiandoc</code></p>
<dd>This program done by Denis Barbier is a sort of precursor of the po4a <font SIZE="-1">SGML</font> module, which more or less deprecates it. As the name says, it handles only the DebianDoc <font SIZE="-1">DTD,</font> which is more or less a deprecated <font SIZE="-1">DTD.</font></dl>
<p> The main advantages of po4a over them are the ease of extra content addition (which is even worse there) and the ability to achieve gettextization.</p>
<h3>Educating developers about translation</h3>
<p>When you try to translate documentation or programs, you face three kinds of problems; linguistics (not everybody speaks two languages), technical (that&#8217;s why po4a exists) and relational/human. Not all developers understand the necessity of translating stuff. Even when good willed, they may ignore how to ease the work of translators. To help with that, po4a comes with lot of documentation which can be referred to. </p>
<p> Another important point is that each translated file begins with a short comment indicating what the file is, how to use it. This should help the poor developers flooded with tons of files in different languages they hardly speak, and help them dealing correctly with it. </p>
<p> In the po4a project, translated documents are not source files anymore. Since <font SIZE="-1">SGML</font> files are habitually source files, it&#8217;s an easy mistake. That&#8217;s why all files present this header: </p>
<pre> | *****************************************************
 | * GENERATED FILE, DO NOT EDIT * 
 | * THIS IS NO SOURCE FILE, BUT RESULT OF COMPILATION *
 | *****************************************************
 |
 | This file was generated by <a href="//www.systutorials.com/docs/linux/man/1-po4a-translate/">po4a-translate</a>(1). Do not store it (in VCS,
 | for example), but store the PO file used as source file by po4a-translate. 
 |
 | In fact, consider this as a binary, and the PO file as a regular source file:
 | If the PO gets lost, keeping this translation up-to-date will be harder ;)</pre>
<p>Likewise, gettext&#8217;s regular <font SIZE="-1">PO</font> files only need to be copied to the <i>po/</i> directory. But <code>this is not the case of the ones manipulated by po4a</code>. The major risk here is that a developer erases the existing translation of his program with the translation of his documentation. (Both of them can&#8217;t be stored in the same <font SIZE="-1">PO</font> file, because the program needs to install its translation as an mo file while the documentation only uses its translation at compile time). That&#8217;s why the <font SIZE="-1">PO</font> files produced by the po-debiandoc module contain the following header: </p>
<pre> #
 # ADVISES TO DEVELOPERS:
 # - you do not need to manually edit POT or PO files.
 # - this file contains the translation of your debconf templates.
 # Do not replace the translation of your program with this !!
 # (or your translators will get very upset)
 #
 # ADVISES TO TRANSLATORS:
 # If you are not familiar with the PO format, gettext documentation 
 # is worth reading, especially sections dedicated to this format.
 # For example, run:
 # info -n '(gettext)PO Files'
 # info -n '(gettext)Header Entry'
 #
 # Some information specific to po-debconf are available at
 # /usr/share/doc/po-debconf/README-trans
 # or <a rel="nofollow" href="http://www.debian.org/intl/l10n/po-debconf/README-trans">http://www.debian.org/intl/l10n/po-debconf/README-trans</a>
 #</pre>
<h3><font SIZE="-1">SUMMARY</font> of the advantages of the gettext based approach</h3>
<dl>
<dt>&bull;</p>
<dd>The translations are not stored along with the original, which makes it possible to detect if translations become out of date.</p>
<dt>&bull;</p>
<dd>The translations are stored in separate files from each other, which prevents translators of different languages from interfering, both when submitting their patch and at the file encoding level.</p>
<dt>&bull;</p>
<dd>It is based internally on <code>gettext</code> (but <code>po4a</code> offers a very simple interface so that you don&#8217;t need to understand the internals to use it). That way, we don&#8217;t have to re-implement the wheel, and because of their wide use, we can think that these tools are more or less bug free.</p>
<dt>&bull;</p>
<dd>Nothing changed for the end-user (beside the fact translations will hopefully be better maintained). The resulting documentation file distributed is exactly the same.</p>
<dt>&bull;</p>
<dd>No need for translators to learn a new file syntax and their favorite <font SIZE="-1">PO</font> file editor (like Emacs&#8217; <font SIZE="-1">PO</font> mode, Lokalize or Gtranslator) will work just fine.</p>
<dt>&bull;</p>
<dd>gettext offers a simple way to get statistics about what is done, what should be reviewed and updated, and what is still to do. Some example can be found at those addresses: </p>
<pre> - <a rel="nofollow" href="http://kv-53.narod.ru/kaider1.png">http://kv-53.narod.ru/kaider1.png</a>
 - <a rel="nofollow" href="http://www.debian.org/intl/l10n/">http://www.debian.org/intl/l10n/</a></pre>
</dl>
<p> But everything isn&#8217;t green, and this approach also has some disadvantages we have to deal with.</p>
<dl>
<dt>&bull;</p>
<dd>Addenda are&#8230; strange at the first glance.</p>
<dt>&bull;</p>
<dd>You can&#8217;t adapt the translated text to your preferences, like splitting a paragraph here, and joining two other ones there. But in some sense, if there is an issue with the original, it should be reported as a bug anyway.</p>
<dt>&bull;</p>
<dd>Even with an easy interface, it remains a new tool people have to learn. </p>
<p> One of my dreams would be to integrate somehow po4a to Gtranslator or Lokalize. When an <font SIZE="-1">SGML</font> file is opened, the strings are automatically extracted. When it&#8217;s saved a translated <font SIZE="-1">SGML</font> file can be written to disk. If we manage to do an <font SIZE="-1">MS</font> Word (<font SIZE="-1">TM</font>) module (or at least <font SIZE="-1">RTF</font>) professional translators may even use it.</dl>
<h2>Authors</h2>
<pre> Denis Barbier &lt;barbier,linuxfr.org&gt;
 Martin Quinson (mquinson#debian.org)</pre>
