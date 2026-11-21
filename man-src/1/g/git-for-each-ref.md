---

title: "git-for-each-ref(1)"
name: "git-for-each-ref"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-for-each-ref/"
description: "git-for-each-ref – Output information on each ref"
---

<pre><code>
 git for-each-ref  [--count=&lt;count&gt;] [--shell|--perl|--python|--tcl]
                   [(--sort=&lt;key&gt;)...] [--format=&lt;format&gt;] [&lt;pattern&gt;...]
                   [--points-at=&lt;object&gt;]
                   [--merged[=&lt;object&gt;]] [--no-merged[=&lt;object&gt;]]
                   [--contains[=&lt;object&gt;]] [--no-contains[=&lt;object&gt;]]
</code></pre>
<p> Iterate over all refs that match <code>&lt;pattern&gt;</code> and show them according to the given <code>&lt;format&gt;</code>, after sorting them according to the given set of <code>&lt;key&gt;</code>. If <code>&lt;count&gt;</code> is given, stop after showing that many refs. The interpolated values in <code>&lt;format&gt;</code> can optionally be quoted as string literals in the specified host language allowing their direct evaluation in that language.  </p>
<h2>OPTIONS</h2>
<p> &lt;pattern&gt;... </p>
<dl>
<dd> <p> If one or more patterns are given, only refs are shown that match against at least one pattern, either using <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3) or literally, in the latter case matching completely or from the beginning up to a slash. </p>
 </dd></dl>
<p> --count=&lt;count&gt; </p>
<dl>
<dd> <p> By default the command shows all refs that match <code>&lt;pattern&gt;</code>. This option makes it stop after showing that many refs. </p>
 </dd></dl>
<p> --sort=&lt;key&gt; </p>
<dl>
<dd> <p> A field name to sort on. Prefix <code>-</code> to sort in descending order of the value. When unspecified, <code>refname</code> is used. You may use the --sort=&lt;key&gt; option multiple times, in which case the last key becomes the primary key. </p>
 </dd></dl>
<p> --format=&lt;format&gt; </p>
<dl>
<dd> <p> A string that interpolates <code>%(fieldname)</code> from a ref being shown and the object it points at. If <code>fieldname</code> is prefixed with an asterisk (<code>*</code>) and the ref points at a tag object, use the value for the field in the object which the tag object refers to (instead of the field in the tag object). When unspecified, <code>&lt;format&gt;</code> defaults to <code>%(objectname) SPC %(objecttype) TAB %(refname)</code>. It also interpolates <code>%%</code> to <code>%</code>, and <code>%xx</code> where <code>xx</code> are hex digits interpolates to character with hex code <code>xx</code>; for example <code>%00</code> interpolates to <code>\0</code> (NUL), <code>%09</code> to <code>\t</code> (TAB) and <code>%0a</code> to <code>\n</code> (LF). </p>
 </dd></dl>
<p> --color[=&lt;when&gt;] </p>
<dl>
<dd> <p> Respect any colors specified in the <code>--format</code> option. The <code>&lt;when&gt;</code> field must be one of <code>always</code>, <code>never</code>, or <code>auto</code> (if <code>&lt;when&gt;</code> is absent, behave as if <code>always</code> was given). </p>
 </dd></dl>
<p> --shell, --perl, --python, --tcl </p>
<dl>
<dd> <p> If given, strings that substitute <code>%(fieldname)</code> placeholders are quoted as string literals suitable for the specified host language. This is meant to produce a scriptlet that can directly be `eval`ed. </p>
 </dd></dl>
<p> --points-at=&lt;object&gt; </p>
<dl>
<dd> <p> Only list refs which points at the given object. </p>
 </dd></dl>
<p> --merged[=&lt;object&gt;] </p>
<dl>
<dd> <p> Only list refs whose tips are reachable from the specified commit (HEAD if not specified). </p>
 </dd></dl>
