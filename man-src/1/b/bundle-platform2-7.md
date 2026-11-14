---
title: "bundle-platform2-7(1)"
name: "bundle-platform2-7"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bundle-platform2-7/"
description: "bundle-platform – Displays platform compatibility information"
---

<p><code>bundle-platform</code> &#8211; Displays platform compatibility information </p>
<h2>Synopsis</h2>
<p><code>bundle platform</code> [&#8211;ruby]</p>
<h2>Description</h2>
<p><code>platform</code> will display information from your Gemfile, Gemfile.lock, and Ruby VM about your platform. </p>
<p> For instance, using this <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5):</p>
<dl>
<dd>
<pre>source &quot;<a rel="nofollow" href="https://rubygems.org">https://rubygems.org</a>&quot;
ruby &quot;1.9.3&quot;
gem &quot;rack&quot;</pre>
<dd></dl>
<p> If you run <code>bundle platform</code> on Ruby 1.9.3, it will display the following output:</p>
<dl>
<dd>
<pre>Your platform is: x86_64-linux
Your app has gems that work on these platforms:
* ruby
Your Gemfile specifies a Ruby version requirement:
* ruby 1.9.3
Your current platform satisfies the Ruby version requirement.</pre>
<dd></dl>
<p> <code>platform</code> will list all the platforms in your <code>Gemfile.lock</code> as well as the <code>ruby</code> directive if applicable from your <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5). It will also let you know if the <code>ruby</code> directive requirement has been met. If <code>ruby</code> directive doesn&#8217;t match the running Ruby VM, it will tell you what part does not.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;ruby</code></p>
<dd>It will display the ruby directive information, so you don&#8217;t have to parse it from the <a href="/docs/linux/man/5-gemfile/">Gemfile</a>(5). </p>
</dl>
