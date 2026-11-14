---
title: "git-tag(1)"
name: "git-tag"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-tag/"
description: "git-tag – Create, list, delete or verify a tag object signed with GPG"
---

<h2 class="name">NAME</h2>
<p> git-tag &#8211; Create, list, delete or verify a tag object signed with GPG </p>
<h2>SYNOPSIS</h2>
<pre><code>
git tag[-a | -s | -u&lt;keyid&gt;][-f][-m&lt;msg&gt; | -F&lt;file&gt;][-e]&lt;tagname&gt;[&lt;commit&gt; | &lt;object&gt;] git tag - d&lt;tagname&gt;... git tag[-n[&lt;num&gt;]] - l[--contains&lt;commit&gt;][--no - contains&lt;commit&gt;][--points - at&lt;object&gt;][--column[=&lt;options&gt;] | --no - column][--create - reflog][--sort = &lt;key&gt;][--format = &lt;format&gt;][--merged&lt;commit&gt;][--no - merged&lt;commit&gt;][&lt;pattern&gt;...] git tag - v[--format = &lt;format&gt;]&lt;tagname&gt;...
</code></pre>
<h2>DESCRIPTION</h2>
<p> Add a tag reference in <code>refs/tags/</code>, unless <code>-d/-l/-v</code> is given to delete, list or verify tags. </p>
<p> Unless <code>-f</code> is given, the named tag must not yet exist. </p>
<p> If one of <code>-a</code>, <code>-s</code>, or <code>-u &lt;keyid&gt;</code> is passed, the command creates a <i>tag</i> object, and requires a tag message. Unless <code>-m &lt;msg&gt;</code> or <code>-F &lt;file&gt;</code> is given, an editor is started for the user to type in the tag message. </p>
<p> If <code>-m &lt;msg&gt;</code> or <code>-F &lt;file&gt;</code> is given and <code>-a</code>, <code>-s</code>, and <code>-u &lt;keyid&gt;</code> are absent, <code>-a</code> is implied. </p>
<p> Otherwise, a tag reference that points directly at the given object (i.e., a lightweight tag) is created. </p>
<p> A GnuPG signed tag object will be created when <code>-s</code> or <code>-u &lt;keyid&gt;</code> is used. When <code>-u &lt;keyid&gt;</code> is not used, the committer identity for the current user is used to find the GnuPG key for signing. The configuration variable <code>gpg.program</code> is used to specify custom GnuPG binary. </p>
<p> Tag objects (created with <code>-a</code>, <code>-s</code>, or <code>-u</code>) are called &quot;annotated&quot; tags; they contain a creation date, the tagger name and e-mail, a tagging message, and an optional GnuPG signature. Whereas a &quot;lightweight&quot; tag is simply a name for an object (usually a commit object). </p>
<p> Annotated tags are meant for release while lightweight tags are meant for private or temporary object labels. For this reason, some git commands for naming objects (like <code>git describe</code>) will ignore lightweight tags by default.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;annotate</p>
<dl>
<dt>
<dd> Make an unsigned, annotated tag object</dl>
<p> -s, &#8211;sign</p>
<dl>
<dt>
<dd> Make a GPG-signed tag, using the default e-mail address&#8217;s key. The default behavior of tag GPG-signing is controlled by <code>tag.gpgSign</code> configuration variable if it exists, or disabled otherwise. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;no-sign</p>
<dl>
<dt>
<dd> Override <code>tag.gpgSign</code> configuration variable that is set to force each and every tag to be signed.</dl>
<p> -u &lt;keyid&gt;, &#8211;local-user=&lt;keyid&gt;</p>
<dl>
<dt>
<dd> Make a GPG-signed tag, using the given key.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Replace an existing tag with the given name (instead of failing)</dl>
<p> -d, &#8211;delete</p>
<dl>
<dt>
<dd> Delete existing tags with the given names.</dl>
<p> -v, &#8211;verify</p>
<dl>
<dt>
<dd> Verify the GPG signature of the given tag names.</dl>
<p> -n&lt;num&gt;</p>
<dl>
<dt>
<dd> &lt;num&gt; specifies how many lines from the annotation, if any, are printed when using -l. Implies <code>&#8211;list</code>. </p>
<p> The default is not to print any annotation lines. If no number is given to <code>-n</code>, only the first line is printed. If the tag is not annotated, the commit message is displayed instead.</dl>
<p> -l, &#8211;list</p>
<dl>
<dt>
<dd> List tags. With optional <code>&lt;pattern&gt;&#8230;</code>, e.g. <code>git tag &#8211;list &#8216;v-*&#8217;</code>, list only the tags that match the pattern(s). </p>
<p> Running &quot;git tag&quot; without arguments also lists all tags. The pattern is a shell wildcard (i.e., matched using <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3)). Multiple patterns may be given; if any of them matches, the tag is shown. </p>
<p> This option is implicitly supplied if any other list-like option such as <code>&#8211;contains</code> is provided. See the documentation for each of those options for details.</dl>
<p> &#8211;sort=&lt;key&gt;</p>
<dl>
<dt>
<dd> Sort based on the key given. Prefix <code>&#8211;</code> to sort in descending order of the value. You may use the &#8211;sort=&lt;key&gt; option multiple times, in which case the last key becomes the primary key. Also supports &quot;version:refname&quot; or &quot;v:refname&quot; (tag names are treated as versions). The &quot;version:refname&quot; sort order can also be affected by the &quot;versionsort.suffix&quot; configuration variable. The keys supported are the same as those in <code>git for-each-ref</code>. Sort order defaults to the value configured for the <code>tag.sort</code> variable if it exists, or lexicographic order otherwise. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</dl>
<p> &#8211;color[=&lt;when&gt;]</p>
<dl>
<dt>
<dd> Respect any colors specified in the <code>&#8211;format</code> option. The <code>&lt;when&gt;</code> field must be one of <code>always</code>, <code>never</code>, or <code>auto</code> (if <code>&lt;when&gt;</code> is absent, behave as if <code>always</code> was given).</dl>
<p> -i, &#8211;ignore-case</p>
<dl>
<dt>
<dd> Sorting and filtering tags are case insensitive.</dl>
<p> &#8211;column[=&lt;options&gt;], &#8211;no-column</p>
<dl>
<dt>
<dd> Display tag listing in columns. See configuration variable <code>column.tag</code> for option syntax. <code>&#8211;column</code> and <code>&#8211;no-column</code> without options are equivalent to <i>always</i> and <i>never</i> respectively. </p>
<p> This option is only applicable when listing tags without annotation lines.</dl>
<p> &#8211;contains [&lt;commit&gt;]</p>
<dl>
<dt>
<dd> Only list tags which contain the specified commit (HEAD if not specified). Implies <code>&#8211;list</code>.</dl>
<p> &#8211;no-contains [&lt;commit&gt;]</p>
<dl>
<dt>
<dd> Only list tags which don&#8217;t contain the specified commit (HEAD if not specified). Implies <code>&#8211;list</code>.</dl>
<p> &#8211;merged [&lt;commit&gt;]</p>
<dl>
<dt>
<dd> Only list tags whose commits are reachable from the specified commit (<code>HEAD</code> if not specified).</dl>
<p> &#8211;no-merged [&lt;commit&gt;]</p>
<dl>
<dt>
<dd> Only list tags whose commits are not reachable from the specified commit (<code>HEAD</code> if not specified).</dl>
<p> &#8211;points-at &lt;object&gt;</p>
<dl>
<dt>
<dd> Only list tags of the given object (HEAD if not specified). Implies <code>&#8211;list</code>.</dl>
<p> -m &lt;msg&gt;, &#8211;message=&lt;msg&gt;</p>
<dl>
<dt>
<dd> Use the given tag message (instead of prompting). If multiple <code>-m</code> options are given, their values are concatenated as separate paragraphs. Implies <code>-a</code> if none of <code>-a</code>, <code>-s</code>, or <code>-u &lt;keyid&gt;</code> is given.</dl>
<p> -F &lt;file&gt;, &#8211;file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Take the tag message from the given file. Use <i>&#8211;</i> to read the message from the standard input. Implies <code>-a</code> if none of <code>-a</code>, <code>-s</code>, or <code>-u &lt;keyid&gt;</code> is given.</dl>
<p> -e, &#8211;edit</p>
<dl>
<dt>
<dd> The message taken from file with <code>-F</code> and command line with <code>-m</code> are usually used as the tag message unmodified. This option lets you further edit the message taken from these sources.</dl>
<p> &#8211;cleanup=&lt;mode&gt;</p>
<dl>
<dt>
<dd> This option sets how the tag message is cleaned up. The <i>&lt;mode&gt;</i> can be one of <i>verbatim</i>, <i>whitespace</i> and <i>strip</i>. The <i>strip</i> mode is default. The <i>verbatim</i> mode does not change message at all, <i>whitespace</i> removes just leading/trailing whitespace lines and <i>strip</i> removes both whitespace and commentary.</dl>
<p> &#8211;create-reflog</p>
<dl>
<dt>
<dd> Create a reflog for the tag. To globally enable reflogs for tags, see <code>core.logAllRefUpdates</code> in <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). The negated form <code>&#8211;no-create-reflog</code> only overrides an earlier <code>&#8211;create-reflog</code>, but currently does not negate the setting of <code>core.logAllRefUpdates</code>.</dl>
<p> &#8211;format=&lt;format&gt;</p>
<dl>
<dt>
<dd> A string that interpolates <code>%(fieldname)</code> from a tag ref being shown and the object it points at. The format is the same as that of <code><a href="/docs/linux/man/1-git-for-each-ref/">git-for-each-ref</a></code>(1). When unspecified, defaults to <code>%(refname:strip=2)</code>.</dl>
<p> &lt;tagname&gt;</p>
<dl>
<dt>
<dd> The name of the tag to create, delete, or describe. The new tag name must pass all checks defined by <code><a href="/docs/linux/man/1-git-check-ref-format/">git-check-ref-format</a></code>(1). Some of these checks may restrict the characters allowed in a tag name.</dl>
<p> &lt;commit&gt;, &lt;object&gt;</p>
<dl>
<dt>
<dd> The object that the new tag will refer to, usually a commit. Defaults to HEAD.</dl>
<h2>CONFIGURATION</h2>
<p> By default, <i>git tag</i> in sign-with-default mode (-s) will use your committer identity (of the form <code>Your Name &lt;your [at] email.address&gt;</code>) to find a key. If you want to use a different default key, you can specify it in the repository configuration as follows: </p>
<dl>
<dt>
<dd>
<pre>
[user]
    signingKey = &lt;gpg-keyid&gt;