<p> --no-merged[=&lt;object&gt;] </p>
<dl>
<dd> <p> Only list refs whose tips are not reachable from the specified commit (HEAD if not specified). </p>
 </dd></dl>
<p> --contains[=&lt;object&gt;] </p>
<dl>
<dd> <p> Only list refs which contain the specified commit (HEAD if not specified). </p>
 </dd></dl>
<p> --no-contains[=&lt;object&gt;] </p>
<dl>
<dd> <p> Only list refs which don&#8217;t contain the specified commit (HEAD if not specified). </p>
 </dd></dl>
<p> --ignore-case </p>
<dl>
<dd> <p> Sorting and filtering refs are case insensitive. </p>
 </dd></dl>
<h2>FIELD NAMES</h2>
<p> Various values from structured fields in referenced objects can be used to interpolate into the resulting output, or as sort keys. </p>
<p> For all objects, the following names can be used: </p>
<p> refname </p>
<dl>
<dd> <p> The name of the ref (the part after $GIT_DIR/). For a non-ambiguous short name of the ref append <code>:short</code>. The option core.warnAmbiguousRefs is used to select the strict abbreviation mode. If <code>lstrip=&lt;N&gt;</code> (<code>rstrip=&lt;N&gt;</code>) is appended, strips <code>&lt;N&gt;</code> slash-separated path components from the front (back) of the refname (e.g. <code>%(refname:lstrip=2)</code> turns <code>refs/tags/foo</code> into <code>foo</code> and <code>%(refname:rstrip=2)</code> turns <code>refs/tags/foo</code> into <code>refs</code>). If <code>&lt;N&gt;</code> is a negative number, strip as many path components as necessary from the specified end to leave <code>-&lt;N&gt;</code> path components (e.g. <code>%(refname:lstrip=-2)</code> turns <code>refs/tags/foo</code> into <code>tags/foo</code> and <code>%(refname:rstrip=-1)</code> turns <code>refs/tags/foo</code> into <code>refs</code>). When the ref does not have enough components, the result becomes an empty string if stripping with positive &lt;N&gt;, or it becomes the full refname if stripping with negative &lt;N&gt;. Neither is an error. </p>
<p> <code>strip</code> can be used as a synonym to <code>lstrip</code>. </p>
 </dd></dl>
<p> objecttype </p>
<dl>
<dd> <p> The type of the object (<code>blob</code>, <code>tree</code>, <code>commit</code>, <code>tag</code>). </p>
 </dd></dl>
<p> objectsize </p>
<dl>
<dd> <p> The size of the object (the same as <i>git cat-file -s</i> reports). Append <code>:disk</code> to get the size, in bytes, that the object takes up on disk. See the note about on-disk sizes in the <code>CAVEATS</code> section below. </p>
 </dd></dl>
<p> objectname </p>
<dl>
<dd> <p> The object name (aka SHA-1). For a non-ambiguous abbreviation of the object name append <code>:short</code>. For an abbreviation of the object name with desired length append <code>:short=&lt;length&gt;</code>, where the minimum length is MINIMUM_ABBREV. The length may be exceeded to ensure unique object names. </p>
 </dd></dl>
<p> deltabase </p>
<dl>
<dd> <p> This expands to the object name of the delta base for the given object, if it is stored as a delta. Otherwise it expands to the null object name (all zeroes). </p>
 </dd></dl>
