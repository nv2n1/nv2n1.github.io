---

title: "dehtmldiff(1)"
name: "dehtmldiff"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dehtmldiff/"
description: "dehtmldiff – get usable diff from an HTML page"
---

<p> dehtmldiff &#8211; get usable diff from an HTML page </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dehtmldiff</code> [<i>file</i>&#8230;]</dt>
<dt> <code>dehtmldiff</code> {[&#8211;help] | [&#8211;version]}</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>dehtmldiff</code></p>
<dd>creates usable diff files from HTML pages. This is useful in the scenario where a patch has been posted to a mailing list viewable via a web page. </dd>
<p> The corrected diff is sent to standard output. Note that you will probably need to use the <code>-l</code> option when applying the patch, in order to ignore any whitespace differences there may be.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Display a short usage message.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Display the version number of dehtmldiff.</dd></dl>
<h2>LIMITATIONS</h2>
<p> The way this command works is fairly primitive; it boils down to some simple text replacements, followed by an <code>unwrapdiff</code> pass. As a result, all of the limitations that apply to <code>unwrapdiff</code> also apply to <code>dehtmldiff</code>.</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
</dt><dd> Package maintainer</dd></dl>
