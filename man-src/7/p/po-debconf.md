---
title: "po-debconf(7)"
name: "po-debconf"
section: "7"
letter: "p"
url: "/docs/linux/man/7-po-debconf/"
description: "po-debconf – introduction"
---

<p>po-debconf &#8211; introduction</p>
<h2>Description</h2>
<p>The goal of <tt>&quot;debconf&quot;</tt> was to make package configuration user-friendly. In order to achieve this, it is important to ensure that users will get the question in their own language. Translators need a framework to easily work on translations without having to track package development; <tt>&quot;po-debconf&quot;</tt> was designed to be able to work with standard <tt>&quot;gettext&quot;</tt> tools when translating debconf templates files.</p>
<h2>Adding I18N Support To Debconf Templates Files</h2>
<p>If you are adding debconf support to your package, you have written a templates file containing English text. To add proper i18n support into your package, you need to:</p>
<dl>
<dt>&#8211; Create <i>debian/po/POTFILES.in</i></p>
<dd>This file contains the list of master templates. It typically contains a single line: </p>
<pre> [type: gettext/rfc822deb] templates</pre>
<p>Paths are relative to the parent directory.</p>
<dt>&#8211; Prepend an underscore before translatable fields in each template</p>
<dd>Normally <tt>&quot;Description&quot;</tt>, <tt>&quot;Choices&quot;</tt> and sometimes <tt>&quot;Default&quot;</tt> fields can be translated.</p>
<dt>&#8211; Run <code>debconf-updatepo</code></p>
<dd>This will create the <i>debian/po/templates.pot</i> file that translators will translate into their language.</p>
<dt>&#8211; Add a build dependency on &quot;po-debconf&quot; in <i>debian/control</i></p>
<dd></dl>
<h2>Update Templates</h2>
<p>In order to help translators, <font SIZE="-1">PO</font> files in your package should always be up-to-date, otherwise they may waste their time translating unused strings. For that, simply call the following command without arguments: </p>
<pre> $ debconf-updatepo</pre>
<p>You should run this command every time you change templates in English, but also when you receive new or updated translations, because translators may have worked on an obsolete <font SIZE="-1">PO</font> file. </p>
<p> If you rename, add or remove some templates files, remember also to edit <i>debian/po/POTFILES.in</i> accordingly, otherwise English strings are missing from <font SIZE="-1">PO</font> files and will be displayed to users even if <font SIZE="-1">PO</font> files are fully translated. </p>
<p> The <code>debconf-updatepo</code> program is idempotent, it modifies <font SIZE="-1">PO</font> files only if their content has been updated. Thus the best way to provide up-to-date <font SIZE="-1">PO</font> files in your source package is to call this command from the <tt>&quot;clean&quot;</tt> target of the <i>debian/rules</i> file. </p>
<p> Please note that you need to run <code>debconf-updatepo</code> even if you use <code>dh_installdebconf</code>. The latter calls <code>po2debconf</code> which used to call <code>debconf-updatepo</code> if outdated files were detected, but this is no more the case because it was not a good solution for at least two reasons:</p>
<dl>
<dt>1.</p>
<dd><code>po2debconf</code> relied on timestamps to detect outdated files, and may be abused when using <tt>&quot;pbuilder&quot;</tt> or if an outdated translation has been stored on disk after templates have been modified</p>
<dt>2.</p>
<dd><code>dh_installdebconf</code> is called long after <tt>&quot;.diff.gz&quot;</tt> file has been generated</dl>
<h2>Merge Translations And Original</h2>
<p>You have to make sure that when your package is compiled, translations will get into the built package. You can do that manually, or automatically using the <code>dh_installdebconf</code> script (make sure to have a versioned build dependency against <tt>&quot;debhelper (&gt;= 4.1.16)&quot;</tt>). </p>
<p> To do that manually, you&#8217;ll have to merge the templates and the translations at compile time (and to have a build depend against <tt>&quot;po-debconf&quot;</tt>) like this: </p>
<pre> $ po2debconf debian/templates &gt; debian/tmp/DEBIAN/templates</pre>
<p><font SIZE="-1"><code>BE CAREFUL</code></font>: the two files called <i>templates</i> are not the same at all. The first one contains only the English text, with marks to denote some fields to be translated while the second contains all languages. That is to say that you <font SIZE="-1">CANNOT</font> keep only the merged templates, or you won&#8217;t be able to deal with translations as people submit them to you.</p>
<h2>New Master Templates</h2>
<p>The new templates file source format is almost identical to one of distributed templates files, but translatable fields are prepended with an underscore. Example: </p>
<pre> Template: debconf/frontend
 Type: select
 _Choices: Dialog, Readline, Gnome, Editor, Noninteractive
 Default: Dialog
 _Description: Interface to use for configuring packages:
 Packages that use debconf for configuration share a common look and
 feel. You can select the type of user interface they use.
 .
 The dialog frontend is a full-screen, character based interface,
 while the readline frontend uses a more traditional plain text
 interface, and the gnome frontend is a modern X interface. The
 editor frontend lets you configure things using your favorite text
 editor. The noninteractive frontend never asks you any questions.</pre>