<p> upstream </p>
<dl>
<dd> <p> The name of a local ref which can be considered "upstream" from the displayed ref. Respects <code>:short</code>, <code>:lstrip</code> and <code>:rstrip</code> in the same way as <code>refname</code> above. Additionally respects <code>:track</code> to show &quot;[ahead N, behind M]&quot; and <code>:trackshort</code> to show the terse version: &quot;&gt;&quot; (ahead), &quot;&lt;&quot; (behind), &quot;&lt;&gt;&quot; (ahead and behind), or &quot;=&quot; (in sync). <code>:track</code> also prints &quot;[gone]&quot; whenever unknown upstream ref is encountered. Append <code>:track,nobracket</code> to show tracking information without brackets (i.e &quot;ahead N, behind M&quot;). </p>
<p> For any remote-tracking branch <code>%(upstream)</code>, <code>%(upstream:remotename)</code> and <code>%(upstream:remoteref)</code> refer to the name of the remote and the name of the tracked remote ref, respectively. In other words, the remote-tracking branch can be updated explicitly and individually by using the refspec <code>%(upstream:remoteref):%(upstream)</code> to fetch from <code>%(upstream:remotename)</code>. </p>
<p> Has no effect if the ref does not have tracking information associated with it. All the options apart from <code>nobracket</code> are mutually exclusive, but if used together the last option is selected. </p>
 </dd></dl>
<p> push </p>
<dl>
<dd> <p> The name of a local ref which represents the <code>@{push}</code> location for the displayed ref. Respects <code>:short</code>, <code>:lstrip</code>, <code>:rstrip</code>, <code>:track</code>, <code>:trackshort</code>, <code>:remotename</code>, and <code>:remoteref</code> options as <code>upstream</code> does. Produces an empty string if no <code>@{push}</code> ref is configured. </p>
 </dd></dl>
<p> HEAD </p>
<dl>
<dd> <p> <i>*</i> if HEAD matches current ref (the checked out branch), &#8216; &#8216; otherwise. </p>
 </dd></dl>
<p> color </p>
<dl>
<dd> <p> Change output color. Followed by <code>:&lt;colorname&gt;</code>, where color names are described under Values in the &quot;CONFIGURATION FILE&quot; section of <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). For example, <code>%(color:bold red)</code>. </p>
 </dd></dl>
<p> align </p>
<dl>
<dd> <p> Left-, middle-, or right-align the content between %(align:...) and %(end). The &quot;align:&quot; is followed by <code>width=&lt;width&gt;</code> and <code>position=&lt;position&gt;</code> in any order separated by a comma, where the <code>&lt;position&gt;</code> is either left, right or middle, default being left and <code>&lt;width&gt;</code> is the total length of the content with alignment. For brevity, the &quot;width=&quot; and/or &quot;position=&quot; prefixes may be omitted, and bare &lt;width&gt; and &lt;position&gt; used instead. For instance, <code>%(align:&lt;width&gt;,&lt;position&gt;)</code>. If the contents length is more than the width then no alignment is performed. If used with <code>--quote</code> everything in between %(align:...) and %(end) is quoted, but if nested then only the topmost level performs quoting. </p>
 </dd></dl>
<p> if </p>
<dl>
<dd> <p> Used as %(if)...%(then)...%(end) or %(if)...%(then)...%(else)...%(end). If there is an atom with value or string literal after the %(if) then everything after the %(then) is printed, else if the %(else) atom is used, then everything after %(else) is printed. We ignore space when evaluating the string before %(then), this is useful when we use the %(HEAD) atom which prints either &quot;*&quot; or &quot; &quot; and we want to apply the <i>if</i> condition only on the <i>HEAD</i> ref. Append &quot;:equals=&lt;string&gt;&quot; or &quot;:notequals=&lt;string&gt;&quot; to compare the value between the %(if:...) and %(then) atoms with the given string. </p>
 </dd></dl>
<p> symref </p>
<dl>
<dd> <p> The ref which the given symbolic ref refers to. If not a symbolic ref, nothing is printed. Respects the <code>:short</code>, <code>:lstrip</code> and <code>:rstrip</code> options in the same way as <code>refname</code> above. </p>
 </dd></dl>
<p> worktreepath </p>
<dl>
<dd> <p> The absolute path to the worktree in which the ref is checked out, if it is checked out in any linked worktree. Empty string otherwise. </p>
 </dd></dl>
