---
title: "spamassassin(1)"
name: "spamassassin"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spamassassin/"
description: "spamassassin – extensible email filter used to identify spam"
---

<h2 class="name">NAME</h2>
<p> spamassassin &#8211; extensible email filter used to identify spam </p>
<h2>DESCRIPTION</h2>
<p> SpamAssassin is an intelligent email filter which uses a diverse range of tests to identify unsolicited bulk email, more commonly known as &#8220;spam&#8221;. These tests are applied to email headers and content to classify email using advanced statistical methods. In addition, SpamAssassin has a modular architecture that allows other technologies to be quickly wielded against spam and is designed for easy integration into virtually any email system.</p>
<h2>SYNOPSIS</h2>
<p> For ease of access, the SpamAssassin manual has been split up into several sections. If you&#8217;re intending to read these straight through for the first time, the suggested order will tend to reduce the number of forward references. </p>
<p> Extensive additional documentation for SpamAssassin is available, primarily on the SpamAssassin web site and wiki. </p>
<p> You should be able to view SpamAssassin&#8217;s documentation with your <i><a href="/docs/linux/man/1-man/">man</a></i>(1) program or <i><a href="/docs/linux/man/1-perldoc/">perldoc</a></i>(1).</p>
<h3><font SIZE="-1">OVERVIEW</font></h3>
<pre>
    spamassassin              SpamAssassin overview (this section)
</pre>
<h3><font SIZE="-1">CONFIGURATION</font></h3>
<pre>
    Mail::SpamAssassin::Conf  SpamAssassin configuration files
</pre>
<h3><font SIZE="-1">USAGE</font></h3>
<pre>
    spamassassin-run          &quot;spamassassin&quot; front-end filtering script
    sa-learn                  train SpamAssassin's Bayesian classifier
    spamc                     client for spamd (faster than spamassassin)
    spamd                     spamassassin server (needed by spamc)
</pre>
<h3><font SIZE="-1">DEFAULT PLUGINS</font></h3>
<pre>
    Mail::SpamAssassin::Plugin::AskDNS
    Mail::SpamAssassin::Plugin::AutoLearnThreshold
    Mail::SpamAssassin::Plugin::Bayes
    Mail::SpamAssassin::Plugin::BodyEval
    Mail::SpamAssassin::Plugin::Check
    Mail::SpamAssassin::Plugin::DKIM
    Mail::SpamAssassin::Plugin::DNSEval
    Mail::SpamAssassin::Plugin::FreeMail
    Mail::SpamAssassin::Plugin::HTMLEval
    Mail::SpamAssassin::Plugin::HTTPSMismatch
    Mail::SpamAssassin::Plugin::Hashcash
    Mail::SpamAssassin::Plugin::HeaderEval
    Mail::SpamAssassin::Plugin::ImageInfo
    Mail::SpamAssassin::Plugin::MIMEEval
    Mail::SpamAssassin::Plugin::MIMEHeader
    Mail::SpamAssassin::Plugin::Pyzor
    Mail::SpamAssassin::Plugin::Razor2
    Mail::SpamAssassin::Plugin::RelayEval
    Mail::SpamAssassin::Plugin::ReplaceTags
    Mail::SpamAssassin::Plugin::SPF
    Mail::SpamAssassin::Plugin::SpamCop
    Mail::SpamAssassin::Plugin::URIDNSBL
    Mail::SpamAssassin::Plugin::URIDetail
    Mail::SpamAssassin::Plugin::URIEval
    Mail::SpamAssassin::Plugin::VBounce
    Mail::SpamAssassin::Plugin::WLBLEval
    Mail::SpamAssassin::Plugin::WhiteListSubject
</pre>
<h2>WEB SITES</h2>
<pre>
    SpamAssassin web site:     <a rel="nofollow" href="http://spamassassin.apache.org/">http://spamassassin.apache.org/</a>
    Wiki-based documentation:  <a rel="nofollow" href="http://wiki.apache.org/spamassassin/">http://wiki.apache.org/spamassassin/</a>
