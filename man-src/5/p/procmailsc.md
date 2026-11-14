---
title: "procmailsc(5)"
name: "procmailsc"
section: "5"
letter: "p"
url: "/docs/linux/man/5-procmailsc/"
description: "procmailsc – procmail weighted scoring technique"
---

<p>procmailsc &#8211; procmail weighted scoring technique</p>
<h2>Synopsis</h2>
<p>[<code>*</code>] <code>w^x condition</code></p>
<h2>Description</h2>
<p>In addition to the traditional true or false conditions you can specify on a recipe, you can use a weighted scoring technique to decide if a certain recipe matches or not. When weighted scoring is used in a recipe, then the final score for that recipe must be positive for it to match. A certain condition can contribute to the score if you allocate it a `weight&#8217; (<code>w</code>) and an `exponent&#8217; (<code>x</code>). You do this by preceding the condition (on the same line) with: </p>
<pre><dl><dt><dd><code>w^x</code>
</dl></pre>
<p>Whereas both <code>w</code> and <code>x</code> are real numbers between -2147483647.0 and 2147483647.0 inclusive. </p>
<h2>Weighted regular expression conditions</h2>
<p>The first time the regular expression is found, it will add <i>w</i> to the score. The second time it is found, <i>w*x</i> will be added. The third time it is found, <i>w*x*x</i> will be added. The fourth time <i>w*x*x*x</i> will be added. And so forth. </p>
<p> This can be described by the following concise formula: </p>
<pre><dl><dt><dd>n
 n k-1 x - 1
w * Sum x = w * -------
 k=1 x - 1
</dl></pre>
<p>It represents the total added score for this condition if <code>n</code> matches are found. </p>
<p> Note that the following case distinctions can be made:<br />
 Tp 8 x=0 Only the first match will contribute w to the score. Any subsequent matches are ignored.<br />
 Tp x=1 Every match will contribute the same w to the score. The score grows linearly with the number of matches found.<br />
 Tp 0&lt;x&lt;1 Every match will contribute less to the score than the previous one. The score will asymptotically approach a certain value (see the <code>NOTES</code> section below).<br />
 Tp 1&lt;x Every match will contribute more to the score than the previous one. The score will grow exponentially.<br />
 Tp x&lt;0 Can be utilised to favour odd or even number of matches. </p>