<p> In addition to the above, for commit and tag objects, the header field names (<code>tree</code>, <code>parent</code>, <code>object</code>, <code>type</code>, and <code>tag</code>) can be used to specify the value in the header field. Fields <code>tree</code> and <code>parent</code> can also be used with modifier <code>:short</code> and <code>:short=&lt;length&gt;</code> just like <code>objectname</code>. </p>
<p> For commit and tag objects, the special <code>creatordate</code> and <code>creator</code> fields will correspond to the appropriate date or name-email-date tuple from the <code>committer</code> or <code>tagger</code> fields depending on the object type. These are intended for working on a mix of annotated and lightweight tags. </p>
<p> Fields that have name-email-date tuple as its value (<code>author</code>, <code>committer</code>, and <code>tagger</code>) can be suffixed with <code>name</code>, <code>email</code>, and <code>date</code> to extract the named component. For email fields (<code>authoremail</code>, <code>committeremail</code> and <code>taggeremail</code>), <code>:trim</code> can be appended to get the email without angle brackets, and <code>:localpart</code> to get the part before the <code>@</code> symbol out of the trimmed email. </p>
<p> The raw data in an object is <code>raw</code>. </p>
<p> raw:size </p>
<dl>
<dd> <p> The raw data size of the object. </p>
 </dd></dl>
<p> Note that <code>--format=%(raw)</code> can not be used with <code>--python</code>, <code>--shell</code>, <code>--tcl</code>, because such language may not support arbitrary binary data in their string variable type. </p>
<p> The message in a commit or a tag object is <code>contents</code>, from which <code>contents:&lt;part&gt;</code> can be used to extract various parts out of: </p>
<p> contents:size </p>
<dl>
<dd> <p> The size in bytes of the commit or tag message. </p>
 </dd></dl>
<p> contents:subject </p>
<dl>
<dd> <p> The first paragraph of the message, which typically is a single line, is taken as the &quot;subject&quot; of the commit or the tag message. Instead of <code>contents:subject</code>, field <code>subject</code> can also be used to obtain same results. <code>:sanitize</code> can be appended to <code>subject</code> for subject line suitable for filename. </p>
 </dd></dl>
<p> contents:body </p>
<dl>
<dd> <p> The remainder of the commit or the tag message that follows the &quot;subject&quot;. </p>
 </dd></dl>
<p> contents:signature </p>
<dl>
<dd> <p> The optional GPG signature of the tag. </p>
 </dd></dl>
<p> contents:lines=N </p>
<dl>
<dd> <p> The first <code>N</code> lines of the message. </p>
 </dd></dl>
<p> Additionally, the trailers as interpreted by <code><a href="/docs/linux/man/1-git-interpret-trailers/">git-interpret-trailers</a></code>(1) are obtained as <code>trailers[:options]</code> (or by using the historical alias <code>contents:trailers[:options]</code>). For valid [:option] values see <code>trailers</code> section of <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1). </p>
<p> For sorting purposes, fields with numeric values sort in numeric order (<code>objectsize</code>, <code>authordate</code>, <code>committerdate</code>, <code>creatordate</code>, <code>taggerdate</code>). All other fields are used to sort in their byte-value order. </p>
<p> There is also an option to sort by versions, this can be done by using the fieldname <code>version:refname</code> or its alias <code>v:refname</code>. </p>
<p> In any case, a field name that refers to a field inapplicable to the object referred by the ref does not cause an error. It returns an empty string instead. </p>
<p> As a special case for the date-type fields, you may specify a format for the date by adding <code>:</code> followed by date format name (see the values the <code>--date</code> option to <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1) takes). </p>
<p> Some atoms like %(align) and %(if) always require a matching %(end). We call them &quot;opening atoms&quot; and sometimes denote them as %($open). </p>
<p> When a scripting language specific quoting is in effect, everything between a top-level opening atom and its matching %(end) is evaluated according to the semantics of the opening atom and only its result from the top-level is quoted.  </p>
<h2>EXAMPLES</h2>
<p> An example directly producing formatted text. Show the most recent 3 tagged commits: </p>
<dl>
<dd> <pre><code>#!/bin/sh
git for-each-ref --count=3 --sort='-*authordate' \
--format='From: %(*authorname) %(*authoremail)
Subject: %(*subject)
Date: %(*authordate)
Ref: %(*refname)
%(*body)
' 'refs/tags'
</code></pre>
 </dd></dl>
