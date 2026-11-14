---
title: "npm-init(3)"
name: "npm-init"
section: "3"
letter: "n"
url: "/docs/linux/man/3-npm-init/"
description: "init — Interactively create a package.json file"
---

<p><code>init</code> &#8212; Interactively create a package.json file</p>
<h2>Synopsis</h2>
<pre>npm.commands.init(args, callback)</pre>
<h2>Description</h2>
<p>This will ask you a bunch of questions, and then write a package.json for you. </p>
<p> It attempts to make reasonable guesses about what you want things to be set to, and then writes a package.json file with the options you&#8217;ve selected. </p>
<p> If you already have a package.json file, it&#8217;ll read that first, and default to the options in there. </p>
<p> It is strictly additive, so it does not delete options from your package.json without a really good reason to do so. </p>
<p> Since this function expects to be run on the command-line, it doesn&#8217;t work very well as a programmatically. The best option is to roll your own, and since JavaScript makes it stupid simple to output formatted JSON, that is the preferred method. If you&#8217;re sure you want to handle command-line prompting, then go ahead and use this programmatically.</p>
<h2>See Also</h2>
<p>npm help package.json </p>
