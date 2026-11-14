---
title: "tv_imdb(1)"
name: "tv_imdb"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tv_imdb/"
description: "tv_imdb – Augment XMLTV listings files with imdb.com data."
---

<h2 class="name">NAME</h2>
<p> tv_imdb &#8211; Augment XMLTV listings files with imdb.com data. </p>
<h2>SYNOPSIS</h2>
<p> tv_imdb &#8211;imdbdir &lt;dir&gt; [&#8211;help] [&#8211;quiet] [&#8211;download]<br />
&nbsp;<wbr>[&#8211;prepStage&nbsp;<wbr>(1-9,all)] </p>
<p> tv_imdb &#8211;imdbdir &lt;dir&gt; [&#8211;help] [&#8211;quiet]<br />
&nbsp;<wbr>[&#8211;with-keywords]&nbsp;<wbr>[&#8211;with-plot]<br />
&nbsp;<wbr>[&#8211;movies-only]&nbsp;<wbr>[&#8211;stats]&nbsp;<wbr>[&#8211;debug]<br />
&nbsp;<wbr>[&#8211;output&nbsp;<wbr><font SIZE="-1">FILE</font>]&nbsp;<wbr>[<font SIZE="-1">FILE&#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> Very similar to tv_cat in semantics (see tv_cat), except whenever a programme appears with &#8220;date&#8221; entry the title and date are used to look up extra data by using the <font SIZE="-1">XMLTV::IMDB</font> package. </p>
<p> <code>&#8211;output </code><font SIZE="-1"><code>FILE</code></font> write to <font SIZE="-1">FILE</font> rather than standard output. </p>
<p> <code>&#8211;with-keywords</code> include IDMb keywords in the output file. </p>
<p> <code>&#8211;with-plot</code> include IDMb plot summary in the output file. </p>
<p> <code>&#8211;quiet</code> disable all status messages (that normally appear on stderr). </p>
<p> <code>&#8211;download</code> try to download data files if they are missing (in &#8211;prepStage). </p>
<p> <code>&#8211;stats</code> output grab stats (stats output disabled in &#8211;quiet mode). </p>
<p> <code>&#8211;debug</code> output info from movie matching </p>
<p> <code>&#8211;movies-only</code> only augment programs that look like movie listings (4 digit &#8216;date&#8217; field). </p>
<p> All programs are checked against imdb.com data (unless &#8211;movies-only is used). </p>
<p> For the purposes of tv_imdb, an &#8220;exact&#8221; match is defined as a case insensitive match against imdb.com data (which may or may not include the transformation of &#8216;&amp;&#8217; to &#8216;and&#8217; and vice-versa. </p>
<p> If the program includes a 4 digit &#8216;date&#8217; field the following matches are attempted, with the first successful match being used: </p>
<p> <code>1.</code> an &#8220;exact&#8221; title/year match against movie titles is done </p>
<p> <code>2.</code> an &#8220;exact&#8221; title match against tv series (and tv mini series) </p>
<p> <code>3.</code> an &#8220;exact&#8221; title match against movie titles with production dates within 2 years of the &#8216;date&#8217; value. </p>
<p> Unless &#8211;movies-only is used, if the program does not include a 4 digit &#8216;date&#8217; field the following matches are attempted, the first succeeding match is used: </p>
<p> <code>1.</code> an &#8220;exact&#8221; title match against tv series (and tv mini series) </p>
<p> When a match is found in the imdb.com data the following is applied: </p>
<p> <code>1.</code> the &#8216;title&#8217; field is set to match exactly the title from the imdb.com data. This includes modification of the case to match and any transformations mentioned above. </p>
<p> <code>2.</code> if the match is a movie, the &#8216;date&#8217; field is set to imdb.com 4 digit year of production. </p>
<p> <code>3.</code> the type of match found (Movie, <font SIZE="-1">TV</font> Movie, Video Movie, <font SIZE="-1">TV</font> Series, or <font SIZE="-1">TV</font> Mini Series) is placed in the &#8216;categories&#8217; field. </p>
<p> <code>4.</code> the url to the <a rel="nofollow" href="http://www.imdb.com">www.imdb.com</a> page is added </p>
<p> <code>5.</code> the director is added if the match was a movie or if only one director is listed in the imdb.com data (because some tv series have &gt; 30 directors) </p>
<p> <code>6.</code> the top 3 billing actors are added. </p>
<p> <code>7.</code> genres added to &#8216;categories&#8217; field (current list of genres are Short, Drama, Comedy, Documentary, Animation, Adult, Action, Family, Romance, Crime, Thriller, Musical, Adventure, Western, Horror, Sci-Fi, Fantasy, Mystery, War, Film-Noir, Music </p>
<p> <code>8.</code> imdb user ratings added to &#8216;star-ratings&#8217; field. </p>
<p> <code>9.</code> imdb keywords added to &#8216;keyword&#8217; fields. </p>
<p> <code>10.</code> imdb plot summary is added.</p>
<h2>HOWTO In order to use tv_imdb, you need:</h2>
<p> <code>1.</code> choose a directory location to use for the tv_imdb database (you&#8217;ll need about 1 <font SIZE="-1">GB</font> of free space), </p>
<p> <code>2a.</code> run &#8216;tv_imdb &#8211;imdbdir &lt;dir&gt; &#8211;prepStage all &#8211;download&#8217; to download the list files from imdb.com. Or, </p>
<p> <code>2b</code> If you have a slow network connection you may prefer to omit the &#8216;&#8211;download&#8217; flag and be prompted for what you need to download by hand. See &lt;<a rel="nofollow" href="http://www.imdb.com/interfaces">http://www.imdb.com/interfaces</a>&gt; for the download sites. Then once you have the files rerun without &#8216;&#8211;download&#8217;. </p>
<p> Note: &#8216;&#8211;prepStage&#8217; sucks a bit of memeory, but you can run each prepStage separately by running &#8211;prepStage with each of the stages (see &#8211;help for details). </p>
<p> <code>3.</code> Once you have the database loaded try &#8216;cat tv.xml | tv_imdb &#8211;imdbdir &lt;dir&gt; &gt; tv1.xml&#8217;. </p>
<p> Feel free to report any problems with these steps to xmltv-devel [at] lists.sf.net.</p>
<h2>BUGS</h2>
<p> The &#8216;&#8211;prepStage&#8217; needs a lot of memory to run at a reasonable speed, over 250 megabytes with the current imdb data files. For there to be 250 megabytes free for tv_imdb, the system will need at least 512 megabytes of <font SIZE="-1">RAM. </font> Running with less can take hours (or days!) &#8211; although fortunately this stage needs to be run only once after downloading the data files. </p>
<p> Could use a &#8211;configure step just like the grabbers so you do not have to specify the &#8211;imdbdir on the command line every time. Also this could step you through the prep stages with more description of what is being done and what is required. Configure could also control the number of actors to add (since some movies have an awful lot), currently we are adding the top 3. </p>
<p> How and what to look up needs to be option driven. </p>
<p> Needs some more controls for fine tuning &#8220;close&#8221; matches. For instance, currently it looks like the North America grabber only has date entries for movies, but the imdb.com data contains made for video movies as well as as real movies, ot is it&#8217;s possible to get the wrong data to be inserted. In this case we may want to say &#8220;ignore tv series&#8221; and &#8220;ignore tv mini series&#8221;. Along with this, we&#8217;d want to define what a &#8220;close&#8221; match is. For instance does a movie by the same title with a date out by 1 year or 2 years considered a match (currently we&#8217;re using 2). </p>
<p> Nice to haves include: verification/addition of programe <font SIZE="-1">MPAA/VCHIP</font> ratings, addition of imdb.com user ratings (by votes) to programes. Potenially we could expand to include &#8220;country of origin&#8221;, &#8220;description&#8221;, &#8220;writer&#8221; and &#8220;producer&#8221; credits, maybe even &#8220;commentator&#8221;. </p>
<p> Heh, if the <font SIZE="-1">XMLTV</font>.dtd supported it, we could even include urls to head shots of the actors :)</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-xmltv/">xmltv</a></i>(5)</p>
<h2>AUTHOR</h2>
<p> Jerry Veldhuis, jerry [at] matilda.com </p>
<h2>Index</h2>
