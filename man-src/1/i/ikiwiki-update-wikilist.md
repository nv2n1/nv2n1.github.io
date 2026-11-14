---
title: "ikiwiki-update-wikilist(1)"
name: "ikiwiki-update-wikilist"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ikiwiki-update-wikilist/"
---

<h2>NAME</h2>

 ikiwiki-update-wikilist - add or remove user from /etc/ikiwiki/wikilist 

<h2>SYNOPSIS</h2>

 ikiwiki-update-wikilist [-r] 

<h2>DESCRIPTION</h2>

 ikiwiki-update-wikilist is designed to be made suid root, but is not installed suid by default. If made suid, it allows users to add or remove their names from the /etc/ikiwiki/wikilist file. 

 By default, the user's name will be added. The -r switch causes the user's name to be removed. 

 If your name is in /etc/ikiwiki/wikilist, the <a HREF="/docs/linux/man/8-ikiwiki-mass-rebuild/">ikiwiki-mass-rebuild</a>(8) command will look for a ~/.ikiwiki/wikilist file, and rebuild the wikis listed in that file. 

<h2>OPTIONS</h2>

 None. 

<h2>AUTHOR</h2>

 Joey Hess &lt;joey [at] ikiwiki.info&gt; 

 

 

 

<h2>Index</h2>