</pre>
</dl>
<p> <code>pager.tag</code> is only respected when listing tags, i.e., when <code>-l</code> is used or implied. The default is to use a pager. See <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</p>
<h2>DISCUSSION</h2>
<h3>On Re-tagging</h3>
<p> What should you do when you tag a wrong commit and you would want to re-tag? </p>
<p> If you never pushed anything out, just re-tag it. Use &quot;-f&quot; to replace the old one. And you&#8217;re done. </p>
<p> But if you have pushed things out (or others could just read your repository directly), then others will have already seen the old tag. In that case you can do one of two things: </p>
<dl>
<dt>
<dd> 1. The sane thing. Just admit you screwed up, and use a different name. Others have already seen one tag-name, and if you keep the same name, you may be in the situation that two people both have &quot;version X&quot;, but they actually have <i>different</i> &quot;X&quot;&#8217;s. So just call it &quot;X.1&quot; and be done with it.</dl>
<dl>
<dt>
<dd> 2. The insane thing. You really want to call the new version &quot;X&quot; too, <i>even though</i> others have already seen the old one. So just use <i>git tag -f</i> again, as if you hadn&#8217;t already published the old one.</dl>
<p> However, Git does <code>not</code> (and it should not) change tags behind users back. So if somebody already got the old tag, doing a <i>git pull</i> on your tree shouldn&#8217;t just make them overwrite the old one. </p>
<p> If somebody got a release tag from you, you cannot just change the tag for them by updating your own one. This is a big security issue, in that people MUST be able to trust their tag-names. If you really want to do the insane thing, you need to just fess up to it, and tell people that you messed up. You can do that by making a very public announcement saying: </p>
<dl>
<dt>
<dd>
<pre>
Ok, I messed up, and I pushed out an earlier version tagged as X. I
then fixed something, and retagged the *fixed* tree as X again.
If you got the wrong tag, and want the new one, please delete
the old one and fetch the new one by doing:
        git tag -d X
        git fetch origin tag X
