---
title: "ikiwiki-mass-rebuild(8)"
name: "ikiwiki-mass-rebuild"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ikiwiki-mass-rebuild/"
---

ikiwiki-mass-rebuild - rebuild all ikiwiki wikis on a system 

<h2>Synopsis</h2>

ikiwiki-mass-rebuild 

<h2>Description</h2>

ikiwiki-mass-rebuild can be used to force a rebuild of all the wikis on a system. You will need to list the setup files for the wikis it should build in the file /etc/ikiwiki/wikilist, which has the format: user /path/to/ikiwiki.setup It's also possible to let a user list setup files in ~user/.ikiwiki/wikilist in their home directory. To do so, list only the user's name, without a setup file. The format of ~/.ikiwiki/wikilist is the same as /etc/ikiwiki/wikilist. 

<h2>Options</h2>

All options are passed on to ikiwiki.

<h2>Author</h2>

Joey Hess &lt;joey [at] ikiwiki.info&gt;
