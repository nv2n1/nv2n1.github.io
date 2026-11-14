---
title: "lintianmaintainer(3)"
name: "lintianmaintainer"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianmaintainer/"
description: "Lintian::Maintainer — Lintian checks shared between multiple scripts"
---

<p>Lintian::Maintainer &#8212; Lintian checks shared between multiple scripts </p>
<h2>Synopsis</h2>
<pre> use Lintian::Maintainer qw(check_maintainer);
 my ($maintainer, $field) = ('John Doe', 'uploader');
 check_maintainer ($maintainer, $field);</pre>
<h2>Description</h2>
<p>This module provides functions to do some Lintian checks that need to be done in multiple places. There are certain low-level checks, such as validating a maintainer name and e-mail address or checking spelling, which apply in multiple situations and should be done in multiple checks scripts or in checks scripts and the Lintian front-end. </p>
<p> The functions provided by this module issue tags directly, usually either taking the tag name to issue as an argument or dynamically constructing the tag name based on function parameters. The caller is responsible for ensuring that all tags are declared in the relevant *.desc file with proper descriptions and other metadata. The possible tags issued by each function are described in the documentation for that function.</p>
<h2>Functions</h2>
<dl COMPACT>
<dt>check_maintainer(<font SIZE="-1">MAINTAINER, FIELD</font>)</p>
<dd>Checks the maintainer name and address <font SIZE="-1">MAINTAINER</font> for Policy compliance and other issues. <font SIZE="-1">FIELD</font> is the context in which the maintainer name and address was seen and should be one of <tt>&quot;maintainer&quot;</tt> (the Maintainer field in a control file), <tt>&quot;uploader&quot;</tt> (the Uploaders field in a control file), or <tt>&quot;changed-by&quot;</tt> (the Changed-By field in a changes file). </p>
<p> The following tags may be issued by this function. The string <tt>%s</tt> in the tags below will be replaced with the value of <font SIZE="-1">FIELD.</font></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>%s-address-is-on-localhost</p>
<dd>The e-mail address portion of <font SIZE="-1">MAINTAINER</font> is at <tt>&quot;localhost&quot;</tt> or some other similar domain. </p>
<p> = item <tt>%s</tt>-address-is-root-user </p>
<p> The user (from email or username) of <font SIZE="-1">MAINTAINER</font> is root.</p>
<dt>%s-address-causes-mail-loops-or-bounces</p>
<dd>The e-mail address portion of <font SIZE="-1">MAINTAINER</font> or <font SIZE="-1">UPLOADER</font> refers to the <font SIZE="-1">PTS</font> e-mail addresses <tt>&quot;package [at] packages.debian.org&quot;</tt> or <tt>&quot;package [at] packages.qa.debian.org&quot;</tt>, or, alternatively refers to a mailing list which is known to bounce off-list mails sent by Debian role accounts.</p>
<dt>%s-address-looks-weird</p>
<dd><font SIZE="-1">MAINTAINER</font> may be syntactically correct, but it isn&#8217;t conventionally formatted. Currently this tag is only issued for missing whitespace between the name and the address.</p>
<dt>%s-address-malformed</p>
<dd><font SIZE="-1">MAINTAINER</font> doesn&#8217;t fit the basic syntax of a maintainer name and address as specified in Policy.</p>
<dt>%s-address-missing</p>
<dd><font SIZE="-1">MAINTAINER</font> does not contain an e-mail address in angle brackets (&lt;&gt;).</p>
<dt>%s-name-missing</p>
<dd><font SIZE="-1">MAINTAINER</font> does not contain a full name before the address, or the e-mail address was not in angle brackets.</p>
<dt>wrong-debian-qa-address-set-as-maintainer</p>
<dd><font SIZE="-1">MAINTAINER</font> appears to be the Debian <font SIZE="-1">QA</font> Group, but the e-mail address portion is wrong for orphaned packages. This tag is only issued for a <font SIZE="-1">FIELD</font> of <tt>&quot;maintainer&quot;</tt>.</p>
<dt>wrong-debian-qa-group-name</p>
<dd><font SIZE="-1">MAINTAINER</font> appears to be the Debian <font SIZE="-1">QA</font> Group, but the name portion is not <tt>&quot;Debian QA Group&quot;</tt>. This tag is only issued for a <font SIZE="-1">FIELD</font> of <tt>&quot;maintainer&quot;</tt>.</dl>
</dl>
<dl COMPACT>
<dd>The last two tags are issued here rather than in a location more specific to checks of the Maintainer control field because they take advantage of the parsing done by the rest of the function.</dl>
</dl>
<h2>Author</h2>
<p>Originally written by Russ Allbery &lt;rra [at] debian.org&gt; for Lintian. Based on code from checks scripts by Marc Brockschmidt and Richard Braakman.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
