---

title: "dpkg-parsechangelog(1)"
name: "dpkg-parsechangelog"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-parsechangelog/"
description: "dpkg-parsechangelog – parse Debian changelog files"
---

<p> dpkg-parsechangelog &#8211; parse Debian changelog files </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-parsechangelog</code> [<i>option</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-parsechangelog</code> reads and parses the changelog of an unpacked Debian source tree and outputs the information in it to standard output in a machine-readable form.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code>, <code>&#8211;file</code> <i>changelog-file</i></dt>
<dd> Specifies the changelog file to read information from. A &#8216;-&#8216; can be used to specify reading from standard input. The default is <code>debian/changelog</code>.</dd>
<dt><code>-F</code> <i>changelog-format</i></dt>
<dd> Specifies the format of the changelog. By default the format is read from a special line near the bottom of the changelog or failing that defaults to the <code>debian</code> standard format. See also <code>CHANGELOG FORMATS</code>.</dd>
<dt><code>-L</code> <i>libdir</i></dt>
<dd> Obsolete option without effect (since dpkg 1.18.8). Setting the perl environment variables <code>PERL5LIB</code> or <code>PERLLIB</code> has a similar effect when looking for the parser perl modules.</dd>
<dt><code>-S</code>, <code>&#8211;show-field</code> <i>field</i></dt>
<dd> Specifies the name of the field to show (since dpkg 1.17.0). The field name is not printed, only its value.</dd>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Show the usage message and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version and exit.</dd></dl>
<h3>Parser Options</h3>
<p> The following options can be used to influence the output of the changelog parser, e.g. the range of entries or the format of the output.</p>
<dl>
<dt><code>&#8211;format</code> <i>output-format</i></dt>
<dd> Set the output format. Currently supported values are <code>dpkg</code> and <code>rfc822</code>. <code>dpkg</code> is the classic output format (from before this option existed) and the default. It consists of one paragraph in Debian control format (see <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5)). If more than one entry is requested, then most fields are taken from the first entry (usually the most recent entry), except otherwise stated:</dd>
<dl>
<dl>
<dt><code>Source:</code> <i>pkg-name</i></dt>
<dd>
</dd><dt><code>Version:</code> <i>version</i></dt>
<dd>
</dd><dt><code>Distribution:</code> <i>target-distribution</i></dt>
<dd>
</dd><dt><code>Urgency:</code> <i>urgency</i></dt>
<dd> The highest urgency of all included entries is used, followed by the concatenated (space-separated) comments from all the versions requested.</dd>
<dt><code>Maintainer:</code> <i>author</i></dt>
<dd>
</dd><dt><code>Date:</code> <i>date</i></dt>
<dd> The date of the entry as a string, as it appears in the changelog. With a <code><a href="/docs/linux/man/3-strptime/">strptime</a></code>(3) format &quot;%a<code>, </code>%d%b%Y%T%z&quot;, but where the day of the week might not actually correspond to the real day obtained from the rest of the date string. If you need a more accurate representation of the date, use the <code>Timestamp</code> field, but take into account it might not be possible to map it back to the exact value in this field.</dd>
<dt><code>Timestamp:</code> <i>timestamp</i></dt>
<dd> The date of the entry as a timestamp in seconds since the epoch (since dpkg 1.18.8).</dd>
<dt><code>Closes:</code> <i>bug-number</i></dt>
<dd> The Closes fields of all included entries are merged.</dd>
<dt><code>Changes:</code> <i>changelog-entries</i></dt>
<dd> The text of all changelog entries is concatenated. To make this field a valid Debian control format multiline field empty lines are replaced with a single full stop and all lines is intended by one space character. The exact content depends on the changelog format.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> The <code>Version</code>, <code>Distribution</code>, <code>Urgency</code>, <code>Maintainer</code> and <code>Changes</code> fields are mandatory. </p>
<p> There might be additional user-defined fields present. </p>
<p> The <code>rfc822</code> format uses the same fields but outputs a separate paragraph for each changelog entry so that all metadata for each entry is preserved.</dd></dl>
<dt><code>&#8211;reverse</code></dt>
<dd> Include all changes in reverse order (since dpkg 1.19.1). </dd>
<p> <code>Note:</code> For the <code>dpkg</code> format the first entry will be the most ancient entry.</p>
<dt><code>&#8211;all</code></dt>
<dd> Include all changes. <code>Note:</code> Other options have no effect when this is in use.</dd>
<dt><code>-s</code>, <code>&#8211;since</code> <i>version</i></dt>
<dd>
</dd><dt><code>-v</code> <i>version</i></dt>
<dd> Include all changes later than <i>version</i>.</dd>
<dt><code>-u</code>, <code>&#8211;until</code> <i>version</i></dt>
<dd> Include all changes earlier than <i>version</i>.</dd>
<dt><code>-f</code>, <code>&#8211;from</code> <i>version</i></dt>
<dd> Include all changes equal or later than <i>version</i>.</dd>
<dt><code>-t</code>, <code>&#8211;to</code> <i>version</i></dt>
<dd> Include all changes up to or equal than <i>version</i>.</dd>
<dt><code>-c</code>, <code>&#8211;count</code> <i>number</i></dt>
<dd>
</dd><dt><code>-n</code> <i>number</i></dt>
<dd> Include <i>number</i> entries from the top (or the tail if <i>number</i> is lower than 0).</dd>
<dt><code>-o</code>, <code>&#8211;offset</code> <i>number</i></dt>
<dd> Change the starting point for <code>&#8211;count</code>, counted from the top (or the tail if <i>number</i> is lower than 0).</dd></dl>
<h2>CHANGELOG FORMATS</h2>
<p> It is possible to use a different format to the standard one, by providing a parser for that alternative format. </p>
<p> In order to have <code>dpkg-parsechangelog</code> run the new parser, a line must be included within the last 40 lines of the changelog file, matching the Perl regular expression: &#8220;<code>\schangelog-format:\s+([0-9a-z]+)\W</code>&#8220;. The part in parentheses should be the name of the format. For example: </p>
<dl>
<dt>
</dt><dd> @@@ changelog-format: <i>otherformat</i> @@@</dd></dl>
<p> Changelog format names are non-empty strings of lowercase alphanumerics (&#8220;a-z0-9&#8221;). </p>
<p> If such a line exists then <code>dpkg-parsechangelog</code> will look for the parser as a <code>Dpkg::Changelog::</code><i>Otherformat</i> perl module; it is an error for it not being present. The parser name in the perl module will be automatically capitalized. The default changelog format is <code>debian</code>, and a parser for it is provided by default. </p>
<p> The parser should be derived from the Dpkg::Changelog class and implement the required documented interface. </p>
<p> If the changelog format which is being parsed always or almost always leaves a blank line between individual change notes, these blank lines should be stripped out, so as to make the resulting output compact. </p>
<p> If the changelog format does not contain date or package name information this information should be omitted from the output. The parser should not attempt to synthesize it or find it from other sources. </p>
<p> If the changelog does not have the expected format the parser should error out, rather than trying to muddle through and possibly generating incorrect output. </p>
<p> A changelog parser may not interact with the user at all.</p>
<h2>NOTES</h2>
<p> All <code>Parser Options</code> except for <code>-v</code> are only supported since dpkg 1.14.16. </p>
<p> Short option parsing with non-bundled values available only since dpkg 1.18.0.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DPKG_COLORS</code></dt>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dd>
<dt><code>DPKG_NLS</code></dt>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>debian/changelog</code></dt>
<dd> The changelog file, used to obtain version-dependent information about the source package, such as the urgency and distribution of an upload, the changes made since a particular release, and the source version number itself.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-deb-changelog/">deb-changelog</a></code>(5). </p>
