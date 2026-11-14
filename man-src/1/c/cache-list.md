---
title: "cache-list(1)"
name: "cache-list"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cache-list/"
description: "cache-list – List contents of the A-REX cache."
---

<h2>NAME</h2>
<p> cache-list &#8211; List contents of the A-REX cache. </p>
<h2>SYNOPSIS</h2>
<p> cache-list [-h] [-c config_file] [url1 [url2 [&#8230;]]] </p>
<h2>DESCRIPTION</h2>
<p> <code>-h</code> &#8211; print short help </p>
<p> <code>-c</code> &#8211; configuration file from which to read cache information. The ARC_CONFIG environment variable can be set in place of this option. </p>
<p> <code>cache-list</code> is used to list all files present in each cache or, given a list of URLs as arguments, shows the location of each URL in the cache if present. If no arguments are given, it prints to stdout each cache directory specified in the configuration file then a list of files in each cache directory and the corresponding URLs of their source in the format: </p>
<p> <code>url filename</code> </p>
<p> If arguments are given, each cache is checked for the existence of each URL. If a URL is present in the cache then the URL and filename are printed to stdout in the above format. </p>
<p> This tool can be useful for finding out if a certain URL is stored in the cache, or simply to give a list of all URLs in the cache. </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
<h2>Index</h2>
