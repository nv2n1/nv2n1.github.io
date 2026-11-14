---
title: "blazeintro(7)"
name: "blazeintro"
section: "7"
letter: "b"
url: "/docs/linux/man/7-blazeintro/"
description: "blazeintro – an introduction to BlazeBlogger"
---

<p>blazeintro &#8211; an introduction to BlazeBlogger</p>
<h2>Synopsis</h2>
<pre> $ blaze-init
 $ blaze-add
 $ blaze-make</pre>
<h2>Description</h2>
<p>This document tries to provide a brief introduction on how to create, configure, add new content to, and generate a static content from the BlazeBlogger repository. </p>
<p> Although each command described below is actually an autonomous utility, on most Unix systems, BlazeBlogger should be shipped with a command wrapper, making it possible to use <tt>&quot;blaze-command&quot;</tt> and more usual <tt>&quot;blaze command&quot;</tt> interchangeably. In this text, however, we will strictly use the first form, as it is the most portable variant.</p>
<h2>Creating a New Blog</h2>
<p>To create a new blog, you have to create a repository first. Similarly to Git, BlazeBlogger repository is just a (usually hidden) directory named <tt>&quot;.blaze&quot;</tt>, where all the blog data and configuration are stored and from which the static content, i.e. the <font SIZE="-1">HTML</font> pages, is generated. In most cases, it is placed in the same directory as the generated content. </p>
<p> Assuming you are already in the directory where the blog repository is to be placed, you can create a new one typing: </p>
<pre> $ blaze-init</pre>
<p>If nothing goes wrong, you should get a response similar to this: </p>
<pre> Created a BlazeBlogger repository in .blaze.</pre>
<p>As the message suggests, you can use the same command any time later to return the repository to a consistent state while leaving the rest of your data (e.g. configuration, blog posts and pages) intact. Optionally, you can force the utility to restore the configuration, theme, style and language files to their initial state by adding the following option: </p>
<pre> $ blaze-init --force</pre>
<h2>Configuring the Blog</h2>
<p>Although the defaults try to be reasonable enough and ready for an immediate use, there are few options you might at least want to know about. </p>
<p> The first thing probably to be changed is an external text editor you will be using for writing your posts. Unless this option is set, BlazeBlogger tries to use system wide settings by looking for <font SIZE="-1">EDITOR</font> environment variable, and if neither of these options is supplied, <tt>&quot;vi&quot;</tt> is used as a considerably reasonable option. To change it to, lets say, <tt>&quot;pico&quot;</tt>, type: </p>
<pre> $ blaze-config core.editor pico</pre>
<p>Another things you might want to change are the heading and subheading of your blog, and the default user name; for example: </p>
<pre> $ blaze-config blog.title My Blog
 $ blaze-config blog.subtitle yet another blog
 $ blaze-config user.name Your Name</pre>
<p>Furthermore, if you intend to generate <font SIZE="-1">RSS</font> feed, you have to specify the base <font SIZE="-1">URL:</font> </p>
<pre> $ blaze-config blog.url <a rel="nofollow" href="http://blog.example.com/">http://blog.example.com/</a></pre>
<p>Finally, if you prefer coloured output in your terminal window, you can enable it individually for each utility that supports it: </p>
<pre> $ blaze-config color.list true
 $ blaze-config color.log true</pre>