<p> If the regular expression is negated (i.e., matches if it isn&#8217;t found), then <code>n</code> obviously can either be zero or one.</p>
<h2>Weighted program conditions</h2>
<p>If the program returns an exitcode of EXIT_SUCCESS (=0), then the total added score will be <code>w</code>. If it returns any other exitcode (indicating failure), the total added score will be <code>x</code>. </p>
<p> If the exitcode of the program is negated, then, the exitcode will be considered as if it were a virtual number of matches. Calculation of the added score then proceeds as if it had been a normal regular expression with <code>n=`exitcode&#8217;</code> matches.</p>
<h2>Weighted length conditions</h2>
<p>If the length of the actual mail is <code>M</code> then: </p>
<pre><dl><dt><dd>* w^x &gt; L
</dl></pre>
<p>will generate an additional score of: </p>
<pre><dl><dt><dd>x
 / M \
w * | --- |
 \ L /
</dl></pre>
<p>And: </p>
<pre><dl><dt><dd>* w^x &lt; L
</dl></pre>
<p>will generate an additional score of: </p>
<pre><dl><dt><dd>x
 / L \
w * | --- |
 \ M /
</dl></pre>
<p>In both cases, if L=M, this will add w to the score. In the former case however, larger mails will be favoured, in the latter case, smaller mails will be favoured. Although x can be varied to fine-tune the steepness of the function, typical usage sets x=1.</p>
<h2>Miscellaneous</h2>
<p>You can query the final score of all the conditions on a recipe from the environment variable <code>$=</code>. This variable is set <i>every</i> time just after procmail has parsed all conditions on a recipe (even if the recipe is not being executed).</p>
<h2>Examples</h2>
<p>The following recipe will ditch all mails having more than 150 lines in the body. The first condition contains an empty regular expression which, because it always matches, is used to give our score a negative offset. The second condition then matches every line in the mail, and consumes up the previous negative offset we gave (one point per line). In the end, the score will only be positive if the mail contained more than 150 lines. </p>
<pre><dl><dt><dd>:0 Bh
* -150^0
* 1^1 ^.*$
/dev/null
</dl></pre>
<p>Suppose you have a priority folder which you always read first. The next recipe picks out the priority mail and files them in this special folder. The first condition is a regular one, i.e., it doesn&#8217;t contribute to the score, but simply has to be satisfied. The other conditions describe things like: john and claire usually have something important to say, meetings are usually important, replies are favoured a bit, mails about Elvis (this is merely an example :-) are favoured (the more he is mentioned, the more the mail is favoured, but the maximum extra score due to Elvis will be 4000, no matter how often he is mentioned), lots of quoted lines are disliked, smileys are appreciated (the score for those will reach a maximum of 3500), those three people usually don&#8217;t send interesting mails, the mails should preferably be small (e.g., 2000 bytes long mails will score -100, 4000 bytes long mails do -800). As you see, if some of the uninteresting people send mail, then the mail still has a chance of landing in the priority folder, e.g., if it is about a meeting, or if it contains at least two smileys. </p>
<pre><dl><dt><dd>:0 HB
* !^Precedence:.*(junk|bulk)
* 2000^0 ^From:.*(john [at] home|claire [at] work)
* 2000^0 ^Subject:.*meeting
* 300^0 ^Subject:.*Re:
* 1000^.75 elvis|presley
* -100^1 ^&gt;
* 350^.9 :-\)
* -500^0 ^From:.*(boss|jane|henry)@work
* -100^3 &gt; 2000
priority_folder
</dl></pre>
<p>If you are subscribed to a mailinglist, and just would like to read the quality mails, then the following recipes could do the trick. First we make sure that the mail is coming from the mailinglist. Then we check if it is from certain persons of whom we value the opinion, or about a subject we absolutely want to know everything about. If it is, file it. Otherwise, check if the ratio of quoted lines to original lines is at most 1:2. If it exceeds that, ditch the mail. Everything that survived the previous test, is filed. </p>
<pre><dl><dt><dd>:0
^From mailinglist-request [at] some.where
{
 :0:
 * ^(From:.*(paula|bill)|Subject:.*skiing)
 mailinglist
 :0 Bh
 * 20^1 ^&gt;
 * -10^1 ^[^&gt;]
 /dev/null
 :0:
 mailinglist
}
</dl></pre>
<p>For further examples you should look in the <code><a href="/docs/linux/man/5-procmailex/">procmailex</a></code>(5) man page.</p>
<h2>Caveats</h2>
<p>Because this speeds up the search by an order of magnitude, the procmail internal egrep will always search for the leftmost <i>shortest</i> match, unless it is determining what to assign to <code>MATCH</code>, in which case it searches the leftmost <i>longest</i> match. E.g. for the leftmost <i>shortest</i> match, by itself, the regular expression:<br />
 Tp <code>.*</code> will always match a zero length string at the same spot.<br />
 Tp <code>.+</code> will always match one character (except newlines of course).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-procmail/">procmail</a></code>(1), <code><a href="/docs/linux/man/5-procmailrc/">procmailrc</a></code>(5), <code><a href="/docs/linux/man/5-procmailex/">procmailex</a></code>(5), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1),</p>
<h2>Bugs</h2>
<p>If, in a length condition, you specify an <code>x</code> that causes an overflow, procmail is at the mercy of the <code><a href="/docs/linux/man/3-pow/">pow</a></code>(3) function in your mathematical library. </p>
<p> Floating point numbers in `engineering&#8217; format (e.g., 12e5) are not accepted.</p>
<h2>Miscellaneous</h2>
<p>As soon as `plus infinity&#8217; (2147483647) is reached, any subsequent <i>weighted</i> conditions will simply be skipped. </p>
<p> As soon as `minus infinity&#8217; (-2147483647) is reached, the condition will be considered as `no match&#8217; and the recipe will terminate early.</p>
<h2>Notes</h2>
<p>If in a regular expression weighted formula <code>0&lt;x&lt;1</code>, the total added score for this condition will asymptotically approach: </p>
<pre><dl><dt><dd>w
-------
 1 - x
</dl></pre>
<p>In order to reach half the maximum value you need </p>
<pre><dl><dt><dd>- ln 2
n = --------
 ln x
</dl></pre>
<p>matches.</p>
<h2>Authors</h2>
<p>Stephen R. van den Berg </p>
<pre><dl><dt><dd>&lt;srb [at] cuci.nl&gt;
</dl></pre>
<p>Philip A. Guenther </p>
<pre><dl><dt><dd>&lt;guenther [at] sendmail.com&gt;
</dl></pre>
