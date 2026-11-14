---
title: "make_services(1)"
name: "make_services"
section: "1"
letter: "m"
url: "/docs/linux/man/1-make_services/"
description: "make_services – generate GNUstep services info"
---

<h2>NAME</h2>
<p> make_services &#8211; generate GNUstep services info </p>
<h2>SYNOPSIS</h2>
<p> <code>make_services</code> [<code>&#8211;test</code> <i>filename</i> ] [<code>&#8211;verbose</code>|<code>&#8211;quiet</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>make_services</code> builds a validated cache of service information for use by programs that want to access the GNUstep services facility. Additionally, it builds a list of applications and service bundles found in the standard directories. This cache is usually stored in the file named <i>.GNUstepServices</i> in the user&#8217;s GNUstep directory. Most commonly, <i>make_services</i> is called from within the GNUstep.sh or GNUstep.csh script to update the service information everytime the GNUstep environmet is set up, i.e. in a login script. But of course it is possible to run <i>make_services</i> from the command line whenever you wish, for example after having installed a new application or service. </p>
<p> The <i>Services</i> menu in an application&#8217;s mainmenu is usually updated automatically. However, it may be neccessary to close an open or torn off menu for the changes to appear. Also, the workspace manager may have to be closed and restarted for file association changes to take effect.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;test </code><i>filename</p>
<dd> check that property list filename</i> contains a valid service information.</p>
<dt><code>&#8211;quiet</p>
<dd> suppress warnings (not recommended but useful in login scripts).</p>
<dt>&#8211;verbose</p>
<dd> give verbose output.</p>
<dt>&#8211;help</p>
<dd> show small help screen.</dl>
<p> </code></p>
<h2>EXAMPLES</h2>
<p> Simply rebuild the cache of service information: </p>
<p> <i>make_services</i> </p>
<p> Check whether the file ServiceInfo.plist contains a valid service description: </p>
<p> <i>make_services &#8211;test ServiceInfo.plist</i></p>
<h2>NOTES</h2>
<p> Giving both <i>&#8211;quiet</i> and <i>&#8211;verbose</i> on the command line will result in verbose output, ignoring the <i>&#8211;quiet</i> argument.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-gnustep/">GNUstep</a>(7), <a href="/docs/linux/man/1-gopen/">gopen</a>(1)</p>
<h2>HISTORY</h2>
<p> Work on <code>make_services</code> started November 1998. This manual page was first written October 2003.</p>
<h2>AUTHORS</h2>
<p> make_services was written by Richard Frith-Macdonald &lt;richard [at] brainstorm.co.uk&gt;. This man page was written by Martin Brecher &lt;martin [at] mb-itconsulting.com&gt;. </p>
<h2>Index</h2>
