---
title: "podebconf-report-po(1)"
name: "podebconf-report-po"
section: "1"
letter: "p"
url: "/docs/linux/man/1-podebconf-report-po/"
description: "podebconf-report-po – send outdated debconf PO files to the last translators"
---

<h2 class="name">NAME</h2>
<p> podebconf-report-po &#8211; send outdated debconf PO files to the last translators </p>
<h2>SYNOPSIS</h2>
<p> <code>podebconf-report-po</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> This program reads a directory with po files to determine which files contain fuzzy or missing translations, launches an editor to allow modifications of mail body and headers, asks confirmation to send mails, and sends them to the last translator requesting updates. The mail will contain the <font SIZE="-1">PO</font> file which has to be updated. <code>podebconf-report-po</code> can be called either in the top-level directory, or in <i>debian</i> or <i>debian/po</i> subdirectories (or, for non debconf translations, from the <code>po</code> directory itself or its parent directory). </p>
<p> <code>podebconf-report-po</code> can also be used to send a call for translations to a mailing list. In that case, the <font SIZE="-1">POT</font> file will be attached. </p>
<p> Different templates exist for translation update requests, request to send updated <font SIZE="-1">PO</font> files to a bug report (<code>&#8211;submit</code>) or for calls for translations (<code>&#8211;call</code>). The template can also be provided by the user. See the <font SIZE="-1"><code>TEMPLATES</code></font> section for more information on the templates.</p>
<h2>OPTIONS</h2>
<p> Many options can be set in a configuration file. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font>.</p>
<dl>
<dt><code>&#8211;addlanguageteam=</code><font SIZE="-1">LANGUAGE</font><code>:</code><font SIZE="-1">LIST</font></p>
<dd> Specify a mailing list for a given language. This mailing list will be added to the <font SIZE="-1">CC</font> list for the <font SIZE="-1">PO</font> files of this language when <code>&#8211;languageteam</code> is used, in addition to the language team specified in the <font SIZE="-1">PO</font> file (if these mailing lists differ). </p>
<p> This is useful to keep the specified team informed, and allow a faster reaction when a translator is known to be inactive. </p>
<p> This option can be specified more than once. The language code and language mailing list are separated by a colon. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;bts=</code><font SIZE="-1">NUMBER</font></p>
<dd> After a bug report has been filed (either manually or with the <code>&#8211;submit</code> flag) to track down translations, <code>podebconf-report-po</code> can be run again, but this time with the <code>&#8211;bts=</code><font SIZE="-1">NUMBER</font> flag. Translators are then requested to respect the <code>Reply-To:</code> header field which is set to this bug report, so that all translations are gathered into a single location.</p>
<dt><code>&#8211;call[=</code><font SIZE="-1">MAILING_LIST</font><code>]</code></p>
<dd> Send a call for translations. If the optional <i></i><font SIZE="-1"><i>MAILING_LIST</i></font><i></i> argument is not specified, the call for translations is sent to the Debian Internationalization list (<i>debian-i18n [at] lists.debian.org</i>). </p>
<p> Calls for translations are useful to receive translations in new languages. </p>
<p> By default, calls for translation are combined with regular requests for updates sent to translators, for the existing translations. You can disable this default behavior with the <code>&#8211;withouttranslators</code> option.</p>
<dt><code>&#8211;conf=</code><font SIZE="-1">FILE</font></p>
<dd> Specify the configuration file. By default, <code>podebconf-report-po</code> reads <i></i>$HOME<i>/.podebconf-report-po.conf</i>.</p>
<dt><code>&#8211;noconf</code></p>
<dd> Do not read any configuration file.</p>
<dt><code>&#8211;deadline=</code><font SIZE="-1">DEADLINE</font></p>
<dd> Specify the deadline for receiving the updated translations (default is no deadline). </p>
<p> This should be a date, which will be prefixed by:<br />
&nbsp;The deadline for receiving the updated translation is<br />
&nbsp;<i></i><font SIZE="-1"><i>DEADLINE</i></font><i></i>. </p>
<p> If the specified string starts with a &#8216;+&#8217;, it will be interpreted by:<br />
&nbsp;LC_ALL=C date -R -d&nbsp;<i></i><font SIZE="-1"><i>DEADLINE</i></font><i></i> </p>
<p> If no deadline is specified (and the <code>&#8211;nodeadline</code> option is not used), a deadline will be prompted to the user, proposing a default deadline set to +10days. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;nodeadline</code></p>
<dd> Deactivate the deadline indication to translators, and avoid the deadline prompts. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;default</code></p>
<dd> Do not open the editor and use the template as is. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;nodefault</code></p>
<dd> Open an editor before sending the email(s).</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Send the email(s) without confirmation. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;noforce</code></p>
<dd> Ask for confirmation before sending email(s).</p>
<dt><code>&#8211;from=</code><font SIZE="-1">FROM</font></p>
<dd> Specify the name and the email address of the sender (default is taken from the <font SIZE="-1"><code>DEBEMAIL</code></font> and <font SIZE="-1"><code>DEBFULLNAME</code></font> environment variables, or from the <font SIZE="-1"><code>EMAIL</code></font> environment variable, or is set to the package maintainer if these variables are not set). </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;gzip</code></p>
<dd> Compress <font SIZE="-1">PO</font> files in attachment with <tt>&quot;gzip&quot;</tt>. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;nogzip</code></p>
<dd> Do not compress <font SIZE="-1">PO</font> files.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print usage information and exit.</p>
<dt><code>&#8211;langs=</code><font SIZE="-1">LANGUAGES</font></p>
<dd> Specify a list of languages to restrict sending the notification only for these languages. The list of languages is comma separated. The <font SIZE="-1">PO</font> files must be named according to these languages, with the .po extension.</p>
<dt><code>&#8211;languageteam</code></p>
<dd> Send the email also to the Language Team as carbon copy. </p>
<p> It is enabled by default. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;nolanguageteam</code></p>
<dd> Do not send the email(s) to the language teams. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;mutt</code></p>
<dd> Send the mails with mutt. This set the <code>&#8211;postpone</code> argument to <i></i>$HOME<i>/postponed</i>.</p>
<dt><code>&#8211;notdebconf</code></p>
<dd> Indicate that it is not a debconf translation. <code>podebconf-report-po</code> will use the <i>translator-po</i>, <i>call-po</i>, or <i>submit-po</i> template (if no other templates are requested in the configuration file or in the command line). These templates do not mention debconf in the subject or mail body and are more suitable for non-debconf translations. </p>
<p> This option also changes the default <i>po</i> directory used by <code>podebconf-report-po</code> (i.e. the <code>&#8211;podir</code> option is not needed when the call is done from the <i>po</i> directory itself or from its parent directory). </p>
<p> By default, a <i>debian/po</i> directory is preferred over a <i>po</i> directory. With this option, only the <i>po</i> directory will be considered. </p>
<p> This option is usually not necessary. <code>podebconf-report-po</code> tries to determine the type of translation based on the current directory and the existence of a <i>debian/po</i> or <i>po</i> directory.</p>
<dt><code>&#8211;package=</code><font SIZE="-1">PACKAGE</font></p>
<dd> Specify the name of the package (default is the source package name).</p>
<dt><code>&#8211;podir=</code><font SIZE="-1">DIR</font></p>
<dd> Specify where the <font SIZE="-1">PO</font> files are located. By default, <code>podebconf-report-po</code> checks if it is called from a <i>po</i> directory, or it searches for a <i>debian/po</i> directory (this can be disabled with the <code>&#8211;notdebconf</code> option), or for a <i>po</i> directory.</p>
<dt><code>&#8211;postpone=</code><font SIZE="-1">MBOX</font></p>
<dd> Do not send emails, append them in <i></i><font SIZE="-1"><i>MBOX</i></font><i></i>. This file can be used as a postponed mailbox with <code>mutt -p</code>.</p>
<dt><code>&#8211;potfile=</code><font SIZE="-1">POTFILE</font></p>
<dd> Specify the <font SIZE="-1">POT</font> file to send to a call for translations (<code>&#8211;call</code>). By default, <code>podebconf-report-po</code> uses the <font SIZE="-1">POT</font> file of the <font SIZE="-1">PO</font> files directory, if there is only one. </p>
<p> This file is also used to find the package&#8217;s name and version, if none were specified with an option, and if no <i>debian/changelog</i> files were found.</p>
<dt><code>&#8211;sendmessage</code></p>
<dd> Only send a message, with no attachments. This can be useful when the translators have a commit access to the package repository.</p>
<dt><code>&#8211;smtp=</code><font SIZE="-1">SERVER</font></p>
<dd> Specify <font SIZE="-1">SMTP</font> server for mailing (default is <tt>&quot;localhost&quot;</tt>). </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;submit</code></p>
<dd> Instead of sending mails to translators, file a bug report against this package to request for translations. This is useful e.g. when preparing non-maintainer uploads to make sure that translations do not get lost.</p>
<dt><code>&#8211;summary</code></p>
<dd> Send a status report to the maintainer with the list of emails sent to translators. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;nosummary</code></p>
<dd> Do not send any status report to the maintainer.</p>
<dt><code>&#8211;utf8</code></p>
<dd> Send the email in <font SIZE="-1">UTF-8.</font> This allow non-ascii characters in the mail body and mail header. The editor must support <font SIZE="-1">UTF-8.</font> </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;noutf8</code></p>
<dd> Send the email(s) in us-ascii. Non-ascii characters are replaced by a question mark.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display additional information while running. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;noverbose</code></p>
<dd> Do not use the verbose mode.</p>
<dt><code>&#8211;templatecall=</code><font SIZE="-1">TEMPLATE</font></p>
<dd> Specify a file to use as a template for the call for translations email(s). The default template is <i>/usr/share/po-debconf/templates/call</i>. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;templatesubmit=</code><font SIZE="-1">TEMPLATE</font></p>
<dd> Specify a file to use as a template for the email(s) sent to translators when the <code>&#8211;submit</code> option is used. The default template is <i>/usr/share/po-debconf/templates/submit</i>. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;templatetranslators=</code><font SIZE="-1">TEMPLATE</font></p>
<dd> Specify a file to use as a template for the email(s) sent to translators. The default template is <i>/usr/share/po-debconf/templates/translators</i>. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;template=</code><font SIZE="-1">TEMPLATE</font></p>
<dd> Specify file to use it as template for the email(s). If a template is specified with this option, this template will be used rather than a template specified with any of the <code>&#8211;templatetranslators</code>, <code>&#8211;templatesubmit</code>, or <code>&#8211;templatecall</code> options. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;notemplate</code></p>
<dd> Use the default template.</p>
<dt><code>&#8211;withtranslators</code></p>
<dd> Send requests for updates to the translators after sending the call for translation. </p>
<p> This option is ignored when the <code>&#8211;call</code> option is not specified. It is enabled by default. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</p>
<dt><code>&#8211;withouttranslators</code></p>
<dd> Do not send requests for translation update to the translators after a call for translations. </p>
<p> This option can be specified in the configuration file to define default behavior of <code>podebconf-report-po</code>. See section <font SIZE="-1"><code>CONFIGURATION FILE</code></font> below.</dl>
<h2>CONFIGURATION FILE</h2>
<p> By default, <code>podebconf-report-po</code> reads <i></i>$HOME<i>/.podebconf-report-po.conf</i>. The configuration file can be set with the <code>&#8211;conf</code> option. You can also ignore any configuration file by specifying the <code>&#8211;noconf</code> option. Command line options can be used to override configuration file settings. </p>
<p> The configuration files accept most of the command line options, without the leading <code>&#8212;</code>: <code>deadline</code>, <code>nodeadline</code>, <code>smtp</code>, <code>from</code>, <code>verbose</code>, <code>force</code>, <code>templatetranslators</code>, <code>templatesubmit</code>, <code>templatecall</code>, <code>template</code>, <code>default</code>, <code>gzip</code>, <code>languageteam</code>, <code>nolanguageteam</code>, <code>addlanguageteam</code>, <code>summary</code>, <code>utf8</code>, <code>withouttranslators</code>, <code>withtranslators</code>. </p>
<p> Lines starting by a number sign (possibly preceded by spaces) are comments and are ignored. </p>
<p> Here is an example:<br />
&nbsp;#&nbsp;This is a comment<br />
&nbsp;smtp smtp.mydomain<br />
&nbsp;from&nbsp;=&nbsp;Me Myself&nbsp;&lt;me [at] mydomain&gt;<br />
&nbsp;utf8</p>
<h2>TEMPLATES</h2>
<p> The templates specified with the <code>&#8211;template</code>, <code>&#8211;templatetranslators</code>, <code>&#8211;templatesubmit</code>, or <code>&#8211;templatecall</code> options can contain the following tags:</p>
<dl>
<dt><code>&lt;from</code>&gt;, <code>&lt;subject</code>&gt;, <code>&lt;reply-to</code>&gt;</p>
<dd> Replaced by the corresponding headers of the email(s).</p>
<dt><code>&lt;filelist</code>&gt;</p>
<dd> In the default mode, it is replaced by comments showing the list of translators with outdated translations. </p>
<p> In the <code>&#8211;submit</code> mode, it is replaced by the list of <font SIZE="-1">PO</font> files with outdated translations. </p>
<p> And in the <code>&#8211;call</code> mode, it is replaced by the list of <font SIZE="-1">PO</font> files found in the <font SIZE="-1">PO</font> directory.</p>
<dt><code>&lt;reply</code>&gt;</p>
<dd> Replaced by a string that indicates how the translators have to reply (e.g. follow the <i>Reply-To</i> tag or sending the <font SIZE="-1">PO</font> to a given bug report).</p>
<dt><code>&lt;deadline</code>&gt;</p>
<dd> Replaced by a string indicating the deadline for the translation (see <code>&#8211;deadline</code>).</p>
<dt><code>&lt;package</code>&gt;</p>
<dd> Replaced by the name of the package (if it was detected).</p>
<dt><code>&lt;statistics</code>&gt;</p>
<dd> Replaced by the statistics of the <font SIZE="-1">PO</font> files found in the <font SIZE="-1">PO</font> directory (in the <code>&#8211;call</code> mode only).</dl>
<p> The <i>/usr/share/po-debconf/templates</i> directory contains the default templates.</p>
<h2>EXAMPLES</h2>
<p> The recommended usage is to call <code>podebconf-report-po</code> from the <i>po</i> directory to be updated: </p>
<p> podebconf-report-po &#8211;call </p>
<p> This will send a call for new translations to the &lt;debian-i18n [at] lists.debian.org&gt; mailing list and will ask translation updates to the previous translators. The language teams will also be notified and should be able to react if the assigned translator is known to be <font SIZE="-1">MIA.</font> </p>
<p> A prompt will ask a deadline to the user (the default is to request translations and updates within 10 days). </p>
<p> Then an editor will display the message to be sent to the mailing list. When this editor exits, <code>podebconf-report-po</code> will ask confirmation to send the mail to the mailing list. </p>
<p> If confirmed, another editor will display the message to be sent to the translators and language teams. <code>podebconf-report-po</code> will ask for another confirmation to send the mails to translators and language teams. </p>
<p> You should make a new release with the received translations after the deadline.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-debconf-updatepo/">debconf-updatepo</a></code>(1)</p>
<h2>AUTHOR</h2>
<pre>
  Fabio Tranchitella &lt;kobold [at] kobold.it&gt;
</pre>
<h2>Index</h2>
