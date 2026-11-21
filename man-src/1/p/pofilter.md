---
title: "pofilter(1)"
name: "pofilter"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pofilter/"
description: "pofilter – Perform quality checks on Gettext PO, XLIFF and TMX localization files."
---

<h2>NAME</h2>
<p> pofilter &#8211; Perform quality checks on Gettext PO, XLIFF and TMX localization files.</p>
<h2>SYNOPSIS</h2>
<p> <code>pofilter </code>[&#8211;version] [-h|&#8211;help] [&#8211;manpage] [&#8211;progress <i>PROGRESS</i>] [&#8211;errorlevel <i>ERRORLEVEL</i>] [-i|&#8211;input] <i>INPUT</i> [-x|&#8211;exclude <i>EXCLUDE</i>] [-o|&#8211;output] <i>OUTPUT</i> [-l|&#8211;listfilters] [&#8211;review] [&#8211;noreview] [&#8211;fuzzy] [&#8211;nofuzzy] [&#8211;nonotes] [&#8211;autocorrect] [&#8211;language <i>LANG</i>] [&#8211;openoffice] [&#8211;mozilla] [&#8211;drupal] [&#8211;gnome] [&#8211;kde] [&#8211;wx] [&#8211;excludefilter <i>FILTER</i>] [-t|&#8211;test <i>FILTER</i>] [&#8211;notranslatefile <i>FILE</i>] [&#8211;musttranslatefile <i>FILE</i>] [&#8211;validcharsfile <i>FILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> Snippet files are created whenever a test fails. These can be examined, corrected and merged back into the originals using pomerge. </p>
<p> See: <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pofilter.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pofilter.html</a> for examples and usage instructions and <a rel="nofollow" href="http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pofilter_tests.html">http://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pofilter_tests.html</a> for full descriptions of all tests.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</dt>
<dd> show program&#8217;s version number and exit</dd>
<dt>-h/&#8211;help</dt>
<dd> show this help message and exit</dd>
<dt>&#8211;manpage</dt>
<dd> output a manpage based on the help</dd>
<dt>&#8211;progress</dt>
<dd> show progress as: dots, none, bar, names, verbose</dd>
<dt>&#8211;errorlevel</dt>
<dd> show errorlevel as: none, message, exception, traceback</dd>
<dt>-i/&#8211;input</dt>
<dd> read from INPUT in tmx, xlf, pot, xliff, po formats</dd>
<dt>-x/&#8211;exclude</dt>
<dd> exclude names matching EXCLUDE from input paths</dd>
<dt>-o/&#8211;output</dt>
<dd> write to OUTPUT in tmx, xlf, pot, po, xliff formats</dd>
<dt>-l/&#8211;listfilters</dt>
<dd> list filters available</dd>
<dt>&#8211;review</dt>
<dd> include units marked for review (default)</dd>
<dt>&#8211;noreview</dt>
<dd> exclude units marked for review</dd>
<dt>&#8211;fuzzy</dt>
<dd> include units marked fuzzy (default)</dd>
<dt>&#8211;nofuzzy</dt>
<dd> exclude units marked fuzzy</dd>
<dt>&#8211;nonotes</dt>
<dd> don&#8217;t add notes about the errors</dd>
<dt>&#8211;autocorrect</dt>
<dd> output automatic corrections where possible rather than describing issues</dd>
<dt>&#8211;language</dt>
<dd> set target language code (e.g. af-ZA) [required for spell check and recommended in general]</dd>
<dt>&#8211;openoffice</dt>
<dd> use the standard checks for OpenOffice translations</dd>
<dt>&#8211;mozilla</dt>
<dd> use the standard checks for Mozilla translations</dd>
<dt>&#8211;drupal</dt>
<dd> use the standard checks for Drupal translations</dd>
<dt>&#8211;gnome</dt>
<dd> use the standard checks for Gnome translations</dd>
<dt>&#8211;kde</dt>
<dd> use the standard checks for KDE translations</dd>
<dt>&#8211;wx</dt>
<dd> use the standard checks for wxWidgets translations</dd>
<dt>&#8211;excludefilter</dt>
<dd> don&#8217;t use FILTER when filtering</dd>
<dt>-t/&#8211;test</dt>
<dd> only use test FILTERs specified with this option when filtering</dd>
<dt>&#8211;notranslatefile</dt>
<dd> read list of untranslatable words from FILE (must not be translated)</dd>
<dt>&#8211;musttranslatefile</dt>
<dd> read list of translatable words from FILE (must be translated)</dd>
<dt>&#8211;validcharsfile</dt>
<dd> read list of all valid characters from FILE (must be in UTF-8) </dd>
</dl>
