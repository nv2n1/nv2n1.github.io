---
title: "blazetheme(7)"
name: "blazetheme"
section: "7"
letter: "b"
url: "/docs/linux/man/7-blazetheme/"
description: "blazetheme – an introduction to BlazeBlogger theme creation"
---

<p>blazetheme &#8211; an introduction to BlazeBlogger theme creation</p>
<h2>Description</h2>
<p>This document tries to provide a brief introduction on how to create new or modify existing theme for your BlazeBlogger web presentation.</p>
<h2>BlazeBlogger Theme Structure</h2>
<p>To make it as easy to alter as possible, BlazeBlogger theme consists of two parts: the template file located in the <tt>&quot;.blaze/theme/&quot;</tt> and corresponding stylesheet in the <tt>&quot;.blaze/style/&quot;</tt> directory. This way, you can easily switch between different styles (e.g. bright and dark one) without even touching the template file, which generally does not tend to vary much.</p>
<h2>Creating the Template File</h2>
<p>The template file is where the page layout is described. It is a bare <font SIZE="-1">HTML</font> (or <font SIZE="-1">XHTML</font>, it really does not matter) file with various placeholders to be substituted by appropriate data. Most of the placeholders are just ordinary <font SIZE="-1">HTML</font> comments with a reserved strings in them. Note that while the case is not significant, the fact that the whole placeholder has to be on a single line is. </p>
<p> For the example usage, see the default template file. </p>
<p> <i>List of Head Placeholders</i> </p>
<p> These are the placeholders that usually appear in the <font SIZE="-1">HEAD</font> section of the <font SIZE="-1">HTML/XHTML</font> document.</p>
<dl>
<dt><code>&lt;!&#8211; content-type &#8211;&gt;</code></p>
<dd>The Content-Type <font SIZE="-1">META</font> tag.</p>
<dt><code>&lt;!&#8211; generator &#8211;&gt;</code></p>
<dd>The Generator <font SIZE="-1">META</font> tag.</p>
<dt><code>&lt;!&#8211; date &#8211;&gt;</code></p>
<dd>The Date <font SIZE="-1">META</font> tag.</p>
<dt><code>&lt;!&#8211; stylesheet &#8211;&gt;</code></p>
<dd>The Stylesheet <font SIZE="-1">LINK</font> tag.</p>
<dt><code>&lt;!&#8211; rss &#8211;&gt;</code></p>
<dd>The <font SIZE="-1">RSS</font> feed <font SIZE="-1">LINK</font> tag.</p>
<dt><code>&lt;!&#8211; page-title &#8211;&gt;</code></p>
<dd>Current page title, usually used inside <font SIZE="-1">TITLE</font> element.</dl>
<p> <i>List of Body Placeholders</i> </p>
<p> These are the placeholders that usually appear in the <font SIZE="-1">BODY</font> section of the <font SIZE="-1">HTML/XHTML</font> document.</p>
<dl>
<dt><code>&lt;!&#8211; title &#8211;&gt;</code></p>
<dd>The blog title, see <tt>&quot;blog.title&quot;</tt> in the BlazeBlogger configuration.</p>
<dt><code>&lt;!&#8211; subtitle &#8211;&gt;</code></p>
<dd>The blog title, see <tt>&quot;blog.subtitle&quot;</tt> in the BlazeBlogger configuration.</p>
<dt><code>&lt;!&#8211; name &#8211;&gt;</code></p>
<dd>The user&#8217;s name, see <tt>&quot;user.name&quot;</tt> in the BlazeBlogger configuration.</p>
<dt><code>&lt;!&#8211; e-mail &#8211;&gt;</code></p>
<dd>The user&#8217;s e-mail, see <tt>&quot;user.email&quot;</tt> in the BlazeBlogger configuration.</p>
<dt><code>&lt;!&#8211; year &#8211;&gt;</code></p>
<dd>The current year.</p>
<dt><code>&lt;!&#8211; tags &#8211;&gt;</code></p>
<dd>List of tags.</p>
<dt><code>&lt;!&#8211; archive &#8211;&gt;</code></p>
<dd>List of months.</p>
<dt><code>&lt;!&#8211; pages &#8211;&gt;</code></p>
<dd>List of pages.</p>
<dt><code>&lt;!&#8211; posts &#8211;&gt;</code></p>
<dd>List of recent blog posts.</p>
<dt><code>&lt;!&#8211; content &#8211;&gt;</code></p>
<dd>Main content (e.g. post or page body, posts listing etc.).</p>
<dt><code>%root%</code></p>
<dd>Relative path to the root directory of the blog; to be used inside links. Note that this placeholder can safely appear in the post/page body as well and will be still taken into account.</p>
<dt><code>%home%</code></p>
<dd>Relative path to the website home (index) page; to be used inside links. Note that this placeholder can safely appear in the post/page body as well and will be still taken into account.</p>
<dt><code>%page[</code><i>id</i><code>]%</code></p>
<dd>Relative path to the page with given <i>id</i>; to be used inside links. Note that this placeholder can safely appear in the post/page body as well and will be still taken into account.</p>
<dt><code>%post[</code><i>id</i><code>]%</code></p>
<dd>Relative path to the post with given <i>id</i>; to be used inside links. Note that this placeholder can safely appear in the post/page body as well and will be still taken into account.</p>
<dt><code>%tag[</code><i>name</i><code>]%</code></p>
<dd>Relative path to the tag with given <i>name</i>; to be used inside links. Note that this placeholder can safely appear in the post/page body as well and will be still taken into account.</dl>
<h2>Creating the Stylesheet</h2>
<p>The stylesheet is just a plain <font SIZE="-1">CSS</font> file (<font SIZE="-1">CSS</font> 2.1 is recommended, although not required) with most of its parts dependent on elements, classes and IDs introduced in the theme file. Those few that are produced by the <code><a href="/docs/linux/man/1-blaze-make/">blaze-make</a></code>(1) are described below. </p>
<p> For the example usage, see the default stylesheet. </p>
<p> <i>List of Obligatory Classes</i></p>
<dl>
<dt><code>post</code></p>
<dd><tt>&quot;H2&quot;</tt> element containing the page/post title.</p>
<dt><code>section</code></p>
<dd><tt>&quot;DIV&quot;</tt> element containing the name of the current section (e.g. monthly archive, tag listing etc.).</p>
<dt><code>information</code></p>
<dd><tt>&quot;DIV&quot;</tt> element, optionally containing the additional information about the post, such as the date of publishing, the post author, or the list of attached tags. It is placed above the post, right below its heading.</p>
<dt><code>post-footer</code></p>
<dd><tt>&quot;DIV&quot;</tt> element, optionally containing the additional information about the post, such as the date of publishing, the post author, or the list of attached tags. It is placed right below the post itself.</p>
<dt><code>date</code></p>
<dd><tt>&quot;SPAN&quot;</tt> element containing the date of publishing.</p>
<dt><code>author</code></p>
<dd><tt>&quot;SPAN&quot;</tt> element containing the post author.</p>
<dt><code>tags</code></p>
<dd><tt>&quot;SPAN&quot;</tt> element containing the list of attached tags.</p>
<dt><code>previous</code></p>
<dd><tt>&quot;DIV&quot;</tt> element containing link to the page with older posts.</p>
<dt><code>next</code></p>
<dd><tt>&quot;DIV&quot;</tt> element containing link to the page with newer posts.</p>
<dt><code>more</code></p>
<dd><tt>&quot;A&quot;</tt> element containing the `Read more&#8217; link.</dl>
<h2>Files</h2>
<dl>
<dt><i>.blaze/theme/</i></p>
<dd>BlazeBlogger themes directory.</p>
<dt><i>.blaze/style/</i></p>
<dd>BlazeBlogger stylesheets directory.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-blaze-config/">blaze-config</a></code>(1), <code><a href="/docs/linux/man/1-blaze-make/">blaze-make</a></code>(1).</p>
<h2>Author</h2>
<p>Written by Jaromir Hradilek &lt;jhradilek [at] gmail.com&gt; </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<p> A copy of the license is included as a file called <font SIZE="-1">FDL</font> in the main directory of the BlazeBlogger source package.</p>