<p>For the complete list of available options, see <code><a href="/docs/linux/man/1-blaze-config/">blaze-config</a></code>(1) manual page. To see the current setting, simply type the option name without the value: </p>
<pre> $ blaze-config user.name</pre>
<p>You can also edit all options at once opening the configuration file in the external text editor: </p>
<pre> $ blaze-config --edit</pre>
<h2>Managing the Blog Posts</h2>
<p>To add a new blog post to the repository, type: </p>
<pre> $ blaze-add</pre>
<p>This will open the external editor with a pre-formatted header and empty body for you to write. Although the most of the header lines are devoted to the exhaustive explanation of what exactly you should and should not fill in, let&#8217;s take a closer look at the five header options just to make sure everything is perfectly clear:</p>
<dl>
<dt>title</p>
<dd>The title of your post; you do not want to omit that one, do you?</p>
<dt>author</p>
<dd>The post author. The user name specified in the configuration is used by default, but you are free to change it to whatever name you wish.</p>
<dt>date</p>
<dd>Date of the publishing of the post. It has to be in the YYYY-MM-DD form (i.e. 17 July 2009 would look like 2009-07-17 etc.) and it has to be filled. The default option is current date.</p>
<dt>tags</p>
<dd>Comma separated list of categories the post belongs to. The exact number of attached tags is not limited as long as they are all listed on the same line. Since tags are completely optional, you can safely leave this option empty, or fill it any time later.</p>
<dt>url</p>
<dd>The use of term `<font SIZE="-1">URL</font>&#8216; in this context is quite vague and simply means the part of the <font SIZE="-1">URL</font> representing the particular post. As it is derived from the post title, you usually do not have to bother with it at all. There are however two cases when it might prove useful: (1) when your title contains special characters (typically foreign diacritical marks) that BlazeBlogger strips away and you still want your <font SIZE="-1">URL</font> look pretty, or (2) in case you want your <font SIZE="-1">URL</font> different from the title, for example because of the title length. Remember that the <font SIZE="-1">URL</font> should consist of alphanumeric characters, hyphens and underscores only.</dl>
<p> Keeping that in mind, your first post might look somehow like the one below: </p>
<pre> # This and following lines beginning with `#' are the post header.
 # Please take your time and replace these options with desired val-
 # ues. Just remember that the date has to be in an YYYY-MM-DD form,
 # tags are a comma separated list of categories the post (pages ig-
 # nore these) belong to, and the url, if provided, should consist of
 # alphanumeric characters, hyphens and underscores only. Specifying
 # your own url is especially recommended when you use non-ASCII cha-
 # racters in your post title.
 #
 # title: The Hobbit, or There and Back Again
 # author: David
 # date: 2009-07-17
 # tags: childrens literature, fantasy
 # url: the-hobbit
 #
 # The header ends here. The rest is the content of your post.
 &lt;p&gt;&amp;ldquo;In a hole in the ground there lived a hobbit.&amp;rdquo;
 &amp;mdash; these are the words that introduces us to the incredible
 world of nowadays classic Tolkien's novel. But what is so
 fascinating about it that generation after generation keep returning
 to its charms?&lt;/p&gt;
 &lt;!-- break --&gt;
 &lt;p&gt;&lt;em&gt;The Hobbit&lt;/em&gt; is a story about Bilbo Baggins, a hobbit ...</pre>
<p>Note that you can use <tt>&quot;&lt;!-- break --&gt;&quot;</tt> to mark the end of the part to be displayed on index page. You can also use a special placeholder, <tt>&quot;%root%&quot;</tt>, as a relative path to the base <font SIZE="-1">URL</font> (directory where the blog is placed) in your links and images. For example, to link the <font SIZE="-1">RSS</font> feed from your blog post, write: </p>
<pre> &lt;a href=&quot;%root%index.rss&quot;&gt;RSS Feed&lt;/a&gt;</pre>
<p>When you are done, save your changes and close the editor. You should get a confirmation message with the <font SIZE="-1">ID</font> of the new post. </p>
<p> If you prefer to write your posts in advance (e.g. work with concepts), you can also add any number of existing files without opening the text editor like this: </p>
<pre> $ blaze-add file1 file2 file3</pre>
<p>To edit the existing post, e.g. with <font SIZE="-1">ID</font> number 3, type: </p>
<pre> $ blaze-edit 3</pre>
<p>To completely remove the post with <font SIZE="-1">ID</font> 3 from the repository, use the following command: </p>
<pre> $ blaze-remove 3</pre>
<p>Do not forget that the utility has no conscience and remorselessly deletes anything you tell it to, with no way to take it back (unless you have backup, of course). To prevent the accidental loss of potentially valuable data, you might want to consider running it in an interactive mode using the <tt>&quot;--interactive&quot;</tt> (or shorter <tt>&quot;-i&quot;</tt>) option and thus having to confirm every deletion.</p>
<h2>Managing the Pages</h2>
<p>Pages are the right place for all those information that have to be immediately accessible from every page on your website (typically the About, Contact, Downloads or Screenshots sections). They are usually kept in a relatively small number and generally do not tend to vary much. In the default theme, they are being listed in the horizontal menu below the blog title. </p>
<p> Similarly to blog posts, you can manage pages using the same commands with additional <tt>&quot;--page&quot;</tt> (or <tt>&quot;-p&quot;</tt> for short) option. Adding new page would therefore look like this: </p>
<pre> $ blaze-add --page</pre>
<p>Unlike posts, pages do not respect tags, nor do they display their author and the date of publishing. The latter is however still taken in account in the sorting process, making it possible to alter the order of pages in the menu according to your taste. </p>
<p> To edit existing page with <font SIZE="-1">ID</font> 3, use: </p>
<pre> $ blaze-edit --page 3</pre>
<p>Finally, to remove pages with <font SIZE="-1">ID</font> 2, type: </p>
<pre> $ blaze-remove --page 2</pre>
<h2>Browsing the Blog Repository</h2>
<p>To display all blog posts in the repository, e.g. to look up an <font SIZE="-1">ID</font> of the particular post, use following command: </p>
<pre> $ blaze-list</pre>
<p>You can also narrow the results by providing the additional specifications like date, tag or author. For example, to find all posts from 19 December 2008 written by David, type: </p>
<pre> $ blaze-list --author David --year 2008 --month 12 --day 19</pre>
<p>To browse pages instead of blog posts, simply add the <tt>&quot;--pages&quot;</tt> option: </p>
<pre> $ blaze-list --pages</pre>
<h2>Generating the Static Content</h2>
<p>To generate the static content from your repository in the current working directory, with all posts, pages, monthly and yearly archives, tags and <font SIZE="-1">RSS</font> feed included, type: </p>
<pre> $ blaze-make</pre>
<p>or if you wish to see a list of files as they are created: </p>
<pre> $ blaze-make --verbose</pre>
<p>You can now check the appearance of your web presentation in the browser and/or copy the files to the hosting. Note that you can force the full paths creation to make it easier to browse the off-line content: </p>
<pre> $ blaze-make --full-paths</pre>
<p>Furthermore, if the public web directory is located on the same server, you can create the content directly in that location by specifying the destination directory: </p>
<pre> $ blaze-make --destdir ~/public_html</pre>
<p>For the complete list of all command line options, see <code><a href="/docs/linux/man/1-blaze-make/">blaze-make</a></code>(1) manual page.</p>
<h2>Observing the Repository History</h2>
<p>Since every significant change in the repository (i.e. its initialization and recovery, as well as post/page addition, editing and removal) is automatically logged along with the exact time of when it happened, you can view the whole history typing: </p>
<pre> $ blaze-log</pre>
<p>or if you want to save space: </p>
<pre> $ blaze-log --short</pre>
<h2>Changing the Blog Theme</h2>
<p>Changing the theme of your blog is rather straightforward. First, extract the content of the theme package to the directory where the static content is being generated; for example, to install the theme called VectorLover: </p>
<pre> $ tar xfz vectorlover-1.0.tar.gz</pre>
<p>Open the template file, in this case <tt>&quot;vectorlover.html&quot;</tt>, in your favourite text editor and replace the sidebar sections like `About&#8217; or `Links&#8217; with appropriate information. Then place both template file and the corresponding stylesheet to the <tt>&quot;.blaze/theme/&quot;</tt> and <tt>&quot;.blaze/style/&quot;</tt> directories respectively: </p>
<pre> $ mv vectorlover.html .blaze/theme/
 $ mv vectorlover.css .blaze/style/</pre>
