---
title: "ikiwiki-transition(1)"
name: "ikiwiki-transition"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ikiwiki-transition/"
---

<h2>NAME</h2>

 ikiwiki-transition - transition ikiwiki pages to new syntaxes, etc 

<h2>SYNOPSIS</h2>

 ikiwiki-transition type ... 

<h2>DESCRIPTION</h2>

 ikiwiki-transition aids in converting wiki pages when there's a major change in ikiwiki syntax. It also handles other transitions not involving wiki pages. 

<h2>prefix_directives your.setup</h2>

 The prefix_directives mode converts all pages from the old preprocessor directive syntax, requiring a space, to the new syntax, prefixed by '!'. 

 Preprocessor directives which already use the new syntax will remain unchanged. 

 Note that if a page contains wiki links with spaces, which some older versions of ikiwiki accepted, the prefix_directives transition will treat these as preprocessor directives and convert them. 

<h2>setupformat your.setup</h2>

 The setupformat mode converts a setup file from using a single wrappers block to using cgi_wrapper, git_wrapper, etc. 

 Note that all comments and any unusual stuff like perl code in the setup file will be lost, as it is entirely rewritten by the transition. 

<h2>aggregateinternal your.setup</h2>

 The aggregateinternal mode moves pages aggregated by the aggregate plugin so that the aggregateinternal option can be enabled. 

<h2>moveprefs your.setup</h2>

 Moves values that used to be admin preferences into the setup file. 

 Note that all comments and any unusual stuff like perl code in the setup file will be lost, as it is entirely rewritten by the move. 

<h2>indexdb your.setup|srcdir</h2>

 The indexdb mode handles converting a plain text .ikiwiki/index file to a binary .ikiwiki/indexdb. You do not normally need to run ikiwiki-transition indexdb; ikiwiki will automatically run it as necessary. 

<h2>hashpassword your.setup|srcdir</h2>

 The hashpassword mode forces any plaintext passwords stored in the .ikiwiki/userdb file to be replaced with password hashes. (The Authen::Passphrase perl module is needed to do this.) 

 If this is not done explicitly, a user's plaintext password will be automatically converted to a hash when a user logs in for the first time after upgrade to ikiwiki 2.48. 

<h2>deduplinks your.setup</h2>

 In the past, bugs in ikiwiki have allowed duplicate link information to be stored in its indexdb. This mode removes such duplicate information, which may speed up wikis afflicted by it. Note that rebuilding the wiki will have the same effect. 

<h2>AUTHOR</h2>

 Josh Triplett &lt;josh [at] freedesktop.org&gt;, Joey Hess &lt;joey [at] ikiwiki.info&gt; 

 

 

 

<h2>Index</h2>