</pre>
<h2>USER MAILING LIST</h2>
<p> A users mailing list exists where other experienced users are often able to help and provide tips and advice. Subscription instructions are located on the SpamAssassin web site.</p>
<h2>CONFIGURATION FILES</h2>
<p> The SpamAssassin rule base, text templates, and rule description text are loaded from configuration files. </p>
<p> Default configuration data is loaded from the first existing directory in:</p>
<dl>
<dt>/var/lib/spamassassin/3.004000</p>
<dd>
<dt>/usr/share/spamassassin</p>
<dd>
<dt>/usr/share/spamassassin</p>
<dd>
<dt>/usr/local/share/spamassassin</p>
<dd>
<dt>/usr/share/spamassassin</p>
<dd></dl>
<p> Site-specific configuration data is used to override any values which had already been set. This is loaded from the first existing directory in:</p>
<dl>
<dt>/etc/mail/spamassassin</p>
<dd>
<dt>/usr/etc/mail/spamassassin</p>
<dd>
<dt>/usr/etc/spamassassin</p>
<dd>
<dt>/usr/local/etc/spamassassin</p>
<dd>
<dt>/usr/pkg/etc/spamassassin</p>
<dd>
<dt>/usr/etc/spamassassin</p>
<dd>
<dt>/etc/mail/spamassassin</p>
<dd>
<dt>/etc/spamassassin</p>
<dd></dl>
<p> From those three directories, SpamAssassin will first read files ending in &#8220;.pre&#8221; in lexical order and then it will read files ending in &#8220;.cf&#8221; in lexical order (most files begin with two numbers to make the sorting order obvious). </p>
<p> In other words, it will read <i>init.pre</i> first, then <i>10_default_prefs.cf</i> before <i>50_scores.cf</i> and <i>20_body_tests.cf</i> before <i>20_head_tests.cf</i>. Options in later files will override earlier files. </p>
<p> Individual user preferences are loaded from the location specified on the <tt>&quot;spamassassin&quot;</tt>, <tt>&quot;sa-learn&quot;</tt>, or <tt>&quot;spamd&quot;</tt> command line (see respective manual page for details). If the location is not specified, <i>~/.spamassassin/user_prefs</i> is used if it exists. SpamAssassin will create that file if it does not already exist, using <i>user_prefs.template</i> as a template. That file will be looked for in:</p>
<dl>
<dt>/etc/mail/spamassassin</p>
<dd>
<dt>/usr/etc/mail/spamassassin</p>
<dd>
<dt>/usr/share/spamassassin</p>
<dd>
<dt>/etc/spamassassin</p>
<dd>
<dt>/etc/mail/spamassassin</p>
<dd>
<dt>/usr/local/share/spamassassin</p>
<dd>
<dt>/usr/share/spamassassin</p>
<dd></dl>
<h2>TAGGING</h2>
<p> The following two sections detail the default tagging and markup that takes place for messages when running <tt>&quot;spamassassin&quot;</tt> or <tt>&quot;spamc&quot;</tt> with <tt>&quot;spamd&quot;</tt> in the default configuration. </p>
<p> Note: before header modification and addition, all headers beginning with <tt>&quot;X-Spam-&quot;</tt> are removed to prevent spammer mischief and also to avoid potential problems caused by prior invocations of SpamAssassin.</p>
<h3><font SIZE="-1">TAGGING FOR SPAM MAILS</font></h3>
<p> By default, all messages with a calculated score of 5.0 or higher are tagged as spam. </p>
<p> If an incoming message is tagged as spam, instead of modifying the original message, SpamAssassin will create a new report message and attach the original message as a message/rfc822 <font SIZE="-1">MIME</font> part (ensuring the original message is completely preserved and easier to recover). </p>
<p> The new report message inherits the following headers (if they are present) from the original spam message:</p>
<dl>
<dt>From: header</p>
<dd>
<dt>To: header</p>
<dd>
<dt>Cc: header</p>
<dd>
<dt>Subject: header</p>
<dd>
<dt>Date: header</p>
<dd>
<dt>Message-ID: header</p>
<dd></dl>
<p> The above headers can be modified if the relevant <tt>&quot;rewrite_header&quot;</tt> option is given (see <tt>&quot;Mail::SpamAssassin::Conf&quot;</tt> for more information). </p>
<p> By default these message headers are added to spam:</p>
<dl>
<dt>X-Spam-Flag: header</p>
<dd> Set to <tt>&quot;YES&quot;</tt>.</dl>
<p> The headers that added are fully configurable via the <tt>&quot;add_header&quot;</tt> option (see <tt>&quot;Mail::SpamAssassin::Conf&quot;</tt> for more information).</p>
<dl>
<dt>spam mail body text</p>
<dd> The SpamAssassin report is added to top of the mail message body, if the message is marked as spam.</dl>
<h3><font SIZE="-1">DEFAULT TAGGING FOR ALL MAILS</font></h3>
<p> These headers are added to all messages, both spam and ham (non-spam).</p>
<dl>
<dt>X-Spam-Checker-Version: header</p>
<dd> The version and subversion of SpamAssassin and the host where SpamAssassin was run.</p>
<dt>X-Spam-Level: header</p>
<dd> A series of &#8220;*&#8221; charactes where each one represents a full score point.</p>
<dt>X-Spam-Status: header</p>
<dd> A string, <tt>&quot;(Yes|No), score=nn required=nn tests=xxx,xxx autolearn=(ham|spam|no|unavailable|failed)&quot;</tt> is set in this header to reflect the filter status. For the first word, &#8220;Yes&#8221; means spam and &#8220;No&#8221; means ham (non-spam).</dl>
<p> The headers that added are fully configurable via the <tt>&quot;add_header&quot;</tt> option (see <tt>&quot;Mail::SpamAssassin::Conf&quot;</tt> for more information).</p>
<h2>INSTALLATION</h2>
<p> The <code>spamassassin</code> command is part of the <code>Mail::SpamAssassin</code> Perl module. Install this as a normal Perl module, using <tt>&quot;perl -MCPAN -e shell&quot;</tt>, or by hand. </p>
<p> Note that it is not possible to use the <tt>&quot;PERL5LIB&quot;</tt> environment variable to affect where SpamAssassin finds its perl modules, due to limitations imposed by perl&#8217;s &#8220;taint&#8221; security checks. </p>
<p> For further details on how to install, please read the <tt>&quot;INSTALL&quot;</tt> file from the SpamAssassin distribution.</p>
<h2>DEVELOPER DOCUMENTATION</h2>
<pre>
    Mail::SpamAssassin
        Spam detector and markup engine
    Mail::SpamAssassin::ArchiveIterator
        find and process messages one at a time
    Mail::SpamAssassin::AutoWhitelist
        auto-whitelist handler for SpamAssassin
    Mail::SpamAssassin::Bayes
        determine spammishness using a Bayesian classifier
    Mail::SpamAssassin::BayesStore
        Bayesian Storage Module
    Mail::SpamAssassin::BayesStore::SQL
        SQL Bayesian Storage Module Implementation
    Mail::SpamAssassin::Conf::LDAP
        load SpamAssassin scores from LDAP database
    Mail::SpamAssassin::Conf::Parser
        parse SpamAssassin configuration
    Mail::SpamAssassin::Conf::SQL
        load SpamAssassin scores from SQL database
    Mail::SpamAssassin::Message
        decode, render, and hold an RFC-2822 message
    Mail::SpamAssassin::Message::Metadata
        extract metadata from a message
    Mail::SpamAssassin::Message::Node
        decode, render, and make available MIME message parts
    Mail::SpamAssassin::PerMsgLearner
        per-message status (spam or not-spam)
    Mail::SpamAssassin::PerMsgStatus
        per-message status (spam or not-spam)
    Mail::SpamAssassin::PersistentAddrList
        persistent address list base class
    Mail::SpamAssassin::Plugin
        SpamAssassin plugin base class
    Mail::SpamAssassin::Plugin::Hashcash
        perform hashcash verification tests
    Mail::SpamAssassin::Plugin::RelayCountry
        add message metadata indicating the country code of each relay
    Mail::SpamAssassin::Plugin::SPF
        perform SPF verification tests
    Mail::SpamAssassin::Plugin::URIDNSBL
        look up URLs against DNS blocklists
    Mail::SpamAssassin::SQLBasedAddrList
        SpamAssassin SQL Based Auto Whitelist