<p>Finally, change the configuration to use this theme: </p>
<pre> $ blaze-config blog.theme vectorlover.html
 $ blaze-config blog.style vectorlover.css</pre>
<p>Run <code><a href="/docs/linux/man/1-blaze-make/">blaze-make</a></code>(1) to re-create the static content with the new outfit. </p>
<p> For more information on how to modify existing theme or create a new one from scratch, see <code><a href="/docs/linux/man/7-blazetheme/">blazetheme</a></code>(7) manual page.</p>
<h2>Changing the Blog Localization</h2>
<p>To change the blog language to, let&#8217;s say, Czech, copy the file <tt>&quot;cs_CZ&quot;</tt> to the <tt>&quot;.blaze/lang/&quot;</tt> directory and change the appropriate configuration option: </p>
<pre> $ blaze-config blog.lang cs_CZ</pre>
<p>Next time you invoke <code><a href="/docs/linux/man/1-blaze-make/">blaze-make</a></code>(1), all generated strings should be properly translated.</p>
<h2>Files</h2>
<dl>
<dt><i>.blaze/config</i></p>
<dd>BlazeBlogger configuration file.</p>
<dt><i>.blaze/log</i></p>
<dd>BlazeBlogger repository log file.</p>
<dt><i>.blaze/theme/</i></p>
<dd>BlazeBlogger themes directory.</p>
<dt><i>.blaze/style/</i></p>
<dd>BlazeBlogger stylesheets directory.</p>
<dt><i>.blaze/lang/</i></p>
<dd>BlazeBlogger language files directory.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-blaze-init/">blaze-init</a></code>(1), <code><a href="/docs/linux/man/1-blaze-config/">blaze-config</a></code>(1), <code><a href="/docs/linux/man/1-blaze-add/">blaze-add</a></code>(1), <code><a href="/docs/linux/man/1-blaze-edit/">blaze-edit</a></code>(1), <code><a href="/docs/linux/man/1-blaze-remove/">blaze-remove</a></code>(1), <code><a href="/docs/linux/man/1-blaze-list/">blaze-list</a></code>(1), <code><a href="/docs/linux/man/1-blaze-make/">blaze-make</a></code>(1), <code><a href="/docs/linux/man/1-blaze-log/">blaze-log</a></code>(1).</p>
<h2>Author</h2>
<p>Written by Jaromir Hradilek &lt;jhradilek [at] gmail.com&gt; </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<p> A copy of the license is included as a file called <font SIZE="-1">FDL</font> in the main directory of the BlazeBlogger source package.</p>
