---
title: "lg_intro(1)"
name: "lg_intro"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lg_intro/"
description: "lg_intro – introduction to the looking glass"
---

<h2>NAME</h2>
<p> lg_intro &#8211; introduction to the looking glass</p>
<h2>INTRODUCTION</h2>
<p> The <code>looking glass</code> offers a web based interface to routers to users without their needing permission to login to the router. This may be a perfect interface for customer support or less savvy folks, and many ISPs have given public access to such an interface as a &quot;route server.&quot;</p>
<h2>DESCRIPTION</h2>
<p> The looking glass consists of two CGI <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) scripts, <i>lg.cgi</i> and <i>lgform.cgi</i>, and the <code><a href="/docs/linux/man/5-lg-conf/">lg.conf</a></code>(5) configuration file. </p>
<p> Both of these scripts begin with reading the configuration file. If there is an error in the file&#8217;s syntax or if the file can not be found, error messages will be displayed on standard-error. The Apache http server redirects standard-error to its error log file by default. </p>
<p> lgform.cgi displays a html form consisting of a list of possible router commands that can be run and a scrolling list of routers that these commands may be run on. When the form is submitted, lg.cgi is run. </p>
<p> lg.cgi begins by performing some basic checks on the arguments passed to it. If these checks pass, lg.cgi either displays cached data from a previous invocation, if that data exists and is within the cache interval, or uses <code><a href="/docs/linux/man/1-clogin/">clogin</a></code>(1) to login to the device and execute the command. The results of the command are cached if applicable and displayed for the user.</p>
<h2>GETTING STARTED</h2>
<p> Besides <code><a href="/docs/linux/man/5-lg-conf/">lg.conf</a></code>(5), additional instructions for setting up the looking glass can be found in the README file under <i>/usr/share/rancid/README.lg</i>. </p>
<p> Note that the looking glass scripts require a few perl modules not included with rancid. Rancid&#8217;s configure process does not check for these. See the README file.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-cloginrc/">cloginrc</a></code>(5), <code><a href="/docs/linux/man/1-clogin/">clogin</a></code>(1), <code><a href="/docs/linux/man/5-lg-conf/">lg.conf</a></code>(5)</p>
<h2>HISTORY</h2>
<p> Rancid&#8217;s looking glass is based on Ed Kern&#8217;s (included by permission, thanks Ed!), which could once be found on <a rel="nofollow" href="http://nitrous.digex.net/">http://nitrous.digex.net/</a> but has apparently been removed. Support for Juniper and Foundry devices, use of rancid&#8217;s device login scripts, and additional commands and checks have been added to the original. </p>
<h2>Index</h2>