<p> A simple example showing the use of shell eval on the output, demonstrating the use of --shell. List the prefixes of all heads: </p>
<dl>
<dd> <pre><code>#!/bin/sh
git for-each-ref --shell --format=&quot;ref=%(refname)&quot; refs/heads | \
while read entry
do
        eval &quot;$entry&quot;
        echo `dirname $ref`
done
</code></pre>
 </dd></dl>
<p> A bit more elaborate report on tags, demonstrating that the format may be an entire script: </p>
<dl>
<dd> <pre><code>#!/bin/sh
fmt='
        r=%(refname)
        t=%(*objecttype)
        T=${r#refs/tags/}
        o=%(*objectname)
        n=%(*authorname)
        e=%(*authoremail)
        s=%(*subject)
        d=%(*authordate)
        b=%(*body)
        kind=Tag
        if test &quot;z$t&quot; = z
        then
                # could be a lightweight tag
                t=%(objecttype)
                kind=&quot;Lightweight tag&quot;
                o=%(objectname)
                n=%(authorname)
                e=%(authoremail)
                s=%(subject)
                d=%(authordate)
                b=%(body)
        fi
        echo &quot;$kind $T points at a $t object $o&quot;
        if test &quot;z$t&quot; = zcommit
        then
                echo &quot;The commit was authored by $n $e
at $d, and titled
    $s
Its message reads as:
&quot;
                echo &quot;$b&quot; | sed -e &quot;s/^/ /&quot;
                echo
        fi
'
eval=`git for-each-ref --shell --format=&quot;$fmt&quot; \
        --sort='*objecttype' \
        --sort=-taggerdate \
        refs/tags`
eval &quot;$eval&quot;
</code></pre>
 </dd></dl>
<p> An example to show the usage of %(if)...%(then)...%(else)...%(end). This prefixes the current branch with a star. </p>
<dl>
<dd> <pre><code>git for-each-ref --format=&quot;%(if)%(HEAD)%(then)* %(else) %(end)%(refname:short)&quot; refs/heads/
</code></pre>
 </dd></dl>
<p> An example to show the usage of %(if)...%(then)...%(end). This prints the authorname, if present. </p>
<dl>
<dd> <pre><code>git for-each-ref --format=&quot;%(refname)%(if)%(authorname)%(then) Authored by: %(authorname)%(end)&quot;
</code></pre>
 </dd></dl>
<h2>CAVEATS</h2>
<p> Note that the sizes of objects on disk are reported accurately, but care should be taken in drawing conclusions about which refs or objects are responsible for disk usage. The size of a packed non-delta object may be much larger than the size of objects which delta against it, but the choice of which object is the base and which is the delta is arbitrary and is subject to change during a repack. </p>
<p> Note also that multiple copies of an object may be present in the object database; in this case, it is undefined which copy&#8217;s size or delta base will be reported.  </p>
<h2>NOTES</h2>
<p> When combining multiple <code>--contains</code> and <code>--no-contains</code> filters, only references that contain at least one of the <code>--contains</code> commits and contain none of the <code>--no-contains</code> commits are shown. </p>
<p> When combining multiple <code>--merged</code> and <code>--no-merged</code> filters, only references that are reachable from at least one of the <code>--merged</code> commits and from none of the <code>--no-merged</code> commits are shown.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-show-ref/">git-show-ref</a></code>(1)  </p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
