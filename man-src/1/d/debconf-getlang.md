---
title: "debconf-getlang(1)"
name: "debconf-getlang"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf-getlang/"
---

<h2 class="name">NAME</h2>
 

 debconf-getlang - extract a language from a templates file 

<h2>SYNOPSIS</h2>

 <pre><code>
debconf - getlang lang master[translation] debconf - getlang-- stats master translation[...]
</code></pre>

<h2>DESCRIPTION</h2>

 Note: This utility is deprecated; you should switch to using the po-debconf package. 

 This program helps make and manage translations of debconf templates. There are basically three situations in which this program might be called:
<dl>
<dt>A translation is just being started.
<dd> You want to provide the translator with a file they can work on that has the English fields from your templates file, plus blank Field-ll fields for the target language that they can fill in. 

 To do this, run the program with first parameter being the code for the language that is being translated to, and the second parameter being the filename of the English templates file.
<dt>A translation is well under way.
<dd> You have changed some English text, or added more items to your templates file, and you want to send the translators a file with the English text plus their current translations (or you are the translator, and you want to generate such a file for your own use). 

 To accomplish this, run the program with the first parameter being the the code for the language that is being translated to, the second parameter being the filename of the master English templates file, and the third parameter being the filename of the current translated file. 

 When run this way, the program is smart enough to notice fuzzy translations. For example a fuzzy Description will be output as Description-&lt;lang&gt;-fuzzy, and a new, blank Description-&lt;lang&gt; will be added. Translators should remove the -fuzzy fields as they correct the fuzzy translations.
<dt>Checking the status of a translation
<dd> To check the status of a translation, use the --status flag, and pass the english template file as the first parameter, and all the other translated templates after that. It will output statistics for each of them. For example: 

 <pre>
  debconf-getlang --stats debian/templates debian/templates.*
</pre></dl>

<h2>NOTE</h2>

 Note that the text in the generated templates may be word-wrapped by debconf.

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-debconf-mergetemplate/">debconf-mergetemplate</a></i>(1)

<h2>AUTHOR</h2>

 Joey Hess &lt;joeyh [at] debian.org&gt; 

<h2>Index</h2>


