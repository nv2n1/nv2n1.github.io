---
title: "ireminder(1)"
name: "ireminder"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ireminder/"
description: "ireminder – Prayer time reminder"
---

<h2 class="name">NAME</h2>
<p> ireminder &#8211; Prayer time reminder </p>
<h2>SYNOPSIS</h2>
<p> <code>ireminder</code> [<code>-ipraytime</code> path] [<code>-skip</code> event_name] [<code>-reminder</code> minutes] [<code>-inplace]</code> [<code>-execr</code> cmd] [<code>-execs</code> cmd] [<code>-help]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>ireminder</code> script is written in perl and is meant to be a simplistic wrapper to call and process the &#8216;ipraytime&#8217; application. <code>ireminder</code> is used to remind the user via audio indicators of an impending Islamic prayer event.</p>
<h2>OPTIONS</h2>
<p> Some of the options within <code>ireminder</code> allow for list inputs, those are meant to be a quoted series of text/numbers.</p>
<dl>
<dt><code>-ipraytime </code><i>path</i></p>
<dd> Specify the path to the ipraytime executable. Unless this options is specified, the script will default to look for the binary in /usr/bin, /usr/local/bin and the current directory.</p>
<dt><code>-skip </code><i>event_name</i></p>
<dd> Specify name of prayer/event to skip, valid options include &quot;imsaak fajr shorooq zuhr asr maghrib isha&quot; (list ok).</p>
<dt><code>-reminder </code><i>minutes</i></p>
<dd> Specify prior to how many minutes to remind (list ok).</p>
<dt><code>-inplace</code></p>
<dd> Specify to print output in-place (without scrolling).</p>
<dt><code>-execr </code><i>cmd</i></p>
<dd> Specify an external application trigger for reminders. The %m directive is recognized and is substituted with the normal output message or string. The %s directive is recognized and is substituted by the salat&#8217;s name.</p>
<dt><code>-execs </code><i>cmd</i></p>
<dd> Specify an external application trigger for when the salat reaches its appointed time (ie. &quot;salat now&quot;). The %m directive is recognized and is substituted with the normal output message or string. The %s directive is recognized and is substituted by the salat&#8217;s name.</p>
<dt><code>-help</code></p>
<dd> Produce a help screen.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs on the web using <a rel="nofollow" href="http://bugs.arabeyes.org">http://bugs.arabeyes.org</a></p>
<h2>AUTHOR</h2>
<p> Written by Nadim Shaikli as part of the Arabeyes.org project.</p>
<h2>COPYRIGHT</h2>
<p> <code>iremidner</code> is subject to the GNU General Public License (GPL).<br />
 Copyright &#169; 2006, Arabeyes, Nadim Shaikli.</p>
<h2>SEE ALSO</h2>
<p> The ITL library (libitl) from the Islamic Tools and Libraries project. It is the underlying requirement for <code>ireminder</code> to function. The ITL library was created and is hosted at <code><a rel="nofollow" href="http://www.arabeyes.org">www.arabeyes.org</a></code>. </p>
<h2>Index</h2>