<h3><font SIZE="-1">SPLITTING CHOICES LIST</font></h3>
<p>Since <tt>&quot;po-debconf&quot;</tt> 0.6.0, localized fields may contain two leading underscores. In this case, the field value is supposed to be a comma separated list of values, which are put in separate msgids. Thus if the previous example did contain </p>
<pre> __Choices: Dialog, Readline, Gnome, Editor, Noninteractive</pre>
<p>there would be 5 different msgids. Note that spaces after commas are not significant. </p>
<p> When a choices list never changes, <tt>&quot;_Choices&quot;</tt> may be considered fine. However, splitting such lists may help avoiding frequent mistakes in translations such as omitting a choice or using non-standard commas. For such reasons, the use of <tt>&quot;__Choices&quot;</tt> will ease translator&#8217;s life and is strongly recommended. </p>
<p> Unfortunately if you decide to switch from <tt>&quot;_Choices&quot;</tt> to <tt>&quot;__Choices&quot;</tt>, all translations become fuzzy. Here is an explanation to make this change without translation loss (it requires <tt>&quot;po-debconf&quot;</tt> &gt;= 1.0). Suppose that we want to switch the previous example to <tt>&quot;__Choices&quot;</tt>. You copy the <i>templates</i> file into a temporary file. </p>
<pre> $ cp debian/templates debian/foo</pre>
<p>Edit <i>debian/foo</i> and keep only <tt>&quot;Template&quot;</tt>, <tt>&quot;Type&quot;</tt> and <tt>&quot;_Choices&quot;</tt> fields, which are in this example </p>
<pre> Template: debconf/frontend
 Type: select
 _Choices: Dialog, Readline, Gnome, Kde, Editor, Noninteractive</pre>
