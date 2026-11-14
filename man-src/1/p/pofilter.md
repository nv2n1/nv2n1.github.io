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
<dt>&#8211;version</p>
<dd> show program&#8217;s version number and exit</p>
<dt>-h/&#8211;help</p>
<dd> show this help message and exit</p>
<dt>&#8211;manpage</p>
<dd> output a manpage based on the help</p>
<dt>&#8211;progress</p>
<dd> show progress as: dots, none, bar, names, verbose</p>
<dt>&#8211;errorlevel</p>
<dd> show errorlevel as: none, message, exception, traceback</p>
<dt>-i/&#8211;input</p>
<dd> read from INPUT in tmx, xlf, pot, xliff, po formats</p>
<dt>-x/&#8211;exclude</p>
<dd> exclude names matching EXCLUDE from input paths</p>
<dt>-o/&#8211;output</p>
<dd> write to OUTPUT in tmx, xlf, pot, po, xliff formats</p>
<dt>-l/&#8211;listfilters</p>
<dd> list filters available</p>
<dt>&#8211;review</p>
<dd> include units marked for review (default)</p>
<dt>&#8211;noreview</p>
<dd> exclude units marked for review</p>
<dt>&#8211;fuzzy</p>
<dd> include units marked fuzzy (default)</p>
<dt>&#8211;nofuzzy</p>
<dd> exclude units marked fuzzy</p>
<dt>&#8211;nonotes</p>
<dd> don&#8217;t add notes about the errors</p>
<dt>&#8211;autocorrect</p>
<dd> output automatic corrections where possible rather than describing issues</p>
<dt>&#8211;language</p>
<dd> set target language code (e.g. af-ZA) [required for spell check and recommended in general]</p>
<dt>&#8211;openoffice</p>
<dd> use the standard checks for OpenOffice translations</p>
<dt>&#8211;mozilla</p>
<dd> use the standard checks for Mozilla translations</p>
<dt>&#8211;drupal</p>
<dd> use the standard checks for Drupal translations</p>
<dt>&#8211;gnome</p>
<dd> use the standard checks for Gnome translations</p>
<dt>&#8211;kde</p>
<dd> use the standard checks for KDE translations</p>
<dt>&#8211;wx</p>
<dd> use the standard checks for wxWidgets translations</p>
<dt>&#8211;excludefilter</p>
<dd> don&#8217;t use FILTER when filtering</p>
<dt>-t/&#8211;test</p>
<dd> only use test FILTERs specified with this option when filtering</p>
<dt>&#8211;notranslatefile</p>
<dd> read list of untranslatable words from FILE (must not be translated)</p>
<dt>&#8211;musttranslatefile</p>
<dd> read list of translatable words from FILE (must be translated)</p>
<dt>&#8211;validcharsfile</p>
<dd> read list of all valid characters from FILE (must be in UTF-8) </p>
</dl>
<h2>Index</h2>
