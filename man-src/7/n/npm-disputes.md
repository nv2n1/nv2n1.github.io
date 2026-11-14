---
title: "npm-disputes(7)"
name: "npm-disputes"
section: "7"
letter: "n"
url: "/docs/linux/man/7-npm-disputes/"
description: "npm-disputes – Handling Module Name Disputes"
---

<p><code>npm-disputes</code> &#8211; Handling Module Name Disputes</p>
<h2>Synopsis</h2>
<dl>
<dt>1.</p>
<dd>Get the author email with <code>npm owner ls &lt;pkgname&gt;</code></p>
<dt>2.</p>
<dd>Email the author, CC <i>support [at] npmjs.com</i></p>
<dt>3.</p>
<dd>After a few weeks, if there&#8217;s no resolution, we&#8217;ll sort it out.</p>
<dd></dl>
<p> Don&#8217;t squat on package names. Publish code or move out of the way.</p>
<h2>Description</h2>
<p>There sometimes arise cases where a user publishes a module, and then later, some other user wants to use that name. Here are some common ways that happens (each of these is based on actual events.)</p>
<dl>
<dt>1.</p>
<dd>Joe writes a JavaScript module <code>foo</code>, which is not node-specific. Joe doesn&#8217;t use node at all. Bob wants to use <code>foo</code> in node, so he wraps it in an npm module. Some time later, Joe starts using node, and wants to take over management of his program.</p>
<dt>2.</p>
<dd>Bob writes an npm module <code>foo</code>, and publishes it. Perhaps much later, Joe finds a bug in <code>foo</code>, and fixes it. He sends a pull request to Bob, but Bob doesn&#8217;t have the time to deal with it, because he has a new job and a new baby and is focused on his new erlang project, and kind of not involved with node any more. Joe would like to publish a new <code>foo</code>, but can&#8217;t, because the name is taken.</p>
<dt>3.</p>
<dd>Bob writes a 10-line flow-control library, and calls it <code>foo</code>, and publishes it to the npm registry. Being a simple little thing, it never really has to be updated. Joe works for Foo Inc, the makers of the critically acclaimed and widely-marketed <code>foo</code> JavaScript toolkit framework. They publish it to npm as <code>foojs</code>, but people are routinely confused when <code>npm install foo</code> is some different thing.</p>
<dt>4.</p>
<dd>Bob writes a parser for the widely-known <code>foo</code> file format, because he needs it for work. Then, he gets a new job, and never updates the prototype. Later on, Joe writes a much more complete <code>foo</code> parser, but can&#8217;t publish, because Bob&#8217;s <code>foo</code> is in the way.</p>
<dd></dl>
<p> The validity of Joe&#8217;s claim in each situation can be debated. However, Joe&#8217;s appropriate course of action in each case is the same.</p>
<dl>
<dt>1.</p>
<dd><code>npm owner ls foo</code>. This will tell Joe the email address of the owner (Bob).</p>
<dt>2.</p>
<dd>Joe emails Bob, explaining the situation <code>as respectfully as possible</code>, and what he would like to do with the module name. He adds the npm support staff <i>support [at] npmjs.com</i> to the CC list of the email. Mention in the email that Bob can run <code>npm owner add joe foo</code> to add Joe as an owner of the <code>foo</code> package.</p>
<dt>3.</p>
<dd>After a reasonable amount of time, if Bob has not responded, or if Bob and Joe can&#8217;t come to any sort of resolution, email support <i>support [at] npmjs.com</i> and we&#8217;ll sort it out. (&quot;Reasonable&quot; is usually at least 4 weeks, but extra time is allowed around common holidays.)</p>
<dd></dl>
<h2>Reasoning</h2>
<p>In almost every case so far, the parties involved have been able to reach an amicable resolution without any major intervention. Most people really do want to be reasonable, and are probably not even aware that they&#8217;re in your way. </p>
<p> Module ecosystems are most vibrant and powerful when they are as self-directed as possible. If an admin one day deletes something you had worked on, then that is going to make most people quite upset, regardless of the justification. When humans solve their problems by talking to other humans with respect, everyone has the chance to end up feeling good about the interaction.</p>
<h2>Exceptions</h2>
<p>Some things are not allowed, and will be removed without discussion if they are brought to the attention of the npm registry admins, including but not limited to:</p>
<dl>
<dt>1.</p>
<dd>Malware (that is, a package designed to exploit or harm the machine on which it is installed).</p>
<dt>2.</p>
<dd>Violations of copyright or licenses (for example, cloning an MIT-licensed program, and then removing or changing the copyright and license statement).</p>
<dt>3.</p>
<dd>Illegal content.</p>
<dt>4.</p>
<dd>&quot;Squatting&quot; on a package name that you <i>plan</i> to use, but aren&#8217;t actually using. Sorry, I don&#8217;t care how great the name is, or how perfect a fit it is for the thing that someday might happen. If someone wants to use it today, and you&#8217;re just taking up space with an empty tarball, you&#8217;re going to be evicted.</p>
<dt>5.</p>
<dd>Putting empty packages in the registry. Packages must have SOME functionality. It can be silly, but it can&#8217;t be <i>nothing</i>. (See also: squatting.)</p>
<dt>6.</p>
<dd>Doing weird things with the registry, like using it as your own personal application database or otherwise putting non-packagey things into it.</p>
<dd></dl>
<p> If you see bad behavior like this, please report it right away.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help 7 registry</p>
<dt>&bull;</p>
<dd>npm help owner</p>
<dd>