<p>Run <code>debconf-gettextize</code> with <tt>&quot;--merge&quot;</tt> and <tt>&quot;--choices&quot;</tt> flags to build <font SIZE="-1">PO</font> files as if <tt>&quot;__Choices&quot;</tt> was written, and merge these <font SIZE="-1">PO</font> files to existing ones: </p>
<pre> $ debconf-gettextize --merge --choices debian/foo</pre>
<p>Eventually you have to remove <i>foo</i> and manually edit <i>debian/templates</i> to replace <tt>&quot;_Choices&quot;</tt> by <tt>&quot;__Choices&quot;</tt> before <code>debconf-updatepo</code> is run.</p>
<h3><font SIZE="-1">PUTTING IN COMMENTS FOR TRANSLATORS</font></h3>
<p><tt>&quot;Dpkg&quot;</tt> maintainers decided that by convention lines beginning with a number sign (<tt>&quot;#&quot;</tt>) are comments in <i>debian/control</i> files, and <tt>&quot;po-debconf&quot;</tt> follows this rule. Since <tt>&quot;po-debconf&quot;</tt> 0.8.0, such comments are written into <font SIZE="-1">PO</font> files, and can then contain valuable information for translators. Incidentally all previous <tt>&quot;po-debconf&quot;</tt> versions ignore lines which do not contain a colon, thus if your comments does not contain any colons, there is no need to add a versioned build dependency against <tt>&quot;po-debconf&quot;</tt>. Here is an example: </p>
<pre> Template: debconf/button-yes
 Type: text
 # Translators, this text will appear on a button, so KEEP IT SHORT
 _Description: Yes</pre>
<p>Special comments have been introduced in <tt>&quot;po-debconf&quot;</tt> 1.0 to deal with strings which are composed of several items (as with <i>Choices</i> field) or paragraphs (like <i>Description</i>). With these directives, developers have a better control over what is exposed to translators. They are in the form <tt>&quot;#flag:</tt>directive<tt>&quot;</tt>; directives are detailed below.</p>
<dl>
<dt><code>translate:</code><i>spec</i>, <code>translate!:</code><i>spec</i></p>
<dd>Mark only some items as translatable; <i>spec</i> is a comma separated list of numbers, it specifies which strings will be printed into <font SIZE="-1">PO</font> files. Ranges can also be defined via a minus sign (for instance <tt>&quot;2-6&quot;</tt>), and a star (<tt>&quot;*&quot;</tt>) means all strings. For instance, with </p>
<pre> Template: partman-basicfilesystems/fat_mountpoint
 Type: select
 #flag:translate:3,4
 __Choices: /dos, /windows, Enter manually, Do not mount it
 _Description: Mount point for this partition:</pre>
<p><tt>&quot;Enter manually&quot;</tt> and <tt>&quot;Do not mount it&quot;</tt> will appear in <font SIZE="-1">PO</font> files but not <tt>&quot;/dos&quot;</tt> and <tt>&quot;/windows&quot;</tt>. When an exclamation mark follows the <code>translate</code> keyword, <i>spec</i> specifies which strings will be discarded from <font SIZE="-1">PO</font> files, all other strings are printed. Previous example is similar to </p>
<pre> Template: partman-basicfilesystems/fat_mountpoint
 Type: select
 #flag:translate!:1,2
 __Choices: /dos, /windows, Enter manually, Do not mount it
 _Description: Mount point for this partition:</pre>
<p>The same keyword can also be applied to the <i>Description</i> field to make sure that some strings are not translated. </p>
<pre> Template: partman-crypto/options_missing
 Type: error
 #flag:translate!:3
 _Description: Required encryption options missing
 The encryption options for ${DEVICE} are incomplete. Please
 return to the partition menu and select all required options.
 .
 ${ITEMS}</pre>
<p>But this is hazardous because context may be dropped from <font SIZE="-1">PO</font> files, please add comments in this case so that translators are not confused.</p>
<dt><code>comment:</code><i>spec</i>, <code>comment!:</code><i>spec</i></p>
<dd>The comment just below this directive applies to the strings specified by <i>spec</i>, which is defined above. By default, a comment written before a translatable field is printed along with all strings belonging to this field. (Note: with <tt>&quot;po-debconf&quot;</tt> &lt; 1.0, the comment was printed only with the first string) </p>
<pre> Template: arcboot-installer/prom-variables
 Type: note
 # Translators, the 4th string of this description has been dropped
 # from PO files. It contains shell commands and should not be
 # translated.
 #flag:comment:3
 # &quot;Stop for Maintenance&quot; should be left in English
 #flag:translate!:4
 _Description: Setting PROM variables for Arcboot
 If this is the first Linux installation on this machine, or if the
 hard drives have been repartitioned, some variables need to be set
 in the PROM before the system is able to boot normally.
 .
 At the end of this installation stage, the system will reboot.
 After this, enter the command monitor from the &quot;Stop for
 Maintenance&quot; option, and enter the following commands:
 .
 setenv OSLoader arcboot
 setenv OSLoadFilename Linux
 .
 You will only need to do this once. Afterwards, enter the &quot;boot&quot;
 command or reboot the system to proceed to the next stage of the
 installation.</pre>
<p>The example above has a comment without <tt>&quot;#flag:comment&quot;</tt> directive, where an implicit <tt>&quot;#flag:comment:*&quot;</tt> is added. This comment appears with all strings, but the one about <i>Stop for Maintenance</i> is printed only before the relevant string.</p>
<dt><code>partial</code></p>
<dd>This keyword tells <code>po2debconf</code> to keep translated strings even if all strings have not been translated. Please use with caution, this keyword has been introduced for very specific purposes.</dl>
<h3><font SIZE="-1">GIVING NOTICES TO TRANSLATORS BEFORE UPLOADING</font></h3>
<p>Usually translators notice on the status web pages (see below) that translations are outdated, and send patches which will be included in future uploads. But developers are encouraged to ask maintainers of outdated translations for an update before an upload, for instance one week in advance. A dedicated tool, <code>podebconf-report-po</code>, has been written for this purpose. Do not hesitate to abuse it!</p>
<h2>Debugging</h2>
<p>You will find that <code>debconf-loadtemplate</code> will not accept a templates file with i18n markups. However, it will accept a merged file, so if you have been debugging your debconf setup like this </p>
<pre> rm /tmp/{config,templates}.dat{,-old}
 debconf-loadtemplate debian/templates
 DEBIAN_PRIORITY=low debconf -freadline debian/config configure 28.0</pre>
<p>you will now need something like this instead: </p>
<pre> po2debconf debian/templates &gt; debian/tmp/DEBIAN/templates
 rm /tmp/{config,templates}.dat{,-old}
 debconf-loadtemplate debian/tmp/DEBIAN/templates
 DEBIAN_PRIORITY=low debconf -freadline debian/config configure 28.0</pre>
<h2>Caveats</h2>
<dl>
<dt>&bull;</p>
<dd><tt>&quot;Debconf&quot;</tt> 1.2.0 recognizes fields in the form <i>Name</i>&#8211;<i>lang</i>.<i>encoding</i>, e.g. <tt>&quot;Description-de.ISO-8859-1&quot;</tt> or <tt>&quot;Choices-ru.KOI8-R&quot;</tt>. By default <code>po2debconf</code> writes templates files in that new format. Older <tt>&quot;debconf&quot;</tt> will ignore these fields, and English text is displayed. See <code><a href="/docs/linux/man/1-po2debconf/">po2debconf</a></code>(1) to know how to change encoding and output format.</p>
<dt>&bull;</p>
<dd>A given English string may be given only one unique translation in a given language. It is impossible to give two different translations, depending on the context. To solve this issue, you have to add special markups to the different occurrences of a given string to make them different. (These markers will only be visible to translators, and they will be removed from the string before being displayed to user) </p>
<p> Such markers must be added to the end of the strings to translate, they must start with <tt>&quot;[ &quot;</tt> (a left bracket followed by a space) and end with <tt>&quot;]&quot;</tt> (right bracket), and may contain any character but brackets or new lines. For example <tt>&quot;[ blahblah]&quot;</tt> is a valid marker while <tt>&quot;[ bla[bla]bla]&quot;</tt> isn&#8217;t. For Perl regexp addicts, the markers are recognized (and removed) using this rule: </p>
<pre> $msg =~ s/\[\s[^\[\]]*\]$//s;</pre>
<dt>&bull;</p>
<dd>Spacing is not handled exactly the same way by <tt>&quot;po-debconf&quot;</tt> and <tt>&quot;debconf-utils&quot;</tt>; with the latter, paragraphs are reformatted when updating and merging translations, so <tt>&quot;debconf-utils&quot;</tt> is very smart and spaces are not considered as being part of strings when determining fuzzy entries. (i.e., the ones needing translator&#8217;s attention because the original changed) </p>
<p> On the other hand <tt>&quot;po-debconf&quot;</tt> relies on <tt>&quot;gettext&quot;</tt> to detect fuzzy entries, and it does not treat spaces as special characters. Thus superfluous spaces must be removed at end of lines in master templates files, or they will appear in <font SIZE="-1">PO</font> and <font SIZE="-1">POT</font> files. </p>
<p> For the same reason, <code>debconf-gettextize</code> can mark text fuzzy because of mismatch with space characters, and translators have to manually unfuzzy such strings. This only happens once when converting templates to <tt>&quot;po-debconf&quot;</tt> format, unless you randomly change spaces in master templates files, which will be painful for translators.</p>
<dt>&bull;</p>
<dd>Normally the <i>Default:</i> field must not be translated when template type is <code>Select</code> or <code>Multiselect</code>. Under rare circumstances (e.g. when selecting the default language for an application) localized values may be meaningful. </p>
<p> The localized value must not be translated, but chosen from the English values listed in the <i>Choices</i> field. The best way to achieve this goal is to insert a comment in your templates file which will be copied into <font SIZE="-1">PO</font> files. </p>
<pre> Template: geneweb/lang
 Type: select
 __Choices: Danish (da), Dutch (nl), English (en), Esperanto (eo)
 # You must NOT translate this string, but you can change its value.
 # The comment between brackets is used to distinguish this msgid
 # from the one in the Choices list; you do not have to worry about
 # them, and have to simply choose a msgstr among the English values
 # listed in the Choices field above, e.g. msgstr &quot;Dutch (nl)&quot;
 _Default: English (en)[ default language]
 _Description: Geneweb default language</pre>
<p>The default value also appears in the <i>Choices</i> field, and both have different translations: the former is an untranslated value chosen among <i>Choices</i> values, whereas the latter is a normal translation. As <tt>&quot;gettext&quot;</tt> cannot have two different translations for the same <i>msgid</i>, both <i>msgids</i> must be different by using bracketed comments as described in a previous subsection. </p>
<p> Prior to <tt>&quot;po-debconf&quot;</tt> 0.8.0, such comments were not available and maintainers had to replace the <i>_Default:</i> field by <i>_DefaultChoice:</i> in order to highlight such fields in <font SIZE="-1">PO</font> files: </p>
<pre> #. DefaultChoice
 msgid &quot;&quot;
 &quot;English[ default: do not translate bracketed material, put your &quot;
 &quot;own language here but UNTRANSLATED. If it is not in the list, &quot;
 &quot;put English (without bracketed material)]&quot;
 msgstr &quot;&quot;
 &quot;Swedish&quot;</pre>
<p>Plain comments in templates files are less error prone and are encouraged.</dl>
<h2>Status Web Pages</h2>
<p>Statistics for <tt>&quot;po-debconf&quot;</tt> translations are available at &lt;<a rel="nofollow" href="http://www.debian.org/intl/l10n/po-debconf/">http://www.debian.org/intl/l10n/po-debconf/</a>&gt; (or from mirrors); they are automatically updated when new packages are uploaded. Only packages shipping <i>debian/po/templates.pot</i> and <i>debian/po/POTFILES.in</i> files are considered, so you should make sure your source package provides them. </p>
<p> Translators can grab <font SIZE="-1">PO</font> and <font SIZE="-1">POT</font> files from there, but they must always get in touch with the previous translator (her mail address can be found in the <font SIZE="-1">PO</font> file) and/or their fellow translators on debian-l10n-<i>&lt;language&gt;</i><tt>@lists</tt>.debian.org (if such a list does exist) to make sure that no one is currently working on the same translation, and read current bugreports against the package they are going to translate to see if a translation has already been reported. </p>
<p> After translating these files, they should submit their work to the maintainer as bug report of severity <code>wishlist</code> with the <code>patch</code> tag.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-debconf-gettextize/">debconf-gettextize</a></code>(1), <code><a href="/docs/linux/man/1-debconf-updatepo/">debconf-updatepo</a></code>(1), <code><a href="/docs/linux/man/1-dh_installdebconf/">dh_installdebconf</a></code>(1), <code><a href="/docs/linux/man/1-podebconf-report-po/">podebconf-report-po</a></code>(1), <code><a href="/docs/linux/man/1-po2debconf/">po2debconf</a></code>(1), <code><a href="/docs/linux/man/7-debconf-devel/">debconf-devel</a></code>(7).</p>
<h2>Authors</h2>
<pre> Martin Quinson &lt;Martin.Quinson [at] ens-lyon.fr&gt;
 Denis Barbier &lt;barbier [at] linuxfr.org&gt;</pre>