</pre>
<h2>BUGS</h2>
<p> See &lt;<a rel="nofollow" href="http://issues.apache.org/SpamAssassin/">http://issues.apache.org/SpamAssassin/</a>&gt;</p>
<h2>AUTHORS</h2>
<p> The SpamAssassin(tm) Project &lt;<a rel="nofollow" href="http://spamassassin.apache.org/">http://spamassassin.apache.org/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> SpamAssassin is distributed under the Apache License, Version 2.0, as described in the file <tt>&quot;LICENSE&quot;</tt> included with the distribution. </p>
<h2>Index</h2>
<dt><a href="#lbAI">WEB SITES</a></p>
<dd>
<dt><a href="#lbAJ">USER MAILING LIST</a></p>
<dd>
<dt><a href="#lbAK">CONFIGURATION FILES</a></p>
<dd>
<dt><a href="#lbAL">TAGGING</a></p>
<dd>
<dt><a href="#lbAO">INSTALLATION</a></p>
<dd>
<dt><a href="#lbAP">DEVELOPER DOCUMENTATION</a></p>
<dd>
<dt><a href="#lbAQ">BUGS</a></p>
<dd>
<dt><a href="#lbAR">AUTHORS</a></p>
<dd>
<dt><a href="#lbAS">COPYRIGHT</a></p>
<dd></dl>
