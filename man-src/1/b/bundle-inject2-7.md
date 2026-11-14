---
title: "bundle-inject2-7(1)"
name: "bundle-inject2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-inject2-7/"
description: "bundle-inject – Add named gem(s) with version requirements to Gemfile"
---

<p><code>bundle-inject</code> &#8211; Add named gem(s) with version requirements to Gemfile </p>
<h2>Synopsis</h2>
<p><code>bundle inject</code> [GEM] [VERSION]</p>
<h2>Description</h2>
<p>Adds the named gem(s) with their version requirements to the resolved [<code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code>][<a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)]. </p>
<p> This command will add the gem to both your [<code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code>][<a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)] and Gemfile.lock if it isn&#8217;t listed yet. </p>
<p> Example:</p>
<dl>
<dd>
<pre>bundle install
bundle inject 'rack' '&gt; 0'</pre>
<dd></dl>
<p> This will inject the &#8216;rack&#8217; gem with a version greater than 0 in your [<code><a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)</code>][<a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5)] and Gemfile.lock</p>
