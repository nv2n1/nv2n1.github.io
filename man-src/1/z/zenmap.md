---
title: "zenmap(1)"
name: "zenmap"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zenmap/"
description: "zenmap – Graphical Nmap frontend and results viewer"
---

<h2 class="name">NAME</h2>
<p> zenmap &#8211; Graphical Nmap frontend and results viewer </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zenmap</code> [<i>options</i>] [<i>results file</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>Zenmap is a multi-platform graphical Nmap frontend and results viewer. Zenmap aims to make Nmap easy for beginners to use while giving experienced Nmap users advanced features. Frequently used scans can be saved as profiles to make them easy to run repeatedly. A command creator allows interactive creation of Nmap command lines. Scan results can be saved and viewed later. Saved scan results can be compared with one another to see how they differ. The results of recent scans are stored in a searchable database. </p>
<p> This man page only describes the few Zenmap command-line options and some critical notes. A much more detailed Zenmap User&#8217;s Guide is available at m[blue]<code><a rel="nofollow" href="http://nmap.org/book/zenmap.html">http://nmap.org/book/zenmap.html</a></code>m[]. Other documentation and information is available from the Zenmap web page at m[blue]<code><a rel="nofollow" href="http://nmap.org/zenmap/">http://nmap.org/zenmap/</a></code>m[].</p>
<h2>OPTIONS SUMMARY</h2>
<p> <code>-f</code>, <code>&#8211;file </code><i>results file</i></p>
<dl>
<dt>
<dd> Open the given results file for viewing. The results file may be an Nmap XML output file (.xml, as produced by <code>nmap -oX</code>) or a Umit scan results file (.usr). This option may be given more than once.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show a help message and exit.</dl>
<p> <code>-n</code>, <code>&#8211;nmap </code><i>Nmap command line</i></p>
<dl>
<dt>
<dd> Run the given Nmap command within the Zenmap interface. After <code>-n</code> or <code>&#8211;nmap</code>, every remaining command line argument is read as the command line to execute. This means that <code>-n</code> or <code>&#8211;nmap</code> must be given last, after any other options. Note that the command line must include the <code>nmap</code> executable name: <code>zenmap -n nmap -sS target</code>.</dl>
<p> <code>-p</code>, <code>&#8211;profile </code><i>profile</i></p>
<dl>
<dt>
<dd> Start with the given profile selected. The profile name is just a string: &quot;Regular scan&quot;. If combined with <code>-t</code>, begin a scan with the given profile against the specified target.</dl>
<p> <code>-t</code>, <code>&#8211;target </code><i>target</i></p>
<dl>
<dt>
<dd> Start with the given target. If combined with <code>-p</code>, begin a scan with the given profile against the specified target.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Increase verbosity (of Zenmap, not Nmap). This option may be given multiple times to get even more verbosity.</dl>
<p> Any other arguments are taken to be the names of results files to open.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>ZENMAP_DEVELOPMENT</code></p>
<dl>
<dt>
<dd> Set <code>ZENMAP_DEVELOPMENT</code> to disable automatic crash reporting.</dl>
<h2>BUGS</h2>
<p> Like their authors, Nmap and Zenmap aren&#8217;t perfect. But you can help make them better by sending bug reports or even writing patches. If Nmap or Zenmap doesn&#8217;t behave the way you expect, first upgrade to the latest version available from m[blue]<code><a rel="nofollow" href="http://nmap.org">http://nmap.org</a></code>m[]. If the problem persists, do some research to determine whether it has already been discovered and addressed. Try Googling the error message or browsing the nmap-dev archives at m[blue]<code><a rel="nofollow" href="http://seclists.org/">http://seclists.org/</a></code>m[]. Read this full manual page as well. If nothing comes of this, mail a bug report to &lt;dev [at] nmap.org&gt;. Please include everything you have learned about the problem, as well as what version of Zenmap you are running and what operating system version it is running on. Problem reports and Zenmap usage questions sent to dev [at] nmap.org are far more likely to be answered than those sent to Fyodor directly. </p>
<p> Code patches to fix bugs are even better than bug reports. Basic instructions for creating patch files with your changes are available at m[blue]<code><a rel="nofollow" href="https://svn.nmap.org/nmap/HACKING">https://svn.nmap.org/nmap/HACKING</a></code>m[]. Patches may be sent to nmap-dev (recommended) or to Fyodor directly.</p>
<h2>HISTORY</h2>
<p> Zenmap was originally derived from Umit, an Nmap GUI created during the Google-sponsored Nmap Summer of Code in 2005 and 2006. The primary author of Umit was Adriano Monteiro Marques. When Umit was modified and integrated into Nmap in 2007, it was renamed Zenmap.</p>
<h2>AUTHORS</h2>
<h3>Nmap</h3>
<p> Fyodor &lt;fyodor [at] nmap.org&gt; (m[blue]<code><a rel="nofollow" href="http://insecure.org">http://insecure.org</a></code>m[]) </p>
<p> Hundreds of people have made valuable contributions to Nmap over the years. These are detailed in the CHANGELOG file which is distributed with Nmap and also available from m[blue]<code><a rel="nofollow" href="http://nmap.org/changelog.html">http://nmap.org/changelog.html</a></code>m[].</p>
<h3>Umit</h3>
<p> Zenmap is derived from the Umit Nmap frontend, which was started by Adriano Monteiro Marques as an Nmap/Google Summer of Code project (&lt;py.adriano [at] gmail.com&gt;, m[blue]<code><a rel="nofollow" href="http://www.umitproject.org">http://www.umitproject.org</a></code>m[]). </p>
<h2>Index</h2>
