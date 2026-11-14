---
title: "git-sh-i18n-envsubst(1)"
name: "git-sh-i18n-envsubst"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-sh-i18n-envsubst/"
description: "git-sh-i18n–envsubst – Git’s own"
---

<p>git-sh-i18n&#8211;envsubst &#8211; Git&#8217;s own </p>
<p> <a href="/docs/linux/man/1-envsubst/">envsubst</a>(1) for i18n fallbacks</p>
<h2>Synopsis</h2>
<pre>eval_gettext () {
 printf &quot;%s&quot; &quot;$1&quot; | (
 export PATH $(<i>git sh-i18n--envsubst</i> --variables &quot;$1&quot;);
 <i>git sh-i18n--envsubst</i> &quot;$1&quot;
 )
}</pre>
<h2>Description</h2>
<p>This is not a command the end user would want to run. Ever. This documentation is meant for people who are studying the plumbing scripts and/or are writing new ones. </p>
<p> <i>git sh-i18n&#8211;envsubst</i> is Git&#8217;s stripped-down copy of the GNU <code><a href="/docs/linux/man/1-envsubst/">envsubst</a>(1)</code> program that comes with the GNU gettext package. It&#8217;s used internally by <code><a href="/docs/linux/man/1-git-sh-i18n/">git-sh-i18n</a></code>(1) to interpolate the variables passed to the <code>eval_gettext</code> function. </p>
<p> No promises are made about the interface, or that this program won&#8217;t disappear without warning in the next version of Git. Don&#8217;t use it.</p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