to get my updated tag.
You can test which tag you have by doing
        git rev-parse X
which should return 0123456789abcdef.. if you have the new version.
Sorry for the inconvenience.
</pre>
</dl>
<p> Does this seem a bit complicated? It <code>should</code> be. There is no way that it would be correct to just &quot;fix&quot; it automatically. People need to know that their tags might have been changed.</p>
<h3>On Automatic following</h3>
<p> If you are following somebody else&#8217;s tree, you are most likely using remote-tracking branches (eg. <code>refs/remotes/origin/master</code>). You usually want the tags from the other end. </p>
<p> On the other hand, if you are fetching because you would want a one-shot merge from somebody else, you typically do not want to get tags from there. This happens more often for people near the toplevel but not limited to them. Mere mortals when pulling from each other do not necessarily want to automatically get private anchor point tags from the other person. </p>
<p> Often, &quot;please pull&quot; messages on the mailing list just provide two pieces of information: a repo URL and a branch name; this is designed to be easily cut&amp;pasted at the end of a <i>git fetch</i> command line: </p>
<dl>
<dt>
<dd>
<pre>
Linus, please pull from
        <a href="git://git..../proj.git">git://git..../proj.git</a> master
to get the following updates...
</pre>
</dl>
<p> becomes: </p>
<dl>
<dt>
<dd>
<pre>
$ git pull <a href="git://git..../proj.git">git://git..../proj.git</a> master
</pre>
</dl>
<p> In such a case, you do not want to automatically follow the other person&#8217;s tags. </p>
<p> One important aspect of Git is its distributed nature, which largely means there is no inherent &quot;upstream&quot; or &quot;downstream&quot; in the system. On the face of it, the above example might seem to indicate that the tag namespace is owned by the upper echelon of people and that tags only flow downwards, but that is not the case. It only shows that the usage pattern determines who are interested in whose tags. </p>
<p> A one-shot pull is a sign that a commit history is now crossing the boundary between one circle of people (e.g. &quot;people who are primarily interested in the networking part of the kernel&quot;) who may have their own set of tags (e.g. &quot;this is the third release candidate from the networking group to be proposed for general consumption with 2.6.21 release&quot;) to another circle of people (e.g. &quot;people who integrate various subsystem improvements&quot;). The latter are usually not interested in the detailed tags used internally in the former group (that is what &quot;internal&quot; means). That is why it is desirable not to follow tags automatically in this case. </p>
<p> It may well be that among networking people, they may want to exchange the tags internal to their group, but in that workflow they are most likely tracking each other&#8217;s progress by having remote-tracking branches. Again, the heuristic to automatically follow such tags is a good thing.</p>
<h3>On Backdating Tags</h3>
<p> If you have imported some changes from another VCS and would like to add tags for major releases of your work, it is useful to be able to specify the date to embed inside of the tag object; such data in the tag object affects, for example, the ordering of tags in the gitweb interface. </p>
<p> To set the date used in future tag objects, set the environment variable GIT_COMMITTER_DATE (see the later discussion of possible values; the most common form is &quot;YYYY-MM-DD HH:MM&quot;). </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
$ GIT_COMMITTER_DATE=&quot;2006-10-02 10:31&quot; git tag -s v1.0.1
</pre>
</dl>
<h2>DATE FORMATS</h2>
<p> The <code>GIT_AUTHOR_DATE</code> and <code>GIT_COMMITTER_DATE</code> environment variables support the following date formats: </p>
<p> Git internal format</p>
<dl>
<dt>
<dd> It is <code>&lt;unix timestamp&gt; &lt;time zone offset&gt;</code>, where <code>&lt;unix timestamp&gt;</code> is the number of seconds since the UNIX epoch. <code>&lt;time zone offset&gt;</code> is a positive or negative offset from UTC. For example CET (which is 1 hour ahead of UTC) is <code>+0100</code>.</dl>
<p> RFC 2822</p>
<dl>
<dt>
<dd> The standard email format as described by RFC 2822, for example <code>Thu, 07 Apr 2005 22:13:13 +0200</code>.</dl>
<p> ISO 8601</p>
<dl>
<dt>
<dd> Time and date specified by the ISO 8601 standard, for example <code>2005-04-07T22:13:13</code>. The parser accepts a space instead of the <code>T</code> character as well. Fractional parts of a second will be ignored, for example <code>2005-04-07T22:13:13.019</code> will be treated as <code>2005-04-07T22:13:13</code>. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 In addition, the date part is accepted in the following formats: <code>YYYY.MM.DD</code>, <code>MM/DD/YYYY</code> and <code>DD.MM.YYYY</code>. </p>
</dl>
</dl>
<h2>NOTES</h2>
<p> When combining multiple <code>&#8211;contains</code> and <code>&#8211;no-contains</code> filters, only references that contain at least one of the <code>&#8211;contains</code> commits and contain none of the <code>&#8211;no-contains</code> commits are shown. </p>
<p> When combining multiple <code>&#8211;merged</code> and <code>&#8211;no-merged</code> filters, only references that are reachable from at least one of the <code>&#8211;merged</code> commits and from none of the <code>&#8211;no-merged</code> commits are shown.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-check-ref-format/">git-check-ref-format</a></code>(1). <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1).</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
