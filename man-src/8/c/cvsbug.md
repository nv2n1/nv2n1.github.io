---
title: "cvsbug(8)"
name: "cvsbug"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cvsbug/"
description: "cvsbug – send problem report (PR) about CVS to a central support site"
---

<p>cvsbug &#8211; send problem report (PR) about CVS to a central support site</p>
<h2>Synopsis</h2>
<p><code>cvsbug</code> [ <i>site</i> ] [ <code>-f</code> <i>problem-report</i> ] [ <code>-t</code> <i>mail-address</i> ]<br />
 [ <code>-P</code> ] [ <code>-L</code> ] [ <code>&#8211;request-id</code> ] [ <code>-v</code> ]</p>
<h2>Description</h2>
<p><code>cvsbug</code> is a tool used to submit <i>problem reports </i> (PRs) to a central support site. In most cases the correct <i>site</i> will be the default. This argument indicates the support site which is responsible for the category of problem involved. Some sites may use a local address as a default. <i>site</i> values are defined by using the <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5). </p>
<p> <code>cvsbug</code> invokes an editor on a problem report template (after trying to fill in some fields with reasonable default values). When you exit the editor, <code>cvsbug </code> sends the completed form to the <i>Problem Report Management System</i> (<code>GNATS</code>) at a central support site. At the support site, the PR is assigned a unique number and is stored in the <code>GNATS</code> database according to its category and submitter-id. <code>GNATS</code> automatically replies with an acknowledgement, citing the category and the PR number. </p>
<p> To ensure that a PR is handled promptly, it should contain your (unique) <i>submitter-id</i> and one of the available <i>categories</i> to identify the problem area. (Use <code>`cvsbug -L&#8217;</code> to see a list of categories.) </p>
<p> The <code>cvsbug</code> template at your site should already be customized with your submitter-id (running `<code>install-sid</code> <i>submitter-id</i>&#8216; to accomplish this is part of the installation procedures for <code>cvsbug</code>). If this hasn&#8217;t been done, see your system administrator for your submitter-id, or request one from your support site by invoking <code>`cvsbug &#8211;request-id&#8217;.</code> If your site does not distinguish between different user sites, or if you are not affiliated with the support site, use <code>`net&#8217;</code> for this field. </p>
<p> The more precise your problem description and the more complete your information, the faster your support team can solve your problems.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code><i> problem-report</i></p>
<dd>specify a file (<i>problem-report</i>) which already contains a complete problem report. <code>cvsbug</code> sends the contents of the file without invoking the editor. If the value for <i>problem-report</i> is <code>`-&#8216;</code>, then <code>cvsbug</code> reads from standard input.</p>
<dt><code>-t</code><i> mail-address</i></p>
<dd>Change mail address at the support site for problem reports. The default <i>mail-address</i> is the address used for the default <i>site</i>. Use the <i>site</i> argument rather than this option in nearly all cases.</p>
<dt><code>-P</code></p>
<dd>print the form specified by the environment variable <code>PR_FORM </code> on standard output. If <code>PR_FORM</code> is not set, print the standard blank PR template. No mail is sent.</p>
<dt><code>-L</code></p>
<dd>print the list of available categories. No mail is sent.</p>
<dt><code>&#8211;request-id</code></p>
<dd>sends mail to the default support site, or <i>site</i> if specified, with a request for your <i>submitter-id</i>. If you are not affiliated with <i>site</i>, use a <i>submitter-id</i> of <code>net</code>&#8216;.</p>
<dt><code>-v</code></p>
<dd>Display the <code>cvsbug</code> version number.</dl>
<p> Note: use <code>cvsbug</code> to submit problem reports rather than mailing them directly. Using both the template and <code>cvsbug</code> itself will help ensure all necessary information will reach the support site.</p>
<h2>Environment</h2>
<p>The environment variable <code>EDITOR</code> specifies the editor to invoke on the template.<br />
 default: <code>vi</code> </p>
<p> If the environment variable <code>PR_FORM</code> is set, then its value is used as the file name of the template for your problem-report editing session. You can use this to start with a partially completed form (for example, a form with the identification fields already completed).</p>
<h2>How To Fill Out A Problem Report</h2>
<p>Problem reports have to be in a particular form so that a program can easily manage them. Please remember the following guidelines:</p>
<dl>
<dt>&bull;</p>
<dd>describe only <code>one problem</code> with each problem report.</p>
<dt>&bull;</p>
<dd>For follow-up mail, use the same subject line as the one in the automatic acknowledgement. It consists of category, PR number and the original synopsis line. This allows the support site to relate several mail messages to a particular PR and to record them automatically.</p>
<dt>&bull;</p>
<dd>Please try to be as accurate as possible in the subject and/or synopsis line.</p>
<dt>&bull;</p>
<dd>The subject and the synopsis line are not confidential. This is because open-bugs lists are compiled from them. Avoid confidential information there.</dl>
<p> See the GNU <code>Info </code> file <code>cvsbug.info</code> or the document <i>Reporting Problems With cvsbug</i>&nbsp;<wbr>for detailed information on reporting problems</p>
<h2>How To Submit Test Cases, Code, Etc.</h2>
<p>Submit small code samples with the PR. Contact the support site for instructions on submitting larger test cases and problematic source code.</p>
<h2>Files</h2>
<p>/tmp/p$$<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>copy of PR used in editing session</p>
<p> /tmp/pf$$<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>copy of empty PR form, for testing purposes</p>
<p> /tmp/pbad$$<tt>&nbsp;<wbr></tt>file for rejected PRs</p>
<h2>Installation And Configuration</h2>
<p>See <code>INSTALL</code> for installation instructions.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/l-gnats/">gnats</a></code>(l), <code><a href="/docs/linux/man/1-query-pr/">query-pr</a></code>(1), <code><a href="/docs/linux/man/1-edit-pr/">edit-pr</a></code>(1), <code><a href="/docs/linux/man/8-gnats/">gnats</a></code>(8), <code><a href="/docs/linux/man/8-queue-pr/">queue-pr</a></code>(8), <code><a href="/docs/linux/man/8-at-pr/">at-pr</a></code>(8), <code><a href="/docs/linux/man/8-mkcat/">mkcat</a></code>(8), <code><a href="/docs/linux/man/8-mkdist/">mkdist</a></code>(8).</p>
<h2>Authors</h2>
<p>Jeffrey Osier, Brendan Kehoe, Jason Merrill, Heinz G. Seidl (Cygnus Support)</p>
<h2>Copying</h2>
<p>Copyright (c) 1992, 1993 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this manual provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual into another language, under the above conditions for modified versions, except that this permission notice may be included in translations approved by the Free Software Foundation instead of in the original English.</p>
