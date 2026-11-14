---
title: "bundle-pristine2-7(1)"
name: "bundle-pristine2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-pristine2-7/"
description: "bundle-pristine – Restores installed gems to their pristine condition"
---

<p><code>bundle-pristine</code> &#8211; Restores installed gems to their pristine condition </p>
<h2>Synopsis</h2>
<p><code>bundle pristine</code></p>
<h2>Description</h2>
<p><code>pristine</code> restores the installed gems in the bundle to their pristine condition using the local gem cache from RubyGems. For git gems, a forced checkout will be performed. </p>
<p> For further explanation, <code>bundle pristine</code> ignores unpacked files on disk. In other words, this command utilizes the local <code>.gem</code> cache or the gem&#8217;s git repository as if one were installing from scratch. </p>
<p> Note: the Bundler gem cannot be restored to its original state with <code>pristine</code>. One also cannot use <code>bundle pristine</code> on gems with a &#8216;path&#8217; option in the Gemfile, because bundler has no original copy it can restore from. </p>
<p> When is it practical to use <code>bundle pristine</code>? </p>
<p> It comes in handy when a developer is debugging a gem. <code>bundle pristine</code> is a great way to get rid of experimental changes to a gem that one may not want. </p>
<p> Why use <code>bundle pristine</code> over <code>gem pristine &#8211;all</code>? </p>
<p> Both commands are very similar. For context: <code>bundle pristine</code>, without arguments, cleans all gems from the lockfile. Meanwhile, <code>gem pristine &#8211;all</code> cleans all installed gems for that Ruby version. </p>
<p> If a developer forgets which gems in their project they might have been debugging, the Rubygems <code>gem pristine [GEMNAME]</code> command may be inconvenient. One can avoid waiting for <code>gem pristine &#8211;all</code>, and instead run <code>bundle pristine</code>.</p>
